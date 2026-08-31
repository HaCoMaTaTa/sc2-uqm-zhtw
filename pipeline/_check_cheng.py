import json
with open(r'Q:\Dos_G\StarControl2\uqm-work\translations\_used_chars.txt', encoding='utf-8') as f:
    data = f.read()
print(f'撐 in _used_chars.txt: {"撐" in data}')

with open(r'Q:\Dos_G\StarControl2\uqm-work\translations\commander.zh-TW.json', encoding='utf-8') as f:
    cmd = json.load(f)
for k, v in cmd.items():
    if k.startswith('_'):
        continue
    if '撐' in v:
        for line in v.split('\n'):
            if '撐' in line:
                print(f'  in {k}: {line!r}')
