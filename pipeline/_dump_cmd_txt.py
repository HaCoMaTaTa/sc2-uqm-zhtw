import zipfile
z = zipfile.ZipFile(r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm')
for n in z.namelist():
    if n.endswith('commander/commander.txt'):
        data = z.read(n)
        with open(r'Q:\Dos_G\StarControl2\uqm-work\_cmd_current.txt', 'wb') as f:
            f.write(data)
        print(f'Wrote {len(data)} bytes to _cmd_current.txt')
        break
