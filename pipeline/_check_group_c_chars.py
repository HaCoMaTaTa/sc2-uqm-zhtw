"""Check char coverage after Group C for HD."""
from pathlib import Path

GROUP_C = ['algoliteruins','androsynth_ruins','burvixeseruins','excavationsite','ruins','stele']

lander_chars = ""
for f in GROUP_C:
    p = Path(f"zh-TW-addon/content/base/lander/energy/{f}.txt")
    if p.exists():
        lander_chars += p.read_text(encoding="utf-8")

lander_cjk = sorted({c for c in lander_chars if 0x4E00 <= ord(c) <= 0x9FFF})
print(f"Group C CJK unique chars: {len(lander_cjk)}")

pool = Path("translations/_used_chars.txt").read_text(encoding="utf-8")
pool_set = set(pool)
missing_pool = [c for c in lander_cjk if c not in pool_set]
print(f"Missing from SD pool: {len(missing_pool)}")
if missing_pool:
    print(" ".join(missing_pool))

hd = Path("_stage_hd_fonts/pkunk.fon")
if hd.exists():
    hd_pngs = {p.stem.upper() for p in hd.glob("*.png")}
    hd_missing = [c for c in lander_cjk if f"{ord(c):05X}" not in hd_pngs]
    print(f"\nHD pkunk.fon missing: {len(hd_missing)}")
    if hd_missing:
        print(" ".join(hd_missing))
    else:
        print("All chars covered ✓")
