# 階段 3 · Content 打包與載入路徑改寫（完成紀錄）

> 日期：2026-08-23
> 狀態：**PASS**（APK 產出、內容確認、CLI 掛接完成；尚未在裝置實測開機）
> 產出：`composeApp-debug.apk` **81.79 MB** 含全部必要 content

---

## 完成準則（AC）

- [x] APK 內含 `assets/uqm-content/{version,gamecontrollerdb.txt,packages/mm-0.8.5-content.uqm,addons/zh-TW.uqm}`
- [x] `.uqm` zip 檔案未被 aapt2 重複壓縮（`noCompress += "uqm"` 生效 — uncompressed size == compressed size）
- [x] Kotlin `UqmContentExtractor` 建置成功，透過 SHA-256 signature 判斷是否需重新解壓
- [x] `MainActivity` 首次啟動觸發解壓，Compose UI 顯示 progress bar
- [x] `EngineActivity.getArguments()` 產生 `--contentdir=<path> --configdir=<path>` CLI 參數傳給 UQM native side
- [x] CLI 參數對齊 `src/uqm.c` 的 long-form option 表：`--contentdir` (`-n`), `--configdir` (`-C`), `--logfile` (`-l`)
- [ ] APK 在 emulator/裝置實測開機（**尚未做**——留給下一次 session 或 Stage 4 觸控前先 sanity check）

---

## 動了什麼

### 1. `build/android/composeApp/build.gradle.kts` — content staging

新增：
- `androidResources.noCompress += listOf("uqm")` — 避免 aapt2 對已壓縮的 `.uqm` 重壓
- `sourceSets["main"].assets.srcDir(build/uqm-content-staged/)` — 額外一個 asset root
- **`stageUqmContent` Copy task** — 從 `Q:\Dos_G\StarControl2\uqm-work\install\content\` 複製 4 個必要檔到 `build/uqm-content-staged/uqm-content/`
- `tasks.named("preBuild") { dependsOn(stageUqmContent) }` — 每次 build 前先 stage

**Configuration cache 陷阱**：`doFirst` 抓 `uqmContentRoot` 若透過 `rootProject.file()` 直接使用會捕捉 Project reference → configuration cache serialization 失敗。**修法**：把 `val root = uqmContentRoot` 做為 `java.io.File` local capture 進 task 內。

### 2. 新檔 `UqmContentExtractor.kt`

- 遞迴列舉 `AssetManager.list("uqm-content")` 全部葉節點
- 用 `openFd()`（非壓縮 asset）或 stream 全掃（壓縮 asset）計算 size
- Signature = SHA-256 of `"relPath:size\n"` 對每個 asset 排序後串接 → 存 `<content>/.uqm-content-version`
- 首次啟動：signature 不符 → 全清 + 全展 + progress 回呼
- 之後：signature 相符 → 跳過（跑一次 signature 計算約 <200 ms，因為只讀 metadata）

### 3. `MainActivity.kt` 改寫

- 移除 `PermissionHelper.getManageExternalStoragePermission()`（不再需要——`getExternalFilesDir()` API 24+ 免權限）
- Compute `userDir = getExternalFilesDir(null)/uqm-megamod`, `contentDir = userDir/content`
- Launch coroutine（IO dispatcher）呼叫 `UqmContentExtractor.ensureExtracted(this, content) { p -> ... }`
- 用 `mutableStateOf<ExtractionState>` 驅動 Compose UI（`Idle`/`Extracting`/`Ready`/`Failed`）
- 完成後 `onStartGame` callback 才 enable，並把 content/user path 傳給 EngineActivity Intent

### 4. `App.kt` 改寫

- 新 signature：`App(extractionState, onStartGame)`
- Start Game 按鈕 `enabled = extractionState is Ready`
- 解壓中顯示 `LinearProgressIndicator` + 目前處理檔名
- 失敗顯示錯誤訊息
- `Context.startGame(...)` extension 新增 `contentDirPath` / `userDirPath` 兩參數，塞進 Intent

### 5. `EngineActivity.kt` 改寫

- `onCreate` 讀 `content_dir` + `user_dir` extra
- `getArguments()` 產生：
  ```
  --contentdir=<userDir>/uqm-megamod/content
  --configdir=<userDir>/uqm-megamod
  --logfile=<userDir>/uqm-megamod/uqm_log.txt  (若啟用 logging)
  ```
- 把原本 `--log=` 改成 `--logfile=` 對齊 UQM CLI 定義

---

## APK Payload 分析

| 類別 | 檔案數 | 未壓縮 | 已壓縮 | 說明 |
|---|---:|---:|---:|---|
| zh-TW content | 4 | 63.7 MB | 63.2 MB | `.uqm` noCompress ✓ |
| DEX | 6 | 28.0 MB | 10.8 MB | Compose Multiplatform 佔大部分 |
| Native libs | 4 | 18.7 MB | 6.7 MB | libSDL2 + libUrQuanMasters + libc++_shared + libandroidx.graphics.path |
| Resources | 357 | 0.3 MB | 0.2 MB | Compose theme + launcher icon |
| Other | 13 | 0.8 MB | 0.8 MB | AndroidManifest + KM metadata |
| META-INF | 76 | 0.02 MB | 0.02 MB | dependency version stamps |
| **總計** | 460 | 111.5 MB | **81.8 MB** | side-load 完全無壓力 |

---

## 執行期資料流

```
啟動 MainActivity
  ↓
extractionState = Extracting("preparing", 0)
  ↓
coroutine (IO) — UqmContentExtractor.ensureExtracted(context, contentDir) { progress → state.value = Extracting(...) }
  ↓
extractionState = Ready
  ↓
User 按 Start Game
  ↓
Context.startGame(loggingEnabled, contentPath, userPath)
  ↓ Intent extras: content_dir, user_dir, logging_enabled
  ↓
EngineActivity.onCreate 讀 extras
  ↓
EngineActivity.getArguments() 產出 ["--contentdir=<contentPath>", "--configdir=<userPath>"]
  ↓ SDL2Activity.nativeSetupJNI (via SDL_main)
  ↓
libUrQuanMasters.so 的 SDL_main(argc, argv) 收到參數
  ↓ getopt_long 解析
  ↓
options.contentDir = <contentPath>
options.configDir = <userPath>
  ↓
prepareContentDir + prepareConfigDir
  ↓
UIO mounts:
  <contentPath>/packages/mm-0.8.5-content.uqm  ← base pack
  <contentPath>/addons/zh-TW.uqm                ← zh-TW addon (shadow-content 覆蓋)
  ↓
Chinese main menu 出現
```

---

## Patches 存檔

放到 `uqm-work/patches/` 沿用既有 pattern：

- **015-android-content-staging.patch** — `build.gradle.kts`（Copy task + noCompress + srcDir）
- **016-android-launcher-content-extract.patch** — `App.kt` + `MainActivity.kt` + `EngineActivity.kt` 的改動
- **017-android-uqm-content-extractor.patch** — 新檔 `UqmContentExtractor.kt`

---

## 尚未完成 · 進到 Stage 4 前必知

1. **APK 沒實測開機** — 只驗證了打包正確。可能踩的雷：
   - `UIO` 可能不喜歡 `getExternalFilesDir()` 底下的 `.uqm` 路徑（emu 上路徑會像 `/storage/emulated/0/Android/data/org.megamod.uqm/files/uqm-megamod/content/`）
   - Zip64 EOCD parsing（patch 007）在 arm64 首次跑實測
   - `SDL_main` 收到參數的 argv[0] 是否 SDL Activity 有塞（會影響 `prepareContentDir` 的 fallback）
   - Compose UI 從 launcher 過渡到 EngineActivity 時是否有 GL context 衝突
2. **觸控 UI 完全沒有** — Stage 4 才做
3. **生命週期沒處理** — 切背景會可能 crash

## 下一步（推薦）

**先在 emulator 或實機做一次 smoke test**：
```powershell
$env:JAVA_HOME = 'Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1'
$env:ANDROID_HOME = 'Q:\Dos_G\StarControl2\Android\sdk'
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\emulator;C:\msys64\usr\bin;$env:Path"
# 開 emulator
emulator -avd uqm_test_arm64 -no-snapshot-load
# 另一個 pwsh：裝 APK
adb install -r Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\composeApp\build\outputs\apk\debug\composeApp-debug.apk
# 開啟 app + 看 logcat
adb logcat -c
adb shell am start -n org.megamod.uqm/.MainActivity
adb logcat *:E UqmContentExtractor:D SDL:D | Select-Object -First 200
```

Smoke test 通過（能開機到主選單）→ **Stage 4 · 觸控 overlay**。若失敗（多半在 UIO mount 或 SDL_main） → 根據 logcat 精修。
