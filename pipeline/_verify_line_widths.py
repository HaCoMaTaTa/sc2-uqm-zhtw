"""Verify that no translated line in commander.zh-TW.json exceeds AlienTextWidth.

commander.AlienTextWidth = RES_SCALE(143) = 143 px in SD mode.
comm.c getLineWithinWidth() FAILS (infinite loop in _count_lines) if a
single "word" (CJK has no spaces = whole line is one word) is >= maxWidth.

Line width = sum(glyph.width + CharSpace) - CharSpace (trailing removed).
CharSpace for commander.fon = 1 (from kerndat.fnt).
"""
import json
import os
import sys
from PIL import Image

FONT_DIR = r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\_stage\zh-TW\shadow-content\base\fonts\commander.fon"
CHAR_SPACE = 1  # from kerndat.fnt
MAX_WIDTH = 143  # commander_desc.AlienTextWidth in SD
SAFETY = 5  # margin
LIMIT = MAX_WIDTH - SAFETY

# Cache glyph widths
_width_cache = {}
def glyph_width(ch: str) -> int:
    if ch in _width_cache:
        return _width_cache[ch]
    cp = ord(ch)
    fname = f'{cp:05x}.png'
    p = os.path.join(FONT_DIR, fname)
    if not os.path.exists(p):
        # For missing chars, use a conservative 8px default (English fallback)
        w = 8
    else:
        try:
            img = Image.open(p)
            w = img.size[0]
        except Exception:
            w = 8
    _width_cache[ch] = w
    return w

def line_width(line: str) -> int:
    """Simulate comm.c width calc: sum(glyph.width + 1) - 1 for last."""
    if not line:
        return 0
    total = 0
    for ch in line:
        if ch == '\n':
            break
        total += glyph_width(ch) + CHAR_SPACE
    if total > 0:
        total -= CHAR_SPACE  # trailing charspace removed
    return total

def check_translation(path: str):
    import re
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    total_bad = 0
    total_lines = 0
    # Match Lua interpolation like <% ... %>
    lua_template = re.compile(r'<%.*?%>')
    for key, val in data.items():
        if key.startswith('_'):
            continue
        lines = val.split('\n')
        for i, line in enumerate(lines):
            # Substitute Lua templates with 15-char ASCII placeholder
            # (captain name max is 15 chars via SIS_CAPTAIN_NAME_MAX)
            substituted = lua_template.sub('X' * 15, line)
            w = line_width(substituted)
            total_lines += 1
            if w >= LIMIT:
                total_bad += 1
                print(f'  BAD  {key} line {i}: {w:3d}px (limit {LIMIT}): {line!r}')
            elif w >= LIMIT - 20:
                print(f'  WARN {key} line {i}: {w:3d}px (close to {LIMIT}): {line!r}')
    print()
    print(f'== Summary ==')
    print(f'  Total lines: {total_lines}')
    print(f'  Bad (>= {LIMIT}px): {total_bad}')
    print(f'  Absolute limit: {MAX_WIDTH}px (comm.c AlienTextWidth)')
    return total_bad == 0

if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else r'Q:\Dos_G\StarControl2\uqm-work\translations\commander.zh-TW.json.new'
    ok = check_translation(p)
    sys.exit(0 if ok else 1)
