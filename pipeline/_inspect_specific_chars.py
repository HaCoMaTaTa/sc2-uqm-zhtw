"""Inspect 我 (U+6211) vs 苦 (U+82E6) in pkunk.fon.

我 has an ascending diagonal stroke (top-right) that extends ABOVE the em-box
top of typical chars like 國 or 苦. If rasterize_font.py measures em based on
國 and crops to em, 我's ascender gets clipped in the source render.
"""
from pathlib import Path
from PIL import Image

FONTS = ["computer.fon", "pkunk.fon", "spathi.fon", "urquan.fon", "utwig.fon"]
CHARS = [
    ("A", "00041"),
    ("苦", "082E6"),
    ("我", "06211"),
    ("普", "0666E"),
    ("恩", "06069"),
    ("族", "0065B"),  # wrong; 族 is U+65CF
    ("首", "09996"),
]
# Fix 族
CHARS = [
    ("A", "00041"),
    ("苦", "082E6"),
    ("我", "06211"),
    ("普", "0666E"),
    ("恩", "06069"),
    ("族", "065CF"),
    ("首", "09996"),
    ("最", "06700"),
    ("高", "09AD8"),
]

BASE = Path("zh-TW-addon/content/base/fonts")

print(f"{'Font':<15} {'char':<3} {'PNG':<6} {'ink[t,b]':<10} {'ink_h':>5} {'top<0?':<8}")
print("-" * 60)
for font in FONTS:
    kerndat = (BASE / font / "kerndat.fnt").read_text(encoding="ascii").splitlines()[0].split()
    va = int(kerndat[4])
    print(f"--- {font} (VertAlign={va}) ---")
    for name, hexcp in CHARS:
        p = BASE / font / f"{hexcp}.png"
        if not p.exists():
            print(f"  {name} (0x{hexcp}) MISSING")
            continue
        img = Image.open(p).convert("L")
        bbox = img.getbbox()
        if bbox is None:
            print(f"  {name} blank")
            continue
        _, top, _, bot = bbox
        # baseline = png_h - VertAlign
        baseline = img.height - va
        print(f"  {name:<3} {img.width}x{img.height:<3} [{top:>2},{bot:>2}]   {bot-top:>3}  "
              f"top_to_base={top - baseline:>3}  bot_to_base={bot - baseline:>3}")
