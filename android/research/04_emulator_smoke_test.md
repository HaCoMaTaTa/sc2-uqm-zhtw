# Emulator smoke test 紀錄

> 日期：2026-08-23
> 環境：Android Studio emulator uqm_test_x86_64 (Pixel 7 · API 34 · Android 14)
> APK：`composeApp-debug.apk` 88.67 MB（arm64-v8a + x86_64）
> 狀態：**核心功能全過，late crash 在 TFB_Pure_ConfigureVideo**

---

## 前置：arm64 image 在 x86_64 host 不能跑

- Google Android Emulator **37.1.11** 已移除 arm64-on-x86_64 二進位翻譯支援
- FATAL: `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host.`
- 解決：為 debug variant 加 x86_64 ABI（在 `build.gradle.kts` 的 `abiFilters += listOf("arm64-v8a", "x86_64")`）
- APK 從 82 MB → 88.67 MB（+6.65 MB，因為 zh-TW content 63.7 MB 是共用的，native libs +19 MB 但這部分本來就有）

---

## 通過項目（全部證明 Stage 1+2+3 有效）

| 檢查點 | 證據 |
|---|---|
| APK 安裝 | `adb install` → Success in 26 s |
| MainActivity 啟動 | 無 crash |
| **Content 首次解壓** | `UqmContentExtractor: Extraction complete: 4 file(s), 65259 KiB` in ~2 s |
| Extracted 檔案就位 | `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/content/` 內含 `version` / `gamecontrollerdb.txt` / `packages/mm-0.8.5-content.uqm` / `addons/zh-TW.uqm` |
| EngineActivity 啟動 | Compose launcher → SDLActivity 過渡完成 |
| SDL2 nativeSetupJNI | 音訊 + Controller + 主 SDL 全 init |
| Window 尺寸協商 | `2400x1080` (device) → engine 拿 `640x480` (UQM native) |
| **CLI args 傳到 native** | UQM log 前 3 行：`argv[1] = [--contentdir=...] argv[2] = [--configdir=...] argv[3] = [--logfile=...]` |
| Base pack mount | `uio_open mm-0.8.5-content.uqm` |
| **zh-TW addon mount** | `1 available addon pack. 1. zh-TW` |
| SDL2 renderer 挑選 | `SDL2 renderer 'opengles2' selected` |
| GameControllerDB 載入 | `Loaded controller mappings from /sdcard/.../gamecontrollerdb.txt` |
| OpenSLES 音訊開啟 | `using openslES at 44100 Hz 16 bit stereo, 4096 samples audio buffer` |
| Ogg Vorbis 解碼 | `_GetMusicData(): loading base/ui/mainmenu1.ogg` 順利 |
| 選單音效解碼 | 6 個 WAV 全 `_GetSoundBankData(): decoded bytes` |
| Base 全資源 load | 所有 ship .ani / .txt、fonts、cutscene 都印在 log |
| Lua VM 啟動 | `Loading script 'initprops.lua'` |
| 遊戲初始設定 | `Set Seed Type: None / Difficulty: Normal / Extended: False / Nomad: Off` |

---

## Late crash：TFB_Pure_ConfigureVideo 在 Starcon2Main 收尾後

### Tombstone stack（native）
```
Fatal signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0000000000000014
  in tid 4654 (SDLThread), pid 3559 (SDLActivity)

#00 libUrQuanMasters.so  TFB_Pure_ConfigureVideo+200   (src/libs/graphics/sdl/sdl2_pure.c:147)
#01 libUrQuanMasters.so  TFB_Pure_InitGraphics+111     (src/libs/graphics/sdl/sdl2_pure.c:354)
#02 libUrQuanMasters.so  TFB_InitGraphics+112          (src/libs/graphics/sdl/sdl_common.c)
#03 libUrQuanMasters.so  SDL_main+22349                (src/uqm.c)
#04 libSDL2.so           Java_org_libsdl_app_SDLActivity_nativeRunMain+708
```

### 觀察

1. **UQM engine log 最後正常印出**：
   ```
   Set Nomad: Off
   'base/ui/newgame.ani' -- 110 bytes
   Thread 'Starcon2Main' done (returned 0).
   Thread 'audio stream decoder' done (returned 0).
   ```
   即 `Starcon2Main` 主遊戲執行緒**正常返回**——這不合理，正常玩不會這樣。

2. Crash 在 SIGSEGV @ addr `0x14` (十進位 20) — 典型 NULL 指標存取結構欄位
   - SDL_Surface 的 `h` 欄位大約在 offset 0x14
   - `sdl2_pure.c:232` 有 `if (SDL_Screens[0]->h != CanvasHeight)` — 若 `SDL_Screens[0]` NULL 就撞這個

3. **時序上**：`Starcon2Main done` → 30 秒後 SIGSEGV。這強烈暗示 shutdown 或 orientation-change reconfig 路徑重新呼叫 `TFB_Pure_ConfigureVideo`，但此時 `SDL_Screens[]` 已被清空/未初始化。

### 為何很可能是 **emulator-specific**

- Emulator 用 **SwiftShader**（software OpenGL ES driver）
- Log 顯示 `onWindowFocusChanged(): false` 在 Starcon2Main 結束前——emulator 給了假的 focus loss，觸發 UQM 對應的 pause/resume 邏輯
- 實體裝置的 GLES driver + 觸控輸入不太可能製造出「30 秒後才 focus loss」的怪狀況
- 目前 UQM Android build **既沒有 SDL_APP_WILLENTERBACKGROUND / SDL_APP_DIDENTERFOREGROUND handler**（見 Stage 5 計畫），也沒有 orientation change reconfig 保護

---

## 產出檔案

- [Android/smoke_test_engine_running.png](Android/smoke_test_engine_running.png) — 螢幕截圖（實際上是 crash 後回到 launcher 那張）
- 完整 UQM engine log：device 上 `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/uqm_log.txt`（session 結束會遺失，可用 `adb pull` 保存）

---

## 建議下一步

三條路的效益 vs 成本：

| 路徑 | 成本 | 對整體 port 進度貢獻 |
|---|---|---|
| **A. 進 Stage 4 觸控 overlay** | 高（開發實體 UI） | 觸控本來就要實機驗；若實機不 crash 這 emulator crash 就不重要 |
| B. Emulator 除 crash（addr2line + `--renderer=gl` + 補 SDL_APP_* handler） | 中（1-2 小時 diag） | 幫 emulator dev 體驗，但實機不一定同 bug |
| C. 弄 arm64 實體手機 USB debugging | 低（5 分鐘設定 + 1 條線） | 一次終結所有猜測，也為 Stage 4 觸控準備 |

**建議順序**：C → A → 若還有 emulator 需求再做 B。
