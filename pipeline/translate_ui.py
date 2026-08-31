"""
UQM UI string translator.

Given:
  - Source .txt file (English UI strings, format: #(ID)\ntext\n\n)
  - JSON dict of {id: translated_text} (translated_text may contain newlines)

Emits: modified file with only specified IDs' content replaced. All others
remain untouched (so untranslated strings stay in English at runtime).

The .txt format:
  #(ID) -- optional comment
  <content line 1>
  <content line 2>
  ...
  (blank line)
  (blank line)
  #(NEXT_ID)
  ...

Content may include `|<n>|` alignment markers; those should be preserved
per translation entry (i.e., the translator decides whether to keep them).
"""

import argparse
import json
import re
from pathlib import Path


ID_LINE = re.compile(r"^#\(([^)]+)\)(.*)$")


def load_txt(path: Path):
    """Parse into list of records: {id, header_line, content_lines, tail_blanks}."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    records = []
    i = 0
    # Skip any leading blanks
    while i < len(lines):
        m = ID_LINE.match(lines[i])
        if m:
            rid = m.group(1)
            header = lines[i]
            i += 1
            content = []
            # Read until next #() or EOF; blank lines within content are kept
            while i < len(lines) and not ID_LINE.match(lines[i]):
                content.append(lines[i])
                i += 1
            # Trim trailing blanks from content and count them as separators
            trailing = 0
            while content and content[-1].strip() == "":
                content.pop()
                trailing += 1
            records.append({
                "id": rid,
                "header": header,
                "content": content,
                "trailing": trailing,
            })
        else:
            # skip stray lines
            i += 1
    return records


def apply_translations(records, translations: dict, strict_line_count: bool = True):
    """Return new records list with content replaced for matched IDs.

    If strict_line_count is False, allow translations to have different
    line counts than source. This is required for comm dialog files where
    each #(TOKEN) block corresponds to one voice segment and \n only
    affects visual line wrapping.
    """
    hits = 0
    warnings = 0
    for r in records:
        if r["id"] in translations:
            new = translations[r["id"]]
            if isinstance(new, str):
                new = new.splitlines()
            new = list(new)
            if strict_line_count and len(new) != len(r["content"]):
                # Safety: enforce same line count as original to avoid engine PANIC
                # when a multi-line block is treated as an array by the game.
                print(f"  WARN: id '{r['id']}' translation has {len(new)} lines "
                      f"but source has {len(r['content'])}. Padding/trimming.")
                warnings += 1
                if len(new) < len(r["content"]):
                    new.extend([""] * (len(r["content"]) - len(new)))
                else:
                    new = new[:len(r["content"])]
            r["content"] = new
            hits += 1
    return hits, warnings


def dump_txt(records, path: Path):
    out = []
    for r in records:
        out.append(r["header"])
        out.extend(r["content"])
        # normalize trailing blanks to at least 2 (matches original layout)
        n_blank = max(2, r["trailing"])
        out.extend([""] * n_blank)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True, type=Path, help="Original UI .txt")
    ap.add_argument("--translations", required=True, type=Path,
                    help="JSON file with {id: translated_text}")
    ap.add_argument("--out", required=True, type=Path, help="Output .txt")
    ap.add_argument("--allow-line-mismatch", action="store_true",
                    help="Allow translation to have different line counts "
                         "than source (required for comm dialog files where "
                         "each block is one voice segment).")
    args = ap.parse_args()

    records = load_txt(args.source)
    print(f"Loaded {len(records)} string records from {args.source}")

    translations = json.loads(args.translations.read_text(encoding="utf-8"))
    print(f"Loaded {len(translations)} translations from {args.translations}")

    hits, warns = apply_translations(records, translations,
                                      strict_line_count=not args.allow_line_mismatch)
    print(f"Applied {hits} translations (matching IDs), {warns} count-mismatch warnings.")
    unmatched = [k for k in translations if not any(r["id"] == k for r in records)]
    if unmatched:
        print(f"WARNING: {len(unmatched)} translation IDs not found in source:")
        for k in unmatched[:10]:
            print(f"  - {k}")
        if len(unmatched) > 10:
            print(f"  ... and {len(unmatched) - 10} more")

    dump_txt(records, args.out)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
