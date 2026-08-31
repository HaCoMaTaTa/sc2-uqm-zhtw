"""
zh-TW Android port · Thrust button icon candidates.

Render 5 button-mock previews so the user can visually compare emoji /
color / stylistic choices. Each mock uses the same circular button
outline the actual overlay uses (84 dp × 2.75 density ≈ 231 px), so
scale + legibility are representative.

Output: Q:\\Dos_G\\StarControl2\\Android\\_icon_candidates\\thrust_*.png
        + a stacked comparison sheet Q:\\...\\thrust_all_candidates.png
"""
from __future__ import annotations
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates")
OUT.mkdir(parents=True, exist_ok=True)

# The touch overlay uses 84 dp circle for the Thrust button. At Pixel 7
# density (2.75) that's ~231 px. Bump to 256 for crisp preview.
BUTTON_PX = 256


def load_font(size: int, cjk: bool = False, emoji: bool = False) -> ImageFont.FreeTypeFont | None:
    """
    Return a font that can render the requested glyph class.

    - `emoji=True` grabs Segoe UI Emoji (color-glyph capable).
    - `cjk=True` grabs 微軟正黑體 for CJK ideographs.
    - Otherwise a generic Segoe UI Symbol.
    Note: Windows fonts fall back on different subsets, so mixing CJK +
    emoji in the SAME `Text.draw` call is unreliable — callers should
    pick the font that fits their specific glyph.
    """
    if emoji:
        paths = [r"C:\Windows\Fonts\seguiemj.ttf"]
    elif cjk:
        paths = [r"C:\Windows\Fonts\msjhbd.ttc",
                 r"C:\Windows\Fonts\msjh.ttc",
                 r"C:\Windows\Fonts\simhei.ttf"]
    else:
        paths = [r"C:\Windows\Fonts\SegoeUISymbol.ttf",
                 r"C:\Windows\Fonts\segoeuib.ttf",
                 r"C:\Windows\Fonts\seguisb.ttf"]
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return None


def draw_button(label: str, bg: tuple[int, int, int, int],
                border: tuple[int, int, int, int],
                text_color: tuple[int, int, int] = (255, 255, 255),
                label_font_size: int = 100,
                label_dy: int = 0,
                font_kind: str = "emoji") -> Image.Image:
    """Circular button with 2 px border, label centered.

    `font_kind` picks the font family: "emoji", "cjk", or "symbol".
    """
    im = Image.new("RGBA", (BUTTON_PX, BUTTON_PX), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    inset = 4
    # Filled circle (background)
    d.ellipse((inset, inset, BUTTON_PX - inset, BUTTON_PX - inset), fill=bg)
    # Border ring — 6 px wide
    d.ellipse((inset, inset, BUTTON_PX - inset, BUTTON_PX - inset),
              outline=border, width=6)

    font = load_font(label_font_size,
                     cjk=(font_kind == "cjk"),
                     emoji=(font_kind == "emoji"))
    if font is not None:
        # Use font.getbbox for accurate centering across emoji + CJK glyphs.
        try:
            bbox = d.textbbox((0, 0), label, font=font, embedded_color=True)
        except TypeError:
            bbox = d.textbbox((0, 0), label, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (BUTTON_PX - w) // 2 - bbox[0]
        y = (BUTTON_PX - h) // 2 - bbox[1] + label_dy
        # embedded_color=True renders color emoji on PIL 9.5+.
        try:
            d.text((x, y), label, font=font, embedded_color=True,
                   fill=text_color)
        except TypeError:
            d.text((x, y), label, font=font, fill=text_color)
    return im


CANDIDATES = [
    # (id, label, bg, border, text_color, font_size, dy, font_kind, description)
    (
        "A_fire_emoji",
        "\U0001F525",  # 🔥
        (0x99, 0x55, 0x00, 0xAA),
        (0xFF, 0xAA, 0x22, 0xFF),
        (255, 255, 255),
        140, -6, "emoji",
        "🔥 火焰 emoji · 當前版本 · 溫暖橘 · 直觀 '點火' 意象",
    ),
    (
        "B_rocket_emoji",
        "\U0001F680",  # 🚀
        (0x22, 0x44, 0x77, 0xAA),
        (0x66, 0xAA, 0xFF, 0xFF),
        (255, 255, 255),
        130, -6, "emoji",
        "🚀 火箭 emoji · 冷藍科技感 · '推進器' 直白意象",
    ),
    (
        "C_lightning",
        "\u26A1",       # ⚡
        (0x66, 0x22, 0x88, 0xAA),
        (0xFF, 0xEE, 0x66, 0xFF),
        (255, 240, 100),
        150, 0, "emoji",
        "⚡ 閃電 · 紫底黃字 · '瞬間爆發力' 意象",
    ),
    (
        "D_filled_triangle",
        "\u25B2",       # ▲
        (0x22, 0x66, 0x33, 0xAA),
        (0x88, 0xFF, 0xAA, 0xFF),
        (200, 255, 220),
        150, -4, "symbol",
        "▲ 實心三角形 · 綠色 · 抽象化的火箭噴嘴/推進錐體",
    ),
    (
        "E_cjk_push",
        "\u63A8",       # 推
        (0x77, 0x33, 0x33, 0xAA),
        (0xFF, 0xAA, 0x88, 0xFF),
        (255, 240, 220),
        130, -6, "cjk",
        "推 中文字 · 磚紅底 · 保留 CJK 主題一致性 · '推進' 直白",
    ),
]


def main() -> None:
    # Render individual PNGs
    imgs = []
    for (name, label, bg, border, txt, fs, dy, font_kind, desc) in CANDIDATES:
        im = draw_button(label, bg, border, txt, fs, dy, font_kind)
        p = OUT / f"thrust_{name}.png"
        im.save(p, "PNG")
        print(f"  wrote {p.name}  ({label!r})  → {desc}")
        imgs.append((name, im, desc))

    # Comparison sheet: 5 buttons in a row + captions
    caption_font = load_font(20, cjk=True)  # CJK-capable for captions
    row_h = BUTTON_PX + 160
    row_w = BUTTON_PX * 5 + 60
    sheet = Image.new("RGB", (row_w, row_h), (30, 30, 40))
    d = ImageDraw.Draw(sheet)
    letters = ["A", "B", "C", "D", "E"]
    for i, ((_, im, desc), letter) in enumerate(zip(imgs, letters)):
        x = 12 + i * (BUTTON_PX + 8)
        y = 10
        sheet.paste(im, (x, y), im)
        # Letter label above button (large yellow) — use symbol font so
        # embedded_color doesn't fight the CJK font.
        letter_font = load_font(30)
        if letter_font:
            d.text((x + 8, y + 4), letter, fill=(255, 220, 100), font=letter_font)
        # Description below — split by " · " into short lines
        if caption_font:
            for j, line in enumerate(desc.split(" · ")[:5]):
                d.text((x + 4, y + BUTTON_PX + 8 + j * 24),
                       line, fill=(220, 220, 220), font=caption_font)

    sheet_path = OUT / "thrust_all_candidates.png"
    sheet.save(sheet_path, "PNG")
    print(f"\ncomparison sheet: {sheet_path}")


if __name__ == "__main__":
    main()
