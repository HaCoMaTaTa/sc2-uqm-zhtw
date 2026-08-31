# Starmap.zh-TW — 中文版星圖

**Source**: `Starmap.png` (原始英文版, 3200 × 4258)
**Output**: `Starmap.zh-TW.png` (v2 純像素重繪版) + `Starmap.zh-TW.svg` (v1 SVG 疊層版)

## 檔案

| 檔案 | 說明 |
|---|---|
| `Starmap.png` | 原始英文版星圖（美術資產） |
| **`Starmap.zh-TW.png`** | **v2 純像素版**：OpenCV inpaint + Pillow 直接改像素，無黑框、圈環完整 |
| `Starmap.zh-TW.svg` | v1 SVG 疊層版（保留作參考） |

## v2 建置流程（推薦）

```powershell
Set-Location Q:\Dos_G\StarControl2\uqm-work
$env:PYTHONIOENCODING='utf-8'

# 首次或重掃 OCR 才需要
python _starmap_ocr_test.py           # → _starmap_out/_ocr_raw.json
python _starmap_ocr_multipass.py      # → _ocr_multipass.json（12 pass 合併）

# 生成中文 PNG（單一命令，直接輸出到 Reference_Material）
python _starmap_v2.py
```

## v2 技術重點

1. **文字偵測**：OpenCV `max(B,G,R) > 50` 抓所有彩色像素（純藍 PKUNK 灰度僅 29，需用 max 通道才抓得到）
2. **文字擦除**：sample 星圖背景色（深藍/黑）直接填 mask 位置 — 避免同色圓環 inpaint 回填
3. **圓環還原**：Pillow 依 `SPHERE_CIRCLES` 手動指定圓心+半徑+顏色重畫種族圈邊框
4. **中文渲染**：Pillow + `NotoSansTC-VF.ttf` 直接繪製，含黑色 outline 提升可讀性
5. **Legend 重繪**：整個底部 Legend 區域清空後以 Pillow 從頭重畫（32 條 + 顏色分類 + 希臘字母 + QuasiSpace 說明）

## 內容範圍

- **~155 星座/恆星** 中文替換（拉丁屬格 → ROC 天文學會譯名；SC2 原創 → 音譯）
- **16 種族影響圈** 中文族名替換 + 圈環用 Pillow 重畫
- **完整 Legend 重繪**：32 條 numbered items（3 欄）+ 彩虹/準空間 bullet + 顏色分類 + 星系希臘字母 + 準空間地圖說明
- **保留原文**：`Star Control II — The Ur-Quan Masters` logo、希臘字母 `α β γ...`、格線數字、QuasiSpace 傳送門字母

## 已知小殘留

以下極少量位置有 anti-alias 邊緣殘留（不影響閱讀）：
- `Columbae` 尾巴 `pae`（天鴿座旁）
- `Crateris` 尾巴 `s`（巨爵座旁）
- `Squidi` 前 `Sq`（斯奎第旁）
- 半人馬座旁 `|` 殘留
- 準空間小地圖標題保留 `QuasiSpace Map` 英文（與內部字母標記一致）

若需精修，可調整 `SPHERE_ERASE_ZONES` 位置或加大 OCR `pad_x/pad_y` 於 `_starmap_v2.py`。

## 譯名權威來源

依 `../07_Glossary/Master_Glossary.md` v0.8、`../07_Glossary/Race_Names.md`、`../07_Glossary/Place_Names.md`、`../06_Locations/Star_Systems.md` 之鎖定譯名。
