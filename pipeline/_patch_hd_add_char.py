"""Patch one CJK char into all HD staged fonts without full rebuild.

Reads each _stage_hd_fonts/<name>.fon, calls rasterize_font.py with
--chars <char> to a temp dir using the ORIGINAL HD ref-font
(install/content/addons/mm-hd/fonts/<name>.fon) so latin metrics match,
then extracts the new PNG + kerndat advance line and merges into the
staged dir.

Usage: python _patch_hd_add_char.py <char>
Example: python _patch_hd_add_char.py 橢
"""
import sys
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAGE = ROOT / "_stage_hd_fonts"
REF_ROOT = ROOT / "install" / "content" / "addons" / "mm-hd" / "fonts"
TTF = Path("C:/Windows/Fonts/NotoSansTC-VF.ttf")

# Matches _build_hd_fonts.ps1
UI_HEAVY = {'label.fon','micro.fon','micro.thin.fon','tiny.fon','tiny.bold.fon',
            'tiny.cond.fon','module.fon','square.fon','probe.fon'}
VERT_SHIFT = {'pkunk.fon': '10'}
SPECIAL_COMPUTER_REF = 'label.fon'  # computer.fon uses label.fon as ref


def patch_one_font(stage_dir: Path, char: str) -> tuple[bool, str]:
    name = stage_dir.name
    hex_id = f"{ord(char):05X}"
    target_png = stage_dir / f"{ord(char):05x}.png"
    if target_png.exists():
        return True, "already present"

    # Determine reference font (computer.fon uses label.fon)
    ref_name = SPECIAL_COMPUTER_REF if name == 'computer.fon' else name
    ref_dir = REF_ROOT / ref_name
    if not (ref_dir / "kerndat.fnt").exists():
        return False, f"no ref kerndat for {ref_name}"

    cjk_scale = '0.85' if name in UI_HEAVY else '1.0'
    vert_shift = VERT_SHIFT.get(name, '0')

    with tempfile.TemporaryDirectory() as td:
        out_dir = Path(td) / name
        cmd = [
            sys.executable, str(ROOT / "rasterize_font.py"),
            "--ref-font", str(ref_dir),
            "--ttf", str(TTF),
            "--chars", char,
            "--out", str(out_dir),
            "--cjk-scale", cjk_scale,
        ]
        if vert_shift != '0':
            cmd += ["--vertalign-adjust", vert_shift]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if res.returncode != 0:
            return False, f"rasterize failed: {res.stderr[-200:]}"

        # Copy new PNG (rasterize_font.py uses lowercase hex filenames)
        src_png = out_dir / f"{ord(char):05x}.png"
        if not src_png.exists():
            # try uppercase as fallback
            alt = out_dir / f"{hex_id}.png"
            if alt.exists():
                src_png = alt
            else:
                return False, f"PNG not generated: {src_png.name}"
        # Preserve engine convention: also lowercase target filename
        target_lc = stage_dir / f"{ord(char):05x}.png"
        target_lc.write_bytes(src_png.read_bytes())

        # Optionally merge kerndat advance entry if temp has one for this glyph.
        # (rasterize_font.py copies source kerndat as-is; new CJK usually has
        # no entry — engine falls back to PNG-width-based advance, which is
        # what we want. So skip kerndat modification.)
        return True, "PNG added (no kerndat entry needed)"


def main():
    if len(sys.argv) < 2:
        print("Usage: python _patch_hd_add_char.py <char> [<char> ...]")
        sys.exit(1)
    chars = []
    for arg in sys.argv[1:]:
        chars.extend(list(arg))
    chars = list(dict.fromkeys(chars))  # dedupe preserve order

    stage_dirs = sorted([d for d in STAGE.iterdir() if d.is_dir()])
    print(f"Patching {len(chars)} char(s) into {len(stage_dirs)} HD fonts:")
    for c in chars:
        print(f"  {c} (U+{ord(c):04X})")
    print()

    total_ok = 0
    total_fail = 0
    for c in chars:
        print(f"--- Char: {c} (U+{ord(c):04X}) ---")
        for sd in stage_dirs:
            ok, msg = patch_one_font(sd, c)
            status = "OK" if ok else "FAIL"
            print(f"  [{status}] {sd.name:22s}  {msg}")
            if ok:
                total_ok += 1
            else:
                total_fail += 1
        print()
    print(f"=== Total: {total_ok} ok, {total_fail} fail ===")


if __name__ == "__main__":
    main()
