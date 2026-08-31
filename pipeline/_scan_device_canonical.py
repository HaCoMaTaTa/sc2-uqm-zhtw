"""_scan_device_canonical.py — 掃描 shipped translations 尋找 29 個 DEVICE 名的既有 canonical."""
import re
from pathlib import Path

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work\translations")

# 29 個 DEVICE_STRING_BASE 條目 (gamestrings.txt idx 149-177)
DEVICES = [
    ("devices",           149, "設備欄位標題"),
    ("Quasi Portal",      150, "準空間傳送門(阿麗露交易)"),
    ("Talking Pet",       151, "會話寵(蟾亞遺物)"),
    ("Utwig Bomb",        152, "憂特族炸彈(先驅者)"),
    ("Sun Device",        153, "太陽/恆星裝置(麥孔 Solar Manipulator)"),
    ("Rosy Sphere",       154, "玫瑰球體(先驅者遺物,厄創組件)"),
    ("Aqua Helix",        155, "蔚藍螺旋(先驅者遺物,厄創組件)"),
    ("Clear Spindle",     156, "澄澈紡錘(先驅者遺物,厄創組件)"),
    ("Broken Ultron (1)", 157, "破損厄創 stage 1"),
    ("Broken Ultron (2)", 158, "破損厄創 stage 2"),
    ("Broken Ultron (3)", 159, "破損厄創 stage 3"),
    ("Perfect Ultron",    160, "完美厄創(修復後)"),
    ("Shofixti Maidens",  161, "修烈士少女(蘇菲斯特族最後女性)"),
    ("Umgah Caster",      162, "陰嘎超波發送器"),
    ("Burvix Caster",     163, "布維超波發送器"),
    ("1 DataPlate",       164, "資料板 1"),
    ("2 DataPlate",       165, "資料板 2"),
    ("3 DataPlate",       166, "資料板 3"),
    ("Taalo Shield",      167, "塔洛防護罩(反 Dnyarri)"),
    ("Egg Case (1)",      168, "蛋殼 stage 1"),
    ("Egg Case (2)",      169, "蛋殼 stage 2"),
    ("Egg Case (3)",      170, "蛋殼 stage 3"),
    ("Syreen Shuttle",    171, "塞蓮穿透艦"),
    ("VUX Beast",         172, "VUX 巨獸"),
    ("Destruct Code",     173, "自毀密碼"),
    ("Warp Pod",          174, "曲速艙/超空間曲速艙"),
    ("Wimbli's Trident",  175, "溫布利三叉戟"),
    ("Glowing Rod",       176, "發光棒"),
    ("Moon Base",         177, "月球基地"),
]

# 需要搜的候選中譯
CANONICAL_HINTS = {
    "devices": ["裝置"],
    "Quasi Portal": ["準空間傳送門", "類空間傳送門"],
    "Talking Pet": ["會話寵"],
    "Utwig Bomb": ["憂特族炸彈", "憂特炸彈"],
    "Sun Device": ["太陽裝置", "恆星裝置", "恆星操控器", "太陽儀器"],
    "Rosy Sphere": ["玫瑰球體", "粉紅球體", "薔薇球體"],
    "Aqua Helix": ["蔚藍螺旋"],
    "Clear Spindle": ["澄澈紡錘"],
    "Broken Ultron (1)": ["破損厄創", "損壞厄創", "未完成厄創", "破碎厄創", "不完整厄創", "殘破厄創"],
    "Broken Ultron (2)": ["破損厄創", "損壞厄創", "未完成厄創", "破碎厄創", "不完整厄創"],
    "Broken Ultron (3)": ["破損厄創", "損壞厄創", "未完成厄創", "破碎厄創", "不完整厄創"],
    "Perfect Ultron": ["完美厄創", "完整厄創", "圓滿厄創"],
    "Shofixti Maidens": ["修烈士少女", "修烈士族少女"],
    "Umgah Caster": ["陰嘎超波發送器", "陰嘎播送器", "陰嘎超波"],
    "Burvix Caster": ["布維超波發送器", "布維超波", "布維斯超波"],
    "1 DataPlate": ["資料板", "數據板"],
    "Taalo Shield": ["塔洛防護罩", "塔洛盾", "塔洛護盾"],
    "Egg Case (1)": ["蛋殼", "蛋艙"],
    "Syreen Shuttle": ["塞蓮穿透艦", "塞蓮太空穿透艦", "塞蓮巡邏穿透艦"],
    "VUX Beast": ["VUX 巨獸", "VUX巨獸", "VUX 野獸", "蟒噬獸"],
    "Destruct Code": ["自毀密碼", "自毀碼", "毀滅碼"],
    "Warp Pod": ["曲速艙", "超空間曲速艙", "扭曲艙"],
    "Wimbli's Trident": ["溫布利三叉戟", "溫布利之三叉戟", "溫布利三叉"],
    "Glowing Rod": ["發光棒", "光棒", "發光杖"],
    "Moon Base": ["月球基地", "月面基地"],
}

results = {}
for en, idx, note in DEVICES:
    if en not in CANONICAL_HINTS:
        results[en] = ("N/A", [])
        continue
    hits_per_variant = {}
    for zh in CANONICAL_HINTS[en]:
        files_matching = []
        for jf in ROOT.glob("*.zh-TW.json"):
            try:
                text = jf.read_text(encoding="utf-8", errors="replace")
                if zh in text:
                    files_matching.append(jf.name)
            except Exception:
                pass
        if files_matching:
            hits_per_variant[zh] = files_matching
    results[en] = (hits_per_variant, [])

# Print report
print(f"\n{'='*70}")
print(f"DEVICE_STRING_BASE 29 條 shipped canonical 掃描")
print(f"{'='*70}\n")

canonical_count = 0
missing_count = 0
for en, idx, note in DEVICES:
    variants, _ = results[en]
    if variants == "N/A":
        continue
    if variants:
        canonical_count += 1
        # Pick the variant with most hits
        best = max(variants.items(), key=lambda x: len(x[1]))
        print(f"[{idx:3d}] {en:<25} → 【{best[0]}】(shipped in {len(best[1])} files)")
        if len(variants) > 1:
            for v, fs in variants.items():
                if v != best[0]:
                    print(f"           另有: {v} ({len(fs)} 檔)")
    else:
        missing_count += 1
        print(f"[{idx:3d}] {en:<25} → ⚠️ 無 shipped canonical")

print(f"\n總計: {canonical_count}/28 有 canonical, {missing_count}/28 需人工決策")
