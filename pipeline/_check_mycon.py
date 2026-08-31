import json

with open(r'Q:\Dos_G\StarControl2\uqm-work\translations\mycon.zh-TW.json', encoding='utf-8') as f:
    d = json.load(f)

# Find 深淵之子 (should be 深層幼體 per v0.7 canonical)
found = False
for k, v in d.items():
    if k == '_notes':
        continue
    if isinstance(v, str) and '深淵之子' in v:
        found = True
        print(f'=== {k} ===')
        print(v)
        print()

if not found:
    print('No 深淵之子 found in dialog tokens')

# Also check _notes for reference mentions
notes_hits = sum(1 for n in d.get('_notes', []) if '深淵之子' in n)
print(f'_notes references (canonical documentation): {notes_hits}')

# Wenyan check
wenyan = ['吾', '爾', '汝', '乃', '矣', '哉', '焉', '兒', '莫']
print()
print('=== Wenyan dialog hits ===')
for w in wenyan:
    total = 0
    for k, v in d.items():
        if k == '_notes' or not isinstance(v, str):
            continue
        total += v.count(w)
    if total > 0:
        print(f'{w}: {total}')
