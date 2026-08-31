#!/usr/bin/env python3
"""
Pkunk v0.7 delta patch (2026-08-18)
- Q1=B: 保留少量 signature 靈啟 tokens 的「吾」
- Q2=B: 不動 dossier
- Q3=B: 輕量 delta patch（不做 v3 clean-room）
- Q4=A: 全依推薦（爾/爾等→你/你們的、乃→是）

保留策略：
  HATE_YOU_FOREVER_2 = 保留全部 7 個「吾」（PLAM PRIKKY 出神招牌）
  SENSE_KOHRAH_VICTORY = 保留 2 個「吾等」（夢境敘述招牌），清 4 個單獨「吾」
  NEED_HELP = 保留 line 0「吾正與你建立靈感聯繫」（psychic link 首句 icon），清 4 個
  其餘所有 tokens = 全清「吾」→「我」

Q4 targeted:
  HATE_YOU_FOREVER_3: 爾×2→你×2, 爾等×1→你們的×1
  WAR_GOES_2: 那石乃→那石是
"""
import json
import re
import sys
from pathlib import Path
from collections import OrderedDict

SRC = Path('translations/pkunk.zh-TW.json')

# ---- load preserving order ----
with SRC.open('r', encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)

SIGNATURE_KEEP_ALL = {'HATE_YOU_FOREVER_2'}
SIGNATURE_KEEP_LINE_0 = {'NEED_HELP'}
SIGNATURE_KEEP_WUDENG_ONLY = {'SENSE_KOHRAH_VICTORY'}

def clear_standalone_wu(text):
    """Replace standalone 吾 (not 吾等) with 我"""
    return re.sub(r'吾(?!等)', '我', text)

changes = []   # (key, before, after, wu_before, wu_after)

for key, val in data.items():
    if key == '_notes' or not isinstance(val, str):
        continue

    original = val
    new_val = val

    wu_before = len(re.findall(r'吾(?!等)', original))
    wudeng_before = len(re.findall(r'吾等', original))

    if key in SIGNATURE_KEEP_ALL:
        # Keep everything as-is
        pass
    elif key in SIGNATURE_KEEP_WUDENG_ONLY:
        # Clear standalone 吾, keep 吾等
        new_val = clear_standalone_wu(new_val)
    elif key in SIGNATURE_KEEP_LINE_0:
        # Keep only line 0's 吾, clear others
        lines = new_val.split('\n')
        for i in range(1, len(lines)):
            lines[i] = clear_standalone_wu(lines[i])
        new_val = '\n'.join(lines)
    else:
        # Default: clear all standalone 吾
        new_val = clear_standalone_wu(new_val)

    # Q4 targeted for HATE_YOU_FOREVER_3 & WAR_GOES_2
    if key == 'HATE_YOU_FOREVER_3':
        new_val = new_val.replace('爾等', '你們的')
        # standalone 爾 (not 爾等, not 偶爾) → 你
        new_val = re.sub(r'(?<!偶)爾(?!等)', '你', new_val)
    if key == 'WAR_GOES_2':
        new_val = new_val.replace('那石乃', '那石是')

    if new_val != original:
        wu_after = len(re.findall(r'吾(?!等)', new_val))
        wudeng_after = len(re.findall(r'吾等', new_val))
        changes.append({
            'key': key,
            'wu_before': wu_before,
            'wu_after': wu_after,
            'wudeng_before': wudeng_before,
            'wudeng_after': wudeng_after,
            'before': original,
            'after': new_val,
        })
        data[key] = new_val

# ---- write back ----
out = json.dumps(data, ensure_ascii=False, indent=2)
with SRC.open('w', encoding='utf-8') as f:
    f.write(out)

# ---- summary ----
print(f'=== Pkunk delta patch summary ===')
print(f'Modified tokens: {len(changes)}')
total_wu_cleared = sum(c['wu_before'] - c['wu_after'] for c in changes)
total_wudeng_cleared = sum(c['wudeng_before'] - c['wudeng_after'] for c in changes)
print(f'吾 cleared:     {total_wu_cleared}')
print(f'吾等 cleared:   {total_wudeng_cleared}')
print()

print('=== per-token changes ===')
for c in changes:
    marker = ''
    if c['key'] == 'HATE_YOU_FOREVER_3':
        marker = '  <Q4.1-3 爾/爾等→你/你們的>'
    elif c['key'] == 'WAR_GOES_2':
        marker = '  <Q4.4 那石乃→那石是>'
    elif c['key'] == 'SENSE_KOHRAH_VICTORY':
        marker = '  <signature: 保留吾等×2>'
    elif c['key'] == 'NEED_HELP':
        marker = '  <signature: 保留 line 0 吾>'
    print(f"  {c['key']:35s}  吾: {c['wu_before']}→{c['wu_after']}  吾等: {c['wudeng_before']}→{c['wudeng_after']}{marker}")

print()
print('=== final purity (dialog only) ===')
# Reload, recount
with SRC.open('r', encoding='utf-8') as f:
    reloaded = json.load(f)
total_wu = 0
total_wudeng = 0
total_er_standalone = 0
total_erdeng = 0
total_nai_not_shi = 0
total_zai = 0
total_yi = 0
total_ru = 0
for k, v in reloaded.items():
    if k == '_notes' or not isinstance(v, str):
        continue
    total_wu += len(re.findall(r'吾(?!等)', v))
    total_wudeng += len(re.findall(r'吾等', v))
    total_er_standalone += len(re.findall(r'(?<!偶)爾(?!等)', v))
    total_erdeng += len(re.findall(r'爾等', v))
    total_nai_not_shi += len(re.findall(r'乃(?!是)', v))
    total_zai += v.count('哉')
    total_yi += v.count('矣')
    total_ru += v.count('汝')

print(f'  吾:   {total_wu}   (target: 8 = HATE_YOU_FOREVER_2×7 + NEED_HELP line 0×1)')
print(f'  吾等: {total_wudeng}   (target: 2 = SENSE_KOHRAH_VICTORY 夢境×2)')
print(f'  爾 (單獨,非偶爾): {total_er_standalone}')
print(f'  爾等: {total_erdeng}')
print(f'  乃 (非乃是): {total_nai_not_shi}')
print(f'  哉:   {total_zai}')
print(f'  矣:   {total_yi}')
print(f'  汝:   {total_ru}')

# Save diff log
DIFF_LOG = Path('_pkunk_delta_diff.md')
with DIFF_LOG.open('w', encoding='utf-8') as f:
    f.write('# Pkunk delta patch diff (2026-08-18)\n\n')
    f.write('**Policy**: Q1=B signature preserve 3 tokens · Q2=B no dossier change · Q3=B lightweight delta · Q4=A recommended\n\n')
    f.write(f'**Summary**: {len(changes)} tokens modified · 吾 cleared: {total_wu_cleared} · 吾等 cleared: {total_wudeng_cleared}\n\n')
    for c in changes:
        f.write(f'## `{c["key"]}`\n\n')
        f.write(f'- 吾: {c["wu_before"]} → {c["wu_after"]}\n')
        if c['wudeng_before'] != c['wudeng_after']:
            f.write(f'- 吾等: {c["wudeng_before"]} → {c["wudeng_after"]}\n')
        f.write('\n')
        f.write('**Before**:\n\n```\n')
        f.write(c['before'])
        f.write('\n```\n\n')
        f.write('**After**:\n\n```\n')
        f.write(c['after'])
        f.write('\n```\n\n---\n\n')

print(f'\nDiff log: {DIFF_LOG}')
