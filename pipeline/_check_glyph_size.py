from PIL import Image
import os

font_dir = r'Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\_stage\zh-TW\shadow-content\base\fonts\commander.fon'
# Sample a few CJK glyphs
samples = ['05b57.png', '08b66.png', '0544a.png', '04f60.png', '0ff01.png', '0ff0c.png']
for s in samples:
    p = os.path.join(font_dir, s)
    if os.path.exists(p):
        img = Image.open(p)
        print(f'{s}: {img.size} (WxH)')

# Also check kerndat
kern = os.path.join(font_dir, 'kerndat.fnt')
with open(kern, 'r', encoding='ascii') as f:
    for line in f.readlines()[:3]:
        print(f'kerndat: {line!r}')
