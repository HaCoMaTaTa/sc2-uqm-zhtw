"""Locate CAT_*_OPT_*_DESC IDs for visible untranslated descriptions."""
import re
from pathlib import Path

en = Path("extracted/base/base/ui/setupmenu.txt").read_text(encoding="utf-8", errors="replace")
lines = en.splitlines()

def find_section(pattern: str) -> None:
    for i, line in enumerate(lines):
        if pattern in line:
            # find nearest #(SECTION) above
            for j in range(i, -1, -1):
                m = re.match(r"^#\(([^)]+)\)", lines[j])
                if m:
                    print(f"  L{i+1} '{line}' -> section {m.group(1)}")
                    break
            return
    print(f"  Not found: {pattern}")

print("Untranslated descriptions from screenshots:")
find_section("Extended Lore that expands")
find_section("Death March starts 100 years")
find_section("The default UQM presentation")
find_section("resemble the default UQM style")
find_section("Kohr-Ah Death March")
find_section("Vanilla difficulty as it was originally intended")
find_section("Various changes to make UQM gameplay easier")
find_section("Various changes to make UQM gameplay harder")
find_section("You will be prompted at the start")
