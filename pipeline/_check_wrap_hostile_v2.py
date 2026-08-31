"""Tightened wrap-hostile scanner — based on empirical vux bugs.

Confirmed bug patterns:
  BUG_A: 4+ same suspect char (~/wave/em-dash/box-draw) run  (vux LIKE_BECAUSE ~~~~)
  BUG_B: Compound scream: dash-run(2+) + fw-exclaim(2+) + fw-paren-latin
         (vux FOOL_AIEE1 / TRUTH: ──！！！（AIEEE!!!）)

Everything else (single `（Betelgeuse）`, single `——`, etc.) is presumed safe
based on shipped examples that work in-game.

Usage: python _check_wrap_hostile_v2.py [--strict]
"""
import argparse, json, re, sys
from pathlib import Path

# BUG_A patterns
BUG_A_PATTS = [
    (re.compile(r'\uff5e{4,}'),  'HIGH', 'BUG_A 4+ fullwidth tilde ~'),
    (re.compile(r'\u301c{4,}'),  'HIGH', 'BUG_A 4+ wave dash <>'),
    (re.compile(r'\u2014{4,}'),  'HIGH', 'BUG_A 4+ em-dash --'),
    (re.compile(r'\u2500{4,}'),  'HIGH', 'BUG_A 4+ box-draw --'),
    (re.compile(r'\u2026{4,}'),  'HIGH', 'BUG_A 4+ ellipsis ...'),
]

# BUG_B compound scream: dash-run(2+) + strong-punct-run(2+) + fw-paren-with-latin
BUG_B_PATT = re.compile(
    r'[\u2014\u2500]{2,}'          # 2+ dashes (em or box)
    r'[\uff01\uff1f]{2,}'          # 2+ FW ! or ?
    r'\uff08[A-Za-z0-9!? ]+\uff09'  # FW paren wrapping ASCII/punct
)

# BUG_B2 variant: FW-latin-paren followed by trailing ellipsis "）……" 
BUG_B2_PATT = re.compile(r'\uff08[A-Za-z0-9!? ]+\uff09\u2026{2,}')

def scan_file(path):
    d = json.loads(path.read_text(encoding='utf-8'))
    hits = []
    for key, val in d.items():
        if key.startswith('_') or not isinstance(val, str):
            continue
        for line_no, line in enumerate(val.split('\n'), 1):
            findings = []
            for patt, sev, lbl in BUG_A_PATTS:
                if patt.search(line):
                    findings.append((sev, lbl))
            if BUG_B_PATT.search(line):
                findings.append(('HIGH', 'BUG_B compound scream (dash + punct + fw-latin-paren)'))
            if BUG_B2_PATT.search(line):
                findings.append(('HIGH', 'BUG_B2 fw-latin-paren + trailing ellipsis (--...)  ---)'))
            if findings:
                hits.append((key, line_no, line, findings))
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--race')
    args = ap.parse_args()
    root = Path('translations')
    files = [root / f'{args.race}.zh-TW.json'] if args.race else sorted(root.rglob('*.zh-TW.json'))
    files = [f for f in files if f.exists() and f.stem != 'gamestrings.zh-TW']
    total = 0
    print('='*72)
    print('Wrap-hostile scan v2 (tightened; empirical bug patterns only)')
    print('='*72)
    for f in files:
        hits = scan_file(f)
        race = f.stem.replace('.zh-TW','')
        status = 'FAIL' if hits else 'PASS'
        print(f'  [{status}] {race:14} HIGH-hits: {len(hits)}')
        for key, ln, line, findings in hits:
            for sev, lbl in findings:
                print(f'      [{sev}] {key} L{ln}: {lbl}')
                print(f'        txt: {line[:120]}')
        total += len(hits)
    print('='*72)
    print(f'Total HIGH lines: {total}')
    print('='*72)
    if args.strict and total > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
