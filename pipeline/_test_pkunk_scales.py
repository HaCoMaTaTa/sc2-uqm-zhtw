"""Test various cjk-scale for pkunk.fon with problem chars (我/普/族/首/高)."""
import subprocess
import shutil
import sys
from pathlib import Path
from PIL import Image

BASE = Path("extracted/base/base/fonts/pkunk.fon")
OUT_ROOT = Path("zh-TW-addon/_test_scales_pkunk")
SCALES = [0.90, 0.80, 0.75, 0.70]
CHARS = "苦首国我普族最高恩"
PROBE = [("A", "00041"), ("苦", "082E6"), ("我", "06211"),
         ("普", "0666E"), ("族", "065CF"), ("首", "09996"),
         ("高", "09AD8")]

# Reference Latin ink baseline
ref_img = Image.open(BASE / "00041.png").convert("L")
ref_bbox = ref_img.getbbox()
print(f"pkunk.fon reference A: {ref_img.size}, ink {ref_bbox}")
print()

for scale in SCALES:
    out = OUT_ROOT / f"{scale:.2f}" / "pkunk.fon"
    if out.exists():
        shutil.rmtree(out)
    cmd = [sys.executable, "rasterize_font.py",
           "--ref-font", str(BASE),
           "--ttf", r"C:\Windows\Fonts\NotoSansTC-VF.ttf",
           "--chars", CHARS,
           "--extra-padding", "0",
           "--cjk-scale", str(scale),
           "--out", str(out)]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"=== pkunk.fon @ scale={scale:.2f} ===")
    max_top_overhang = 0
    max_bot_overhang = 0
    for name, hexcp in PROBE:
        p = out / f"{hexcp}.png"
        if not p.exists():
            continue
        img = Image.open(p).convert("L")
        bbox = img.getbbox()
        if not bbox:
            continue
        _, top, _, bot = bbox
        top_overhang = max(0, ref_bbox[1] - top)  # CJK above Latin
        bot_overhang = max(0, bot - ref_bbox[3])  # CJK below Latin
        max_top_overhang = max(max_top_overhang, top_overhang)
        max_bot_overhang = max(max_bot_overhang, bot_overhang)
        marker = "❌" if (top_overhang or bot_overhang) else "✓"
        print(f"  {name} {img.width}x{img.height}, ink [{top:>2},{bot:>2}]  "
              f"top_over={top_overhang} bot_over={bot_overhang} {marker}")
    print(f"  MAX: top_overhang={max_top_overhang}, bot_overhang={max_bot_overhang}")
    print()
