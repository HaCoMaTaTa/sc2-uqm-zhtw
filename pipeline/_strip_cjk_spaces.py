#!/usr/bin/env python3
"""Strip CJK-CJK spaces from translation JSON (post-patch-006).

Patch 006 in src/uqm/comm.c getLineWithinWidth treats CJK char (U+4E00..U+9FFF)
as a word boundary, so we no longer need ASCII spaces between CJK groups for
_count_lines() wrap. Spaces between CJK and ASCII (Lua templates, punctuation)
are preserved to keep those tokens as their own "word" if needed.

Skips the `_notes` array (metadata block) so hand-written notes are not touched.

Usage:
    python _strip_cjk_spaces.py translations/shofixti.zh-TW.json [--dry-run]
    python _strip_cjk_spaces.py translations/*.zh-TW.json --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Match one or more space/tab BETWEEN two CJK characters (does not consume the CJKs)
CJK_SPACE_CJK = re.compile(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])')


def process(path: Path, dry_run: bool = False) -> tuple[int, int]:
    """Return (spaces_removed, lines_changed)."""
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    result: list[str] = []
    in_notes = False
    spaces_removed = 0
    lines_changed = 0

    for line in lines:
        stripped = line.lstrip()
        # Detect entering / leaving _notes array
        if not in_notes and '"_notes"' in line and '[' in line:
            in_notes = True
            result.append(line)
            continue
        if in_notes:
            result.append(line)
            # Leave _notes block when we hit the closing ']'
            if stripped.startswith(']'):
                in_notes = False
            continue

        new_line = CJK_SPACE_CJK.sub('', line)
        if new_line != line:
            spaces_removed += len(line) - len(new_line)
            lines_changed += 1
        result.append(new_line)

    new_text = '\n'.join(result)
    if new_text != text and not dry_run:
        path.write_text(new_text, encoding='utf-8')
    return spaces_removed, lines_changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+', type=Path)
    ap.add_argument('--dry-run', action='store_true',
                    help='Show counts without writing changes')
    args = ap.parse_args()

    total_spaces = 0
    total_lines = 0
    for f in args.files:
        if not f.exists():
            print(f'  SKIP: {f} (does not exist)', file=sys.stderr)
            continue
        spaces, lines = process(f, args.dry_run)
        total_spaces += spaces
        total_lines += lines
        tag = '[dry-run]' if args.dry_run else '[write]'
        print(f'  {tag} {f}: removed {spaces} spaces across {lines} lines')

    print(f'\nTOTAL: {total_spaces} spaces across {total_lines} lines')


if __name__ == '__main__':
    main()
