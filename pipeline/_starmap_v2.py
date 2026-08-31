"""
v2: Direct pixel-editing rebuild.
- Load Starmap.png with OpenCV
- Build unified mask of all English text regions (OCR + sphere areas + legend)
- Inpaint with cv2.INPAINT_TELEA → English pixels vanish, background stars/nebula preserved
- Convert to Pillow, draw Chinese with Noto Sans TC directly on pixels
- Save Starmap.zh-TW.png

Advantages over v1 SVG approach:
  ✓ No black rectangles — background remains natural
  ✓ No svglib/librsvg font matching pain
  ✓ Precise pixel-level control of every label
"""

import json
import re
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# =============================================================================
# Paths
# =============================================================================
IMG_SRC   = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.png")
OCR_JSON  = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_ocr_multipass.json")
IMG_OUT   = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.zh-TW.png")
INPAINTED = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_inpainted.png")
MASK_OUT  = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_mask.png")
REPORT    = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_v2_report.txt")

FONT_TTF  = Path(r"C:\Windows\Fonts\NotoSansTC-VF.ttf")   # Traditional Chinese
FONT_ALT  = Path(r"C:\Windows\Fonts\msjhbd.ttc")           # Microsoft JhengHei Bold (fallback)

IMG_W, IMG_H = 3200, 4258

# =============================================================================
# Translation dictionary (comprehensive)
# =============================================================================

CONSTELLATIONS = {
    "andromedae":"仙女座","antilae":"唧筒座","antliae":"唧筒座","apodis":"天燕座",
    "aquarii":"寶瓶座","aquilae":"天鷹座","arae":"天壇座","arietis":"白羊座",
    "aurigae":"御夫座","bootis":"牧夫座","caeli":"雕具座","camelopardalis":"鹿豹座",
    "cancri":"巨蟹座","capricorni":"摩羯座","carinae":"船底座","cassiopeiae":"仙后座",
    "centauri":"半人馬座","cephei":"仙王座","ceti":"鯨魚座","chameleonis":"蝘蜓座",
    "chamaeleonis":"蝘蜓座","circini":"圓規座","columbae":"天鴿座","comae":"后髮座",
    "coronae":"冕座","corvi":"烏鴉座","crateris":"巨爵座","crucis":"南十字座",
    "cygni":"天鵝座","cygnus":"天鵝座","delphini":"海豚座","doradus":"劍魚座",
    "draconis":"天龍座","equulei":"小馬座","eridani":"波江座","fornacis":"天爐座",
    "geminorum":"雙子座","gruis":"天鶴座","herculis":"武仙座","horologii":"時鐘座",
    "hydrae":"長蛇座","hydri":"水蛇座","indi":"印第安座","lacertae":"蝎虎座",
    "leonis":"獅子座","leporis":"天兔座","librae":"天秤座","lupi":"豺狼座",
    "lyncis":"天貓座","lyrae":"天琴座","mensae":"山案座","microscopii":"顯微鏡座",
    "monocerotis":"麒麟座","muscae":"蒼蠅座","normae":"矩尺座","octantis":"南極座",
    "ophiuchi":"蛇夫座","orionis":"獵戶座","pavonis":"孔雀座","pegasi":"飛馬座",
    "persei":"英仙座","phoenicis":"鳳凰座","pictoris":"繪架座","piscium":"雙魚座",
    "piscis":"南魚座","pyxidis":"羅盤座","puppis":"船尾座","reticuli":"網罟座",
    "sagitarii":"人馬座","sagittarii":"人馬座","sagittae":"天箭座","sculptoris":"玉夫座",
    "scorpii":"天蠍座","scuti":"盾牌座","serpentis":"巨蛇座","sextantis":"六分儀座",
    "tauri":"金牛座","telescopii":"望遠鏡座","trianguli":"三角座","tucanae":"杜鵑座",
    "ursae":"熊座","velorum":"船帆座","virginis":"室女座","volantis":"飛魚座",
    "vulpeculae":"狐狸座",
}

NAMED_STARS = {
    "sol":"太陽（Sol）","sirius":"天狼星","vega":"織女星","betelgeuse":"參宿四",
    "procyon":"南河三","arcturus":"大角星","rigel":"參宿七","antares":"心宿二",
    "aldebaran":"畢宿五","canopus":"老人星","fomalhaut":"北落師門","capella":"五車二",
    "regulus":"軒轅十四","deneb":"天津四","pollux":"北河三","altair":"河鼓二",
    "mira":"芻藁增二","menkar":"天囷一","hyades":"畢宿星團","achernar":"水委一",
    "bellatrix":"參宿五","algol":"大陵五","alcor":"開陽增一","mizar":"開陽",
    "wolf":"沃夫星","luyten":"呂坦星","lalande":"拉朗德星","krueger":"克魯格星",
    "groombridge":"葛倫布利吉","lacaille":"拉卡伊星","giclas":"吉克拉斯",
    "klystron":"克利斯壯","chandrasekhar":"錢卓卡","mersenne":"梅森","zeeman":"日曼",
    "vela":"微拉","cerenkov":"切連科夫","kepler":"克卜勒","copernicus":"哥白尼",
    "maksutov":"馬克蘇托夫","hyperion":"海柏利昂","arianni":"阿里安尼","brahe":"第谷",
    "raynet":"雷奈特","saurus":"薩魯斯","metis":"梅蒂斯","olber":"歐柏",
    "lentilis":"蘭提利斯","vitalis":"維塔利斯","hyginus":"海吉努斯","almagest":"至大論",
    "gorno":"戈爾諾","organon":"歐加農","ptolemae":"托勒密","squidi":"斯奎第",
    "illuminati":"光明會","lipi":"利皮",
}

LOOKUP = {**CONSTELLATIONS, **NAMED_STARS}

# OCR misread fixes → canonical dict key
OCR_FIXES = {
    "horolggii":"horologii","camblopardalis":"camelopardalis","culptoris":"sculptoris",
    "krueg":"krueger","carin":"carinae","colu":"columbae","centau":"centauri",
    "gentauri":"centauri","iclas":"giclas","cru":"crucis","crugis":"crucis",
    "sag":"sagittarii","mmmrnmhrm":None,"'arietis":"arietis","ntis":"sextantis",
    "huminati":"illuminati","+canopus":"canopus","ucanae":"tucanae","votantis":"volantis",
    "vota":"volantis","aldebar":"aldebaran","olf":"wolf","alta":"altair","mizal":"mizar",
    "ibrae":"librae","lacerta":"lacertae","crate":"crateris","mages":"almagest",
    "camelo":"camelopardalis","chameleoni":"chameleonis","phoenici":"phoenicis",
    "reticul":"reticuli","sextan":"sextantis","tucana":"tucanae","aquari":"aquarii",
    "hyad":"hyades",
    # sphere labels — hardcoded, so skip OCR fragments
    "umgal":None,"mycon":None,"pkunk":None,
    # noise
    "hla":None,"ho":None,"el":None,"en":None,"op":None,
}

# =============================================================================
# Hand-placed labels
# =============================================================================

# OCR-missed constellation labels: (dict_key, cx, cy) — cx,cy = TEXT BASELINE-LEFT anchor
MANUAL_LABELS = [
    ("squidi",      686, 1810),
    ("gruis",       800, 1910),
    ("herculis",    560, 1940),
    ("capricorni",  830, 1520),   # left of ZOQ-FOT-PIK area
    ("serpentis",  1435, 2975),
    ("scuti",      1710, 2905),
    ("columbae",    400, 2525),
    ("cru",        1652, 1160),
    ("lipi",       1769,  460),
    ("mira",       1246, 2417),
]

# Race sphere labels: (name, cx, cy, w_hint, h_hint, color_rgb, fontsize)
# cx,cy = CENTER of the original English curved arc label
# Sphere circles: (cx, cy, radius, color_rgb, line_width) — estimated from image
# Used to redraw ring outline after inpaint erases parts of the arc.
SPHERE_CIRCLES = [
    # cx    cy    r    color             lw
    ( 880,  720, 440, ( 95,221,221), 5),   # THRADDASH teal
    (2340,  390, 195, (255,144, 64), 4),   # SUPOX orange
    (2620,  390, 185, (136,187,238), 4),   # UTWIG light blue
    (2050, 1180, 790, (200,200,200), 5),   # KOHR-AH grey (outer massive)
    (2050, 1180, 700, ( 51,255, 51), 5),   # UR-QUAN green (second-outer)
    ( 830, 1290, 290, (176,144,224), 5),   # UMGAH purple
    ( 160, 3110, 250, (102,170,255), 5),   # PKUNK blue
    (1750, 3260, 280, (136,204,238), 5),   # YEHAT light blue
    (1600, 2610, 225, ( 80,120,255), 5),   # VUX blue
    (2050, 2220, 225, (255,136,204), 5),   # MYCON pink
    ( 380, 2400, 280, (255, 60,204), 5),   # ILWRATH magenta
    (1400, 2280, 155, (221, 68,221), 4),   # ORZ magenta
    (2620, 2900, 155, (255, 60, 60), 4),   # DRUUGE red
    ( 890, 1980, 250, (255,144, 40), 5),   # SPATHI orange
    ( 150, 1210, 155, ( 90,170,255), 4),   # ARILOU small blue
    (1350, 1500, 100, (255, 60, 60), 4),   # ZOQ-FOT-PIK red trio
]

# Race sphere Chinese labels: (name, cx, cy, w_hint, h_hint, color_rgb, fontsize)
# cx,cy = position where Chinese label center should sit
SPHERE_ANCHORS = [
    # name        cx    cy   mw   mh  color             fs
    ("撻伐族",     945,  310, 500, 100, (95, 221, 221), 62),   # THRADDASH teal
    ("蘇菩族",    2280,  200, 260,  90, (255,144, 64), 46),   # SUPOX orange
    ("憂特族",    2620,  220, 280,  90, (136,187,238), 54),   # UTWIG light blue
    ("烏寬柯亞",  2150,  380, 340,  90, (200,200,200), 48),   # KOHR-AH grey outer
    ("烏寬族",    2050,  475, 260,  90, ( 51,255, 51), 54),   # UR-QUAN green
    ("陰嘎族",     680, 1055, 340, 100, (176,144,224), 58),   # UMGAH purple
    ("普恩族",     220, 2860, 260,  90, (102,170,255), 50),   # PKUNK blue
    ("翼哈特族",  1400, 3050, 300,  90, (136,204,238), 50),   # YEHAT light blue
    ("VUX",      1595, 2445, 200,  90, ( 80,120,255), 62),   # VUX blue
    ("麥孔族",    2050, 2065, 340, 100, (255,136,204), 62),   # MYCON pink
    ("蛛狂族",     480, 2145, 340,  90, (255, 60,204), 58),   # ILWRATH magenta
    ("歐茲族",    1417, 2178, 200,  80, (221, 68,221), 46),   # ORZ magenta
    ("毒賈族",    2560, 2810, 280,  90, (255, 60, 60), 58),   # DRUUGE red
    ("史怕族",     825, 1735, 300,  90, (255,144, 40), 58),   # SPATHI orange
    ("阿麗露",     190, 1085, 240,  75, ( 90,170,255), 42),   # ARILOU small blue
    ("佐-佛-皮", 1350, 1620, 260,  75, (255, 60, 60), 40),   # ZOQ-FOT-PIK below circle
]

# Additional sphere-area text erasure zones — big enough to fully cover curved English
SPHERE_ERASE_ZONES = [
    # (x, y, w, h) — padded rectangle around sphere curved-English label
    ( 620,  180, 620, 240),   # THRADDASH
    (2000,   80, 600, 240),   # SUPOX
    (2280,  100, 640, 240),   # UTWIG
    (1830,  260, 620, 260),   # KOHR-AH
    (1760,  360, 560, 280),   # UR-QUAN
    ( 350,  920, 700, 260),   # UMGAH
    (  10, 2620, 580, 400),   # PKUNK — extended up (curve above ring)
    (1100, 2700, 720, 500),   # YEHAT — extended up (curved above ring)
    (1340, 2280, 500, 400),   # VUX — extended up+down
    (1700, 1900, 620, 300),   # MYCON
    ( 100, 1900, 720, 500),   # ILWRATH — full arc coverage top-right
    (1200, 2060, 400, 240),   # ORZ
    (2280, 2560, 640, 400),   # DRUUGE — extended right and up
    ( 520, 1600, 600, 260),   # SPATHI
    (   0,  980, 460, 220),   # ARILOU
    (1080, 1360, 500, 300),   # ZOQ-FOT-PIK
    (2870, 3200, 350,  70),   # QuasiSpace Map mini-title
]

# =============================================================================
# Legend translations
# =============================================================================

LEGEND_ITEMS = [
    ("1",  "地球、星際基地、史怕族在冥王星"),
    ("2",  "翼哈特族母星"),
    ("3",  "普恩族母星"),
    ("4",  "VUX 母星"),
    ("5",  "麥孔族母星"),
    ("6",  "姆姆族＆晶智族母星"),
    ("7",  "歐茲族母星"),
    ("8",  "毒賈族母星"),
    ("9",  "蛛狂族母星"),
    ("10", "史怕族母星"),
    ("11", "塞蓮族母星"),
    ("12", "佐-佛-皮母星"),
    ("13", "陰嘎族母星、會話寵"),
    ("14", "撻伐族母星"),
    ("15", "憂特族母星"),
    ("16", "蘇菩族母星"),
    ("17", "斯萊族母星"),
    ("18", "修烈士族母星"),
    ("19", "恩澤伐特（您的母星）"),
    ("20", "薩瑪特拉"),
    ("21", "烏寬扭曲艙"),
    ("22", "太陽裝置"),
    ("23", "澤克斯上將＆修烈士族少女們"),
    ("24", "澤克斯的獸"),
    ("25", "麥孔卵夾（三處）"),
    ("26", "安卓辛族遺跡"),
    ("27", "塔洛盾"),
    ("28", "塞蓮艦隊庫"),
    ("29", "布維族廣播器"),
    ("30", "水螺旋"),
    ("31", "憂特族炸彈"),
    ("32", "阿麗露母星（於準空間中）"),
]

LEGEND_BULLETS = [
    ("彩虹星球位置",             (255,170,255)),
    ("準空間傳送門出口（見地圖）",  ( 51,255, 51)),
]

# =============================================================================
# Helpers
# =============================================================================

def normalize_ocr(t):
    t = t.strip().lower()
    t = re.sub(r"[.,;:!?'\"()\[\]{}\-\u2018\u2019]+$", "", t)
    t = re.sub(r"^[.,;:!?'\"()\[\]{}\-\u2018\u2019]+", "", t)
    return t

def load_ocr_matches():
    data = json.loads(OCR_JSON.read_text(encoding="utf-8"))
    matches = []
    for r in data:
        if r["conf"] < 40:
            continue
        raw = r["text"]
        key = normalize_ocr(raw)
        if key in OCR_FIXES:
            fx = OCR_FIXES[key]
            if fx is None:
                continue
            key = fx
        if len(key) < 2 or re.fullmatch(r"\d+", key):
            continue
        if r["y"] > 3200:
            continue
        zh = LOOKUP.get(key)
        if not zh:
            continue
        matches.append({"key": key, "zh": zh,
                        "x": r["x"], "y": r["y"], "w": r["w"], "h": r["h"]})
    # Add manual overrides (fixed w/h)
    for key, x, y in MANUAL_LABELS:
        zh = LOOKUP.get(key)
        if not zh:
            continue
        if any(m["key"] == key and abs(m["x"]-x)<80 for m in matches):
            continue
        matches.append({"key": key, "zh": zh, "x": x, "y": y, "w": 140, "h": 32})
    return matches

# =============================================================================
# Step 1: Build inpaint mask
# =============================================================================

def build_mask(matches, img_bgr):
    """Build inpaint mask combining:
    - OCR bboxes (dilated) — precise text location for straight labels
    - Sphere areas: use connected-component analysis to find only TEXT-shaped
      pixels (filters out ring arcs, star icons, grid lines).
    - Legend area (bottom): full rectangle since we redraw it entirely.
    """
    mask = np.zeros((IMG_H, IMG_W), dtype=np.uint8)

    # ---- OCR text: dilated rects (precise straight-label positions) ----
    for m in matches:
        x, y, w, h = m["x"], m["y"], m["w"], m["h"]
        pad_x = 24   # generous — catches trailing letters ("s", "r", "ae", etc.)
        pad_y = 12
        cv2.rectangle(mask,
                      (max(0, x - pad_x), max(0, y - pad_y)),
                      (min(IMG_W, x + w + pad_x), min(IMG_H, y + h + pad_y)),
                      255, thickness=-1)

    # ---- Sphere curved labels ----
    # Within each sphere zone, mask ALL colored (non-black) pixels.
    # NOTE: we use MAX(B,G,R) instead of grayscale because pure-blue pixels
    # (like PKUNK's (255,0,0)) have grayscale ~29, below any reasonable text
    # threshold. Max-channel correctly identifies any coloured text.
    max_channel = img_bgr.max(axis=2)  # per-pixel max across BGR
    bright_all = (max_channel > 50).astype(np.uint8) * 255

    zone_mask = np.zeros_like(bright_all)
    for zx, zy, zw, zh in SPHERE_ERASE_ZONES:
        zx0, zy0 = max(0, zx), max(0, zy)
        zx1, zy1 = min(IMG_W, zx + zw), min(IMG_H, zy + zh)
        zone_mask[zy0:zy1, zx0:zx1] = 255

    sphere_bright = cv2.bitwise_and(bright_all, zone_mask)
    # Dilate to ensure full text coverage including anti-aliased edges
    sphere_bright = cv2.dilate(sphere_bright, np.ones((3, 3), np.uint8), iterations=2)
    print(f"  [sphere] bright pixels within zones: {int((sphere_bright > 0).sum())}")

    mask = np.maximum(mask, sphere_bright)

    # ---- Legend body (bottom, y >= 3450): full erase since we redraw ----
    cv2.rectangle(mask, (0, 3450), (IMG_W, IMG_H), 255, thickness=-1)

    # ---- Color word labels row: full erase ----
    cv2.rectangle(mask, (1360, 3210), (2260, 3270), 255, thickness=-1)

    # ---- Dwarf / Giant / Supergiant labels: full erase ----
    cv2.rectangle(mask, (1180, 3280), (1540, 3560), 255, thickness=-1)

    # ---- QuasiSpace Map mini-title inside green rectangle ----
    cv2.rectangle(mask, (2870, 3200), (3220, 3270), 255, thickness=-1)

    return mask

# =============================================================================
# Step 2: Inpaint
# =============================================================================

def inpaint(img_bgr, mask):
    """Two-stage erase strategy:
    1. Fill mask pixels with pure background (sampled dark) — GUARANTEED to
       remove same-color letters (rings + text share color; inpaint would
       otherwise refill from ring neighbours).
    2. Rings will be redrawn later in Pillow using known circle params.
    3. Very small radius inpaint pass afterwards smooths hard edges near mask
       boundary for constellation/star labels (where surrounding pixels are
       dark bg, so no color-bleed risk).
    """
    h, w = img_bgr.shape[:2]

    # Sample global dark background from corners (median of darkest 30%)
    corner_samples = []
    for cx, cy in [(50, 4200), (3100, 4200), (50, 100), (3100, 100),
                    (1600, 4200), (50, 2000), (3100, 2000)]:
        x0, y0 = max(0, cx-25), max(0, cy-25)
        x1, y1 = min(w, cx+25), min(h, cy+25)
        patch = img_bgr[y0:y1, x0:x1].reshape(-1, 3)
        lum = patch[:, 0].astype(int) + patch[:, 1].astype(int) + patch[:, 2].astype(int)
        sorted_idx = np.argsort(lum)
        dark = patch[sorted_idx[:len(sorted_idx) // 3]]
        corner_samples.append(dark)
    all_dark = np.vstack(corner_samples)
    bg_color = np.median(all_dark, axis=0).astype(np.uint8)
    print(f"  [inpaint] sampled bg = BGR({bg_color[0]},{bg_color[1]},{bg_color[2]})")

    # Step 1: hard fill mask pixels with bg color (perfect erase, no color-bleed)
    result = img_bgr.copy()
    result[mask > 0] = bg_color

    # Step 2: subtle noise for texture continuity with surrounding starfield
    if (mask > 0).sum() > 0:
        noise = np.random.randint(-6, 7, size=(mask > 0).sum() * 3,
                                   dtype=np.int16).reshape(-1, 3)
        filled = result[mask > 0].astype(np.int16) + noise
        result[mask > 0] = np.clip(filled, 0, 255).astype(np.uint8)

    return result

# =============================================================================
# Step 3: Load fonts (multiple sizes)
# =============================================================================

class FontPool:
    def __init__(self, path):
        self.path = str(path)
        self._cache = {}
    def get(self, size):
        if size not in self._cache:
            self._cache[size] = ImageFont.truetype(self.path, size)
        return self._cache[size]

# =============================================================================
# Step 4: Draw Chinese overlays
# =============================================================================

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_all(img_pil, matches, font_pool):
    draw = ImageDraw.Draw(img_pil)

    # ---- Redraw sphere ring outlines (inpaint may have broken them) ----
    for cx, cy, r, rgb, lw in SPHERE_CIRCLES:
        bbox = (cx - r, cy - r, cx + r, cy + r)
        draw.ellipse(bbox, outline=rgb, width=lw)

    # ---- Constellation & star labels (from OCR + manual) ----
    label_color = (184, 218, 255)   # #B8DAFF pale-blue like original
    for m in matches:
        fs = max(min(int(m["h"] * 0.95), 42), 20)
        font = font_pool.get(fs)
        zh = m["zh"]
        # Position: text top-left at bbox top-left, slightly adjusted
        tx = m["x"]
        ty = m["y"] - 2
        # Draw with black outline for readability
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            draw.text((tx+dx, ty+dy), zh, font=font, fill=(0,0,0))
        draw.text((tx, ty), zh, font=font, fill=label_color)

    # ---- Race sphere labels (colored, centered) ----
    for name, cx, cy, mw, mh, rgb, fs in SPHERE_ANCHORS:
        font = font_pool.get(fs)
        bbox = font.getbbox(name)
        w_text = bbox[2] - bbox[0]
        h_text = bbox[3] - bbox[1]
        tx = cx - w_text // 2
        ty = cy - h_text // 2 - bbox[1]  # correct for baseline
        # Draw with black outline
        for dx in (-2,-1,0,1,2):
            for dy in (-2,-1,0,1,2):
                if dx or dy:
                    draw.text((tx+dx, ty+dy), name, font=font, fill=(0,0,0))
        draw.text((tx, ty), name, font=font, fill=rgb)

    # ---- Color word labels: 紅 橙 黃 綠 藍 白 ----
    color_labels = [("紅", 1406), ("橙", 1552), ("黃", 1710),
                    ("綠", 1873), ("藍", 2032), ("白", 2196)]
    font = font_pool.get(32)
    for zh, cx in color_labels:
        bbox = font.getbbox(zh)
        w_text = bbox[2] - bbox[0]
        tx = cx - w_text // 2
        ty = 3220
        draw.text((tx, ty), zh, font=font, fill=(255,255,255))

    # ---- Dwarf / Giant / Supergiant labels ----
    for zh, cy in [("矮星", 3295), ("巨星", 3390), ("超巨星", 3490)]:
        font = font_pool.get(32)
        bbox = font.getbbox(zh)
        w_text = bbox[2] - bbox[0]
        tx = 1345 - w_text // 2
        draw.text((tx, cy), zh, font=font, fill=(255,255,255))

    # ---- Legend body (32 items × 3 columns) ----
    LEG_X0 = 100
    LEG_Y0 = 3540
    COL_W  = 570
    ITEM_H = 40
    PER_COL = 11

    # Title
    title_font = font_pool.get(36)
    draw.text((LEG_X0, LEG_Y0 - 55), "母星、物品與其他有用位置：",
              font=title_font, fill=(255,255,255))

    item_font = font_pool.get(28)
    num_font  = font_pool.get(28)
    for i, (num, zh) in enumerate(LEGEND_ITEMS):
        col = i // PER_COL
        row = i % PER_COL
        x0 = LEG_X0 + col * COL_W
        y0 = LEG_Y0 + row * ITEM_H
        # Number in yellow
        draw.text((x0, y0), f"{num}.", font=num_font, fill=(255,221, 68))
        num_bbox = num_font.getbbox(f"{num}.")
        draw.text((x0 + num_bbox[2] - num_bbox[0] + 8, y0), zh,
                  font=item_font, fill=(255,255,255))

    # ---- Legend bullets (Rainbow / QuasiSpace portal) ----
    bullet_x = LEG_X0 + 2 * COL_W
    bullet_y0 = LEG_Y0 + PER_COL * ITEM_H
    for i, (zh, rgb) in enumerate(LEGEND_BULLETS):
        y0 = bullet_y0 + i * ITEM_H
        # Draw open circle
        draw.ellipse((bullet_x, y0 + 4, bullet_x + 24, y0 + 28),
                     outline=rgb, width=3)
        draw.text((bullet_x + 36, y0), zh, font=item_font, fill=(255,255,255))

    # ---- Star system designations (Greek alphabet) ----
    des_x = 2350
    des_y = LEG_Y0 - 55
    desig_font = font_pool.get(32)
    draw.text((des_x, des_y), "星系命名（希臘字母順序）",
              font=desig_font, fill=(255,170,255))

    greek = [("α", "Alpha"), ("η", "Eta"),
             ("β", "Beta"),  ("θ", "Theta"),
             ("γ", "Gamma"), ("ι", "Iota"),
             ("δ", "Delta"), ("κ", "Kappa"),
             ("ε", "Epsilon"), ("λ", "Lambda")]
    greek_font_yellow = font_pool.get(30)
    greek_font_white  = font_pool.get(30)
    for i, (g, name) in enumerate(greek):
        col = i % 2
        row = i // 2
        x0 = des_x + col * 200
        y0 = des_y + 50 + row * 42
        draw.text((x0, y0), g, font=greek_font_yellow, fill=(255,221,68))
        draw.text((x0 + 40, y0), name, font=greek_font_white, fill=(255,255,255))

    # ---- QuasiSpace map explanation ----
    qs_x = 2350
    qs_y = LEG_Y0 + 300
    draw.text((qs_x, qs_y), "準空間地圖", font=desig_font, fill=(136,221,255))
    qs_lines = [
        "每個傳送門旁的字母，",
        "對應其在超空間中的",
        "出口點所標示的字母。",
        "",
        "超空間與準空間之間",
        "的雙向傳送門位置",
        "（每月開啟一次）。",
    ]
    qs_font = font_pool.get(26)
    for i, line in enumerate(qs_lines):
        draw.text((qs_x, qs_y + 50 + i * 38), line,
                  font=qs_font, fill=(255,255,255))

    return img_pil

# =============================================================================
# Main
# =============================================================================

def main():
    print(f"[load] {IMG_SRC}")
    img_bgr = cv2.imread(str(IMG_SRC))
    if img_bgr is None:
        raise SystemExit(f"Cannot read {IMG_SRC}")
    print(f"  {img_bgr.shape}")

    print("[ocr] load matches")
    matches = load_ocr_matches()
    print(f"  matches: {len(matches)}")

    print("[mask] build")
    mask = build_mask(matches, img_bgr)
    cv2.imwrite(str(MASK_OUT), mask)
    print(f"  saved {MASK_OUT}")

    print("[inpaint] cv2.INPAINT_TELEA r=5")
    clean_bgr = inpaint(img_bgr, mask)
    cv2.imwrite(str(INPAINTED), clean_bgr, [cv2.IMWRITE_PNG_COMPRESSION, 6])
    print(f"  saved {INPAINTED}")

    print("[pillow] convert & draw")
    # BGR → RGB → Pillow
    clean_rgb = cv2.cvtColor(clean_bgr, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(clean_rgb)

    font_pool = FontPool(FONT_TTF if FONT_TTF.exists() else FONT_ALT)
    print(f"  font: {font_pool.path}")

    img_pil = draw_all(img_pil, matches, font_pool)

    print(f"[save] {IMG_OUT}")
    img_pil.save(IMG_OUT, format="PNG", optimize=True)
    print(f"  size: {IMG_OUT.stat().st_size:,} bytes")

    # Write report
    lines = [
        "=== Starmap.zh-TW.png v2 build ===",
        f"OCR matches applied: {len(matches)}",
        f"Sphere labels: {len(SPHERE_ANCHORS)}",
        f"Sphere erase zones: {len(SPHERE_ERASE_ZONES)}",
        f"Legend items: {len(LEGEND_ITEMS)}",
        f"Font: {font_pool.path}",
        f"Output: {IMG_OUT}",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"  report: {REPORT}")

if __name__ == "__main__":
    main()
