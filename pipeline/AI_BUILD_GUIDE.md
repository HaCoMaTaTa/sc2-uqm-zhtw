# AI 建置指引 (SC2 zh-TW 中文化打包流程)

> **給 AI 助手**：使用者要求做任何字型/翻譯/資源修改前，**必先讀完本文件**、確認目標（SD/HD/3DO）、依對應流程執行、驗證後才回報完成。

---

## 🎯 三大目標對應表（每次改前確認）

| 目標 | Addon 檔 | 主 Build Script | 主 Package Script | 遊戲載入條件 |
|---|---|---|---|---|
| **SD** (320×240) | `zh-TW.uqm` | `build_zh-TW.ps1` | `package_zh-TW.ps1` | 預設 |
| **HD** (1280×960) | `zh-TW-hd.uqm` (+ `zh-TW.uqm`) | `_build_hd_fonts.ps1` | `_package_hd_addon.ps1` | `--addon mm-hd --addon zh-TW --addon zh-TW-hd` |
| **3DO** (未來) | `zh-TW-3do.uqm` (TBD) | TBD | TBD | TBD |

**掛載順序 (低→高覆蓋)**：`base` → `mm-hd` → `zh-TW` → `zh-TW-hd`

> **關鍵**：HD 模式時 zh-TW-hd 覆蓋一切。SD 模式時只用 zh-TW。**改錯 addon 等於沒改**。

---

## ✅ 每次修改前必問三題

1. **這次改動要影響哪個模式？** SD? HD? 兩者? 3DO?
2. **改的是「字型 kerndat」還是「PNG glyph」還是「翻譯 .txt/.json」？** 決定要跑哪些 script
3. **使用者實際玩的是哪個模式？** 若使用者只玩 HD、卻只改 SD 檔 → 使用者看不出任何差別 (session 2026-08-13 學到的教訓)

若答不出來 → **問使用者**、不要臆測。

---

## 🔧 標準工作流

### 修改「翻譯內容」(.txt / .json)

僅改 SD (zh-TW.uqm) 就夠——因翻譯文字內容 HD 也吃 zh-TW.uqm 的 `shadow-content/base/...`

```powershell
# 1. 編輯 translations/<name>.zh-TW.json
# 2. 重新 build+package (SD)
cd Q:\Dos_G\StarControl2\uqm-work
.\package_zh-TW.ps1     # 會自動叫 build_zh-TW.ps1
# 3. 驗證: 檢查 install/content/addons/zh-TW.uqm 的 timestamp
Get-Item install\content\addons\zh-TW.uqm | Format-Table Length, LastWriteTime
```

### 修改「SD 字型」(kerndat / rasterize)

編輯 `build_zh-TW.ps1` 內 `$fontsToRasterize` 迴圈的 rasterize_font.py 參數，然後：
```powershell
.\package_zh-TW.ps1
```

### 修改「HD 字型」(kerndat / rasterize)

編輯 `_build_hd_fonts.ps1` 內 `$vertShift` / `$cjkScale` map 或加 rasterize_font.py 參數，然後：
```powershell
.\_build_hd_fonts.ps1        # 重建 _stage_hd_fonts/ (39 個 font, 約 3 分鐘)
.\_package_hd_addon.ps1      # 打包 zh-TW-hd.uqm (Compress-Archive 約 10 分鐘, 80 MB)
```
**注意**：`_package_hd_addon.ps1` 用 PowerShell `Compress-Archive`, 對 117k+ 檔案很慢, 等 5-10 分鐘正常。中間 file size 是 0 → 正常, 是暫存階段。

### 修改「字元池」(_used_chars.txt 沒某個字)

自 v0.7 起 `build_zh-TW.ps1` 的字元池自動掃 `zh-TW-addon/content/base/ui/setupmenu.txt`。若你**新增了不在既有翻譯的 CJK 字**，需重跑 `package_zh-TW.ps1` (含 build) 讓字元池同步。

若是 HD 缺字：跑 SD 的 package 先更新 `_used_chars.txt`，再跑 `_build_hd_fonts.ps1`。

---

## 📁 主要檔案的角色

| 檔案 | 角色 |
|---|---|
| `translate_ui.py` | JSON → txt 的轉譯器 (setupmenu, ipmenu, credits...) |
| `rasterize_font.py` | TTF → PNG glyph 產生器 (--cjk-scale, --vertalign-adjust 等) |
| `build_zh-TW.ps1` | SD 全流程 (翻譯 + 字型 rasterize) |
| `package_zh-TW.ps1` | SD 打包 zh-TW.uqm (預設自動叫 build) |
| `_build_hd_fonts.ps1` | HD 字型 rasterize 到 `_stage_hd_fonts/` |
| `_package_hd_addon.ps1` | 打包 `_stage_hd_fonts/` → zh-TW-hd.uqm |

---

## 📜 Lesson Learned (真實踩過的坑)

### L1: HD 用了 zh-TW-hd.uqm 覆蓋 SD, SD 字型改動對 HD 完全無效

**症狀**: 使用者截圖看不出改善。
**排查**: 檢查 `zh-TW-hd.uqm` 的 timestamp。若沒重建 → HD 沒生效。
**規避**: 改字型前先問「使用者玩什麼模式」。若是 HD → 改 `_build_hd_fonts.ps1`。
**日期**: 2026-08-13 (A1 pkunk clipping)。

### L2: 「shrink CJK」不是 top-clipping 的最佳解，「shift baseline」才是

**教訓**: `--cjk-scale 0.85` 縮字避免溢出，但字變小又難讀。改用 `--vertalign-adjust N` 直接下移全體 baseline，Latin + CJK 同步下移，不改字大小。
**用途**: HD 對話上緣頂到框 → 加 vertalign +10。
**副作用**: 底部行間可能擠。實測 pkunk +10 底部無明顯問題，但複雜字元 (descender) 需再測。
**日期**: 2026-08-13 (A1 pkunk clipping)。

### L3: 字元池 (_used_chars.txt) 沒掃到某檔 → 缺字型

**症狀**: 某些字在遊戲中顯示為空框、tofu、或 substitution glyph。
**原因**: `build_zh-TW.ps1` 的字元池掃描清單漏掉了某 `.txt` 檔。
**規避**: 新增翻譯檔到 `zh-TW-addon/content/` 時**同步加到 `build_zh-TW.ps1` 的字元池清單**（大約 L410-445）。
**日期**: 2026-08-13 (Setup Menu 中「弊/頁」等字缺, 因 `setupmenu.txt` 未加入字元池)。

### L4: 對 rasterize_font.py 加參數時要保持 backward-compat

**教訓**: `--vertalign-adjust` 用預設值 0 = no-op。舊呼叫端不加該參數也不會出錯。
**規避**: 新增功能永遠給預設值。

### L5: pkunk.fon 的 kerndat cell_h < PNG_h

**觀察**: pkunk.fon SD `pkunk.fon 11 1 1 6` → cell_h=11, PNG_h=14。行間會有 3 列重疊。這是 UQM 設計如此，不是 bug。VertAlign 調整不改 cell_h。
**副作用**: 若 VertAlign 太大 → 相鄰行的 PNG 底部可能覆蓋下行的頂部 (但因 CJK descender 通常空白, 實測不明顯)。

### L6: PowerShell `Compress-Archive -CompressionLevel Optimal` 對大量小檔極慢

**症狀**: `_package_hd_addon.ps1` 執行 5-10 分鐘。
**規避**: 這是 PowerShell 內建限制，可考慮換 7z (未來)。目前接受此耗時。
**日期**: 2026-08-13 (HD 重建, 117,466 entries)。

### L7: `git checkout <file>` 保留最近 committed 版本

**用途**: 想「取消所有未 commit 的改動」時，`git checkout <file>` 是最快方法。
**注意**: 不要對想保留的改動亂用。用 `git status` 先看。
**日期**: 2026-08-13 (A1 revert SD 改動)。

### L8: 主選單字大 = graphics 設 Original 拉伸 SD 內容，不是 bug

**症狀**: HD 模式主選單「新遊戲/讀取存檔」超大。
**原因**: 使用者把 Setup → Graphics 設為 Original (SD 320×240 拉伸至 1280×960, slab.fon 32×34 SD 拉成 128 HD 像素)。
**規避**: 使用者截圖回報「字太大」時，先問是否設定為 HD。
**日期**: 2026-08-13。

### L9: 詞彙表對照要以 `Master_Glossary.md` 為 canonical

**位置**: `Q:\Dos_G\StarControl2\StarControl2_TW_Localization\07_Glossary\Master_Glossary.md`。
**次要**: `Fixed_Terms.csv` 有較舊譯法，可能與 Master 衝突, **以 Master (v0.5.2 標記) 為準**。
**例子**: Hellbore Cannon = 火獄穿甲炮 (Master v0.5.2), 不是 地獄砲 (Fixed_Terms manual)。
**日期**: 2026-08-13 (Setup Menu B3 詞彙對齊)。

---

## 🚦 Deploy 驗證 checklist (打包後必查)

```powershell
# 1. addon 檔案 timestamp + 大小合理
Get-Item Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm, `
         Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW-hd.uqm |
    Format-Table Name, Length, LastWriteTime -AutoSize

# 2. 想確認裡面某個 kerndat 有沒有改到
& "C:\Program Files\7-Zip\7z.exe" e install\content\addons\zh-TW-hd.uqm `
    "zh-TW-hd/shadow-content/addons/mm-hd/fonts/pkunk.fon/kerndat.fnt" -so |
    Select-Object -First 1

# 3. 想確認翻譯有沒有生效
& "C:\Program Files\7-Zip\7z.exe" e install\content\addons\zh-TW.uqm `
    "zh-TW/shadow-content/base/gamestrings.txt" -so |
    Select-String -Pattern "某個中文字"
```

---

## 🚀 啟動遊戲

```powershell
# HD 模式 (使用者預設)
cd Q:\Dos_G\StarControl2\uqm-work\install
.\launch_hd.ps1

# SD 模式
.\UrQuanMasters-zip64.exe --windowed --addon zh-TW
```

**注意**: 必用 `UrQuanMasters-zip64.exe` (patched)，因 addon 常為 Zip64 格式（超過 65,535 檔案）。原始 `UrQuanMasters.exe` 不支援 Zip64，會 silently 忽略 addon，遊戲全變英文。

---

## 📞 若不確定要問使用者的問題模板

- 「這次改動想影響 SD, HD, 還是兩者都要？」
- 「目前你玩的是 HD 模式對嗎？（不是的話請告訴我）」
- 「這個字型調整是否只針對某一族對話？還是所有對話？」
- 「你希望改字大小 (--cjk-scale) 還是改位置 (--vertalign-adjust) ？」
