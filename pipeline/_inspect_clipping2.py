"""Inspect reference Latin 'A' + CJK 苦 dimensions per font.

The engine renders each glyph at (baseline_y - HotSpot.y, x). Since HotSpot.y
depends on THAT glyph's PNG height, a glyph with PNG_h=15 (苦) draws its top
ONE ROW HIGHER than an 'A' with PNG_h=14 would draw.

Reveals whether CJK PNG height matches Latin PNG height per font.
"""
from pathlib import Path
from PIL import Image

FONTS_DIR = Path("zh-TW-addon/content/base/fonts")
FONTS = ["computer.fon", "pkunk.fon", "slylandro.fon", "yehat.fon",
         "vux.fon", "syreen.fon", "shofixti.fon", "utwig.fon", "urquan.fon"]

print(f"{'Font':<18} {'cell_h':>6} {'VA':>3} "
      f"{'A[wxh]':<8} {'苦[wxh]':<8}  {'A ink':<12} {'苦 ink':<12} "
      f"{'A top->line':>12} {'苦 top->line':>12}")
print("-" * 120)

for f in FONTS:
    fdir = FONTS_DIR / f
    if not fdir.exists():
        continue
    kerndat = (fdir / "kerndat.fnt").read_text(encoding="ascii").splitlines()[0].split()
    cell_h = int(kerndat[1])
    va = int(kerndat[4])
    # 'A' = U+0041
    a_png = fdir / "00041.png"
    # 苦 = U+82E6
    k_png = fdir / "082E6.png"
    if not a_png.exists() or not k_png.exists():
        continue
    a = Image.open(a_png).convert("L")
    k = Image.open(k_png).convert("L")
    a_bbox = a.getbbox()
    k_bbox = k.getbbox()

    # baseline is at PNG row (png_h - VA). PNG top row is at screen row baseline - (png_h - VA).
    # If we set baseline_screen_y = 0 for both, screen row = png_row - (png_h - VA).
    # PNG top (row 0) sits at screen row -(png_h - VA) = VA - png_h
    a_top_screen = va - a.height  # screen y of PNG row 0
    k_top_screen = va - k.height
    a_ink = f"[{a_bbox[1]},{a_bbox[3]}]" if a_bbox else "(blank)"
    k_ink = f"[{k_bbox[1]},{k_bbox[3]}]" if k_bbox else "(blank)"
    # Ink top's screen y (relative to baseline)
    a_ink_top_screen = a_top_screen + a_bbox[1] if a_bbox else None
    k_ink_top_screen = k_top_screen + k_bbox[1] if k_bbox else None

    print(f"{f:<18} {cell_h:>6} {va:>3} "
          f"{a.width}x{a.height:<5} {k.width}x{k.height:<5} "
          f"{a_ink:<12} {k_ink:<12} "
          f"{a_ink_top_screen:>12} {k_ink_top_screen:>12}")

# Positive `top->line` means ink is BELOW baseline (bad).
# Negative means ink is ABOVE baseline (normal).
# CJK ink_top_screen much MORE NEGATIVE than Latin = CJK ink extends higher above baseline
# = MORE LIKELY TO CLIP TOP of preceding line's text box.
