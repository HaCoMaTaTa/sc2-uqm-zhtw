"""Inspect vertical alignment of key CJK/box-drawing chars in computer.fon."""
from PIL import Image
import os

FONT_DIR = r'Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\_stage\zh-TW\shadow-content\base\fonts\commander.fon'

# Show alpha column analysis (where pixels are)
def analyze(cp: int):
    p = os.path.join(FONT_DIR, f'{cp:05x}.png')
    if not os.path.exists(p):
        print(f'U+{cp:04X}: NOT FOUND')
        return
    img = Image.open(p)
    # get alpha channel (or the whole thing if greyscale/binary)
    if img.mode == '1':
        img = img.convert('L')
    if img.mode == 'L':
        pixels = list(img.getdata())
        w, h = img.size
        # find first & last row with any non-zero pixel
        rows_with_pixel = []
        for y in range(h):
            row = pixels[y*w:(y+1)*w]
            if any(p != 0 for p in row):
                rows_with_pixel.append(y)
        if rows_with_pixel:
            top, bot = rows_with_pixel[0], rows_with_pixel[-1]
            print(f'U+{cp:04X}: PNG={w}x{h}  ink_top={top}  ink_bot={bot}  (height {bot-top+1}px)')
        else:
            print(f'U+{cp:04X}: PNG={w}x{h}  BLANK')
    else:
        print(f'U+{cp:04X}: PNG={img.size} mode={img.mode}')

# Reference chars for baseline comparison
targets = [
    ('A', 0x41),
    ('.', 0x2E),
    ('警', 0x8B66),
    ('一', 0x4E00),  # ideographic "one"
    ('人', 0x4EBA),
    ('中', 0x4E2D),
    ('─', 0x2500),  # box drawings
    ('—', 0x2014),  # em dash
    ('…', 0x2026),
    ('！', 0xFF01),  # fullwidth exclamation
    ('，', 0xFF0C),
]

for label, cp in targets:
    analyze(cp)
