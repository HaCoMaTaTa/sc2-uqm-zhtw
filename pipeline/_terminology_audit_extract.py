"""
Terminology Audit Phase 1 · 從 StarControl2_TW_Localization/ 抽 canonical + 偵測內部衝突

Usage:
    python _terminology_audit_extract.py

Outputs:
    _terminology_master_table_2026-08-18.csv    # 完整 canonical 主表
    _terminology_audit_phase1_2026-08-18.md     # 內部衝突報告

策略：
- 掃所有 *.md 和 *.csv 檔於 StarControl2_TW_Localization/
- 從 markdown 表格 `| English | **中文** |` 提取 EN→ZH pair
- 從 CSV 檔提取 EN→ZH
- 同 EN 出現 >1 種 ZH → 標為 conflict
- 排除歷史區/廢止區 (Forbidden_Translations.md § 一, 舊譯歷史)
"""
from __future__ import annotations
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"q:\Dos_G\StarControl2\StarControl2_TW_Localization")
UQM_WORK = Path(r"q:\Dos_G\StarControl2\uqm-work")
DATE = "2026-08-18"

# ─────────────────────────────────────────────────────────
# 過濾規則
# ─────────────────────────────────────────────────────────
# 檔案：跳過歷史/範本/廢止
SKIP_DIRS = {"Reference_Material"}  # 舊譯來源、僅供參考
SKIP_FILES = {"Race_Template.md", "Character_Template.md", "Ship_Template.md"}

# 區段：這些 heading 之後的內容是「歷史/廢止/禁止」，跳過
SKIP_HEADINGS = re.compile(
    r"^\s{0,3}#+\s*(禁止譯法|Forbidden|歷史|已被|舊譯|廢止|obsolete|已廢止|禁止|Old translations|已完成|Phase\s*\d+.*完成|變更歷史)",
    re.IGNORECASE,
)

# 表頭：跳過表頭列
TABLE_HEADER = re.compile(r"^\s*\|\s*English\s*\|.*繁", re.IGNORECASE)
TABLE_SEPARATOR = re.compile(r"^\s*\|\s*[-:]+\s*\|.*[-:]")

# 提取表格列：`| EN | ZH | ...`
TABLE_ROW = re.compile(
    r"^\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*(?:\|.*)?$"
)

# 判斷 English 欄：必須含 ASCII 字母（除 Gg 特殊 case）
def is_english_like(s: str) -> bool:
    s = s.strip("* ").strip()
    if not s:
        return False
    # 允許純英文、含空格連字號句點單引號
    if re.match(r"^[A-Za-z][A-Za-z0-9 \-'.\(\)/&,!]*$", s):
        return True
    return False

# 判斷 Chinese 欄：必須含 CJK 或為特殊 marker
def is_chinese_like(s: str) -> bool:
    s = s.strip("* ").strip("`").strip()
    if not s:
        return False
    if s in ("—", "-", "N/A", "?", "待定", "待議", "待查證"):
        return False
    # 含 CJK 統一漢字
    if re.search(r"[\u4e00-\u9fff\u3400-\u4dbf]", s):
        return True
    # 保留原文的情境：`保留原文`
    if "保留" in s and "原文" in s:
        return True
    return False

# 抽取 ZH：從加粗（`**中文**`）優先，否則第一段中文字
ZH_BOLD = re.compile(r"\*\*([^*]+?)\*\*")

def extract_zh(cell: str) -> str | None:
    """從表格 cell 抽出 canonical ZH。優先 **粗體**，否則第一段連續 CJK。"""
    cell = cell.strip()
    # 先嘗試找 **粗體 CJK**
    for m in ZH_BOLD.finditer(cell):
        val = m.group(1).strip()
        if is_chinese_like(val):
            # 去掉尾部說明「（v0.4）」「（暫定）」
            val = re.sub(r"[（(].*?[)）]$", "", val).strip()
            val = re.sub(r"（\s*Ur-.*?[)）]", "", val).strip()  # 去尾註英文
            return val
    # fallback：第一段 CJK
    m = re.search(r"[\u4e00-\u9fff][\u4e00-\u9fff·\-\s／/]{0,20}", cell)
    if m:
        val = m.group(0).strip()
        if val:
            return val
    return None


def extract_en(cell: str) -> str | None:
    """從表格 cell 抽出 canonical EN。"""
    cell = cell.strip()
    # 去掉 markdown 粗體
    cell = re.sub(r"\*\*(.+?)\*\*", r"\1", cell).strip()
    # 去掉尾部說明「（Ur-Quan Hierarchy）」等括號
    cell = re.sub(r"\s*[（(].*?[)）]\s*$", "", cell).strip()
    # 若含中文則不算 EN
    if re.search(r"[\u4e00-\u9fff]", cell):
        return None
    if is_english_like(cell):
        return cell.strip()
    return None


# ─────────────────────────────────────────────────────────
# 掃描
# ─────────────────────────────────────────────────────────
# entries[EN] = list of (ZH, source_file, line_no)
entries: dict[str, list[tuple[str, str, int]]] = defaultdict(list)


def scan_markdown(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    lines = text.splitlines()
    skip_mode = False
    for i, line in enumerate(lines, 1):
        # 遇 heading 檢查是否進入「跳過區」
        if re.match(r"^\s{0,3}#+\s", line):
            skip_mode = bool(SKIP_HEADINGS.match(line))
            continue
        if skip_mode:
            continue
        # 表格列
        if TABLE_SEPARATOR.match(line):
            continue
        if TABLE_HEADER.match(line):
            continue
        m = TABLE_ROW.match(line)
        if not m:
            continue
        en_cell, zh_cell = m.group(1), m.group(2)
        en = extract_en(en_cell)
        if not en:
            continue
        zh = extract_zh(zh_cell)
        if not zh:
            continue
        # normalize
        en_key = en.strip().rstrip(".").strip()
        entries[en_key].append((zh, rel, i))


def scan_csv(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            en = (row.get("english") or "").strip()
            zh = (row.get("chinese") or "").strip()
            if not en or not zh:
                continue
            if not is_chinese_like(zh) and not is_english_like(zh):
                continue
            en_key = en.rstrip(".").strip()
            entries[en_key].append((zh, rel, i))


def scan_all() -> None:
    for path in ROOT.rglob("*.md"):
        # skip
        parts = path.relative_to(ROOT).parts
        if any(p in SKIP_DIRS for p in parts):
            continue
        if path.name in SKIP_FILES:
            continue
        scan_markdown(path)
    for path in ROOT.rglob("*.csv"):
        parts = path.relative_to(ROOT).parts
        if any(p in SKIP_DIRS for p in parts):
            continue
        scan_csv(path)


# ─────────────────────────────────────────────────────────
# 分析與輸出
# ─────────────────────────────────────────────────────────
def normalize_zh(s: str) -> str:
    """歸一化 ZH · 用於等價比對。"""
    s = s.strip()
    # 去頭尾標點
    s = s.strip("「」『』\"'*# ")
    # 去尾註「（暫定）」等
    s = re.sub(r"[（(](暫定|待議|待決|obsolete|舊|廢止|已廢)[^)）]*[)）]$", "", s).strip()
    # 「烏寬克澤札」與「烏寬・克澤札」等價（去中黑點）
    s = s.replace("·", "").replace("・", "").replace("‧", "").replace("．", "")
    return s


def summarize() -> tuple[int, list[tuple[str, list[tuple[str, str, int]]]]]:
    """回傳 (total_canonical, conflict_list)。"""
    conflicts = []
    for en, rows in entries.items():
        # 去重 ZH（歸一化後）
        zh_variants: dict[str, list[tuple[str, str, int]]] = defaultdict(list)
        for zh, src, ln in rows:
            key = normalize_zh(zh)
            zh_variants[key].append((zh, src, ln))
        if len(zh_variants) > 1:
            conflicts.append((en, sorted(rows, key=lambda x: x[1])))
    return len(entries), conflicts


def write_master_csv() -> Path:
    out = UQM_WORK / f"_terminology_master_table_{DATE}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["English", "Chinese", "Source", "LineNo"])
        for en in sorted(entries.keys()):
            for zh, src, ln in entries[en]:
                w.writerow([en, zh, src, ln])
    return out


def write_phase1_report(conflicts: list) -> Path:
    out = UQM_WORK / f"_terminology_audit_phase1_{DATE}.md"
    total = len(entries)
    total_rows = sum(len(v) for v in entries.values())
    # 分類：conflict 之嚴重度
    high = []  # ≥3 個 variants
    mid = []   # 2 個 variants
    for en, rows in conflicts:
        variants = set(normalize_zh(zh) for zh, _, _ in rows)
        if len(variants) >= 3:
            high.append((en, rows))
        else:
            mid.append((en, rows))

    with out.open("w", encoding="utf-8") as f:
        f.write(f"# Phase 1 · 規範檔內部一致性稽核（{DATE}）\n\n")
        f.write("> 自動化抽取 · 由 `_terminology_audit_extract.py` 產出。\n")
        f.write("> **shipped-preference 策略**：實際決策應對照 shipped JSON。此報告僅識別「規範檔內部」衝突。\n\n")
        f.write("## 統計\n\n")
        f.write(f"- 掃描檔案：`StarControl2_TW_Localization/**/*.{{md,csv}}` （跳過 Reference_Material · 跳過 Template · 跳過歷史/禁止區段）\n")
        f.write(f"- 抽取獨立 canonical 詞：**{total}** 條\n")
        f.write(f"- 表格總列數（含跨檔重複）：**{total_rows}** 列\n")
        f.write(f"- 內部衝突項：**{len(conflicts)}**\n")
        f.write(f"  - 🔴 高嚴重度（≥3 種譯法並存）：**{len(high)}**\n")
        f.write(f"  - 🟠 中嚴重度（2 種譯法並存）：**{len(mid)}**\n\n")
        f.write("---\n\n")

        def dump_conflict_group(title: str, group: list) -> None:
            f.write(f"## {title}（{len(group)} 項）\n\n")
            for idx, (en, rows) in enumerate(sorted(group, key=lambda x: x[0].lower()), 1):
                # 分組同 ZH
                by_zh: dict[str, list[tuple[str, int]]] = defaultdict(list)
                for zh, src, ln in rows:
                    by_zh[zh].append((src, ln))
                f.write(f"### #{idx} · `{en}`\n\n")
                for zh in sorted(by_zh.keys()):
                    srcs = by_zh[zh]
                    f.write(f"- **{zh}** ({len(srcs)} 處)：")
                    f.write("、".join(f"`{s}:{l}`" for s, l in srcs[:8]))
                    if len(srcs) > 8:
                        f.write(f" … （+{len(srcs)-8}）")
                    f.write("\n")
                f.write("\n")
            f.write("---\n\n")

        if high:
            dump_conflict_group("🔴 高嚴重度衝突", high)
        if mid:
            dump_conflict_group("🟠 中嚴重度衝突", mid)

        f.write("## 附註\n\n")
        f.write("- 本報告是**自動化的第一次通盤掃描**。人工閱讀可能會發現：\n")
        f.write("  - 某些「衝突」實為 delta（舊 canonical 未更新 · 例如 Fixed_Terms.csv 未追上 Master_Glossary.md）\n")
        f.write("  - 某些同一 English 在不同語境合法有多譯（例如 Cannon 憂特 vs 毒賈）\n")
        f.write("  - 「保留原文」與「中譯」共存，通常代表新舊 canonical policy 交替期\n")
        f.write("- 建議搭配 shipped JSON 對照（Phase 2）決定最終 canonical\n\n")
    return out


def main() -> int:
    if not ROOT.exists():
        print(f"ROOT not found: {ROOT}", file=sys.stderr)
        return 1
    scan_all()
    total, conflicts = summarize()
    print(f"Extracted {total} unique canonical terms")
    print(f"Detected {len(conflicts)} internal conflicts")
    csv_path = write_master_csv()
    md_path = write_phase1_report(conflicts)
    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
