"""Look for race sphere labels in raw OCR at any conf, including partial matches."""
import json
import re
from pathlib import Path

OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
data = json.loads((OUT / "_ocr_raw.json").read_text(encoding="utf-8"))

# Known sphere label letter patterns (partial)
patterns = {
    "THRADDASH": ["THR", "RAD", "DAS", "ASH", "HRA", "RDD"],
    "SUPOX": ["SUP", "POX", "UPO"],
    "UTWIG": ["UTW", "TWI", "WIG"],
    "KOHR-AH": ["KOH", "OHR", "HR-", "R-A", "-AH"],
    "UR-QUAN": ["UR-", "R-Q", "QUA", "UAN"],
    "UMGAH": ["UMG", "MGA", "GAH"],
    "PKUNK": ["PKU", "KUN", "UNK"],
    "YEHAT": ["YEH", "EHA", "HAT"],
    "VUX": ["VUX"],
    "MYCON": ["MYC", "YCO", "CON"],
    "ILWRATH": ["ILW", "LWR", "WRA", "RAT", "ATH"],
    "ORZ": ["ORZ"],
    "DRUUGE": ["DRU", "RUU", "UUG", "UGE"],
    "SPATHI": ["SPA", "PAT", "ATH", "THI"],
    "ARILOU": ["ARI", "RIL", "ILO", "LOU"],
    "ZOQ": ["ZOQ"],
    "FOT": ["FOT"],
    "PIK": ["PIK"],
}

print("== Loose match for sphere labels (upper-case detected fragments) ==")
found = {k: [] for k in patterns}
for r in data:
    t = r["text"].upper()
    if len(t) < 3 or r["conf"] < 20:
        continue
    if r["y"] > 3400:  # skip legend area
        continue
    for name, pats in patterns.items():
        for p in pats:
            if p in t:
                found[name].append(r)
                break

for name, hits in found.items():
    if hits:
        print(f"\n  {name}:")
        for h in hits[:5]:
            print(f"    text={h['text']!r:20s} conf={h['conf']:3d} @({h['x']:4d},{h['y']:4d}) {h['w']}x{h['h']}")
