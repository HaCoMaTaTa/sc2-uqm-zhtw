"""_check_device_hd_chars.py — Verify 81 device CJK chars are all in HD stage."""
from pathlib import Path

DEVICE_CHARS = "三修傳光利創厄叉嘎器地基塔塞士太女完密寵少布彈憂戟損料旋族曲會月板梭棒殼毀波洛準溫澄澈炸烈特獸玫珍球瑰發破碼空紡維罩置美自艙蓮蔚藍蛋螺裝話護資超送速錘門間防陰陽體"
chars_needed = set(c for c in DEVICE_CHARS if "\u4e00" <= c <= "\u9fff")
print(f"Device unique CJK chars: {len(chars_needed)}")

hd_stage = Path(r"Q:\Dos_G\StarControl2\uqm-work\_stage_hd_fonts")
existing = set()
if hd_stage.exists():
    for font_dir in hd_stage.iterdir():
        if font_dir.is_dir():
            for png in font_dir.glob("*.png"):
                try:
                    cp = int(png.stem, 16)
                    if 0x4E00 <= cp <= 0x9FFF:
                        existing.add(chr(cp))
                except ValueError:
                    pass

missing = sorted(chars_needed - existing)
if missing:
    print(f"MISSING in HD stage: {len(missing)} chars")
    print(f"Chars: {' '.join(missing)}")
    print(f"Codepoints: {' '.join(f'U+{ord(c):04X}' for c in missing)}")
    print(f"\nTo patch, run:")
    print(f"  python _patch_hd_add_char.py {' '.join(missing)}")
else:
    print("[OK] All device chars present in HD stage - no rebuild needed.")
