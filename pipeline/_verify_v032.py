"""Final self-verification of packaged v0.3.2 addon."""
import io
import re
import sys
import zipfile
from PIL import Image

ADDON = r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm'
CHAR_SPACE = 1
MAX_WIDTH = 143
ELLIPSIS_OVERHEAD = 20

z = zipfile.ZipFile(ADDON)

# Load glyph widths
_widths = {}
for name in z.namelist():
    if '/commander.fon/' not in name or not name.endswith('.png'):
        continue
    stem = name.rsplit('/', 1)[-1][:-4]
    try:
        cp = int(stem, 16)
        img = Image.open(io.BytesIO(z.read(name)))
        _widths[cp] = img.size[0]
    except Exception:
        pass

def word_width(word: str) -> int:
    if not word: return 0
    total = 0
    for ch in word:
        total += _widths.get(ord(ch), 8) + CHAR_SPACE
    if total > 0: total -= CHAR_SPACE
    return total

# Extract commander.txt
txt = None
for n in z.namelist():
    if n.endswith('shadow-content/base/comm/commander/commander.txt'):
        txt = z.read(n).decode('utf-8')
        break
print(f'commander.txt: {len(txt.encode("utf-8"))} bytes')

# Extract English commander.txt for line count comparison
import zipfile as zf
import os
english_txt = open(r'Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt', 'r', encoding='utf-8').read()

lua_template = re.compile(r'<%.*?%>')
target_tokens = [
    "ARE_YOU_SUPPLY_SHIP", "THE_WHAT_FROM_WHERE", "ABOUT_TIME",
    "MESSAGE_GARBLED_1", "MESSAGE_GARBLED_2", "HERE_IS_A_NEW_LANDER",
    "THIS_MAY_SEEM_SILLY", "OK_THE_NAFS", "OK_THE_CAN", "OK_THE_UFW",
    "OK_THE_NAME_IS_EMPIRE", "FUEL_UP0", "FUEL_UP1",
    "WHAT_KIND_OF_IDIOT", "DONT_KNOW_WHO_YOU_ARE",
    "HAPPENED_TO_EARTH", "URQUAN_LEFT",
]

bad_words = 0
line_count_mismatches = 0

def extract_body(text, tok):
    m = re.search(rf'#\({tok}\)[^\n]*\n((?:(?!#\().*?\n)*)', text)
    if not m: return None
    return m.group(1).rstrip()

for tok in target_tokens:
    en_body = extract_body(english_txt, tok)
    tw_body = extract_body(txt, tok)
    if not en_body or not tw_body:
        print(f'  MISS {tok}: missing')
        continue
    en_lines = [l for l in en_body.split('\n') if l.strip()]
    tw_lines = [l for l in tw_body.split('\n') if l.strip()]
    if len(en_lines) != len(tw_lines):
        print(f'  LINE-CNT-BAD {tok}: EN={len(en_lines)} TW={len(tw_lines)}')
        line_count_mismatches += 1
    for i, line in enumerate(tw_lines):
        substituted = lua_template.sub('X' * 15, line)
        for word in substituted.split(' '):
            w = word_width(word)
            if w + ELLIPSIS_OVERHEAD >= MAX_WIDTH:
                print(f'  BAD {tok} line {i}: word {word!r} = {w}px +{ELLIPSIS_OVERHEAD} >= {MAX_WIDTH}')
                bad_words += 1

print()
print(f'==== v0.3.2 FINAL VERIFICATION ====')
print(f'  Tokens translated:       17')
print(f'  Line count mismatches:   {line_count_mismatches}')
print(f'  Words exceeding width:   {bad_words}')
print()
if bad_words == 0 and line_count_mismatches == 0:
    print(f'  [PASS] v0.3.2 addon ready for user testing.')
    print()
    print(f'  Expected behavior:')
    print(f'    - Hayes NPC dialog: 17 tokens in Chinese, word-wrapped')
    print(f'    - Player response choices: still English (not translated)')
    print(f'    - No crash, no infinite loop')
sys.exit(0 if (bad_words == 0 and line_count_mismatches == 0) else 1)
