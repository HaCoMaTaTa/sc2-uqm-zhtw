"""Inspect CJK glyph clipping in existing rasterized fonts.

For each font's 苦 (U+82E6) PNG:
  - PNG height
  - Ink top/bottom rows (bounding box)
  - Baseline row (= png_h - VertAlign from kerndat)
  - Cell top row (= baseline_row - (cell_h - VertAlign) + 1)
  - Ink ROWS ABOVE cell top (clipped by text-box)
"""
import sys
from pathlib import Path
from PIL import Image

FONTS_DIR = Path("zh-TW-addon/content/base/fonts")
CHAR_HEX = "082E6"  # 苦
FONTS_TO_CHECK = ["computer.fon", "pkunk.fon", "slylandro.fon", "yehat.fon",
                  "vux.fon", "syreen.fon", "shofixti.fon"]

print(f"{'Font':<20} {'cell_h':>6} {'VertAlign':>9} {'PNG_h':>5} "
      f"{'ink[top,bot]':<14} {'baseline':>8} {'cell_top':>8} {'ovhd':>4}")
print("-" * 100)
for font in FONTS_TO_CHECK:
    fdir = FONTS_DIR / font
    kerndat = (fdir / "kerndat.fnt").read_text(encoding="ascii").splitlines()[0].split()
    cell_h = int(kerndat[1])
    vert_align = int(kerndat[4])
    png = fdir / f"{CHAR_HEX}.png"
    if not png.exists():
        print(f"{font:<20} (no {CHAR_HEX}.png)")
        continue
    img = Image.open(png).convert("L")
    bbox = img.getbbox()
    if bbox is None:
        print(f"{font:<20} (blank PNG)")
        continue
    _, ink_top, _, ink_bot = bbox
    png_h = img.height
    baseline = png_h - vert_align
    # cell TOP row (above baseline): baseline_row - cell_h + 1 (line_height above baseline)
    # UQM uses cell_h as line_height; the text-box clips PNG at baseline_row - cell_h
    cell_top = baseline - cell_h
    overhead = max(0, cell_top - ink_top) if cell_top > ink_top else 0
    # ink rows ABOVE cell top → visually clipped
    print(f"{font:<20} {cell_h:>6} {vert_align:>9} {png_h:>5} "
          f"[{ink_top:>3},{ink_bot:>3}]        {baseline:>8} {cell_top:>8} {overhead:>4}")
