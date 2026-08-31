"""
Draw candidate icons for the direct-star-map button.

Each candidate is rendered on a 200×200 rounded square with a translucent
black background and white outline, matching the in-game overlay style
(same as ic_thrust and the existing 4 contextual buttons).
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont

CELL         = 300
ICON_PX      = 200
GLYPH_R      = 62
STROKE       = 18
STROKE_THIN  = 8
LABEL_H      = 60
PADDING      = 20
BG_COLOR     = (40, 40, 50)
FRAME_ALPHA  = 102     # translucent 66/255
GLYPH_COLOR  = (255, 255, 255)
FRAME_COLOR  = (255, 255, 255, FRAME_ALPHA)
BUTTON_BG    = (0, 0, 0, FRAME_ALPHA)


CANDIDATES = [
    ('A', 'Constellation (current)'),
    ('B', 'Folded paper map'),
    ('C', 'Location pin'),
    ('D', 'Globe / meridians'),
    ('E', 'Compass rose'),
    ('F', 'Map + route line'),
    ('G', 'Grid map (Material)'),
]

N = len(CANDIDATES)
TOTAL_W = CELL * N + PADDING * 2
TOTAL_H = CELL + LABEL_H + PADDING * 2

canvas = Image.new('RGB', (TOTAL_W, TOTAL_H), BG_COLOR)
try:
    font_label = ImageFont.truetype('arial.ttf', 18)
    font_header = ImageFont.truetype('arialbd.ttf', 16)
except OSError:
    font_label = ImageFont.load_default()
    font_header = font_label


def frame(draw, cx, cy):
    """Rounded square with translucent black bg + white outline."""
    # Draw on an RGBA overlay so alpha works.
    x0, y0 = cx - ICON_PX // 2, cy - ICON_PX // 2
    x1, y1 = cx + ICON_PX // 2, cy + ICON_PX // 2
    draw.rounded_rectangle((x0, y0, x1, y1), radius=20,
                           fill=(0, 0, 0), outline=(255, 255, 255), width=4)


def a_constellation(draw, cx, cy):
    r = GLYPH_R
    pts = [
        (cx - r,           cy + int(r * 0.3)),
        (cx - int(r * 0.45), cy - int(r * 0.5)),
        (cx,               cy + int(r * 0.1)),
        (cx + int(r * 0.45), cy - int(r * 0.5)),
        (cx + r,           cy + int(r * 0.3)),
    ]
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=GLYPH_COLOR, width=STROKE_THIN)
    for p in pts:
        dr = 8
        draw.ellipse((p[0] - dr, p[1] - dr, p[0] + dr, p[1] + dr),
                     fill=GLYPH_COLOR)


def b_folded_map(draw, cx, cy):
    """Three folded panels — the classic Google Maps 2010-2015 icon."""
    r = GLYPH_R
    # Three vertical panels, alternating tilt to simulate accordion fold.
    p1 = [
        (cx - r,             cy - int(r * 0.75)),
        (cx - int(r * 0.35), cy - int(r * 0.9)),
        (cx - int(r * 0.35), cy + int(r * 0.75)),
        (cx - r,             cy + int(r * 0.9)),
    ]
    p2 = [
        (cx - int(r * 0.35), cy - int(r * 0.9)),
        (cx + int(r * 0.35), cy - int(r * 0.75)),
        (cx + int(r * 0.35), cy + int(r * 0.9)),
        (cx - int(r * 0.35), cy + int(r * 0.75)),
    ]
    p3 = [
        (cx + int(r * 0.35), cy - int(r * 0.75)),
        (cx + r,             cy - int(r * 0.9)),
        (cx + r,             cy + int(r * 0.75)),
        (cx + int(r * 0.35), cy + int(r * 0.9)),
    ]
    for panel in (p1, p2, p3):
        draw.polygon(panel, outline=GLYPH_COLOR, width=STROKE_THIN)
    # A small squiggly route line
    route_pts = [
        (cx - int(r * 0.7), cy - int(r * 0.15)),
        (cx - int(r * 0.2), cy - int(r * 0.35)),
        (cx + int(r * 0.15), cy + int(r * 0.1)),
        (cx + int(r * 0.65), cy + int(r * 0.4)),
    ]
    for i in range(len(route_pts) - 1):
        draw.line([route_pts[i], route_pts[i + 1]], fill=GLYPH_COLOR,
                  width=STROKE_THIN)


def c_location_pin(draw, cx, cy):
    r = GLYPH_R
    head_cy = cy - int(r * 0.15)
    head_r = int(r * 0.65)
    # Round head
    draw.ellipse((cx - head_r, head_cy - head_r, cx + head_r, head_cy + head_r),
                 outline=GLYPH_COLOR, width=STROKE)
    # Sharp point at bottom — triangle
    tip_y = cy + int(r * 0.95)
    ratio = 0.60
    p1 = (cx - int(head_r * ratio), head_cy + int(head_r * ratio))
    p2 = (cx + int(head_r * ratio), head_cy + int(head_r * ratio))
    p3 = (cx, tip_y)
    draw.polygon([p1, p2, p3], fill=GLYPH_COLOR)
    # Center dot (fill circle in head)
    dr = int(head_r * 0.45)
    draw.ellipse((cx - dr, head_cy - dr, cx + dr, head_cy + dr),
                 fill=(0, 0, 0))
    draw.ellipse((cx - dr, head_cy - dr, cx + dr, head_cy + dr),
                 outline=GLYPH_COLOR, width=STROKE_THIN)


def d_globe(draw, cx, cy):
    r = GLYPH_R
    # Sphere
    draw.ellipse((cx - r, cy - r, cx + r, cy + r),
                 outline=GLYPH_COLOR, width=STROKE)
    # Equator
    draw.line([(cx - r, cy), (cx + r, cy)], fill=GLYPH_COLOR,
              width=STROKE_THIN)
    # Two latitude arcs (upper + lower)
    lat_offset = int(r * 0.55)
    lat_rx = int(r * 0.95)
    lat_ry = int(r * 0.18)
    # Upper latitude
    draw.arc((cx - lat_rx, cy - lat_offset - lat_ry,
              cx + lat_rx, cy - lat_offset + lat_ry),
             start=0, end=180, fill=GLYPH_COLOR, width=STROKE_THIN)
    # Lower latitude
    draw.arc((cx - lat_rx, cy + lat_offset - lat_ry,
              cx + lat_rx, cy + lat_offset + lat_ry),
             start=180, end=360, fill=GLYPH_COLOR, width=STROKE_THIN)
    # Central meridian
    mrx = int(r * 0.35)
    draw.ellipse((cx - mrx, cy - r, cx + mrx, cy + r),
                 outline=GLYPH_COLOR, width=STROKE_THIN)


def e_compass(draw, cx, cy):
    r = GLYPH_R
    # Outer ring
    draw.ellipse((cx - r, cy - r, cx + r, cy + r),
                 outline=GLYPH_COLOR, width=STROKE)
    # 4-point star (diamond)
    star = [
        (cx, cy - int(r * 0.85)),
        (cx + int(r * 0.28), cy),
        (cx, cy + int(r * 0.85)),
        (cx - int(r * 0.28), cy),
    ]
    draw.polygon(star, fill=GLYPH_COLOR)
    # Small N marker dot
    dr = 6
    draw.ellipse((cx - dr, cy - int(r * 0.85) - dr * 2 - 2,
                  cx + dr, cy - int(r * 0.85) - 2),
                 fill=GLYPH_COLOR)
    # Horizontal cross line (E-W)
    draw.line([(cx - int(r * 0.85), cy), (cx + int(r * 0.85), cy)],
              fill=GLYPH_COLOR, width=STROKE_THIN)


def f_map_route(draw, cx, cy):
    """Simple map card + a curved route line with start/end pins."""
    r = GLYPH_R
    # Rounded rectangle
    x0, y0 = cx - r, cy - int(r * 0.8)
    x1, y1 = cx + r, cy + int(r * 0.8)
    draw.rounded_rectangle((x0, y0, x1, y1), radius=8,
                           outline=GLYPH_COLOR, width=STROKE_THIN)
    # Fold line down the middle
    draw.line([(cx, y0), (cx, y1)], fill=GLYPH_COLOR, width=STROKE_THIN)
    # Curved route
    route = [
        (cx - int(r * 0.7), cy + int(r * 0.4)),
        (cx - int(r * 0.2), cy),
        (cx + int(r * 0.2), cy - int(r * 0.15)),
        (cx + int(r * 0.6), cy - int(r * 0.4)),
    ]
    for i in range(len(route) - 1):
        draw.line([route[i], route[i + 1]], fill=GLYPH_COLOR,
                  width=STROKE_THIN)
    # Start dot
    dr = 8
    p = route[0]
    draw.ellipse((p[0] - dr, p[1] - dr, p[0] + dr, p[1] + dr),
                 fill=GLYPH_COLOR)
    # End "pin"
    p = route[-1]
    draw.ellipse((p[0] - dr, p[1] - dr, p[0] + dr, p[1] + dr),
                 fill=GLYPH_COLOR)


def g_grid_map(draw, cx, cy):
    """Material-design 'map' icon: rectangular tile with subtle terrain."""
    r = GLYPH_R
    x0, y0 = cx - r, cy - int(r * 0.75)
    x1, y1 = cx + r, cy + int(r * 0.75)
    # Outer rounded rectangle
    draw.rounded_rectangle((x0, y0, x1, y1), radius=10,
                           outline=GLYPH_COLOR, width=STROKE)
    # 2 diagonal terrain lines (simplified topographic feel)
    draw.line([(x0 + 10, cy - int(r * 0.2)),
               (cx - int(r * 0.1), y0 + 15)],
              fill=GLYPH_COLOR, width=STROKE_THIN)
    draw.line([(cx - int(r * 0.1), y0 + 15),
               (cx + int(r * 0.5), cy + int(r * 0.3))],
              fill=GLYPH_COLOR, width=STROKE_THIN)
    # A single location dot on the map
    dot_r = 10
    draw.ellipse((cx + int(r * 0.35) - dot_r, cy + int(r * 0.2) - dot_r,
                  cx + int(r * 0.35) + dot_r, cy + int(r * 0.2) + dot_r),
                 fill=GLYPH_COLOR)


drawers = [a_constellation, b_folded_map, c_location_pin, d_globe,
           e_compass, f_map_route, g_grid_map]

# --------------------------------------------------------------------------
draw_ctx = ImageDraw.Draw(canvas)

# Header
draw_ctx.text((PADDING, 6),
              'Direct-star-map button — 7 icon candidates',
              fill=(220, 220, 220), font=font_header)

for i, (label, name) in enumerate(CANDIDATES):
    cx = PADDING + CELL * i + CELL // 2
    cy = PADDING + CELL // 2 + 20
    frame(draw_ctx, cx, cy)
    drawers[i](draw_ctx, cx, cy)
    # Label text
    txt = f'{label} · {name}'
    bbox = draw_ctx.textbbox((0, 0), txt, font=font_label)
    tw = bbox[2] - bbox[0]
    draw_ctx.text((cx - tw // 2, cy + ICON_PX // 2 + 12),
                  txt, fill=(255, 255, 255), font=font_label)

out = r'Q:\Dos_G\StarControl2\Android\_icon_candidates_starmap.png'
canvas.save(out, format='PNG')
print(f'Wrote {out}  ({canvas.size[0]}x{canvas.size[1]})')
