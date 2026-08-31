"""Generate enlarged orbitbackground-018.png (grid measurement mask, PC mode)
and orbitbackground-021.png (grid background tile, PC mode) for CJK reports.

Original: both 5x5. New: 8x10 (adds 3 horizontal / 5 vertical padding) so
CJK 8x8 glyphs get horizontal breathing room and enough vertical space to
avoid cramping baselines.

- Frame 018: whole 5x5 solid green (00FF00 mask). Enlarge to 8x10 solid green
  because DrawFilledStamp uses this only as a mask filled with foreground color,
  and MakeReport uses GetFrameRect(frame 18) to derive x/y cell step size.
  Only the dimensions matter for step; but keeping it filled is safe.

- Frame 021: original 5x5 dark blue dot pattern; PC mode draws it as-is at each
  cell (via DrawStamp) so it visually tiles into a blue grid background.
  For CJK we rewrite it as a dark-grey 8x10 tile (RGB(30,30,30) opaque, with
  4 transparent corner pixels matching the original antialias corners) so:
    * The full report area becomes uniformly dark grey (better contrast
      against the white text from zh-TW patch 032 + zh-TW-hd fonteffect
      overrides).
    * The cell grid pattern effectively disappears -- neighbouring tiles
      blend into a solid dark-grey backdrop.
  If you need a subtle grid line, adjust CORNER_ALPHA below.
"""

from PIL import Image
from pathlib import Path
import shutil

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work")
SRC_DIR = ROOT / "extracted" / "base" / "base" / "nav"
DST_DIR = ROOT / "zh-TW-addon" / "content" / "base" / "nav"

CELL_W, CELL_H = 8, 10

# zh-TW patch 032: dark-grey backdrop for lander discovery report cells.
BG_COLOR = (30, 30, 30, 255)          # opaque dark grey
CORNER = (0, 0, 0, 0)                 # fully transparent corner pixel

DST_DIR.mkdir(parents=True, exist_ok=True)

# --- Frame 018 (green mask, used for cell step size measurement) ---
# Just fill an 8x10 canvas with the original green mask color.
src18 = Image.open(SRC_DIR / "orbitbackground-018.png").convert("RGBA")
mask_color = src18.getpixel((2, 2))  # sample center pixel
new18 = Image.new("RGBA", (CELL_W, CELL_H), mask_color)
new18.save(DST_DIR / "orbitbackground-018.png")
print(f"018: {src18.size} -> {new18.size}, color={mask_color}")

# --- Frame 021 (PC-mode grid background tile) ---
# Dark-grey 8x10 tile with transparent corners (mimics original antialias
# corners of the 5x5 blue dot -- keeps a subtle rounded feel when tiles meet).
new21 = Image.new("RGBA", (CELL_W, CELL_H), BG_COLOR)
new21.putpixel((0, 0), CORNER)
new21.putpixel((CELL_W - 1, 0), CORNER)
new21.putpixel((0, CELL_H - 1), CORNER)
new21.putpixel((CELL_W - 1, CELL_H - 1), CORNER)
new21.save(DST_DIR / "orbitbackground-021.png")
print(f"021: {(CELL_W, CELL_H)} dark grey RGB{BG_COLOR[:3]} + 4 alpha corners")

# --- Copy the .ani file so the addon lookup resolves in the same directory ---
# (Otherwise game might load base .ani which references PNG relatively -- our
# override PNGs might not be found. Safer to include a matching .ani.)
src_ani = SRC_DIR / "orbitbackground.ani"
dst_ani = DST_DIR / "orbitbackground.ani"
shutil.copyfile(src_ani, dst_ani)
print(f"copied {src_ani.name}")

# We also need to copy the OTHER PNGs so the .ani references still resolve
# from the addon dir. Copy all frames.
copied = 0
for src_png in SRC_DIR.glob("orbitbackground-*.png"):
    dst_png = DST_DIR / src_png.name
    if src_png.name in ("orbitbackground-018.png", "orbitbackground-021.png"):
        continue  # already written our overrides
    shutil.copyfile(src_png, dst_png)
    copied += 1
print(f"copied {copied} other frames")
