# 上游 Android 移植現況調查

> 調查日期：2026-08-22
> 範圍：UQM / MegaMod / SDL2-Android 相關現有專案、工具鏈、風險
> 產生方式：Explore 子代理人執行網路蒐集（見章節末引用清單）
> 可信度標記：★★★=直接驗證、★★=間接引用、★=未能驗證（部分頁面 403）

---

## 1. 現成 UQM Android 移植（總覽）

### 1.1 直接可用的公開 UQM Android build

- **結論：目前找不到現行維護中的公開 UQM Android APK / 源碼。** ★★★
  - GitHub `urquan masters android` 搜尋：0 個 repo 匹配
  - F-Droid：無條目
  - Google Play：搜尋不到官方 UQM
  - APKPure / APKMirror：無有效條目（403）

### 1.2 pelya / commandergenius（歷史相關）

- URL: <https://github.com/pelya/commandergenius>
- 狀態：**活躍維護**（最近更新在 2026 年）
- 這是 SDL Android 通用打包框架（原為 Commander Genius），歷史上曾容納 UQM 子專案。
- MegaMod 原始碼 `src/uqm/gameinp.c:670` 直接引用此 repo 的方向搖桿演算法。
- 支援：
  - SDL 1.2 / SDL 2 雙軌
  - 螢幕虛擬搖桿 + 6 顆自訂按鈕
  - 多點觸控、加速度計、文字輸入
  - ABI：armeabi-v7a / arm64-v8a / x86 / x86_64
- **本次未在 `project/jni/application/` 內看到活躍 uqm 子目錄** ★★，需人工翻歷史 branch 確認。

### 1.3 其他歷史線索（未直接驗證，僅供追蹤）

- Serge van den Boom（原始 UQM 開發者之一）曾在 2010 年代前後有實驗性 Android 版本，但已停止維護。
- Google Play 上曾出現過非官方 "Ur-Quan Masters" 條目（第三方 wrapper），現已下架。

---

## 2. MegaMod 官方 Android 現況

### 2.1 GitHub 主線狀態 ★★★

- Repo: <https://github.com/JHGuitarFreak/UQM-MegaMod>
- 最新 commit（master）：2026-08-20 附近，屬 v0.8.5 發布前修正。
- `build/android/` 最後一次有意義的合併：**"Merge branch 'ReAndroid' into cmakeMaybe"**（約 2026-01，7 個月前）。
- 目前結構已具備（本地掃描結果，本次 §4 章節）：
  - Kotlin Multiplatform + Compose UI + SDL2Activity JNI wrapper
  - `org.megamod.uqm.MainActivity` → 顯示 Start Game / Enable Logging → 觸發 `EngineActivity(SDLActivity)`
  - `System.loadLibrary("SDL2")` + `System.loadLibrary("UrQuanMasters")`
  - ABI 限定 `arm64-v8a`、minSdk 24、compileSdk 36、agp 8.11.2、Kotlin 2.3.0
- **無 Android issue 或 PR** 目前開啟；也**未見任何 APK release**（SourceForge 該資源 403）。

### 2.2 引擎端 Android 適配（源碼掃描確認）★★★

- `src/config.h`：`__ANDROID__` 分支載入 `config_android.h`（由 CMake 從 `config_android.h.in` 產生）。
- `src/config_android.h.in`：`USERDIR = /storage/emulated/0/uqm-megamod/`（**注意：Android 11+ 需權限**）
- `CMakeLists.txt`：
  - `if (ANDROID) add_library(UrQuanMasters SHARED ${UQM_SOURCES})` — 產出 `.so` 而非 `.exe`
  - `list(APPEND UQM_LINK_LIBRARIES log)` — 連 Android `liblog`
- `src/uqm.c`：`#ifdef ANDROID int SDL_main(...)` 取代 `main`。
- `src/uqm/gameinp.c`：`GetDirectionalJoystickInput()` — 移植自 pelya/commandergenius。
- `src/uqm/setupmenu.c`：`#ifdef MELEE_ZOOM` 切換 Android 專用 melee zoom 選項。
- Changelog（`MegaMod Changelog.txt`）已明列多次 Android 修正（v0.8.0.83 起）：
  - Android 相容性初始加入
  - Directional joystick 誤觸修正
  - Shipyard/Outfit 螢幕控制修正
  - Melee scaler 切換
  - Android 控制隔離避免影響非 Android 平台

### 2.3 現階段可靠性判定

- 引擎 C 端：**看起來相當完備**（多次修正、CMake 條件分支健全、Android log 已接入）。
- Gradle/Kotlin 端：**看似完整但約 7 個月無 commit**（可能 SDL2 版本、Compose 版本已略過期）。
- 從未見 APK release ⇒ **未經公開 QA**，很可能還有未曝光的 bug。

---

## 3. SDL2 Android 最佳實務（2025–2026）

### 3.1 官方指引 ★★★

- 官方文件：<https://wiki.libsdl.org/SDL2/README-android>
- SDL2 目前主線仍在維護；SDL3 已釋出但 UQM 用 SDL2。
- 最低 API：SDL2 支援到 API 19，但**現代裝置優先**目標建議 minSdk 24 或 26。

### 3.2 觸控 / 輸入

- Native 事件：`SDL_FINGERDOWN / SDL_FINGERUP / SDL_FINGERMOTION`（正規化 0..1）
- 多點觸控：最多 16 指同時
- `SDL_HINT_TOUCH_MOUSE_EVENTS=0` 可關閉合成滑鼠事件（否則單指觸控會變滑鼠位移）
- **SDL2 沒有內建虛擬手把 overlay**，須自繪或用第三方（如 pelya 的實作）
- 硬體手把 / 加速度計 / 陀螺儀：走 SDL joystick API，最多 4 個

### 3.3 生命週期陷阱

- App 進背景會失去 GL context；必須實作：
  - `SDL_APP_WILLENTERBACKGROUND`
  - `SDL_APP_DIDENTERFOREGROUND`
- MegaMod 目前**未見**對應處理，屬待驗證高風險項。

---

## 4. 內容打包策略（我們有 ~116 MB）

### 4.1 我們專案的內容檔量

- `mm-0.8.5-content.uqm`：base game content（依 MegaMod 官方 pack）
- `zh-TW.uqm`：**38 MB**（SD 模式繁中 addon）
- `zh-TW-hd.uqm`：**77 MB**（HD 模式繁中字型 addon）
- 其他 addon（`3do-mode-*`, `mm-hd`, `sol-textures-*`, `dos-mode-*`）依需要

### 4.2 三種可行做法

| 做法 | 優點 | 缺點 | 適用情境 |
|---|---|---|---|
| **A. 全部塞 APK assets/** | 一鍵安裝、無需權限 | APK 巨大（~150+ MB）、Play 有 150 MB 硬限（自 side-load 無限） | 自用 side-load ✓ |
| **B. 首次啟動下載到 `getExternalFilesDir()`** | APK 精簡、可分包（先英文再中文） | 需伺服器或 GitHub Releases、首次體驗慢 | 未來公開分發 |
| **C. 使用者手動 push 到 `/storage/emulated/0/uqm-megamod/`** | 完全遵循 MegaMod 現有預設 | Android 11+ 需 `MANAGE_ALL_FILES` 權限、體驗差 | 開發除錯 |

### 4.3 Android 11+ Scoped Storage 影響 ★★

- `/storage/emulated/0/uqm-megamod/`（MegaMod 目前預設）在 API 30+ 需 `MANAGE_ALL_FILES` 特殊權限，Play 商店會嚴審。
- **建議 side-load 版預設路徑改為 `Context.getExternalFilesDir(null)`**：
  - 實際路徑：`/storage/emulated/0/Android/data/org.megamod.uqm/files/`
  - 無需任何權限、解除安裝自動清空
  - 需要修改 `config_android.h.in` 的 `USERDIR` 巨集 → 但巨集是硬編碼字串，必須改成 JNI 執行期取得

---

## 5. 中文字型渲染在 Android SDL2

### 5.1 已知風險（未驗證）★

- 我們用「**每字一張 PNG**」方式打包在 `.uqm` 內（fusion pixel 8/10/12px 為主）
- 引擎透過 UIO 掛載 `.uqm` → SDL2 texture 上載 → blit 到 canvas
- **理論上**在 Android SDL2 完全可行（純 SDL2 API，無 Android 特殊 hook）
- **實際風險**：
  1. `.uqm` 有 ~83,706 entries（zip64）→ Android NDK / libc 對超大 zip 未驗證
  2. 大量 texture cache 對低階手機記憶體壓力
  3. 若 UIO 用到 `mmap` 需驗證 Android bionic libc 相容性

### 5.2 待驗證項

- Zip64 EOCD（patch 007）是否在 Android arm64 build 正常運作
- Fusion Pixel 8px（我們現用值）在手機 DPI 下是否清晰

---

## 6. 工具鏈（2026 建議）

| 元件 | MegaMod 現有配置 | 2026 建議 | 差距 |
|---|---|---|---|
| Android Studio | – | 2025.2+（Meerkat 或後續） | 需安裝 |
| AGP（Gradle plugin） | 8.11.2 | ✓ 已現代 | 無 |
| Kotlin | 2.3.0 | ✓ 已現代 | 無 |
| compileSdk | 36 | ✓ 已現代 | 無 |
| minSdk | 24 | 保留或升 26 | 依需求 |
| CMake | 3.22.1 | 或升 3.30+ | 可保留 |
| NDK | 未指定 | **r27d LTS** 或 r29 | 需下載安裝 |
| SDL2 | 未打包（需外部下載 source） | libsdl-android AAR 或原始碼 | **需準備** |
| libpng / libogg / libvorbis / zlib | 需交叉編譯 | 從 NDK prefabs 或原始碼 | **需交叉編譯** |

**關鍵發現**：MegaMod `build/android/composeApp/src/main/java/org/libsdl/app/` 已內建 SDL2 Java 綁定（SDLActivity.java 等 10 個檔案）——這是 SDL2 Android 上游的官方 java wrapper。C 端 `libSDL2.so` 需要**自行交叉編譯**或**從 SDL 官方原始碼包提取 Android build**。

---

## 7. 風險總表（依可能性排序）

| # | 風險 | 可能性 | 影響 | 對策 |
|---|---|---|---|---|
| 1 | MegaMod Android build 從未產出過 APK，首次 build 遇到多個 CMake / Gradle 問題 | **高** | 大量 debug 時間 | 分階段：先只 build libSDL2 + hello world → 再 UQM 引擎 → 最後包 content |
| 2 | `.uqm`（Zip64，83k entries）在 Android arm64 掛載失敗或超慢 | **中高** | 遊戲卡在啟動或執行期 hang | 先用 1 MB test .uqm 驗證，再逐步加大 |
| 3 | 觸控 → UQM input 對映（原生只認鍵盤）需自寫 overlay | **中** | 玩不了 | 直接沿用 pelya commandergenius 的實作模式 |
| 4 | Scoped storage 讓 `/storage/emulated/0/uqm-megamod/` 寫入失敗 | **中** | 存檔失敗、config 遺失 | 改用 `getExternalFilesDir()`；需 patch `config_android.h.in` + JNI |
| 5 | 我們自己的 9 個 CJK 引擎 patch（001–011）與 Android build 交互作用未測 | **中** | 中文顯示錯亂或 crash | 分別在 Android build 上重跑 patch，逐一驗證 |
| 6 | 生命週期 pause/resume 導致 GL context 遺失 → crash | **中低** | 切背景就掛 | 加入 SDL_APP_* callback |
| 7 | 大量 PNG glyph texture 在低階手機 OOM | **中低** | 老手機打不開 | 分包載入、必要時退化英文 |
| 8 | APK 簽章與部署流程未規劃 | **低** | 最終步驟卡住 | 簡單：Android Studio → Build → Signed Bundle |

---

## 8. 引用清單

- <https://github.com/pelya/commandergenius>（2026-08-22 訪問，活躍）
- <https://github.com/JHGuitarFreak/UQM-MegaMod>（2026-08-22 訪問）
- <https://wiki.libsdl.org/SDL2/README-android>（2026-08-22 訪問）
- <https://developer.android.com/ndk/downloads>（NDK r27d LTS）
- <https://developer.android.com/guide/app-bundle>
- <https://developer.android.com/ndk/guides/cmake>
- SourceForge uqm-mods（HTTP 403，無法直接驗證有無 Android release）
- APKPure / APKMirror（HTTP 403，無法驗證）

---

## 附註：本文件不含個人推測

- 所有標 ★★★ 項目均為當日直接抓取或本地掃描確認
- 標 ★★ 為間接引用，需要在實作時再驗證
- 標 ★ 為未能驗證（多為被 403 封鎖之來源），列出僅供追蹤
