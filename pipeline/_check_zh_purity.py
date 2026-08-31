# -*- coding: utf-8 -*-
"""Build-time purity check for zh-TW race translations.

Ensures no regression on:
1. Bare English race names in dialog text (per _analysis/SC2-詞彙對照表-v0.3.md)
2. Simplified-only Chinese characters (should be Traditional / 繁體)

Not checked (verified as intentional style):
- CJK + ASCII space + CJK (used as narrative pause per §9)

Usage:
  python _check_zh_purity.py            # summary only
  python _check_zh_purity.py --verbose  # show every violation
  python _check_zh_purity.py --strict   # exit 1 on any violation (for CI/build gate)

Exit codes:
  0 = all clean OR non-strict mode
  1 = violations detected in --strict mode
"""
import argparse
import json
import re
import sys
from pathlib import Path

# ==============================================================================
# Config
# ==============================================================================

# Race names that MUST be Chinese in dialog (per v0.3 詞彙對照表).
# Names present in dialog will be flagged unless whitelisted below.
RACE_NAMES = [
    'Spathi', 'Ur-Quan', 'Ilwrath', 'Yehat', 'Syreen', 'Shofixti',
    'Umgah', 'Melnorme', 'Pkunk', 'Slylandro',
    'Chenjesu', 'Mmrnmhrm', 'Mycon', 'Arilou', 'Chmmr', 'Zoq-Fot-Pik',
    'Orz', 'Androsynth', 'Utwig', 'Supox',
    'Thraddash', 'Druuge', 'Kohr-Ah', 'Kzer-Za',
]

# Alien words kept in English on purpose (v0.3 §5 招牌用語).
# These are stripped from lines BEFORE race name scanning.
ALIEN_WHITELIST = {
    'Homosap', 'Hunam', 'Hootmans', 'Huge-glands',
    'Wezzy-Wezzah', 'Huffi-Muffi-Guffi', 'Ta Puun', 'Puun-Taffy',
    'Snork', 'AIEEEE', 'HAIL', 'Har-Har', 'Kyaiee', 'Hee',
    'BGAK', 'PKUNKRA', 'PLAM PRIKKY',
    'Precursor', 'Precursors',
}

# Tokens allowed to contain bare English race names (e.g. self-etymology).
# Format: 'race:TOKEN_KEY' → matches translations/<race>.zh-TW.json[<TOKEN_KEY>]
TOKEN_EXEMPT = {
    'pkunk:GENERAL_INFO_NEUTRAL_4',  # 『Pkunk』意為和平 — 釋名 metadata
    'pkunk:SHIP_GIFT',                # 烈憤艦（Pkunk Fury） — v0.5.2 canonical 艦名首介英文（Rebuild v2 2026-08-15）
    'arilou:CONFUSED_RESPONSE',      # 阿麗露·萊蕾 (Arilou Lalee'lay) — 釋名首介
    'chmmr:WE_ARE_FREE',              # 我方為查姆族(Chmmr) — 誕生宣告首介
    'kohrah:HELLO_AND_DIE_1',         # 我方乃烏寬柯亞族(Ur-Quan Kohr-Ah) — 儀式自介
    'supox:FROM_SUPOX',               # 蘇波·狸藻族(Supox Utricularia) — 釋名首介
    'yehatrebels:YEHAT_CAVALRY',      # 普恩烈憤艦（Pkunk Fury） — Q6 canonical 艦名首介英文
    'syreen:OUR_NEW_WORLD',           # 烏寬主宰九號（Ur-Quan Master Nine） — v0.7 首介英文 gloss (Rebuild-Compare 2026-08-17)
}

# ==============================================================================
# CANONICAL Chinese race names (per _analysis/SC2-詞彙對照表.md v0.2 + v0.3).
# FORBIDDEN_ZH_VARIANTS = homophones/typos that would fragment the vocab.
# If any translation contains a forbidden variant → FAIL (must use canonical).
# ==============================================================================
FORBIDDEN_ZH_VARIANTS = {
    # canonical -> [variants that MUST NOT appear]
    # v0.4 Phase 14c 更新：canonical 對齊 Master_Glossary，舊 v0.3 canonical 列為 variant
    '塞蓮族':  ['賽倫族', '賽蓮族', '塞倫族'],     # Syreen (female species, 蓮 feminine)
    '史怕族':  ['史帕族', '斯帕族', '史巴族', '思怕族'],   # Spathi
    '烏寬族':  ['烏爾寬族', '奧寬族', '烏寬人'],          # Ur-Quan
    '蛛狂族':  ['伊爾拉斯族', '伊瑞斯族', '伊爾夫族'],    # Ilwrath
    # v0.4 rename: Yehat 葉哈特族 → 翼哈特族
    '翼哈特族': ['葉哈特族', '葉哈族', '耶哈族', '葉哈塔族'],   # Yehat (v0.4 Phase 8.5b rename)
    # v0.4 rename: Shofixti 蘇菲斯特族 → 修烈士族
    '修烈士族': ['蘇菲斯特族', '蘇菲特族', '蘇菲斯族', '蕭菲斯族', '修飛族'],  # Shofixti (v0.4)
    # v0.4 rename: Umgah 阿姆嘎族 → 陰嘎族
    '陰嘎族':  ['阿姆嘎族', '阿姆嘎', '昂加族', '烏姆嘎族', '烏姆嘎', '姆嘎族'],  # Umgah (v0.4)
    # v0.4 rename: Melnorme 梅爾諾 → 梅諾商 (NO 族 suffix)
    # NOTE: 「梅諾」moved from variant→canonical because 梅諾商 contains 梅諾. Cannot block substring.
    '梅諾商':  ['梅爾諾', '米爾諾', '梅爾諾姆', '梅爾諾族'],  # Melnorme (v0.4)
    '普恩族':  ['普肯族', '普庫族', '朋克族'],            # Pkunk
    '斯萊族':  ['斯萊蘭德族', '斯萊蘭卓族', '斯萊蘭多族'],# Slylandro
    '晶智族':  ['陳吉蘇族', '簡結蘇族'],                  # Chenjesu (v0.2)
    '姆姆族':  ['姆穆族', '莫莫族', '姆恩族'],            # Mmrnmhrm (v0.2)
    '查姆族':  ['查嗯族', '克姆族'],                      # Chmmr (v0.2)
    '麥孔族':  ['麥空族', '邁孔族', '麥崆族', '梅蒙族'],   # Mycon (v0.4: also block 梅蒙誤植)
    '安卓辛族': ['安卓辛特族', '安卓森族'],               # Androsynth (v0.2)
    '阿麗露':  ['阿瑞婁族', '阿麗露族', '阿麗魯'],        # Arilou Lalee'lay (v0.2 no 族 suffix)
    # v0.4 rename: Supox 蘇波族 → 蘇菩族
    '蘇菩族':  ['蘇波族', '蘇波克斯族', '蘇波希族', '蘇波氏族'],  # Supox (v0.4)
    '憂特族':  ['烏特維格族', '烏特維族', '尤特族'],      # Utwig (locked in supox 2026-08-07)
    # v0.4 rename: Druuge 德魯族 → 毒賈族
    '毒賈族':  ['德魯族', '卓魯格族', '德魯格族', '杜魯族'],  # Druuge (v0.4)
    # v0.4 new: Thraddash 撒達許族 → 撻伐族
    '撻伐族':  ['撒達許族', '撒達許', '斯拉達族'],  # Thraddash (v0.4)
    # v0.4 new: Dnyarri 尼亞里族 → 蟾亞族
    '蟾亞族':  ['尼亞里族', '尼亞里', '迪亞里族'],  # Dnyarri (v0.4)
    # v0.4 Phase 14c: §1.4 已有慣例中譯的專有名詞（Alien_Speech_Rule §1.4）
    # 這些既有中譯已完成翻譯，遊戲文本內不應出現裸英文。
    # 若有 bare 英文 → 譯者漏翻，應立即修正為對應中文。
    '多加':    ['Dogar'],   # Ilwrath 邪神之一（Alien_Speech §2.1）
    '卡宗':    ['Kazon'],   # Ilwrath 邪神之一（Alien_Speech §2.1）
    # Individuals
    '泰蘭娜':  ['泰拉娜', '塔拉娜', '塔蘭娜'],           # Talana
    '費佛':    ['菲弗', '飛佛', '費弗'],                  # Fwiffo (Spathi)
    '海斯':    ['海斯艦長'],  # Hayes 保留 raw 「海斯」,dialog 加艦長時另外處理
    # Places
    '蓋亞':    ['蓋婭', '該亞', '蓋雅'],                  # Gaia
    '賽拉':    ['塞拉', '賽亞'],                          # Syra
    '史怕瓦':  ['史帕瓦', '思怕瓦', '史怕娃', '斯帕蒂瓦', '史帕蒂瓦'],  # Spathiwa (v0.5 rename 娃→瓦)
    # ==========================================================
    # v0.5.2 Round 5 canonical drift 防禦 (Reaudit_Dialogue.md 升級)
    # ==========================================================
    '迴避者':  ['潛匿艦', '閃匿艦'],  # Eluder (v0.5.2 D3 commander Reaudit 統一)
    '苦刑器':  ['苦刊器', '極痛裝置'],  # Excruciator (v0.5.2 Q1 melnorme;苦刊 typo)
    '星幣':    ['信用點數'],  # Interstar Credits (v0.5.2 Q2 melnorme)
    '布維族':  ['波維克塞族'],  # Burvixese (v0.5.2 Q3 melnorme)
    '通道九號': ['九號廈道', '九號廊道'],  # Corridor Nine (v0.5.2 D2 commander Reaudit)
    '烈憤艦':  ['火炬艦'],  # Pkunk Fury (v0.5.2 Q6 yehatrebels;火炬艦 給 Thraddash 用)
    '宿敵號':  ['復仇者艦'],  # Nemesis (v0.5.2 D11 starbase Reaudit;不含「復仇者號」因玩家旗艦用)
    # Alliance names (Round 5 D8 melnorme Reaudit 統一 commander canonical)
    '異星諸邦協和聯盟': ['異族列邦協和會'],  # New Alliance name_2 (v0.5.2 melnorme/thraddash/zoqfotpik retrofit)
    '聯合世界聯邦': ['諸邦聯合體'],  # New Alliance name_3 (v0.5.2 melnorme/thraddash/zoqfotpik retrofit)
    # Star names (Round 5 D1 thraddash Reaudit 統一 gamestrings canonical)
    '織女星': ['織女一'],  # Vega (v0.5.2 D1 thraddash 對齊 gamestrings canonical)
    # Character gag names (Round 5 D1 safeones Reaudit 跨檔統一)
    '賈德·魔怪': ['沃格·賈德'],  # Jud the Vug (v0.5.2 D1 safeones 統一 dossier;spathi 已 retrofit)
    # Star names (Round 5 syreen Reaudit 統一 mycon Q8 canonical)
    '歐加農': ['奧甘農'],  # Organon (v0.5.2 syreen D1 統一 mycon Q8 canonical;Master_Glossary line 110)
    # Star names (Round 5 utwig Reaudit 統一 gamestrings/melnorme canonical)
    # NOTE: Arcturus 大角→大角星 drift 無法用 FORBIDDEN 追蹤（「大角」是「大角星」的子字串,會自我觸發）
    #       仰賴人工 grep + Level 3 Reaudit 抓 drift
    '畢宿星團ζ': ['畢宿ζ'],  # Zeta Hyades (v0.5.2 utwig D4 統一 gamestrings + melnorme v0.5.2 D7 canonical;「畢宿ζ」非「畢宿星團ζ」子字串,安全)
    # Precursor artifacts (Round 5 druuge+supox Reaudit 統一 utwig/Master_Glossary canonical)
    '厄創': ['奧創裝置'],  # Ultron (v0.5.2 D1 druuge+supox 統一 Master_Glossary line 200 canonical;取代舊「奧創裝置」;utwig 已用「厄創」)
    # Weapon devices (Round 5 yehat Reaudit 統一 shofixti/Master_Glossary canonical)
    '榮耀彈': ['榮耀裝置'],  # Glory Device (v0.5.2 D1 yehat+starbase 統一 Master_Glossary line 209 canonical;取代舊「榮耀裝置」;shofixti/spathi 已用「榮耀彈」)
    # NOTE: Utwig=憂特族/Zoq-Fot-Pik=佐-佛-皮/Mael-Num=梅努族 這些 rename 已在上方 v0.4 區塊
    #       Path of Now and Forever=現在與永恆之道 是敘述用語,非族名,採用 grep 追蹤而非 forbidden
}

# NOTE (v0.4 Phase 14c 2026-08-08):
# Master_Glossary rename cascade applied. Old v0.3 canonical names (葉哈特族/蘇菲斯特族/
# 阿姆嘎族/梅爾諾/蘇波族/德魯族) are now BLOCKED as forbidden variants.
# Removed old '梅諾' variant entry — replaced by '梅諾商' canonical (substring conflict).


# Simplified-only characters (NEVER valid 繁體). Conservative — bilateral chars
# like 著/被/曾/面/概/著 are excluded because they exist in both scripts.
SIMPLIFIED_ONLY = set(
    # Common daily-use simp chars
    '吗说帮让实还会来过经现为们这发开离国两问间关广厂产难双欢观权园团图压虽龙风飞'
    # Speech-related radical (讠)
    '讣讥讨讪训议讯讲讳讵讶讷许讹论讼讽设访诀证诃评诅诈诉诊词译试诗诚话诞诠询详诨语'
    '诫误诵请诸诺读诽课谁调谅谈谊谋谎谐谓谕谘谚谜谢谣谨谩谬谱谴'
    # Metal radical (钅)
    '铁银锁钱钟录铺锋销钢针钥锐锦铃铜锅锤锥锯锹钞钩钮铲铸锭错锣锚钉钓'
    # Money radical (贝)
    '贞负贡财责贤败账货质贩贪贫贬购贮贯贱贴贵贷贸贺贼贾贿资赈赊赋赌赏赐赔赖赚赛赞赢'
    # Grass/food radicals
    '苏荆荐荡荣荤药获莱莲营萧葱蒋蓝药获荣'
    # Vehicle radical (车)
    '轧轨转轮软轰轴轻载较辄辅辆辈辉辐输辖辙'
    # Walk radical (辶)
    '边过还这进远违连迟选递逻遗'
    # Door radical (门)
    '闪闭闯闲闷闹阁阅阔'
    # Hill/place
    '队阵阶际陆陈险难'
    # People/Person
    '价伪优侠党员'
    # Silk radical (纟)
    '纠红级约纪纬纯纱纳纵纷纸纹纺组细织终绊绍绑结绒绕绘给络绝统继绢绣综绪绯绳维绵绷'
    '绸绿缀缅缆缉缎缓缔编缘缚缝缠缩缰缴'
    # Bird radical (鸟)
    '鸠鸡鸣鸥鸦鸭鸯鸳鸵鸽鹅鹏鹤鹰鹳'
    # Fish radical (鱼)
    '鲁鲍鲜鲤鲨鲫鲸鳖'
    # Page radical (页)
    '页顶项顺须顽顾顿颂预领颊颐频颓颖颗题颜额颤'
    # Horse radical (马)
    '驮驯驰驱驶驻骂骄骇验骏骑骗骚骤'
    # Others
    '国场坏块声备奋娱学宁宠审宪对寻导层岁带帅师应张归当战戏扬扫扑执担拟拥据损摊摆摇'
    '数断旧时晓晒暂朴条构枪柜标栏树样梦检楼横欧灭灯炉烂烛烧热爷独狮猎猪猫献玛现画'
    '疗盘盖矿码砖硕确碍礼简类罢罗罚习翘耻聪肃胁胆脉脏脚舰艰灵静竞'
    # Extra
    '飘饭饮饰饱饲饺饼馆麦'
)

# ==============================================================================

RACE_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(r) for r in RACE_NAMES) + r')\b')


def scan_race_names(text):
    """Return list of (matched_name, context_line)."""
    hits = []
    for ln in text.split('\n'):
        stripped = ln
        for w in ALIEN_WHITELIST:
            stripped = stripped.replace(w, '')
        for m in RACE_PATTERN.finditer(stripped):
            hits.append((m.group(1), ln.strip()[:120]))
    return hits


def scan_simplified(text):
    """Return dict of {simplified_char: count}."""
    hits = {}
    for ch in text:
        if ch in SIMPLIFIED_ONLY:
            hits[ch] = hits.get(ch, 0) + 1
    return hits


def scan_forbidden_zh(text):
    """Return list of (variant, canonical) hits for forbidden zh variants."""
    hits = []
    for canonical, variants in FORBIDDEN_ZH_VARIANTS.items():
        for v in variants:
            if v in text:
                hits.append((v, canonical, text.count(v)))
    return hits


def check_file(path, verbose=False):
    """Return (race_hits, simp_hits, forbidden_hits, tokens_affected)."""
    race_name = path.stem.replace('.zh-TW', '')
    d = json.loads(path.read_text(encoding='utf-8'))

    all_race = []       # [(token, name, ctx)]
    all_simp = {}       # {char: count}
    all_forbidden = []  # [(token, variant, canonical, count)]
    tokens_affected = set()

    for tok, val in d.items():
        if tok.startswith('_') or not isinstance(val, str):
            continue
        exempt_key = f'{race_name}:{tok}'
        if exempt_key in TOKEN_EXEMPT:
            continue

        rh = scan_race_names(val)
        sh = scan_simplified(val)
        fh = scan_forbidden_zh(val)

        if rh or sh or fh:
            tokens_affected.add(tok)
        for name, ctx in rh:
            all_race.append((tok, name, ctx))
        for ch, c in sh.items():
            all_simp[ch] = all_simp.get(ch, 0) + c
        for v, canonical, c in fh:
            all_forbidden.append((tok, v, canonical, c))

    return all_race, all_simp, all_forbidden, tokens_affected


def main():
    parser = argparse.ArgumentParser(description='zh-TW purity check for race translations.')
    parser.add_argument('--verbose', action='store_true', help='show every violation')
    parser.add_argument('--strict', action='store_true', help='exit 1 on any violation')
    parser.add_argument('--race', help='check only this race')
    parser.add_argument('--dir', default='translations', help='translations directory')
    args = parser.parse_args()

    tdir = Path(args.dir)
    if not tdir.exists():
        print(f'error: {tdir} not found', file=sys.stderr)
        return 2

    if args.race:
        files = [tdir / f'{args.race}.zh-TW.json']
    else:
        files = sorted(tdir.glob('*.zh-TW.json'))
        # gamestrings is a huge system-strings file — skip by default
        files = [f for f in files if f.stem != 'gamestrings.zh-TW']

    if not files:
        print('error: no translation files found', file=sys.stderr)
        return 2

    grand_race = 0
    grand_simp = 0
    grand_forbidden = 0
    grand_files = 0

    print('=' * 60)
    print('zh-TW purity check')
    print('=' * 60)

    for path in files:
        if not path.exists():
            print(f'  (skip: {path.name} not found)')
            continue
        race, simp, forbidden, tokens = check_file(path, verbose=args.verbose)
        r = path.stem.replace('.zh-TW', '')
        n_race = len(race)
        n_simp = sum(simp.values())
        n_forbidden = sum(c for _, _, _, c in forbidden)
        grand_race += n_race
        grand_simp += n_simp
        grand_forbidden += n_forbidden
        if n_race or n_simp or n_forbidden:
            grand_files += 1

        status = 'FAIL' if (n_race or n_simp or n_forbidden) else 'PASS'
        print(f'  [{status}] {r:12} race={n_race:3d}  simp={n_simp:3d}  variant={n_forbidden:3d}  tokens={len(tokens):3d}')

        if args.verbose:
            if race:
                print(f'    ── 英文族名 ──')
                for tok, name, ctx in race[:20]:
                    print(f'      [{tok}] {name}: {ctx}')
                if len(race) > 20:
                    print(f'      ... 還有 {len(race)-20} 個')
            if simp:
                print(f'    ── 簡體字 ──')
                for ch, c in sorted(simp.items(), key=lambda x: -x[1]):
                    print(f'      {ch}: {c}')
            if forbidden:
                print(f'    ── 禁用中文變體 ──')
                for tok, v, canonical, c in forbidden:
                    print(f'      [{tok}] {v!r} x{c} → 應為 {canonical!r}')

    print('=' * 60)
    print(f'總計: race={grand_race}, simp={grand_simp}, variant={grand_forbidden}, 有問題檔案={grand_files}')
    print('=' * 60)

    if args.strict and (grand_race or grand_simp or grand_forbidden):
        print('\nSTRICT mode: violations found — exit 1', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
