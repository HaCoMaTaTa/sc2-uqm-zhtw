# APK / ZIP 安全掃描報告

> **掃描時間**: 2026-08-31 13:32
> **掃描服務**: VirusTotal (<https://www.virustotal.com>)
> **報告狀態**: SHA256 已產生 · VirusTotal URL 待手動上傳確認

## 檔案清單

| 檔案 | 大小 (MB) | SHA256 | VirusTotal 報告 |
|---|---:|---|---|
| 激戰M星雲II-v3.8-release-20260831_1114.apk | 387.09 | `d64dc8577b7ce66432453bd836ddc8b1d405aa05347ce96e6eef68baf45a0962` | [檢視](https://www.virustotal.com/gui/file/d64dc8577b7ce66432453bd836ddc8b1d405aa05347ce96e6eef68baf45a0962) |
| 激戰M星雲II-v3.8-debug-20260831_1114.apk | 393.3 | `5743b83f0ac1a0ee8f18819f844bf15587c782bdf1b9327e69331470c066b889` | [檢視](https://www.virustotal.com/gui/file/5743b83f0ac1a0ee8f18819f844bf15587c782bdf1b9327e69331470c066b889) |
| SC2-zhTW-v1.0.12.zip | 349.83 | `e9a0fdfe7a2eb726e8b4723b4b793ff380a507d7bfbdeb957f61f0fc4d9d9acf` | [檢視](https://www.virustotal.com/gui/file/e9a0fdfe7a2eb726e8b4723b4b793ff380a507d7bfbdeb957f61f0fc4d9d9acf) |

## 手動掃描步驟

1. 開啟 <https://www.virustotal.com/gui/home/upload>
2. 拖曳上表任一檔案上傳（若表格內 URL 已顯示掃過結果，直接檢視即可）
3. 等待掃描完成（每檔約 1 分鐘）
4. 複製結果頁 URL → 貼回本檔對應列的『VirusTotal 報告』欄
5. commit 本檔更新
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
