"""Dump all CAT_*_OPT_*_DESC content from setupmenu.txt for reference."""
import re
from pathlib import Path

en = Path("extracted/base/base/ui/setupmenu.txt").read_text(encoding="utf-8", errors="replace")

# Parse into records: {id: [content_lines]}
records = {}
current_id = None
current_content = []
for line in en.splitlines():
    m = re.match(r"^#\(([^)]+)\)", line)
    if m:
        if current_id:
            # trim trailing blanks
            while current_content and current_content[-1] == "":
                current_content.pop()
            records.setdefault(current_id, []).append(current_content)
        current_id = m.group(1)
        current_content = []
    else:
        current_content.append(line)
if current_id:
    while current_content and current_content[-1] == "":
        current_content.pop()
    records.setdefault(current_id, []).append(current_content)

# Print key CATs
KEYS_TO_SHOW = [
    "CAT_53_OPTS", "CAT_53_OPT_0_DESC", "CAT_53_OPT_1_DESC", "CAT_53_OPT_2_DESC", "CAT_53_OPT_3_DESC",
    "CAT_54_OPTS", "CAT_54_OPT_0_DESC", "CAT_54_OPT_1_DESC",
    "CAT_59_OPTS", "CAT_59_OPT_0_DESC", "CAT_59_OPT_1_DESC", "CAT_59_OPT_2_DESC", "CAT_59_OPT_3_DESC",
    "CAT_63_OPTS", "CAT_63_OPT_0_DESC", "CAT_63_OPT_1_DESC", "CAT_63_OPT_2_DESC", "CAT_63_OPT_3_DESC",
    "CAT_67_OPTS", "CAT_67_OPT_0_DESC", "CAT_67_OPT_1_DESC",
    "CAT_70_OPTS", "CAT_70_OPT_0_DESC", "CAT_70_OPT_1_DESC",
    "CAT_72_OPTS", "CAT_72_OPT_0_DESC", "CAT_72_OPT_1_DESC",
    "CAT_81_OPTS", "CAT_81_OPT_0_DESC", "CAT_81_OPT_1_DESC", "CAT_81_OPT_2_DESC",
    "CAT_82_OPTS", "CAT_82_OPT_0_DESC", "CAT_82_OPT_1_DESC", "CAT_82_OPT_2_DESC", "CAT_82_OPT_3_DESC",
]

for k in KEYS_TO_SHOW:
    if k in records:
        for i, content in enumerate(records[k]):
            marker = f" [dup #{i+1}]" if len(records[k]) > 1 else ""
            print(f"#({k}){marker}")
            for l in content:
                print(f"  {l}")
            print()
    else:
        print(f"NOT FOUND: {k}")
        print()
