from pathlib import Path
p = Path(r'Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\gamestrings.txt')
text = p.read_text(encoding='utf-8')
lines = text.split('\n')
# Find MAINMENU section
start_idx = -1
for i, line in enumerate(lines):
    if 'MAINMENU_STRING_BASE' in line:
        start_idx = i
        break
print(f'Start line: {start_idx}')
# Print until next STRING_BASE marker
end_idx = start_idx + 300
for i in range(start_idx + 1, min(len(lines), start_idx + 300)):
    if 'STRING_BASE' in lines[i] and i > start_idx + 5:
        end_idx = i
        break
print(f'End line: {end_idx}')
print(f'---BLOCK---')
for line in lines[start_idx:end_idx]:
    print(line)
