"""
_add_missing_keys.py — 補 48 個漏譯到 gamestrings.zh-TW.json (scope B/C/D/E/F)
scope I (Credits 4 個) 因觸發主選單位移 bug 已排除。
"""
import json
import shutil
from collections import OrderedDict
from pathlib import Path

path = Path(r'Q:\Dos_G\StarControl2\uqm-work\translations\gamestrings.zh-TW.json')
backup = path.with_suffix('.json.pre-audit-a.bak')

# Backup
if not backup.exists():
    shutil.copy2(path, backup)
    print(f"[OK] Backup: {backup}")
else:
    print(f"[SKIP] Backup exists: {backup}")

# Load
with open(path, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
print(f"[OK] Loaded {len(data)} keys")

# 48 new keys
new_keys = [
    # B · 行星掃描 UI (8)
    ('Complete!', '完成！'),
    ('data...', '資料中…'),
    ('MINERAL SCAN', '礦物掃描'),
    ('ENERGY SCAN', '能量掃描'),
    ('BIOLOGICAL SCAN', '生物掃描'),
    ('(MORE', '（更多'),
    ('MIN.SCAN', '礦物掃'),
    ('ENE.SCAN', '能量掃'),
    ('BIO.SCAN', '生物掃'),
    # C · 行星類型 (12)
    ('Gas Giant', '氣態巨行星'),
    ('Blue Gas Giant', '藍氣態巨行星'),
    ('Cyan Gas Giant', '青氣態巨行星'),
    ('Green Gas Giant', '綠氣態巨行星'),
    ('Grey Gas Giant', '灰氣態巨行星'),
    ('Orange Gas Giant', '橙氣態巨行星'),
    ('Purple Gas Giant', '紫氣態巨行星'),
    ('Red Gas Giant', '紅氣態巨行星'),
    ('Violet Gas Giant', '紫羅蘭氣態巨行星'),
    ('Yellow Gas Giant', '黃氣態巨行星'),
    ('Quasi-Degenerate', '準簡併態'),
    ('Super-Dense', '超緻密'),
    # D · Sa-Matra (2)
    ('The Sa-Matra', '薩瑪特拉'),
    ('Sa-Matra', '薩瑪特拉'),
    # E · Planet I~XVI (16)
    ('Planet I', '行星 I'),
    ('Planet II', '行星 II'),
    ('Planet III', '行星 III'),
    ('Planet IV', '行星 IV'),
    ('Planet V', '行星 V'),
    ('Planet VI', '行星 VI'),
    ('Planet VII', '行星 VII'),
    ('Planet VIII', '行星 VIII'),
    ('Planet IX', '行星 IX'),
    ('Planet X', '行星 X'),
    ('Planet XI', '行星 XI'),
    ('Planet XII', '行星 XII'),
    ('Planet XIII', '行星 XIII'),
    ('Planet XIV', '行星 XIV'),
    ('Planet XV', '行星 XV'),
    ('Planet XVI', '行星 XVI'),
    # F · 遭遇/戰鬥 HUD (10)
    ('Crimson Corp', '血紅集團'),
    ('(In response to your statement', '（回應你的發言'),
    ('Remaining Crew:', '剩餘船員:'),
    ('Cdr. Hayes', '海斯艦長'),
    ('Fleet Points: ', '艦隊分數: '),
    ('FP: ', 'FP: '),
    ('ENCOUNTER IN', '遭遇於'),
    ('Deep Space', '深空'),
    ('ENCOUNTER AT', '遭遇於'),
    ('BATTLE GROUP', '戰鬥編隊'),
]

assert len(new_keys) == 49, f"Expected 49, got {len(new_keys)}"  # B:9 C:12 D:2 E:16 F:10

added = 0
skipped = 0
for k, v in new_keys:
    if k in data:
        print(f"  [SKIP] already exists: {k!r}")
        skipped += 1
    else:
        data[k] = v
        added += 1

print(f"[OK] Added: {added}, Skipped (existing): {skipped}")

# Write back
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print(f"[OK] Written: {path}")

# Verify parse
with open(path, encoding='utf-8') as f:
    verify = json.load(f)
print(f"[OK] Verify: {len(verify)} keys total")
