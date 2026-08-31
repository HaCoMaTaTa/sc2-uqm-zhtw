"""_analyze_p9_chars.py — find new CJK chars introduced by patch 009 star names."""
import json
from pathlib import Path

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work")
gs_json = json.loads((ROOT / "translations" / "gamestrings.zh-TW.json").read_text(encoding="utf-8"))

# Collect all CJK chars from ZH postfix entries
p9_chars = set()
for k, v in gs_json.items():
    if k.startswith("_STAR_POSTFIX_ZH_") and k != "_STAR_POSTFIX_ZH_NOTES":
        for c in v:
            if "\u4e00" <= c <= "\u9fff":
                p9_chars.add(c)

print(f"Star name unique CJK chars (patch 009): {len(p9_chars)}")

# Load previously staged HD chars to find which are NEW
hd_stage = ROOT / "_stage_hd_fonts"
existing_chars = set()
if hd_stage.exists():
    # Look at one font dir (e.g., computer.fon) to enumerate coverage
    for font_dir in hd_stage.iterdir():
        if font_dir.is_dir() and (font_dir / "computer.fon" if (font_dir / "computer.fon").exists() else font_dir).name.endswith(".fon"):
            for png in font_dir.glob("*.png"):
                # PNG filename is uppercase hex codepoint (e.g., "5F65.png")
                try:
                    codepoint = int(png.stem, 16)
                    if 0x4E00 <= codepoint <= 0x9FFF:
                        existing_chars.add(chr(codepoint))
                except ValueError:
                    pass
            break

# Actually iterate all font dirs to build union
existing_chars = set()
if hd_stage.exists():
    for font_dir in hd_stage.iterdir():
        if font_dir.is_dir():
            for png in font_dir.glob("*.png"):
                try:
                    codepoint = int(png.stem, 16)
                    if 0x4E00 <= codepoint <= 0x9FFF:
                        existing_chars.add(chr(codepoint))
                except ValueError:
                    pass

print(f"HD-staged existing CJK chars (union across fonts): {len(existing_chars)}")

new_chars = p9_chars - existing_chars
print(f"NEW chars requiring HD rasterization: {len(new_chars)}")
if new_chars:
    print("Chars:", "".join(sorted(new_chars)))
    print("Argument for _patch_hd_add_char.py:")
    print("  python _patch_hd_add_char.py " + " ".join(sorted(new_chars)))
