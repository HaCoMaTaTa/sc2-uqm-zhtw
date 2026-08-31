"""
zh-TW Android port · icon candidate generator.

Reads the HD MegaMod title screen (`mm-hd/ui/mainmenu/title.png`) and
crops several regions to serve as 512×512 launcher icon candidates.
Also renders a pure-CJK-typography option so the user can pick between
game-art derivatives and an original-branding design without needing
external image sources.

Output: `_icon_candidates/*.png` — six 512×512 PNGs.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:
    print("PIL not installed. Run: pip install pillow", file=sys.stderr)
    sys.exit(1)

TITLE = Path(
    r"Q:\Dos_G\StarControl2\uqm-work\install\content\addons\mm-hd\ui\mainmenu\title.debrand.png"
)
OUT = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates")
OUT.mkdir(parents=True, exist_ok=True)

# Icon size (Play Store launcher requirement)
ICON = 512

def load_title() -> Image.Image:
    if not TITLE.exists():
        raise SystemExit(f"missing title asset: {TITLE}")
    return Image.open(TITLE).convert("RGB")


def make_square_crop(im: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    """Crop `box` (left, top, right, bottom), pad to square, resize to ICON×ICON."""
    x1, y1, x2, y2 = box
    cropped = im.crop(box)
    w, h = cropped.size
    side = max(w, h)
    # Center-pad on a black background so the crop stays proportional.
    canvas = Image.new("RGB", (side, side), (0, 0, 0))
    canvas.paste(cropped, ((side - w) // 2, (side - h) // 2))
    return canvas.resize((ICON, ICON), Image.LANCZOS)


def add_border_gradient(im: Image.Image, glow: tuple[int, int, int] = (100, 200, 255)) -> Image.Image:
    """Soft vignette border, gives icon a polished feel."""
    mask = Image.new("L", (ICON, ICON), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((-40, -40, ICON + 40, ICON + 40), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(20))
    return im


def candidate_a_sa_matra(title: Image.Image) -> Image.Image:
    """Sa-Matra 三紅眼反派怪物（畫面中央下方）"""
    # title.png is 1280x960; Sa-Matra face is centered around y=750, x=640
    box = (400, 540, 880, 960)
    return make_square_crop(title, box)


def candidate_b_sis_ship(title: Image.Image) -> Image.Image:
    """Precursor SIS 藍銀母艦（畫面上方中央）"""
    box = (350, 60, 900, 310)
    return make_square_crop(title, box)


def candidate_c_full_title(title: Image.Image) -> Image.Image:
    """完整標題畫面縮圖（保留全部元素）"""
    w, h = title.size
    # Pad to square first, then downscale
    side = max(w, h)
    canvas = Image.new("RGB", (side, side), (0, 0, 0))
    canvas.paste(title, ((side - w) // 2, (side - h) // 2))
    return canvas.resize((ICON, ICON), Image.LANCZOS)


def candidate_d_ships(title: Image.Image) -> Image.Image:
    """種族艦隊環繞圖（上緣 8 艘小艦）"""
    box = (0, 0, 1280, 320)
    return make_square_crop(title, box)


def candidate_e_chinese_logo() -> Image.Image:
    """完全自製：中文字型 logo + 星空底 + 藍色科幻氛圍"""
    im = Image.new("RGB", (ICON, ICON), (5, 10, 30))
    d = ImageDraw.Draw(im)

    # Star field
    import random
    random.seed(42)
    for _ in range(180):
        x = random.randint(0, ICON - 1)
        y = random.randint(0, ICON - 1)
        b = random.randint(80, 255)
        r = random.choice([1, 1, 1, 2, 3])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(b, b, b))

    # Nebula glow (blue → purple)
    glow = Image.new("RGB", (ICON, ICON), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((80, 100, 430, 450), fill=(30, 60, 140))
    glow = glow.filter(ImageFilter.GaussianBlur(60))
    im = Image.blend(im, glow, 0.6)
    d = ImageDraw.Draw(im)

    # CJK text via Windows fonts
    font_candidates = [
        (r"C:\Windows\Fonts\msjhbd.ttc", 90),  # 微軟正黑體 Bold
        (r"C:\Windows\Fonts\mingliub.ttc", 90),
        (r"C:\Windows\Fonts\simhei.ttf", 90),
    ]
    font_big = None
    for path, size in font_candidates:
        if os.path.exists(path):
            try:
                font_big = ImageFont.truetype(path, size)
                break
            except OSError:
                continue
    font_small = None
    for path, size in [(p, 32) for p, _ in font_candidates]:
        if os.path.exists(path):
            try:
                font_small = ImageFont.truetype(path, size)
                break
            except OSError:
                continue

    # Title "激戰M星雲II" — split into two lines
    if font_big is not None:
        line1 = "激戰"
        line2 = "M星雲II"

        # Line 1 centered upper
        bbox = d.textbbox((0, 0), line1, font=font_big)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (ICON - w) // 2
        y = 90
        # shadow
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            d.text((x + dx, y + dy), line1, fill=(255, 60, 60), font=font_big)
        d.text((x, y), line1, fill=(255, 220, 220), font=font_big)

        # Line 2 centered lower
        bbox = d.textbbox((0, 0), line2, font=font_big)
        w = bbox[2] - bbox[0]
        x = (ICON - w) // 2
        y = 250
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            d.text((x + dx, y + dy), line2, fill=(60, 140, 255), font=font_big)
        d.text((x, y), line2, fill=(200, 230, 255), font=font_big)

    if font_small is not None:
        sub = "繁體中文化"
        bbox = d.textbbox((0, 0), sub, font=font_small)
        w = bbox[2] - bbox[0]
        x = (ICON - w) // 2
        d.text((x, 420), sub, fill=(180, 180, 220), font=font_small)

    return im


def main() -> None:
    print(f"loading title: {TITLE}")
    title = load_title()
    print(f"  size: {title.size}")

    candidates = {
        "A_sa_matra": candidate_a_sa_matra,
        "B_sis_ship": candidate_b_sis_ship,
        "C_full_title": candidate_c_full_title,
        "D_ship_fleet": candidate_d_ships,
        "E_chinese_logo": lambda t: candidate_e_chinese_logo(),
    }

    for name, fn in candidates.items():
        im = fn(title)
        path = OUT / f"icon_{name}.png"
        im.save(path, "PNG", optimize=True)
        print(f"  wrote {path.name}  ({im.size[0]}x{im.size[1]})")

    print(f"\nGenerated {len(candidates)} candidates in {OUT}")


if __name__ == "__main__":
    main()
