"""Compare glyph alignments before/after rasterizer fix."""
import io
from PIL import Image
import sys

# Backup old computer.fon glyphs for comparison, then generate new versions
OLD_DIR = r'Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\_stage\zh-TW\shadow-content\base\fonts\commander.fon'
NEW_DIR = r'Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\fonts\computer.fon'

# Same target chars from earlier inspection
targets = [
    ('A', 0x41),
    ('.', 0x2E),
    ('警', 0x8B66),
    ('一', 0x4E00),
    ('人', 0x4EBA),
    ('中', 0x4E2D),
    ('─', 0x2500),
    ('—', 0x2014),
    ('…', 0x2026),
    ('！', 0xFF01),
    ('，', 0xFF0C),
]

def ink_range(path):
    import os
    if not os.path.exists(path):
        return None
    img = Image.open(path)
    if img.mode == '1':
        img = img.convert('L')
    if img.mode != 'L':
        img = img.convert('L')
    w, h = img.size
    from PIL import Image as _I
    pixels = list(img.getdata())
    rows_with_pixel = [y for y in range(h) if any(pixels[y*w + x] != 0 for x in range(w))]
    if not rows_with_pixel:
        return (w, h, None, None)
    return (w, h, rows_with_pixel[0], rows_with_pixel[-1])

print(f'{"char":<6} {"cp":<7} {"OLD (w,h,top,bot)":<24} {"NEW (w,h,top,bot)":<24}')
print('-' * 80)
import os
for label, cp in targets:
    fn = f'{cp:05x}.png'
    old_p = os.path.join(OLD_DIR, fn)
    new_p = os.path.join(NEW_DIR, fn)
    old_i = ink_range(old_p)
    new_i = ink_range(new_p)
    old_s = str(old_i) if old_i else 'missing'
    new_s = str(new_i) if new_i else 'missing'
    print(f'{label:<6} U+{cp:04X}  {old_s:<24} {new_s:<24}')
