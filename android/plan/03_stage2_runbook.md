# 階段 2 · 套用 9 個 CJK 引擎 patch（完成紀錄）

> 日期：2026-08-23
> 狀態：**PASS**（實際發現：patches 已在 Stage 1 build 內）
> 產出：驗證用 `composeApp-debug.apk` 18.54 MB，`libUrQuanMasters.so` 內含全 CJK patch 符號

---

## 關鍵發現：patches 早已 committed 在 MegaMod 主分支

git log 顯示 CJK patches 是 MegaMod 分支 HEAD 上 5 個直接 commit：

```
042530a  zh-TW patch 011: localize star-map cursor-hover cluster name
f907715  zh-TW patch 009: Chinese star cluster names for hyperspace + encounter UI
21f3316  zh-TW patch 008: fix CJK scan report hang + cell size mismatch
6311c53  zh-TW patches 001-006 applied state (CJK localization)
207a5eb  UIO: add Zip64 EOCD Record support (zh-TW patch 007)
```

**含意**：Stage 1 產出的 `libUrQuanMasters.so` 早就是「MegaMod + 9 個 CJK patches + 3 個 Android 修 patches」的 fully-patched build。**Stage 2 不必再重跑 `git apply`**。

---

## 完成準則（AC）

- [x] 9 個 CJK patches 全部在 `git log` 可見（包含 001–006 bundle + 007 + 008 + 009 + 011）
- [x] 對應源碼標記在檔案內（marker check 全綠）
- [x] Clean rebuild 通過（`.cxx` + `thirdparty/` + `composeApp/build/` 全清 → 2m 38s BUILD SUCCESSFUL）
- [x] `libUrQuanMasters.so` 含 CJK 相關符號：`utf8StringCount`、`utf8StringCountN`、`GetClusterNameLocalized`、`SplitSubPages`、`getLineWithinWidth`、`prepareShadowAddons`、`SDL_main`
- [x] APK 內含正確 `.so`（arm64-v8a）：`libSDL2.so` + `libUrQuanMasters.so` + `libc++_shared.so`

---

## 每個 patch 的 Android 端驗證

| Patch | 目標 | 源碼標記檢查 | 符號檢查 | Android 相容性 |
|---|---|---|---|---|
| 001 | `report.c` UTF-8 char count + adaptive cell grid | `utf8StringCount(StrPtr)` 已在 `MakeReport()` call site | `utf8StringCount` symbol T (public) | 純 C，無平台相關 ✓ |
| 002 | `gamestr.h` `ELEMENTS_STRING_COUNT` = 133 (非 135) | `#define ELEMENTS_STRING_COUNT 133` | — (compile-time constant) | 純 header ✓ |
| 003 | `Enter Orbit` 較大字型 | 已 committed in bundle `6311c53` | — (font selection code) | 純 UI 邏輯 ✓ |
| 004 | 礦物撿取字型與位置 | 已 committed in bundle `6311c53` | — | 純 UI 邏輯 ✓ |
| 005 | `font.c` CJK 無 CharSpace | 已 committed in bundle `6311c53` | — | 純 C，字型繪製 ✓ |
| 006 | `comm.c` CJK 對話換行（防 `_count_lines` 無限迴圈） | `getLineWithinWidth` + `SplitSubPages` 存在 | `SplitSubPages` symbol t (static local) · `getLineWithinWidth` symbol T | 純 C ✓ |
| 007 | `uio/zip/zip.c` Zip64 EOCD | `zh-TW patch (007-uio-zip64-eocd)` marker at zip.c:667 | — (in `zip_fillDirStructureCentral()`) | **arm64 `off_t = 64bit`**（Windows i386 是 32bit）→ 反而更原生支援 ✓ |
| 008 | `report.c` CJK scan cell grid + word-wrap | `utf8StringCountN` + `RES_DESCALE` in report.c | `utf8StringCountN` symbol T | 純 C ✓ |
| 009 | 星圖 postfix 中文（`STAR_POSTFIX_ZH_BASE=1024`） | `#define STAR_POSTFIX_ZH_COUNT 149` + `STAR_POSTFIX_ZH_BASE = 1024` | `GetClusterNameLocalized` symbol T | 純 C ✓ |
| 011 | 星圖 cursor hover 中文標籤 | `zh-TW patch 011` marker at pstarmap.c:1812 | — (in `PickCluster` handler) | 純 UI 邏輯 ✓ |

**注**：patches 003/004 是 UI 字型選擇邏輯（`SetContextFont(MicroFont)` 之類），沒有新增 public 函式符號，只改內部呼叫。已在 bundle commit `6311c53` 內。

---

## 沒有的 patches: 010, 012–014

- **010**：race SoI zh 標籤——**純 addon shadow-content 覆蓋，不動引擎**（`ships/<race>/<file>.txt` 是 addon 檔）。故沒有 010.patch 檔。
- **012 / 013 / 014**：本次 Android port 新增的 3 個 build-system patch，已在 Stage 1 建立於 `uqm-work/patches/`，這裡對 CJK 譯文沒影響。

---

## Clean rebuild 命令與時間

```powershell
$env:JAVA_HOME = 'Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1'
$env:ANDROID_HOME = 'Q:\Dos_G\StarControl2\Android\sdk'
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\cmdline-tools\latest\bin;$env:ANDROID_HOME\emulator;C:\msys64\usr\bin;$env:Path"
Set-Location Q:\Dos_G\StarControl2\UQM-MegaMod\build\android
Remove-Item composeApp\.cxx, composeApp\build -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item Q:\Dos_G\StarControl2\UQM-MegaMod\thirdparty -Recurse -Force -ErrorAction SilentlyContinue
.\gradlew.bat --no-daemon :composeApp:assembleDebug --console=plain
```

- **實測時間**：2m 38s（clean）
- **依賴 fetch**：SDL2 2.32.10 + libpng 1.6.54 + libogg 1.3.6 + libvorbis 1.3.7（Xiph 官方，patch 013 生效）
- **無警告 fatal**（僅 vorbisfile.c 一則 `unused variable 'fpu'`，不影響）

---

## `libUrQuanMasters.so` 符號證據（llvm-nm）

```
Q:\Dos_G\StarControl2\Android\sdk\ndk\27.2.12479018\toolchains\llvm\prebuilt\windows-x86_64\bin\llvm-nm.exe libUrQuanMasters.so
```

```
00000000000e31e0 T SDL_main                    ← Android 入口點
000000000011f250 T utf8StringCount              ← patch 001 · 008
000000000011f2ac T utf8StringCountN             ← patch 008
00000000001c052c T GetClusterNameLocalized      ← patch 009
0000000000116b74 t SplitSubPages                ← patch 006 (static)
0000000000170864 T getLineWithinWidth           ← patch 006
00000000000e2d60 T prepareShadowAddons          ← MegaMod addon mount
```

Architecture: `elf64-littleaarch64`（arm64-v8a）✓

---

## 尚未完成

- **APK 尚未實測開機**（Stage 3 之前無 content pack，開會空畫面/crash）
- **content 未打包**（`mm-0.8.5-content.uqm` + `zh-TW.uqm` 116 MB 沒進 APK）→ Stage 3
- **`config_android.h` USERDIR 仍硬編碼** `/storage/emulated/0/uqm-megamod/` → Stage 3 需改為 JNI 執行期取 `getExternalFilesDir()`

---

## 下一步

**Stage 3**：Content 打包與載入路徑改寫（見 [00_Porting_Plan.md §階段 3](../00_Porting_Plan.md)）。
