# -*- coding: utf-8 -*-
"""Wrap-hostile character sequence check (v1.0.11).

Blocks the class of engine wrap-bug seen in vux.LIKE_BECAUSE — 4+ consecutive
fullwidth tilde U+FF5E (or wave dash U+301C) cause getLineWithinWidth() to
overflow character-by-character into a vertical column.

Currently HIGH-severity only (`~` >= 4). MED-severity findings (repeated `!`,
`?`, etc.) are reported but do not fail --strict.

Usage: python _check_wrap_hostile.py [--strict] [--verbose] [--race NAME]
"""
import argparse, json, re, sys
from pathlib import Path

# (char, min-run, severity, label)
CHECKS = [
    ('\uff5e', 4, 'HIGH', 'fullwidth tilde ~'),
    ('\u301c', 4, 'HIGH', 'wave dash <>'),
    ('\uff01', 6, 'MED',  'fullwidth ! excessive'),
    ('\uff1f', 6, 'MED',  'fullwidth ? excessive'),
    ('\u3002', 5, 'MED',  'fullwidth . excessive'),
    ('\uff0a', 4, 'MED',  'fullwidth *'),
    ('\uff1d', 4, 'MED',  'fullwidth ='),
    ('\uff3f', 4, 'MED',  'fullwidth _'),
    ('\u3000', 3, 'LOW',  'ideographic space run'),
]

def scan_file(path):
    d = json.loads(path.read_text(encoding='utf-8'))
    hits = []
    for key, val in d.items():
        if key.startswith('_') or not isinstance(val, str):
            continue
        for ch, threshold, sev, lbl in CHECKS:
            for m in re.finditer(re.escape(ch) + f'{{{threshold},}}', val):
                cs, ce = max(0, m.start()-25), min(len(val), m.end()+25)
                ctx = val[cs:ce].replace('\n', '\\n')
                hits.append((sev, key, len(m.group()), ch, ord(ch), lbl, ctx))
    return hits

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true',
                        help='exit 1 on any HIGH severity finding')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--race', help='scan one race JSON (name)')
    args = parser.parse_args()

    tdir = Path('translations')
    if args.race:
        files = sorted(tdir.rglob(f'{args.race}.zh-TW.json'))
    else:
        files = sorted(tdir.rglob('*.zh-TW.json'))
        files = [f for f in files if f.stem != 'gamestrings.zh-TW']

    total_high = 0
    total_med = 0
    total_low = 0
    print('=' * 72)
    print('Wrap-hostile character sequence check')
    print('=' * 72)

    for path in files:
        if not path.exists():
            continue
        hits = scan_file(path)
        highs = [h for h in hits if h[0] == 'HIGH']
        meds = [h for h in hits if h[0] == 'MED']
        lows = [h for h in hits if h[0] == 'LOW']
        race = path.stem.replace('.zh-TW', '')
        status = 'FAIL' if highs else 'PASS'
        marker = f'  [{status}] {race:14} HIGH={len(highs)} MED={len(meds)} LOW={len(lows)}'
        print(marker)
        total_high += len(highs); total_med += len(meds); total_low += len(lows)

        if (highs or args.verbose) and (highs or meds):
            for sev, key, n, ch, o, lbl, ctx in (highs + (meds if args.verbose else [])):
                print(f'      [{sev}] [{key}] {n}x U+{o:04X} {lbl}')
                print(f'        ctx: ...{ctx}...')

    print('=' * 72)
    print(f'Total: HIGH={total_high}  MED={total_med}  LOW={total_low}')
    print('=' * 72)

    if args.strict and total_high > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
