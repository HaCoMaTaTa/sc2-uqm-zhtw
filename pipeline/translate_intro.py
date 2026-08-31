"""
Translate UQM intro-style script files.

intro.txt (and similar cutscene scripts) use a mini-DSL:
  COMMAND arg1 arg2 ...
  #(comment) or #(<TOKEN>)
  TFI <text-line-1>
  <text-line-2>       (continuation until next command or blank line)
  TFO
  WAIT 2000

The `TFI` (Text Fade-In) command is followed by one or more text lines
containing the actual translatable text. We do exact string substitution:
each JSON entry pairs the exact source multi-line text with its translation.

Usage:
  python translate_intro.py \
      --source  Q:\...\intro.txt \
      --translations Q:\...\intro.zh-TW.json \
      --out     Q:\...\intro.zh-TW.txt

JSON format (both keys and values may contain '\n' for multi-line):
  {
    "There were many great battles...": "戰役無數，浩瀚無比……",
    "Earth and her partners in the\nAlliance of Free Stars...": "地球與自由星域聯盟的夥伴們……"
  }
"""
import argparse
import json
import re
from pathlib import Path


def find_tfi_block(text: str, tfi_index: int):
    """Given text index of a 'TFI ' occurrence at start of line, return
    (start_of_text_after_TFI, end_index_of_block).

    Block ends at the next line starting with a command (uppercase word) or
    a '#(' comment/token. The text portion excludes trailing newline.
    """
    # Locate start of text: after "TFI "
    text_start = tfi_index + 4
    # Find next line starting with a token — commands: uppercase word optionally
    # followed by args, or '#(' comment, or blank line.
    idx = text_start
    while idx < len(text):
        # Advance to next newline
        nl = text.find("\n", idx)
        if nl == -1:
            return text_start, len(text)
        next_line_start = nl + 1
        if next_line_start >= len(text):
            return text_start, len(text)
        # Peek next line's first non-space char
        next_line = text[next_line_start:text.find("\n", next_line_start) if text.find("\n", next_line_start) != -1 else len(text)]
        stripped = next_line.strip()
        if not stripped:
            return text_start, nl  # end at nl (last newline before blank)
        # A command line starts with either:
        #   1. `#(` — comment or token marker, or
        #   2. an ALL-CAPS identifier (2+ chars) followed by whitespace or EOL.
        # Just an uppercase LETTER followed by lowercase text (e.g. "Alliance")
        # is a continuation of the TFI block, not a command.
        if stripped.startswith("#("):
            return text_start, nl
        first_word_match = re.match(r"^[A-Z][A-Z0-9_]+(\s|$)", stripped)
        if first_word_match:
            return text_start, nl
        # Otherwise, this is a continuation line of TFI
        idx = next_line_start

    return text_start, len(text)


def apply_translations(text: str, translations: dict):
    """For each TFI text block, look up the exact multi-line text in
    translations and substitute if present. Returns (new_text, stats)."""
    # Find every "TFI " at the start of a line
    pattern = re.compile(r"(?m)^TFI ")
    hits = 0
    misses = []
    result = []
    last = 0

    for m in pattern.finditer(text):
        tfi_at = m.start()
        result.append(text[last:tfi_at])  # everything before this TFI
        text_start, text_end = find_tfi_block(text, tfi_at)
        original = text[text_start:text_end]
        if original in translations:
            new = translations[original]
            result.append("TFI " + new)
            hits += 1
        else:
            # Preserve original unchanged; record miss
            result.append(text[tfi_at:text_end])
            misses.append(original)
        last = text_end

    result.append(text[last:])
    return "".join(result), hits, misses


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--translations", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8", errors="replace")
    translations = json.loads(args.translations.read_text(encoding="utf-8"))
    print(f"Loaded {len(translations)} translation entries")

    new_text, hits, misses = apply_translations(text, translations)
    print(f"Translated {hits} TFI blocks")
    if misses:
        print(f"MISS ({len(misses)}) — untranslated TFI blocks (kept as English):")
        for i, m in enumerate(misses):
            first_line = m.split("\n")[0][:60]
            print(f"  [{i}] {first_line!r}")
    unmatched = [k for k in translations if k not in text]
    if unmatched:
        print(f"WARN: {len(unmatched)} translation KEYS not found in source:")
        for k in unmatched[:5]:
            print(f"  - {k[:60]!r}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
