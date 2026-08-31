# 本地中文化專案盤點（Android 移植視角）

> 掃描日期：2026-08-22
> 目的：釐清哪些 Windows 端資產可直接搬到 Android build、哪些需重寫

---

## 1. 中文化資產總覽

### 1.1 譯文與腳本（`uqm-work/translations/`）

- **35 個** `*.zh-TW.json` 翻譯檔（種族對話 + gamestrings + setupmenu + intro + cutscene + lander reports）
- 語系純度驗證：`_check_zh_purity.py`（fail-fast on 中英混雜 / 簡體字）
- 行數對齊驗證：`_check_line_counts.py`（NPC 對話配音時序對齊）
- Lua 模板檢查：`_check_lua_templates.py`（`<% ... %>` 首參數必須為 CJK）
- **可攜性**：★★★ 100% 可移植（純資料，與平台無關）

### 1.2 引擎 patches（`uqm-work/patches/`）

9 個 patch 對 MegaMod C 原始碼：

| Patch | 標的檔案 | 功能 | Android 適用性 |
|---|---|---|---|
| 001 | `report.c` | UTF-8 字元計數 + 動態 cell grid | ✓ 必要 |
| 002 | `gamestr.h` | `ELEMENTS_STRING_COUNT` 133/135 修正 | ✓ 必要（content pack 相依） |
| 003 | `orbit.c` | Enter Orbit 字型放大 | ✓ 建議 |
| 004 | `report.c` | 礦物撿取字型與位置 | ✓ 建議 |
| 005 | `font.c` | CJK 無字元間距 | ✓ 必要 |
| 006 | `comm.c` | CJK 對話換行 | ✓ **關鍵**（無限迴圈修正） |
| 007 | `uio/{types,uioutils,zip/zip}.h/.c` | Zip64 EOCD 支援 | ✓ **關鍵**（addon 掛載） |
| 009 | `sis.c` `encount.c` + `gamestr.h` | 星圖 postfix ZH（`STAR_POSTFIX_ZH_BASE=1024`） | ✓ 建議 |
| 011 | `pstarmap.c` | 星圖 cursor hover ZH | ✓ 建議 |

- **可攜性**：★★★ 100%（純 C 修改、不涉及平台 API）。**唯一風險**：patch 007 引入的 Zip64 讀取邏輯依賴 `off_t` 寬度，Android arm64 是 64-bit，應與 Windows i686 (32-bit) 行為不同 → 需驗證。

### 1.3 中文字型資源

- **SD addon**（`zh-TW.uqm` = **38.01 MB**）
  - Fusion Pixel 8/10/12 px 打包成每字一 PNG
  - `commander.fon`（Hayes）、`player.fon`、種族專屬字型（`arilou.fon` / `chmmr.fon` / `umgah.fon` / `talkingpet.fon` / `thraddash.fon` 等）
  - `starcon.fon` PC 選單專用（Fusion Pixel 8px）
- **HD addon**（`zh-TW-hd.uqm` = **77.84 MB**）
  - 相同內容 HD 尺寸重掃
  - 對應 MegaMod HD 模式（2x 解析度）
- **總計**：~116 MB 純 addon（不含 base game content pack）
- **可攜性**：★★★ 100%（PNG + kerndat.fnt，SDL2 直接可讀）

### 1.4 Build / package 腳本（PowerShell）

- `build_zh-TW.ps1`：JSON → .txt 譯文合成
- `package_zh-TW.ps1`：.txt → .uqm zip 打包 + 字型 shadow 重定向
- **可攜性**：★★（邏輯可轉但需要在 Linux/macOS 平台改成 bash 或 Python，若 Android build 在 Windows 進行則可沿用）

### 1.5 Windows 執行檔（`install/UrQuanMasters-zip64.exe`）

- 32-bit MSYS2 MINGW32 build，套用 patches 001–011
- **不可攜**：純 Windows 產物，Android 需完全從源碼重建（`.so` 而非 `.exe`）

---

## 2. Windows 端依賴清單

| 依賴 | Windows 版本 | Android 對應 | 移植方式 |
|---|---|---|---|
| SDL2 | 32-bit MSYS2 mingw | libSDL2.so (arm64) | NDK 交叉編譯或使用 SDL 官方 Android build |
| SDL2_mixer | 32-bit MSYS2 mingw | libSDL2_mixer.so (arm64) | 同上 |
| SDL2_net | 32-bit MSYS2 mingw | libSDL2_net.so (arm64) | 同上（若需 netplay） |
| libpng | zlib1 | libpng.so | NDK prefab 或原始碼 |
| libogg / libvorbis | .dll | .so | 同上 |
| zlib | zlib1.dll | Android system 內建 | 直接連 |
| libintl / iconv | .dll | Android bionic 部分支援 | 可能需 gettext 相容層或跳過 |

---

## 3. MegaMod Android scaffolding（本地端已存在）

### 3.1 位置

`Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\`

### 3.2 已有內容

```
build/android/
├── build.gradle.kts               # Kotlin Multiplatform root
├── settings.gradle.kts
├── gradle/
│   ├── libs.versions.toml          # agp 8.11.2, Kotlin 2.3.0
│   └── wrapper/
├── gradle.properties
├── gradlew / gradlew.bat
├── proguard-rules.pro
├── install-debug.sh / install-release.sh
├── clean.sh
└── composeApp/
    ├── build.gradle.kts            # NDK CMake 整合、arm64-v8a only
    └── src/
        ├── androidMain/
        │   ├── AndroidManifest.xml # MainActivity + EngineActivity
        │   ├── kotlin/org/megamod/uqm/
        │   │   ├── MainActivity.kt      # Compose 啟動畫面
        │   │   ├── EngineActivity.kt    # SDLActivity subclass
        │   │   ├── App.kt               # Start Game 按鈕
        │   │   ├── PermissionAssistant.kt
        │   │   ├── SettingsManager.kt
        │   │   ├── Platform.kt
        │   │   └── Greeting.kt
        │   ├── res/                # Launcher icon、theme、layout
        │   └── composeResources/drawable/title.png
        └── main/
            └── java/org/libsdl/app/     # SDL2 官方 Java 綁定 (10 檔)
                ├── SDLActivity.java
                ├── SDLSurface.java
                ├── SDLAudioManager.java
                ├── SDLControllerManager.java
                ├── SDL.java
                └── HIDDevice*.java (4 檔)
```

### 3.3 build.gradle.kts 摘要（`composeApp/`）

- `namespace = "org.megamod.uqm"`
- `applicationId = "org.megamod.uqm"`
- `compileSdk = 36`, `minSdk = 24`, `targetSdk = 36`
- `abiFilters = ["arm64-v8a"]`（**只支援 arm64**）
- CMake：`-DANDROID_STL=c++_shared` + `-DCMAKE_VERBOSE_MAKEFILE=ON`
- `externalNativeBuild.cmake.path = file("../../../CMakeLists.txt")`（**直接使用主 CMakeLists！**）

### 3.4 EngineActivity.kt 摘要

```kotlin
class EngineActivity : SDLActivity() {
    var uqm = "UrQuanMasters"
    override fun loadLibraries() {
        System.loadLibrary("c++_shared")
        System.loadLibrary("SDL2")
        System.loadLibrary(uqm)              // ← 我們要 build 出 libUrQuanMasters.so
    }
    override fun getMainSharedObject(): String = "lib${uqm}.so"
    // 支援 --log=FILE argument 由 MainActivity 傳入
}
```

### 3.5 CMakeLists.txt 對應段落

- `elseif (ANDROID) configure_file(config_android.h.in → config_android.h)`
- `if (ANDROID) add_library(UrQuanMasters SHARED ${UQM_SOURCES})`（非 exe，直接產 `.so`）
- `if (ANDROID) list(APPEND UQM_LINK_LIBRARIES log)`
- `NOT ANDROID` 時才 build 32-bit Windows exe

---

## 4. 缺失 / 需補完項目（Android build 要能跑）

### 4.1 必要缺項

1. **libSDL2.so for arm64**：目前 `build/android/` **沒有**帶入 SDL2 C 源碼或預編譯 `.so`
   - 需下載 SDL2 official source（https://libsdl.org/download-2.0.php）並 NDK 交叉編譯
   - 或用 `libsdl-org` 官方 Android build script
2. **libSDL2_mixer.so**（若需要遊戲音樂/音效）
3. **libpng.so / libogg.so / libvorbis.so / zlib**（若不用 NDK prefab）
4. **content pack**：`mm-0.8.5-content.uqm`（~40 MB）+ `zh-TW.uqm`（38 MB）+ 選配 `zh-TW-hd.uqm`（77 MB）
5. **虛擬手把 overlay**：SDL2 沒有內建，需在 `EngineActivity.kt` 或 SDLSurface 上加繪
6. **`config_android.h.in` 的 USERDIR patch**：從硬編碼 `/storage/emulated/0/uqm-megamod/` 改成 JNI 取得 `getExternalFilesDir()`

### 4.2 引擎 patch × Android build 交互作用（需驗證）

- **patch 007 (Zip64)** 於 arm64 (`off_t = 64bit`) 首次執行時應該行為正確，但需實測。
- **patch 001 (report.c UTF-8)** 純 C 邏輯，跨平台 OK。
- **patch 006 (comm.c 換行)** 純 C 邏輯，跨平台 OK。
- **患者 patch 005 (font.c CJK spacing)** 純 C 邏輯，跨平台 OK。
- 其他 patch 皆屬同性質，理論上 100% 相容。

### 4.3 未知數

- MegaMod `build/android/` scaffold **從未成功產出過 APK**（無 release 紀錄）
- Kotlin Compose UI 可能與新版 SDL2 Activity 生命週期有衝突
- 主 `CMakeLists.txt` 有一些 `if (WIN32)` 分支，Android 條件下可能未涵蓋所有必要 include path

---

## 5. 移植友善度總分

| 面向 | 完成度 | 說明 |
|---|---|---|
| C 引擎 Android 條件分支 | **80%** | config_android.h、CMake 分支、log 連結、SDL_main override 都齊 |
| Gradle / Kotlin 側 scaffolding | **60%** | 目錄結構齊全但可能 build fail（未 QA） |
| 中文化資產 | **100%** | 純 addon 檔，直接搬 |
| 引擎 patches (001-011) | **100%** | 純 C 修改，Android 適用 |
| 觸控 UI | **0%** | 完全沒有實作 |
| Content 部署路徑 | **20%** | 硬編碼 `/storage/emulated/0/` 不符 scoped storage |
| Native lib 交叉編譯 | **0%** | 沒有 SDL2/libpng/libogg 的 Android build 產物或 script |
| APK 簽章 | **0%** | 尚未規劃 keystore |
| 測試裝置 / CI | **0%** | 未規劃 |

**綜合評估**：**約 40% 完成度**。C 引擎與資產側非常成熟，Android app 殼與 native lib 交叉編譯是主要缺口。
