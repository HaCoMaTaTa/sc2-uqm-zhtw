"""Check char coverage after Group B for HD."""
from pathlib import Path

GROUP_B = ['chmmrbase','chmmrhome','destroyedbase','earthbase','precursorbase',
           'shofixtibase','spathimonument','syreenbase','syreenvault',
           'urquanwreck','zfpcolony']

lander_chars = ""
for f in GROUP_B:
    p = Path(f"zh-TW-addon/content/base/lander/energy/{f}.txt")
    if p.exists():
        lander_chars += p.read_text(encoding="utf-8")

lander_cjk = sorted({c for c in lander_chars if 0x4E00 <= ord(c) <= 0x9FFF})
print(f"Group B CJK unique chars: {len(lander_cjk)}")

pool = Path("translations/_used_chars.txt").read_text(encoding="utf-8")
pool_set = set(pool)
missing_from_pool = [c for c in lander_cjk if c not in pool_set]
print(f"Missing from pool: {len(missing_from_pool)}")
if missing_from_pool:
    print(" ".join(missing_from_pool))

# Check HD pkunk.fon for missing chars (representative HD font)
hd = Path("_stage_hd_fonts/pkunk.fon")
if hd.exists():
    hd_pngs = {p.stem.upper() for p in hd.glob("*.png")}
    hd_missing = []
    for c in lander_cjk:
        hex_name = f"{ord(c):05X}"
        if hex_name not in hd_pngs:
            hd_missing.append(c)
    print(f"\nHD pkunk.fon missing: {len(hd_missing)}")
    if hd_missing:
        print(" ".join(hd_missing))
    else:
        print("All chars covered ✓")
