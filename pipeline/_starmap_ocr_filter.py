"""Filter OCR results and print clean high-confidence text hits."""
import json
import re
from pathlib import Path

OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
data = json.loads((OUT / "_ocr_raw.json").read_text(encoding="utf-8"))

# Strip pure numbers (grid axis) and low-conf items
def keep(r):
    t = r["text"]
    if re.fullmatch(r"\d+\W?", t):
        return False
    if r["conf"] < 60:
        return False
    if len(t) < 3:
        return False
    # skip pure symbols / greek noise
    if not re.search(r"[A-Za-z]{3,}", t):
        return False
    return True

clean = [r for r in data if keep(r)]
print(f"clean: {len(clean)}")
for r in clean:
    print(f"  {r['text']:24s} conf={r['conf']:3d} @({r['x']:4d},{r['y']:4d})")
