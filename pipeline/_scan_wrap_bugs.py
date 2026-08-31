"""Scan all translations/**/*.zh-TW.json for character sequences that MAY trigger
the same class of engine wrap-bug seen in vux.LIKE_BECAUSE ('嗯～～～～').

Focus:
  (1) Runs of >=3 identical non-standard-Chinese-punct fullwidth chars.
      Fullwidth-tilde 〜 U+301C / ～ U+FF5E are prime suspects.
      Also flag repeated fullwidth *, =, _, +, @, #, etc.
  (2) Runs of >=5 identical common punct (may still overflow):
      ！！！！！  ？？？？？  。。。。。  ，，，，，
  (3) Runs of half-width punct >=6 (---, ***, ~~~, ===, ___)
      that are followed/preceded by CJK (mixed pattern risk)
  (4) Runs of any single-char >=8 (long overflow suspects)

Common SAFE patterns (skip):
  ……  ——  ──  — well-known CJK punctuation, wrap-safe.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(r'Q:\Dos_G\StarControl2\uqm-work\translations')

# SUSPECT fullwidth chars — 全形但不是標準中文標點, wrap 引擎沒 rule
SUSPECT_FW_CHARS = [
    '\u301c',  # 〜 wave dash
    '\uff5e',  # ～ fullwidth tilde  (vux 已中招)
    '\uff0a',  # ＊ fullwidth asterisk
    '\uff1d',  # ＝ fullwidth equal
    '\uff3f',  # ＿ fullwidth underscore
    '\uff0b',  # ＋ fullwidth plus
    '\uff20',  # ＠ fullwidth at
    '\uff03',  # ＃ fullwidth hash
    '\uff04',  # ＄ fullwidth dollar
    '\uff05',  # ％ fullwidth percent
    '\uff06',  # ＆ fullwidth ampersand
    '\uff3c',  # ＼ fullwidth backslash
    '\uff0f',  # ／ fullwidth slash
    '\uff5c',  # ｜ fullwidth pipe
    '\u3000',  # 　 ideographic space
]

# COMMON but potentially overflow-inducing punctuation
FW_PUNCT_LONG = [
    '\uff01',  # ！
    '\uff1f',  # ？
    '\u3002',  # 。
    '\uff0c',  # ，
    '\uff1b',  # ；
    '\uff1a',  # ：
]

# HW ASCII punct
HW_ASCII_LONG = ['-', '*', '~', '=', '_', '+', '#', '.']

# COMMON SAFE (skip - well-established CJK punctuation)
COMMON_SAFE_PATTERNS = [
    ('\u2026\u2026', 'ellipsis ……'),           # …… (2× U+2026)
    ('\u2014\u2014', 'em-dash ——'),             # ——
    ('\u2500\u2500', 'box-draw ──'),            # ── (used as dash in this project)
]

findings = []

def is_cjk_char(c):
    o = ord(c)
    return 0x4e00 <= o <= 0x9fff or 0x3400 <= o <= 0x4dbf

for jf in sorted(ROOT.rglob('*.zh-TW.json')):
    try:
        d = json.loads(jf.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'!! parse error {jf.name}: {e}')
        continue

    for key, val in d.items():
        if key.startswith('_'):
            continue
        if not isinstance(val, str):
            continue

        # (1) Suspect FW chars — flag runs of >=3
        for ch in SUSPECT_FW_CHARS:
            for m in re.finditer(re.escape(ch) + r'{3,}', val):
                # Get context
                ctx_start = max(0, m.start() - 30)
                ctx_end = min(len(val), m.end() + 30)
                ctx = val[ctx_start:ctx_end].replace('\n', '↵')
                findings.append({
                    'severity': 'HIGH',
                    'file': jf.relative_to(ROOT).as_posix(),
                    'key': key,
                    'ch': ch,
                    'unicode': f'U+{ord(ch):04X}',
                    'run_len': len(m.group()),
                    'context': ctx,
                    'kind': 'suspect FW char run'
                })

        # (2) Common FW punct — flag runs of >=5
        for ch in FW_PUNCT_LONG:
            for m in re.finditer(re.escape(ch) + r'{5,}', val):
                ctx_start = max(0, m.start() - 30)
                ctx_end = min(len(val), m.end() + 30)
                ctx = val[ctx_start:ctx_end].replace('\n', '↵')
                findings.append({
                    'severity': 'MED',
                    'file': jf.relative_to(ROOT).as_posix(),
                    'key': key,
                    'ch': ch,
                    'unicode': f'U+{ord(ch):04X}',
                    'run_len': len(m.group()),
                    'context': ctx,
                    'kind': 'common FW punct excessive'
                })

        # (3) HW ASCII punct >=6 adjacent to CJK
        for ch in HW_ASCII_LONG:
            for m in re.finditer(re.escape(ch) + r'{6,}', val):
                # Check adjacent chars
                left = val[m.start()-1] if m.start() > 0 else ''
                right = val[m.end()] if m.end() < len(val) else ''
                if is_cjk_char(left) or is_cjk_char(right):
                    ctx_start = max(0, m.start() - 30)
                    ctx_end = min(len(val), m.end() + 30)
                    ctx = val[ctx_start:ctx_end].replace('\n', '↵')
                    findings.append({
                        'severity': 'MED',
                        'file': jf.relative_to(ROOT).as_posix(),
                        'key': key,
                        'ch': ch,
                        'unicode': f'U+{ord(ch):04X}',
                        'run_len': len(m.group()),
                        'context': ctx,
                        'kind': 'HW punct run adjacent CJK'
                    })

# Report
severity_order = {'HIGH':0, 'MED':1, 'LOW':2}
findings.sort(key=lambda x: (severity_order.get(x['severity'], 3), x['file'], x['key']))

print('='*80)
print(f'Wrap-bug scan: {len(findings)} suspect run(s) found')
print('='*80)

if not findings:
    print('  (no findings — no runs of 3+ suspect FW chars, 5+ common FW punct, or 6+ HW punct adjacent CJK)')
else:
    prev_sev = None
    for f in findings:
        if f['severity'] != prev_sev:
            print(f"\n--- Severity: {f['severity']} ---")
            prev_sev = f['severity']
        print(f"  {f['file']} :: {f['key']}")
        print(f"     {f['run_len']}× {f['ch']!r} ({f['unicode']}) — {f['kind']}")
        print(f"     ctx: ...{f['context']}...")
