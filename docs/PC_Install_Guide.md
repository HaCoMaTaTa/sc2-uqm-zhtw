# PC 版安裝與操作說明

> 適用：Windows 7 / 8.1 / 10 / 11 · 64-bit 均可（安裝包內建 32-bit exe，因原 UQM 引擎為 i386）

---

## 一、系統需求

| 項目 | 最低 | 建議 |
|---|---|---|
| 作業系統 | Windows 7 SP1 | Windows 10/11 |
| CPU | 任何雙核 x86 | Intel/AMD 現代 CPU |
| RAM | 512 MB 空閒 | 2 GB |
| 硬碟 | 400 MB 空閒 | 1 GB（含存檔）|
| 顯卡 | OpenGL 2.0 | OpenGL 3.0+ |
| 螢幕 | 1024×768 | 1280×960 (HD 模式) |

## 二、下載

前往 GitHub Release 頁面：
- <https://github.com/HaCoMaTaTa/uqm-megamod-zhTW/releases/latest>
- 下載 `SC2-zhTW-v1.0.13.zip`（或最新版）
- 下載 `SC2-zhTW-v1.0.13.zip.sha256`（用來驗證檔案完整性）

## 三、驗證 SHA256

```powershell
# PowerShell
Get-FileHash SC2-zhTW-v1.0.13.zip -Algorithm SHA256
# 對照 SC2-zhTW-v1.0.13.zip.sha256 檔內的 hash 值
```

## 四、安裝

1. **解壓** `SC2-zhTW-v1.0.13.zip` 到你想要的位置（例：`C:\Games\SC2-zhTW\`）
   - 解壓後應該看到 `UrQuanMasters-zip64.exe`、`SDL2.dll`、`content/` 等
2. **無需執行 installer** — 這是綠色版
3. **無需 admin 權限**

## 五、Windows Defender / 防毒警告

因為 exe 沒有購買 Authenticode 商業簽章，Windows Defender SmartScreen 可能會擋：

**方法 1**：右鍵 → 內容 → 一般 → 底部「解除封鎖」→ 套用

**方法 2**：SmartScreen 彈窗時 → 「其他資訊」→ 「仍要執行」

**方法 3**：加入 Windows Defender 白名單：
```powershell
Add-MpPreference -ExclusionPath 'C:\Games\SC2-zhTW\'
```

**安全性**：所有 exe 已通過 VirusTotal 掃描，報告連結見 [Security_Scan_Report.md](Security_Scan_Report.md)。

## 六、啟動

**主啟動**：雙擊 `UrQuanMasters-zip64.exe`

**建議命令列參數**（若你想直接進中文）：
```powershell
.\UrQuanMasters-zip64.exe --windowed --addon zh-TW
```

**HD 模式**（需要下載額外 HD 資產）：
```powershell
.\UrQuanMasters-zip64.exe --windowed --addon mm-hd --addon zh-TW --addon zh-TW-hd --resfactor 2
```

## 七、操作說明

### 主選單
- **↑↓** 移動選項
- **Enter** 確認
- **Esc** 返回上一層

### 星圖 / 太陽系
- **方向鍵** 移動游標
- **Enter** 選取星系
- **F6** 星圖搜尋（可打中文別名，patch 031 支援）
- **F7** HyperSpace / QuasiSpace 星圖切換
- **PageUp / PageDown** 星圖縮放

### 對話
- **Enter / Space** 下一頁
- **↑↓** 選擇玩家回應
- **Esc** 中斷對話（有時可用）

### 戰鬥（Super Melee）
- **方向鍵** 旋轉船 / 加速
- **Enter** 主武器
- **Right Shift** 特殊武器
- **Esc** 暫停 / 退出

### 快速鍵
| 鍵 | 功能 |
|---|---|
| F1 | 暫停 |
| F3 | 快速存檔 |
| F4 | 快速讀檔 |
| F5 | 除錯 |
| F6 | 星圖搜尋 |
| F7 | 星圖切換 |
| F8 | 螢幕截圖 |
| F10 | 離開 |
| F11 | 全螢幕切換 |

## 八、存檔位置

Windows 預設：
```
%APPDATA%\uqm\
```

若想使用可攜式存檔，加參數 `--configdir .\config`。

## 九、中文化涵蓋範圍

| 畫面 | 涵蓋 |
|---|---|
| 主選單 | ✅ |
| 對話（NPC + 玩家）| ✅ 26 族已 Level 3 audit |
| Setup 選單 | ✅ |
| 星圖標籤 | ✅ |
| 星系名（首介英+中）| ✅ patch 009/011 |
| 星系別名搜尋（F6）| ✅ patch 031 |
| 種族 SoI 標籤 | ✅ patch 010 |
| 存讀檔 | ✅（存檔位置說明為英文）|
| 戰鬥模組名 | ✅ |
| Lander 掃描報告 | ✅ patch 008 修 hang |
| 太空站 UI | ✅ |
| Intro 動畫字幕 | ✅ |
| 片尾字幕 | ✅ |
| Kzer-Za 主線（74 tokens）| ❌ 待另案 |

## 十、已知問題

- **Zip64 addon**：必須用 `UrQuanMasters-zip64.exe`（原版 exe 不支援 Zip64 · 會 log 顯示英文）
- **HD 模式資產另下**：`zh-TW-hd.uqm` 未內建於本 zip · 走 Releases 額外附件下載
- **首次啟動 game.log 有 warning**：字型預熱期，遊戲正常運作可忽略
- **主選單「Setup」項目位置**：若你的 mm-pc.cfg 內 optWhichMenu 不同會有微差

## 十一、疑難排解

### 遊戲全英文
- 檢查 `.\content\addons\zh-TW.uqm` 存在
- 執行時加 `--addon zh-TW --logfile game.log`，查 `game.log` 找「addon packs」訊息

### 對話 crash 回主選單
- 檢查是否用 `-zip64.exe` 版
- 檢查 `game.log` 有無「Warning: Invalid UTF8 sequence」爆量 → 可能字型 CharSpace 設定錯

### 星圖無法搜尋中文
- 需要 patch 031（已內建於本 release）
- 若還是不行，開 game.log 查 STAR SEARCH 訊息

### 存檔遺失
- 檢查 `%APPDATA%\uqm\` 是否有 `.mgs` 檔
- 若你有加 `--configdir` → 存檔在該路徑

## 十二、移除

因為是綠色版，直接刪除 `C:\Games\SC2-zhTW\` 資料夾即可。存檔在 `%APPDATA%\uqm\`（若你想留就別刪）。

## 十三、資源與支援

- **GitHub Issues**：<https://github.com/HaCoMaTaTa/uqm-megamod-zhTW/issues>
- **翻譯錯誤回報**：附上 tag/場景 + 建議中譯
- **技術 bug**：附上 `game.log` 最後 100 行

## 十四、致謝與授權

見 [../NOTICE](../NOTICE) 與 [../LICENSE.CONTENT](../LICENSE.CONTENT)。
