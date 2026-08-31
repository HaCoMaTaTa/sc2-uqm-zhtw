"""Root-cause-based wrap-hostile scanner (v3).

Derived from code analysis of UQM-MegaMod/src/uqm/comm.c:getLineWithinWidth().

CONFIRMED root cause:
  getLineWithinWidth() only breaks at:
    1. ASCII space  ' '
    2. Line terminators \\n \\r \\0
    3. CJK Unified Ideographs U+4E00–U+9FFF (zh-TW patch)

  Any run of characters OUTSIDE these categories that exceeds the
  alien-specific `AlienTextWidth` triggers infinite wrap failure —
  the caller re-invokes getLineWithinWidth on the SAME word repeatedly,
  each time advancing baseline.y, cascading text down the screen.

Empirical widths (per char) in DOS SIS_SCREEN_WIDTH=~243px mode:
  ASCII printable:  7px glyph + 1px CharSpace = 8px effective
  Fullwidth punct / dashes / ellipsis (>=0x2000): 14px + 1px = 15px

Alien-specific text widths (from src/uqm/comm/*.c):
  arilou, chmmr, druuge, ilwrath, kohrah, melnorme, mycon, orz, pkunk,
  slyland, spahome (=safeones), spathi, supox, syreen, talkpet, thraddc,
  umgah, urquan, utwig                                     : SIS_TEXT_WIDTH-16  = 211
  vux                                                     : (STW-16)>>1        = 105  << HALF!
  yehat, rebel (=yehatrebels)                             : (STW-16)*2/3       = 140
  zoqfotpik                                               : STW>>1 - offset    = 112
  commander, starbase                                     : RES_SCALE(143)     = 143
  shofixti, slyhome                                       : SIS_TEXT_WIDTH     = 227

Scanning: for each translation dialogue line, find atomic non-CJK non-space runs
and estimate width. Flag any run whose width exceeds the alien's text_width.
"""
import json, re, sys
from pathlib import Path

# Per-file text_width map (defaults to 211 if not listed)
ALIEN_WIDTH = {
    'arilou':      211,
    'chmmr':       211,
    'commander':   143,
    'druuge':      211,
    'ilwrath':     211,
    'kohrah':      211,
    'melnorme':    211,
    'mycon':       211,
    'orz':         211,
    'pkunk':       211,
    'probe':       211,   # slylandro probe, likely default
    'safeones':    211,   # spahome
    'shofixti':    227,
    'slylandro':   211,   # slyland (in HyperSpace); slyhome uses 227
    'spathi':      211,
    'starbase':    143,
    'supox':       211,
    'syreen':      211,
    'talkingpet':  211,
    'thraddash':   211,
    'umgah':       211,
    'urquan':      211,
    'utwig':       211,
    'vux':         105,   # << HALF-WIDTH  <<<<<<<<<<<
    'yehat':       140,
    'yehatrebels': 140,
    'zoqfotpik':   112,
}

# Char width helper
def char_width(ch):
    o = ord(ch)
    if 0x4e00 <= o <= 0x9fff or 0x3400 <= o <= 0x4dbf:
        return None  # CJK — is a break point, doesn't participate in atomic word
    if o < 0x80:
        return 8   # ASCII 7px + 1px charspace
    return 15      # Fullwidth 14px + 1px charspace

def atomic_words_of_line(line):
    """Yield (text, width, start_index) for each atomic non-CJK non-space run.
    
    Note: Lua templates <% ... %> are replaced at runtime with CJK or short
    English tokens (star names, captain name, etc.). Treat them as break points
    for wrap analysis (equivalent to a single space) since they typically start
    and end with punctuation that gives the wrap engine break room.
    """
    # Replace Lua templates with a single space (acts as wrap break)
    line = re.sub(r'<%[^%]*%>', ' ', line)
    current = []
    start = 0
    for i, ch in enumerate(line):
        w = char_width(ch)
        if w is None or ch == ' ':
            if current:
                yield ''.join(current), sum(x for x in [char_width(c) for c in current] if x), start
                current = []
        else:
            if not current:
                start = i
            current.append(ch)
    if current:
        yield ''.join(current), sum(x for x in [char_width(c) for c in current] if x), start

def scan_all(root=Path(r'Q:\Dos_G\StarControl2\uqm-work\translations')):
    hits = []
    for jf in sorted(root.rglob('*.zh-TW.json')):
        stem = jf.stem.replace('.zh-TW', '')
        # lander/ subdirs — use hosting alien's width? Actually lander reports don't
        # use getLineWithinWidth (they use DoDiscoveryReport). Skip.
        if 'lander' in jf.parts:
            continue
        # skip *.v3 / *.merged etc.
        if any(x in jf.stem for x in ['.v3', '.v2', '.merged', '.partial', '.pre-']):
            continue
        text_width = ALIEN_WIDTH.get(stem, 211)  # default 211
        d = json.loads(jf.read_text(encoding='utf-8'))
        for key, val in d.items():
            if key.startswith('_') or not isinstance(val, str):
                continue
            for line_no, line in enumerate(val.split('\n'), 1):
                for word, width, start in atomic_words_of_line(line):
                    if width > text_width:
                        hits.append({
                            'file': jf.relative_to(root).as_posix(),
                            'alien': stem,
                            'text_width': text_width,
                            'key': key,
                            'line_no': line_no,
                            'atomic_word': word,
                            'width_est': width,
                            'overflow_by': width - text_width,
                            'text_full': line[:100],
                        })
    return hits

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--alien')
    ap.add_argument('--verbose', action='store_true')
    args = ap.parse_args()
    hits = scan_all()
    if args.alien:
        hits = [h for h in hits if h['alien'] == args.alien]
    hits.sort(key=lambda h: (-h['overflow_by'], h['file'], h['key']))
    print('=' * 78)
    print(f'Wrap-hostile scan v3 (empirical widths): {len(hits)} atomic words overflow')
    print('=' * 78)
    prev_alien = None
    for h in hits:
        if h['alien'] != prev_alien:
            print(f'\n--- {h["alien"]} (text_width={h["text_width"]}px) ---')
            prev_alien = h['alien']
        print(f'  [{h["key"]}] L{h["line_no"]}: word="{h["atomic_word"]}" width={h["width_est"]}px overflow={h["overflow_by"]}px')
        if args.verbose:
            print(f'    line: {h["text_full"]}')
    print('=' * 78)
    print(f'Total overflow atomic words: {len(hits)}')
    print('=' * 78)
    if args.strict and hits:
        sys.exit(1)

if __name__ == '__main__':
    main()
