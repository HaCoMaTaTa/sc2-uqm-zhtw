"""Quick check: are all 25 race label CJK chars in HD stage?"""
from pathlib import Path

RACES_ZH = "安卓辛族阿麗露晶智族查姆族毒賈族地球人蛛狂族柯亞族梅諾商姆族麥孔族歐茲普恩族修烈士族斯萊族史怕族蘇菩族塞蓮族撻伐族陰嘎族烏寬族憂特族翼哈特族佐佛皮"

chars_needed = set(c for c in RACES_ZH if '\u4e00' <= c <= '\u9fff')
print(f"Total unique CJK chars in 25 race labels: {len(chars_needed)}")

# Check HD stage
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

missing = chars_needed - existing
if missing:
    print(f"MISSING in HD stage: {len(missing)} chars: {' '.join(sorted(missing))}")
    print(f"Codepoints: {' '.join(f'U+{ord(c):04X}' for c in sorted(missing))}")
else:
    print("[OK] All chars present in HD stage - no rebuild needed.")
