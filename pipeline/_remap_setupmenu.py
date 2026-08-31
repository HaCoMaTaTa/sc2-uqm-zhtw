"""
Convert setupmenu.zh-TW.json (english-text-keys format) → ID-keys format.

Draft has:
  {
    "English string": "中文翻譯",
    "Multi-line\nEnglish": "多行\n中文",
    ...
  }

Target format (what translate_ui.py expects):
  {
    "TITLE": "翻譯",
    "SUBTITLES": "line1\nline2\nline3",  # multi-line joined
    "CAT_0_OPTS": "opt1\nopt2\nopt3",
    "CAT_0_OPT_0_DESC": "desc line 1\ndesc line 2",
    ...
  }

Strategy: Parse setupmenu.txt records. For each record, look up each line
in draft and assemble the translation. Missing = keep English (untranslated
lines fall through per translate_ui.py behavior).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work")
SRC_TXT = ROOT / "extracted" / "base" / "base" / "ui" / "setupmenu.txt"
DRAFT_JSON = ROOT / "translations" / "setupmenu.zh-TW.json"
OUT_JSON = ROOT / "translations" / "setupmenu.zh-TW.json.remapped"

ID_LINE = re.compile(r"^#\(([^)]+)\)(.*)$")


def parse_records(txt_path):
    """Parse .txt into list of {id, content_lines}."""
    text = txt_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    records = []
    i = 0
    while i < len(lines):
        m = ID_LINE.match(lines[i])
        if m:
            rid = m.group(1)
            i += 1
            content = []
            while i < len(lines) and not ID_LINE.match(lines[i]):
                content.append(lines[i])
                i += 1
            # Trim trailing blanks
            while content and content[-1].strip() == "":
                content.pop()
            records.append({"id": rid, "content": content})
        else:
            i += 1
    return records


def make_multi_variants(lines):
    """Given content lines, produce all possible sub-string keys that could
    appear in draft. Returns list of (start, end) index ranges of contiguous
    non-blank line groups + the whole joined multi-line if reasonable."""
    variants = []
    n = len(lines)
    # Whole content (joined with \n) - primary lookup for multi-line values
    variants.append(("\n".join(lines), 0, n))
    # Individual non-blank lines
    for i, line in enumerate(lines):
        if line.strip():
            variants.append((line, i, i + 1))
    # Contiguous non-blank runs
    i = 0
    while i < n:
        if lines[i].strip():
            j = i
            while j < n and lines[j].strip():
                j += 1
            if j - i > 1:
                variants.append(("\n".join(lines[i:j]), i, j))
            i = j
        else:
            i += 1
    return variants


def remap(draft, records):
    """Build ID-keyed dict from draft (english→chinese) by matching against records."""
    id_map = {}
    unmapped_draft_keys = set(k for k in draft if not k.startswith("_"))
    unmatched_records = []

    for rec in records:
        rid = rec["id"]
        lines = rec["content"]
        if not lines:
            continue

        # Try 1: whole content matches a draft key exactly
        whole = "\n".join(lines)
        if whole in draft:
            id_map[rid] = draft[whole]
            unmapped_draft_keys.discard(whole)
            continue

        # Try 2: assemble line-by-line, preserving blanks
        assembled = []
        any_line_translated = False
        for line in lines:
            if line.strip() == "":
                assembled.append(line)
            elif line in draft:
                assembled.append(draft[line])
                unmapped_draft_keys.discard(line)
                any_line_translated = True
            else:
                assembled.append(line)  # keep English

        if any_line_translated:
            id_map[rid] = "\n".join(assembled)
        else:
            unmatched_records.append(rid)

    return id_map, unmapped_draft_keys, unmatched_records


def main():
    print(f"=== Parsing {SRC_TXT.name} ===")
    records = parse_records(SRC_TXT)
    print(f"  {len(records)} records")

    print(f"\n=== Loading draft {DRAFT_JSON.name} ===")
    draft = json.loads(DRAFT_JSON.read_text(encoding="utf-8"))
    non_meta = {k: v for k, v in draft.items() if not k.startswith("_")}
    print(f"  {len(non_meta)} english-keyed translations (excluding metadata)")

    print("\n=== Remapping ===")
    id_map, unmapped, unmatched = remap(non_meta, records)
    print(f"  [OK] Mapped {len(id_map)} IDs")
    print(f"  [WARN] {len(unmapped)} draft keys did NOT match any record content")
    print(f"  [INFO] {len(unmatched)} records had no translated lines (unaffected)")

    if unmapped:
        print(f"\n  First 10 unmapped draft keys (English text with no match):")
        for k in list(unmapped)[:10]:
            preview = k.replace("\n", " / ")[:70]
            print(f"    '{preview}'")

    # Preserve _notes, _comment_old
    output = {}
    if "_notes" in draft:
        output["_notes"] = draft["_notes"]
    if "_comment_old" in draft:
        output["_comment_old"] = draft["_comment_old"]
    # Add all mapped translations
    output.update(id_map)

    OUT_JSON.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n=== Wrote {OUT_JSON} ===")
    print(f"  {len(id_map)} ID-keyed translations")
    print(f"  Total keys (with metadata): {len(output)}")


if __name__ == "__main__":
    main()
