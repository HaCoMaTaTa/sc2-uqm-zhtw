"""
Star Control II Starmap.png → Traditional Chinese SVG overlay.

Pipeline:
1. Load OCR results (from _starmap_ocr_test.py)
2. Fuzzy-match each detected English text to a translation dict
3. Group multi-word legend entries into single lines
4. Generate SVG with:
   - Original PNG as background <image> (embedded as base64 data URI)
   - Black rounded rects covering each matched English text
   - Chinese <text> overlays with matching color/size
   - Hardcoded race sphere labels near circle centers
   - Redrawn Chinese legend section (bottom)
5. Report matched / unmatched items

Coord conversion (from map grid to pixel):
   x_pixel = 101 + 2.94 * x_map
   y_pixel = 3057 - 2.94 * y_map    (y-axis inverted)
"""
import base64
import json
import re
from pathlib import Path
from html import escape

# =============================================================================
# 1. Paths
# =============================================================================

IMG_PATH = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.png")
OCR_JSON = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_ocr_multipass.json")
OUT_SVG  = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.zh-TW.svg")
REPORT   = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out\_build_report.txt")

IMG_W, IMG_H = 3200, 4258

# CJK font family — must match a real installed font name (librsvg/Pango do exact match)
FONT_FAMILY = "Microsoft JhengHei"

# =============================================================================
# 2. Translation dictionary
#    Key = lowercased English text (stripped of trailing punctuation)
#    Val = { "zh": Chinese, "note": optional info }
# =============================================================================

# 2a. Constellation genitive forms → Chinese 星座 (ROC 天文學會譯名)
CONSTELLATIONS = {
    "andromedae":     "仙女座",
    "antilae":        "唧筒座",   # SC2 spelling of Antliae
    "antliae":        "唧筒座",
    "apodis":         "天燕座",
    "aquarii":        "寶瓶座",
    "aquilae":        "天鷹座",
    "arae":           "天壇座",
    "arietis":        "白羊座",
    "aurigae":        "御夫座",
    "bootis":         "牧夫座",
    "caeli":          "雕具座",
    "camelopardalis": "鹿豹座",
    "cancri":         "巨蟹座",
    "canis":          "犬座",     # ambiguous, generic
    "capricorni":     "摩羯座",
    "carinae":        "船底座",
    "cassiopeiae":    "仙后座",
    "centauri":       "半人馬座",
    "cephei":         "仙王座",
    "ceti":           "鯨魚座",
    "chameleonis":    "蝘蜓座",
    "chamaeleonis":   "蝘蜓座",
    "circini":        "圓規座",
    "columbae":       "天鴿座",
    "comae":          "后髮座",
    "coronae":        "冕座",
    "corvi":          "烏鴉座",
    "crateris":       "巨爵座",
    "crucis":         "南十字座",
    "cygni":          "天鵝座",
    "cygnus":         "天鵝座",
    "delphini":       "海豚座",
    "doradus":        "劍魚座",
    "draconis":       "天龍座",
    "equulei":        "小馬座",
    "eridani":        "波江座",
    "fornacis":       "天爐座",
    "geminorum":      "雙子座",
    "gruis":          "天鶴座",
    "herculis":       "武仙座",
    "horologii":      "時鐘座",
    "hydrae":         "長蛇座",
    "hydri":          "水蛇座",
    "indi":           "印第安座",
    "lacertae":       "蝎虎座",
    "leonis":         "獅子座",
    "leporis":        "天兔座",
    "librae":         "天秤座",
    "lupi":           "豺狼座",
    "lyncis":         "天貓座",
    "lyrae":          "天琴座",
    "mensae":         "山案座",
    "microscopii":    "顯微鏡座",
    "monocerotis":    "麒麟座",
    "muscae":         "蒼蠅座",
    "normae":         "矩尺座",
    "octantis":       "南極座",
    "ophiuchi":       "蛇夫座",
    "orionis":        "獵戶座",
    "pavonis":        "孔雀座",
    "pegasi":         "飛馬座",
    "persei":         "英仙座",
    "phoenicis":      "鳳凰座",
    "pictoris":       "繪架座",
    "piscium":        "雙魚座",
    "piscis":         "南魚座",
    "pyxidis":        "羅盤座",
    "puppis":         "船尾座",
    "reticuli":       "網罟座",
    "sagitarii":      "人馬座",   # SC2 spelling of Sagittarii
    "sagittarii":     "人馬座",
    "sagittae":       "天箭座",
    "sculptoris":     "玉夫座",
    "scorpii":        "天蠍座",
    "scuti":          "盾牌座",
    "serpentis":      "巨蛇座",
    "sextantis":      "六分儀座",
    "tauri":          "金牛座",
    "telescopii":     "望遠鏡座",
    "trianguli":      "三角座",
    "tucanae":        "杜鵑座",
    "ursae":          "熊座",
    "velorum":        "船帆座",
    "virginis":       "室女座",
    "volantis":       "飛魚座",
    "vulpeculae":     "狐狸座",
}

# 2b. Named stars & astronomers / SC2-original names → Chinese
#     Uses ROC astronomical translation where standard; audio-transliteration otherwise
NAMED_STARS = {
    # Real named stars (ROC 天文學會譯名)
    "sol":            "太陽（Sol）",
    "sirius":         "天狼星",
    "vega":           "織女星",
    "betelgeuse":     "參宿四",
    "procyon":        "南河三",
    "arcturus":       "大角星",
    "rigel":          "參宿七",
    "antares":        "心宿二",
    "aldebaran":      "畢宿五",
    "canopus":        "老人星",
    "fomalhaut":      "北落師門",
    "capella":        "五車二",
    "regulus":        "軒轅十四",
    "deneb":          "天津四",
    "pollux":         "北河三",
    "altair":         "河鼓二",
    "mira":           "芻藁增二",
    "menkar":         "天囷一",
    "hyades":         "畢宿星團",
    "achernar":       "水委一",
    "bellatrix":      "參宿五",
    "algol":          "大陵五",
    "alcor":          "開陽增一",
    "mizar":          "開陽",
    "wolf":           "沃夫星",
    "luyten":         "呂坦星",
    "lalande":        "拉朗德星",
    "krueger":        "克魯格星",
    "groombridge":    "葛倫布利吉",
    "lacaille":       "拉卡伊星",
    "giclas":         "吉克拉斯",
    # SC2-original / astronomer-named stars (transliterated)
    "klystron":       "克利斯壯",
    "chandrasekhar":  "錢卓卡",
    "mersenne":       "梅森",
    "zeeman":         "日曼",
    "vela":           "微拉",       # single-star context on map
    "cerenkov":       "切連科夫",
    "kepler":         "克卜勒",
    "copernicus":     "哥白尼",
    "maksutov":       "馬克蘇托夫",
    "hyperion":       "海柏利昂",
    "arianni":        "阿里安尼",
    "brahe":          "第谷",
    "raynet":         "雷奈特",
    "saurus":         "薩魯斯",
    "metis":          "梅蒂斯",
    "olber":          "歐柏",
    "lentilis":       "蘭提利斯",
    "vitalis":        "維塔利斯",
    "hyginus":        "海吉努斯",
    "almagest":       "至大論",
    "gorno":          "戈爾諾",
    "octantis":       "南極座",     # named star or constellation genitive
    "organon":        "歐加農",     # Master_Glossary v0.5
    "ptolemae":       "托勒密",
    "octantis":       "南極座",
    "squidi":         "斯奎第",
    "illuminati":     "光明會",
    "lipi":           "利皮",       # SC2-only star name
    "letum":          "利圖姆",
}

# 2c. Race sphere labels (curved text — replaced with straight labels)
RACE_SPHERES = {
    "thraddash": "撻伐族",
    "supox":     "蘇菩族",
    "utwig":     "憂特族",
    "kohr-ah":   "柯亞族",
    "ur-quan":   "烏寬族",
    "umgah":     "陰嘎族",
    "pkunk":     "普恩族",
    "yehat":     "翼哈特族",
    "vux":       "VUX",
    "mycon":     "麥孔族",
    "ilwrath":   "蛛狂族",
    "orz":       "歐茲族",
    "druuge":    "毒賈族",
    "spathi":    "史怕族",
    "arilou":    "阿麗露",
    "zoq":       "佐",
    "fot":       "佛",
    "pik":       "皮",
    "zoq-fot-pik": "佐-佛-皮",
}

# 2d. Legend title / labels / colors / dwarf-giant / Greek alphabet
LEGEND_MISC = {
    # Section headers
    "homeworlds":     "母星、",
    "items":          "物品",
    "&":              "與",
    "other":          "其他",
    "useful":         "有用",
    "locations":      "地點",
    "locations:":     "地點：",
    "rainbow":        "彩虹",
    "world":          "星球",
    "location":       "位置",
    # Colors (star classification)
    "red":            "紅",
    "orange":         "橙",
    "yellow":         "黃",
    "green":          "綠",
    "blue":           "藍",
    "white":          "白",
    "dwarf":          "矮星",
    "giant":          "巨星",
    "supergiant":     "超巨星",
    # Greek alphabet (kept as-is, but labels translated)
    "alpha":          "α  Alpha",
    "beta":           "β  Beta",
    "gamma":          "γ  Gamma",
    "delta":          "δ  Delta",
    "epsilon":        "ε  Epsilon",
    "zeta":           "ζ  Zeta",
    "eta":            "η  Eta",
    "theta":          "θ  Theta",
    "iota":           "ι  Iota",
    "kappa":          "κ  Kappa",
    "lambda":         "λ  Lambda",
    "-lota":          "ι  Iota",   # OCR misread
    # Star system designation heading
    "star":           "星系",
    "system":         "命名",
    "designations":   "（希臘",
    "(in":            "字母",
    "the":            "順序）",
    "greek":          "",
    "alphabet)":      "",
    # QuasiSpace map heading
    "quasispace":     "準空間",
    "map":            "地圖",
    "portal":         "傳送門",
    "exit":           "出口",
    "(see":           "（見",
    "map)":           "地圖）",
    # QuasiSpace map body text
    "between":        "之間",
    "hyperspace":     "超空間",
    "and":            "與",
    "quasispace)":    "準空間）",
    # portal-corresponds sentence
    "letter":         "字母",
    "next":           "旁的",
    "each":           "每個",
    "corresponds":    "對應",
    "marking":        "所標",
    "its":            "其",
    "point":          "點於",
    "bi-directional": "雙向",
    "(open":          "（每月",
    "monthly":        "開啟）",
    "(your":          "（您的",
    "homeworld)":     "母星）",
}

# 2e. Homeworld / item labels in legend (multi-word groups)
#     These are matched by regex on the JOINED legend rows, so we don't need per-word here.
#     But we list common single-word tokens for the matcher:
LEGEND_HOMEWORLDS = {
    "earth,":         "地球",
    "starbase":       "星際基地",
    "spathi":         "史怕族",
    "pluto":          "冥王星",
    "umgah":          "陰嘎族",
    "yehat":          "翼哈特族",
    "pkunk":          "普恩族",
    "vux":            "VUX",
    "mycon":          "麥孔族",
    "supox":          "蘇菩族",
    "thraddash":      "撻伐族",
    "druuge":         "毒賈族",
    "mmrnmhrm":       "姆姆族",
    "slylandro":      "斯萊族",
    "chenjesu":       "晶智族",
    "shofixti":       "修烈士族",
    "syreen":         "塞蓮族",
    "arilou":         "阿麗露",
    "burvix":         "布維族",
    "zoq-fot-pik":    "佐-佛-皮",
    "homeworld":      "母星",
    "homeworld)":     "母星）",
    "sa-matra":       "薩瑪特拉",
    "warp":           "扭曲",
    "pod":            "艙",
    "utwig":          "憂特族",
    "bomb":           "炸彈",
    "sun":            "太陽",
    "device":         "裝置",
    "aqua":           "水",
    "helix":          "螺旋",
    "fleet":          "艦隊",
    "vault":          "庫",
    "beast":          "獸",
    "maidens":        "少女們",
    "talking":        "會話",
    "pet":            "寵",
    "shield":         "盾",
    "taalo":          "塔洛",
    "ruins":          "遺跡",
    "'caster":        "廣播器",
    "caster":         "廣播器",
    "egg-case":       "卵夾",
    "admiral":        "上將",
    "zex":            "澤克斯",
    "zex's":          "澤克斯的",
    "ur-quan":        "烏寬族",
    "androsynth":     "安卓辛族",
}

# Aggregate all dictionaries into one lookup (later entries override earlier)
LOOKUP = {}
for d in (CONSTELLATIONS, NAMED_STARS, RACE_SPHERES, LEGEND_MISC, LEGEND_HOMEWORLDS):
    for k, v in d.items():
        LOOKUP[k.lower()] = v

# =============================================================================
# 3. Race sphere labels — direct pixel coordinates (measured from image)
#    Each entry: (name, cx, cy, mask_w, mask_h, color, fs)
#    cx,cy = approximate CENTER of the original English curved arc label
# =============================================================================

SPHERE_ANCHORS = [
    # (name,       cx,   cy,   mw,  mh, color,     fs)
    ("撻伐族",     945,  350, 480, 100, "#5FDDDD", 62),   # THRADDASH top arc
    ("蘇菩族",    2280,  200, 260,  80, "#FF9040", 46),   # SUPOX
    ("憂特族",    2620,  220, 280,  80, "#88BBEE", 54),   # UTWIG
    ("烏寬柯亞",  2150,  380, 320,  80, "#BBBBBB", 46),   # KOHR-AH grey outer top
    ("烏寬族",    2050,  475, 260,  80, "#33FF33", 54),   # UR-QUAN green
    ("陰嘎族",     680, 1055, 320,  95, "#B090E0", 58),   # UMGAH (from OCR UMGAL bbox center)
    ("普恩族",     220, 2860, 240,  80, "#66AAFF", 50),   # PKUNK bottom-left
    ("翼哈特族",  1400, 3050, 300,  80, "#88CCEE", 50),   # YEHAT bottom-mid
    ("VUX",      1370, 2560, 200,  80, "#3366FF", 62),   # VUX
    ("麥孔族",    2050, 2105, 320, 100, "#FF88CC", 62),   # MYCON (from OCR 1913,2036 bbox 275x135)
    ("蛛狂族",     480, 2145, 300,  80, "#FF33CC", 58),   # ILWRATH top arc (LEFT half)
    ("歐茲族",    1417, 2178, 180,  70, "#DD44DD", 46),   # ORZ small
    ("毒賈族",    2560, 2810, 260,  80, "#FF3333", 58),   # DRUUGE bottom
    ("史怕族",     825, 1735, 260,  80, "#FF9933", 58),   # SPATHI top arc (LEFT half)
    ("阿麗露",     190, 1085, 220,  60, "#3399FF", 40),   # ARILOU small blue
    ("佐-佛-皮", 1080, 2500, 260,  70, "#FF3333", 40),   # ZOQ-FOT-PIK combined
]

# =============================================================================
# 4. Load OCR & match
# =============================================================================

ocr_records = json.loads(OCR_JSON.read_text(encoding="utf-8"))
print(f"[load] {len(ocr_records)} OCR records")

def normalize(t: str) -> str:
    t = t.strip().lower()
    # Strip trailing punctuation
    t = re.sub(r"[.,;:!?'\"()\[\]{}\-\u2018\u2019]+$", "", t)
    t = re.sub(r"^[.,;:!?'\"()\[\]{}\-\u2018\u2019]+", "", t)
    return t

# OCR noise fixes (common misreads observed)
OCR_FIXES = {
    "horolggii":  "horologii",
    "camblopardalis": "camelopardalis",
    "culptoris":  "sculptoris",
    "krueg":      "krueger",
    "carin":      "carinae",
    "colu":       "columbae",
    "centau":     "centauri",
    "gentauri":   "centauri",
    "iclas":      "giclas",     # OCR dropped G — matches (402, 2880)
    "cru":        "crucis",
    "crugis":     "crucis",
    "sag":        "sagittarii",
    "mmmrnmhrm":  "mmrnmhrm",
    "'arietis":   "arietis",
    "ntis":       "sextantis",  # trailing fragment
    "huminati":   "illuminati",
    "+canopus":   "canopus",
    "ucanae":     "tucanae",
    "votantis":   "volantis",
    "vota":       "volantis",
    "aldebar":    "aldebaran",
    "olf":        "wolf",
    "alta":       "altair",
    "mizal":      "mizar",
    "gorno":      "gorno",
    "ibrae":      "librae",       # OCR truncated Librae
    "lacerta":    "lacertae",     # OCR truncated Lacertae
    "crate":      "crateris",     # OCR truncated Crateris
    "mages":      "almagest",     # OCR truncated Almagest
    "camblopardalis": "camelopardalis",
    "camelo":     "camelopardalis",
    "chameleoni": "chameleonis",
    "phoenici":   "phoenicis",
    "reticul":    "reticuli",
    "sextan":     "sextantis",
    "tucana":     "tucanae",
    "aquari":     "aquarii",
    "piscium":    "piscium",
    "hyad":       "hyades",
    "hla":        None,          # noise
    "umgal":      None,          # sphere label — hardcoded elsewhere
    "mycon":      None,          # sphere label
    "pkunk":      None,          # sphere label
    "ho":         None,
    "el":         None,
    "en":         None,
    "op":         None,
}

# Hardcoded overrides for labels OCR could not find at all
# Format: (english_key, x, y, w, h, fallback_conf)
MANUAL_LABELS = [
    # Constellation labels missed by OCR (approx pixel positions from visual inspection)
    ("squidi",      686, 1810, 130, 45),
    ("gruis",       937, 1920, 100, 45),
    ("herculis",    560, 1940, 145, 45),
    # illuminati handled by OCR huminati→illuminati fix
    ("capricorni", 1162, 1520, 170, 45),
    ("serpentis",  1435, 2975, 175, 45),
    ("scuti",      1710, 2905, 115, 45),
    ("columbae",    400, 2525, 175, 45),
    ("cru",        1652, 1160,  75, 45),
    ("lipi",       1769,  460,  75, 45),
    ("mira",       1246, 2417,  95, 45),   # OCR "Mira" mis-matched to "Admiral"
]


matched = []   # list of dicts: {text, zh, x, y, w, h, conf, orig}
unmatched = []

for r in ocr_records:
    if r["conf"] < 40:
        continue
    raw = r["text"]
    key = normalize(raw)
    # Apply fix table
    if key in OCR_FIXES:
        fixed = OCR_FIXES[key]
        if fixed is None:
            continue  # noise / already handled
        key = fixed
    if len(key) < 2:
        continue
    # Skip pure numbers (grid axes)
    if re.fullmatch(r"\d+", key):
        continue
    # Skip Greek letter or single letter fragments
    if re.fullmatch(r"[αβγδεζηθικλμνξοπρστυφχψω]+", raw):
        continue
    # Legend section (y > 3200 covers star matrix, color labels, and item list — handled separately)
    if r["y"] > 3200:
        continue
    zh = LOOKUP.get(key)
    if zh:
        matched.append({**r, "key": key, "zh": zh})
    else:
        unmatched.append({**r, "key": key})

# Merge in manual overrides for OCR-missing labels
for key, x, y, w, h in MANUAL_LABELS:
    zh = LOOKUP.get(key)
    if not zh:
        print(f"[warn] manual label {key!r} has no dict entry")
        continue
    # Avoid duplicate if OCR already matched nearby
    dup = any(abs(m["x"] - x) < 50 and abs(m["y"] - y) < 30 and m["key"] == key for m in matched)
    if dup:
        continue
    matched.append({
        "text": key, "conf": 100, "x": x, "y": y, "w": w, "h": h,
        "key": key, "zh": zh, "src": "manual",
    })

print(f"[match] matched={len(matched)}, unmatched={len(unmatched)} (in map body)")

# =============================================================================
# 5. Build SVG
# =============================================================================

svg_parts = []
svg_parts.append(f'<?xml version="1.0" encoding="UTF-8"?>')
svg_parts.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'xmlns:xlink="http://www.w3.org/1999/xlink" '
    f'width="{IMG_W}" height="{IMG_H}" viewBox="0 0 {IMG_W} {IMG_H}" '
    f'font-family="{FONT_FAMILY}" '
    f'font-weight="600">')
svg_parts.append('<title>Star Control II — Galactic Map (Traditional Chinese)</title>')

# 5.1 Background image — embed as base64 so librsvg/browsers can render standalone
img_b64 = base64.b64encode(IMG_PATH.read_bytes()).decode("ascii")
svg_parts.append(
    f'<image x="0" y="0" width="{IMG_W}" height="{IMG_H}" '
    f'preserveAspectRatio="none" '
    f'xlink:href="data:image/png;base64,{img_b64}"/>'
)

# 5.2 Cover-and-replace all matched map-body labels
#     Each match: draw a black rounded rect matching bbox, then overlay Chinese text.
svg_parts.append('<!-- ==================== Map body labels ==================== -->')
for m in matched:
    x, y, w, h = m["x"], m["y"], m["w"], m["h"]
    zh = m["zh"]
    # Expand bbox slightly to fully hide English
    pad_x, pad_y = 4, 3
    rx, ry = x - pad_x, y - pad_y
    rw, rh = w + 2 * pad_x, h + 2 * pad_y
    # Detect if this is a large label (likely Latin body text ~30 px)
    fs = max(min(int(h * 0.95), 42), 18)
    # Draw mask
    svg_parts.append(
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#000000" opacity="0.92"/>'
    )
    # Draw Chinese overlay centered vertically in bbox
    tx = x
    ty = y + h - int(h * 0.15)
    svg_parts.append(
        f'<text x="{tx}" y="{ty}" fill="#B8DAFF" font-size="{fs}">'
        f'{escape(zh)}</text>'
    )

# 5.3 Race sphere labels (hardcoded pixel coords)
svg_parts.append('<!-- ==================== Race sphere labels ==================== -->')
for name, cx, cy, mw, mh, color, fs in SPHERE_ANCHORS:
    # Draw a wide black mask rect centered at (cx, cy) to hide underlying curved English arc
    svg_parts.append(
        f'<rect x="{cx - mw//2}" y="{cy - mh//2}" width="{mw}" height="{mh}" '
        f'fill="#000000" opacity="0.90" rx="8" ry="8"/>'
    )
    # Vertical center: for baseline text, adjust y by fs*0.35
    ty = cy + int(fs * 0.35)
    svg_parts.append(
        f'<text x="{cx}" y="{ty}" fill="{color}" font-size="{fs}" '
        f'text-anchor="middle" font-weight="700">{escape(name)}</text>'
    )

# 5.4 Redraw the entire legend section (bottom, y > 3400)
#     Blank the original English legend by overlaying a black rect,
#     then draw the Chinese legend from scratch.
svg_parts.append('<!-- ==================== Legend section (redrawn in Chinese) ==================== -->')
LEGEND_TOP = 3450
svg_parts.append(
    f'<rect x="0" y="{LEGEND_TOP}" width="{IMG_W}" height="{IMG_H - LEGEND_TOP}" '
    f'fill="#000000"/>'
)
# Also cover the "Dwarf/Giant/Supergiant" english labels (all on left of star matrix)
svg_parts.append(
    f'<rect x="1180" y="3270" width="360" height="280" fill="#000000"/>'
)

# Section 1: Color / Dwarf-Giant reference matrix (left of legend, ~x 1300-2100, y 3200-3450 originally)
# We redraw this too — it also overlaps with our black cover
# (The original color-classification chart is at y~3130-3450 — we'll keep the star icons visible
#  by ONLY covering below y=3450 as done, then draw a small chart on top of the redrawn legend.)

# Color labels above star matrix (row 1) — leave alone since y < 3400
# The Red/Orange/Yellow/... labels were at y=3228 (above cutoff) — they stay in original.
# BUT their translations should be shown. Add small Chinese labels below them:
color_labels = [
    ("紅", 1406), ("橙", 1552), ("黃", 1710), ("綠", 1873), ("藍", 2032), ("白", 2196),
]
# Cover original English color words with a wide black rect
svg_parts.append(
    f'<rect x="1360" y="3210" width="900" height="55" fill="#000000"/>'
)
for zh, x0 in color_labels:
    svg_parts.append(
        f'<text x="{x0}" y="3250" fill="#FFFFFF" font-size="30" '
        f'text-anchor="middle" font-weight="700">{escape(zh)}</text>'
    )
# Giant / Supergiant chinese overlay (row 2, y=3390, 3496) — these are BELOW the cutoff for cover
# So redraw as part of legend

# Now: redrawn Chinese legend body
# Layout: 4 columns of numbered items + Star system designations + QuasiSpace map explanation

LEGEND_ITEMS = [
    # (number, zh_text) — matches original 3-column layout of Starmap.png legend
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

# Special bullet items (not numbered — use round icons M/F on the map)
LEGEND_BULLETS = [
    ("彩虹星球位置",    "#FFAAFF"),   # M icon
    ("準空間傳送門出口（見地圖）",  "#33FF33"),   # F icon
]

# Layout config — 3 columns of ~11 items each, matches original English layout
LEGEND_X0 = 100
LEGEND_Y0 = 3540
COL_W = 570
ITEM_H = 40
COLS = 3

svg_parts.append(
    f'<text x="{LEGEND_X0}" y="{LEGEND_Y0}" fill="#FFFFFF" font-size="34" font-weight="700">'
    f'母星、物品與其他有用位置：</text>'
)

# 3 columns of 11, 11, 10 items (matches original layout)
per_col = 11
for i, (num, zh) in enumerate(LEGEND_ITEMS):
    col = i // per_col
    row = i % per_col
    x0 = LEGEND_X0 + col * COL_W
    y0 = LEGEND_Y0 + 55 + row * ITEM_H
    svg_parts.append(
        f'<text x="{x0}" y="{y0}" fill="#FFFFFF" font-size="26">'
        f'<tspan font-weight="700" fill="#FFDD44">{escape(num)}. </tspan>{escape(zh)}</text>'
    )

# Special bullet items (Rainbow world / QuasiSpace portal) — after item 32
BULLET_X = LEGEND_X0 + 2 * COL_W
BULLET_Y_START = LEGEND_Y0 + 55 + 11 * ITEM_H  # after last item in col 3
for i, (zh, color) in enumerate(LEGEND_BULLETS):
    y0 = BULLET_Y_START + i * ITEM_H
    svg_parts.append(
        f'<circle cx="{BULLET_X + 12}" cy="{y0 - 8}" r="12" fill="none" '
        f'stroke="{color}" stroke-width="3"/>'
    )
    svg_parts.append(
        f'<text x="{BULLET_X + 36}" y="{y0}" fill="#FFFFFF" font-size="26">{escape(zh)}</text>'
    )

# Color / dwarf-giant chart labels (below the color row 3200)
# The original 顯示 star icons of size Dwarf / Giant / Supergiant in a matrix ranged y~3260-3450
# Add Chinese labels beside them
matrix_x_labels = [(1330, "巨"), (1330, "超巨"), (1330, "矮")]
# Actually the matrix is: row 1 = supergiant, row 2 = giant, row 3 = dwarf
# The English labels "Giant" and "Supergiant" are shown at y=3390 and 3496
# Let's add Chinese labels ABOVE the English at those positions
svg_parts.append(
    f'<text x="1345" y="3310" fill="#FFFFFF" font-size="30" text-anchor="middle" '
    f'font-weight="700">矮星</text>'
)
svg_parts.append(
    f'<text x="1345" y="3405" fill="#FFFFFF" font-size="30" text-anchor="middle" '
    f'font-weight="700">巨星</text>'
)
svg_parts.append(
    f'<text x="1283" y="3505" fill="#FFFFFF" font-size="30" text-anchor="middle" '
    f'font-weight="700">超巨星</text>'
)

# Right-side legend: Star System Designations + QuasiSpace Map explanation
# Original was at x~1320+ and x~2740+
# We redraw at the right side of legend section
DESIG_X = 2350
DESIG_Y = LEGEND_Y0
svg_parts.append(
    f'<text x="{DESIG_X}" y="{DESIG_Y}" fill="#FFAAFF" font-size="30" font-weight="700">'
    f'星系命名（希臘字母順序）</text>'
)
greek_pairs = [
    ("α", "Alpha"),   ("η", "Eta"),
    ("β", "Beta"),    ("θ", "Theta"),
    ("γ", "Gamma"),   ("ι", "Iota"),
    ("δ", "Delta"),   ("κ", "Kappa"),
    ("ε", "Epsilon"), ("λ", "Lambda"),
]
for i, (g, name) in enumerate(greek_pairs):
    col = i % 2
    row = i // 2
    x0 = DESIG_X + col * 200
    y0 = DESIG_Y + 50 + row * 42
    svg_parts.append(
        f'<text x="{x0}" y="{y0}" fill="#FFFFFF" font-size="28">'
        f'<tspan font-weight="700" fill="#FFDD44">{g}</tspan>  {name}</text>'
    )

# QuasiSpace map explanation (right side)
QS_X = 2350
QS_Y = LEGEND_Y0 + 300
svg_parts.append(
    f'<text x="{QS_X}" y="{QS_Y}" fill="#88DDFF" font-size="30" font-weight="700">'
    f'準空間地圖</text>'
)
qs_lines = [
    "每個傳送門旁的字母對應",
    "所標其超空間出口點。",
    "",
    "雙向傳送門於超空間",
    "與準空間之間開啟",
    "（每月開啟一次）。",
]
for i, line in enumerate(qs_lines):
    svg_parts.append(
        f'<text x="{QS_X}" y="{QS_Y + 50 + i * 40}" fill="#FFFFFF" font-size="26">'
        f'{escape(line)}</text>'
    )

svg_parts.append('</svg>')

svg_text = "\n".join(svg_parts)
OUT_SVG.parent.mkdir(parents=True, exist_ok=True)
OUT_SVG.write_text(svg_text, encoding="utf-8")
print(f"[write] {OUT_SVG} ({len(svg_text):,} chars, {OUT_SVG.stat().st_size:,} bytes)")

# =============================================================================
# 6. Report
# =============================================================================

report_lines = []
report_lines.append(f"=== Starmap.zh-TW.svg build report ===")
report_lines.append(f"OCR records: {len(ocr_records)}")
report_lines.append(f"Matched: {len(matched)}")
report_lines.append(f"Unmatched (map body): {len(unmatched)}")
report_lines.append(f"Race sphere labels (hardcoded): {len(SPHERE_ANCHORS)}")
report_lines.append(f"Legend items: {len(LEGEND_ITEMS)}")
report_lines.append("")
report_lines.append("== Unmatched map-body OCR text (may need dict entry) ==")
for u in unmatched[:80]:
    report_lines.append(f"  {u['text']:24s} key={u['key']!r:20s} conf={u['conf']:3d} @({u['x']:4d},{u['y']:4d})")
if len(unmatched) > 80:
    report_lines.append(f"  ... and {len(unmatched)-80} more")

REPORT.write_text("\n".join(report_lines), encoding="utf-8")
print(f"[report] {REPORT}")
print("")
print("\n".join(report_lines[:15]))
