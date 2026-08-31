"""Print line counts per token for all 17 translated tokens (Hayes NPC dialog)."""
import re
from pathlib import Path

src = Path(r'Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt')
text = src.read_text(encoding='utf-8')

tokens = [
    "ARE_YOU_SUPPLY_SHIP", "THE_WHAT_FROM_WHERE", "ABOUT_TIME",
    "MESSAGE_GARBLED_1", "MESSAGE_GARBLED_2", "HERE_IS_A_NEW_LANDER",
    "THIS_MAY_SEEM_SILLY", "OK_THE_NAFS", "OK_THE_CAN", "OK_THE_UFW",
    "OK_THE_NAME_IS_EMPIRE", "FUEL_UP0", "FUEL_UP1",
    "WHAT_KIND_OF_IDIOT", "DONT_KNOW_WHO_YOU_ARE",
    "HAPPENED_TO_EARTH", "URQUAN_LEFT",
]

for tok in tokens:
    m = re.search(rf'#\({tok}\)[^\n]*\n((?:(?!#\().*?\n)*)', text)
    if not m:
        print(f'{tok}: NOT FOUND')
        continue
    body = m.group(1).rstrip()
    lines = [l for l in body.split('\n') if l.strip()]
    print(f'{tok}: {len(lines)} lines')
    for i, l in enumerate(lines):
        print(f'  [{i}] {l}')
    print()
