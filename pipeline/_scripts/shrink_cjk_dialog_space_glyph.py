"""Shrink the ASCII space glyph (0x20) in CJK-shadowed dialog fonts.

The default space glyph in dialog fonts like shofixti.fon is 5-6 px wide.
For CJK translations that use space-delimited chunks as word-wrap hints, this
creates visible ~12 px on-screen gaps between chunks. Users perceive these as
"random empty spaces" that hurt readability.

This script rewrites the shadow's 00020.png to be a narrower blank PNG
(default 2 px wide, matching most CJK space intuition of a hair-space).

Only applies to fonts listed in DIALOG_FONTS — leaves system fonts alone.
Applied AFTER rasterize_font.py in build_zh-TW.ps1.
"""

from PIL import Image
from pathlib import Path

SHADOW_ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\fonts")
DIALOG_FONTS = [
    # only fonts we rasterize CJK into and are used for alien dialog
    "shofixti.fon",
    "urquan.fon",
    "slylandro.fon",
    "computer.fon",
    "commander.fon",  # full-shadowed, uses computer.fon backing
    "player.fon",     # ditto
    "slides.fon",
    "slab.fon",
]

NEW_SPACE_WIDTH = 2  # px. 0 would break some layout; 1 too tight; 2 is safe.


def shrink_space(font_dir: Path):
    space = font_dir / "00020.png"
    if not space.exists():
        return None
    orig = Image.open(space)
    if orig.width <= NEW_SPACE_WIDTH:
        return f"{font_dir.name}: already narrow ({orig.width})"
    new = Image.new(orig.mode, (NEW_SPACE_WIDTH, orig.height), 0)
    new.save(space, "PNG", optimize=True)
    return f"{font_dir.name}: {orig.width}x{orig.height} -> {NEW_SPACE_WIDTH}x{orig.height}"


def main():
    for f in DIALOG_FONTS:
        d = SHADOW_ROOT / f
        if not d.is_dir():
            print(f"skip: {f} (not in shadow)")
            continue
        result = shrink_space(d)
        if result:
            print(result)


if __name__ == "__main__":
    main()
