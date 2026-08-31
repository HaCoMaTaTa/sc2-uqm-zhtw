"""Empirical test: use SPACES for word wrap instead of \\n page breaks.

Rationale:
- getLineWithinWidth() breaks at SPACES (like English word-wrap).
- If CJK text has NO spaces, whole line = one "word" = infinite loop if >width.
- If we INSERT spaces between semantic chunks, engine word-wraps to fit.
- BONUS: keeping same \\n count as English preserves voice-cue timing.

Test approach: use exactly 8 lines (matching English ARE_YOU_SUPPLY_SHIP),
with spaces within each line to allow wrapping.
"""
import shutil
import subprocess
import sys
import os

os.chdir(r'Q:\Dos_G\StarControl2\uqm-work')

# Diagnostic: use SPACES for wrap, same line count as English (8 lines)
diag = '''{
  "_notes": ["Space-wrap diagnostic: same \\n count as English, spaces for wrap"],
  "ARE_YOU_SUPPLY_SHIP": "警告！ 身分不明 星艦！\\n我是 指揮官海斯 地球奴隸行星 星際基地。\\n超波訊號 極弱\\n情況危急 能量 核心耗盡\\n掃描儀 與雷達 皆失效\\n無法辨識 爾方艦艇。\\n爾等是 階層 補給船嗎？\\n重複， 是補給船嗎？"
}'''

# Backup current
src = r'translations\commander.zh-TW.json'
bak = r'translations\commander.zh-TW.json.pages-v031'
if not os.path.exists(bak):
    shutil.copy(src, bak)

with open(src, 'w', encoding='utf-8') as f:
    f.write(diag)

print('Wrote space-wrap diagnostic JSON.')
print('Rebuilding...')
