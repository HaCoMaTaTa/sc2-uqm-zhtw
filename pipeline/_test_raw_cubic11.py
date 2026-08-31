"""Test raw Cubic 11 rendering to diagnose distortion issue."""
from PIL import Image, ImageDraw, ImageFont

chars = '星圖清單遊戲航行存檔讀取離開設定返回'
ttf = ImageFont.truetype('_downloads/Cubic_11.ttf', 11)

# Method 1: render each char at natural size, pack side by side
imgs = []
for ch in chars:
    canvas = Image.new('L', (20, 20), 0)
    ImageDraw.Draw(canvas).text((2, 2), ch, fill=255, font=ttf, anchor='lt')
    bbox = canvas.getbbox()
    if bbox:
        cropped = canvas.crop(bbox)
        imgs.append((ch, cropped, canvas))
    else:
        imgs.append((ch, canvas, canvas))

# Show both: cropped tight and full canvas
tot_w = sum(im.width for _, im, _ in imgs) + len(imgs) * 4
tot_h = max(im.height for _, im, _ in imgs)
combined = Image.new('L', (tot_w, tot_h), 0)
x = 0
for ch, im, _ in imgs:
    combined.paste(im, (x, 0))
    x += im.width + 4
combined.resize((tot_w * 10, tot_h * 10), Image.NEAREST).save('_raw_cubic11_tight.png')

# Full canvas (uncropped) shows baseline positioning
full_w = 20 * len(imgs) + len(imgs) * 4
full_combined = Image.new('L', (full_w, 20), 0)
x = 0
for ch, _, full in imgs:
    full_combined.paste(full, (x, 0))
    x += full.width + 4
full_combined.resize((full_w * 10, 200), Image.NEAREST).save('_raw_cubic11_full.png')
print('saved _raw_cubic11_tight.png and _raw_cubic11_full.png')
print('char sizes:', ', '.join([f'{ch}:{im.width}x{im.height}' for ch, im, _ in imgs]))
