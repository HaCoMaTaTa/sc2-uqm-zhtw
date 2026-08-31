"""_extract_terms.py — 從 28 NPC 對話檔抽取所有專有名詞/特殊詞。

策略:
  A. Capitalized 連續詞(2+ 字元開頭大寫,可能是 proper noun)
  B. 引號內字串 (`"..."`, `` `...' ``, `'...'`)
  C. 星號詞 (`*...*`) — Orz 專用
  D. 全大寫詞 (SNORT, HEEEEELP, etc.) — 擬聲/強調
  E. 連字號名(Ur-Quan, Zoq-Fot-Pik, etc.)
  F. Lua template 內第一個字串參數(comm.getColor("blue", ...)等)

排除:
  - Token headers (#(TOKEN))
  - Voice cue (`slylandro-XXX.ogg`)
  - 通用英文詞(I, a, the, of, and, etc.)
  - 已在 SC2-詞彙對照表.md 的詞

輸出:
  - _terms/<race>.terms.json — 每族的候選詞清單
  - _terms/_summary.md — 總覽表
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
COMM_DIR = ROOT / "extracted" / "base" / "base" / "comm"
# Phase 12: 詞彙表已遷移到 StarControl2_TW_Localization/Reference_Material/
GLOSSARY_MD = ROOT.parent / "StarControl2_TW_Localization" / "Reference_Material" / "SC2-詞彙對照表.md"
PROMPT_MD = ROOT.parent / "StarControl2_TW_Localization" / "Reference_Material" / "SC2_繁中化_AI翻譯提詞.md"
OUT_DIR = ROOT / "_terms"

# ---------------------------------------------------------------------------
# 已知的通用詞(要排除,不算專有名詞)
# ---------------------------------------------------------------------------
STOP_WORDS = {
    # 英文常用詞
    "I", "A", "An", "The", "This", "That", "These", "Those",
    "It", "He", "She", "We", "You", "They", "Me", "My", "Our", "Us",
    "Your", "Their", "Its", "His", "Her", "Them", "Him",
    "Is", "Are", "Was", "Were", "Be", "Been", "Being", "Am",
    "Do", "Does", "Did", "Have", "Has", "Had",
    "Will", "Would", "Can", "Could", "Should", "May", "Might", "Must",
    "And", "Or", "But", "So", "If", "Then", "When", "Where", "Why", "How",
    "What", "Who", "Which", "Whom", "Whose",
    "In", "On", "At", "To", "From", "For", "Of", "With", "By", "As",
    "Not", "No", "Yes", "Yeah", "Yeh", "Oh", "Ah", "Ha", "Hi", "Hello",
    "Now", "Then", "Here", "There", "Some", "Any", "All", "None", "Both",
    "Very", "Really", "Just", "Only", "Also", "Even", "Still",
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "First", "Last", "Next", "Previous", "Once", "Twice",
    "Well", "OK", "Okay", "Please", "Sorry", "Thanks", "Thank",
    "Look", "See", "Know", "Think", "Say", "Said", "Tell", "Told", "Go", "Come",
    "Get", "Give", "Make", "Take", "Put", "Let", "Use", "Try", "Want", "Need",
    "Good", "Bad", "Great", "Nice", "Big", "Small", "New", "Old",
    "But", "About", "Because", "Since", "While", "Before", "After",
    "Above", "Below", "Between", "Under", "Over", "Through",
    "More", "Most", "Less", "Least", "Few", "Many", "Much",
    "Every", "Each", "Other", "Another", "Same", "Different",
    "Wow", "Whoa", "Hmm", "Hmmm", "Uh", "Um", "Er", "Eh",
    "Sure", "Certainly", "Actually", "Indeed", "Perhaps", "Maybe",
    "However", "Therefore", "Moreover", "Anyway", "Anywise",
    "Time", "Times", "Day", "Days", "Year", "Years", "World", "Worlds",
    "People", "Race", "Races", "Ship", "Ships", "Planet", "Planets",
    "Space", "Star", "Stars", "System", "Systems", "Galaxy", "Galaxies",
    "Life", "Death", "War", "Peace", "Love", "Hate",
    "Way", "Ways", "Thing", "Things", "Fact", "Facts",
    "Sir", "Madam", "Traveller", "Traveler", "Captain",
    "Goodbye", "Farewell", "Welcome", "Congratulations",
}
# 把 STOP_WORDS 全部改成小寫做比對(case-insensitive)
STOP_WORDS_LC = {w.lower() for w in STOP_WORDS}

# 常見縮寫 / contraction
CONTRACTION_RE = re.compile(r"^[A-Za-z]+'(s|re|ll|d|ve|m|t)$")

# 特殊模式:即使在 STOP_WORDS 也要保留(因為是遊戲特有用法)
FORCE_INCLUDE = {
    "Way",  # "The Path of Now and Forever" 相關
}

# 引號/星號模式
QUOTE_PATS = [
    (re.compile(r'"([^"\n]{2,80})"'),   "double"),
    (re.compile(r"``([^`\n]{2,80})''"), "backtick"),
    (re.compile(r"`([^`\n]{2,80})'"),  "backtick_single"),
    (re.compile(r"\*([^*\n]{2,80})\*"), "asterisk"),
]

# 至少 2 個字元、以大寫開頭、可包含連字號 & 撇號
CAPWORD = re.compile(r"\b([A-Z][A-Za-z0-9\-']*(?:\s+[A-Z][A-Za-z0-9\-']*)*)\b")

# 純大寫詞(SNORT!, HEEEEELP! 之類)
ALLCAPS = re.compile(r"\b([A-Z]{2,}[!?]*)\b")

# Lua template 內的第一個字串參數
LUA_PARAM = re.compile(r'<%[^%]*?\(\s*"([^"]{2,40})"')


def load_txt(path: Path) -> list[str]:
    """回傳除 header/voice-cue 之外的內文行。"""
    lines = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#("):
            continue
        lines.append(raw)
    return lines


def extract_from_race(race: str, comm_path: Path) -> dict:
    """回傳單一種族的候選詞 dict。"""
    lines = load_txt(comm_path)
    text = "\n".join(lines)

    result = {
        "race": race,
        "capitalized": Counter(),
        "quoted_double": Counter(),
        "quoted_backtick": Counter(),
        "asterisk": Counter(),
        "allcaps": Counter(),
        "lua_params": Counter(),
    }

    # (A) Capitalized 詞
    for m in CAPWORD.finditer(text):
        word = m.group(1).strip()
        if len(word) < 2:
            continue
        # 每個 " " 分詞
        tokens = word.split()
        for tok in tokens:
            tok_clean = tok.rstrip(".,;:!?")
            if len(tok_clean) < 2:
                continue
            if tok_clean.lower() in STOP_WORDS_LC and tok_clean not in FORCE_INCLUDE:
                continue
            # 過濾 contraction (I'm, don't, we'll, ...)
            if CONTRACTION_RE.match(tok_clean):
                continue
            # 過濾:一個字母也不行、只是常見連字符詞
            if tok_clean.upper() == tok_clean and len(tok_clean) < 4:
                # 短全大寫給 allcaps bucket 抓
                continue
            result["capitalized"][tok_clean] += 1
        # 也把整段 multi-word capitalized 抓進來(可能是頭銜/專名)
        if len(tokens) >= 2:
            phrase = word.rstrip(".,;:!?")
            # 過濾:全是 STOP_WORDS 或 contraction
            if all(t.lower() in STOP_WORDS_LC or CONTRACTION_RE.match(t) for t in phrase.split()):
                continue
            result["capitalized"][phrase] += 1

    # (B) 引號內容
    for pat, tag in QUOTE_PATS:
        for m in pat.finditer(text):
            content = m.group(1).strip()
            if len(content) < 2 or len(content) > 60:
                continue
            key = f"quoted_{tag.split('_')[0]}"
            if key not in result:
                key = "quoted_backtick"
            if "double" in tag:
                result["quoted_double"][content] += 1
            elif "asterisk" == tag:
                result["asterisk"][content] += 1
            else:
                result["quoted_backtick"][content] += 1

    # (D) 全大寫詞
    for m in ALLCAPS.finditer(text):
        w = m.group(1).rstrip(".,;:!?")
        if len(w) >= 3 and w not in {"OK", "USA", "PS", "II", "III", "IV"}:
            result["allcaps"][w] += 1

    # (F) Lua template 第一個參數
    for m in LUA_PARAM.finditer(text):
        result["lua_params"][m.group(1)] += 1

    return result


def collect_glossary_terms() -> set[str]:
    """讀既有詞彙表 + AI 翻譯提詞 md,抽出所有英文 term。"""
    terms: set[str] = set()

    for src in (GLOSSARY_MD, PROMPT_MD):
        if not src.is_file():
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            # 抽表格第一欄
            m = re.match(r"^\|\s*\**([A-Za-z][A-Za-z0-9\-'\s/\.,()\[\]]*?)\**\s*\|", line)
            if m:
                t = m.group(1).strip().rstrip(".").strip()
                if t and len(t) > 1:
                    terms.add(t)
                    # 也拆單詞
                    for w in re.findall(r"[A-Z][A-Za-z0-9\-']+", t):
                        terms.add(w)
            # 抽本文內以 `code` 或粗體標的英文詞
            for m2 in re.finditer(r"`([A-Za-z][A-Za-z0-9\-'\s]{1,40})`", line):
                terms.add(m2.group(1).strip())
            for m3 in re.finditer(r"\*\*([A-Z][A-Za-z0-9\-'\s]{1,40})\*\*", line):
                t = m3.group(1).strip()
                if t and t[0].isupper():
                    terms.add(t)
                    for w in re.findall(r"[A-Z][A-Za-z0-9\-']+", t):
                        terms.add(w)
    return terms


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)

    if not COMM_DIR.is_dir():
        print(f"[ERROR] {COMM_DIR} 不存在", file=sys.stderr)
        return 1

    known_terms = collect_glossary_terms()
    print(f"已有詞彙表已知 {len(known_terms)} 條 term")

    all_terms_by_race = {}
    all_seen_terms: Counter = Counter()
    race_of_term: dict[str, set[str]] = defaultdict(set)

    for race_dir in sorted(COMM_DIR.iterdir()):
        if not race_dir.is_dir():
            continue
        race = race_dir.name
        comm_txt = race_dir / f"{race}.txt"
        if not comm_txt.is_file():
            continue
        info = extract_from_race(race, comm_txt)
        all_terms_by_race[race] = info

        # aggregate
        for bucket in ["capitalized", "quoted_double", "quoted_backtick",
                       "asterisk", "allcaps", "lua_params"]:
            for term, count in info[bucket].items():
                all_seen_terms[term] += count
                race_of_term[term].add(race)

    # 寫每族的原始檔
    for race, info in all_terms_by_race.items():
        (OUT_DIR / f"{race}.terms.json").write_text(
            json.dumps(
                {k: (dict(v) if isinstance(v, Counter) else v)
                 for k, v in info.items()},
                ensure_ascii=False, indent=2
            ),
            encoding="utf-8"
        )

    # 產出「未在詞彙表」的候選清單
    novel_terms: list[dict] = []
    for term, count in all_seen_terms.items():
        # 判斷是否已知
        if term in known_terms:
            continue
        # 也判斷首詞(比如 "Zoq" 是 "Zoq-Fot-Pik" 的一部分)
        first_word = term.split("-")[0].split()[0]
        if first_word in known_terms:
            continue
        # 太短或純數字跳過
        if len(term) < 3:
            continue
        if term.isdigit():
            continue
        # 後置雙保險:整個 term (全部拆單詞) 若都是 stop-word / contraction,跳過
        term_tokens = term.replace("-", " ").split()
        if term_tokens and all(
            t.lower() in STOP_WORDS_LC or CONTRACTION_RE.match(t) or t.isdigit()
            for t in term_tokens
        ):
            continue
        # 純大寫短字(<= 3 字元)保守跳過,交給 allcaps bucket 專屬處理
        if term.upper() == term and len(term) <= 3:
            continue
        races_using = sorted(race_of_term[term])
        novel_terms.append({
            "term": term,
            "total_count": count,
            "races": races_using,
            "num_races": len(races_using),
        })

    # 依 (total_count, num_races) 排序
    novel_terms.sort(key=lambda x: (-x["total_count"], -x["num_races"], x["term"]))

    (OUT_DIR / "_novel_terms.json").write_text(
        json.dumps(novel_terms, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    # 產出可讀 summary md
    md = ["# NPC 對話「候選特殊詞」抽取報告", ""]
    md.append(f"- 掃描種族數: **{len(all_terms_by_race)}**")
    md.append(f"- 找到未在既有詞彙表的候選詞: **{len(novel_terms)}**")
    md.append("")
    md.append("## Top 60 候選詞(依總出現次數)")
    md.append("")
    md.append("| 詞 | 總次數 | 出現族數 | 種族 |")
    md.append("|---|---:|---:|---|")
    for entry in novel_terms[:60]:
        races_str = ", ".join(entry["races"][:5])
        if len(entry["races"]) > 5:
            races_str += f"…(+{len(entry['races']) - 5})"
        md.append(f"| `{entry['term']}` | {entry['total_count']} | {entry['num_races']} | {races_str} |")

    md.append("")
    md.append("## 每族專屬詞(該族唯一使用,可能是族內招牌)")
    md.append("")
    per_race_unique = defaultdict(list)
    for entry in novel_terms:
        if entry["num_races"] == 1:
            per_race_unique[entry["races"][0]].append(entry)

    for race in sorted(per_race_unique):
        items = per_race_unique[race]
        if not items:
            continue
        md.append(f"### {race} ({len(items)} 詞)")
        md.append("")
        md.append("| 詞 | 次數 |")
        md.append("|---|---:|")
        for entry in items[:20]:
            md.append(f"| `{entry['term']}` | {entry['total_count']} |")
        if len(items) > 20:
            md.append(f"| _…以及 {len(items) - 20} 詞_ | |")
        md.append("")

    (OUT_DIR / "_summary.md").write_text("\n".join(md), encoding="utf-8")

    print(f"\n★ 產出:")
    print(f"  · {OUT_DIR}/_novel_terms.json — 完整候選清單 ({len(novel_terms)} 條)")
    print(f"  · {OUT_DIR}/_summary.md — 人類閱讀報告")
    print(f"  · {OUT_DIR}/<race>.terms.json — 每族原始抽取")
    print(f"\n頂 20 候選詞快速預覽:")
    for entry in novel_terms[:20]:
        races = ", ".join(entry["races"][:3])
        if len(entry["races"]) > 3:
            races += f"…(+{len(entry['races']) - 3})"
        print(f"  {entry['total_count']:>3}× [{entry['num_races']} 族] {entry['term']:<30} — {races}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
