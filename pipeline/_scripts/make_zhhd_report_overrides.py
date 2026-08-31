"""Generate zh-TW-hd addon overrides for the lander discovery report UI.

Produces 3 PNGs that shadow mm-hd assets so the HD lander report becomes
readable for dense CJK text:

  1. nav/orbitbackground/orbitbackground-021.png   -- 20x20 dark grey tile
     Overrides mm-hd/nav/orbitbackground/orbitbackground-021.png (bright
     blue dot). Together with the SD tile emitted by make_report_cells.py
     this produces a uniform dark-grey report backdrop.

  2. lander/fonteffect-000.png                     -- 40x40 palette PNG
  3. lander/fonteffect-001.png                     -- 40x40 palette PNG

     Font effect frames. Original mm-hd assets use palettes
     [(0,0,212),(0,4,252)] (blue "typing" flash) and
     [(0,252,0),(0,212,0)] (green "rest" colour). Because PC-mode
     report.c applies these as a per-pixel colour overlay through
     SetContextFontEffect(), the palette colours override any
     BUILD_COLOR fgcolor set by MakeReport. Overriding both palettes to
     whites makes the report body text render white -- matches the new
     high-contrast dark-grey backdrop.

Output goes to an _intermediate stage directory; a downstream packaging
script (_repackage_hd_addon.ps1) is responsible for wiring the files
into zh-TW-hd.uqm at:

    zh-TW-hd/shadow-content/addons/mm-hd/nav/orbitbackground/
    zh-TW-hd/shadow-content/addons/mm-hd/lander/

The mm-hd fonteffect PNGs are read from the shipped mm-hd.uqm content
package under install/content/addons/mm-hd.uqm so we can preserve the
exact palette layout (only the RGB triples change).
"""

from PIL import Image
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work")
STAGE = ROOT / "zh-TW-addon" / "_intermediate" / "zh-TW-hd-overrides"
MMHD_UQM = ROOT / "install" / "content" / "addons" / "mm-hd.uqm"
SEVEN_ZIP = r"C:\Program Files\7-Zip\7z.exe"

# zh-TW patch 032 colour set.
GRID_RGB = (30, 30, 30)                   # dark grey backdrop
GRID_ALPHA_CORNER = (0, 0, 0, 0)          # transparent corners
FONTEFF_000_PAL = [(220, 220, 220),       # typing frame: dim -> bright
                   (255, 255, 255)]
FONTEFF_001_PAL = [(255, 255, 255),       # rest frame:   bright -> dim
                   (220, 220, 220)]

HD_GRID_SIZE = (20, 20)


def _extract_mmhd_fonteffect(dst: Path) -> None:
    """Pull the two mm-hd fonteffect PNGs out of mm-hd.uqm into `dst`."""
    if not MMHD_UQM.is_file():
        sys.exit(f"missing {MMHD_UQM} -- run install first")
    dst.mkdir(parents=True, exist_ok=True)
    cmd = [
        SEVEN_ZIP, "e", str(MMHD_UQM),
        "mm-hd/lander/fonteffect-000.png",
        "mm-hd/lander/fonteffect-001.png",
        f"-o{dst}", "-y",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"7z extract failed:\n{result.stdout}\n{result.stderr}")


def _emit_grid(out_path: Path) -> None:
    w, h = HD_GRID_SIZE
    im = Image.new("RGBA", (w, h), (*GRID_RGB, 255))
    im.putpixel((0, 0), GRID_ALPHA_CORNER)
    im.putpixel((w - 1, 0), GRID_ALPHA_CORNER)
    im.putpixel((0, h - 1), GRID_ALPHA_CORNER)
    im.putpixel((w - 1, h - 1), GRID_ALPHA_CORNER)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(out_path, optimize=True)
    print(f"  grid {w}x{h} dark grey -> {out_path.relative_to(ROOT)}")


def _emit_fonteffect(src_png: Path, new_pal: list, out_path: Path) -> None:
    im = Image.open(src_png)
    if im.mode != "P":
        sys.exit(f"{src_png} not palette mode ({im.mode})")
    pal = list(im.getpalette())
    r0, g0, b0 = new_pal[0]
    r1, g1, b1 = new_pal[1]
    pal[0:6] = [r0, g0, b0, r1, g1, b1]
    im.putpalette(pal)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(out_path, optimize=True)
    print(f"  fonteffect palette -> {out_path.relative_to(ROOT)}")


def main() -> int:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)

    _emit_grid(STAGE / "nav" / "orbitbackground" / "orbitbackground-021.png")

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        _extract_mmhd_fonteffect(td_path)
        _emit_fonteffect(
            td_path / "fonteffect-000.png",
            FONTEFF_000_PAL,
            STAGE / "lander" / "fonteffect-000.png",
        )
        _emit_fonteffect(
            td_path / "fonteffect-001.png",
            FONTEFF_001_PAL,
            STAGE / "lander" / "fonteffect-001.png",
        )

    print(f"stage ready: {STAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
