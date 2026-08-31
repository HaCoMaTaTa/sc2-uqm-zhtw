"""Quick OCR probe on Starmap.png — dump bounding boxes and confidence."""
import json
import os
import sys
from pathlib import Path

import cv2
import numpy as np
import pytesseract
from pytesseract import Output

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESS

IMG = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.png")
OUT_DIR = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")
OUT_DIR.mkdir(exist_ok=True)

print(f"[read] {IMG}", flush=True)
img = cv2.imread(str(IMG))
h, w = img.shape[:2]
print(f"[dim] {w} x {h}", flush=True)

# Convert to grayscale + threshold to make text stand out
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Text on this map is light on dark black background.
# Simple threshold: brighten anything above mid-grey.
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Save preview
cv2.imwrite(str(OUT_DIR / "_binary_preview.png"), binary)

print("[ocr] running tesseract (this may take ~30-60s on 3200x4258)...", flush=True)
data = pytesseract.image_to_data(binary, lang="eng", output_type=Output.DICT,
                                  config="--psm 11")  # sparse text, no orientation
n = len(data["text"])
print(f"[ocr] {n} raw records", flush=True)

# Filter valid text records
results = []
for i in range(n):
    txt = (data["text"][i] or "").strip()
    conf = int(float(data["conf"][i])) if data["conf"][i] not in ("", "-1") else -1
    if not txt or conf < 30:
        continue
    if len(txt) < 2:
        continue
    x, y, ww, hh = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
    results.append({
        "text": txt, "conf": conf,
        "x": x, "y": y, "w": ww, "h": hh,
    })

print(f"[filtered] {len(results)} text candidates (conf>=30, len>=2)", flush=True)

out_json = OUT_DIR / "_ocr_raw.json"
out_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"[wrote] {out_json}", flush=True)

# Print a small sample
print("\n-- first 30 hits --")
for r in results[:30]:
    print(f"  {r['text']:24s} conf={r['conf']:3d}  @({r['x']:4d},{r['y']:4d}) {r['w']}x{r['h']}")
