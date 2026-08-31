"""Deep-verify the built addon before asking user to test."""
import zipfile
from pathlib import Path

zh = Path(r"Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm")
z = zipfile.ZipFile(zh)

# 1. Check commander.txt structure
print("=" * 60)
print("1. commander.txt structure check")
print("=" * 60)
with z.open("zh-TW/shadow-content/base/comm/commander/commander.txt") as f:
    data = f.read().decode("utf-8")
print(f"File size: {len(data.encode('utf-8'))} bytes")
lines = data.splitlines()
print(f"Total lines: {len(lines)}")

# Compare each TOKEN header format vs original
orig_path = Path(r"Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\comm\commander\commander.txt")
orig_data = orig_path.read_text(encoding="utf-8")
orig_lines = orig_data.splitlines()

import re
orig_headers = {ln.split(None, 1)[0]: ln for ln in orig_lines if ln.startswith("#(")}
new_headers  = {ln.split(None, 1)[0]: ln for ln in lines      if ln.startswith("#(")}

print(f"Original headers: {len(orig_headers)}")
print(f"New headers:      {len(new_headers)}")

diff_hdrs = 0
for tok, oh in orig_headers.items():
    if tok in new_headers:
        nh = new_headers[tok]
        if oh != nh:
            diff_hdrs += 1
            print(f"HEADER DIFF: {tok}")
            print(f"  orig: {oh!r}")
            print(f"  new : {nh!r}")
print(f"Header format changes: {diff_hdrs}")

# 2. Verify commander.fon has fixed kerndat name
print()
print("=" * 60)
print("2. commander.fon/kerndat.fnt name check")
print("=" * 60)
with z.open("zh-TW/shadow-content/base/fonts/commander.fon/kerndat.fnt") as f:
    kern = f.read().decode("ascii").splitlines()[0]
print(f"first line: {kern!r}")
if kern.startswith("commander.fon "):
    print("OK — starts with commander.fon")
else:
    print("BAD — first token does not match dir name")

# 3. Check Chinese content of translated tokens for anything suspicious
print()
print("=" * 60)
print("3. Suspicious content check")
print("=" * 60)
translated_toks = ["ARE_YOU_SUPPLY_SHIP", "THE_WHAT_FROM_WHERE", "MESSAGE_GARBLED_1",
                   "OK_THE_NAME_IS_EMPIRE", "FUEL_UP1"]

# Parse blocks
block_re = re.compile(r"^#\(([^)]+)\)")
blocks = {}
cur = None
buf = []
for ln in lines:
    m = block_re.match(ln)
    if m:
        if cur:
            blocks[cur] = buf
        cur = m.group(1)
        buf = [ln]
    else:
        buf.append(ln)
if cur:
    blocks[cur] = buf

for tok in translated_toks:
    if tok not in blocks:
        print(f"MISSING {tok}")
        continue
    block = blocks[tok]
    # Header + content until blank
    content = []
    for ln in block[1:]:
        if ln == "":
            break
        content.append(ln)
    max_len = max((len(x) for x in content), default=0)
    print(f"{tok}: {len(content)} lines, max {max_len} chars")
    if max_len > 60:
        print(f"  Long line: {content[0][:80]}")

z.close()
