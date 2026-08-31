"""Analyze which CAT_*_OPT_*_DESC entries have non-empty content in the English source."""
import re
from pathlib import Path

en = Path("extracted/base/base/ui/setupmenu.txt").read_text(encoding="utf-8", errors="replace")
lines = en.splitlines()

# Parse into records
records = {}
current_id = None
current_content = []
for line in lines:
    m = re.match(r"^#\(([^)]+)\)", line)
    if m:
        if current_id:
            while current_content and current_content[-1] == "":
                current_content.pop()
            records[current_id] = current_content
        current_id = m.group(1)
        current_content = []
    else:
        current_content.append(line)
if current_id:
    while current_content and current_content[-1] == "":
        current_content.pop()
    records[current_id] = current_content

# Filter DESC entries
desc_re = re.compile(r"^CAT_(\d+)_OPT_(\d+)_DESC$")
non_empty_descs = []
empty_descs = []
for key, content in records.items():
    m = desc_re.match(key)
    if m:
        if content and any(l.strip() for l in content):
            non_empty_descs.append((int(m.group(1)), int(m.group(2)), key, content))
        else:
            empty_descs.append(key)

print(f"Total CAT_*_OPT_*_DESC records: {sum(1 for k in records if desc_re.match(k))}")
print(f"  Non-empty (need translation): {len(non_empty_descs)}")
print(f"  Empty (skip): {len(empty_descs)}")

# Group by CAT
from collections import defaultdict
cat_groups = defaultdict(list)
for cat_n, opt_n, key, content in non_empty_descs:
    cat_groups[cat_n].append((opt_n, key, content))

# Filter to only NOT already translated
import json
data = json.loads(Path("translations/setupmenu.zh-TW.json").read_text(encoding="utf-8"))
already_done = {k for k in data if desc_re.match(k)}

untranslated = []
for cat_n in sorted(cat_groups):
    for opt_n, key, content in cat_groups[cat_n]:
        if key not in already_done:
            untranslated.append((cat_n, opt_n, key, content))

print(f"\n=== UNTRANSLATED non-empty DESCs: {len(untranslated)} ===")
print(f"Covering {len(set(u[0] for u in untranslated))} unique CATs\n")

for cat_n, opt_n, key, content in untranslated:
    print(f"--- {key} ---")
    for line in content:
        print(f"  {line}")
    print()
