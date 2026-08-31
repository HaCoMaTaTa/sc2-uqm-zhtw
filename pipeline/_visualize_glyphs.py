"""Print ASCII art of key glyphs to visually confirm alignment."""
from PIL import Image
import io
import zipfile

ADDON = r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm'
z = zipfile.ZipFile(ADDON)

samples = [
    ('A (Latin ref)', 0x41),
    ('. (period)', 0x2E),
    ('警 (full CJK)', 0x8B66),
    ('一 (one - flat)', 0x4E00),
    ('中 (middle)', 0x4E2D),
    ('─ (box dash)', 0x2500),
    ('… (ellipsis)', 0x2026),
    ('！ (FW ex)', 0xFF01),
    ('， (FW comma)', 0xFF0C),
    ('。 (CJK period)', 0x3002),
]

for label, cp in samples:
    name = f'zh-TW/shadow-content/base/fonts/commander.fon/{cp:05x}.png'
    try:
        data = z.read(name)
    except KeyError:
        print(f'{label}: MISSING')
        continue
    img = Image.open(io.BytesIO(data))
    if img.mode == '1':
        img = img.convert('L')
    if img.mode != 'L':
        img = img.convert('L')
    w, h = img.size
    print(f'{label} (U+{cp:04X}) {w}x{h}:')
    for y in range(h):
        row = ''.join('#' if img.getpixel((x, y)) > 128 else '.' for x in range(w))
        marker = '  <-- baseline' if y == 12 else ''
        print(f'  row {y:2d}: {row}{marker}')
    print()
