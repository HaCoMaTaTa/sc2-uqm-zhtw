"""Compare raw Fusion Pixel 12px vs Cubic 11 rendering."""
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

def check_coverage(ttf_path, chars):
    tt = TTFont(ttf_path)
    cmap = tt.getBestCmap()
    missing = [ch for ch in chars if ord(ch) not in cmap]
    tt.close()
    return len(chars) - len(missing), len(chars), missing

chars = '星圖清單遊戲航行存檔讀取離開設定返回貨物名冊礦能源生物自動掃描登陸攻擊燃料模組船員聲音音樂電腦閱速艦長旗艦'
fusion = '_downloads/fusion-pixel-12px/fusion-pixel-12px-proportional-zh_hant.ttf'
have, need, missing = check_coverage(fusion, chars)
print(f'Fusion Pixel 12px zh_hant: {have}/{need}, missing: {"".join(missing)}')

# Render sample
test_chars = '星圖清單遊戲航行存檔讀取離開設定返回'
ttf = ImageFont.truetype(fusion, 12)
imgs = []
for ch in test_chars:
    canvas = Image.new('L', (20, 20), 0)
    ImageDraw.Draw(canvas).text((2, 2), ch, fill=255, font=ttf, anchor='lt')
    bbox = canvas.getbbox()
    imgs.append((ch, canvas.crop(bbox) if bbox else canvas))

tot_w = sum(im.width for _, im in imgs) + len(imgs) * 4
tot_h = max(im.height for _, im in imgs)
combined = Image.new('L', (tot_w, tot_h), 0)
x = 0
for ch, im in imgs:
    combined.paste(im, (x, 0))
    x += im.width + 4
combined.resize((tot_w * 10, tot_h * 10), Image.NEAREST).save('_raw_fusion12_tight.png')
print('saved _raw_fusion12_tight.png')
print('sizes:', ', '.join([f'{c}:{i.width}x{i.height}' for c, i in imgs]))
