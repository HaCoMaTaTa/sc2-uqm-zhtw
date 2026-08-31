import io, zipfile, re
from PIL import Image
z = zipfile.ZipFile(r'Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm')
p = 'zh-TW/shadow-content/base/fonts/commander.fon/'
def w(c): 
    try: return Image.open(io.BytesIO(z.read(f'{p}{ord(c):05x}.png'))).size[0]
    except: return 8

CS = 2
LIMIT = 143

problem_pages = [
    ('RADIOS_ON_MERCURY page 1', '...在地表搜刮 放射性元素礦床。...'),
    ('VERY_IMPRESSIVE page 6',   '...第一步很清楚 把你的 前驅族設備和軟體 搬過來...'),
    ('IT_WAS_ABANDONED page 1',  '...這麼多年 我方一直聽 他們胡言亂語的 廣播 竟從未 起疑。'),
    ('ABOUT_BASE_AGAIN page 2',  '...我方透過望遠鏡 觀察月球基地 確認 底下仍有 大量活動...'),
]
for name, page in problem_pages:
    print(f'==== {name} ====')
    for word in page.split(' '):
        total = sum(w(c) + CS for c in word) - (CS if word else 0)
        m = ' >>OVER<<' if total >= LIMIT else ''
        print(f'  ({total:3d}px){m}  {word!r}')
    print()
