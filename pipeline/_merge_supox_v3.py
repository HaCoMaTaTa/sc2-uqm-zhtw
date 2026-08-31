"""Merge supox v3 partials 1-3 into full v3 JSON preserving shipped key order + v3 _notes.

Usage: python _merge_supox_v3.py
Output: translations/supox.zh-TW.v3.json
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).parent
TR = ROOT / 'translations'

SHIPPED = TR / 'supox.zh-TW.json'
PARTIALS = [TR / f'supox.zh-TW.v3.partial-{i}.json' for i in (1, 2, 3)]
OUT = TR / 'supox.zh-TW.v3.json'

V3_NOTES = [
    "v0.7 Rebuild-Compare v3 — Supox (蘇菩族) comm dialog · clean-room + shipped 對比 + 逐項擇優。",
    "字型 supox.fon (無專用,共用 slab), AlienTextWidth = STD (~224px SD)。",
    "===== 角色 voice (dossier §四 v0.7) =====",
    "  Supox 蘇菩族 = 植物演化智慧生命;溫和禮貌、園藝比擬、道德高尚、無心機。",
    "  Utwig 憂特族的『葉』,Utwig 為『根』:共生哲學 (共生是本能,不是選擇)。",
    "  自稱:『我方』/『我方蘇菩』/『共生之枝』(SYMBIOTS)/『根系之聲』(DO_THIS_BEFORE_SPACE)/",
    "        『綠色的守望者』(HELLO_BEFORE_KOHRAH_SPACE_2)/『執行者』(GOOD_HINTS)",
    "  【廢除】『吾等蘇菩』(Phase 14c++ 遺留) → v3 全改『我方蘇菩』",
    "  稱訪客 canonical:『艦長』/『碳基同胞』/『航行者』/『動物之友』/『園守』/『葉之族』/『友善同胞』/『面具族』(→Utwig)",
    "  hostile 稱訪客:『拔根者』/『素食者』/『兩雄蕊、邪惡的素食者』/『玷污葉子之徒』",
    "===== v0.7 canonical decisions (Q&A locked) =====",
    "  Q1=B 保留 Phase 14c++ 詩意 identity icon (共生之枝/根系之聲/綠色的守望者) · 廢 吾等蘇菩→我方蘇菩",
    "  Q2=A shipped 保留:阿拉拉艦長 (Ala-la'la · 4 字精簡)",
    "  Q3=A shipped 保留:弗利克 (Vlik · 意為完美好用又營養的泥土)",
    "  Q4=B dossier §四:露特星 (Root · 音譯 · 對齊 Utwig 憂特星 Fahz)",
    "  Q5=A Master_Glossary L315:憂特監督者 (Utwig Proctor · 對齊 Utwig v3 canonical · 廢 shipped 憂特族護法)",
    "  Q6=C 混合:招牌詞採 dossier (碳基同胞/葉之族/面具族/共生者);一般依語感 (航行者/園守/動物之友/友善同胞)",
    "  Q7=A OUT_TAKES 全採 dossier §六例 6 版本 (第二把交椅→配角 · 隻狗如何→條狗更棒)",
    "  Q8=A GOODBYE_ALLIED_HOMEWORLD 升級 May-式招牌 (再見友善之族→願光永達您的葉,友善同胞) · GOODBYE_AFTER_SPACE 保留",
    "  Q9=A 標點統一:全升級 `…` → `……` (Style_Guide 標準)",
    "  Q10=A 共生體 → 共生者 (植物學家生命個體語感)",
    "  Q11=B shipped 保留:蘇菩·狸藻族 (Supox Utricularia · 中間點分隔 種名+屬名)",
    "  Q12=A shipped 保留:玩家 response 我方 (Mirror Mimicry 保護 · 玩家艦長=集體代表)",
    "===== v0.3 詞彙鎖定 (canonical, 保留) =====",
    "  Supox = 蘇菩族 (v0.4 使用者重設, 廢除 蘇波族)",
    "  Supox Utricularia = 蘇菩·狸藻族 (Utricularia=狸藻屬食蟲植物, 種族全稱)",
    "  Utwig = 憂特族 · Kohr-Ah = 柯亞族 · Ur-Quan = 烏寬族 · Druuge = 毒賈族",
    "  Utwig Proctor = 憂特監督者 (Master_Glossary L315 · v0.7 update: shipped 憂特族護法 廢)",
    "  Sa-Matra = 薩瑪特拉 (v0.7 cross-race canonical · 廢 shipped 薩-瑪特拉)",
    "  Ultron = 厄創 (Druuge 賣給 Utwig 的假聖物)",
    "  Tender Shoot = 嫩芽號 · Ala-la'la 阿拉拉艦長 · Vlik 弗利克 · Root 露特星",
    "  Nalnar = 納爾納 · Mali = 馬利 · Beta Leporis = 天兔座β",
    "===== 星圖 (v0.3 §4, 保留) =====",
    "  Antares = 心宿二 · Horologii = 時鐘座 · Beta Leporis = 天兔座β · Crateris = 巨爵座",
    "===== 聯盟名對齊 (v0.3 name_1..name_4, 保留) =====",
    "  name_1 = 新自由星系聯盟 · name_2 = 異星諸邦協和聯盟",
    "  name_3 = 聯合世界聯邦 · name_4 = <captain> 帝國",
    "===== v3 主要改動 (相對 shipped) =====",
    "  T1 NEUTRAL_SPACE/HOMEWORLD_HELLO_1: 同為碳基造物的朋友 → 碳基同胞 (dossier §四 招牌)",
    "  T2 NEUTRAL_SPACE/HOMEWORLD_HELLO_2: 遠行者 → 航行者 (dossier §四 canonical)",
    "  T3 HOSTILE_SPACE_HELLO_2: `你們` 統一敘事 · 標點統一",
    "  T4 UTWIG_NEARBY: 那戴著面具的一族 → 面具族 (em-dash apposition)",
    "  T5 OUR_SPECIES: 吾等蘇菩→我方蘇菩 (Q1B) · 根(Root)→露特星(Root) (Q4B)",
    "  T6 TAKE_ULTRON / DO_THIS_AFTER_SPACE: 憂特族護法→憂特監督者 (Q5A)",
    "  T7 HELLO_BEFORE_KOHRAH_SPACE_2: 花園守護者→園守 (Q6C 招牌)",
    "  T8 HELLO_AFTER_KOHRAH_SPACE_2: 動物同伴→動物之友 (Q6C 招牌)",
    "  T9 GENERAL_INFO_AFTER_SPACE_1: 吾等蘇菩→我方蘇菩 (Q1B)",
    "  T10 SAMATRA: 薩-瑪特拉→薩瑪特拉 (cross-race v0.7 canonical)",
    "  T11 can_you_help: 兩片葉從同一根汲水 → 雙葉共汲於一根 (dossier §四 招牌隱喻)",
    "  T12 DONT_NEED: 然,→然而, (讀順度)",
    "  T13 GOOD_HINTS: 知識是憂特族的職掌 → 智慧屬憂特之領域,我方蘇菩僅為執行者 (dossier §六例 3)",
    "  T14 bye_allied_homeworld: 多葉之族→葉之族 (Q6C)",
    "  T15 GOODBYE_ALLIED_HOMEWORLD: 再見友善之族 → 願光永達您的葉,友善同胞 (Q8A May-式)",
    "  T16 OUT_TAKES: 全採 dossier §六例 6 (第二把交椅→配角 等)",
    "  T17 標點:『…』→『……』(Q9A · Style_Guide 標準 · ALMOST_THERE/GREAT_DO_MORE/HELLO_AFTER_KOHRAH_SPACE_1/BATTLE_HAPPENS_1/FLEET_ON_WAY/HOW_HELP/GOOD_HINTS/OUT_TAKES)",
    "  T18 共生體→共生者 (SYMBIOTS/tell_us_of_your_species) (Q10A)",
    "  T19 HELLO_1/HOMEWORLD_HELLO_1 加句號斷句:『問候您,碳基同胞。 願您的根永得灌溉。』(dossier §六例 1)",
    "===== 排版 =====",
    "  詩意問候句 · line count 對齊 · Mirror Mimicry 保護 · May-式 招牌貫徹 GOODBYE"
]


def main() -> int:
    shipped = json.loads(SHIPPED.read_text(encoding='utf-8'))
    # get shipped key order (excluding _notes)
    shipped_keys = [k for k in shipped.keys() if not k.startswith('_')]

    # merge partials
    merged: dict[str, str] = {}
    for p in PARTIALS:
        data = json.loads(p.read_text(encoding='utf-8'))
        for k, v in data.items():
            if k.startswith('_'):
                continue
            if k in merged:
                raise SystemExit(f'duplicate key across partials: {k}')
            merged[k] = v

    # verify token set
    v3_keys = set(merged.keys())
    shipped_set = set(shipped_keys)
    missing = shipped_set - v3_keys
    extra = v3_keys - shipped_set
    if missing:
        raise SystemExit(f'missing tokens in v3: {sorted(missing)}')
    if extra:
        raise SystemExit(f'extra tokens in v3 (not in shipped): {sorted(extra)}')

    # write in shipped key order + v3 notes
    out = {'_notes': V3_NOTES}
    for k in shipped_keys:
        out[k] = merged[k]

    OUT.write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    print(f'[OK] wrote {OUT} · tokens={len(shipped_keys)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
