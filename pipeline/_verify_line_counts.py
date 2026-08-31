"""Verify line count of each entry matches English original."""
import json
import re
from pathlib import Path

src = Path(r'Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt')
trans_path = Path(r'Q:\Dos_G\StarControl2\uqm-work\translations\commander.zh-TW.json')

text = src.read_text(encoding='utf-8')
trans = json.loads(trans_path.read_text(encoding='utf-8'))

mismatches = 0
matches = 0
for tok, val in trans.items():
    if tok.startswith('_'):
        continue
    m = re.search(rf'#\({tok}\)[^\n]*\n((?:(?!#\().*?\n)*)', text)
    if not m:
        print(f'  MISS  {tok}: not found in source')
        continue
    body = m.group(1).rstrip()
    src_lines = len([l for l in body.split('\n') if l.strip()])
    trans_lines = len([l for l in val.split('\n') if l.strip()])
    if src_lines != trans_lines:
        print(f'  BAD   {tok}: source={src_lines} trans={trans_lines}')
        mismatches += 1
    else:
        matches += 1

print()
print(f'== Line count check ==')
print(f'  Matches:   {matches}')
print(f'  Mismatches: {mismatches}')
