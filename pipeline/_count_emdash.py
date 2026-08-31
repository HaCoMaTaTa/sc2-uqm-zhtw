#!/usr/bin/env python3
"""One-shot analysis: em-dash (U+2014) usage in zh-TW translations."""
import json, glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

translations = glob.glob(r'Q:\Dos_G\StarControl2\uqm-work\translations\*.zh-TW.json')
total_em = 0
total_double_em = 0
total_single_em = 0
per_file = []

for p in translations:
    fname = os.path.basename(p)
    if fname == 'gamestrings.zh-TW.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        continue
    em = 0
    dem = 0
    sem = 0
    for k, v in d.items():
        if k == '_notes':
            continue
        if not isinstance(v, str):
            continue
        em += v.count('\u2014')
        dem += len(re.findall(r'\u2014\u2014', v))
        sem += len(re.findall(r'(?<!\u2014)\u2014(?!\u2014)', v))
    if em > 0:
        per_file.append((fname, em, dem, sem))
    total_em += em
    total_double_em += dem
    total_single_em += sem

per_file.sort(key=lambda x: -x[1])

FILE_H = 'file'
EM_H = 'em'
PAIRS_H = 'pairs'
SINGLE_H = 'single'

print('=== em-dash (U+2014) usage across translations/*.zh-TW.json ===')
print(f'TOTAL em-dash chars: {total_em}')
print(f'  double pairs: {total_double_em}  (= {total_double_em*2} chars)')
print(f'  isolated single: {total_single_em} chars')
print(f'  leftover/odd: {total_em - total_double_em*2 - total_single_em}')
print()
print(f'{FILE_H:<35} {EM_H:>6} {PAIRS_H:>6} {SINGLE_H:>6}')
for f, e, d, s in per_file[:30]:
    print(f'{f:<35} {e:>6} {d:>6} {s:>6}')
