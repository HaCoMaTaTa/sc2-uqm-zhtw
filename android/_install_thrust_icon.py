"""
zh-TW Android port · install the chosen Thrust button icon (option I —
Precursor mothership + flame trail) into the APK's drawable resources.

Generates one PNG at 216 px (xxhdpi, matches the 84 dp Thrust button
scaled by 2.75 density with a bit of headroom), plus mdpi/hdpi/xhdpi/
xxxhdpi copies. Compose loads whichever matches the device density.

Also updates the source generator's output name so it lands at the
Android res directory path Compose expects.
"""
from __future__ import annotations
from pathlib import Path

from PIL import Image

RES_ROOT = Path(
    r"Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\composeApp\src\androidMain\res"
)
SOURCE = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates\thrust_I_precursor_ship.png")

# Compose drawable density buckets. Base is xxhdpi @ 216 (dp × 2.75 rounded
# to a nice square). Others are scaled proportionally.
DENSITIES = {
    "drawable-mdpi":     84,     # 1.0×
    "drawable-hdpi":    126,     # 1.5×
    "drawable-xhdpi":   168,     # 2.0×
    "drawable-xxhdpi":  252,     # 3.0× (nominal for Pixel 7)
    "drawable-xxxhdpi": 336,     # 4.0×
}


def main() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    print(f"source: {SOURCE.name}  ({src.size})")
    for folder, size in DENSITIES.items():
        target_dir = RES_ROOT / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        scaled = src.resize((size, size), Image.LANCZOS)
        out = target_dir / "ic_thrust.png"
        scaled.save(out, "PNG", optimize=True)
        print(f"  {folder}/ic_thrust.png  {size}x{size}")


if __name__ == "__main__":
    main()
