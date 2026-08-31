"""Verify space-wrap translation: each SPACE-DELIMITED WORD must fit within
AlienTextWidth. getLineWithinWidth breaks at spaces, so as long as no single
word (span between spaces) exceeds width, wrapping works.
"""
import json
import os
import sys
import re
from PIL import Image

FONT_DIR = r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\_stage\zh-TW\shadow-content\base\fonts\commander.fon"
CHAR_SPACE = 2  # commander.fon kerndat: "commander.fon 14 2 1 4" → CharSpace=2
MAX_WIDTH = 143
LIMIT = MAX_WIDTH - 5
ELLIPSIS_OVERHEAD = 28  # lead+trail "..." at 2px each + CharSpaces overhead

_width_cache = {}
def glyph_width(ch: str) -> int:
    if ch in _width_cache:
        return _width_cache[ch]
    cp = ord(ch)
    p = os.path.join(FONT_DIR, f'{cp:05x}.png')
    if not os.path.exists(p):
        w = 8
    else:
        try:
            w = Image.open(p).size[0]
        except Exception:
            w = 8
    _width_cache[ch] = w
    return w

def word_width(word: str) -> int:
    if not word:
        return 0
    total = 0
    for ch in word:
        total += glyph_width(ch) + CHAR_SPACE
    if total > 0:
        total -= CHAR_SPACE
    return total

def check_translation(path: str):
    lua_template = re.compile(r'<%.*?%>')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    total_bad = 0
    total_lines = 0
    for key, val in data.items():
        if key.startswith('_'):
            continue
        for line_idx, line in enumerate(val.split('\n')):
            total_lines += 1
            substituted = lua_template.sub('X' * 15, line)
            words = substituted.split(' ')
            for w_idx, word in enumerate(words):
                w = word_width(word)
                # A "word" needs to fit including possible lead ellipsis
                # (SplitSubPages adds "..." to any page NOT starting the whole track)
                effective = w + ELLIPSIS_OVERHEAD
                if effective >= MAX_WIDTH:
                    print(f'  BAD  {key} line {line_idx} word {w_idx}: {w}px (+{ELLIPSIS_OVERHEAD}ellips = {effective}): {word!r}')
                    total_bad += 1
                elif effective >= LIMIT:
                    print(f'  WARN {key} line {line_idx} word {w_idx}: {w}px (+ellips = {effective}): {word!r}')
    print()
    print(f'== Summary ==')
    print(f'  Total lines: {total_lines}')
    print(f'  Bad words (+ellipsis >= {MAX_WIDTH}): {total_bad}')
    return total_bad == 0

if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else r'Q:\Dos_G\StarControl2\uqm-work\translations\commander.zh-TW.json'
    ok = check_translation(p)
    sys.exit(0 if ok else 1)
