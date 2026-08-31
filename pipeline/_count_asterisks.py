#!/usr/bin/env python3
"""Count asterisk usage across shipped translations."""
import json, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob(r'Q:\Dos_G\StarControl2\uqm-work\translations\*.zh-TW.json')
per = []
total_pair = 0
total_star = 0
for p in files:
    name = os.path.basename(p)
    if name == 'gamestrings.zh-TW.json':
        continue
    if '.pre-' in name or '.v3' in name or '.partial' in name:
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        continue
    stars = 0
    pairs = 0
    for k, v in d.items():
        if k == '_notes' or not isinstance(v, str):
            continue
        stars += v.count('*')
        pairs += len(re.findall(r'\*\*', v))
    if stars > 0:
        per.append((name, stars, pairs))
    total_star += stars
    total_pair += pairs

per.sort(key=lambda x: -x[1])

H_FILE = 'file'
H_STARS = 'stars'
H_PAIRS = '** pairs'

print('=== ALL translations: * (asterisk) counts ===')
print(f'{H_FILE:<35} {H_STARS:>6} {H_PAIRS:>10}')
for f, s, p in per[:25]:
    print(f'{f:<35} {s:>6} {p:>10}')
print()
print(f'TOTAL raw * chars: {total_star}')
print(f'TOTAL ** pair matches: {total_pair}  (= {total_pair * 2} chars)')
print(f'ORPHAN unpaired *: {total_star - total_pair * 2}')
