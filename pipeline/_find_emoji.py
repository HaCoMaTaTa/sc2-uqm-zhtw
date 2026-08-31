import os, json
translations_dir = r'Q:\Dos_G\StarControl2\uqm-work\translations'
targets = ['\U0001f331', '\U0001f3a8', '\U0001f3ad', '\U0001f3af']

for root, dirs, files in os.walk(r'Q:\Dos_G\StarControl2\uqm-work'):
    # Skip huge directories
    if any(x in root for x in ['install', 'zh-TW-addon', '_stage', 'extracted', '__pycache__', '.git']):
        continue
    for f in files:
        if not (f.endswith('.json') or f.endswith('.txt')):
            continue
        p = os.path.join(root, f)
        try:
            with open(p, encoding='utf-8') as fp:
                content = fp.read()
        except Exception:
            continue
        for t in targets:
            if t in content:
                idx = content.index(t)
                surrounding = content[max(0,idx-30):idx+30]
                print(f'{p}: U+{ord(t):05X} {t!r}  ... {surrounding!r}')
