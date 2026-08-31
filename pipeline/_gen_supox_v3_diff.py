"""Generate Supox v3 vs shipped diff Markdown report.

Reads translations/supox.zh-TW.json (shipped) and translations/supox.zh-TW.v3.json,
produces _reaudit_supox_v3_diff.md with:
- 🟢 identical (protected · no change)
- 🟡 minor (voice preserved · small polish)
- 🟠 major (canonical/招牌 icon 更新)
- 🔴 critical (voice/identity 重大變更 · 罕見)
- ✨ v3-only new feature (canonical升級/招牌 icon 首次應用)

Each diff entry lists A(shipped) / B(v3) / C(custom, if applicable) options with recommendation.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
TR = ROOT / 'translations'
EN = ROOT / 'extracted' / 'base' / 'base' / 'comm' / 'supox' / 'supox.txt'

SHIPPED = TR / 'supox.zh-TW.json'
V3 = TR / 'supox.zh-TW.v3.json'
OUT = ROOT / '_reaudit_supox_v3_diff.md'


def parse_en(path: Path) -> dict[str, str]:
    """Parse EN source into {token: english_text}."""
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    tokens: dict[str, str] = {}
    tok: str | None = None
    buf: list[str] = []
    for ln in lines:
        m = re.match(r'^#\(([^)]+)\)', ln)
        if m:
            if tok is not None:
                while buf and buf[-1] == '':
                    buf.pop()
                tokens[tok] = '\n'.join(buf)
            tok = m.group(1)
            buf = []
        elif tok is not None:
            buf.append(ln)
    if tok is not None:
        while buf and buf[-1] == '':
            buf.pop()
        tokens[tok] = '\n'.join(buf)
    return tokens


# 分類與備註（人工預先分類 · 這些是本次 Rebuild-Compare 有實質變動的 tokens）
CATEGORIES = {
    # 🟠 Major canonical / 招牌 icon 更新
    'NEUTRAL_SPACE_HELLO_1':   ('🟠', 'B', '碳基同胞 canonical (Q6C 招牌) · 節奏調整 dossier §六例 1 · F5 fluency: 永得→永遠得到'),
    'NEUTRAL_SPACE_HELLO_2':   ('🟠', 'B', '航行者 canonical (Q6C 招牌) · F6 fluency: 永達→永遠照到'),
    'NEUTRAL_HOMEWORLD_HELLO_1':('🟠', 'B', '碳基同胞 canonical (Q6C 招牌) · F5 fluency'),
    'NEUTRAL_HOMEWORLD_HELLO_2':('🟠', 'B', '航行者 canonical (Q6C 招牌) · F6 fluency'),
    'UTWIG_NEARBY':            ('🟠', 'B', 'Wearers of Masks → 面具族 canonical (Q6C 招牌) · F9 fluency: 逗號 apposition (即)'),
    'TAKE_ULTRON':             ('🟠', 'B', '憂特族護法 → 憂特監督者 canonical (Q5A Master_Glossary L315) · Read-Aloud "當時正舉行" 修訂'),
    'HELLO_AFTER_KOHRAH_SPACE_2':('🟠', 'B', 'faunal comrade → 動物之友 canonical (Q6C 招牌)'),
    'DO_THIS_AFTER_SPACE':     ('🟠', 'B', '憂特族護法 → 憂特監督者 canonical (Q5A)'),
    'SAMATRA':                 ('🟠', 'B', '薩-瑪特拉 → 薩瑪特拉 (cross-race v0.7 canonical · 對齊 Chmmr/Kohr-Ah/Utwig/Kzer-Za v3)'),
    'GOOD_HINTS':              ('🟠', 'B', '知識是憂特族的職掌 → 智慧屬憂特之領域,我方蘇菩僅為執行者 (dossier §六例 3 招牌對憂特依賴) · 然事實上→但事實上 Read-Aloud'),
    'bye_allied_homeworld':    ('🟠', 'B', 'Leafy Ones 多葉之族 → 葉之族 canonical (Q6C 招牌)'),
    'GOODBYE_ALLIED_HOMEWORLD':('🟠', 'B', '再見友善之族 → 願光永遠照到您的葉,友善同胞 (Q8A May-式招牌升級 · F8 fluency: 永達→永遠照到)'),
    'OUT_TAKES':               ('🟠', 'B', '全採 dossier §六例 6 版本 · F4 fluency: 加『真正的』CAPS icon + 不然→甚至 (better yet 精確)'),

    # 🟡 Minor · Phase 14c++ 廢除 (吾等蘇菩 → 我方蘇菩) or 招牌 palette
    'OUR_SPECIES':             ('🟡', 'B', '吾等蘇菩→我方蘇菩 (Q1B 廢 Phase 14c++ wenyan) · F12 fluency: Root pun 保留為「露特星(Root,意為「根」)」音義並存'),
    'GENERAL_INFO_AFTER_SPACE_1':('🟡', 'B', '吾等蘇菩→我方蘇菩 (Q1B 廢 Phase 14c++ wenyan)'),
    'SYMBIOTS':                ('🟡', 'B', '共生體 → 共生者 (Q10A dossier §四 生命個體語感) · 共生之枝 保留 (Q1B)'),
    'tell_us_of_your_species': ('🟡', 'B', '共生體 → 共生者 (Q10A · 玩家 response 對齊)'),
    'YEAH_SORRY':              ('🟡', 'B', '此混淆 → 這場混淆 (Read-Aloud §4.5.4 冗餘書面修訂) · 完美美好又營養的土壤→完美好用又營養的泥土 (dossier canonical)'),
    'HOSTILE_SPACE_HELLO_2':   ('🟡', 'B', '雙雄蕊 → 兩雄蕊 (dossier §四 canonical 與 HIDEOUS_MONSTERS 對齊) · 昏暗母星→病弱母星 (dossier §四 canonical) · F1 fluency: 罵人段您們→你們'),
    'DONT_NEED':               ('🟡', 'B', '然, → 然而, (Read-Aloud §4.5.1 意連詞 更現代)'),
    'can_you_help':            ('🟡', 'B', '兩片葉從同一根汲水 → 雙葉共汲於一根 (dossier §四 招牌隱喻 canonical)'),
    'HELLO_AFTER_KOHRAH_SPACE_1':('🟡', 'B', '標點 … → …… (Q9A · 3 處)'),
    'ALMOST_THERE':            ('🟡', 'B', '標點 … → …… (Q9A)'),
    'GREAT_DO_MORE':           ('🟡', 'B', '標點 … → …… (Q9A)'),
    'BATTLE_HAPPENS_1':        ('🟡', 'B', '標點 … → …… (Q9A · 2 處)'),
    'FLEET_ON_WAY':            ('🟡', 'B', '標點 … → …… (Q9A · 2 處)'),
    'HOW_HELP':                ('🟡', 'B', '標點 … → …… (Q9A)'),
    'HIDEOUS_MONSTERS':        ('🟡', 'B', 'F10 fluency: 罵詞退 A「葉之玷汙者」+ 保 B 動詞「走開/連根拔起」·  混合最佳'),
    'ABOUT_BATTLE':            ('🟡', 'B', '中文分號空白 icon 微調 (「;」→「； 」讀順)'),
    'ALLIED_HOMEWORLD_HELLO_4':('🟡', 'B', '永遠得到授粉 → 精簡 (dossier §四 canonical) · F7 fluency: 永得→永遠得到'),
}


def render_pair(en: str, a: str, b: str, note: str, marker: str, rec: str) -> str:
    """Render one diff entry as Markdown block."""
    return (
        f'\n**EN**:\n```\n{en}\n```\n'
        f'**A · shipped**:\n```\n{a}\n```\n'
        f'**B · v3**:\n```\n{b}\n```\n'
        f'{marker} **推薦：{rec}** · {note}\n'
    )


def main() -> int:
    en_tokens = parse_en(EN)
    shipped = json.loads(SHIPPED.read_text(encoding='utf-8'))
    v3 = json.loads(V3.read_text(encoding='utf-8'))

    # buckets
    buckets: dict[str, list[str]] = {'🔴': [], '🟠': [], '🟡': [], '✨': [], '🟢': []}
    identical = 0
    changed = 0

    dialog_keys = [k for k in v3.keys() if not k.startswith('_')]

    for k in dialog_keys:
        a = shipped.get(k, '')
        b = v3[k]
        en = en_tokens.get(k, '(no EN source · player template)')
        if a == b:
            identical += 1
            buckets['🟢'].append(k)
            continue
        changed += 1
        marker, rec, note = CATEGORIES.get(k, ('🟡', 'B', '（未分類 · 微調）'))
        entry = f'### `{k}`\n' + render_pair(en, a, b, note, marker, rec)
        buckets[marker].append(entry)

    total = len(dialog_keys)
    lines: list[str] = []
    lines.append('# Supox v3 vs Shipped · Rebuild-Compare Diff Report')
    lines.append('')
    lines.append(f'**Race**: Supox (蘇菩族) · **Method**: v0.7 dossier-based Rebuild-Compare  ')
    lines.append(f'**Timestamp**: 2026-08-17 · Q&A locked (Q1B/Q2A/Q3A/Q4B/Q5A/Q6C/Q7A/Q8A/Q9A/Q10A/Q11B/Q12A)  ')
    lines.append(f'**Total tokens**: {total}  ·  **Changed**: {changed}  ·  **Identical**: {identical}  ')
    lines.append('')
    lines.append('## Summary')
    lines.append('')
    lines.append('| Marker | Count | Meaning |')
    lines.append('|---|---:|---|')
    lines.append(f'| 🔴 Critical | {len(buckets["🔴"])} | Voice/identity 重大變更 |')
    lines.append(f'| 🟠 Major | {len(buckets["🟠"])} | canonical / 招牌 icon 更新 |')
    lines.append(f'| 🟡 Minor | {len(buckets["🟡"])} | voice 保留 · 細節微調 |')
    lines.append(f'| ✨ New | {len(buckets["✨"])} | canonical 升級/招牌 icon 首次應用 |')
    lines.append(f'| 🟢 Identical | {len(buckets["🟢"])} | 未變（Q&A 鎖定保留 shipped） |')
    lines.append('')
    lines.append('## Decision quick-answer template')
    lines.append('')
    lines.append('```')
    lines.append('🔴 全 <A|B|C>')
    lines.append('🟠 全 <A|B|C|依推薦>')
    lines.append('🟡 全 <A|B|C|依推薦>')
    lines.append('✨ 全 <A|B|C|依推薦>')
    lines.append('（如有個別 override 於下方列出）')
    lines.append('```')
    lines.append('')

    # Emit each bucket
    for marker in ('🔴', '🟠', '🟡', '✨'):
        entries = buckets[marker]
        if not entries:
            continue
        lines.append(f'## {marker} {"Critical" if marker == "🔴" else "Major" if marker == "🟠" else "Minor" if marker == "🟡" else "New"} ({len(entries)} tokens)')
        lines.append('')
        for e in entries:
            lines.append(e)
            lines.append('')

    # Identical (list only, no bodies)
    lines.append(f'## 🟢 Identical / Preserved ({len(buckets["🟢"])} tokens · Q&A locked)')
    lines.append('')
    for k in buckets['🟢']:
        lines.append(f'- `{k}`')

    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'[OK] wrote {OUT.name}')
    print(f'  total={total}  changed={changed}  identical={identical}')
    for m in ('🔴', '🟠', '🟡', '✨', '🟢'):
        print(f'  {m}={len(buckets[m])}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
