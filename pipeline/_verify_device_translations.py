"""_verify_device_translations.py"""
import json
from pathlib import Path

d = json.loads(Path(r"Q:\Dos_G\StarControl2\uqm-work\translations\gamestrings.zh-TW.json").read_text(encoding="utf-8"))
devs = ["devices","Quasi Portal","Talking Pet","Utwig Bomb","Sun Device",
        "Rosy Sphere","Aqua Helix","Clear Spindle","Broken Ultron","Perfect Ultron",
        "Shofixti Maidens","Umgah Caster","Burvix Caster","1 DataPlate","2 DataPlate",
        "3 DataPlate","Taalo Shield","Egg Case","Syreen Shuttle","VUX Beast",
        "Destruct Code","Warp Pod","Wimbli's Trident","Glowing Rod","Moon Base"]
missing = [k for k in devs if k not in d]
print(f"25 device keys check: {25-len(missing)}/25 present")
if missing:
    print(f"MISSING: {missing}")
for k in devs:
    print(f"  {k:<25} -> {d.get(k, 'MISSING')}")

# Collect CJK chars
chars = set()
for k in devs:
    v = d.get(k, "")
    for c in v:
        if "\u4e00" <= c <= "\u9fff":
            chars.add(c)
print(f"\nTotal unique CJK chars: {len(chars)}")
print(f"Chars: {''.join(sorted(chars))}")
