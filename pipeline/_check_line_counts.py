# -*- coding: utf-8 -*-
"""Build-time check: `\n` line count alignment between source .txt and translation JSON.

Voice cue timing depends on line count per token matching the English source
(each `\n` = one SplitSubPages page = one audio slice offset).
Mismatch causes SoundDecoder_Load to read past OGG EOF → crash.

Usage:
  python _check_line_counts.py            # all races, summary only
  python _check_line_counts.py --verbose  # show every mismatch token
  python _check_line_counts.py --strict   # exit 1 on any mismatch
  python _check_line_counts.py --race X   # single race
"""
import argparse
import json
import re
import sys
from pathlib import Path


def parse_source(path):
    """Parse an extracted .txt file into {token: line_count}."""
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    tokens = {}
    tok = None
    buf = []
    for ln in lines:
        m = re.match(r'^#\(([^)]+)\)', ln)
        if m:
            if tok is not None:
                # Strip trailing empty lines from buffer
                while buf and buf[-1] == '':
                    buf.pop()
                tokens[tok] = len(buf)
            tok = m.group(1)
            buf = []
        elif tok is not None:
            buf.append(ln)
    if tok is not None:
        while buf and buf[-1] == '':
            buf.pop()
        tokens[tok] = len(buf)
    return tokens


def json_line_counts(path):
    """Return {token: line_count} for translation JSON string values.

    Excludes `name_\\d+` tokens — these are Alliance/Empire name-string fragments
    concatenated at runtime, not dialog with voice cues.
    """
    d = json.loads(path.read_text(encoding='utf-8'))
    result = {}
    name_re = re.compile(r'^name_\d+$')
    for k, v in d.items():
        if k.startswith('_') or not isinstance(v, str):
            continue
        if name_re.match(k):
            continue
        # If value is empty string, count is 0; otherwise line count = 1 + \n count
        if v == '':
            result[k] = 0
        else:
            result[k] = v.count('\n') + 1
    return result


def check_race(race, base='.'):
    """Return (source_counts, json_counts, mismatches)."""
    root = Path(base)
    src = root / f'extracted/base/base/comm/{race}/{race}.txt'
    tgt = root / f'translations/{race}.zh-TW.json'
    if not src.exists():
        return None, None, f'source not found: {src}'
    if not tgt.exists():
        return None, None, f'translation not found: {tgt}'

    src_counts = parse_source(src)
    tgt_counts = json_line_counts(tgt)

    mismatches = []
    for tok in tgt_counts:
        if tok not in src_counts:
            mismatches.append((tok, 'MISSING_IN_SOURCE', 0, tgt_counts[tok]))
            continue
        if src_counts[tok] != tgt_counts[tok]:
            mismatches.append((tok, 'DIFF', src_counts[tok], tgt_counts[tok]))
    return src_counts, tgt_counts, mismatches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--race')
    args = parser.parse_args()

    if args.race:
        races = [args.race]
    else:
        # Enumerate translated race JSONs (exclude gamestrings/setupmenu/intro)
        tdir = Path('translations')
        races = []
        for p in sorted(tdir.glob('*.zh-TW.json')):
            r = p.stem.replace('.zh-TW', '')
            if r in ('gamestrings', 'setupmenu', 'intro'):
                continue
            # Only include races that have extracted comm sources
            if (Path('extracted/base/base/comm') / r / f'{r}.txt').exists():
                races.append(r)

    total_mismatch = 0
    print('=' * 64)
    print('Line-count alignment check (source .txt vs .zh-TW.json)')
    print('=' * 64)

    for r in races:
        src, tgt, m = check_race(r)
        if isinstance(m, str):
            print(f'  [SKIP] {r:12} {m}')
            continue
        n = len(m)
        total_mismatch += n
        status = 'PASS' if n == 0 else 'FAIL'
        print(f'  [{status}] {r:12} tokens={len(tgt):3d}  mismatches={n}')

        if n > 0 and args.verbose:
            for tok, kind, sc, tc in m[:30]:
                if kind == 'DIFF':
                    print(f'    [{tok}] src={sc} lines  tgt={tc} lines  (diff={tc-sc:+d})')
                else:
                    print(f'    [{tok}] {kind}')
            if n > 30:
                print(f'    ... 還有 {n-30} 個')

    print('=' * 64)
    print(f'總計不匹配 tokens: {total_mismatch}')
    print('=' * 64)

    if args.strict and total_mismatch:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
