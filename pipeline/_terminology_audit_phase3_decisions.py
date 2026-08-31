"""
Terminology Audit Phase 3 · 對照 md 規範 vs shipped 主流 · 產出決策清單

Usage:
    python _terminology_audit_phase3_decisions.py

Inputs:
    _terminology_master_table_2026-08-18.csv    (Phase 1 · md 規範抽出)
    _terminology_shipped_matrix_2026-08-18.csv  (Phase 2 · shipped 使用矩陣)

Output:
    _terminology_audit_phase3_decisions_2026-08-18.md   (決策清單 · A/B/C)

策略：
- 以 Phase 2 seed EN 為 pivot（187 條精選 canonical）
- 對每個 EN：
    - md 側：找權威 canonical（優先 Master_Glossary → *_Names.md → Fixed_Terms.csv）
    - shipped 側：找主流 variant（total 最高）+ 次要 variant
- 分類：
    ✅ 一致（規範=shipped 主流）→ 不列入決策
    🔴 明確衝突（規範權威 ≠ shipped 主流）
    🟠 多譯並存（shipped 主流 A，次要 B 也超過 15%）
    🟣 規範過時（Master_Glossary 新 · Fixed_Terms.csv 舊 · shipped 追 Master）
    ⚪ shipped 缺席（規範定但 shipped 用 0 次 · dossier canonical 塌陷警訊）
    ⚫ 規範缺席（shipped 用了但規範沒鎖）
"""
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

UQM_WORK = Path(r"q:\Dos_G\StarControl2\uqm-work")
DATE = "2026-08-18"

MASTER_CSV = UQM_WORK / f"_terminology_master_table_{DATE}.csv"
SHIPPED_CSV = UQM_WORK / f"_terminology_shipped_matrix_{DATE}.csv"
OUT_MD = UQM_WORK / f"_terminology_audit_phase3_decisions_{DATE}.md"

# 規範側 source 優先序（數字小 = 權威高）
SOURCE_PRIORITY = {
    "07_Glossary/Master_Glossary.md":  1,
    "07_Glossary/Race_Names.md":       2,
    "07_Glossary/Ship_Names.md":       2,
    "07_Glossary/Tech_Names.md":       2,
    "07_Glossary/Place_Names.md":      2,
    "07_Glossary/Character_Names.md":  2,
    "07_Glossary/Fixed_Terms.csv":     3,  # 舊 canonical
    "07_Glossary/Forbidden_Translations.md": 99,  # 禁止 · 不列為權威
}


def source_prio(src: str) -> int:
    # 精確 match 優先
    if src in SOURCE_PRIORITY:
        return SOURCE_PRIORITY[src]
    # 前綴 match
    for k, v in SOURCE_PRIORITY.items():
        if src.startswith(k.split("/")[0]):
            return 5
    # 04_Ships/05_Technology/06_Locations/03_Characters/01_World_Lore/02_Races 等 dossier
    for prefix in ("02_Races/", "04_Ships/", "05_Technology/", "06_Locations/",
                   "03_Characters/", "01_World_Lore/", "08_Translation_Rules/"):
        if src.startswith(prefix):
            return 6
    return 10


# ─────────────────────────────────────────────────────────
# 讀 Phase 1 master table
# ─────────────────────────────────────────────────────────
def load_master() -> dict[str, list[tuple[str, str, int]]]:
    """Returns md_map[EN_lower] = [(ZH, source, lineno), ...]"""
    m = defaultdict(list)
    with MASTER_CSV.open(encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        for row in r:
            en = row["English"].strip()
            zh = row["Chinese"].strip()
            src = row["Source"].strip()
            ln = int(row["LineNo"])
            if en and zh:
                m[en.lower()].append((zh, src, ln))
    return m


def load_shipped() -> tuple[dict, list[str]]:
    """Returns:
        shipped_map[EN] = {"category": ..., "variants": {variant: {race: count, ..., "_total": N}}}
        races: list of race column names
    """
    m = {}
    races = []
    with SHIPPED_CSV.open(encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        # detect race columns (all cols except Category, English, Variant, Total)
        headers = r.fieldnames or []
        races = [h for h in headers if h not in ("Category", "English", "Variant", "Total")]
        for row in r:
            en = row["English"].strip()
            var = row["Variant"].strip()
            cat = row["Category"].strip()
            total = int(row["Total"])
            if total == 0:
                continue
            if en not in m:
                m[en] = {"category": cat, "variants": {}}
            per_race = {race: int(row[race]) for race in races if int(row[race]) > 0}
            per_race["_total"] = total
            m[en]["variants"][var] = per_race
    return m, races


# ─────────────────────────────────────────────────────────
# 規範側「權威 canonical」判斷
# ─────────────────────────────────────────────────────────
def normalize_zh(s: str) -> str:
    """歸一化 ZH 用於等價比對"""
    s = s.strip().strip("「」『』\"'*# `")
    s = s.replace("·", "").replace("・", "").replace("‧", "").replace("．", "")
    # 去尾部說明（暫定/待議/舊）
    import re
    s = re.sub(r"[（(](暫定|待議|待決|obsolete|舊|廢止|已廢|見上|見下)[^)）]*[)）]$", "", s).strip()
    return s


def find_md_canonical(md_entries: list[tuple[str, str, int]]) -> tuple[str | None, list[str], list[tuple[str, str, int]]]:
    """
    對某 EN 的所有 md 側 entries，找出「權威 canonical」。
    Returns (primary_zh, all_variants_normalized, all_entries_sorted_by_priority)
    """
    if not md_entries:
        return None, [], []
    # 依 source priority 排序
    sorted_entries = sorted(md_entries, key=lambda x: (source_prio(x[1]), x[1], x[2]))
    # 取最高權威的 ZH
    highest_prio = source_prio(sorted_entries[0][1])
    top_group = [e for e in sorted_entries if source_prio(e[1]) == highest_prio]
    # 若最高權威組有多個 ZH · 取出現次數最多的
    from collections import Counter
    zh_counter = Counter(normalize_zh(e[0]) for e in top_group)
    primary = zh_counter.most_common(1)[0][0] if zh_counter else None
    # 所有 normalized 變體 · 去重
    all_norm = list(set(normalize_zh(e[0]) for e in sorted_entries))
    return primary, all_norm, sorted_entries


# ─────────────────────────────────────────────────────────
# 比對邏輯
# ─────────────────────────────────────────────────────────
def analyze(md_map, shipped_map):
    """對每個 EN 判斷分類"""
    decisions = []  # list of dict
    for en, shipped_info in shipped_map.items():
        cat = shipped_info["category"]
        variants = shipped_info["variants"]  # variant -> per_race dict
        # shipped 主流
        by_total = sorted(variants.items(), key=lambda kv: -kv[1]["_total"])
        primary_var, primary_per_race = by_total[0]
        primary_total = primary_per_race["_total"]
        total_all = sum(v["_total"] for v in variants.values())
        primary_share = primary_total / total_all if total_all else 0
        # 次要 variants
        minor_vars = [(v, p["_total"]) for v, p in by_total[1:]]

        # md 側查詢
        md_entries = md_map.get(en.lower(), [])
        md_primary, md_variants_norm, md_entries_sorted = find_md_canonical(md_entries)

        # 決策分類
        shipped_primary_norm = normalize_zh(primary_var)
        md_primary_norm = normalize_zh(md_primary) if md_primary else None

        record = {
            "en": en,
            "category": cat,
            "shipped_primary": primary_var,
            "shipped_primary_share": primary_share,
            "shipped_primary_total": primary_total,
            "shipped_minors": minor_vars,
            "shipped_races_using_primary": {k: v for k, v in primary_per_race.items() if k != "_total"},
            "md_primary": md_primary,
            "md_variants_norm": md_variants_norm,
            "md_entries": md_entries_sorted,
            "total_all": total_all,
        }

        if not md_primary:
            record["type"] = "⚫ 規範缺席"  # shipped 用但規範沒定
            decisions.append(record)
            continue

        if shipped_primary_norm == md_primary_norm:
            # 主流一致
            if len(minor_vars) > 0 and minor_vars[0][1] >= max(1, primary_total * 0.15):
                record["type"] = "🟠 shipped 多譯並存"  # 主流對，但有次要
                decisions.append(record)
            else:
                record["type"] = "✅ 完全一致"
                # 不加入 decisions（減少雜訊）
        else:
            # 主流不一致
            if shipped_primary_norm in md_variants_norm:
                # shipped 主流是 md 側「已知變體」之一 · 但不是主權威
                record["type"] = "🟣 規範內部有此譯 · shipped 選了非主權威"
            else:
                record["type"] = "🔴 shipped 主流 ≠ 規範權威"
            decisions.append(record)

    return decisions


# ─────────────────────────────────────────────────────────
# 產報告
# ─────────────────────────────────────────────────────────
def format_races(per_race: dict, limit=6) -> str:
    items = sorted(((r, c) for r, c in per_race.items()), key=lambda kv: -kv[1])
    parts = [f"{r}×{c}" for r, c in items[:limit]]
    tail = "" if len(items) <= limit else f" …+{len(items)-limit}"
    return "、".join(parts) + tail


def format_md_sources(entries: list[tuple[str, str, int]], limit=4) -> str:
    parts = []
    for zh, src, ln in entries[:limit]:
        parts.append(f"「**{zh}**」`{src}:{ln}`")
    tail = "" if len(entries) <= limit else f" …+{len(entries)-limit}"
    return "、".join(parts) + tail


def write_report(decisions: list) -> None:
    # 分類
    by_type = defaultdict(list)
    for d in decisions:
        by_type[d["type"]].append(d)

    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write(f"# Phase 3 · 規範 vs shipped 決策清單（{DATE}）\n\n")
        f.write("> 對照 Phase 1 md 規範側 canonical 與 Phase 2 shipped JSON 主流用法 · 產出決策項\n")
        f.write("> **shipped-preference 策略**：預設建議「以 shipped 為準 · 修規範對齊」· 除非規範是 v0.7 新版而 shipped 尚未 retrofit\n\n")
        f.write("## 統計\n\n")
        total = len(decisions)
        f.write(f"- **需決策項總數**：**{total}**（僅列有差異者 · ✅ 完全一致者已濾除）\n")
        for typ in ["🔴 shipped 主流 ≠ 規範權威", "🟣 規範內部有此譯 · shipped 選了非主權威",
                    "🟠 shipped 多譯並存", "⚫ 規範缺席"]:
            n = len(by_type.get(typ, []))
            f.write(f"  - {typ}：**{n}**\n")
        f.write("\n---\n\n")

        def dump_section(title: str, group: list) -> None:
            if not group:
                return
            f.write(f"## {title}（{len(group)} 項）\n\n")
            group_sorted = sorted(group, key=lambda d: -d["total_all"])
            for i, d in enumerate(group_sorted, 1):
                f.write(f"### #{i} · `{d['en']}` 【{d['category']}】\n\n")
                # shipped 側
                f.write(f"- **shipped 主流**：「**{d['shipped_primary']}**」× {d['shipped_primary_total']} ")
                f.write(f"（{d['shipped_primary_share']:.0%} · 出處：{format_races(d['shipped_races_using_primary'])}）\n")
                if d["shipped_minors"]:
                    for v, n in d["shipped_minors"]:
                        share = n / d["total_all"] if d["total_all"] else 0
                        # 找哪些 race 用此 variant
                        var_races = {k: v2 for k, v2 in d.get("shipped_races_using_primary", {}).items() if False}
                        # 從 shipped_map 直接找？我沒帶 · 用簡短
                        f.write(f"  - shipped 次要：「{v}」× {n}（{share:.0%}）\n")
                # md 側
                if d["md_entries"]:
                    f.write(f"- **規範側**：{format_md_sources(d['md_entries'])}\n")
                    if d["md_primary"] and normalize_zh(d["md_primary"]) != normalize_zh(d["shipped_primary"]):
                        f.write(f"- ⚠️ **權威 canonical**「**{d['md_primary']}**」與 shipped 主流「**{d['shipped_primary']}**」**不同**\n")
                else:
                    f.write(f"- **規範側**：**未鎖定**（規範缺席）\n")
                # 建議
                if d["type"] == "🔴 shipped 主流 ≠ 規範權威":
                    f.write(f"- **建議**：📌 若規範為 v0.7 新版（Master_Glossary 標記）→ retrofit shipped\n")
                    f.write(f"  · 若規範舊而 shipped 為玩家熟悉譯 → 升版規範對齊 shipped\n")
                elif d["type"] == "🟣 規範內部有此譯 · shipped 選了非主權威":
                    f.write(f"- **建議**：📌 shipped 用的是 md 側「已知變體」但不是主權威 · 建議統一為主權威「{d['md_primary']}」\n")
                elif d["type"] == "🟠 shipped 多譯並存":
                    f.write(f"- **建議**：📌 shipped 內部多譯並存 · 建議統一為主流「{d['shipped_primary']}」· 修少數異體\n")
                elif d["type"] == "⚫ 規範缺席":
                    f.write(f"- **建議**：📌 規範側完全沒鎖定此 EN · 建議補入 Master_Glossary\n")
                f.write(f"- **決策**：A. 依建議 · B. 保留現況 · C. 自訂\n\n")
            f.write("---\n\n")

        dump_section("🔴 shipped 主流 ≠ 規範權威", by_type.get("🔴 shipped 主流 ≠ 規範權威", []))
        dump_section("🟣 規範內部有此譯 · shipped 選了非主權威", by_type.get("🟣 規範內部有此譯 · shipped 選了非主權威", []))
        dump_section("🟠 shipped 多譯並存（規範對 · shipped 內部亂）", by_type.get("🟠 shipped 多譯並存", []))
        dump_section("⚫ 規範缺席（shipped 用了但規範沒鎖）", by_type.get("⚫ 規範缺席", []))

        f.write("## 附註\n\n")
        f.write("- 本清單**僅列有差異者**（✅ 完全一致者已濾除，減少雜訊）\n")
        f.write("- shipped-preference 策略：預設建議「以 shipped 為準」· 除非規範明顯較新（v0.7 標記）\n")
        f.write("- Voice 塌陷警訊（例如 dossier §四 canonical 但 shipped 用 0 次）**不在此清單** · 見 Phase 2 報告 Voice 段\n")
        f.write("- 未列 EN = 完全一致 · 無需決策\n")


def main() -> int:
    if not MASTER_CSV.exists() or not SHIPPED_CSV.exists():
        print(f"Missing input CSV. Expected:\n  {MASTER_CSV}\n  {SHIPPED_CSV}")
        return 1
    print(f"Loading Phase 1 master table...")
    md_map = load_master()
    print(f"  {len(md_map)} unique EN in md")
    print(f"Loading Phase 2 shipped matrix...")
    shipped_map, races = load_shipped()
    print(f"  {len(shipped_map)} unique EN in shipped ({len(races)} races)")
    print(f"Analyzing...")
    decisions = analyze(md_map, shipped_map)
    print(f"  {len(decisions)} decision items")
    write_report(decisions)
    print(f"Wrote: {OUT_MD}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
