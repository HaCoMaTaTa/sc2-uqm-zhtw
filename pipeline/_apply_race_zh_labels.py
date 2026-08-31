"""_apply_race_zh_labels.py — Patch 010: 星圖種族勢力圈 (SoI) 中文標籤 + 船塢 UI 艦名

Read each ships/<race>/<file>.txt from the base content, copy to
zh-TW-addon/content/base/ships/<race>/<file>.txt (shadow), and replace THREE
positions with Chinese translation:
  * index 1 (2nd `#(...)` header content)           = SoI label (star map, ship stat, encounter)
  * index N-3 (3rd-to-last `#(...)` header content) = UPPER race name (shipyard UI · v0.7.2 new)
  * index N-2 (2nd-to-last `#(...)` header content) = UPPER ship name (shipyard UI · v0.7.2 new)

All other entries (mixed-case race/ship names, captain names, description) stay English.

No engine patch needed — this is pure addon shadow-content override.

Affects (via race_strings[]):
  * pstarmap.c: star map SoI label (idx 1)
  * pstarmap.c: hover tooltip (idx 1)
  * shipstat.c: combat/melee ship stat header (idx 1)
  * encount.c: encounter dialog race header (idx 1)
  * shipyard.c DrawShipyardShipText: shipyard UI 右下角紅框 race + ship name
    (idx N-3 / N-2, uses ModuleFont — HD version has 3035 glyphs, SD has 0)

v0.7.2 (2026-08-17): 擴充為 3 個 index patch
  - 血淚教訓：用戶回報船塢右下角艦名保留英文（EARTHLING CRUISER）· 追源發現
    shipyard.c 讀 race_strings[-3] / [-2]（全大寫版）· 這兩個 index 從未被 patch。
  - v0.5.2 canonical 錯字修正：Supox Blade 舊 Ship_Names.md 譯「鐢刃艦」·
    「鐢」U+9422 為烹容器 · 意義不符 Blade · v0.7.2 修正為「刀刃艦」（暫用 · 待確認）
"""
import shutil
from pathlib import Path

BASE = Path(r"Q:\Dos_G\StarControl2\uqm-work\_megamod_content\UQM-MegaMod-Content-master\base\ships")
DST = Path(r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\ships")

# race → (filename, soi_label_idx1, race_upper_zh, ship_upper_zh)
# soi_label_idx1: 星圖勢力圈標籤（3-4 字通用族名）
# race_upper_zh: 船塢 UI 上排 race name（對應原文全大寫 EARTHLING/ARILOU 等）
# ship_upper_zh: 船塢 UI 下排 ship type（對應原文全大寫 CRUISER/SKIFF 等）
RACE_MAP = {
    #                filename           soi_label     race_upper   ship_upper
    "androsynth":  ("guardian.txt",    "安卓辛族",    "安卓辛族",   "守衛艦"),
    "arilou":      ("skiff.txt",       "阿麗露",     "阿麗露",     "快艇"),
    "chenjesu":    ("broodhome.txt",   "晶智族",     "晶智族",     "育巢艦"),   # user Q_BROODHOME
    "chmmr":       ("avatar.txt",      "查姆族",     "查姆族",     "復仇號"),
    "druuge":      ("mauler.txt",      "毒賈族",     "毒賈族",     "重擊者"),
    "human":       ("cruiser.txt",     "地球人",     "地球人",     "巡洋艦"),
    "ilwrath":     ("avenger.txt",     "蛛狂族",     "蛛狂族",     "復仇者"),
    "kohrah":      ("marauder.txt",    "柯亞族",     "柯亞族",     "掠奪者"),
    "melnorme":    ("trader.txt",      "梅諾商",     "梅諾商",     "貿易艦"),
    "mmrnmhrm":    ("xform.txt",       "姆姆族",     "姆姆族",     "變形艦"),   # user Q_MMRNMHRM_XFORM
    "mycon":       ("podship.txt",     "麥孔族",     "麥孔族",     "莢艦"),
    "orz":         ("nemesis.txt",     "歐茲",       "歐茲",       "宿敵號"),
    "pkunk":       ("fury.txt",        "普恩族",     "普恩族",     "烈憤艦"),   # v0.5.2 shipped canonical (pkunk.zh-TW.json L82/L234)
    "shofixti":    ("scout.txt",       "修烈士族",   "修烈士族",   "偵察艦"),
    "slylandro":   ("probe.txt",       "斯萊族",     "斯萊族",     "探測器"),
    "spathi":      ("eluder.txt",      "史怕族",     "史怕族",     "迴避者"),
    "supox":       ("blade.txt",       "蘇菩族",     "蘇菩族",     "刀刃艦"),   # v0.7.2 修正 · 舊「鐢刃艦」錯字（鐢=烹容器）· 待用戶最終確認
    "syreen":      ("penetrator.txt",  "塞蓮族",     "塞蓮族",     "穿透艦"),
    "thraddash":   ("torch.txt",       "撻伐族",     "撻伐族",     "火炬艦"),
    "umgah":       ("drone.txt",       "陰嘎族",     "陰嘎族",     "蜂機艦"),
    "urquan":      ("dreadnought.txt", "烏寬族",     "烏寬族",     "無畏艦"),   # R1=A: Kzer-Za 派系
    "utwig":       ("jugger.txt",      "憂特族",     "憂特族",     "重砲艦"),
    "vux":         ("intruder.txt",    "VUX",        "VUX",        "入侵者"),   # R2=A: 保英文
    "yehat":       ("terminator.txt",  "翼哈特族",   "翼哈特族",   "終結者"),
    "zoqfotpik":   ("stinger.txt",     "佐-佛-皮",   "佐-佛-皮",   "刺激者號"), # R3=A: Master_Glossary canonical
}


def process(race: str, filename: str, soi_label: str, race_upper: str, ship_upper: str):
    src_file = BASE / race / filename
    dst_file = DST / race / filename

    if not src_file.exists():
        print(f"  [SKIP] {race}: source not found → {src_file}")
        return False

    dst_file.parent.mkdir(parents=True, exist_ok=True)
    text = src_file.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Collect all `#(...)` header line indices for position-based patching.
    header_line_indices = [i for i, line in enumerate(lines) if line.startswith("#(")]

    if len(header_line_indices) < 3:
        print(f"  [ERR] {race}: fewer than 3 headers ({len(header_line_indices)}) in {src_file}")
        return False

    # Patch index 1 (SoI label · 2nd header content)
    idx1_line = header_line_indices[1]
    original_soi = lines[idx1_line + 1] if idx1_line + 1 < len(lines) else "(missing)"
    lines[idx1_line + 1] = soi_label

    # Patch index N-3 (UPPER race name · 3rd-to-last header content · shipyard UI)
    idxN3_line = header_line_indices[-3]
    original_race_upper = lines[idxN3_line + 1] if idxN3_line + 1 < len(lines) else "(missing)"
    lines[idxN3_line + 1] = race_upper

    # Patch index N-2 (UPPER ship name · 2nd-to-last header content · shipyard UI)
    idxN2_line = header_line_indices[-2]
    original_ship_upper = lines[idxN2_line + 1] if idxN2_line + 1 < len(lines) else "(missing)"
    lines[idxN2_line + 1] = ship_upper

    dst_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  [OK] {race:<12} idx1 {original_soi!r} → {soi_label!r} · "
          f"[N-3] {original_race_upper!r} → {race_upper!r} · "
          f"[N-2] {original_ship_upper!r} → {ship_upper!r}")
    return True


def main():
    ok = 0
    fail = 0
    for race, (filename, soi_label, race_upper, ship_upper) in RACE_MAP.items():
        if process(race, filename, soi_label, race_upper, ship_upper):
            ok += 1
        else:
            fail += 1
    print(f"\n=== patch 010 v0.7.2 race labels: {ok} ok, {fail} fail ({len(RACE_MAP)} total) ===")
    if fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
