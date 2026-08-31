"""
Install the chosen icon (composite E+A) into the Android APK resource
directories. Generates all 5 launcher-icon densities (mdpi 48×48 →
xxxhdpi 192×192) plus a Play Store 512×512 promo copy, both square
(ic_launcher.png) and round (ic_launcher_round.png).

Also replaces the adaptive-icon XML files so the Play Store's round /
squircle / teardrop launcher crops render the same composite (not the
compose-multiplatform template's default green sample).
"""
from __future__ import annotations
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageFilter

RES_ROOT = Path(
    r"Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\composeApp\src\androidMain\res"
)
SOURCE = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates\icon_G_pure_no_text.png")

DENSITIES = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}


def make_round(im: Image.Image) -> Image.Image:
    """Return a round-masked variant."""
    size = im.size[0]
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((0, 0, size - 1, size - 1), fill=255)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(im, (0, 0), mask)
    return result


def install_launcher_icons() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    print(f"source: {SOURCE} ({src.size})")

    for folder, size in DENSITIES.items():
        target_dir = RES_ROOT / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        # Square
        square = src.resize((size, size), Image.LANCZOS)
        square.save(target_dir / "ic_launcher.png", "PNG", optimize=True)

        # Round (transparent outside circle)
        round_im = make_round(square)
        round_im.save(target_dir / "ic_launcher_round.png", "PNG", optimize=True)

        print(f"  {folder}/  {size}x{size}  (square + round)")


def install_adaptive_icon() -> None:
    """
    Compose Multiplatform's default project ships adaptive-icon XML that
    references a vector drawable and a colour background — designed for
    the CM template's green sample icon. Override both layers so API 26+
    launchers show OUR composite, not a green blob.
    """
    # Layered adaptive icon in mipmap-anydpi-v26/ic_launcher.xml
    adaptive_xml = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
</adaptive-icon>
"""
    (RES_ROOT / "mipmap-anydpi-v26").mkdir(parents=True, exist_ok=True)
    (RES_ROOT / "mipmap-anydpi-v26" / "ic_launcher.xml").write_text(adaptive_xml)
    (RES_ROOT / "mipmap-anydpi-v26" / "ic_launcher_round.xml").write_text(adaptive_xml)
    print("wrote adaptive-icon XML (foreground + background)")

    # Background layer: dark blue starry field, no text
    src = Image.open(SOURCE).convert("RGBA")

    # Adaptive icon layers must be 432×432 with content in inner 288×288
    # safe zone (see https://developer.android.com/develop/ui/views/launch/icon_design_adaptive)
    ADAPT = 432
    for density_folder, base in [
        ("mipmap-mdpi", 108),
        ("mipmap-hdpi", 162),
        ("mipmap-xhdpi", 216),
        ("mipmap-xxhdpi", 324),
        ("mipmap-xxxhdpi", 432),
    ]:
        target_dir = RES_ROOT / density_folder
        # Background: just a dark blue nebula with stars (no CJK text, no
        # creature — those go on the foreground so Android launchers can
        # animate parallax between the two).
        bg = Image.new("RGBA", (base, base), (5, 10, 30, 255))
        d = ImageDraw.Draw(bg)
        import random
        random.seed(42)
        star_count = int(base * base / 900)
        for _ in range(star_count):
            x = random.randint(0, base - 1)
            y = random.randint(0, base - 1)
            b = random.randint(120, 255)
            r = random.choice([1, 1, 2])
            d.ellipse((x - r, y - r, x + r, y + r), fill=(b, b, b, 255))
        glow_layer = Image.new("RGBA", (base, base), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow_layer)
        gd.ellipse(
            (int(base * 0.15), int(base * 0.25),
             int(base * 0.85), int(base * 0.85)),
            fill=(30, 60, 140, 180),
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(int(base * 0.12)))
        bg = Image.alpha_composite(bg, glow_layer)
        bg.save(target_dir / "ic_launcher_background.png", "PNG", optimize=True)

        # Foreground: composite icon scaled to inner safe zone (66/108 = 61%)
        # of the total layer, transparent margin around.
        fg = Image.new("RGBA", (base, base), (0, 0, 0, 0))
        inner = int(base * 0.66)
        scaled = src.resize((inner, inner), Image.LANCZOS)
        offset = (base - inner) // 2
        fg.paste(scaled, (offset, offset), scaled)
        fg.save(target_dir / "ic_launcher_foreground.png", "PNG", optimize=True)

        print(f"  {density_folder}/ ic_launcher_background.png + ic_launcher_foreground.png ({base}x{base})")

    # Remove legacy vector foreground (drawable-v24/ic_launcher_foreground.xml) so
    # AGP doesn't merge the CM template's green diamond over our PNGs.
    for stale in [
        RES_ROOT / "drawable-v24" / "ic_launcher_foreground.xml",
        RES_ROOT / "drawable" / "ic_launcher_background.xml",
    ]:
        if stale.exists():
            stale.unlink()
            print(f"removed stale template: {stale.relative_to(RES_ROOT)}")


def make_play_store_promo() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    promo = src.resize((512, 512), Image.LANCZOS)
    promo_path = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates\playstore_512.png")
    promo.save(promo_path, "PNG", optimize=True)
    print(f"promo: {promo_path}")


if __name__ == "__main__":
    install_launcher_icons()
    install_adaptive_icon()
    make_play_store_promo()
    print("\nDone. Rebuild the APK to see the new icon.")
