"""Crop the map into 6 tiles for visual inspection of race sphere labels."""
from pathlib import Path
from PIL import Image

IMG = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.png")
OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")

im = Image.open(IMG)
w, h = im.size
print(f"orig {w}x{h}")

# Map area only (skip legend below y=3100)
map_h = 3100
# 3 columns x 2 rows of the map body
cols, rows = 3, 2
cw = w // cols
rh = map_h // rows
for r in range(rows):
    for c in range(cols):
        x0, y0 = c * cw, r * rh
        x1, y1 = min(x0 + cw + 100, w), min(y0 + rh + 100, map_h)
        crop = im.crop((x0, y0, x1, y1))
        # Downscale for viewing
        crop.thumbnail((1200, 1200))
        f = OUT / f"tile_r{r}c{c}_x{x0}-{x1}_y{y0}-{y1}.png"
        crop.save(f)
        print(f"  {f.name}")
