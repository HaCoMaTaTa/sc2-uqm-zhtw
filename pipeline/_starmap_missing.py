"""Diagnose: what did OCR miss? Search raw OCR for specific constellation names."""
import json
from pathlib import Path

OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
data = json.loads((OUT / "_ocr_raw.json").read_text(encoding="utf-8"))

# Constellations visible in the rendered PNG but not covered:
suspects = ["corvi", "antilae", "antliae", "apodis", "octantis", "squidi", "gruis",
            "herculis", "illuminati", "huminati", "lalande", "mira", "canopus",
            "volantis", "rigel", "persei", "piscium", "aquarii", "leonis", "ptolemae",
            "giclas", "serpentis", "scuti", "hydrae", "columbae", "geminorum",
            "normae", "capricorni", "hydrae"]

print("== Match by substring (case-insensitive) ==")
for s in suspects:
    hits = [r for r in data if s in r["text"].lower()]
    if hits:
        print(f"\n  '{s}':")
        for h in hits[:3]:
            print(f"    text={h['text']!r:22s} conf={h['conf']:3d} @({h['x']:4d},{h['y']:4d})")
    else:
        print(f"\n  '{s}': (NONE FOUND)")
