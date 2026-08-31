# 階段 1 · Native lib 交叉編譯（完成紀錄）

> 日期：2026-08-23
> 狀態：**PASS**
> 產出：`composeApp-debug.apk` 18.54 MB · `libSDL2.so` 5.7 MB · `libUrQuanMasters.so` 12.1 MB

---

## 完成準則（AC）

- [x] `./gradlew :composeApp:assembleDebug` 成功產出 debug APK
- [x] APK 內含 `lib/arm64-v8a/libSDL2.so` + `libUrQuanMasters.so`
- [ ] `libUrQuanMasters.so` 內含 `SDL_main` symbol（未 readelf 驗證，但既然 link 成功可推定）
- [ ] APK 在 emulator 上實測開機（**尚未做** — 屬 Stage 3+ 的 content 部署後才有意義）

---

## 修好的 5 個問題

### 1. NDK 版本 AGP 靜默降版 (build.gradle.kts)

**症狀**：初次跑 assembleDebug 時 AGP 挑 `ndk\27.0.12077973`（隨 cmdline-tools 一起下來的舊 rc 版），而非我們刻意裝的 `27.2.12479018` LTS。

**修法**：`android { ndkVersion = "27.2.12479018" }`

**Patch**：`uqm-work/patches/014-android-ndk-version-pin.patch`

---

### 2. libvorbis URL 404 (helpers.cmake)

**症狀**：`Build step for libvorbis failed: 1` → ninja 顯示 HTTP 404

**根因**：MegaMod `FetchVorbis()` 指向 `https://github.com/JHGuitarFreak/vorbis/archive/refs/tags/uqm-megamod.tar.gz` — 這個 fork repo 已被刪除（API 也 404）。

**修法**：改用 Xiph 官方 <https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.gz> · SHA256=`0e982409a9c3fc82ee06e08205b1355e5c6aa4c36bca58146ef399621b0ce5ab`

**Patch**：`uqm-work/patches/013-android-vorbis-and-ogg-alias.patch`（同 patch 內）

---

### 3. Xiph libvorbis `find_package(Ogg)` 找不到 (helpers.cmake)

**症狀**：`Could NOT find Ogg (missing: OGG_LIBRARY OGG_INCLUDE_DIR)`

**根因**：Xiph libvorbis 的 `cmake/FindOgg.cmake` 用 `find_library(OGG_LIBRARY NAMES ogg ...)` 要磁碟上真的 `.a`/`.so` 檔。FetchContent 平行 build 時 ogg 二進位還沒產生。

**修法**（兩步）：
1. `FetchOgg()` 內建 `add_library(Ogg::ogg ALIAS ogg)` 讓 CMake target 存在
2. `FetchVorbis()` 拆解 `FetchContent_MakeAvailable` 為 `Populate` + patch `cmake/FindOgg.cmake` + `add_subdirectory`。stub 版 FindOgg 只認 `Ogg::ogg` target。

**Patch**：`uqm-work/patches/013-android-vorbis-and-ogg-alias.patch`

---

### 4. `sh` 不在 PATH (build/unix/recurse)

**症狀**：`CMake Error at CMakeLists.txt:305 (message): recurse script failed with exit code: The system cannot find the file specified`

**根因**：MegaMod CMakeLists 用 `execute_process(COMMAND sh "${CMAKE_SOURCE_DIR}/build/unix/recurse" "uqm" ...)` 枚舉源碼檔。Android build 走「Linux」分支需要 `sh`。Windows 默認無 sh。

**修法**：把 MSYS2 sh 加到 PATH：
```powershell
$env:Path = "...;C:\msys64\usr\bin;$env:Path"
```
（**Windows 環境變數不設**，只在 build session 加入，避免污染其他工作）

**無 patch**（純 build 環境設定）

---

### 5. `lander.c` `-Werror=format-security` (CMakeLists.txt)

**症狀**：
```
error: format string is not a string literal (potentially insecure)
sprintf (pPSD->AmountBuf, GAME_STRING (ELEMENTS_STRING_BASE + 133));
```

**根因**：NDK Clang 預設加 `-Werror=format-security`；UQM 的 lander.c 刻意用 runtime GAME_STRING() 當 sprintf format 傳「元素描述」。這是 UQM 原設計意圖（`GAME_STRING` 回傳 static 文字，包含 `%d` 之類的格式符）。

**修法**：
```cmake
if (ANDROID)
    list (APPEND UQM_LINK_LIBRARIES log)
    target_compile_options (UrQuanMasters PRIVATE -Wno-error=format-security)
endif ()
```

**關鍵陷阱**：一開始我把 flag 加到 `COMMON_C_FLAGS` 字串，結果 CMake 把 `" -Wno-error=format-security"` 當成一個 quoted arg 傳給 clang，clang 把它當檔名找不到就掛掉。**必須用 `target_compile_options` 列表形式**。

**Patch**：`uqm-work/patches/012-android-format-security.patch`

---

## 重跑 Stage 1 的完整命令

```powershell
# 1) 設環境
$env:JAVA_HOME = 'Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1'
$env:ANDROID_HOME = 'Q:\Dos_G\StarControl2\Android\sdk'
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\cmdline-tools\latest\bin;$env:ANDROID_HOME\emulator;C:\msys64\usr\bin;$env:Path"

# 2) 進到 project
Set-Location Q:\Dos_G\StarControl2\UQM-MegaMod\build\android

# 3) build（首次 ~5-10 min，增量 ~30s）
.\gradlew.bat --no-daemon :composeApp:assembleDebug --console=plain

# 4) 產出
Get-ChildItem composeApp\build\outputs\apk\debug\*.apk
# → composeApp-debug.apk (18.54 MB)
```

---

## 尚未完成 · 進到 Stage 2 前必知

- APK **可以編**、**沒實測跑**
- APK 內**沒有 game content**（`mm-0.8.5-content.uqm`、`zh-TW.uqm` 都沒進 assets/）
- 若現在裝到 emulator，`libUrQuanMasters.so` 找不到 base game content 應該會直接 crash 或空畫面
- 這是 **Stage 3（Content 部署）** 的工作

## 尚未套用的其他 patches

Stage 1 只驗證 native build 能編。**中文化引擎 patches 001–011 尚未 apply**。這是 Stage 2 的工作：
- 從 `uqm-work/patches/` 依序 apply 001–011（跳過 Windows-only 段落若有）
- 每次 apply 後跑 `assembleDebug` 確認仍 build

---

## 下一步

**Stage 2**：把 zh-TW patches 001–011 apply 到 MegaMod source，逐一驗證 Android build 仍過。

**Stage 3**：把 `mm-0.8.5-content.uqm` + `zh-TW.uqm` 打包到 APK assets 並修 `config_android.h` USERDIR 路徑（現在硬編碼 `/storage/emulated/0/uqm-megamod/`）。
