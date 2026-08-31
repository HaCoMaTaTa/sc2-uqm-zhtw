"""Crop rasterized preview into 4 tiles for viewing."""
from pathlib import Path
from PIL import Image

PNG = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.zh-TW.png")
OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")

im = Image.open(PNG)
w, h = im.size
print(f"orig {w}x{h}")

# 4 tiles: top-left, top-right, mid, legend
tiles = [
    ("tl",  0,     0,     w//2, h*40//100),
    ("tr",  w//2,  0,     w,    h*40//100),
    ("bl",  0,     h*40//100, w//2, h*75//100),
    ("br",  w//2,  h*40//100, w,    h*75//100),
    ("leg", 0,     h*75//100, w,    h),
]
for name, x0, y0, x1, y1 in tiles:
    tile = im.crop((x0, y0, x1, y1))
    tile.thumbnail((1400, 1400))
    out = OUT / f"preview_{name}.png"
    tile.save(out, optimize=True)
    print(f"  {out.name}: {tile.size}")
