import os
import zipfile

TEXT = '警告！身分不明星艦！\n我是地球奴隸行星星際基地指揮官海斯。\n我方超波通訊，訊號極弱\n情況危急，能量核心已耗盡\n掃描儀與深空雷達皆失效\n無法辨識爾方艦艇。\n爾等是否為預定之階層補給船？\n重複，爾等是否為補給船？'

chars = set(TEXT) - {'\n'}
print(f'{len(chars)} unique chars in ARE_YOU_SUPPLY_SHIP Chinese text')

z = zipfile.ZipFile(r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm')
fonts_pngs = {}
for n in z.namelist():
    if '/commander.fon/' not in n: continue
    if not n.endswith('.png'): continue
    fname = n.rsplit('/', 1)[-1]
    stem = fname[:-4]
    try:
        cp = int(stem, 16)
        fonts_pngs[cp] = n
    except ValueError:
        pass

missing = []
for ch in sorted(chars, key=ord):
    cp = ord(ch)
    if cp not in fonts_pngs:
        missing.append((cp, ch))
        print(f'MISSING: U+{cp:05X} {ch!r}')
    else:
        pass  # Present

if not missing:
    print(f'All {len(chars)} chars have PNGs in commander.fon.')

# Also verify each PNG isn't corrupt/zero-byte
print()
print('=== Sizes of critical PNGs ===')
for ch in sorted(chars, key=ord):
    cp = ord(ch)
    if cp in fonts_pngs:
        info = z.getinfo(fonts_pngs[cp])
        if info.file_size < 50:
            print(f'  SMALL: U+{cp:05X} {ch!r}  {info.file_size} bytes')
