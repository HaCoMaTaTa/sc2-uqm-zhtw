import io, zipfile
from PIL import Image
z = zipfile.ZipFile(r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm')
p = 'zh-TW/shadow-content/base/fonts/commander.fon/'
def w(c): 
    try: return Image.open(io.BytesIO(z.read(f'{p}{ord(c):05x}.png'))).size[0]
    except: return None

# Test all 4 pages of RADIOS_ON_MERCURY with SplitSubPages ellipsis
pages = [
    '在這系統 拿放射性物質 最快的方法 就是登陸水星...',
    '...在地表搜刮 放射性元素礦床。...',
    '...但要小心。 水星環境 相當險惡！...',
    '...留意地震 還有那些 高溫區！',
]
CS = 2
LIMIT = 143
print(f'Limit: {LIMIT}px, CharSpace={CS}')
for pi, page in enumerate(pages):
    print()
    print(f'== Page {pi}: {page!r} ==')
    for word in page.split(' '):
        total = 0
        details = []
        for c in word:
            cw = w(c) or 8
            details.append(f'{c}({cw})')
            total += cw + CS
        if total > 0: total -= CS
        marker = ' !!!!' if total >= LIMIT else ''
        joined = ' '.join(details)
        print(f'  word ({total:3d}px){marker}: {joined}')
