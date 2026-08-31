"""Test raw Fusion Pixel 10px at exactly 10px."""
from PIL import Image, ImageDraw, ImageFont

chars = '星圖清單遊戲航行存檔讀取離開設定返回貨物'
ttf = ImageFont.truetype('_downloads/fusion-pixel-10px/fusion-pixel-10px-proportional-zh_hant.ttf', 10)
imgs = []
for ch in chars:
    canvas = Image.new('L', (16, 16), 0)
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
combined.resize((tot_w * 10, tot_h * 10), Image.NEAREST).save('_raw_fusion10_tight.png')
print(f'saved _raw_fusion10_tight.png, sizes:')
for ch, im in imgs:
    print(f'  {ch}: {im.width}x{im.height}')
