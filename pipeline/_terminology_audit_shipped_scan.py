"""
Terminology Audit Phase 2 · shipped JSON 跨族譯法統計 + Voice 稽核

Usage:
    python _terminology_audit_shipped_scan.py

Outputs:
    _terminology_shipped_matrix_2026-08-18.csv    # 每個 EN×變體 × 每個 JSON 的次數矩陣
    _terminology_audit_phase2_2026-08-18.md       # 跨族歧異報告 + Voice 統計 + 決策建議

策略：
- 對每個 seed EN，掃所有 shipped JSON 找已知變體
- 統計每族用什麼、多少次 → 產跨族矩陣
- 找「多譯法並存」的 EN → 標為 discrepancy
- Voice 自稱統計（audit-policy 第 6 層）
- 只掃 dialog value（不掃 _notes / 不掃 key）
"""
from __future__ import annotations
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

UQM_WORK = Path(r"q:\Dos_G\StarControl2\uqm-work")
TRANSLATIONS = UQM_WORK / "translations"
DATE = "2026-08-18"

# ─────────────────────────────────────────────────────────
# Seed canonical + known variants
# 每個 EN 列出：[canonical, obsolete1, obsolete2, ...]
# 掃描會統計每個變體的出現次數
# ─────────────────────────────────────────────────────────
SEEDS: dict[str, dict[str, list[str]]] = {
    # ═════════ 種族名 ═════════
    "race": {
        "Ur-Quan":          ["烏寬族", "烏寬", "烏爾寬", "爾奎人", "烏寬人"],
        "Kzer-Za":          ["烏寬克澤札", "克澤札", "克澤-札", "克澤咋", "克澤"],
        "Kohr-Ah":          ["烏寬柯亞", "柯亞族", "柯亞", "柯耳阿", "科爾阿"],
        "Chenjesu":         ["晶智族", "晶智", "蒼捷蘇族", "陳傑蘇族", "珍捷蘇族"],
        "Mmrnmhrm":         ["姆姆族", "姆姆", "米米族"],
        "Chmmr":            ["查姆族", "查姆", "卡姆爾族"],
        "Shofixti":         ["修烈士族", "修烈士", "蘇菲斯特族", "蘇菲斯特", "修飛族"],
        "Yehat":            ["翼哈特族", "翼哈特", "葉哈特族", "葉哈特", "葉海特族"],
        "Yehat Rebels":     ["翼哈特叛軍", "葉哈特叛軍"],
        "Arilou":           ["阿麗露", "阿麗露族", "艾拉羅族"],
        "Syreen":           ["塞蓮族", "塞蓮", "賽蓮族", "西蓮族"],
        "Spathi":           ["史怕族", "史怕", "斯帕蒂族", "史帕族"],
        "Safe Ones":        ["平安族", "史怕族最高議會"],
        "Umgah":            ["陰嘎族", "陰嘎", "阿姆嘎族", "阿姆嘎", "姆嘎族"],
        "Mycon":            ["麥孔族", "麥孔", "梅蒙族"],
        "VUX":              ["VUX", "烏克斯族"],
        "Ilwrath":          ["蛛狂族", "蛛狂", "伊爾雷斯族", "艾瓦斯族"],
        "Androsynth":       ["安卓辛族", "安卓辛", "安卓合成族", "雌雄同體人"],
        "Utwig":            ["憂特族", "憂特", "烏特威格族"],
        "Supox":            ["蘇菩族", "蘇菩", "蘇波族", "蘇波"],
        "Pkunk":            ["普恩族", "普恩", "普恩克族"],
        "Thraddash":        ["撻伐族", "撻伐", "撒達許族", "撒達許", "斯拉達族"],
        "Slylandro":        ["斯萊族", "斯萊", "斯萊藍卓族"],
        "Slylandro Probe":  ["斯萊探測器", "探測器"],
        "Druuge":           ["毒賈族", "毒賈", "德魯族", "德魯", "德魯格族"],
        "Melnorme":         ["梅諾商", "梅爾諾", "梅爾諾姆", "梅諾族"],
        "Orz":              ["歐茲族", "歐茲", "奧茲族", "奧茲"],
        "Zoq-Fot-Pik":      ["佐-佛-皮", "佐佛皮族", "佐-佛-皮族"],
        "Dnyarri":          ["蟾亞族", "蟾亞", "尼亞里族", "尼亞里", "迪亞里族"],
        "Talking Pet":      ["會話寵", "會話寵物"],
        "Taalo":            ["塔洛族", "塔洛"],
        "Precursor":        ["先驅者", "先驅", "先民", "祖先"],
        "Burvixese":        ["布維族", "波維克塞族"],
        "Mael-Num":         ["梅努族", "邁爾努族"],
        "Sentient Milieu":  ["感知聯盟", "意識邦聯", "感知界"],
    },
    # ═════════ 艦艇名 ═════════
    "ship": {
        "Dreadnought":      ["無畏艦", "無畏", "恐懼艦", "無敵艦"],
        "Marauder":         ["掠奪者", "掠劫者", "襲擊者"],
        "Broodhome":        ["母巢艦", "育巢艦", "母船", "繁殖巢"],
        "Avatar":           ["復仇號", "阿凡達", "化身艦"],
        "Terminator":       ["終結者", "終結者號", "終止者"],
        "Fury":             ["烈憤艦", "憤怒者", "火炬艦", "愠怒者"],
        "Scout":            ["偵察艦", "偵察機", "偵察者"],
        "Skiff":            ["快艇", "小艇", "輕舟"],
        "Penetrator":       ["穿透艦", "穿透船", "破壁艦"],
        "Eluder":           ["迴避者", "潛匿艦", "閃匿艦", "躲避者", "逃避者"],
        "Drone":            ["蜂機艦", "無人機", "蜂型艦"],
        "Intruder":         ["入侵者", "入侵艦", "闖入者"],
        "Guardian":         ["守衛艦", "守護者", "護衛艦", "守護神"],
        "Avenger":          ["復仇者", "復仇艦"],
        "Podship":          ["莢艦", "豆莢艦", "莢船"],
        "Probe":            ["斯萊探測器", "探測器", "探測船", "探測機"],
        "Jugger":           ["重砲艦", "重擊者"],
        "Blade":            ["鋒刃艦", "鐢刃艦", "刀鐤", "刃艦", "刀刃號"],
        "Torch":            ["火炬艦", "火把", "火燄艦"],
        "Mauler":           ["重擊者", "重槌者"],
        "Nemesis":          ["宿敵號", "宿敵", "復仇者號"],
        "Stinger":          ["刺針號", "刺激者號", "螫針"],
        "Vindicator":       ["復仇者號", "復仇艦"],
        "Tobermoon":        ["土柏月亮號"],
    },
    # ═════════ 角色名 ═════════
    "character": {
        "Commander Hayes":  ["海斯艦長", "海斯", "海斯指揮官"],
        "Talana":           ["泰蘭娜", "塔拉娜"],
        "Fwiffo":           ["費佛", "費弗", "菲佛"],
        "Trade Master Greenish": ["綠光貿易官", "綠光"],
        "ZEX":              ["澤克斯", "傑斯"],
        "Burton":           ["巴頓艦長", "巴頓"],
        "Tanaka":           ["田中"],
        "Katana":           ["武士刀"],
        "Daikon":           ["蘿蔔"],
        "Farnsworth":       ["方斯渥教授", "方斯渥"],
        "Rand":             ["蘭德艦長", "蘭德"],
        "Jud the Vug":      ["賈德·魔怪", "賈德魔怪", "沃格·賈德", "無法名狀的賈德"],
    },
    # ═════════ 科技/文物 ═════════
    "tech": {
        "Sa-Matra":         ["薩瑪特拉", "薩-瑪特拉", "薩·瑪特拉", "莎瑪特拉"],
        "Ultron":           ["厄創", "厄創器", "奧創裝置", "奧創", "終極"],
        "Rosy Sphere":      ["玫瑰球體", "玫瑰球", "粉紅球"],
        "Aqua Helix":       ["蔚藍螺旋", "水螺旋", "青玉螺旋"],
        "Clear Spindle":    ["澄澈紡錘", "澄澈紡錐", "清澈紡錘"],
        "Sun Device":       ["太陽裝置", "太陽器"],
        "Taalo Shield":     ["塔洛防護罩", "塔洛盾", "塔洛之盾"],
        "Glowing Rod":      ["發光魔杖", "發光棒", "發光魔法棒"],
        "Trident of Wimbli": ["温布利三叉戟", "溫布利三叉戟", "Wimbli 三叉戟"],
        "Vortex Spawner":   ["漩渦生成器"],
        "Portal Spawner":   ["傳送門生成器", "傳送門發生器", "傳送門產生器"],
        "Bomb":             ["炸彈"],
        "Deep Child":       ["深層幼體", "深子", "深淵之子"],
        "Excruciator":      ["苦刑器", "極痛裝置"],
        "Glory Device":     ["榮耀彈", "榮耀裝置", "光榮裝置"],
        "BUTT Missile":     ["屁彈飛彈", "BUTT 飛彈"],
        "limpet":           ["吸附雷", "吸附機", "吸附砲"],
        "Fusion Bolt":      ["融合彈"],
        "F.R.I.E.D. Blades": ["旋轉刀刃"],
        "Photon Crystals":  ["光子晶體彈"],
        "Plasmoids":        ["電漿團"],
        "Antimatter Cone":  ["反物質錐"],
        "Bubble Cannon":    ["泡泡彈"],
        "Blazer Form":      ["燃燒衝撞形態"],
        "Flame Jets":       ["火焰噴流"],
        "Twin Pulsar Cannons": ["雙脈衝砲"],
        "Autotracking Laser": ["自動追蹤雷射"],
        "Particle Beam":    ["粒子束"],
        "Syreen Song":      ["塞蓮之歌"],
        "Glob Launcher":    ["漿團發射器"],
        "Triple Bullets":   ["三連發彈"],
        "Antimatter Spray": ["反物質吐射"],
        # 模組
        "Hellbore Cannon":  ["火獄穿甲炮", "火獄穿甲砲", "地獄砲", "地獄鑽砲"],
        "Shiva Furnace":    ["濕婆熔爐", "希瓦爐", "希瓦熔爐"],
        "Ion-Bolt Gun":     ["離子波砲", "離子束槍"],
        "Fusion Blaster":   ["融合爆能砲", "融合爆能"],
        "Point-Defense Laser": ["點防禦雷射", "點防禦"],
        "Blaster":          ["爆能砲", "爆能"],
        "Dynamo":           ["發電機", "發電機模組", "能量發電機"],
        "Fuel Tank":        ["燃料艙"],
        "Crew Pod":         ["船員艙"],
        "Storage Bay":      ["貨艙", "儲藏艙"],
        "lander":           ["登陸艇", "登陸器", "行星登陸艇"],
        "Star Control":     ["星際指揮部", "星控", "星球控制"],
        "HyperSpace":       ["超空間"],
        "QuasiSpace":       ["準空間"],
        "TrueSpace":        ["真實空間"],
        "HyperWave":        ["超波通訊", "超波"],
        "FunRom":           ["歡樂晶片", "歡樂ROM"],
        "slave shield":     ["奴役護盾", "奴役制度"],
    },
    # ═════════ 地點名 ═════════
    "place": {
        "Sol":              ["太陽系", "索爾", "Sol"],
        "Earth":            ["地球"],
        "Sirius":           ["天狼星"],
        "Betelgeuse":       ["參宿四"],
        "Procyon":          ["南河三"],
        "Arcturus":         ["大角星", "大角"],
        "Vega":             ["織女星", "織女一"],
        "Vulpeculae":       ["狐狸座"],
        "Draconis":         ["天龍座"],
        "Alpha Tucanae":    ["杜鵑座", "杜鵑座 α"],
        "Alpha Pavonis":    ["孔雀座", "孔雀座 α"],
        "Beta Corvi":       ["烏鴉座 β", "烏鴉座"],
        "Delta Crateris":   ["巨爵座 δ", "巨爵座"],
        "Zeta Persei":      ["英仙座 ζ", "英仙座"],
        "Zeta Sextantis":   ["六分儀座 ζ", "六分儀座"],
        "Beta Brahe":       ["第谷", "第谷 β", "布拉赫", "布拉赫β"],
        "Zeta Hyades":      ["畢宿星團", "畢宿星團ζ", "畢宿ζ"],
        "Groombridge":      ["葛倫布利吉"],
        "Giclas":           ["吉克拉斯"],
        "Oort Cloud":       ["歐特雲", "Oort 雲"],
        "Unzervalt":        ["恩澤伐特", "船帆星 II"],
        "Kyabetsu":         ["高麗菜"],
        "Falayalaralfali":  ["法拉雅拉拉法利"],
        "Syra":             ["席拉"],
        "Delta Gorno":      ["戈爾諾", "戈爾諾座 δ"],
        "Alpha Cerenkov":   ["契倫科夫 α", "契倫科夫"],
        "Delta Lyncis":     ["天貓座 δ", "天貓座"],
        "Organon":          ["歐加農", "奧甘農"],
    },
    # ═════════ 勢力/教義/宗教 ═════════
    "faction": {
        "Alliance of Free Stars": ["自由星系聯盟", "自由星辰聯盟"],
        "New Alliance of Free Stars": ["新自由星系聯盟"],
        "Ur-Quan Hierarchy":      ["烏寬戰奴階層", "烏寬階層"],
        "Battle Thrall":          ["戰奴"],
        "Fallow Slave":           ["禁足奴族"],
        "Doctrinal War":          ["教義戰爭"],
        "Doctrine of Slavery":    ["奴役派"],
        "Doctrine of Extermination": ["滅絕派"],
        "Path of Now and Forever":  ["現在與永恆之道", "今與永恆之道"],
        "Eternal Doctrine":       ["永恆教條"],
        "Utwig Proctorate":       ["憂特監督團"],
        "Crimson Corporation":    ["血紅集團", "紅色財團"],
        "Culture Nineteen":       ["第十九文化"],
        "Slave Revolt":           ["奴隸起義"],
        "Slave War":              ["奴隸戰爭"],
        "Great Beyond":           ["蒼宇彼方"],
        # 宗教
        "Juffo-Wup":              ["聖源", "Juffo-Wup"],
        "Frungy":                 ["苙戎奇", "Frungy"],
        "Dogar":                  ["多加"],
        "Kazon":                  ["卡宗"],
        "The Sport of Kings":     ["諸王之運動"],
        "Void":                   ["虛空"],
        "Non":                    ["異類", "Non"],
        # 資源與貨幣
        "Credits":                ["星幣", "信用點數"],
        "Interstar Credits":      ["星幣"],
        "RU":                     ["RU", "資源單位"],
    },
    # ═════════ 招牌感嘆/擬聲 ═════════
    "interjection": {
        "Kyaiee!":     ["殺呀", "Kyaiee"],
        "Hyai!":       ["唉呀", "Hyai"],
        "HYAIEEE!":    ["嗚呀啊", "HYAIEEE"],
        "Ha!":         ["Ha!"],
        "Banzai!":     ["萬歲", "Banzai"],
        "Aieee!":      ["Aieee", "啊咦", "啊咿"],
        "Lykeee-lieee!": ["Lykeee-lieee"],
        "hee-hee-hee": ["嘿嘿嘿", "hee-hee-hee"],
        "Ho-ho-ho":    ["Ho-ho-ho"],
        "SNORT!":      ["SNORT", "哼嗤"],
        "HARG!":       ["HARG", "哈哈哈"],
        "Har! Har!":   ["Har! Har!"],
    },
}

# ─────────────────────────────────────────────────────────
# Voice self-references（audit-policy 第 6 層）
# ─────────────────────────────────────────────────────────
VOICE_TERMS = [
    # 現代/中性
    "我方", "我們", "我族", "我等", "咱們", "咱倆", "咱",
    # 文言（v0.7 應減少）
    "吾", "吾等", "爾", "爾等", "汝", "之", "乃", "哉", "焉", "此等", "彼等",
    # 敬語/謙語
    "敝方", "敝下", "敝人", "本人", "本座", "本官", "本尊",
    # 特殊自稱
    "小的", "本蟹", "俺", "本武士", "本商號", "本合約代表人",
]

# ─────────────────────────────────────────────────────────
# Files
# ─────────────────────────────────────────────────────────
# 只掃 comm dialog + 少數 UI · 排除 backup/partial/v2/v3
def is_target_json(p: Path) -> bool:
    n = p.name
    if not n.endswith(".zh-TW.json"):
        return False
    if ".v" in n or ".pre-" in n or ".bak" in n or "partial" in n or ".merged." in n:
        return False
    return True


TARGET_JSONS = sorted(p for p in TRANSLATIONS.glob("*.zh-TW.json") if is_target_json(p))


# ─────────────────────────────────────────────────────────
# Scanning
# ─────────────────────────────────────────────────────────
def flatten_dialog(obj, out: list) -> None:
    """遞迴收集所有 dialog value（跳過 _notes / 跳過 key 名）"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k.startswith("_"):
                continue  # skip _notes
            flatten_dialog(v, out)
    elif isinstance(obj, list):
        for item in obj:
            flatten_dialog(item, out)
    elif isinstance(obj, str):
        out.append(obj)


def count_non_overlapping(text: str, variants: list[str]) -> dict[str, int]:
    """
    對同一 EN 的多個 variants 做 non-overlapping 計數。
    做法：按長度降序，先計最長 variant，計完後將其匹配位置遮蔽（`\x01`），
    避免短 variant 重複計到「短 variant 為長 variant 之子字串」的情況。
    例：variants=['陰嘎族','陰嘎']，text 含 3 個「陰嘎族」+ 1 個獨立「陰嘎」
        → 「陰嘎族」= 3、「陰嘎」= 1（非 4）
    """
    counts = {v: 0 for v in variants if v}
    tmp = text
    for v in sorted((v for v in variants if v), key=len, reverse=True):
        n = tmp.count(v)
        counts[v] = n
        if n > 0:
            tmp = tmp.replace(v, "\x01" * len(v))
    return counts


def scan_json(path: Path) -> tuple[dict, dict]:
    """
    Returns:
        variant_counts: dict[category][EN][variant] -> count
        voice_counts: dict[voice_term] -> count
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  skip {path.name}: {e}", file=sys.stderr)
        return {}, {}
    dialogs = []
    flatten_dialog(data, dialogs)
    all_text = "\n".join(dialogs)

    variant_counts = {}
    for cat, seeds in SEEDS.items():
        variant_counts[cat] = {}
        for en, variants in seeds.items():
            variant_counts[cat][en] = count_non_overlapping(all_text, variants)

    # voice terms 也做 non-overlapping，避免「吾」計到「吾等」
    voice_counts = count_non_overlapping(all_text, VOICE_TERMS)

    return variant_counts, voice_counts


# ─────────────────────────────────────────────────────────
# Report
# ─────────────────────────────────────────────────────────
def write_matrix_csv(all_data: dict) -> Path:
    out = UQM_WORK / f"_terminology_shipped_matrix_{DATE}.csv"
    races = sorted(all_data.keys())
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Category", "English", "Variant", *races, "Total"])
        for cat in SEEDS:
            for en, variants in SEEDS[cat].items():
                for var in variants:
                    row = [cat, en, var]
                    total = 0
                    for r in races:
                        c = all_data[r]["variants"].get(cat, {}).get(en, {}).get(var, 0)
                        row.append(c)
                        total += c
                    row.append(total)
                    if total > 0:
                        w.writerow(row)
    return out


def write_voice_csv(all_data: dict) -> Path:
    out = UQM_WORK / f"_terminology_shipped_voice_{DATE}.csv"
    races = sorted(all_data.keys())
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Voice Term", *races, "Total"])
        for term in VOICE_TERMS:
            row = [term]
            total = 0
            for r in races:
                c = all_data[r]["voice"].get(term, 0)
                row.append(c)
                total += c
            row.append(total)
            w.writerow(row)
    return out


def write_phase2_report(all_data: dict, matrix_csv: Path, voice_csv: Path) -> Path:
    out = UQM_WORK / f"_terminology_audit_phase2_{DATE}.md"
    races = sorted(all_data.keys())

    # 找 discrepancies：對每個 EN，若有 ≥2 個變體出現次數 > 0 → 標為 discrepancy
    def find_discrepancies():
        """回傳 list of (severity, cat, en, per_race_counts, primary, minor)"""
        result = []
        for cat in SEEDS:
            for en, variants in SEEDS[cat].items():
                # 各變體的全域總數
                global_totals = {v: 0 for v in variants}
                # per_race: dict[race][var] -> count
                per_race = {r: {} for r in races}
                for r in races:
                    for v in variants:
                        c = all_data[r]["variants"].get(cat, {}).get(en, {}).get(v, 0)
                        per_race[r][v] = c
                        global_totals[v] += c
                nonzero = {v: n for v, n in global_totals.items() if n > 0}
                if len(nonzero) < 2:
                    continue
                # primary = 用最多的變體
                primary = max(nonzero.items(), key=lambda kv: kv[1])
                # minors
                minors = {v: n for v, n in nonzero.items() if v != primary[0]}
                # severity
                total = sum(nonzero.values())
                minor_share = sum(minors.values()) / total
                if minor_share > 0.4:
                    sev = "🔴"
                elif minor_share > 0.15:
                    sev = "🟠"
                else:
                    sev = "🟡"
                result.append((sev, cat, en, per_race, primary, minors, total))
        return result

    discrepancies = find_discrepancies()
    high = [d for d in discrepancies if d[0] == "🔴"]
    mid = [d for d in discrepancies if d[0] == "🟠"]
    low = [d for d in discrepancies if d[0] == "🟡"]

    with out.open("w", encoding="utf-8") as f:
        f.write(f"# Phase 2 · shipped JSON 譯法統計 + 跨族歧異 + Voice 稽核（{DATE}）\n\n")
        f.write("> 自動化掃描 · 由 `_terminology_audit_shipped_scan.py` 產出。\n")
        f.write(f"> **策略**：shipped-preference · 以實際 JSON 使用量為主 · 回頭建議修規範檔對齊。\n\n")
        f.write("## 統計\n\n")
        f.write(f"- 掃描 shipped JSON：**{len(TARGET_JSONS)}** 檔（純 dialog value · 排除 `_notes` / key / backup / partial）\n")
        f.write(f"- Seed canonical EN：**{sum(len(v) for v in SEEDS.values())}** 條（跨 {len(SEEDS)} 類別）\n")
        f.write(f"- Voice terms 統計：**{len(VOICE_TERMS)}** 個自稱/文言助詞\n")
        f.write(f"- 檢測到跨族譯法歧異：**{len(discrepancies)}** 項\n")
        f.write(f"  - 🔴 高嚴重度（次要譯法占比 >40%）：**{len(high)}**\n")
        f.write(f"  - 🟠 中嚴重度（占比 15-40%）：**{len(mid)}**\n")
        f.write(f"  - 🟡 低嚴重度（占比 <15% · 主要為個位數散落）：**{len(low)}**\n\n")
        f.write(f"**原始資料**：\n")
        f.write(f"- 譯法矩陣 CSV：`{matrix_csv.name}`\n")
        f.write(f"- Voice 統計 CSV：`{voice_csv.name}`\n\n")
        f.write("---\n\n")

        def dump_discrepancy_group(title: str, group: list) -> None:
            f.write(f"## {title}（{len(group)} 項）\n\n")
            for idx, (sev, cat, en, per_race, primary, minors, total) in enumerate(
                sorted(group, key=lambda x: -x[6]), 1
            ):
                p_var, p_count = primary
                f.write(f"### #{idx} · `{en}` 【{cat}】· 主流「{p_var}」× {p_count}（{p_count/total:.0%}）\n\n")
                # 次要譯法
                for m_var, m_count in sorted(minors.items(), key=lambda kv: -kv[1]):
                    # 找是哪些 race 用了此變體
                    users = []
                    for r, counts in per_race.items():
                        if counts.get(m_var, 0) > 0:
                            users.append(f"{r}×{counts[m_var]}")
                    users_str = "、".join(users[:5])
                    if len(users) > 5:
                        users_str += f" …+{len(users)-5}"
                    f.write(f"- ⚠️ **「{m_var}」× {m_count}**（{m_count/total:.0%}）· 出處：{users_str}\n")
                f.write(f"- **建議**：shipped-preference → 統一為「**{p_var}**」；修規範檔對齊（若尚未鎖為此）；修 shipped 少數異體以達 100%\n")
                f.write(f"- **決策**：A. 統一為「{p_var}」 · B. 保留現況 · C. 自訂\n\n")
            f.write("---\n\n")

        if high:
            dump_discrepancy_group("🔴 高嚴重度歧異", high)
        if mid:
            dump_discrepancy_group("🟠 中嚴重度歧異", mid)
        if low:
            dump_discrepancy_group("🟡 低嚴重度歧異", low)

        # ═════════ Voice 稽核 ═════════
        f.write("## Voice 定量稽核（audit-policy 第 6 層）\n\n")
        f.write("每族自稱/文言助詞出現次數。**閾值**：文言助詞（吾/吾等/爾/爾等/汝/之/乃/哉）應接近 0（v0.7 現代體政策）· 例外為 v0.4 尚未 Rebuild-Compare 的族。\n\n")
        # 找每族文言助詞總數 >20 的 → 高汙染
        formal_chars = ["吾", "吾等", "爾", "爾等", "汝", "之", "乃", "哉", "焉"]
        f.write("### 文言污染排行（每族文言助詞總和 >20）\n\n")
        pollution = []
        for r in races:
            total = sum(all_data[r]["voice"].get(c, 0) for c in formal_chars)
            pollution.append((r, total))
        pollution.sort(key=lambda x: -x[1])
        f.write("| 族 | 吾 | 吾等 | 爾 | 爾等 | 汝 | 之 | 乃 | 哉 | 焉 | 總和 |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for r, tot in pollution:
            if tot < 20:
                continue
            v = all_data[r]["voice"]
            f.write(f"| **{r}** | {v.get('吾',0)} | {v.get('吾等',0)} | {v.get('爾',0)} | {v.get('爾等',0)} | {v.get('汝',0)} | {v.get('之',0)} | {v.get('乃',0)} | {v.get('哉',0)} | {v.get('焉',0)} | **{tot}** |\n")
        f.write("\n> 「之」多為現代連詞（星光之意/永恆之道）· 不必然文言污染 · 需人工抽查。\n\n")

        # 每族主要自稱
        f.write("### 每族主要自稱使用（我方 / 我族 / 我等 / 我們 / 特殊）\n\n")
        f.write("| 族 | 我方 | 我族 | 我等 | 我們 | 敝方 | 本官 | 本座 | 本尊 | 俺 | 小的 | 咱們 |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for r in races:
            v = all_data[r]["voice"]
            f.write(f"| **{r}** | {v.get('我方',0)} | {v.get('我族',0)} | {v.get('我等',0)} | {v.get('我們',0)} | {v.get('敝方',0)} | {v.get('本官',0)} | {v.get('本座',0)} | {v.get('本尊',0)} | {v.get('俺',0)} | {v.get('小的',0)} | {v.get('咱們',0)} |\n")
        f.write("\n---\n\n## 附註\n\n")
        f.write("- 此報告只**偵測**歧異 · 不動 JSON · 實際 retrofit 需另行執行\n")
        f.write("- 「建議」皆為 shipped-preference：以主流用法為 canonical、少數為次要 → 建議 retrofit 少數對齊主流\n")
        f.write("- 若你想反其道（rules-preference），需在決策時逐項推翻建議\n")
        f.write("- Voice 統計是「詞頻」· 不是「voice 塌陷」判定 · 塌陷需結合英文原文情境分析\n")
    return out


# ─────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────
def main() -> int:
    if not TRANSLATIONS.exists():
        print(f"translations not found: {TRANSLATIONS}", file=sys.stderr)
        return 1
    print(f"Scanning {len(TARGET_JSONS)} JSON files...")
    all_data = {}
    for p in TARGET_JSONS:
        race = p.name.replace(".zh-TW.json", "")
        var, voice = scan_json(p)
        all_data[race] = {"variants": var, "voice": voice}
    print(f"Scanned {len(all_data)} races")
    matrix_csv = write_matrix_csv(all_data)
    voice_csv = write_voice_csv(all_data)
    md_path = write_phase2_report(all_data, matrix_csv, voice_csv)
    print(f"Wrote: {matrix_csv}")
    print(f"Wrote: {voice_csv}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
