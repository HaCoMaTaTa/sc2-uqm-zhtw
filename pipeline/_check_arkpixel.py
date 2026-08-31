from fontTools.ttLib import TTFont
tt = TTFont('_downloads/ark-pixel-10px/ark-pixel-10px-proportional-zh_tw.ttf')
cmap = tt.getBestCmap()
chars = '星圖清單遊戲航行存檔讀取離開設定返回'
print(f'Total glyphs in font: {len(cmap)}')
for ch in chars:
    cp = ord(ch)
    has = cp in cmap
    print(f'  U+{cp:04X} {ch}: {"yes" if has else "MISSING"}')
tt.close()
