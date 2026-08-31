"""Find missing constellations via wider substring search."""
import json
from pathlib import Path

OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
data = json.loads((OUT / "_ocr_multipass.json").read_text(encoding="utf-8"))

# Location hints from visual observation (approx pixel coords, r=range)
targets = {
    "squidi":     (1850, 1830, 200),   # near map(600, 420), tile r1c1
    "gruis":      (2100, 1930, 200),   # near map(700, 385)
    "herculis":   (1900, 1990, 200),   # near map(600, 365)
    "illuminati": (2050, 2170, 300),   # HUMINATI is at (785, 2174) — wait tile offset
    "giclas":     (400, 2880, 200),    # near map(105, 60)? actually iclas hit at (402, 2880)
    "serpentis":  (1600, 3060, 250),   # tile r1c1 bottom
    "scuti":      (1650, 3060, 200),
    "columbae":   (400, 2540, 200),
    "capricorni": (1550, 1300, 250),   # tile r0c1 mid
}

for name, (tx, ty, rad) in targets.items():
    nearby = [h for h in data if abs(h["x"] - tx) < rad and abs(h["y"] - ty) < rad]
    print(f"\n{name} @ ({tx},{ty}) ±{rad}:")
    for h in sorted(nearby, key=lambda x: -x["conf"])[:8]:
        print(f"  {h['text']:22s} conf={h['conf']:3d} @({h['x']:4d},{h['y']:4d})")
