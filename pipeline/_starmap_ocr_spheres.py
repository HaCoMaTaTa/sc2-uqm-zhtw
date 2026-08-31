"""Search for race sphere labels in raw OCR output at ANY confidence."""
import json
from pathlib import Path

OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
data = json.loads((OUT / "_ocr_raw.json").read_text(encoding="utf-8"))

sphere_labels = ["THRADDASH", "SUPOX", "UTWIG", "KOHR", "UR-QUAN", "URQUAN", "UMGAH",
                 "PKUNK", "YEHAT", "VUX", "MYCON", "ILWRATH", "ORZ", "DRUUGE",
                 "SPATHI", "ARILOU"]

print("== Sphere labels found in OCR ==")
for r in data:
    t = r["text"].upper()
    for lbl in sphere_labels:
        if lbl in t and len(t) >= 3:
            print(f"  {r['text']:20s} conf={r['conf']:3d} @({r['x']:4d},{r['y']:4d})")
            break

# Also count race labels appearing in legend section (y > 3550)
print("\n== Any single-word text at y in (150, 3400) (map body) with conf >= 30 ==")
print("Looking for candidates that might be race labels but OCR mangled...")
for r in data:
    t = r["text"].strip()
    if not t: continue
    y = r["y"]
    if 150 <= y <= 3400 and r["conf"] >= 20 and len(t) >= 3 and t.upper() == t:
        print(f"  {r['text']:20s} conf={r['conf']:3d} @({r['x']:4d},{r['y']:4d})")
