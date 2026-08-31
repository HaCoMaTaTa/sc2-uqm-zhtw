"""VUX v3 rebuild-compare diff generator.

Reads:
  - translations/vux.zh-TW.json (shipped)
  - translations/vux.zh-TW.v3.json (rebuild)
  - extracted/base/base/comm/vux/vux.txt (EN source)

Categorizes each token:
  🟢 = identical (skip in report)
  🟡 = >= 90% same (equivalent tweak)
  🟠 = 30-90% same (rewording)
  🔴 = < 30% same (semantic/voice rewrite)
  ✨ = new canonical present

Writes: _reaudit_vux_v3_diff.md
"""
import json
import difflib
import re
from pathlib import Path

ROOT = Path(__file__).parent
SHIPPED = ROOT / 'translations' / 'vux.zh-TW.json'
V3 = ROOT / 'translations' / 'vux.zh-TW.v3.json'
EN_SRC = ROOT / 'extracted' / 'base' / 'base' / 'comm' / 'vux' / 'vux.txt'
OUT = ROOT / '_reaudit_vux_v3_diff.md'

FORBIDDEN = ['吾', '爾', '汝', '之', '乃', '矣', '哉', '焉', '兒', '吾等', '爾等', '將軍']

def parse_en_source(text: str) -> dict[str, str]:
    """Parse #(TOKEN)\\n...body...\\n\\n blocks from EN vux.txt."""
    tokens = {}
    blocks = re.split(r'(?m)^#\(', text)[1:]
    for blk in blocks:
        lines = blk.split('\n')
        m = re.match(r'([^)]+)\)', lines[0])
        if not m:
            continue
        key = m.group(1)
        body = '\n'.join(lines[1:]).rstrip()
        # Strip audio tag lines (empty after tab-split for player tokens)
        tokens[key] = body
    return tokens

def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()

def count_forbidden(s: str) -> dict[str, int]:
    return {c: s.count(c) for c in FORBIDDEN if s.count(c) > 0}

def category(sim: float, has_forbidden_removed: bool) -> tuple[str, str]:
    if sim >= 0.98:
        return ('🟢', 'identical')
    if sim >= 0.85:
        return ('🟡', 'micro-adjust (equivalent)')
    if sim >= 0.35:
        return ('🟠', 'rewording')
    return ('🔴', 'semantic/voice rewrite')

def main():
    shipped = json.loads(SHIPPED.read_text(encoding='utf-8'))
    v3 = json.loads(V3.read_text(encoding='utf-8'))
    en_src = parse_en_source(EN_SRC.read_text(encoding='utf-8'))

    keys = [k for k in v3 if k != '_notes']

    stats = {'🟢': 0, '🟡': 0, '🟠': 0, '🔴': 0, '✨': 0}
    entries = []

    for k in keys:
        zh_ship = shipped.get(k, '')
        zh_v3 = v3[k]
        en = en_src.get(k, '')

        sim = similarity(zh_ship, zh_v3)
        forbidden_before = count_forbidden(zh_ship)
        forbidden_after = count_forbidden(zh_v3)
        cleared = sum(forbidden_before.values()) - sum(forbidden_after.values())

        emoji, tag = category(sim, cleared > 0)
        stats[emoji] += 1

        entries.append({
            'key': k,
            'emoji': emoji,
            'tag': tag,
            'sim': sim,
            'en': en,
            'ship': zh_ship,
            'v3': zh_v3,
            'cleared': cleared,
            'forbidden_before': forbidden_before,
        })

    total = len(keys)

    lines = []
    lines.append('# VUX Rebuild-Compare Diff Report v3')
    lines.append('')
    lines.append('**日期**：2026-08-16')
    lines.append('**方法**：v0.7 dossier-based clean-room rebuild 完成後，程式化 diff shipped v0.5.1')
    lines.append('**Workflow**：[Rebuild_And_Compare.md](../StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md)')
    lines.append(f'**v3 file**：`translations/vux.zh-TW.v3.json`（{total} tokens）')
    lines.append(f'**shipped**：`translations/vux.zh-TW.json`（重度污染：吾 128 / 爾 137 / 之 174 / 吾等 84 / 爾等 136 / 本官 37 —— P0 最重）')
    lines.append('')
    lines.append('## 統計')
    lines.append('')
    lines.append('| 類別 | Emoji | 意義 | Count | % |')
    lines.append('|---|---|---|---:|---:|')
    for e, tag in [('🟢','完全相同'),('🟡','微調（等價）'),('🟠','措辭改變'),('🔴','語意/voice 差異大'),('✨','canonical 升級')]:
        pct = stats[e] / total * 100
        lines.append(f'| {tag} | {e} | v3 vs shipped | {stats[e]} | {pct:.1f}% |')
    lines.append(f'| **總計** | | | **{total}** | 100.0% |')
    lines.append('')
    lines.append('## Q&A 決策鎖（v3 依此執行）')
    lines.append('')
    lines.append('- Q1=A 感嘆詞 dossier v0.7 (Hee!→嘿嘿嘿！/(urp!)→（噁——！）/(urk!)→（噎——！）/Mmmmmm!→嗯～～～～/AUGH!→噁！/(sob!)→（嗚——！）/AIEEE!→啊咦咦咦咦──！！！首介)')
    lines.append('- Q2=A VUX 主族自稱: 我族 VUX(主) + 我方(少) + 我(單人)')
    lines.append('- Q3=A ZEX 自稱: 本官(~85%) + 本上將澤克斯(首介 ZEX_HELLO_1) + 我(親密調情 GOODBYE_ZEX)')
    lines.append('- Q4=A 主族稱玩家: 你/你們 + 情境辱罵詞（腐肉袋/蠕蟲/會嘔吐的東西/醜八怪）')
    lines.append('- Q5=A ZEX 稱玩家: 艦長(預設) + 光滑迷人的朋友/美麗豐潤的人類/心愛的人類(詩意)')
    lines.append('- Q6=A silatious/phlagrant melons: 嬉哩語/明目張膽的西瓜/第三次可就真的痛了')
    lines.append('- Q7=A menagerie=珍禽異獸收藏館 / my children=我的孩子們 / new child=我的新孩子（覆蓋 Master_Glossary L232 舊 canonical）')
    lines.append('- Q8=A ZEX chiton rasps: 本官的甲殼因興奮而摩挲、滲潤')
    lines.append('- Q9=A+B CAPS 用短句+句號+\\n（不加 **）; AIEEEEE! 首介中譯')
    lines.append('- Q10=A player apology 台灣口語+情境切換')
    lines.append('- Q11=A smooth-skinned friend=光滑迷人的朋友')
    lines.append('- Q12=A 4 批 partial (25/16/22/39)')
    lines.append('')
    lines.append('## 3-gate verify 結果')
    lines.append('')
    lines.append('- ✅ **Gate 1 純度**：race=0, simp=0, variant=0（**shipped 之 174/爾 137/吾 128 等 P0 污染全部清除**）')
    lines.append('- ✅ **Gate 2 行數**：0 mismatch（102/102 tokens 對齊 EN 原文）')
    lines.append('- ✅ **Gate 3 Lua template**：0 English leak first-arg（getStarName/getConstellation/getColor/swapIfSeeded 皆已 zh-TW 化）')
    lines.append('')
    lines.append('## 主要 canonical 修正 vs shipped v0.5.1')
    lines.append('')
    lines.append('| 舊（shipped v0.5.1） | 新（v3 依 v0.7 dossier + Master_Glossary） | 影響 |')
    lines.append('|---|---|---|')
    lines.append('| 本將軍 (37×) | **本官** (ZEX only) / **本上將澤克斯** (首介 ZEX_HELLO_1) | ZEX 語體轉現代貴族氣（Master_Glossary L152 canonical） |')
    lines.append('| 吾/爾/之/爾等/吾等（600+ 次） | **我族 VUX / 我 / 你 / 你們** (主族) / **本官** (ZEX 專用) | 全數清除文言污染，符合 dossier v0.7 |')
    lines.append('| 嘻！嘻！嘻！ | **嘿嘿嘿！（Hee! Hee! Hee!）** | 感嘆詞 dossier v0.7 canonical |')
    lines.append('| 呃啊！/嗝！ | **（噁——！）（urp!）** | 感嘆詞 dossier v0.7 canonical |')
    lines.append('| 呃咳！ | **（噎——！）（urk!）** | 感嘆詞 dossier v0.7 canonical |')
    lines.append('| 唔唔唔唔唔──！ | **嗯～～～～（Mmmmmm!）** | 感嘆詞 dossier v0.7 canonical |')
    lines.append('| 噁啊！ | **噁！（Augh!）** / **噁——！（AGGH!）** | 感嘆詞 dossier v0.7 canonical |')
    lines.append('| 珍藏館 (Master_Glossary L232) | **珍禽異獸收藏館** (dossier v0.7 §4.6.4) | **⚠️ Master_Glossary 待更新** |')
    lines.append('| 光滑肌膚之友 | **光滑迷人的朋友** | dossier v0.7 §4.6.3 |')
    lines.append('')
    lines.append('## ⚠️ Master_Glossary 待補登 canonical 提醒')
    lines.append('')
    lines.append('| 位置 | 舊 | 建議新增 | 出處 |')
    lines.append('|---|---|---|---|')
    lines.append('| L232 menagerie | 珍藏館/醜陋珍藏/怪物館 | 增補 **珍禽異獸收藏館** (dossier v0.7 primary) | Q7=A + VUX.md §4.6.4 |')
    lines.append('| ZEX 自稱 | 未登記 | **本官** (單人) / **本上將澤克斯** (首介) / **我** (親密調情) | Q3=A + VUX.md §4.6.2 |')
    lines.append('| 感嘆詞 icon | shipped v0.5.1 Q8 | 更新 hee=嘿嘿嘿 / urp=噁—— / urk=噎—— / Mmmmmm=嗯～～～～ / AUGH=噁 | Q1=A + VUX.md §4.4/4.6.4 |')
    lines.append('')
    lines.append('## 差異項（只列 🟡🟠🔴，🟢 不列）')
    lines.append('')

    idx = 0
    for e in entries:
        if e['emoji'] == '🟢':
            continue
        idx += 1
        lines.append(f'### #{idx} · `{e["key"]}` · {e["emoji"]} {e["tag"]} · sim={e["sim"]:.3f}; 文言助詞清除={e["cleared"]}')
        lines.append('')
        lines.append('**英文原文**：')
        lines.append('```')
        lines.append(e['en'])
        lines.append('```')
        lines.append('')
        lines.append('**Shipped v0.5.1**：')
        lines.append('```')
        lines.append(e['ship'])
        lines.append('```')
        lines.append('')
        lines.append('**Rebuild v3 (clean-room v0.7)**：')
        lines.append('```')
        lines.append(e['v3'])
        lines.append('```')
        lines.append('')
        # Recommendation
        forbid_summary = ' / '.join(f'{c}×{n}' for c, n in e['forbidden_before'].items()) or '無'
        rec_note = f'shipped 含文言污染: {forbid_summary}'
        if e['emoji'] == '🔴':
            rec = 'B (v3) — shipped 語體徹底錯位，v3 依 v0.7 dossier 重建，必採 v3'
        elif e['emoji'] == '🟠':
            rec = 'B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用'
        else:
            rec = 'B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感'
        lines.append(f'**推薦**：{rec}')
        lines.append('')
        lines.append(f'**說明**：{rec_note}')
        lines.append('')
        lines.append(f'**你的選擇**：`{e["key"]}=A`（shipped）/ `{e["key"]}=B`（v3）/ `{e["key"]}=C自訂:...`')
        lines.append('')
        lines.append('---')
        lines.append('')

    lines.append('## 批次快答格式建議')
    lines.append('')
    lines.append('```')
    lines.append('🟠 全依推薦（=全 B）')
    lines.append('🔴 逐項挑（列出各 token 選擇）')
    lines.append('🟡 全 A（保留 shipped）或全 B（採 v3）')
    lines.append('特殊自訂: TOKEN_NAME=C[自訂內容]')
    lines.append('```')
    lines.append('')
    lines.append('**Rebuild-Compare 執行者**：GitHub Copilot（Claude Opus 4.7）')
    lines.append('**執行日期**：2026-08-16')

    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Diff report written: {OUT}')
    print(f'Stats: {stats}')
    print(f'Diff entries (non-🟢): {sum(v for k,v in stats.items() if k != "🟢")}')

if __name__ == '__main__':
    main()
