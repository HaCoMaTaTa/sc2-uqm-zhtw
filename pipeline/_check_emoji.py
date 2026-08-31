import zipfile
z = zipfile.ZipFile(r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm')
targets = ['\U0001f331', '\U0001f3a8', '\U0001f3ad', '\U0001f3af']
found = False
for n in z.namelist():
    if not n.endswith('.txt'): continue
    if 'font' in n.lower(): continue
    try:
        data = z.read(n).decode('utf-8', errors='replace')
    except Exception:
        continue
    for t in targets:
        if t in data:
            print(f'{n}: contains U+{ord(t):05X}')
            found = True
if not found:
    print('No emoji found in any text file inside addon.')

# List all font PNGs with codepoint > 0xFFFF
print()
print('=== Suspicious font PNGs (codepoint > 0xFFFF) ===')
for n in z.namelist():
    if not n.endswith('.png'): continue
    if '.fon/' not in n and '.fon\\' not in n: continue
    fname = n.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
    stem = fname[:-4]
    try:
        cp = int(stem, 16)
    except ValueError:
        continue
    if cp > 0xFFFF:
        print(f'  {n}  (U+{cp:X})')
