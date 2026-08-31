"""_dashboard.py — Star Control 2 zh-TW NPC 翻譯進度總覽

用法:
    python _dashboard.py             # 只印到 console
    python _dashboard.py --md        # 另存 _dashboard.md
    python _dashboard.py --json      # 另存 _dashboard.json (機器用)
    python _dashboard.py --next N    # 只列出下一個建議處理的 N 個 NPC

盤點來源(相對於 uqm-work/):
    A) extracted/base/base/comm/<race>/<race>.txt      — 英文原文
    B) zh-TW-addon/content/base/comm/<race>/<race>.txt — 中文影子檔(build 產出)
    C) translations/<race>.zh-TW.json                  — JSON 翻譯字典
    D) install/content/addons/zh-TW.uqm                — 已打包 addon(內含 comm/<race>/)

每個 NPC 的狀態:
    NOT_STARTED   — 沒 JSON、沒 shadow、沒 packaged
    IN_JSON       — 有 JSON 但還沒 build
    IN_SHADOW     — 已 build 到 shadow content(但 addon 未 repackage)
    PACKAGED      — 已打包進 zh-TW.uqm(遊戲能看到)

字型與寬度資料來自 UQM-MegaMod 原始碼(2026-08-05 版) +
uqm-work/_analysis/../memories/repo/uqm-font-hacks.md
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import zipfile
from dataclasses import dataclass, field, asdict
from pathlib import Path

# ---------------------------------------------------------------------------
# 路徑常數(相對於此腳本所在資料夾 = uqm-work/)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
EN_COMM_DIR = ROOT / "extracted" / "base" / "base" / "comm"
ZH_SHADOW_COMM = ROOT / "zh-TW-addon" / "content" / "base" / "comm"
TRANSLATIONS_DIR = ROOT / "translations"
PACKAGED_ADDON = ROOT / "install" / "content" / "addons" / "zh-TW.uqm"

# ---------------------------------------------------------------------------
# 種族靜態資訊表
#   font_res    : UQM_MegaMod 引擎的 AlienFont 常數(供除錯定位用)
#   font_file   : 實際的 .fon 資料夾(即字型 key,決定 shadow redirect 對象)
#   font_native_h : 該字型原生 PNG 高度(px)
#   cjk_safe    : 該字型是否 >= 14px 高、能容納 CJK(見 uqm-font-hacks.md)
#   width_kind  : 對話文字寬度類型
#       FULL     — SIS_TEXT_WIDTH        (最寬,約 200 px SD)
#       STD      — SIS_TEXT_WIDTH - 16   (絕大多數,~ 184 px SD)
#       TWO_THIRDS — * 2 / 3             (~ 122 px SD,中等風險)
#       HALF     — >> 1                  (~ 92 px SD,高風險)
#       FIXED143 — RES_SCALE(143)        (commander 專用)
#   risk_notes  : 已知需注意的技術地雷
#
# 資料來源:
#   uqm/comm/<race>/<race>c.c 的 AlienFont / AlienTextWidth 欄位。
#   來自 grep 於 2026-08-05: UQM-MegaMod v0.8.5-branch。
# ---------------------------------------------------------------------------

# 內容資料夾名 → 對話 .c 檔案 short-key
CONTENT_TO_SRC = {
    "arilou":      "arilouc",
    "chmmr":       "chmmrc",
    "commander":   "comandr",     # 內容資料夾 vs 原始碼命名差
    "druuge":      "druugec",
    "ilwrath":     "ilwrathc",
    "kohrah":      "blackurc",    # Kohr-Ah 用 BlackUrquan 對話結構
    "melnorme":    "melnorm",
    "mycon":       "myconc",
    "orz":         "orzc",
    "pkunk":       "pkunkc",
    "probe":       "urquanc",     # Ur-Quan Probe 沿用 urquan 設定
    "robot":       "orzc",        # Orz 幻化 / robot form,假設沿用 orz
    "safeones":    "spahome",     # Spathi Safe Ones(遊戲後期)
    "shofixti":    "shofixt",
    "slylandro":   "slyhome",     # 內容目錄 slylandro/ 對應原始碼 slyhome/
    "spathi":      "spathic",
    "starbase":    "starbas",
    "supox":       "supoxc",
    "syreen":      "syreenc",
    "talkingpet":  "talkpet",
    "thraddash":   "thraddc",
    "umgah":       "umgahc",
    "urquan":      "urquanc",
    "utwig":       "utwigc",
    "vux":         "vuxc",
    "yehat":       "yehatc",
    "yehatrebels": "rebel",
    "zoqfotpik":   "zoqfotc",
}

# short-key → (font_res, font_file, font_native_h, cjk_safe, width_kind)
SRC_INFO = {
    "arilouc":  ("ARILOU_FONT",      "arilou.fon",    9,  False, "STD"),
    "blackurc": ("BLACKURQ_FONT",    "kohrah.fon",    16, True,  "STD"),
    "chmmrc":   ("CHMMR_FONT",       "chmmr.fon",     10, False, "STD"),
    "comandr":  ("COMMANDER_FONT",   "commander.fon", 9,  False, "FIXED143"),
    "druugec":  ("DRUUGE_FONT",      "druuge.fon",    11, False, "STD"),   # micro-ish
    "ilwrathc": ("ILWRATH_FONT",     "ilwrath.fon",   14, True,  "STD"),
    "melnorm":  ("MELNORME_FONT",    "melnorme.fon",  11, False, "STD"),   # micro-like
    "myconc":   ("MYCON_FONT",       "mycon.fon",     15, True,  "STD"),
    "orzc":     ("ORZ_FONT",         "orz.fon",       15, True,  "STD"),
    "pkunkc":   ("PKUNK_FONT",       "pkunk.fon",     14, True,  "STD"),
    "rebel":    ("YEHAT_FONT",       "yehat.fon",     14, True,  "TWO_THIRDS"),
    "shofixt":  ("SHOFIXTI_FONT",    "shofixti.fon",  16, True,  "FULL"),
    "slyhome":  ("SLYLANDRO_FONT",   "slylandro.fon", 14, True,  "FULL"),
    "slyland":  ("SLYLAND_FONT",     "slyland.fon",   10, False, "STD"),   # 星際遊牧 Slylandro
    "spahome":  ("SPATHI_FONT",      "spathi.fon",    15, True,  "STD"),
    "spathic":  ("SPATHI_FONT",      "spathi.fon",    15, True,  "STD"),
    "starbas":  ("COMMANDER_FONT",   "commander.fon", 9,  False, "FULL"),
    "supoxc":   ("SUPOX_FONT",       "supox.fon",     11, False, "STD"),
    "syreenc":  ("SYREEN_FONT",      "syreen.fon",    17, True,  "STD"),
    "talkpet":  ("TALKING_PET_FONT", "talkpet.fon",   14, True,  "STD"),   # 假定
    "thraddc":  ("THRADD_FONT",      "thraddash.fon", 12, False, "STD"),
    "umgahc":   ("UMGAH_FONT",       "umgah.fon",     8,  False, "STD"),
    "urquanc":  ("URQUAN_FONT",      "urquan.fon",    16, True,  "STD"),
    "utwigc":   ("UTWIG_FONT",       "utwig.fon",     18, True,  "STD"),
    "vuxc":     ("VUX_FONT",         "vux.fon",       12, False, "HALF"),
    "yehatc":   ("YEHAT_FONT",       "yehat.fon",     14, True,  "TWO_THIRDS"),
    "zoqfotc":  ("ZOQFOTPIK_FONT",   "zoqfotpik.fon", 14, True,  "HALF"),
}

WIDTH_LABEL_PX_SD = {   # 供人類閱讀的近似像素值(SD 模式),精確值以引擎為準
    "FULL":       "≈200",
    "STD":        "≈184",
    "TWO_THIRDS": "≈122",
    "HALF":       "≈92 ",
    "FIXED143":   "143 ",
}

WIDTH_RISK_LEVEL = {
    "FULL":       0,   # 幾乎不會爆
    "STD":        1,   # 基準
    "FIXED143":   2,   # 中低
    "TWO_THIRDS": 3,   # 中高
    "HALF":       4,   # 高(易觸發 _count_lines 死結)
}

# ---------------------------------------------------------------------------
# 資料結構
# ---------------------------------------------------------------------------
STATUS_NOT_STARTED = "NOT_STARTED"
STATUS_IN_JSON     = "IN_JSON"
STATUS_IN_SHADOW   = "IN_SHADOW"
STATUS_PACKAGED    = "PACKAGED"

STATUS_ORDER = {
    STATUS_PACKAGED:    3,
    STATUS_IN_SHADOW:   2,
    STATUS_IN_JSON:     1,
    STATUS_NOT_STARTED: 0,
}


@dataclass
class NpcInfo:
    race: str
    en_txt_path: str = ""
    en_tokens: int = 0
    json_path: str = ""
    json_tokens_translated: int = 0
    shadow_txt_path: str = ""
    shadow_exists: bool = False
    packaged: bool = False
    src_key: str = ""
    font_res: str = "?"
    font_file: str = "?"
    font_native_h: int = 0
    cjk_safe: bool = False
    width_kind: str = "?"
    width_px_sd: str = "?"
    status: str = STATUS_NOT_STARTED
    risk_score: int = 0
    risk_notes: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# 掃描函式
# ---------------------------------------------------------------------------
TOKEN_RE = re.compile(r"^#\(([^)]+)\)", re.MULTILINE)

def count_tokens_in_txt(path: Path) -> int:
    if not path.is_file():
        return 0
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    # 唯一 token 數(#(FOO) 若重複只算一次)
    return len(set(TOKEN_RE.findall(text)))


def count_translated_in_json(path: Path) -> int:
    if not path.is_file():
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return 0
    if not isinstance(data, dict):
        return 0
    # 只算「有實際翻譯內容」的 key,空字串不算
    return sum(1 for v in data.values() if isinstance(v, str) and v.strip())


def get_packaged_races(zip_path: Path) -> set[str]:
    """回傳 zh-TW.uqm 內含有 comm/<race>/<race>.txt 的 race 集合。"""
    if not zip_path.is_file():
        return set()
    races = set()
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            for name in zf.namelist():
                m = re.search(r"(?:^|/)comm/([^/]+)/\1\.txt$", name)
                if m:
                    races.add(m.group(1))
    except zipfile.BadZipFile:
        pass
    return races


def scan_npcs() -> list[NpcInfo]:
    if not EN_COMM_DIR.is_dir():
        print(f"[ERROR] 找不到英文對話目錄: {EN_COMM_DIR}", file=sys.stderr)
        print("        請先跑 build_zh-TW.ps1 或確認 extracted/ 已解壓 base pack", file=sys.stderr)
        sys.exit(1)

    packaged = get_packaged_races(PACKAGED_ADDON)

    npcs: list[NpcInfo] = []
    for race_dir in sorted(EN_COMM_DIR.iterdir()):
        if not race_dir.is_dir():
            continue
        race = race_dir.name
        en_txt = race_dir / f"{race}.txt"
        if not en_txt.is_file():
            # 不是所有種族目錄都是有 .txt 的(過濾非對話目錄)
            continue

        info = NpcInfo(race=race, en_txt_path=str(en_txt.relative_to(ROOT)))
        info.en_tokens = count_tokens_in_txt(en_txt)

        # JSON 翻譯字典(檔名慣例:<race>.zh-TW.json)
        json_path = TRANSLATIONS_DIR / f"{race}.zh-TW.json"
        info.json_path = str(json_path.relative_to(ROOT))
        info.json_tokens_translated = count_translated_in_json(json_path)

        # Shadow content 是否已 build
        shadow_txt = ZH_SHADOW_COMM / race / f"{race}.txt"
        info.shadow_txt_path = str(shadow_txt.relative_to(ROOT))
        info.shadow_exists = shadow_txt.is_file()

        # 是否已打包
        info.packaged = race in packaged

        # 種族技術資訊
        src_key = CONTENT_TO_SRC.get(race, "")
        info.src_key = src_key
        if src_key in SRC_INFO:
            fres, ffile, fh, safe, wkind = SRC_INFO[src_key]
            info.font_res = fres
            info.font_file = ffile
            info.font_native_h = fh
            info.cjk_safe = safe
            info.width_kind = wkind
            info.width_px_sd = WIDTH_LABEL_PX_SD.get(wkind, "?")

        # 決定狀態
        if info.packaged:
            info.status = STATUS_PACKAGED
        elif info.shadow_exists:
            info.status = STATUS_IN_SHADOW
        elif info.json_tokens_translated > 0:
            info.status = STATUS_IN_JSON
        else:
            info.status = STATUS_NOT_STARTED

        # 風險評估
        risk = WIDTH_RISK_LEVEL.get(info.width_kind, 1)
        if not info.cjk_safe:
            risk += 2
            info.risk_notes.append(
                f"字型 {info.font_file} 原生 {info.font_native_h}px < 14px,需要 shadow redirect"
            )
        if info.width_kind == "HALF":
            info.risk_notes.append("寬度僅一半,CJK 極易觸發 _count_lines 死結")
        elif info.width_kind == "TWO_THIRDS":
            info.risk_notes.append("寬度 2/3,CJK 需嚴格 space-wrap")
        elif info.width_kind == "FIXED143":
            info.risk_notes.append("commander/starbase 使用固定 143 px,已知需 space-wrap")
        if not src_key:
            risk += 1
            info.risk_notes.append("找不到原始碼對應,字型/寬度未確認")
        info.risk_score = risk

        npcs.append(info)

    return npcs


# ---------------------------------------------------------------------------
# 輸出
# ---------------------------------------------------------------------------
STATUS_SYMBOL = {
    STATUS_NOT_STARTED: "  .",
    STATUS_IN_JSON:     " J ",
    STATUS_IN_SHADOW:   " S ",
    STATUS_PACKAGED:    "PKG",
}


def format_console(npcs: list[NpcInfo], next_n: int = 0) -> str:
    lines = []
    lines.append("=" * 100)
    lines.append(" Star Control 2 zh-TW NPC 對話翻譯進度總覽")
    lines.append("=" * 100)

    total = len(npcs)
    n_packaged  = sum(1 for n in npcs if n.status == STATUS_PACKAGED)
    n_shadow    = sum(1 for n in npcs if n.status == STATUS_IN_SHADOW)
    n_json      = sum(1 for n in npcs if n.status == STATUS_IN_JSON)
    n_todo      = sum(1 for n in npcs if n.status == STATUS_NOT_STARTED)
    total_tokens = sum(n.en_tokens for n in npcs)
    translated_tokens = sum(n.json_tokens_translated for n in npcs)
    pct = 100.0 * translated_tokens / total_tokens if total_tokens else 0

    lines.append(
        f" 種族數: {total:3d}   "
        f"已打包 {n_packaged:2d}   影子 {n_shadow:2d}   "
        f"僅 JSON {n_json:2d}   未動 {n_todo:2d}"
    )
    lines.append(
        f" 對話 token 覆蓋率: {translated_tokens} / {total_tokens} ({pct:.1f}%)"
    )
    lines.append("")

    # 主表:依狀態(未動→已打包)、風險由高到低
    def sort_key(n: NpcInfo):
        return (STATUS_ORDER[n.status], -n.risk_score, n.race)

    sorted_npcs = sorted(npcs, key=sort_key)

    lines.append(
        f" {'狀態':<3}  {'種族':<12} {'EN':>4} {'zh':>4}  "
        f"{'字型':<15} {'原生':<5} {'寬度':<5} {'風險':>2}  備註"
    )
    lines.append(" " + "-" * 98)

    for n in sorted_npcs:
        cjk_mark = "★" if n.cjk_safe else "!"
        note = " / ".join(n.risk_notes) if n.risk_notes else ""
        # 截斷過長備註
        if len(note) > 40:
            note = note[:37] + "..."
        lines.append(
            f" {STATUS_SYMBOL[n.status]}  {n.race:<12} "
            f"{n.en_tokens:>4} {n.json_tokens_translated:>4}  "
            f"{n.font_file:<15} {n.font_native_h:>2}px{cjk_mark} "
            f"{n.width_px_sd:<5} {n.risk_score:>2}  {note}"
        )

    lines.append("")
    lines.append(" 圖例:")
    lines.append("   狀態  PKG=已打包 / S=已 build 到 shadow / J=僅有 JSON / .=未動")
    lines.append("   原生  ★=字型 >=14px CJK 可用 / !=太小需 shadow redirect")
    lines.append("   風險  越高越危險(字寬窄 + 字型小 + 未查證 累加)")
    lines.append("")

    # 建議下一步
    todo = [n for n in sorted_npcs if n.status == STATUS_NOT_STARTED]
    if todo:
        # 建議順序:低風險先做累積信心,再攻高風險
        low_risk_first = sorted(todo, key=lambda n: (n.risk_score, -n.en_tokens, n.race))
        lines.append(" 建議處理順序(先低風險累積戰果,最後攻高風險):")
        show = low_risk_first[: (next_n if next_n else 5)]
        for i, n in enumerate(show, 1):
            note = f"  ({'; '.join(n.risk_notes)})" if n.risk_notes else ""
            lines.append(
                f"   {i}. {n.race:<12} "
                f"{n.en_tokens:>3} tokens, 字型 {n.font_file}({n.font_native_h}px), "
                f"寬度 {n.width_kind}{note}"
            )

    return "\n".join(lines)


def format_markdown(npcs: list[NpcInfo]) -> str:
    total = len(npcs)
    n_packaged  = sum(1 for n in npcs if n.status == STATUS_PACKAGED)
    n_shadow    = sum(1 for n in npcs if n.status == STATUS_IN_SHADOW)
    n_json      = sum(1 for n in npcs if n.status == STATUS_IN_JSON)
    n_todo      = sum(1 for n in npcs if n.status == STATUS_NOT_STARTED)
    total_tokens = sum(n.en_tokens for n in npcs)
    translated_tokens = sum(n.json_tokens_translated for n in npcs)
    pct = 100.0 * translated_tokens / total_tokens if total_tokens else 0

    lines = [
        "# Star Control 2 zh-TW NPC 翻譯進度總覽",
        "",
        f"- 種族總數: **{total}**",
        f"- 已打包(PKG): {n_packaged}",
        f"- 已 build 到 shadow(S): {n_shadow}",
        f"- 僅有 JSON(J): {n_json}",
        f"- 未動(.): {n_todo}",
        f"- 對話 token 覆蓋率: **{translated_tokens} / {total_tokens} ({pct:.1f}%)**",
        "",
        "| 狀態 | 種族 | EN tokens | zh tokens | 字型檔 | 原生px | CJK 可用 | 寬度種類 | 寬度 px(SD) | 風險 | 備註 |",
        "|---|---|---:|---:|---|---:|:---:|---|---|---:|---|",
    ]
    def sort_key(n: NpcInfo):
        return (STATUS_ORDER[n.status], -n.risk_score, n.race)
    for n in sorted(npcs, key=sort_key):
        cjk_mark = "✅" if n.cjk_safe else "❌"
        note = "; ".join(n.risk_notes) if n.risk_notes else ""
        lines.append(
            f"| {STATUS_SYMBOL[n.status].strip()} | {n.race} | {n.en_tokens} | "
            f"{n.json_tokens_translated} | `{n.font_file}` | {n.font_native_h} | "
            f"{cjk_mark} | {n.width_kind} | {n.width_px_sd} | {n.risk_score} | {note} |"
        )
    lines.append("")
    lines.append("圖例:PKG = 已打包 / S = 已 build 影子 / J = 只有 JSON / . = 未動")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", action="store_true", help="另存 _dashboard.md")
    ap.add_argument("--json", action="store_true", help="另存 _dashboard.json(供腳本使用)")
    ap.add_argument("--next", type=int, default=0, help="只列出建議處理的前 N 個(0 = 預設 5 個)")
    args = ap.parse_args()

    npcs = scan_npcs()
    print(format_console(npcs, next_n=args.next))

    if args.md:
        md_path = ROOT / "_dashboard.md"
        md_path.write_text(format_markdown(npcs), encoding="utf-8")
        print(f"\n[寫出] {md_path.relative_to(ROOT)}")
    if args.json:
        json_path = ROOT / "_dashboard.json"
        json_path.write_text(
            json.dumps([asdict(n) for n in npcs], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[寫出] {json_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
