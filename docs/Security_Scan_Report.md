# APK / ZIP 安全掃描報告

> **掃描時間**: 2026-08-31
> **掃描服務**: VirusTotal (<https://www.virustotal.com>)
> **報告狀態**: ✅ **兩個檔案皆通過掃描 · 0 個引擎偵測為惡意 · 0 個可疑**

## 檔案清單

| 檔案 | 大小 (MB) | SHA256 | VirusTotal 報告 | 檢出結果 |
|---|---:|---|---|---|
| 激戰M星雲II-v3.8-release.apk | 387.09 | `d64dc8577b7ce66432453bd836ddc8b1d405aa05347ce96e6eef68baf45a0962` | [檢視](https://www.virustotal.com/gui/file/d64dc8577b7ce66432453bd836ddc8b1d405aa05347ce96e6eef68baf45a0962/detection) | **0 / 74**（所有引擎皆判定安全）|
| SC2-zhTW-v1.0.12.zip | 349.83 | `e9a0fdfe7a2eb726e8b4723b4b793ff380a507d7bfbdeb957f61f0fc4d9d9acf` | [檢視](https://www.virustotal.com/gui/file/e9a0fdfe7a2eb726e8b4723b4b793ff380a507d7bfbdeb957f61f0fc4d9d9acf/detection) | **0 / 74**（所有引擎皆判定安全）|

## 掃描結果詳情

### 激戰M星雲II-v3.8-release.apk（Android release · 387 MB）

| 類別 | 數量 | 說明 |
|---|---:|---|
| **Malicious（惡意）** | **0** | ✅ 零檢出 |
| **Suspicious（可疑）** | **0** | ✅ 零疑點 |
| Undetected（無威脅） | ~42 | Microsoft / Symantec / McAfee / Fortinet / CrowdStrike / SentinelOne / Malwarebytes / TrendMicro / ClamAV / Kaspersky / BitDefender 等主流大廠皆通過 |
| Timeout | ~24 | 大 APK + 大量 native lib（libSDL2 / libpng / libvorbis / libUrQuanMasters）掃描超時（**非安全問題**）|
| Type-unsupported | 7 | 該引擎不支援 APK 檔案類型 |
| Failure | 2 | 引擎自身處理錯誤 |

### SC2-zhTW-v1.0.12.zip（PC 中文化包 · 350 MB）

| 類別 | 數量 | 說明 |
|---|---:|---|
| **Malicious（惡意）** | **0** | ✅ 零檢出 |
| **Suspicious（可疑）** | **0** | ✅ 零疑點 |
| Undetected（無威脅） | ~38 | 同上大廠 + AliCloud / TrendMicro / Ikarus 等 |
| Timeout | ~24 | 大 zip + patched exe + 完整 content pack + shadow addon 掃描超時（**非安全問題**）|
| Type-unsupported | 8 | 不支援 zip / exe 檔案類型 |
| Failure | 5 | 引擎自身處理錯誤（Arcabit / DeepInstinct / Skyhigh / Trustlook / WithSecure）|

## 為什麼有 Timeout / Type-unsupported / Failure

- **Timeout**：檔案大 + 內容多樣，部分引擎預設時限跑不完就中斷 · **不代表有威脅**
- **Type-unsupported**：某些企業級引擎專掃 Windows exe 或特定格式，不處理 APK/zip
- **Failure**：引擎自身錯誤，非檔案問題

**核心指標是 Malicious 與 Suspicious 兩欄 · 兩個檔案皆為 0**。

## 若你想自己再驗證一次

1. 開表格內任一「檢視」連結
2. 你會看到本次的完整掃描細節（每個引擎的結果）
3. 若想再重掃：點右上角 `Reanalyze file`（需 VT 帳號登入 · 支援 GitHub SSO）
4. 交叉驗證：<https://any.run/> · <https://www.hybrid-analysis.com/>

## 給下載者的話

- 本專案作者已透過本地 `Get-FileHash` 產生 SHA256 sidecar（`.sha256` 檔案）
- 你可自行對照下載檔案的 hash（見 [PC_Install_Guide.md § 三](PC_Install_Guide.md) / [Android_Install_Guide.md § 四](Android_Install_Guide.md)）
- 本掃描報告以「掃描時 SHA256 對應之檔案」為準，若你下載到的 hash 與上表不符，代表下載損毀或被中間人竄改
## APK 權限清單（僅供對照 · release 版）

| 權限 | 用途 |
|---|---|
| `WAKE_LOCK` | 玩遊戲時螢幕不睡（`EngineActivity.setKeepScreenOn`）|
| `VIBRATE` | 未來 haptic 預留（目前未觸發）|
| `WRITE_EXTERNAL_STORAGE` (maxSdkVersion=29) | 舊 Android 相容（Android 10+ 自動忽略）|

**已移除**（過去版本曾有，v1.5 起清理）：`INTERNET`, `MANAGE_EXTERNAL_STORAGE`, `PACKAGE_USAGE_STATS`, `DUMP`, `READ_EXTERNAL_STORAGE`

## 常見誤判說明

- **VirusTotal < 5 引擎警告**：屬正常範圍。自簽 APK + 大量 native lib (libSDL2/libpng/libvorbis) + Zip64 asset 常被啟發式引擎誤判
- **Windows Defender SmartScreen**：因 exe 未購買 Authenticode 簽章，右鍵 → 內容 → 解除封鎖即可
- **Android Play Protect 警告**：因非 Play Store 來源；設定裡明確 allow 即可

如發現任何真的可疑報告，請開 GitHub Issue 附上 VirusTotal 連結，我會第一時間查看。
