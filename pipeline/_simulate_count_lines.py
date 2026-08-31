"""Simulate UQM _count_lines() exactly to find infinite-loop-triggering subtitles.

Reads glyph widths from the PACKAGED ADDON ZIP (source of truth for what the
game actually loads), not from a temp _stage/ folder that may not exist.

Reproduces:
- SplitSubPages() page splitting with lead/trail "..." for non-ASCII-punct endings
- CharSpace = 2 (from kerndat)
- getLineWithinWidth() word-wrap logic with backing-off on overflow
- _count_lines() do-while loop -- INFINITE LOOP if getLineWithinWidth
  returns FALSE without advancing pStr
"""
import io
import re
import sys
import zipfile
from pathlib import Path
from PIL import Image

HERE = Path(__file__).parent.resolve()   # pipeline/
ADDON = str(HERE / 'install' / 'content' / 'addons' / 'zh-TW.uqm')
CHAR_SPACE = 2  # verified from kerndat.fnt: "commander.fon 14 2 1 4"
MAX_WIDTH = 143  # AlienTextWidth for commander

# Read widths directly from the packaged addon (source of truth)
_widths = {}
_missing = set()
try:
    z = zipfile.ZipFile(ADDON)
    for name in z.namelist():
        if '/commander.fon/' not in name or not name.endswith('.png'):
            continue
        stem = name.rsplit('/', 1)[-1][:-4]
        try:
            cp = int(stem, 16)
            _widths[cp] = Image.open(io.BytesIO(z.read(name))).size[0]
        except Exception:
            pass
    print(f'Loaded {len(_widths)} glyph widths from packaged addon.')
except Exception as e:
    print(f'WARNING: Cannot read addon {ADDON}: {e}')
    print('  Sim may use fallback widths (INACCURATE).')

def char_width(ch):
    cp = ord(ch)
    if cp in _widths:
        return _widths[cp]
    _missing.add(ch)
    return 8  # fallback

def get_char_from_string(text, ptr):
    """Return (unicode_char, new_ptr). ptr is byte offset into UTF-8 text."""
    if ptr >= len(text):
        return '\0', ptr
    ch = text[ptr]
    return ch, ptr + 1

def text_rect_width(text_chars):
    """Sum(width + CharSpace) - CharSpace (trailing subtract if any width>0)."""
    if not text_chars:
        return 0
    total = 0
    for ch in text_chars:
        total += char_width(ch) + CHAR_SPACE
    if total > 0:
        total -= CHAR_SPACE
    return total

def get_line_within_width(text, max_width, max_chars):
    """Simulates comm.c getLineWithinWidth(). Returns (chars_consumed_len,
    start_next_ptr, eol, ok_advanced) matching engine behavior.

    ok_advanced=False AND eol=False AND start_next==0 → infinite loop trigger.
    """
    ptr = 0
    char_count = 0
    old_count = 1
    eol = False
    while True:
        word_start = ptr
        # Scan one word
        while True:
            if ptr >= len(text) or text[ptr] == '\0':
                eol = True
                done = True
                break
            ch = text[ptr]
            ptr += 1
            eol = ch in ('\0', '\n', '\r')
            done = eol or char_count >= max_chars
            if done or ch == ' ':
                break
            char_count += 1

        # TextRect on first char_count chars from text[0:]
        text_slice = text[:char_count]
        rect_w = text_rect_width(text_slice)

        if rect_w >= max_width:
            # Back off
            return old_count, word_start, False  # False = not eol
        if done:
            return char_count, ptr, eol

        # Fits and not done: continue to next word
        old_count = char_count
        char_count += 1  # for the space we skipped

def count_lines(subtitle_text, max_width):
    """Simulate _count_lines. Returns num_lines or 'INFINITE_LOOP'."""
    text = subtitle_text
    ptr = 0
    num_lines = 0
    seen = set()
    for _ in range(200):  # safety cap
        num_lines += 1
        if ptr in seen:
            # We revisited same position → engine would infinite-loop here.
            return 'INFINITE_LOOP', num_lines
        seen.add(ptr)
        remaining = text[ptr:]
        if not remaining:
            return num_lines, num_lines
        char_count, next_offset, eol = get_line_within_width(remaining, max_width, (1 << 16) - 1)
        if eol:
            return num_lines, num_lines
        ptr = ptr + next_offset
    return 'RUNAWAY_LOOP', num_lines


def split_sub_pages(block_text):
    """Simulate SplitSubPages() adding lead/trail '...' for non-ASCII-punct."""
    import string
    ascii_punct_isspace = set(string.punctuation + string.whitespace)

    pages = []
    lines = block_text.split('\n')
    lines = [l for l in lines if l.strip()]  # skip blank
    for i, line in enumerate(lines):
        is_last = (i == len(lines) - 1)
        # aft_ellips: 3 if not last AND line's last char (as byte) is NOT ispunct
        # AND NOT isspace. Because C uses last BYTE of UTF-8, non-ASCII always
        # fails ispunct/isspace.
        last_char = line[-1] if line else ''
        # Since we're checking char-by-char (not byte), use rough rule:
        # if last char > 0x7F (non-ASCII), aft_ellips = 3
        if not is_last and last_char and (ord(last_char) > 0x7F or last_char not in ascii_punct_isspace):
            aft = 3
        else:
            aft = 0

        lead = 3 if i > 0 and pages and pages[-1].endswith('...') else 0
        page_text = ('.' * lead) + line + ('.' * aft)
        pages.append(page_text)
    return pages


def check_all_translations():
    import json
    trans = json.loads(open(str(HERE / 'translations' / 'commander.zh-TW.json'), encoding='utf-8').read())

    lua_template = re.compile(r'<%.*?%>')
    # Simulate MAX-length captain name (UQM SIS_CAPTAIN_NAME_MAX = 15 ASCII chars)
    max_captain = 'X' * 15

    total_pages = 0
    bad = 0
    for tok, val in trans.items():
        if tok.startswith('_'):
            continue
        # Skip player-response tokens (lowercase) — no _count_lines call
        if tok[0].islower():
            continue
        # Substitute Lua template with max-plausible captain name
        val = lua_template.sub(max_captain, val)
        pages = split_sub_pages(val)
        for pnum, page in enumerate(pages):
            total_pages += 1
            result, num_lines = count_lines(page, MAX_WIDTH)
            if result == 'INFINITE_LOOP':
                print(f'  INFINITE_LOOP {tok} page {pnum}: {page!r}')
                bad += 1
            elif result == 'RUNAWAY_LOOP':
                print(f'  RUNAWAY {tok} page {pnum}: {page!r}')
                bad += 1
    print()
    print(f'== Summary ==')
    print(f'  Total NPC subtitle pages checked: {total_pages}')
    print(f'  Infinite-loop pages:              {bad}')
    print(f'  Char widths sample: A={char_width("A")}px, 中={char_width("中")}px, ！={char_width("！")}px, ，={char_width("，")}px, . ={char_width(".")}px, space={char_width(" ")}px, X={char_width("X")}px, CharSpace={CHAR_SPACE}px')
    if _missing:
        print()
        print(f'  ★★★★ WARNING: {len(_missing)} chars NOT in packaged addon, fell back to 8px:')
        print(f'      {sorted(_missing)[:30]}')
        print(f'      → Widths were UNDER-ESTIMATED. Sim result may be WRONG.')
        print(f'      → Rebuild + repackage before trusting sim.')
        sys.exit(2)  # hard-fail
    if bad > 0:
        sys.exit(1)

check_all_translations()
