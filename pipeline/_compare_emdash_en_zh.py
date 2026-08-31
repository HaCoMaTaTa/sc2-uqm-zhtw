#!/usr/bin/env python3
"""Cross-reference: does English `--` in original text drive `——` in zh-TW?
Compares raw counts of `--` in _en_source/**/*.txt vs `——` in translations."""
import glob, os, re, sys, json

sys.stdout.reconfigure(encoding='utf-8')

en_root = r'Q:\Dos_G\StarControl2\uqm-work\_en_source'
zh_root = r'Q:\Dos_G\StarControl2\uqm-work\translations'

# Grab English source txt files (SUBTITLE sections)
en_files = {}
for p in glob.glob(os.path.join(en_root, '*', '*.txt')):
    race = os.path.basename(os.path.dirname(p))
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        en_files[race] = f.read()

# Match to zh files
races = sorted(en_files.keys())
print(f"{'race':<15} {'en_dashes(--)':>15} {'en_ellipsis(...)':>17} {'zh_em(——)':>12} {'zh_ellip(……)':>14}")
tot_en = 0
tot_zh_pair = 0
for race in races:
    en_text = en_files[race]
    # count `--` (double hyphen, not `---` triple)
    en_dd = len(re.findall(r'(?<!-)--(?!-)', en_text))
    en_ell = en_text.count('...')
    zh_path = os.path.join(zh_root, f'{race}.zh-TW.json')
    zh_em_pair = 0
    zh_ell = 0
    if os.path.exists(zh_path):
        try:
            with open(zh_path, 'r', encoding='utf-8') as f:
                d = json.load(f)
            for k, v in d.items():
                if k == '_notes' or not isinstance(v, str):
                    continue
                zh_em_pair += len(re.findall(r'——', v))
                zh_ell += v.count('……')
        except Exception:
            pass
    tot_en += en_dd
    tot_zh_pair += zh_em_pair
    print(f'{race:<15} {en_dd:>15} {en_ell:>17} {zh_em_pair:>12} {zh_ell:>14}')

print()
print(f'TOTAL en `--`  count: {tot_en}')
print(f'TOTAL zh `——`  count: {tot_zh_pair}')
print(f'Diff (zh added): {tot_zh_pair - tot_en}')
