# UQM-MegaMod Android build 環境（stage 0 完成 2026-08-22）

## 環境路徑
- Android Studio: `C:\Program Files\Android\Android Studio\` (Meerkat 2026.1.3.7)
- Android SDK: `Q:\Dos_G\StarControl2\Android\sdk\` (刻意放 Q: 節省 C:)
- Build JDK: `Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1\` (Temurin 21 LTS zip)
- AVD: `uqm_test_arm64` (Pixel 7 · API 34 · arm64-v8a · google_apis)
- MegaMod Android project: `Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\`

## CRITICAL: Studio 的 JBR 25 不能跑 Gradle 8.14.3
- Android Studio Meerkat 內建 `jbr\` 是 **OpenJDK 25.0.2**
- Gradle 8.14.3 只支援到 Java 24，跑起來報錯 `What went wrong: 25.0.2`（訊息不友善但根因就是 Java 版本）
- **必須**用獨立 JDK 21 LTS：Adoptium Temurin 21 zip（Q:\...\Android\jdk21\）
- `JAVA_HOME` 要指到 Temurin 21，**不要**指到 Studio 的 jbr
- IDE 內部可以繼續用 JBR（GUI-only），CLI Gradle 用 Temurin 21

## 環境變數（User scope 已設）
- `ANDROID_HOME = Q:\Dos_G\StarControl2\Android\sdk`
- `ANDROID_SDK_ROOT = Q:\Dos_G\StarControl2\Android\sdk`
- `JAVA_HOME = Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1`
- `PATH` 加：`$JAVA_HOME\bin;$ANDROID_HOME\{platform-tools,cmdline-tools\latest\bin,emulator}`

## 已安裝 SDK 元件
- platform-tools 37.0.1（adb）
- emulator 37.1.11
- build-tools;36.0.0
- platforms;android-34（基本測試目標）
- platforms;android-36（MegaMod scaffold compileSdk）
- ndk;27.2.12479018（r27d LTS）
- cmake;3.22.1（MegaMod scaffold 指定版本）
- system-images;android-34;google_apis;arm64-v8a

## 驗證腳本
- `Q:\Dos_G\StarControl2\Android\_stage0_verify.ps1` — 23 項檢查，全綠 = stage 0 完成

## Gradle sync（無 native build）
- `.\gradlew.bat tasks` 首次 ~2m 39s（下載 gradle-8.14.3-bin.zip 230MB + 所有 plugin）
- 通過代表 Kotlin 2.3.0 + AGP 8.11.2 + Compose 1.9.3 相容性全部 OK

## Stage 1 完成 (2026-08-23): assembleDebug 產出 APK
- `composeApp-debug.apk` 18.54 MB
- 內含 `libSDL2.so` (5.7 MB) + `libUrQuanMasters.so` (12.1 MB, 我們的引擎) + `libc++_shared.so`
- MSYS2 sh 必須在 PATH: `$env:Path = "...;C:\msys64\usr\bin;$env:Path"` (CMakeLists 呼叫 `sh build/unix/recurse` 枚舉源碼)
- 用 `-Wno-error=format-security` 讓 lander.c 的 `sprintf(buf, GAME_STRING(...))` 通過（動態 format string 是 UQM 設計原意，desktop build 因 GCC 較寬鬆才通過）

## Stage 1 三個修改（存到 uqm-work/patches/）
- **012-android-format-security.patch** (`CMakeLists.txt` 6 行): `if (ANDROID) target_compile_options(UrQuanMasters PRIVATE -Wno-error=format-security)`。**注意**：必須用 `target_compile_options` 而非 append to `COMMON_C_FLAGS` — CMake 會把 `" -Wno-..."` 當成一整個 quoted arg 給 clang，clang 把它當檔名找不到就掛掉。
- **013-android-vorbis-and-ogg-alias.patch** (`helpers.cmake` 39 行):
  - libvorbis URL 換成 Xiph 官方 (原 `JHGuitarFreak/vorbis` fork 已 404, tag `uqm-megamod` 消失)
  - 新 URL: `https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.gz` SHA256=0e982409a9c3fc82ee06e08205b1355e5c6aa4c36bca58146ef399621b0ce5ab
  - FetchOgg 加 `add_library(Ogg::ogg ALIAS ogg)` (需在 FetchVorbis 前生效)
  - FetchVorbis 拆 `FetchContent_MakeAvailable` 為 `Populate` + patch FindOgg.cmake + `add_subdirectory`，Xiph libvorbis 的 `find_package(Ogg REQUIRED)` 內部走 `find_library(OGG_LIBRARY)` 要真檔案 — Populate 後覆寫其 `cmake/FindOgg.cmake` 為 stub 只認 `Ogg::ogg` target
- **014-android-ndk-version-pin.patch** (`build/android/composeApp/build.gradle.kts` 4 行): `ndkVersion = "27.2.12479018"` 強制 r27d LTS (否則 AGP silently 挑 27.0 rc)

## Stage 1 完整 build 流程（重跑用）
```powershell
$env:JAVA_HOME = 'Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1'
$env:ANDROID_HOME = 'Q:\Dos_G\StarControl2\Android\sdk'
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\cmdline-tools\latest\bin;$env:ANDROID_HOME\emulator;C:\msys64\usr\bin;$env:Path"
Set-Location Q:\Dos_G\StarControl2\UQM-MegaMod\build\android
.\gradlew.bat --no-daemon :composeApp:assembleDebug --console=plain
# 首次 ~5-10 min (fetch SDL2+libpng+libogg+libvorbis + 全 clang cross-compile)
# 增量 ~30s
```

## Stage 1 尚未完成
- APK **尚未**在 emulator 或裝置實測開機
- **完全未打包 content pack**（`mm-0.8.5-content.uqm` + `zh-TW.uqm`）→ 開啟後應該找不到 base game 資產而 crash 或報錯
- **未做觸控 UI overlay**、生命週期處理
- 這些是 Stage 3+ 的工作

## Stage 2 完成 (2026-08-23): CJK patches 早已 committed
- **關鍵發現**: MegaMod HEAD 已含 9 個 CJK patches 為 committed 分支 commit（`6311c53` bundle 001-006 + `207a5eb` patch 007 + `21f3316` patch 008 + `f907715` patch 009 + `042530a` patch 011）
- **含意**: Stage 1 build 出的 `libUrQuanMasters.so` 早就是「MegaMod + 全 CJK patches + 3 Android patches」的 fully-patched build，Stage 2 不必再 `git apply`
- Clean rebuild 2m 38s PASS
- `.so` 內符號驗證：`SDL_main`, `utf8StringCount`, `utf8StringCountN`, `GetClusterNameLocalized`, `SplitSubPages`, `getLineWithinWidth`, `prepareShadowAddons` 皆存在
- patch 007 (Zip64) 在 arm64 (`off_t=64bit`) 反而**比 Windows i686 (32bit) 更原生**
- patch 010 (race SoI zh) 是**純 addon shadow-content**，不動引擎，故沒有 `010.patch` 檔案
- 用 llvm-nm 檢驗符號位置: `Q:\...\Android\sdk\ndk\27.2.12479018\toolchains\llvm\prebuilt\windows-x86_64\bin\llvm-nm.exe`

## Stage 3 完成 (2026-08-23): Content 打包 + CLI 掛接
- APK **81.79 MB**（含 63.7 MB zh-TW content + 18.7 MB native libs + 28 MB DEX）
- Content 4 檔位置 `assets/uqm-content/{version,gamecontrollerdb.txt,packages/mm-0.8.5-content.uqm,addons/zh-TW.uqm}`
- **HD addon (zh-TW-hd.uqm 78 MB) 首發不含**，之後可加 asset pack
- `androidResources.noCompress += listOf("uqm")` 讓 aapt2 不重複壓縮 `.uqm` — uncompressed==compressed
- Gradle Copy task `stageUqmContent` 把檔案從 `../../../../uqm-work/install/content/` 搬到 `build/uqm-content-staged/uqm-content/`；`preBuild` 依賴它

## Stage 3 · Configuration cache 陷阱
- Gradle 8.14 configuration cache **不允許 `doFirst` closure 捕捉 Project reference**
- 具體：`rootProject.file()` 回傳的 `File` 若直接用在 doFirst 內會 fail with "cannot serialize Gradle script object references"
- **修法**：`val root = uqmContentRoot` 做為純 `java.io.File` local capture 進 registering block 內，再在 doFirst 用 `root`

## Stage 3 · Kotlin app shell 資料流
- MainActivity → `getExternalFilesDir(null)/uqm-megamod/{content,}` (免權限, 卸載自清)
- UqmContentExtractor 用 SHA-256 signature (`"relPath:size\n"` sorted) 檢查 `<content>/.uqm-content-version` 是否需重解壓
- App.kt Compose UI: `ExtractionState` sealed class (Idle/Extracting/Ready/Failed) 驅動 progress bar + Start Game enabled 狀態
- EngineActivity.getArguments() 產生 `--contentdir=<contentDir> --configdir=<userDir> --logfile=...`
- CLI 對齊 `src/uqm.c` getopt: `--contentdir` (-n), `--configdir` (-C), `--logfile` (-l)——**注意**是 `--logfile` 不是 `--log`（原 EngineActivity 有錯，Stage 3 修好）

## Stage 3 尚未完成
- **APK 沒實測開機**（emulator/裝置未跑過）
- 可能踩的雷：UIO mount `getExternalFilesDir()` 路徑、SDL_main 收到 argv[0]、Zip64 EOCD 首次 arm64 執行
- Stage 4 觸控 UI overlay 尚未開始
- 生命週期 (pause/resume GL context loss) 未處理

## Stage 3 · emulator smoke test (2026-08-23): 核心過、late crash
- **arm64 image 不能在 x86_64 host 跑** (Google Emulator 37.1.11 移除 QEMU2 二進位翻譯)
- **解法**: 加 x86_64 ABI 到 `abiFilters += listOf("arm64-v8a", "x86_64")` (APK +6.65 MB → 88.67 MB)
- 裝了 `system-images;android-34;google_apis;x86_64` + 建 AVD `uqm_test_x86_64` (Pixel 7)
- **通過**: content 解壓 (63.7 MB / 2s)、SDL_main 進 UQM、`1 available addon pack: zh-TW`、Ogg/WAV 解碼、所有 base 資源載入完
- **Late crash**: SIGSEGV in `TFB_Pure_ConfigureVideo+200` 在 `Starcon2Main` 執行緒正常返回後 30 秒
  - stack: TFB_Pure_ConfigureVideo → TFB_Pure_InitGraphics → TFB_InitGraphics → SDL_main+22349
  - fault addr `0x14` = NULL 指標偏移 (可能 `SDL_Screens[0]->h` in sdl2_pure.c:232)
  - 觸發時機: emulator SwiftShader GL + `onWindowFocusChanged: false` 觸發 pause/resume 路徑
  - **極可能實機 arm64 不會發生** (沒有 SwiftShader driver 假 focus loss)

## Stage 3 · crash 修好 (2026-08-23): patch 018
- **root cause**: `sdl2_pure.c:234` 直接 deref `SDL_Screens[0]->h` 沒 NULL guard
- 當 Android emulator 送假 `onWindowFocusChanged(false)` 時，引擎第二次進 `TFB_Pure_ConfigureVideo` 走 `window != NULL` else branch，但 `SDL_Screens[0]` 尚未 init → NULL deref
- **修法** (patch 018): 加 `if (SDL_Screens[0] != NULL && SDL_Screens[0]->h != CanvasHeight)` 防禦
- 這是**跨平台 upstream bug**，桌面若遇 orientation change 也會撞
- **驗證**: 重 build (58s 增量) + 重跑 emulator → **主選單顯示成功！**
- 截圖: `Android/smoke_test_after_fix.png` 顯示 UQM v0.8.5 MegaMod Debug 主選單 (地球背景 + Setup/Exit + "Main Menu Music by Saibuster")
- addr2line 解 crash 位址技巧: `& $addr2line -f -C -e <path>/libUrQuanMasters.so 0xfda58`; unstripped .so 在 `.cxx/Debug/*/obj/x86_64/`

## Stage 3 · emulator boot 順序 (重跑用)
```powershell
$env:Path = "Q:\Dos_G\StarControl2\Android\sdk\emulator;Q:\Dos_G\StarControl2\Android\sdk\platform-tools;$env:Path"
# headless + SwiftShader + no snapshot
Start-Process 'Q:\Dos_G\StarControl2\Android\sdk\emulator\emulator.exe' -ArgumentList '-avd','uqm_test_x86_64','-no-snapshot-load','-no-audio','-no-boot-anim','-gpu','swiftshader_indirect' -WindowStyle Hidden
# 開機 ~140s → boot_completed
adb wait-for-device
while ((adb shell getprop sys.boot_completed) -ne '1') { Start-Sleep 5 }
```

## Stage 3 · 直接啟 EngineActivity 跳過按鈕 (dev 測試用)
```powershell
$contentDir = '/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/content'
$userDir = '/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod'
adb shell am start -n 'org.megamod.uqm/org.megamod.uqm.EngineActivity' `
  --es content_dir "$contentDir" --es user_dir "$userDir" `
  --ez logging_enabled true --es log_file_path "$userDir/uqm_log.txt"
# MainActivity 必須先跑過一次觸發 extraction (adb start MainActivity → 等 UqmContentExtractor: Extraction complete)
```

## Stage 4 完成 (2026-08-23): 觸控 overlay + 360° 類比搖桿 + 中文選單
- **CLI**: EngineActivity.getArguments() 加 `--addon=zh-TW` → 開機自動掛載繁中 addon (patch 019)
- **UI v1** (patch 020 前): 4 方向 D-pad + A/B/ESC — 通過 tap 測試但戰鬥 UX 差
- **UI v2** (patch 020): 360° analog stick + Weapon/Special/ESC — user spec 是「推方向=飛船自動轉向並前進」
- 路徑: SDLActivity.onNativeKeyDown/Up(keycode) 從 Kotlin 直接呼叫，SDL2 native 內建 Android→SDL scancode 對映；UQM 引擎照收
- Compose Kotlin **陷阱**: pointer state 改動 <16ms 時 Compose 會 collapse frames，`LaunchedEffect(pressed)` 可能觀察不到中間 pressed=true — **必解法**: 在 `pointerInput` handler 內同步呼叫 SDLActivity.onNativeKeyDown/Up，不繞道 Compose state
- Pointer 事件 pass 用 `PointerEventPass.Initial` 才能在 SDL surface 之前搶到；`event.changes.forEach { if (it.pressed) it.consume() }` 防 SDL 收到假 mouse click

## Stage 4 · 類比搖桿→鍵盤翻譯規則 (patch 020, computeKeys())
- Dead zone: `magNorm < 0.2`
- 推**近乎正下方** (`y > 0.7·R` AND `|x| < 0.15·R`) → `KEYCODE_DPAD_DOWN`（給選單存檔位用）
- 其他任何推 → `KEYCODE_DPAD_UP`（thrust · 符合「推方向=前進」spec）
- 水平轉向: `x > 0.15·R` → `RIGHT`; `x < -0.15·R` → `LEFT`; 中間段 no turn（推正上正下純直行）
- Weapon = `KEYCODE_ENTER` (66) 對應 UQM `1.weapon.2 = Return`（戰鬥+選單雙用）
- Special = `KEYCODE_SHIFT_RIGHT` (60) 對應 UQM `1.special.1 = RightShift`
- ESC = `KEYCODE_ESCAPE` (111)
- 選單 up/left/right 全 OK；只有 down 需要「幾乎正下方」推

## Stage 4 · P2 完成 (2026-08-23): 虛擬 SDL joystick + dirjoystick=3
- **patch 021**: `CMakeLists.txt` — 在 `if (ANDROID)` block 加
  `target_sources(UrQuanMasters PRIVATE ${CMAKE_SOURCE_DIR}/src/android_virtual_joystick.c)`
  (recurse 系不掃 android_*.c，直接 target_sources 附加)
- **patch 022**: `src/uqm.c` line 2000 — `else if (temp < 0 || temp > 2)` → `> 4`
  修 MegaMod 原本的 bug: 錯誤訊息說「0-4」但 code 卡在 2。3 和 4 都是合法值（左/右搖桿 + auto-thrust）
- **patch 023**: `EngineActivity.getArguments()` 加 `arguments.add("--dirjoystick=3")`
- **patch 024**: 新 `src/android_virtual_joystick.c` (~180 行) — 3 個 JNI functions:
  - `nativeAttach()`: SDL_InitSubSystem(JOYSTICK) → SDL_JoystickAttachVirtual(GAMECONTROLLER, 6, 15, 0)
    → SDL_JoystickOpen → **註冊 controller mapping**（見下）→ **push CONTROLLERDEVICEADDED**
  - `nativeSetAxes(x, y)`: clamp -1..1 → `SDL_JoystickSetVirtualAxis(handle, LEFTX=0, sx)` + LEFTY=1
  - `nativeDetach()`: close + detach
- **patch 025**: 新 `VirtualJoystick.kt` — object with 3 external funs + `ensureAttached()` synchronized
  + `setAxes(x, y)`. TouchOverlay 的 AnalogStick `LaunchedEffect(Unit)` 呼叫 ensureAttached，
  pointer loop 每次事件 setAxes(offset.x/R, offset.y/R)
- **patch 020 (updated)**: TouchOverlay P2 版 — 移除 `computeKeys()` 的 KEYCODE_DPAD_LEFT/RIGHT
  發射（避免鍵盤 L/R 與 dirjoy auto-turn 打架），改在 top-right 加兩個 48dp `←` `→` 按鈕
  給選單 L/R 導覽用。垂直: UP 任何推方向, DOWN 只在 near-straight-down carve-out。

## Stage 4 · P2 · CRITICAL: SDL_JoystickAttachVirtual → GameController 需 mapping
- `SDL_JoystickAttachVirtual(SDL_JOYSTICK_TYPE_GAMECONTROLLER, ...)` **不**自動註冊 controller mapping
- 沒 mapping → `SDL_IsGameController(device_index)` return FALSE → UQM `create_joystick()`
  裡的 `if (!SDL_IsGameController) return` gate 直接踢掉
- **解**: attach 後 `SDL_JoystickGetGUID(handle)` → `SDL_JoystickGetGUIDString` →
  `SDL_snprintf` 完整 mapping (leftx:a0,lefty:a1,...,dpright:b14,platform:Android)
  → `SDL_GameControllerAddMapping(mapping)` (ret=0 表新加, 1 表 update)
- **另注意**: mapping 加得晚 (attach 後才加) → SDL 不會自動再 fire CONTROLLERDEVICEADDED
  → 手動 `SDL_PushEvent({type=SDL_CONTROLLERDEVICEADDED, cdevice.which=device_index})`
  讓 UQM 的 vcontrol.c event pump 收到並 create_joystick
- **另注意 device_index vs instance_id**: `SDL_IsGameController(device_index)` 是 int
  順序 index (0, 1, 2, ...)，不是 SDL_JoystickID。要透過 loop
  `for i in 0..SDL_NumJoysticks() { if SDL_JoystickGetDeviceInstanceID(i) == our_id { device_index = i } }`

## Stage 4 · P2 · CRITICAL: DirJoyActive gates joystick auto-turn
- `GetDirectionalJoystickInput()` 開頭: `if (!DirJoyActive || !optDirJoy[player]) return 0`
- `DirJoyActive` 只在 combat/lander/interplanetary 特定 state 內 TRUE (battle.c:485, lander.c:2667, solarsys.c:3192)
- 選單/戰艦內部/存檔畫面時 FALSE → **虛擬 joystick 軸只在戰鬥有效**
- 選單用鍵盤鍵繼續有效 (analog stick emit KEYCODE_DPAD_UP/DOWN + top-right ← → 按鈕)

## Stage 4 · P2 交付
- APK: `Q:\Dos_G\StarControl2\Android\release\uqm-megamod-zhTW-p2-YYYYMMDD-HHMM.apk` (~93 MB)
- 模擬器自我驗證 logs 確認:
  - `UqmVJoy: attached virtual joystick id=0 name='Virtual Controller' naxes=6`
  - `UqmVJoy: added controller mapping for GUID ...: ret=0`
  - `UqmVJoy: virtual joystick is recognized as a GameController`
  - `UqmVJoy: pushed CONTROLLERDEVICEADDED for device_index=0: ret=1`
  - Kotlin stick → nativeSetAxes 流量 (nx=0.05 ny=0.22..0.87 連續軸值)
  - UP → DOWN 轉換在 ny=0.7 觸發（carve-out 正確）
- **真正的戰鬥 auto-turn 效果需玩家實測**（自動化 adb input swipe 難模擬 melee 選隊+開打）

## Stage 5 完成 (2026-08-24): HD 啟動 + 覆蓋層 v3 (hotkeys + pinch + Classic 骨架)

### HD content 打包
- **patch 027 (build.gradle.kts)**: `requiredContentPaths` 加 `addons/mm-hd.uqm`, `addons/zh-TW-hd.uqm` — Gradle Copy task 一併 stage
- **patch 028 (EngineActivity)**: `getArguments()` 加：
  - `--addon=mm-hd --addon=zh-TW --addon=zh-TW-hd`（三 addon 疊層順序 mirror Play_HD.bat）
  - `--res=1280x960 --scale=bilinear --fullscreen=2 --opengl`
- **mm-hd 打包**: 用 `[System.IO.Compression.ZipFile]::Open` + `CompressionLevel::NoCompression` 把 mm-hd/ (12382 files, 231 MB) 壓成 mm-hd.uqm (232 MB, 24 秒完成)。PNG 已壓過，用 STORE 節省時間
- **APK size 403 MB**（含 mm-hd.uqm 232MB + zh-TW.uqm 40MB + zh-TW-hd.uqm 82MB + packages/mm-0.8.5-content.uqm 26MB + libs 20MB）— side-load only, 不能上 Play Store (200 MB 上限)

### 覆蓋層 v3 (patch 020 更新)
- **Top-left**: `[M / modern]` ↔ `[C / classic]` 切換按鈕（48dp）— 讀寫 SharedPreferences 記憶偏好
- **Top-right row 1**: `[F6][F7][F3][F4]` 4 個 48dp 熱鍵
  - F6 (KEYCODE_F6 = 136) = 星圖搜尋（觸發 SDL_StartTextInput → Android IME）
  - F7 (KEYCODE_F7 = 137) = HS/QS 星圖切換
  - F3 (KEYCODE_F3 = 133) = 快速存檔
  - F4 (KEYCODE_F4 = 134) = 快速讀檔
- **Top-right row 2**: `[←][→][ESC]`（原有）
- **Modern mode 底左**: 200dp 類比搖桿（沒變）
- **Classic mode 底左**: 4-way `[↑][↓][←][→]` 十字型 D-pad — **骨架**，之後可加 haptic / 8 方向對角
- **Pinch-to-zoom**: `PinchZoomDetector` composable 全螢幕底層偵測。**PointerEventPass.Main** (buttons/stick 在 Initial 已 consume 掉自己的手指)。兩指距離 ±30% baseline → 送 1 次 KEYCODE_PAGE_UP/DOWN → UQM 星圖 zoom in/out
- **patch 029 (OverlayPrefs.kt)**: 新 object `OverlayPrefs` 管理 ControlMode enum + SharedPreferences 持久化，被 `EngineActivity.onCreate` 初始化

### F 鍵對應 (uqm-work/extracted/base/menu.key)
| F 鍵 | UQM action | 手機 overlay 有否 |
|------|---|---|
| F1 | pause | 沒（可透過 ESC → menu） |
| F3 | quicksave | ✓ 熱鍵 |
| F4 | quickload | ✓ 熱鍵 |
| F5 | debug | 沒（debug 用） |
| F6 | search（星圖）| ✓ 熱鍵 |
| F7 | togglemap | ✓ 熱鍵 |
| F8 | screenshot | 沒 |
| F10 | exit | 沒（ESC → Quit 也可） |
| F11 | fullscreen toggle | 沒（Android 無意義） |
| ESC | in-game menu | ✓ 已在覆蓋層 |
| PageUp/Down | 星圖 zoom | ✓ pinch 手勢自動送 |

## Stage 5 · CRITICAL: HD 開啟需要三個條件全對，缺一不可
1. **mm-hd.uqm 壓縮結構** — 必須有 `mm-hd/` 頂層資料夾包起來（同 zh-TW.uqm 結構 `zh-TW/uqm.rmp`）
   - 錯：`mm-hd.rmp` `battle/` `comm/` ... 攤平在 zip root → UQM 把每個子資料夾誤認為獨立 addon（`11 available addon packs: battle, comm, cutscene, fonts, lander, nav, planets, ships, ui, zh-TW, zh-TW-hd`），mm-hd 不在清單裡
   - 對：`mm-hd/mm-hd.rmp` `mm-hd/battle/` ... → `3 available addon packs: mm-hd, zh-TW, zh-TW-hd`
   - PowerShell zip 時要 `$entryPath = "mm-hd/$rel"`，不能只給 `$rel`
2. **`--resfactor=2` CLI flag**（Stage 5 新加，patch 022）
   - **原本 MegaMod 沒有這個 flag** — `resolutionfactor` 只能從 `uqm.cfg` 讀。Play_HD.bat 靠 PowerShell 直接寫 cfg
   - Android 沒 cfg 寫入路徑，`--configdir` 是 Android/data 目錄不是 UQM 硬編路徑 → 必須加 CLI flag 才能繞過 cfg
   - `--res=1280x960` 只設 window 尺寸；`resolutionfactor` 才決定 HD/SD（uqm.c:675 `resolutionFactor = isAddonAvailable(HD_MODE) ? options.resolutionFactor.value : 0`）
3. **`--addon=mm-hd`** — 沒這個 UQM 不會 scan mm-hd，`isAddonAvailable("mm-hd")` 就 false → 強制 resolutionFactor=0

### HD 驗證 (UQM log)
- Boot log 應該有 `3 available addon packs: mm-hd, zh-TW, zh-TW-hd`（不是 11 個）
- 應該有 `Loading resource index 'mm-hd.rmp'`
- 應該有 `'addons/mm-hd/ui/mainmenu/title.ani' -- 43 bytes`（載 HD title）
- 主選單右下角應顯示 **`v0.8.5 HD MegaMod Debug`**（SD 只有 `MegaMod Debug`）

### Stage 5 已知未修 bug
- **Setup / Load Game 選單 HD 模式在模擬器全黑**：進 setup 或 load game 後 SDL 畫布空白，音樂正常播放（orbit.mod loops）。可能是 Swiftshader GL 對 HD 子選單的 canvas re-init 問題，需實機驗證是否為 emulator only
- **症狀**: `adb uninstall + install` 後 extraction 立即 EACCES on FileOutputStream
- **根因**: `/storage/emulated/0/Android/data/<package>/files/uqm-megamod` 目錄 owner 是「舊 UID」(u0_a193)，新裝的 app 拿到新 UID (u0_a194) → 無權寫入舊目錄
- **解**: 
  1. **改用 `adb install -r <apk>`**（reinstall preserving 舊 UID + data）— 不會踩雷
  2. 或先手動 `adb shell rm -rf /storage/emulated/0/Android/data/<package>/files/uqm-megamod`
  3. 或在 extractor 內偵測 mkdirs 失敗 → 呼叫 SAF 清理（複雜、不建議）
- 實機玩家全新安裝不會遇此問題（沒舊 UID 檔案）

### 自我驗證 (模擬器 x86_64 Pixel 7 API 34)
- 383 MB extraction 10.5 秒完成
- 主選單 HD 中文顯示 ✓（可看 `Android/release/p5_hd_boot.png`）
- Mode 切換 `[M] → [C]` UI 正確替換 ✓（`Android/release/p5_classic.png` 顯示 D-pad 取代搖桿）
- F3/F4/F6/F7 tap 皆送出對應 KEYCODE ✓（logcat 確認 keydown 133/134/136/137）
- Modern 搖桿 + 虛擬 SDL joystick 全鏈通（同 Stage 4 P2）
- Pinch 手勢因 adb shell input 不支援多指觸控，**未自動驗證**；程式邏輯保守（用 PointerEventPass.Main + filter isConsumed 避免與 stick/button 衝突）

### Stage 5 · APK 交付
- `Q:\Dos_G\StarControl2\Android\release\uqm-megamod-zhTW-hd-p2-YYYYMMDD-HHMM.apk` (~403 MB, side-load only)

## Stage 6 完成 (2026-08-24): 品牌化 + 圖示 + 權限清理

### APK 命名
- **App label** (strings.xml): `激戰M星雲II (Ur-Quan Masters HD zh-TW)`
- **APK filename** (Gradle): `setProperty("archivesBaseName", "激戰M星雲II")` → 激戰M星雲II-debug.apk
- **applicationId** 保持 ASCII `org.megamod.uqm` (Android package system 硬性限制)

### 圖示
- 資產來源: `mm-hd/ui/mainmenu/title.debrand.png` (無 branding 版標題畫面, 1280×960)
- 組合設計 (E+A composite):
  - 底: 深藍星雲 + 星空點綴 (build_starry_bg)
  - 中: Sa-Matra 三紅眼怪物 crop (y=540-960, x=400-880), 黑背景 chroma-key 透明, 縮到 360×360
  - 上: 「激戰M星雲II」紅字發光
  - 下: 「繁體中文化 · HD MegaMod」小字
- 生成腳本: `Q:\Dos_G\StarControl2\Android\_gen_composite.py` + `_install_icons.py`
- 5 密度全套 (mdpi 48 / hdpi 72 / xhdpi 96 / xxhdpi 144 / xxxhdpi 192) + round variants
- Adaptive icon foreground/background 分層 (API 26+)：safe zone 66% (inner 288/432)
- Play Store 512×512 promo: `Android/_icon_candidates/playstore_512.png`
- **刪除** compose-multiplatform 樣板的 `drawable-v24/ic_launcher_foreground.xml` + `drawable/ic_launcher_background.xml` (綠鑽石樣板圖)

### AndroidManifest 權限清理 (安全性掃描 + Play Store readiness)
| 權限 | 動作 | 原因 |
|---|---|---|
| INTERNET | 移除 | UQM netplay 關；不需連網 |
| READ_EXTERNAL_STORAGE | 移除 | scoped storage 完全不需要 |
| MANAGE_EXTERNAL_STORAGE | 移除 | 🚨 Play Store 會直接拒；也會觸發防毒軟體 |
| PACKAGE_USAGE_STATS | 移除 | 🚨 需要 Settings 手動授權；遊戲宣告不合理 |
| DUMP | 移除 | 🚨 root-only；防毒會標紅 |
| WRITE_EXTERNAL_STORAGE | 保留 (maxSdkVersion=29) | 舊 Android 相容 |
| VIBRATE | 保留 | 未來 haptic 預留 |
| **WAKE_LOCK** | **新增** | 玩遊戲時螢幕不睡 (EngineActivity 要 setKeepScreenOn) |
| allowBackup="true" | 改 false | 防止 Android auto-backup 把 380 MB content 塞進 Google Drive |
| fullBackupContent | 新加 false | 同上 |

### 資源負載分析 (交付給下載者的規格說明)
- **APK 400 MB**: 374 MB assets + 37 MB native (2 ABIs) + 28 MB dex + 1 MB resources
- **裝置佔用 780 MB**: 400 APK + 380 extracted content + 5 saves/config
- **RAM peak 200-400 MB**
- **最低機型**: Android 7.0 (API 24), 1 GB RAM, 900 MB free, OpenGL ES 3.0, 64-bit ARM (2016+)
- **實用機型**: Android 8.0+, 2 GB+ RAM, Snapdragon 660+ 級 SoC

### 交付
- APK: `Q:\Dos_G\StarControl2\Android\release\激戰M星雲II-v1.0-YYYYMMDD-HHMM.apk` (~400 MB, side-load only, dual-ABI)
- Play Store promo: `Q:\Dos_G\StarControl2\Android\_icon_candidates\playstore_512.png`

### Stage 6 · Icon 生成腳本 (可重跑)
```powershell
$env:PYTHONIOENCODING = 'utf-8'
python Q:\Dos_G\StarControl2\Android\_gen_icon_candidates.py  # 5 個候選 A-E
python Q:\Dos_G\StarControl2\Android\_gen_composite.py       # E+A 合成 F
python Q:\Dos_G\StarControl2\Android\_install_icons.py       # 佈到 res/mipmap-*/
```

### Stage 6 · 尚未做
- **Release keystore + assembleRelease** (目前 debug 簽章)
- R8 minifyEnabled + shrinkResources (dex 可再減 5 MB)

## Stage 6 · fix 2/3/4 完成 (2026-08-24 commit d5dec2b)

### #2 KEEP_SCREEN_ON — 螢幕不睡
- `EngineActivity.onCreate` 加 `window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)`
- 沒用 WakeLock class — Window flag 綁定 Activity lifecycle，Home 鍵/工作切換自動釋放，無需自己 lifecycle 管理
- Manifest 已宣告 WAKE_LOCK 權限 (Stage 6 前置)

### #3 Back gesture → SDLK_ESCAPE
- `EngineActivity.onCreate` 註冊 `onBackPressedDispatcher.addCallback(this, OnBackPressedCallback(true))` 攔截 Android 系統 back
- callback 內同步 `SDLActivity.onNativeKeyDown/Up(KEYCODE_ESCAPE)` — SDL 收到 ESC 進 UQM in-game menu
- 相容 Android 13+ Predictive Back gesture（滑手勢動畫還在，但放開時觸發 ESC 而非 finish）
- 避免玩家誤觸手勢丟失遊戲進度

### #4 星圖點擊跳位 — 引擎級 patch
三個檔案改動：
- **`src/libs/input/sdl/vcontrol.c`**：
  - 新增 file-scope 全域 `int touchClickPending / touchClickX / touchClickY`
  - 在 event switch 加 `case SDL_MOUSEBUTTONDOWN:` — 只認 `SDL_BUTTON_LEFT`
  - 座標寫入 canvas-space 值（SDL_RenderSetLogicalSize 已自動轉換 real screen px → game canvas px）
- **`src/libs/input/sdl/vcontrol.h`**：
  - `extern int touchClickPending;` 等 3 個 externs
  - 用 `int` 而非 `COORD/BOOLEAN` — 讓 header 不依賴 libs/misc.h 型別鏈
- **`src/uqm/planets/pstarmap.c: DoMoveCursor`**：
  - 加 `#include "libs/input/sdl/vcontrol.h"`
  - 在鍵盤方向鍵處理前檢查 `touchClickPending`
  - 扣掉 `SIS_ORG_X/Y` 拿到 SIS viewport 內座標
  - 走 `DISP_TO_UNIVERSEX/Y` 巨集 → universe 座標
  - 呼叫 `UpdateCursorLocation(0, 0, &univPt) + UpdateCursorInfo + UpdateFuelRequirement` 走鍵盤同樣的 path
  - 設 `isMove = TRUE` 讓當 frame 重繪
  - 每 frame 都清 flag — 越界 tap 不會殘留

**特點**：touchClickPending 只有 pstarmap.c 讀，其他 screen（melee/dialog/lander）從不檢查，所以觸控在非星圖狀態是無害的 no-op

### Stage 6 fix 交付
- **APK**: `Q:\Dos_G\StarControl2\Android\release\激戰M星雲II-v1.2-YYYYMMDD-HHMM.apk` (404.5 MB, +4 MB 新代碼)
- **git commit**: `d5dec2b` (Q:\Dos_G\StarControl2\UQM-MegaMod)

### Stage 6 fix 驗證
- 模擬器 x86_64 Pixel 7 API 34
- HD 主選單 renders (v0.8.5 HD MegaMod Debug)
- Android BACK 不再 finish EngineActivity (topResumedActivity 保持) ✓
- 星圖 click-to-jump 需玩家實測（進入遊戲後在 hyperspace/quasispace 才觸發 star map）

### Stage 5 · 未完 / 已知限制
- **實機命名輸入未實測**：SDL_StartTextInput 在 SDL2-Android 應會自動觸發系統 IME，但需玩家實測（開新遊戲取船名）
- **星圖點擊跳位**：本輪跳過（無 UQM mouse handler；需引擎 patch）
- **純旋轉模式**：本輪跳過（dirjoystick=3 auto-align 已足夠日常）
- **Classic mode**：只做骨架 4-way；未做 8-way 對角、haptic、mode-specific 按鈕
- **F5/F8/F10/F11 熱鍵**：未做（debug/exit/screenshot 少用）

## Stage 4 · APK 交付位置
- `Q:\Dos_G\StarControl2\Android\release\uqm-megamod-zhTW-analog-YYYYMMDD-HHMM.apk`
- ~93 MB · dual-ABI (arm64-v8a + x86_64) · 內含 mm-0.8.5-content.uqm + 最新 zh-TW.uqm
- 實機安裝: `adb install -r -t <path>` 或直接複製到手機再點開

## Stage 3 · UQM log 位置 (emulator)
- `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/uqm_log.txt`
- 也是 `--configdir` + `--userDir` 的 base
- Content 在: `/sdcard/Android/data/org.megamod.uqm/files/uqm-megamod/content/{version,gamecontrollerdb.txt,packages/*,addons/*}`

## Stage 3 未完成
- **完全沒實機測**（只 emulator）
- late crash 未除
- Stage 4 觸控 UI 尚未開始

## sdkmanager 授權接受技巧
- `sdkmanager --licenses` 是互動式，需要多個 y 回應
- **陷阱**：用 PowerShell 直接 `'y' * 100 | ...` 會生成 "yyyy...y" 一整串（無 newline），只算一個 y
- **正解**：`1..200 | ForEach-Object { "y" } | Out-File $yfile -Encoding ASCII` 產生真正的多行 y，再用 `Start-Process -RedirectStandardInput $yfile` 傳入

## winget 卡住的情境
- `winget install Microsoft.OpenJDK.21` 會觸發隱藏 UAC（無視窗），在無頭 PowerShell 環境會卡住
- **替代**：Adoptium Temurin 21 zip 直接下載解壓，無 UAC 完全 portable
- URL: `https://api.adoptium.net/v3/binary/latest/21/ga/windows/x64/jdk/hotspot/normal/eclipse`
