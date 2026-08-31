"""Deep inspection: every translated entry for suspicious bytes."""
import re
from pathlib import Path

new_path = Path(r"Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\comm\commander\commander.txt")
orig_path = Path(r"Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt")

new_data = new_path.read_bytes()
orig_data = orig_path.read_bytes()

# Parse blocks from each file
BLOCK_RE = re.compile(rb"^#\(([^)]+)\)", re.MULTILINE)

def parse_blocks(data):
    blocks = {}
    positions = [(m.start(), m.group(1).decode()) for m in BLOCK_RE.finditer(data)]
    for i, (pos, tok) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(data)
        blocks[tok] = data[pos:end]
    return blocks

orig_blocks = parse_blocks(orig_data)
new_blocks = parse_blocks(new_data)

# Identify tokens that changed (i.e., were translated)
changed = []
for tok, ob in orig_blocks.items():
    if tok in new_blocks and new_blocks[tok] != ob:
        changed.append(tok)

print(f"Changed tokens: {len(changed)}")
print()

for tok in changed:
    ob = orig_blocks[tok]
    nb = new_blocks[tok]
    ol = ob.rstrip(b"\n").split(b"\n")
    nl = nb.rstrip(b"\n").split(b"\n")
    print(f"===== {tok} =====")
    print(f"  orig lines: {len(ol)}   new lines: {len(nl)}")
    if len(ol) != len(nl):
        print(f"  !!! LINE COUNT MISMATCH")
    for i, line in enumerate(nl):
        b = len(line)
        # check for suspicious bytes
        weird = []
        if b > 200:
            weird.append(f"len={b}")
        if b"\x00" in line:
            weird.append("NULL byte")
        if b"\r" in line:
            weird.append("CR byte")
        # ensure template braces balance
        opens = line.count(b"<%")
        closes = line.count(b"%>")
        if opens != closes:
            weird.append(f"template braces {opens}!={closes}")
        # check for very high non-BMP characters
        try:
            s = line.decode("utf-8")
            for ch in s:
                cp = ord(ch)
                if cp > 0xFFFF:
                    weird.append(f"non-BMP U+{cp:X}")
                    break
        except UnicodeDecodeError as e:
            weird.append(f"BAD UTF-8: {e}")
        marker = " [WEIRD: " + ", ".join(weird) + "]" if weird else ""
        try:
            preview = line.decode("utf-8")[:60]
        except:
            preview = repr(line[:60])
        print(f"  [{i}] {b:>4}b: {preview}{marker}")
    print()
