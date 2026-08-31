"""Rasterize Starmap.zh-TW.svg → PNG with Noto Sans TC font registered."""
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Register the CJK font that our SVG references
FONT_PATH = Path(r"C:\Windows\Fonts\NotoSansTC-VF.ttf")
FONT_NAME = "NotoSansTC"
if not FONT_PATH.exists():
    FONT_PATH = Path(r"C:\Windows\Fonts\msjh.ttc")
    FONT_NAME = "MSJhengHei"

try:
    pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH)))
    print(f"[font] registered {FONT_NAME} from {FONT_PATH.name}")
except Exception as e:
    print(f"[warn] font register failed: {e}")

# Also register aliases the SVG font-family chain might expect
for alias in ("Noto Sans TC", "Microsoft JhengHei", "PingFang TC", "sans-serif"):
    try:
        pdfmetrics.registerFont(TTFont(alias, str(FONT_PATH)))
    except Exception:
        pass

SVG = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.zh-TW.svg")
PNG = SVG.with_suffix(".png")

print(f"[read] {SVG}")
drawing = svg2rlg(str(SVG))
if drawing is None:
    raise SystemExit("svg2rlg returned None")
print(f"[drawing] size = {drawing.width} x {drawing.height}")

renderPM.drawToFile(drawing, str(PNG), fmt="PNG", dpi=72)
print(f"[write] {PNG} ({PNG.stat().st_size:,} bytes)")
