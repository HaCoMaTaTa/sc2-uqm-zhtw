"""Extract all untranslated tokens from commander.txt with their English text."""
import json
import re
from pathlib import Path

src_path = Path(r'Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt')
trans_path = Path(r'Q:\Dos_G\StarControl2\uqm-work\translations\commander.zh-TW.json')

src = src_path.read_text(encoding='utf-8')
trans = json.loads(trans_path.read_text(encoding='utf-8'))
translated_tokens = {k for k in trans if not k.startswith('_')}

# Find all tokens in source order
tokens = []
for m in re.finditer(r'#\(([A-Za-z0-9_]+)\)[^\n]*\n((?:(?!#\().*\n?)*)', src):
    tok = m.group(1)
    body = m.group(2).rstrip()
    lines = [l for l in body.split('\n') if l.strip()]
    tokens.append((tok, lines))

print(f'Total tokens in source: {len(tokens)}')
print(f'Already translated: {len(translated_tokens)}')
print()

untrans = [t for t in tokens if t[0] not in translated_tokens]
print(f'==== UNTRANSLATED TOKENS ({len(untrans)}) ====')
print()
for tok, lines in untrans:
    print(f'#({tok})')
    for i, l in enumerate(lines):
        print(f'  [{i}] {l}')
    print()
