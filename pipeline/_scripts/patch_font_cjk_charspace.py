"""Apply zh-TW CharSpace-for-CJK patch to font.c.

For CJK Unicode codepoints (U+4E00-U+9FFF), the rasterized glyph PNGs already
have tight bbox padding (via `rasterize_font.py --extra-padding 0`). The
engine's per-char CharSpace add-on then produces visible gaps between Chinese
characters that hurt readability.

This script replaces every occurrence of:
    <var> += <char>->disp.width + FontPtr->CharSpace;
with:
    /* zh-TW patch: no CharSpace for CJK (glyph already padded) */
    <var> += <char>->disp.width;
    if (ch < 0x4E00 || ch > 0x9FFF)
        <var> += FontPtr->CharSpace;

Applied to all 4 sites in font.c: TextRect, _text_blt, TextRectAlt, _text_blt_alt.
The single _text_blt_fade "advance-past-space" loop is left alone -- it only
executes when the char is ASCII space, not CJK.
"""

import re
from pathlib import Path

path = Path(r"Q:\Dos_G\StarControl2\UQM-MegaMod\src\libs\graphics\font.c")
text = path.read_text(encoding="utf-8", errors="strict")

# Pattern matches:
#   [indent]<var> += <char>->disp.width + FontPtr->CharSpace;
# where <var> in {width, origin.x} and <char> in {charFrame, fontChar}.
# Captures indent so we preserve it in the replacement.
pat = re.compile(
    r"([ \t]+)(width|origin\.x) \+= (charFrame|fontChar)->disp\.width \+ FontPtr->CharSpace;",
)

def repl(m):
    indent, var, ch = m.group(1), m.group(2), m.group(3)
    return (
        f"{indent}/* zh-TW patch: skip CharSpace for CJK codepoints (PNG already padded) */\n"
        f"{indent}{var} += {ch}->disp.width;\n"
        f"{indent}if (ch < 0x4E00 || ch > 0x9FFF)\n"
        f"{indent}\t{var} += FontPtr->CharSpace;"
    )

new_text, n = pat.subn(repl, text)
print(f"Replaced {n} occurrences")
if n == 0:
    raise SystemExit("No matches found -- pattern may need updating")

path.write_text(new_text, encoding="utf-8")
print(f"Wrote {path}")

# Verify no remnants left
remaining = new_text.count("disp.width + FontPtr->CharSpace")
print(f"Remaining unpatched sites: {remaining}")
