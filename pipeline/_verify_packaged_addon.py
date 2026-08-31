"""Final self-verification: extract commander.txt from packaged addon and check
every line's width against the AlienTextWidth = 143px limit."""
import json
import os
import re
import sys
import zipfile
from pathlib import Path
from PIL import Image

HERE = Path(__file__).parent.resolve()   # pipeline/
ADDON = str(HERE / 'install' / 'content' / 'addons' / 'zh-TW.uqm')
FONT_DIR_IN_ZIP = 'zh-TW/shadow-content/base/fonts/commander.fon/'
CHAR_SPACE = 1
MAX_WIDTH = 143
LIMIT = MAX_WIDTH - 5  # 138

# Load font glyph widths from the addon ZIP itself
z = zipfile.ZipFile(ADDON)
_widths = {}
for name in z.namelist():
    if not name.startswith(FONT_DIR_IN_ZIP): continue
    if not name.endswith('.png'): continue
    stem = name[len(FONT_DIR_IN_ZIP):-4]
    try:
        cp = int(stem, 16)
    except ValueError:
        continue
    import io
    data = z.read(name)
    img = Image.open(io.BytesIO(data))
    _widths[cp] = img.size[0]

def line_width(line: str) -> int:
    if not line:
        return 0
    total = 0
    for ch in line:
        cp = ord(ch)
        w = _widths.get(cp, 8)  # fallback 8px if missing
        total += w + CHAR_SPACE
    if total > 0:
        total -= CHAR_SPACE
    return total

# Extract commander.txt and parse blocks
txt_bytes = None
for n in z.namelist():
    if n.endswith('shadow-content/base/comm/commander/commander.txt'):
        txt_bytes = z.read(n)
        break
if not txt_bytes:
    print('ERROR: commander.txt not found in addon')
    sys.exit(2)

text = txt_bytes.decode('utf-8')
print(f'Read commander.txt: {len(txt_bytes)} bytes, {len(text.splitlines())} lines')

# Parse blocks: #(TOKEN) header ... content ... blank lines
lua_template = re.compile(r'<%.*?%>')

blocks = []
current_id = None
current_lines = []
for line in text.split('\n'):
    m = re.match(r'#\(([A-Z0-9_]+)\)', line)
    if m:
        if current_id:
            blocks.append((current_id, current_lines))
        current_id = m.group(1)
        current_lines = []
    elif current_id and line.strip():
        current_lines.append(line)
if current_id:
    blocks.append((current_id, current_lines))

print(f'Parsed {len(blocks)} blocks')
print()

# Check each block: only check ones with CJK content (translated)
bad_count = 0
warn_count = 0
translated_blocks = 0
for tok, lines in blocks:
    has_cjk = any(any('\u4e00' <= c <= '\u9fff' or '\u3000' <= c <= '\u303f' or '\uff00' <= c <= '\uffef' for c in line) for line in lines)
    if not has_cjk:
        continue
    translated_blocks += 1
    for i, line in enumerate(lines):
        # Substitute Lua template with 15-char ASCII placeholder
        substituted = lua_template.sub('X' * 15, line)
        w = line_width(substituted)
        if w >= MAX_WIDTH:
            print(f'  BAD  {tok} line {i}: {w:3d}px >= {MAX_WIDTH}: {line!r}')
            bad_count += 1
        elif w >= LIMIT:
            print(f'  WARN {tok} line {i}: {w:3d}px close to limit: {line!r}')
            warn_count += 1

print()
print(f'==== VERIFICATION SUMMARY ====')
print(f'  Blocks with CJK: {translated_blocks}')
print(f'  Bad lines (>= {MAX_WIDTH}px absolute limit): {bad_count}')
print(f'  Warn lines (>= {LIMIT}px safety limit):     {warn_count}')
if bad_count == 0:
    print()
    print(f'  [PASS] No line exceeds AlienTextWidth = {MAX_WIDTH}px.')
    print(f'         Infinite loop in _count_lines() will NOT be triggered.')
sys.exit(0 if bad_count == 0 else 1)
