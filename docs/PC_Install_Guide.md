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
- <https://github.com/HaCoMaTaTa/sc2-uqm-zhtw/releases/latest>
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
   - **建議避開** `C:\Program Files\` 與 OneDrive 同步資料夾（權限與同步衝突）
   - 解壓後你會看到：
     - `UrQuanMasters-zip64.exe` ← 主程式
     - **`Play_HD.bat`** ← ⭐ **推薦：雙擊即玩**（HD 全螢幕）
     - `Play_HD_windows.bat` ← HD 視窗模式
     - `Setup.bat` ← 進 in-game 設定選單
     - `快速開始.txt`、`README.md`、`content/`、`LICENSES/` 等
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

### 6.1 一鍵啟動 · **雙擊 batch 檔即玩**

Zip 內已內建啟動 batch，**不用打任何命令列**、**不用手動改 config**、**不用手動勾 addon**——直接雙擊就跑：

| Batch 檔 | 模式 | 解析度 | 適用 |
|---|---|---|---|
| ⭐ **`Play_HD.bat`** | **HD 全螢幕** | 1280×960 | **推薦 · 現代 PC** |
| `Play_HD_windows.bat` | HD 視窗 | 1280×960 | 雙螢幕 · 常 alt-tab · 邊玩邊查資料 |
| `Setup.bat` | 進 in-game Setup | — | 改音量／鍵配／addon／難度 |

> ℹ️ **本版 release 只驗證並推薦 HD 模式**（zh-TW-hd 字型 + mm-hd 圖像）。Zip 內雖含 `Play_SD.bat`，但 SD 模式尚未完成完整驗證，**不建議使用**。

**這些 batch 做了什麼**（給進階讀者）：

- **智慧更新** `%APPDATA%\uqm-megamod\uqm.cfg` 內的 graphics keys（resolutionfactor / reswidth / resheight / fullscreen / alwaysgl）
- **保留** 使用者其他設定（音量／鍵配／cheat／已勾 addon）——切換全螢幕 ↔ 視窗 **不會弄丟你的個人化設定**
- 自動附帶正確的 `--addon` 參數：`--addon mm-hd --addon zh-TW --addon zh-TW-hd`

> 💡 **首次執行**：Windows Defender SmartScreen 可能會擋——「更多資訊」→「仍要執行」即可。詳見上一節「五、Windows Defender / 防毒警告」。

### 6.2 進階：命令列啟動

若你要自訂啟動參數（例如自訂解析度或 configdir）：

**HD 模式全螢幕**（`fullscreen=2` 是 exclusive fullscreen）：
```powershell
.\UrQuanMasters-zip64.exe --fullscreen=2 --res=1280x960 --opengl --scale=none --cscan=2 --addon mm-hd --addon zh-TW --addon zh-TW-hd
```

**HD 視窗模式**：
```powershell
.\UrQuanMasters-zip64.exe --fullscreen=0 --res=1280x960 --opengl --scale=none --cscan=2 --addon mm-hd --addon zh-TW --addon zh-TW-hd
```

**注意**：手打命令列會**跳過**智慧更新 `uqm.cfg` 的步驟——如果你之前有跑過 Play_HD.bat，config 內的 graphics keys 已被鎖成該模式。下次改用 batch 時會被覆寫，這是預期行為。

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

Windows 預設（MegaMod fork）：
```
%APPDATA%\uqm-megamod\
├── uqm.cfg          ← 遊戲設定（graphics/音量/鍵配/addon）
└── save\            ← 存檔（.mgs / .mgc 檔）
```

> ⚠️ **注意**：本 release 基於 **UQM MegaMod fork**，存檔路徑是 `uqm-megamod\`（不是原版 UQM 的 `uqm\`）。從原版 UQM 遷移過來的存檔需手動搬到 `uqm-megamod\save\`。

**HD / 視窗 存檔通用**：切換 `Play_HD.bat` ↔ `Play_HD_windows.bat` **不會**遺失或分離存檔——兩者使用同一個 save 資料夾。

**可攜式存檔**（存檔跟遊戲一起搬）：加參數 `--configdir .\config`——若要走 batch 又想可攜式，可自製一個 `Play_Portable.bat` 複製 `Play_HD.bat` 內容並在最後那行加 `--configdir .\config`。

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
- 檢查 `%APPDATA%\uqm-megamod\save\` 是否有 `.mgs` 檔
- 若你有加 `--configdir` → 存檔在該路徑
- 若從原版 UQM 遷移：存檔可能在 `%APPDATA%\uqm\save\`（要手動搬到 `%APPDATA%\uqm-megamod\save\`）

## 十二、移除

因為是綠色版，直接刪除 `C:\Games\SC2-zhTW\` 資料夾即可。存檔在 `%APPDATA%\uqm-megamod\`（若你想留就別刪）。

## 十三、資源與支援

- **GitHub Issues**：<https://github.com/HaCoMaTaTa/sc2-uqm-zhtw/issues>
- **翻譯錯誤回報**：附上 tag/場景 + 建議中譯
- **技術 bug**：附上 `game.log` 最後 100 行

## 十四、致謝與授權

見 [../NOTICE](../NOTICE) 與 [../LICENSE.CONTENT](../LICENSE.CONTENT)。
