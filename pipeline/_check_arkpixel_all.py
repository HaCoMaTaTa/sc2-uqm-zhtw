"""Check which Ark Pixel variant has best Traditional Chinese coverage."""
from fontTools.ttLib import TTFont
from pathlib import Path

# Common menu characters
chars = '星圖清單遊戲航行存檔讀取離開設定返回貨物名冊礦能源生物自動掃描登陸新讀取設定攻擊燃料模組船員聲音音樂電腦閱速艦長旗艦'

variants = list(Path('_downloads/ark-pixel-10px').glob('*.ttf'))
results = []
for v in variants:
    tt = TTFont(v)
    cmap = tt.getBestCmap()
    missing = [ch for ch in chars if ord(ch) not in cmap]
    have = len(chars) - len(missing)
    results.append((v.name, len(cmap), have, len(chars), missing[:10]))
    tt.close()

results.sort(key=lambda x: -x[2])
print(f"{'Variant':<50} {'Total':>7} {'Menu':>7} Missing sample")
for name, total, have, need, missing in results:
    ms = ''.join(missing) if missing else '(none)'
    print(f"  {name:<48} {total:>7} {have:>3}/{need} {ms}")
