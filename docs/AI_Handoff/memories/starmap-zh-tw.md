# Starmap.zh-TW 建置流程

## 檔案位置
- 原圖：`StarControl2_TW_Localization/Reference_Material/Starmap.png` (3200×4258，社群美術重製版)
- **v3 Perl 向量版**（推薦）：
  - `Starmap.zh-TW.perl.pdf` (1.45 MB, 向量可縮放)
  - `Starmap.zh-TW.perl.png` (1.70 MB, 3300×2550 @ 300 DPI)
  - 建置：`uqm-work/_uqmmap/zh_workspace/map_zh.pl`（Alan De Smet Perl 修改版）
- v2 純像素版（保留參考）：`Starmap.zh-TW.png` (6.72 MB, 3200×4258)
- v1 SVG 疊層版（保留參考）：`Starmap.zh-TW.svg` (3.19 MB)

## v3 Perl 建置關鍵
- 來源：`http://www.highprogrammer.com/alan/games/video/uqm/uqmmap.zip`（HTTP 版活著，HTTPS 404）
- 需 Strawberry Perl 5.42 + `cpanm PDF::API2`（含 Font::TTF、Devel::Cycle 依賴）
- PDF::API2 不吃 TTC 檔或 Variable Font — 需用 fonttools 從 `msjhbd.ttc` 抽出單一 face TTF
- 中文化流程：Python 產生 `map_zh.pl`（inject 翻譯表 + zh() helper + 換 TTF 字型）
- `starcon.txt` 不動、`plandata.c` 不動，只改 map.pl 邏輯
- 執行：`perl map_zh.pl --spheres=modern --spoilers -o starmap_zh.pdf`
- 光柵化：PyMuPDF `fitz.get_pixmap(dpi=300)`


## v2 關鍵技術教訓
- **max(B,G,R) > 50** 抓文字像素，不是 grayscale threshold — 純藍 (255,0,0) 灰度只有 29，會漏抓
- **cv2.INPAINT_TELEA/NS 對同色鄰居會回填相同顏色** — 種族圈曲線英文與圈環同色，inpaint 會抹不掉。改用 "sample 背景色直接填 mask"
- 直接填黑會斷圓環 → **Pillow 後續用 SPHERE_CIRCLES 手動重畫圓環**
- SPHERE_ERASE_ZONES 要**同時包含曲線標籤的上下曲線區域**（曲線英文可從圓的一側繞到另一側），單一 top-only rect 不夠
- OCR bbox 尾部字母易漏 → padding 從 6→14→24 pixel


## 工具鏈
- Tesseract 5.5.3：`C:\Program Files\Tesseract-OCR\tesseract.exe`（winget: `tesseract-ocr.tesseract`）
- ImageMagick 7.1.2 (SVG delegate: rsvg-convert)：`C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe`
- Python: pytesseract 0.3.13, Pillow 12, OpenCV 4.10, svglib+reportlab（備援，缺 CJK）

## 關鍵坑
- svglib 光柵化不吃 CJK font-family 疊層 → 用 ImageMagick + rsvg 才對
- SVG 用 `font-family="Microsoft JhengHei"`（單一名，非 fallback list）
- 背景 PNG 必須 base64 內嵌（`xlink:href="data:image/png;base64,..."`），rsvg 不會讀相對路徑 href
- OCR PSM 11 (sparse) 對 ~230 星座/星名 OK，但曲線種族圈標籤 (THRADDASH/UMGAH/etc.) 幾乎全 miss → 手動座標
- Multipass OCR (thresh100/thresh70/blue-channel/adaptive × PSM 11/6/12 = 12 pass + dedup) 找回 ~130 個原 raw pass 漏掉的
- OCR 常見截字：Librae→ibrae, Lacertae→Lacerta, Crateris→Crate, Almagest→mages, Illuminati→Huminati — 皆進 OCR_FIXES 表

## Grid → Pixel 換算
- x_pixel = 101 + 2.94 * x_map_grid
- y_pixel = 3057 - 2.94 * y_map_grid（Y 反向）

## 種族圈中心像素座標（實測）
UMGAH=(678,1052) MYCON=(1913,2036) — 以 OCR bbox 中心為錨
其他種族圈手動測量：見 SPHERE_ANCHORS in `_build_starmap_zhTW.py`

## 32-item Legend Layout
原圖 3 欄：Col1 items 1-11 x=100 / Col2 items 12-22 x=670 / Col3 items 23-32 x=1240
+ 特殊 bullet items：彩虹星球位置 / 準空間傳送門出口（用 M/F 圓 icon）
+ 星系希臘字母命名（右上）
+ 準空間地圖說明（右下）

## 保留原文
- Star Control II — The Ur-Quan Masters logo（美術資產）
- 希臘字母 α β γ 等
- 格線數字 100..900
