"""Complete missing HD fonts by calling rasterize_font.py for each."""
import subprocess
import sys
from pathlib import Path

TTF = r"C:\Windows\Fonts\NotoSansTC-VF.ttf"
CHARS_FILE = "translations/_used_chars.txt"

UI_HEAVY = {'label.fon','micro.fon','micro.thin.fon','tiny.fon','tiny.bold.fon',
            'tiny.cond.fon','module.fon','square.fon','probe.fon'}

# Explicit per-font vertshift (from _build_hd_fonts.ps1)
VERT_SHIFT = {'pkunk.fon': 10}

REMAINING = ['syreen.fon','talkingpet.fon','thraddash.fon','tiny.bold.fon',
             'tiny.cond.fon','tiny.fon','umgah.fon','urquan.fon','utwig.fon',
             'vux.fon','yehat.fon','zoqfotpik.fon']

for f in REMAINING:
    ref = Path(f"install/content/addons/mm-hd/fonts/{f}")
    out = Path(f"_stage_hd_fonts/{f}")
    if out.exists() and (out / "kerndat.fnt").exists():
        print(f"  [skip] {f} (exists)")
        continue
    if not ref.exists():
        print(f"  [skip] {f} (no ref)")
        continue
    scale = "0.85" if f in UI_HEAVY else "1.0"
    cmd = [sys.executable, "rasterize_font.py",
           "--ref-font", str(ref), "--ttf", TTF,
           "--chars-file", CHARS_FILE, "--out", str(out),
           "--cjk-scale", scale]
    if f in VERT_SHIFT:
        cmd += ["--vertalign-adjust", str(VERT_SHIFT[f])]
    print(f"  [run] {f} scale={scale}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if 'Rasterized:' in line:
            print(f"    {line}")

print()
count = sum(1 for _ in Path("_stage_hd_fonts").iterdir() if _.is_dir())
print(f"Total fonts now: {count}")
