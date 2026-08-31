"""Improved OCR: multiple PSM modes + better thresholding + dedup by position."""
import json
from pathlib import Path

import cv2
import numpy as np
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

IMG = Path(r"Q:\Dos_G\StarControl2\StarControl2_TW_Localization\Reference_Material\Starmap.png")
OUT = Path(r"Q:\Dos_G\StarControl2\uqm-work\_starmap_out")

img = cv2.imread(str(IMG))
h_img, w_img = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Multiple preprocessing pipelines
preps = {}

# 1. Simple threshold
_, preps["thresh100"] = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# 2. Lower threshold to catch dim text
_, preps["thresh70"] = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)

# 3. Extract blue channel (blue labels: Corvi, Antilae, Apodis etc.)
b, g, r = cv2.split(img)
# Blue-dominant pixels
blue_mask = ((b.astype(int) - r.astype(int) > 30) & (b > 120)).astype(np.uint8) * 255
preps["blue"] = blue_mask

# 4. Adaptive threshold
preps["adaptive"] = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 51, -20)

# Save previews
for name, prep in preps.items():
    cv2.imwrite(str(OUT / f"_prep_{name}.png"), prep)
    print(f"  saved _prep_{name}.png")

# Run OCR on each preprocessed image with multiple PSM modes
all_hits = []
psm_modes = [11, 6, 12]  # sparse-no-orient, uniform-block, sparse-with-osd

for prep_name, prep_img in preps.items():
    for psm in psm_modes:
        try:
            data = pytesseract.image_to_data(prep_img, lang="eng",
                                              output_type=Output.DICT,
                                              config=f"--psm {psm}")
        except Exception as e:
            print(f"  [err] {prep_name}/psm{psm}: {e}")
            continue
        n = len(data["text"])
        added = 0
        for i in range(n):
            txt = (data["text"][i] or "").strip()
            conf = int(float(data["conf"][i])) if data["conf"][i] not in ("", "-1") else -1
            if not txt or conf < 40 or len(txt) < 3:
                continue
            if not any(c.isalpha() for c in txt):
                continue
            x, y, ww, hh = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            all_hits.append({
                "text": txt, "conf": conf, "x": x, "y": y, "w": ww, "h": hh,
                "src": f"{prep_name}/psm{psm}",
            })
            added += 1
        print(f"  {prep_name}/psm{psm}: +{added} hits")

print(f"\n[total] {len(all_hits)} raw hits before dedup")

# Dedup: keep highest-conf hit within 20 pixels
def dedup(hits):
    hits = sorted(hits, key=lambda h: -h["conf"])
    kept = []
    for h in hits:
        ok = True
        for k in kept:
            # If same/similar text at nearby position, skip
            if abs(h["x"] - k["x"]) < 40 and abs(h["y"] - k["y"]) < 30:
                if h["text"].lower() == k["text"].lower() or \
                   (len(h["text"]) > 4 and len(k["text"]) > 4 and
                    (h["text"].lower() in k["text"].lower() or k["text"].lower() in h["text"].lower())):
                    ok = False
                    break
        if ok:
            kept.append(h)
    return kept

dedup_hits = dedup(all_hits)
print(f"[dedup] {len(dedup_hits)} hits after dedup")

(OUT / "_ocr_multipass.json").write_text(
    json.dumps(dedup_hits, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"[write] {OUT / '_ocr_multipass.json'}")

# Search for previously missing constellation names
missing = ["corvi", "antilae", "apodis", "octantis", "squidi", "gruis",
           "herculis", "illuminati", "huminati", "lalande", "mira", "canopus",
           "volantis", "rigel", "persei", "piscium", "aquarii", "leonis", "ptolemae",
           "giclas", "serpentis", "scuti", "hydrae", "columbae", "geminorum",
           "normae", "capricorni"]
print("\n== Newly recovered constellations ==")
for m in missing:
    hits = [h for h in dedup_hits if m in h["text"].lower()]
    if hits:
        for h in hits[:2]:
            print(f"  {m:14s}: {h['text']:22s} conf={h['conf']:3d} @({h['x']:4d},{h['y']:4d}) src={h['src']}")
    else:
        print(f"  {m:14s}: (still missing)")
