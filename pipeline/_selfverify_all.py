"""_selfverify_all.py — 全 NPC 翻譯 pre-flight 檢查

用途:build/package 之後、遊戲測試之前執行,把 90% 的 crash 前兆
     直接在命令列擋下來,不用開遊戲。

檢查層次(每個 NPC):
  Phase A: JSON 靜態檢查       — 只要有 JSON 就跑(不需 build)
  Phase B: 引擎 sim             — 需要 packaged addon 內有該 NPC 字型
  Phase C: kerndat 完整性      — 需要 shadow content 已 build
  Phase D: game.log crash 掃描 — 需要 install/game.log(僅整體一次)

每 NPC 判定:
  GREEN  — 通過
  YELLOW — 警告(接近寬度上限、常見危險 pattern),不會 crash
  RED    — 幾乎確定 crash(sim 判定死結、缺字型 glyph 過多)
  SKIP   — 尚未翻譯或資料不足(NOT_STARTED)

Exit code:
  0 = 全 GREEN / SKIP
  1 = 有 RED
  2 = --strict 且有 YELLOW
  3 = 缺 packaged addon glyph → sim 不可信,重 build+package 再跑

用法:
  python _selfverify_all.py                    # 全部
  python _selfverify_all.py --npc slylandro    # 只跑一個
  python _selfverify_all.py --strict           # YELLOW 也 fail
  python _selfverify_all.py --no-log           # 跳過 game.log 掃描
  python _selfverify_all.py --verbose          # 印出每筆詳情
"""
from __future__ import annotations
import argparse
import io
import json
import re
import string
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image

# 復用 dashboard 的種族靜態資料
try:
    import _dashboard as dash
except ImportError:
    print("[ERROR] 找不到 _dashboard.py,請在 uqm-work/ 底下執行", file=sys.stderr)
    sys.exit(3)

ROOT = Path(__file__).resolve().parent
ADDON_PATH = ROOT / "install" / "content" / "addons" / "zh-TW.uqm"
SHADOW_ROOT = ROOT / "zh-TW-addon" / "content" / "base"
GAME_LOG = ROOT / "install" / "game.log"

# ---------------------------------------------------------------------------
# AlienTextWidth 數值(SD 模式;由 units.h + comm.h + <race>c.c 計算)
#   CanvasWidth (SD)  = 320
#   STATUS_WIDTH      = 64
#   SAFE_X (SD)       = 0
#   SPACE_WIDTH       = 320 - 64 = 256
#   SIS_SCREEN_WIDTH  = 256 - 14 = 242
#   TEXT_X_OFFS       = 1
#   SIS_TEXT_WIDTH    = 242 - 2 = 240
# ---------------------------------------------------------------------------
SIS_TEXT_WIDTH_SD = 240

WIDTH_PX = {
    "FULL":       SIS_TEXT_WIDTH_SD,                # 240
    "STD":        SIS_TEXT_WIDTH_SD - 16,           # 224
    "TWO_THIRDS": ((SIS_TEXT_WIDTH_SD - 16) * 2) // 3,  # 149
    "HALF":       (SIS_TEXT_WIDTH_SD - 16) >> 1,    # 112
    "FIXED143":   143,
}

# 引擎額外會加上的 "..." lead/trail 開銷(用來抓「本頁 fit 但下一頁加 ... 就爆」)
ELLIPSIS_OVERHEAD_PX = 20

# 保險緩衝(避免邊界偽陰性)
SAFETY_MARGIN_PX = 5

# Phase A 靜態警告的 CJK 連字閾值。
# 計算依據:CJK glyph 約 15-17px + CharSpace 2px,
# 扣除 ellipsis overhead 20px + safety 5px,得到「單 run 才會撞牆」的字數。
# 這只是 heuristic —— 只在 sim 無法跑(字型不在 addon)時才作為 YELLOW 警告,
# 若 sim 跑過就抑制(sim 是權威)。
CJK_RUN_THRESHOLD = {
    "FULL":       14,   # ~240px / 17 + margin
    "STD":        12,   # ~224px
    "FIXED143":   9,    # 143px commander/starbase 專用
    "TWO_THIRDS": 8,    # ~149px
    "HALF":       6,    # ~112px
}

# ---------------------------------------------------------------------------
# 掃描 game.log 用的 crash pattern
# ---------------------------------------------------------------------------
LOG_PATTERNS_FATAL = [
    (re.compile(r"blocking on 'DCQ'", re.IGNORECASE), "renderer 死結 — 多半是 _count_lines 無限迴圈"),
    (re.compile(r"undefined resource", re.IGNORECASE), "資源 key 未定義 — 可能 RMP 或 shadow 路徑錯誤"),
    (re.compile(r"fatal error", re.IGNORECASE), "引擎回報 fatal"),
    (re.compile(r"cannot open|couldn'?t open", re.IGNORECASE), "檔案開啟失敗"),
]
LOG_PATTERNS_WARN = [
    (re.compile(r"could not find|not found", re.IGNORECASE), "找不到資源"),
    (re.compile(r"warning:", re.IGNORECASE), "engine warning"),
    (re.compile(r"missing", re.IGNORECASE), "missing 訊息"),
]

# ---------------------------------------------------------------------------
# 判定等級
# ---------------------------------------------------------------------------
LVL_GREEN = "GREEN"
LVL_YELLOW = "YELLOW"
LVL_RED = "RED"
LVL_SKIP = "SKIP"

# 顏色順序(用來 aggregate 最壞值)
LVL_RANK = {LVL_SKIP: -1, LVL_GREEN: 0, LVL_YELLOW: 1, LVL_RED: 2}


@dataclass
class Finding:
    phase: str        # "A/JSON" "B/SIM" "C/FONT" "D/LOG"
    level: str        # GREEN / YELLOW / RED
    tag: str          # 簡短 token(供 grep)
    detail: str       # 人類可讀


@dataclass
class NpcResult:
    race: str
    status: str       # dashboard 的 status
    max_width_px: int
    findings: list = field(default_factory=list)

    @property
    def level(self) -> str:
        if not self.findings:
            return LVL_SKIP if self.status == dash.STATUS_NOT_STARTED else LVL_GREEN
        return max((f.level for f in self.findings), key=lambda l: LVL_RANK[l])


# ===========================================================================
# 字型 glyph 寬度快取(從 packaged addon 讀取)
# ===========================================================================
class FontMetrics:
    """從 zh-TW.uqm 讀取指定字型的 glyph 寬度與 CharSpace。"""

    def __init__(self, font_file: str, zip_path: Path):
        self.font_file = font_file
        self.widths: dict[int, int] = {}
        self.char_space: int = 1
        self.font_available: bool = False
        self.missing_chars: set[str] = set()
        self._load(zip_path)

    def _load(self, zip_path: Path):
        if not zip_path.is_file():
            return
        prefix = f"{self.font_file}/"
        try:
            with zipfile.ZipFile(zip_path, "r") as zf:
                # 抓 kerndat.fnt
                kern_hits = [n for n in zf.namelist() if n.endswith(f"/{self.font_file}/kerndat.fnt")]
                if not kern_hits:
                    return
                self.font_available = True
                kern_data = zf.read(kern_hits[0]).decode("ascii", errors="replace")
                first_line = kern_data.splitlines()[0] if kern_data else ""
                # 格式: "<name> <Leading> <CharSpace> <KernAmount> <VertAlign>"
                parts = first_line.split()
                if len(parts) >= 3 and parts[2].isdigit():
                    self.char_space = int(parts[2])

                # 抓所有 glyph png(檔名 = 五位十六進位碼點)
                for name in zf.namelist():
                    m = re.search(rf"/{re.escape(self.font_file)}/([0-9a-fA-F]+)\.png$", name)
                    if not m:
                        continue
                    try:
                        cp = int(m.group(1), 16)
                        w = Image.open(io.BytesIO(zf.read(name))).size[0]
                        self.widths[cp] = w
                    except Exception:
                        pass
        except zipfile.BadZipFile:
            pass

    def width(self, ch: str) -> int:
        cp = ord(ch)
        if cp in self.widths:
            return self.widths[cp]
        # ASCII 沒有 glyph 通常是引擎 fallback,給保守估計
        self.missing_chars.add(ch)
        return 8

    def text_rect_width(self, s: str) -> int:
        if not s:
            return 0
        total = sum(self.width(c) + self.char_space for c in s)
        return max(0, total - self.char_space)


# ===========================================================================
# Phase A: JSON 靜態 pattern 檢查
# ===========================================================================
LUA_TEMPLATE_RE = re.compile(r"<%.*?%>")
CJK_RE = re.compile(r"[\u3400-\u9FFF\uF900-\uFAFF]")

def is_cjk_char(ch: str) -> bool:
    return bool(CJK_RE.match(ch))


def phase_a_check_json(
    npc: dash.NpcInfo,
    findings: list[Finding],
    sim_will_run: bool = False,
):
    """靜態掃描 JSON 內容,找已知危險 pattern。不需要 build。

    sim_will_run: 若 True,表示 Phase B 會用真實 glyph 寬度跑 sim。此時
        Phase A 的啟發式 LONG_CJK_RUN / LEAD_ELLIPSIS_HEAVY 只是雜訊,
        會被降級為只在 --verbose 模式下顯示的 GREEN(不影響總判定)。
    """
    heuristic_level = LVL_GREEN if sim_will_run else LVL_YELLOW

    json_path = ROOT / npc.json_path
    if not json_path.is_file():
        return
    try:
        data = json.loads(json_path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError as e:
        findings.append(Finding("A/JSON", LVL_RED, "JSON_INVALID",
                                f"JSON 無法解析: {e}"))
        return
    if not isinstance(data, dict):
        findings.append(Finding("A/JSON", LVL_RED, "JSON_NOT_DICT",
                                f"JSON 頂層必須是物件,實際為 {type(data).__name__}"))
        return

    # 依 NPC 寬度類別選啟發式閾值(見檔頂 CJK_RUN_THRESHOLD 註解)
    threshold = CJK_RUN_THRESHOLD.get(npc.width_kind, 12)

    # 靜態 pattern 檢查
    for tok, val in data.items():
        if tok.startswith("_"):  # meta 欄位
            continue
        if not isinstance(val, str) or not val.strip():
            continue

        # 替換 Lua 模板成保守長字串(SIS_CAPTAIN_NAME_MAX = 15)
        # patch 006: 用 CJK 字元 (星) 而非 ASCII X,模擬實際遊戲中
        # template 展開為中文星名/艦長名,確保 wrap point 正確。
        text = LUA_TEMPLATE_RE.sub("星" * 15, val)

        for lineno, line in enumerate(text.split("\n"), 1):
            if not line.strip():
                continue

            # (1) 連續 CJK 字元過多 → 沒空格切點,可能 wrap 失敗
            run = 0
            max_run = 0
            for ch in line:
                if is_cjk_char(ch):
                    run += 1
                    max_run = max(max_run, run)
                else:
                    run = 0
            if max_run >= threshold:
                findings.append(Finding(
                    "A/JSON", heuristic_level, "LONG_CJK_RUN",
                    f"{tok} 第{lineno}行連續 {max_run} 個 CJK 無空格 "
                    f"(寬度類 {npc.width_kind} 建議 <{threshold}): {line[:40]}"
                ))

            # (2) 行尾 CJK 標點 → SplitSubPages 會加 "..."(交給 sim 判斷)

            # (3) 行首 lead ellipsis + 稍長 word → 常見的 close-to-edge
            #     lead-ellipsis 已吃 ~20px,連字閾值減 3 才觸發
            lead_thresh = max(3, threshold - 3)
            if line.startswith("...") and max_run >= lead_thresh:
                findings.append(Finding(
                    "A/JSON", heuristic_level, "LEAD_ELLIPSIS_HEAVY",
                    f"{tok} 第{lineno}行 lead '...' 後接 {max_run}+ CJK,可能超寬"
                ))


# ===========================================================================
# Phase B: 引擎 sim(1:1 移植自 _simulate_count_lines.py,勿改動邏輯)
# ===========================================================================

def _get_line_within_width(fm: FontMetrics, text: str, max_width: int, max_chars: int):
    """1:1 對應 comm.c getLineWithinWidth() 含 patch 006 的 CJK-as-word-boundary
    邏輯 (每個 U+4E00–U+9FFF 字元本身就是一個 wrap point,不需 ASCII 空格分隔)。
    回傳 (char_count, next_ptr, eol_bool)。
    """
    ptr = 0
    char_count = 0
    old_count = 1
    eol = False
    while True:
        word_start = ptr
        ch_is_cjk_break = False
        # 掃一個 word
        while True:
            if ptr >= len(text) or text[ptr] == "\0":
                eol = True
                done = True
                break
            ch = text[ptr]
            ptr += 1
            eol = ch in ("\0", "\n", "\r")
            done = eol or char_count >= max_chars
            if done or ch == " ":
                ch_is_cjk_break = False
                break
            char_count += 1
            # patch 006: CJK 字元本身即為 word 邊界,累加後立即斷 word
            if 0x4E00 <= ord(ch) <= 0x9FFF:
                ch_is_cjk_break = True
                break

        text_slice = text[:char_count]
        rect_w = fm.text_rect_width(text_slice)

        if rect_w >= max_width:
            # 退到上一個 word 邊界
            return old_count, word_start, False
        if done:
            return char_count, ptr, eol

        # 塞得下且未結束 → 繼續下一個 word
        old_count = char_count
        # patch 006: 只有 ASCII 空格邊界需要累加分隔符;CJK 邊界不佔 char
        if not ch_is_cjk_break:
            char_count += 1  # 給剛剛跳過的 space


def _count_lines(fm: FontMetrics, page_text: str, max_width: int) -> tuple[str, int]:
    """1:1 對應 comm.c _count_lines()。回傳 (verdict, num_lines)。
    verdict: OK / INFINITE_LOOP / RUNAWAY
    """
    text = page_text
    ptr = 0
    num_lines = 0
    seen: set[int] = set()
    for _ in range(200):
        num_lines += 1
        if ptr in seen:
            # 回到同一位置 = 引擎會 do-while 死迴圈
            return "INFINITE_LOOP", num_lines
        seen.add(ptr)
        remaining = text[ptr:]
        if not remaining:
            return "OK", num_lines
        _cc, next_offset, eol = _get_line_within_width(
            fm, remaining, max_width, (1 << 16) - 1
        )
        if eol:
            return "OK", num_lines
        ptr = ptr + next_offset
    return "RUNAWAY", num_lines


def _split_sub_pages(block_text: str) -> list[str]:
    """複製 SplitSubPages():非 ASCII 標點結尾 → 加 '...' lead/trail。"""
    ascii_punct = set(string.punctuation + string.whitespace)
    pages = []
    lines = [l for l in block_text.split("\n") if l.strip()]
    for i, line in enumerate(lines):
        is_last = (i == len(lines) - 1)
        last_char = line[-1] if line else ""
        aft = 0
        if not is_last and last_char and (ord(last_char) > 0x7F or last_char not in ascii_punct):
            aft = 3
        lead = 3 if i > 0 and pages and pages[-1].endswith("...") else 0
        pages.append(("." * lead) + line + ("." * aft))
    return pages


def phase_b_sim(npc: dash.NpcInfo, fm: FontMetrics, findings: list[Finding]):
    """對 JSON 內容跑逐頁 sim。需字型可用。"""
    if not fm.font_available:
        findings.append(Finding(
            "B/SIM", LVL_YELLOW, "FONT_NOT_IN_ADDON",
            f"packaged addon 內無 {fm.font_file},sim 跳過(需要 shadow 該字型後重打包)"
        ))
        return
    if npc.width_kind not in WIDTH_PX:
        findings.append(Finding(
            "B/SIM", LVL_YELLOW, "UNKNOWN_WIDTH_KIND",
            f"寬度類別 {npc.width_kind} 未知,無法 sim"
        ))
        return

    max_width = WIDTH_PX[npc.width_kind]
    json_path = ROOT / npc.json_path
    if not json_path.is_file():
        return
    try:
        data = json.loads(json_path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return  # A phase 已回報

    total_pages = 0
    bad_pages = 0
    warn_pages = 0
    for tok, val in data.items():
        if tok.startswith("_") or not isinstance(val, str) or not val.strip():
            continue
        # 只 sim NPC subtitle(commonly大寫 token);玩家回應(通常首字小寫)沒有 _count_lines
        if tok and tok[0].islower():
            continue
        # patch 006: template 展開後含 CJK,用「星」模擬 (15 chars 保守上限)
        text = LUA_TEMPLATE_RE.sub("星" * 15, val)

        for pnum, page in enumerate(_split_sub_pages(text)):
            total_pages += 1
            verdict, n_lines = _count_lines(fm, page, max_width)
            if verdict != "OK":
                bad_pages += 1
                findings.append(Finding(
                    "B/SIM", LVL_RED, "COUNT_LINES_LOOP",
                    f"{tok}[page {pnum}] → {verdict}(引擎會死結)  文本: {page[:40]!r}"
                ))
            # patch 006 後,verdict=OK 即代表遊戲能正確 wrap
            # (原 NEAR_EDGE 啟發式已冗餘 — 只有純 ASCII 且無 space 的 page
            #  才會判 single-line,但 SC2 對話幾乎全 CJK,永不觸發)

    # Missing glyph 檢查
    if fm.missing_chars:
        # 過濾:排除純 ASCII、控制字元、空格
        nontrivial = {c for c in fm.missing_chars if ord(c) > 0x7F}
        if nontrivial:
            sample = "".join(sorted(nontrivial)[:20])
            findings.append(Finding(
                "B/SIM", LVL_RED, "MISSING_GLYPHS",
                f"字型 {fm.font_file} 缺 {len(nontrivial)} 個 CJK glyph(遊戲會顯示成方塊):{sample}"
            ))


# ===========================================================================
# Phase C: kerndat.fnt 完整性
# ===========================================================================
def phase_c_check_kerndat(npc: dash.NpcInfo, findings: list[Finding]):
    """檢查 shadow content 內字型的 kerndat.fnt 第一 token 是否等於資料夾名。"""
    if not npc.font_file or npc.font_file == "?":
        return
    kern_path = SHADOW_ROOT / "fonts" / npc.font_file / "kerndat.fnt"
    if not kern_path.is_file():
        # 沒 shadow 就沒事(引擎會 fallback 到 base)
        return
    try:
        first = kern_path.read_text(encoding="ascii", errors="replace").splitlines()[0]
    except (OSError, IndexError):
        findings.append(Finding("C/FONT", LVL_RED, "KERNDAT_UNREADABLE",
                                f"{npc.font_file}/kerndat.fnt 讀不到"))
        return
    first_token = first.split(None, 1)[0] if first else ""
    if first_token != npc.font_file:
        findings.append(Finding(
            "C/FONT", LVL_RED, "KERNDAT_NAME_MISMATCH",
            f"{npc.font_file}/kerndat.fnt 第一 token '{first_token}' != 資料夾名 '{npc.font_file}' "
            f"→ 遊戲啟動該對話時會 renderer 死結(見 uqm-font-hacks.md)"
        ))


# ===========================================================================
# Phase D: game.log 掃描(全域,只跑一次)
# ===========================================================================
def phase_d_scan_log(findings_by_npc: dict[str, list[Finding]], quiet: bool):
    if not GAME_LOG.is_file():
        return
    try:
        text = GAME_LOG.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    lines = text.splitlines()

    fatal_hits: list[tuple[int, str, str]] = []
    warn_hits: list[tuple[int, str, str]] = []

    for idx, line in enumerate(lines):
        for pat, tag in LOG_PATTERNS_FATAL:
            if pat.search(line):
                fatal_hits.append((idx + 1, tag, line.rstrip()))
        for pat, tag in LOG_PATTERNS_WARN:
            if pat.search(line):
                warn_hits.append((idx + 1, tag, line.rstrip()))

    # 掛到「__log__」偽 NPC entry(統一顯示)
    log_findings: list[Finding] = []
    for lineno, tag, snippet in fatal_hits:
        log_findings.append(Finding(
            "D/LOG", LVL_RED, "LOG_FATAL",
            f"[game.log:{lineno}] {tag}  →  {snippet[:100]}"
        ))
    if quiet:
        # 只列前 3 條 warn
        warn_hits = warn_hits[:3]
    for lineno, tag, snippet in warn_hits:
        log_findings.append(Finding(
            "D/LOG", LVL_YELLOW, "LOG_WARN",
            f"[game.log:{lineno}] {tag}  →  {snippet[:100]}"
        ))
    if log_findings:
        findings_by_npc["__log__"] = log_findings


# ===========================================================================
# 主流程
# ===========================================================================
def format_finding_lines(fs: list[Finding], verbose: bool) -> list[str]:
    if not fs:
        return []
    lines = []
    # 依 level 分組;YELLOW/RED 一律顯示,GREEN 略;verbose 則全顯示
    for f in fs:
        if f.level == LVL_GREEN and not verbose:
            continue
        marker = {"RED": "!!", "YELLOW": " ~", "GREEN": " .", "SKIP": " ."}[f.level]
        lines.append(f"    {marker} [{f.phase}] {f.tag}: {f.detail}")
    return lines


LEVEL_COLOR = {
    LVL_GREEN:  "\033[32mGREEN \033[0m",
    LVL_YELLOW: "\033[33mYELLOW\033[0m",
    LVL_RED:    "\033[31mRED   \033[0m",
    LVL_SKIP:   "SKIP  ",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--npc", type=str, default="", help="只檢查單一種族")
    ap.add_argument("--strict", action="store_true", help="YELLOW 也 exit 1")
    ap.add_argument("--no-log", action="store_true", help="跳過 game.log 掃描")
    ap.add_argument("--verbose", "-v", action="store_true", help="列出所有 finding(含 GREEN 摘要)")
    ap.add_argument("--no-color", action="store_true", help="關閉 ANSI 顏色")
    args = ap.parse_args()

    if args.no_color:
        for k in LEVEL_COLOR:
            LEVEL_COLOR[k] = k.ljust(6)

    npcs = dash.scan_npcs()
    if args.npc:
        npcs = [n for n in npcs if n.race == args.npc]
        if not npcs:
            print(f"[ERROR] 找不到種族 {args.npc}", file=sys.stderr)
            return 3

    # 逐 NPC 檢查
    results: list[NpcResult] = []
    font_cache: dict[str, FontMetrics] = {}

    for npc in npcs:
        max_w = WIDTH_PX.get(npc.width_kind, 0)
        r = NpcResult(race=npc.race, status=npc.status, max_width_px=max_w)

        # NOT_STARTED 就跳過所有 phase(但仍列一筆 SKIP)
        if npc.status == dash.STATUS_NOT_STARTED:
            results.append(r)
            continue

        # 先載字型,才能知道 sim 是否會跑,再決定 phase A 的降級策略
        if npc.font_file not in font_cache:
            font_cache[npc.font_file] = FontMetrics(npc.font_file, ADDON_PATH)
        fm = font_cache[npc.font_file]
        sim_will_run = fm.font_available and npc.width_kind in WIDTH_PX

        # A: JSON 靜態檢查(sim 會跑時,啟發式警告降級為 GREEN)
        phase_a_check_json(npc, r.findings, sim_will_run=sim_will_run)

        # B: Sim(需字型 cache)
        phase_b_sim(npc, fm, r.findings)

        # C: kerndat
        phase_c_check_kerndat(npc, r.findings)

        results.append(r)

    # D: game.log(全域一次)
    log_findings_map: dict[str, list[Finding]] = {}
    if not args.no_log and not args.npc:
        phase_d_scan_log(log_findings_map, quiet=not args.verbose)

    # ========== 輸出 ==========
    print("=" * 100)
    print(" Star Control 2 zh-TW pre-flight check  ({} NPC)".format(len(results)))
    print("=" * 100)

    # NPC 逐條
    counts = {LVL_GREEN: 0, LVL_YELLOW: 0, LVL_RED: 0, LVL_SKIP: 0}
    fonts_untrusted = False
    for r in results:
        lvl = r.level
        counts[lvl] += 1
        print(f" [{LEVEL_COLOR[lvl]}] {r.race:<12} (status={r.status:<12} width={r.max_width_px:>3}px)")
        for line in format_finding_lines(r.findings, args.verbose):
            print(line)
            if "MISSING_GLYPHS" in line:
                fonts_untrusted = True

    # game.log 區塊
    if log_findings_map.get("__log__"):
        print()
        print(" [game.log] 引擎日誌訊號:")
        for line in format_finding_lines(log_findings_map["__log__"], args.verbose):
            print(line)

    print()
    print(f" 統計: RED={counts[LVL_RED]}  YELLOW={counts[LVL_YELLOW]}  "
          f"GREEN={counts[LVL_GREEN]}  SKIP={counts[LVL_SKIP]}")

    if fonts_untrusted:
        print()
        print(" ★ 警告:有 NPC 字型缺 glyph → sim 結果不完全可信")
        print("   請先 rasterize CJK 到該字型後,重新 build+package,再跑一次")
        return 3

    if counts[LVL_RED] > 0:
        return 1
    if args.strict and counts[LVL_YELLOW] > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
