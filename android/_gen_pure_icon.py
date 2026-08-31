"""
zh-TW Android port · pure-image icon (no CJK text overlay).

Composite the Sa-Matra creature face on top of the starry nebula
background. NO title text — the launcher already renders the app_name
under the icon.
"""
from __future__ import annotations
import os
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

TITLE = Path(
    r"Q:\Dos_G\StarControl2\uqm-work\install\content\addons\mm-hd\ui\mainmenu\title.debrand.png"
)
OUT = Path(r"Q:\Dos_G\StarControl2\Android\_icon_candidates")
ICON = 512


def build_starry_bg() -> Image.Image:
    im = Image.new("RGB", (ICON, ICON), (5, 10, 30))
    d = ImageDraw.Draw(im)
    random.seed(42)
    for _ in range(240):
        x = random.randint(0, ICON - 1)
        y = random.randint(0, ICON - 1)
        b = random.randint(80, 255)
        r = random.choice([1, 1, 1, 2, 3])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(b, b, b))
    # Nebula glow — deeper + centered so the creature stands out
    glow = Image.new("RGB", (ICON, ICON), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((60, 60, ICON - 60, ICON - 60), fill=(35, 55, 130))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    return Image.blend(im, glow, 0.6)


def sa_matra_transparent() -> Image.Image:
    """Sa-Matra face with black background alpha-cut + soft radial fade
    so the crop edges blend into whatever background we composite onto,
    instead of showing a hard rectangle."""
    title = Image.open(TITLE).convert("RGBA")
    face = title.crop((400, 540, 880, 960))  # 480w × 420h
    px = face.load()
    for y in range(face.height):
        for x in range(face.width):
            r, g, b, _ = px[x, y]
            brightness = (r + g + b) / 3
            if brightness < 15:
                px[x, y] = (0, 0, 0, 0)
            elif brightness < 40:
                alpha = int((brightness - 15) / 25 * 200)
                px[x, y] = (r, g, b, alpha)

    # Radial fade: circle centered on the crop, alpha=255 at center →
    # alpha=0 at radius. Multiplies with existing alpha so already-
    # transparent pixels stay transparent.
    w, h = face.size
    cx, cy = w // 2, h // 2
    inner_r = min(w, h) * 0.38   # fully opaque within this radius
    outer_r = min(w, h) * 0.60   # fully transparent past this radius
    for y in range(h):
        for x in range(w):
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            if dist <= inner_r:
                factor = 1.0
            elif dist >= outer_r:
                factor = 0.0
            else:
                factor = 1.0 - (dist - inner_r) / (outer_r - inner_r)
            r, g, b, a = px[x, y]
            px[x, y] = (r, g, b, int(a * factor))
    return face


def build_pure_icon() -> Image.Image:
    """Starry background + Sa-Matra face, centered, NO text."""
    bg = build_starry_bg()
    result = bg.convert("RGBA")

    # Center the creature slightly higher than geometric center so the
    # tentacles (bottom of the face) don't crowd the icon's bottom edge
    # once launchers apply their circular/squircle mask.
    face = sa_matra_transparent()
    fw, fh = face.size
    side = max(fw, fh)
    face_square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    face_square.paste(face, ((side - fw) // 2, (side - fh) // 2), face)

    # Scale up — no text competing for space now, so make the creature
    # the hero of the icon. 420×420 fits comfortably in the 66%-of-108
    # adaptive-icon safe zone (66% of ~636 canvas = 420).
    scaled = face_square.resize((420, 420), Image.LANCZOS)
    fx = (ICON - 420) // 2
    fy = (ICON - 420) // 2 - 20  # nudge up by 20 px
    result.paste(scaled, (fx, fy), scaled)

    return result.convert("RGB")


def main() -> None:
    im = build_pure_icon()
    path = OUT / "icon_G_pure_no_text.png"
    im.save(path, "PNG", optimize=True)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
