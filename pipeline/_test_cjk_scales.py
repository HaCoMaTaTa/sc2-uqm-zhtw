"""Test various cjk-scale values on computer.fon and pkunk.fon.

For each scale in [1.0, 0.90, 0.85, 0.80, 0.75], rasterize 苦 into a test
dir and report ink bounding box vs Latin 'A' ink.

Goal: find scale that makes CJK ink fit within Latin ink range vertically
(no top or bottom overhang).
"""
import subprocess
import shutil
import sys
from pathlib import Path
from PIL import Image

BASE = Path("extracted/base/base/fonts")
OUT_ROOT = Path("zh-TW-addon/_test_scales")
SCALES = [1.0, 0.90, 0.85, 0.80]
FONTS = ["computer.fon", "pkunk.fon", "slylandro.fon", "yehat.fon",
         "vux.fon", "syreen.fon", "shofixti.fon", "utwig.fon",
         "urquan.fon", "kohrah.fon", "spathi.fon", "mycon.fon",
         "orz.fon", "ilwrath.fon"]

def ink_bbox(path: Path):
    img = Image.open(path).convert("L")
    bbox = img.getbbox()
    return img.size, bbox

def rasterize(font: str, scale: float, out: Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    cmd = [
        sys.executable, "rasterize_font.py",
        "--ref-font", str(BASE / font),
        "--ttf", r"C:\Windows\Fonts\NotoSansTC-VF.ttf",
        "--chars", "苦首国中王高麗菜",
        "--extra-padding", "0",
        "--out", str(out),
    ]
    if scale != 1.0:
        cmd += ["--cjk-scale", str(scale)]
    subprocess.run(cmd, capture_output=True, text=True, check=True)

for font in FONTS:
    print(f"\n=== {font} ===")
    # Reference Latin 'A'
    ref_a = BASE / font / "00041.png"
    (w, h), a_box = ink_bbox(ref_a)
    print(f"  Latin A ref: {w}x{h}, ink {a_box}")
    for scale in SCALES:
        out = OUT_ROOT / f"scale_{scale:.2f}" / font
        rasterize(font, scale, out)
        # measure 苦
        k_png = out / "082E6.png"
        (w2, h2), k_box = ink_bbox(k_png)
        # compute overhang vs Latin ink
        overhang_top = max(0, a_box[1] - k_box[1])   # CJK ink starts above A ink
        overhang_bot = max(0, k_box[3] - a_box[3])   # CJK ink extends below A ink
        print(f"  scale={scale:.2f}: 苦 {w2}x{h2}, ink {k_box}"
              f"  overhang_top={overhang_top}  overhang_bot={overhang_bot}")
