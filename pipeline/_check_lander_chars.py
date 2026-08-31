"""Check if HD fonts are missing any chars from new lander/energy files."""
from pathlib import Path

FILES = ['aquahelix','burvixcaster','eggcase','fwiffo','maidens','motherark',
         'sphere','spindle','sundevice','taalodevice','ultron','umgahcaster','utwigbomb']

lander_chars = ""
for f in FILES:
    p = Path(f"zh-TW-addon/content/base/lander/energy/{f}.txt")
    if p.exists():
        lander_chars += p.read_text(encoding="utf-8")

lander_cjk = sorted({c for c in lander_chars if 0x4E00 <= ord(c) <= 0x9FFF})
print(f"Lander CJK unique chars: {len(lander_cjk)}")

pool = Path("translations/_used_chars.txt").read_text(encoding="utf-8")
pool_set = set(pool)
missing = [c for c in lander_cjk if c not in pool_set]
print(f"Missing from pool: {len(missing)}")
if missing:
    print("Missing chars:")
    print(" ".join(missing))
else:
    print("All chars covered ✓")

# Also check HD fonts (pkunk.fon rasterization)
hd_pkunk = Path("_stage_hd_fonts/pkunk.fon")
if hd_pkunk.exists():
    hd_pkunk_pngs = {p.stem for p in hd_pkunk.glob("*.png")}
    hd_missing = []
    for c in lander_cjk:
        hex_name = f"{ord(c):05X}"
        if hex_name.lower() not in {p.lower() for p in hd_pkunk_pngs}:
            hd_missing.append(c)
    print(f"\nHD pkunk.fon missing: {len(hd_missing)}")
    if hd_missing:
        print(" ".join(hd_missing[:20]))
