# Android 版安裝與操作說明

> 版本：v3.8（2026-08-31 release）
> 適用：Android 7.0（API 24）以上、arm64-v8a 或 x86_64、1 GB RAM、900 MB 空閒空間

---

## 一、系統需求

| 項目 | 最低 | 建議 |
|---|---|---|
| Android 版本 | 7.0（Nougat）| 8.0+ (Oreo+) |
| ABI | arm64-v8a 或 x86_64 | arm64-v8a（現代手機）|
| RAM | 1 GB | 2 GB+ |
| 空間 | 900 MB（APK 400 MB + 解壓 380 MB + 存檔 5 MB）| 1.5 GB |
| GPU | OpenGL ES 3.0 | OpenGL ES 3.2 |
| SoC | 2016 以後 64-bit ARM | Snapdragon 660 等級以上 |

## 二、下載

前往 GitHub Releases：
- <https://github.com/HaCoMaTaTa/sc2-uqm-zhtw/releases/latest>
- 下載 **`激戰M星雲II-v3.8-release.apk`**（一般玩家版）
  - 若你要 debug 版（可插 adb logcat 除錯），下載 `激戰M星雲II-v3.8-debug.apk`
  - Debug 與 Release 的**簽章不同**，不能互升，只能擇一裝

## 三、安全性

**VirusTotal 掃描結果**：見 [Security_Scan_Report.md](Security_Scan_Report.md)

**APK 權限清單**（release 版）：

| 權限 | 用途 | 是否敏感 |
|---|---|---|
| `WAKE_LOCK` | 玩遊戲時螢幕不睡 | 否 |
| `VIBRATE` | 未來 haptic 預留（v3.8 尚未觸發）| 否 |
| `WRITE_EXTERNAL_STORAGE` (maxSdkVersion=29) | 舊 Android 相容 | 否 · Android 10+ 自動忽略 |

**已明確移除**（過去版本曾有）：
- ❌ INTERNET（不需連網 · 移除即免除 telemetry 疑慮）
- ❌ MANAGE_EXTERNAL_STORAGE（Play Store 拒用權限）
- ❌ PACKAGE_USAGE_STATS（隱私敏感）
- ❌ DUMP（root-only · 防毒會標紅）
- ❌ READ_EXTERNAL_STORAGE（不需要）

## 四、驗證 SHA256

**方式 1**：手機檔案管理員內建（部分廠商如 Samsung）

**方式 2**：用電腦
```powershell
# PowerShell
Get-FileHash 激戰M星雲II-v3.8-release.apk -Algorithm SHA256
# 對照 Releases 頁面 SHA256 值
```

**方式 3**：Android 上用 Termux
```bash
pkg install openssl
openssl dgst -sha256 激戰M星雲II-v3.8-release.apk
```

## 五、安裝

### 步驟 1：允許不明來源安裝

**Android 8.0+**：設定 → 應用程式 → 特殊權限 → 安裝未知應用程式 → 選「檔案管理員」或「Chrome」→ 「允許」

**Android 7**：設定 → 安全性 → 開啟「不明的來源」

### 步驟 2：點擊 apk 安裝

用檔案管理員找到下載的 `激戰M星雲II-v3.8-release.apk`，點擊 → 「安裝」→ 「開啟」。

### 步驟 3：Play Protect 警告（若有）

「Play Protect 未識別此應用程式」→ 點 「詳細資訊」→ 「仍要安裝」。這是因為非 Play Store 來源，不代表 App 危險。

### 步驟 4：首次啟動 → 解壓資產

首次開啟時，App 會解壓 383 MB 內建 assets 到 `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/content/`：

- 解壓進度：進度條 0~100%
- 時間：約 10-30 秒（依 SoC 效能）
- 完成後「Start Game」按鈕變綠

## 六、操作說明

### 主選單（觸控）

- 點方向 = 移動 focus
- 點畫面上「Enter」或雙擊選項 = 確認
- 點「ESC」或系統 back 手勢 = 返回

### 觸控 UI（進遊戲後）

畫面上有透明 overlay 疊在遊戲畫面上。

**兩種模式**（左上角 M/C 按鈕切換）：

#### Modern mode（預設）
- **左下**：200dp 類比搖桿 · 推方向 = 飛船自動轉向並前進（dirjoystick=3）
- **右上**：`[F6][F7][F3][F4]`、`[←][→][ESC]` 熱鍵
- **雙指縮放**：星圖 zoom in/out（等同 PageUp/PageDown）

#### Classic mode
- **左下**：4-way `[↑][↓][←][→]` D-pad
- **右上**：同上熱鍵

### 熱鍵說明

| 按鈕 | 對應 | 用途 |
|---|---|---|
| **F6** | KEYCODE_F6 | 星圖搜尋（觸發 IME 中文輸入 · patch 030）|
| **F7** | KEYCODE_F7 | HyperSpace / QuasiSpace 星圖切換 |
| **F3** | KEYCODE_F3 | 快速存檔 |
| **F4** | KEYCODE_F4 | 快速讀檔 |
| **←/→** | LEFT/RIGHT | 選單導覽 |
| **ESC** | ESCAPE | 遊戲內選單 · 返回 |
| **武器** | ENTER | 主武器 / 對話下一頁 |
| **特殊** | RIGHT_SHIFT | 特殊武器 |

### Back 手勢

Android 系統 back = ESC（不會 finish activity · 用 patch 019/020 攔截）· 避免誤觸丟失進度。

### 星圖點擊跳位（patch 004）

進入星圖時，直接點畫面上任何位置 = 游標跳過去。等同鍵盤方向鍵移動。

### 星圖 CJK 別名搜尋（patch 031）

按 F6 開啟搜尋輸入 · 打「參宿四」也能找到 Betelgeuse。詳見 [../translation/06_Locations/](../translation/06_Locations/) 別名對照。

## 七、Debug vs Release 差異

| 項目 | Debug | Release |
|---|---|---|
| 檔案大小 | ~400 MB | ~380 MB |
| ABI | arm64 + x86_64 | arm64 only（可切換）|
| R8 minify | 無 | 有 |
| Native strip | 無 DWARF | 已 strip |
| 簽章 | debug keystore | uqm-zh-tw keystore |
| 效能 | 略慢 | 略快 |
| 除錯 | `adb logcat` 可看 UQM 訊息 | 訊息簡化 |
| 主選單顯示 | `v0.8.5 HD MegaMod Debug` | `v0.8.5 HD MegaMod` |
| 升級性 | debug ↔ release **不能互升**（簽章不同）| 相同簽章版本間可升 |

**建議**：一般玩家用 Release · 想除錯或幫忙回報 bug 用 Debug。

## 八、已知限制

- **不上 Play Store**：CC BY-NC-SA 2.5 的 NonCommercial 與商業平台可能有爭議 · 詳見 [License_And_Attribution.md](License_And_Attribution.md)
- **無雲端存檔**：存檔只在裝置本地（`/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/`）
- **無多語 IME 切換介面內**：星圖搜尋依系統預設 IME 語言
- **首次啟動 sudo cold**：解壓 380 MB 需 10-30 秒 · 別以為 App 卡死
- **不支援分割畫面 / picture-in-picture**：SDL2 全螢幕獨占
- **手把支援**：Modern mode 內建虛擬 SDL joystick · 實體手把可運作但按鍵對應可能需自訂

## 九、疑難排解

### 首次啟動 EACCES / 無法解壓

**症狀**：`adb uninstall` 後 install 立即報 EACCES on FileOutputStream

**原因**：`/sdcard/Android/data/<package>/files/uqm-megamod` 是舊 UID 建立的，新裝的 App 拿到新 UID 沒權限寫

**解法**：
```
方法 A：改用 adb install -r（保留 UID）
方法 B：手動 rm -rf /sdcard/Android/data/org.megamod.uqm/files/uqm-megamod
方法 C：卸載時勾「同時清除資料」
```

### 觸控搖桿沒反應

- 檢查是否在 Modern mode（左上按鈕）
- 檢查是否在戰鬥/lander/interplanetary state（`DirJoyActive` 只在這幾個 state TRUE）
- 選單 state 用鍵盤方向鍵（stick 也會 emit UP/DOWN KEYCODE）

### 星圖點擊沒跳

- 只在 `pstarmap` state 有效 · 其他畫面 tap 被吞掉
- 檢查是否誤觸到搖桿或熱鍵區

### F 鍵按下無反應

- Modern mode 右上熱鍵在特定 state 可能被吞（如戰鬥中）
- 可先按 ESC 進 menu 再按

### 進入戰鬥後 crash

- 檢查 `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/uqm_log.txt`
- 常見：`Thread 'Unknown' blocking on 'DCQ'` → 字型 CharSpace 錯 · 開 issue 附 log

## 十、移除

長按 App 圖示 → 拖到「解除安裝」→ 確認。

**注意**：解除安裝**會同時清掉解壓的 380 MB content**（在 `/sdcard/Android/data/org.megamod.uqm/`）· 若你想留存檔，先手動備份 `.mgs` 檔。

## 十一、回報 bug

**必附**：
1. Android 版本（設定 → 關於手機）
2. 手機型號 + SoC
3. APK 版本（release v3.8 / debug）
4. `uqm_log.txt` 最後 100 行（`/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/uqm_log.txt`）
5. 螢幕截圖（若是 UI 問題）

**回報位置**：<https://github.com/HaCoMaTaTa/sc2-uqm-zhtw/issues>（用 `bug_report.md` 樣板）

## 十二、致謝與授權

見 [../NOTICE](../NOTICE) 與 [../LICENSE.CONTENT](../LICENSE.CONTENT)。

**特別致謝**：Android 版基於 MegaMod build/android/ scaffold（JHGuitarFreak），加上 12 個 Android 專屬 patches + 3 個引擎 patches 才能實機運作。
