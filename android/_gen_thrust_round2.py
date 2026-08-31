"""
zh-TW Android port · Thrust button icon candidates (round 2, hand-drawn styles).

Five more candidates rendered with PIL primitives instead of relying on
system emoji fonts. Styles:
  F. Pixel-art flame pillar (8-bit, chunky pixels, retro)
  G. 8-point compass rose / 八方星 (wuxia-inspired symmetry)
  H. Brushstroke 「衝」 (calligraphy motion character)
  I. UQM Precursor mothership silhouette going up (game-themed)
  J. Sa-Matra sunburst radiating outward (game villain vibe)

Output: Q:\\Dos_G\\StarControl2\\Android\\_icon_candidates\\thrust_[FGHIJ]_*.png
        + Q:\\...\\thrust_hand_drawn_candidates.png (comparison sheet)
"""
from __future__ import annotations
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates")
BUTTON_PX = 256


def load_cjk_font(size: int) -> ImageFont.FreeTypeFont | None:
    for path in (r"C:\Windows\Fonts\msjhbd.ttc",
                 r"C:\Windows\Fonts\kaiu.ttf",
                 r"C:\Windows\Fonts\simhei.ttf"):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return None


def base_button(bg: tuple, border: tuple) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGBA", (BUTTON_PX, BUTTON_PX), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    inset = 4
    d.ellipse((inset, inset, BUTTON_PX - inset, BUTTON_PX - inset), fill=bg)
    d.ellipse((inset, inset, BUTTON_PX - inset, BUTTON_PX - inset),
              outline=border, width=6)
    return im, d


def f_pixel_flame() -> Image.Image:
    """Chunky 8-bit style flame pillar with orange/yellow gradient."""
    im, d = base_button((0x55, 0x11, 0x00, 0xAA), (0xFF, 0x88, 0x22, 0xFF))
    # 16×16 pixel grid, cell = 12 px, centered
    cell = 12
    grid_size = 16
    grid_px = grid_size * cell
    offset = (BUTTON_PX - grid_px) // 2
    # Flame shape — bottom wide, top narrow, licks up
    # 1 = orange, 2 = yellow (hotter center), 3 = red (edges)
    flame = [
        "................",
        "................",
        "................",
        "................",
        ".......22.......",
        "......2222......",
        ".....221122.....",
        "....22111122....",
        "....22111122....",
        "...2211111122...",
        "...2211112122...",
        "..221111121122..",
        "..221211121122..",
        "..222111121222..",
        "...222212122....",
        "................",
    ]
    colors = {
        "1": (0xFF, 0xFF, 0x66, 0xFF),  # yellow (hottest core)
        "2": (0xFF, 0x88, 0x22, 0xFF),  # orange
        "3": (0xCC, 0x22, 0x00, 0xFF),  # red (edges)
    }
    for y, row in enumerate(flame):
        for x, ch in enumerate(row):
            if ch in colors:
                px = offset + x * cell
                py = offset + y * cell
                d.rectangle((px, py, px + cell - 1, py + cell - 1),
                            fill=colors[ch])
    return im


def g_compass_rose() -> Image.Image:
    """8-pointed compass rose (八方星) — wuxia symmetry."""
    im, d = base_button((0x22, 0x11, 0x44, 0xAA), (0xEE, 0xCC, 0x66, 0xFF))
    cx = cy = BUTTON_PX // 2
    outer = 90
    inner = 30
    # 8 alternating long/short points
    pts = []
    for i in range(16):
        angle = math.pi * 2 * i / 16 - math.pi / 2  # start at top
        r = outer if i % 2 == 0 else inner
        pts.append((cx + math.cos(angle) * r, cy + math.sin(angle) * r))
    # Fill
    d.polygon(pts, fill=(0xEE, 0xCC, 0x66, 0xFF))
    # Center dot
    d.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=(0xFF, 0xFF, 0xEE, 0xFF))
    # Inner cross highlight
    d.line((cx, cy - outer + 6, cx, cy + outer - 6),
           fill=(0xFF, 0xFF, 0xCC, 0xFF), width=2)
    d.line((cx - outer + 6, cy, cx + outer - 6, cy),
           fill=(0xFF, 0xFF, 0xCC, 0xFF), width=2)
    return im


def h_brushstroke_chong() -> Image.Image:
    """Chinese 「衝」 (charge/thrust) rendered in bold brush style."""
    im, d = base_button((0x11, 0x22, 0x33, 0xAA), (0xCC, 0xFF, 0xFF, 0xFF))
    font = load_cjk_font(200)
    if font is None:
        return im
    text = "衝"
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (BUTTON_PX - w) // 2 - bbox[0]
    y = (BUTTON_PX - h) // 2 - bbox[1] - 8
    # Shadow / brush thickening
    for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 0)]:
        d.text((x + dx, y + dy), text, font=font, fill=(0xCC, 0xFF, 0xFF, 0xFF))
    return im


def i_precursor_ship() -> Image.Image:
    """UQM Precursor mothership silhouette pointing up with a flame trail."""
    im, d = base_button((0x00, 0x11, 0x33, 0xAA), (0x66, 0xCC, 0xFF, 0xFF))
    cx = BUTTON_PX // 2
    # Ship body (rounded rectangle-ish)
    ship_top = 50
    ship_bot = 160
    # Nose cone
    d.polygon(
        [(cx, ship_top), (cx - 26, ship_top + 40), (cx + 26, ship_top + 40)],
        fill=(0xCC, 0xEE, 0xFF, 0xFF),
    )
    # Body
    d.rectangle((cx - 26, ship_top + 40, cx + 26, ship_bot),
                fill=(0xCC, 0xEE, 0xFF, 0xFF))
    # Cockpit dot
    d.ellipse((cx - 10, ship_top + 55, cx + 10, ship_top + 75),
              fill=(0x66, 0xAA, 0xEE, 0xFF))
    # Wings
    d.polygon(
        [(cx - 26, ship_top + 80), (cx - 65, ship_bot),
         (cx - 26, ship_bot)],
        fill=(0xAA, 0xDD, 0xFF, 0xFF),
    )
    d.polygon(
        [(cx + 26, ship_top + 80), (cx + 65, ship_bot),
         (cx + 26, ship_bot)],
        fill=(0xAA, 0xDD, 0xFF, 0xFF),
    )
    # Flame trail (2 tapering flames beneath)
    flame_layer = Image.new("RGBA", (BUTTON_PX, BUTTON_PX), (0, 0, 0, 0))
    fd = ImageDraw.Draw(flame_layer)
    fd.polygon(
        [(cx - 20, ship_bot), (cx - 8, ship_bot + 45),
         (cx, ship_bot + 30), (cx + 8, ship_bot + 45),
         (cx + 20, ship_bot)],
        fill=(0xFF, 0xAA, 0x22, 0xFF),
    )
    fd.polygon(
        [(cx - 12, ship_bot), (cx, ship_bot + 60), (cx + 12, ship_bot)],
        fill=(0xFF, 0xEE, 0x88, 0xFF),
    )
    flame_layer = flame_layer.filter(ImageFilter.GaussianBlur(1))
    im = Image.alpha_composite(im, flame_layer)
    return im


def j_sunburst() -> Image.Image:
    """Sa-Matra style sunburst — radiating rays from center."""
    im, d = base_button((0x11, 0x00, 0x22, 0xAA), (0xFF, 0x44, 0x66, 0xFF))
    cx = cy = BUTTON_PX // 2
    outer = 105
    inner_star = 30
    # 12 long rays
    ray_len = 100
    for i in range(12):
        angle = math.pi * 2 * i / 12
        x1 = cx + math.cos(angle) * inner_star
        y1 = cy + math.sin(angle) * inner_star
        x2 = cx + math.cos(angle) * (inner_star + ray_len - 20)
        y2 = cy + math.sin(angle) * (inner_star + ray_len - 20)
        # Tapered rays via polygon
        perp = angle + math.pi / 2
        w = 6
        d.polygon([
            (x1 + math.cos(perp) * w, y1 + math.sin(perp) * w),
            (x2, y2),
            (x1 - math.cos(perp) * w, y1 - math.sin(perp) * w),
        ], fill=(0xFF, 0x88, 0x44, 0xFF))
    # Central bright core with 3 red "eyes" hint
    d.ellipse((cx - 32, cy - 32, cx + 32, cy + 32),
              fill=(0xFF, 0xEE, 0xAA, 0xFF))
    # Three eye-dots (Sa-Matra ref)
    r = 8
    d.ellipse((cx - 20 - r, cy - 4 - r, cx - 20 + r, cy - 4 + r),
              fill=(0xCC, 0x11, 0x22, 0xFF))
    d.ellipse((cx + 20 - r, cy - 4 - r, cx + 20 + r, cy - 4 + r),
              fill=(0xCC, 0x11, 0x22, 0xFF))
    d.ellipse((cx - r, cy + 14 - r, cx + r, cy + 14 + r),
              fill=(0xCC, 0x11, 0x22, 0xFF))
    return im


CANDIDATES = [
    ("F_pixel_flame", "F", f_pixel_flame,
     "8-bit 像素風 · 分明黃紅色階 · 復古/UQM 原味"),
    ("G_compass_rose", "G", g_compass_rose,
     "八方星 (八方風) · 紫底金色 · 對稱華麗 · 全向推進"),
    ("H_brush_chong", "H", h_brushstroke_chong,
     "衝 中文字 · 深藍底青筆刷 · 武俠書法感"),
    ("I_precursor_ship", "I", i_precursor_ship,
     "Precursor 母艦剪影 · 火焰尾跡 · 遊戲主題貼合"),
    ("J_sunburst", "J", j_sunburst,
     "Sa-Matra 光芒放射 · 3 紅眼 · Ur-Quan 反派主題"),
]


def main() -> None:
    imgs = []
    for (name, letter, fn, desc) in CANDIDATES:
        im = fn()
        p = OUT / f"thrust_{name}.png"
        im.save(p, "PNG")
        print(f"  wrote {p.name}  → {desc}")
        imgs.append((letter, im, desc))

    # Sheet
    caption_font = load_cjk_font(20)
    row_h = BUTTON_PX + 170
    row_w = BUTTON_PX * 5 + 60
    sheet = Image.new("RGB", (row_w, row_h), (30, 30, 40))
    d = ImageDraw.Draw(sheet)
    letter_font = load_cjk_font(30)
    for i, (letter, im, desc) in enumerate(imgs):
        x = 12 + i * (BUTTON_PX + 8)
        y = 10
        sheet.paste(im, (x, y), im)
        if letter_font:
            d.text((x + 8, y + 4), letter, fill=(255, 220, 100), font=letter_font)
        if caption_font:
            for j, line in enumerate(desc.split(" · ")[:5]):
                d.text((x + 4, y + BUTTON_PX + 8 + j * 24),
                       line, fill=(220, 220, 220), font=caption_font)
    sheet_path = OUT / "thrust_hand_drawn_candidates.png"
    sheet.save(sheet_path, "PNG")
    print(f"\ncomparison sheet: {sheet_path}")


if __name__ == "__main__":
    main()
