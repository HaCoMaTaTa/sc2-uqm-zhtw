"""Extract star postfix table from gamestrings.txt (index 0..149)."""
from pathlib import Path
import re

content = Path("extracted/base/base/gamestrings.txt").read_text(encoding="utf-8", errors="replace")
lines = content.splitlines()

names = []
for line in lines[:1554]:  # STAR_NUMBER_BASE starts at L1554
    m = re.match(r'^#\(([^)]+)\)', line)
    if m:
        names.append(m.group(1))

for i, name in enumerate(names[:160]):
    print(f"  {i} = {name}")
