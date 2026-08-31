"""
Composite E+A icon: dark starry nebula background + CJK title text
+ Sa-Matra creature face as centerpiece.
"""
from pathlib import Path
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

TITLE = Path(
    r"Q:\Dos_G\StarControl2\uqm-work\install\content\addons\mm-hd\ui\mainmenu\title.debrand.png"
)
OUT = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates")
ICON = 512


def build_starry_bg() -> Image.Image:
    im = Image.new("RGB", (ICON, ICON), (5, 10, 30))
    d = ImageDraw.Draw(im)
    random.seed(42)
    for _ in range(220):
        x = random.randint(0, ICON - 1)
        y = random.randint(0, ICON - 1)
        b = random.randint(80, 255)
        r = random.choice([1, 1, 1, 2, 3])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(b, b, b))
    # Nebula glow
    glow = Image.new("RGB", (ICON, ICON), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((90, 130, 430, 430), fill=(30, 60, 140))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    return Image.blend(im, glow, 0.55)


def load_font(size: int) -> ImageFont.FreeTypeFont | None:
    for path in (
        r"C:\Windows\Fonts\msjhbd.ttc",
        r"C:\Windows\Fonts\mingliub.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
    ):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
    return None


def sa_matra_transparent() -> Image.Image:
    """Sa-Matra face with black background alpha-cut to transparent."""
    title = Image.open(TITLE).convert("RGBA")
    face = title.crop((400, 540, 880, 960))  # 480 wide x 420 tall
    # Cheap chroma-key: pixels darker than a threshold become transparent
    px = face.load()
    for y in range(face.height):
        for x in range(face.width):
            r, g, b, _ = px[x, y]
            # Keep bright pixels; fade near-black to alpha
            brightness = (r + g + b) / 3
            if brightness < 15:
                px[x, y] = (0, 0, 0, 0)
            elif brightness < 40:
                alpha = int((brightness - 15) / 25 * 200)
                px[x, y] = (r, g, b, alpha)
    return face


def build_composite() -> Image.Image:
    bg = build_starry_bg()
    result = bg.convert("RGBA")

    # Sa-Matra face — square-crop the tall crop and downscale to ~360×360
    face = sa_matra_transparent()
    fw, fh = face.size
    side = max(fw, fh)
    # Center within a square canvas
    face_square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    face_square.paste(face, ((side - fw) // 2, (side - fh) // 2), face)
    face_scaled = face_square.resize((360, 360), Image.LANCZOS)
    # Position: centered vertically slightly below center
    fx = (ICON - 360) // 2
    fy = 140
    result.paste(face_scaled, (fx, fy), face_scaled)

    # Text overlay
    d = ImageDraw.Draw(result)
    title_font = load_font(72)
    if title_font is not None:
        text = "激戰M星雲II"
        bbox = d.textbbox((0, 0), text, font=title_font)
        w = bbox[2] - bbox[0]
        x = (ICON - w) // 2
        y = 30
        # Red glowing shadow
        for dx, dy in [(-2, -1), (2, -1), (-2, 1), (2, 1), (0, -2), (0, 2)]:
            d.text((x + dx, y + dy), text, fill=(200, 40, 40), font=title_font)
        d.text((x, y), text, fill=(255, 240, 240), font=title_font)

    sub_font = load_font(30)
    if sub_font is not None:
        sub = "繁體中文化 · HD MegaMod"
        bbox = d.textbbox((0, 0), sub, font=sub_font)
        w = bbox[2] - bbox[0]
        x = (ICON - w) // 2
        y = ICON - 60
        for dx, dy in [(-1, 0), (1, 0)]:
            d.text((x + dx, y + dy), sub, fill=(60, 100, 200), font=sub_font)
        d.text((x, y), sub, fill=(200, 220, 255), font=sub_font)

    return result.convert("RGB")


def main() -> None:
    im = build_composite()
    path = OUT / "icon_F_composite_E_plus_A.png"
    im.save(path, "PNG", optimize=True)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
