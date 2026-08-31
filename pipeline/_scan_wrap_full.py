"""Comprehensive wrap-hostile risk scanner for ALL translations/**/*.zh-TW.json.
Detects the *complex* class of wrap-bug demonstrated by vux LIKE_BECAUSE (~~~~)
and vux FOOL_AIEE1 / TRUTH (mixed dash + FW-paren-latin-FW-paren + ellipsis).

Risk factors (per line):
  R1 Same-char run >= threshold  (~4, 4dash, 6exclaim etc.)
  R2 FW paren + half-width word + FW paren   ex: （AIEEE!!!）
  R3 Mix of `——` (U+2014) + `──` (U+2500) on SAME line
  R4 Closing bracket 」）、 immediately followed by …… ellipsis
  R5 Line has 3+ *different* non-CJK punct types (compound complexity)
  R6 Total non-CJK char density > 40% in line of length >= 20

Severity:
  HIGH = R1(严重 <= vux tilde case) or R2+R3+R4 same-line
  MED  = R2 alone, or R3 alone, or R4 alone, or R5+R6
  LOW  = R1 borderline (fw ! ≥ 6), R6 alone
"""
import json, re, sys
from pathlib import Path

ROOT = Path(r'Q:\Dos_G\StarControl2\uqm-work\translations')

# R1 same-char run thresholds (HIGH)
R1_CHARS = {
    '\uff5e': 4,   # ～ tilde
    '\u301c': 4,   # 〜 wave dash
    '\u2014': 4,   # — em-dash
    '\u2500': 4,   # ─ box-draw
    '\u2026': 6,   # … ellipsis (6+, i.e. 「……」 x3 = 6)
}
# R1-MED
R1_MED = {
    '\uff01': 6,   # ！
    '\uff1f': 6,   # ？
    '\u3002': 6,   # 。
    '\uff0a': 4,   # ＊
}

# R2: FW paren wrap ASCII (fullwidth `（` + latin/punct + `）`)
R2_PATT = re.compile(r'\uff08[A-Za-z0-9!?.]+\uff09')

# R3: mixed dash types on same line (em-dash AND box-draw)
def has_r3(line):
    return '\u2014' in line and '\u2500' in line

# R4: closing bracket immediately followed by ……
R4_PATT = re.compile(r'[\u300d\u300f\uff09\u3001]\u2026\u2026')

# R5/R6 support: count non-CJK chars per line
def line_stats(line):
    total = len(line)
    if total == 0:
        return 0, 0, set()
    non_cjk = 0
    puncts = set()
    for c in line:
        o = ord(c)
        if o < 128:  # ASCII
            non_cjk += 1
            if not c.isalnum() and c != ' ':
                puncts.add(c)
        elif 0x4e00 <= o <= 0x9fff or 0x3400 <= o <= 0x4dbf:
            pass  # CJK
        elif 0x3000 <= o <= 0x303f or 0xff01 <= o <= 0xff60:
            # CJK punctuation
            non_cjk += 1
            puncts.add(c)
        elif o in (0x2014, 0x2015, 0x2500, 0x2501, 0x2026, 0x2020, 0x2039, 0x203a, 0xff5e, 0x301c):
            non_cjk += 1
            puncts.add(c)
    return total, non_cjk, puncts

hits = []
for jf in sorted(ROOT.rglob('*.zh-TW.json')):
    d = json.loads(jf.read_text(encoding='utf-8'))
    for key, val in d.items():
        if key.startswith('_') or not isinstance(val, str):
            continue
        for line_no, line in enumerate(val.split('\n'), 1):
            findings = []

            # R1 HIGH
            for ch, threshold in R1_CHARS.items():
                for m in re.finditer(re.escape(ch) + f'{{{threshold},}}', line):
                    findings.append(('HIGH', f'R1 {len(m.group())}x U+{ord(ch):04X}'))
            # R1 MED
            for ch, threshold in R1_MED.items():
                for m in re.finditer(re.escape(ch) + f'{{{threshold},}}', line):
                    findings.append(('MED', f'R1 {len(m.group())}x U+{ord(ch):04X}'))

            # R2
            r2_matches = list(R2_PATT.finditer(line))
            if r2_matches:
                findings.append(('MED', f'R2 FW-paren-ASCII {len(r2_matches)}x'))

            # R3 (only if line has both em-dash and box-draw)
            if has_r3(line):
                findings.append(('MED', 'R3 em-dash + box-draw mixed'))

            # R4
            if R4_PATT.search(line):
                findings.append(('MED', 'R4 bracket-then-ellipsis'))

            # R5/R6 combined
            total, non_cjk, puncts = line_stats(line)
            if total >= 20:
                r5 = len(puncts) >= 3
                r6 = non_cjk / total > 0.40
                if r5 and r6:
                    findings.append(('MED', f'R5+R6 {len(puncts)} punct types, {non_cjk}/{total}={non_cjk*100//total}%'))
                elif r6:
                    findings.append(('LOW', f'R6 {non_cjk}/{total}={non_cjk*100//total}% non-CJK'))

            if findings:
                # Escalate: if 2+ MED findings on same line → HIGH
                med_count = sum(1 for s,_ in findings if s == 'MED')
                if med_count >= 2:
                    findings.insert(0, ('HIGH', f'ESCALATED: {med_count} MED risks compound'))
                hits.append({
                    'file': jf.relative_to(ROOT).as_posix(),
                    'key': key,
                    'line_no': line_no,
                    'findings': findings,
                    'text': line[:100]
                })

# Sort by highest severity per hit
SEV = {'HIGH': 0, 'MED': 1, 'LOW': 2}
def max_sev(h):
    return min(SEV[f[0]] for f in h['findings'])

hits.sort(key=lambda h: (max_sev(h), h['file'], h['key']))

# Report
print('=' * 80)
print(f'Comprehensive wrap-hostile scan: {len(hits)} risky lines found')
print('=' * 80)

def sev_of(h):
    for order in ['HIGH', 'MED', 'LOW']:
        if any(f[0] == order for f in h['findings']):
            return order
    return 'LOW'

by_sev = {'HIGH':[], 'MED':[], 'LOW':[]}
for h in hits:
    by_sev[sev_of(h)].append(h)

for sev in ['HIGH', 'MED', 'LOW']:
    print(f'\n===== {sev} ({len(by_sev[sev])}) =====')
    for h in by_sev[sev]:
        f_summary = ' | '.join(f'{s}:{d}' for s,d in h['findings'])
        print(f'  {h["file"]:35} :: {h["key"]:30} L{h["line_no"]}')
        print(f'     {f_summary}')
        print(f'     txt: {h["text"]}')
