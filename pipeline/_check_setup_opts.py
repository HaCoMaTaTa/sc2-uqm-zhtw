from pathlib import Path
p = Path(r'Q:/Dos_G/StarControl2/uqm-work/_megamod_content_085/UQM-MegaMod-Content-0.8.5/base/ui/setupmenu.txt')
lines = p.read_text(encoding='utf-8').splitlines()
targets = ['Lander View Style', 'Font Style', 'Display Mode', 'Scanning Style', 'Alternate Orz Font']
for i, ln in enumerate(lines):
    if any(t == ln.strip() for t in targets):
        print(f"L{i+1}: {ln}")
        for j in range(i+1, min(i+10, len(lines))):
            print(f"     {lines[j]}")
        print()
