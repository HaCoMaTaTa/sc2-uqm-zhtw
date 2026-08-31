# UQM-MegaMod 繁中版 Android 移植計畫

> 版本：v0.1（初稿）
> 日期：2026-08-22
> 目標裝置：Android 10+（arm64-v8a），現代手機
> 移植路徑：**B — 從 MegaMod 主線加 SDL2-Android NDK build 原生移植**
> 分發方式：自用 side-load APK
> 輸入方式：螢幕虛擬搖桿 + 按鈕 overlay

---

## 前言 · 本計畫的三大結論

1. **好消息**：MegaMod 上游已內建 Android build scaffolding（`UQM-MegaMod/build/android/`，含 Kotlin + Compose + SDLActivity JNI wrapper + CMake 條件分支），我們**不需要從零開始**。
2. **中等消息**：這份 scaffolding **從未產出過公開 APK**，最後一次有意義的 commit 在 2026-01（7 個月前），實作完成度約 40%。首次 build 大概率需除錯。
3. **關鍵發現**：所有中文化資產（35 個譯文 JSON、9 個引擎 patch、SD/HD 兩份 addon、字型 rasterize 產物）**100% 平台無關**，可直接搬到 Android 端，**不需要重譯或重打包內容**。核心工作是**打通 native build + 補完 Android app 殼**。

---

## 第 0 章 · 決策總表

| 決策項 | 選擇 | 理由 |
|---|---|---|
| 移植路徑 | **B**（原生 NDK build） | A 沒有現成 APK 可 fork；C（Termux）體驗差 |
| 目標 ABI | **arm64-v8a only** | MegaMod scaffold 已限定；現代手機 100% 支援 |
| Min SDK | **24**（Android 7.0） | MegaMod scaffold 現值；也可考慮升 26 |
| Target SDK | **36**（Android 15） | 現有值，符合 Play 商店要求 |
| SDL 版本 | **SDL2**（不升 SDL3） | UQM 引擎與所有 patch 都相容 SDL2 |
| Content 部署 | **APK assets/ + 首次啟動解壓** | 116 MB 對 side-load OK；不用 scoped storage 特殊權限 |
| USERDIR 路徑 | **`Context.getExternalFilesDir()`** | 免權限、卸載自清 |
| 開發環境 | **Windows 主機 + Android Studio** | 使用者現有工作站已在 Windows |
| 建置系統 | **AGP + Gradle + CMake（既有 scaffold）** | 沿用 MegaMod 已寫好的 build.gradle.kts |
| Native deps | **NDK 交叉編譯 SDL2/libpng/libogg/libvorbis** | 尚無 AAR，需自 build |
| 觸控 UI | **透明 overlay 疊在 SDLSurface 上** | SDL2 沒有內建虛擬搖桿 |
| 引擎 patches | **9 個全套用**（001–011） | 純 C，Android 無相容問題 |
| 簽章 | **本機 keystore + Android Studio signing wizard** | 自用不需 Play 上架簽章 |

---

## 第 1 章 · 分階段任務清單

> 每個階段有明確**驗收條件（AC）**。前一階段 AC 未達成前不進入下一階段。

### 階段 0：環境準備（Prerequisite）

**目標**：Android 開發環境齊備，能開啟 MegaMod Android project。

**任務**：
1. 安裝 **Android Studio** 最新穩定版（2025.2 Meerkat 或後續）
2. 從 SDK Manager 安裝：
   - Android SDK 36（compileSdk）
   - Android SDK 24（minSdk）
   - **NDK r27d LTS**
   - CMake 3.22.1+
3. 匯入 `UQM-MegaMod/build/android/` 為 Gradle project
4. 觸發初次 Gradle sync，記錄所有錯誤 → 存至 `Android/research/03_gradle_sync_errors.md`

**AC**：
- [ ] Android Studio 能開啟專案不 crash
- [ ] Gradle sync 完成或錯誤全部歸類（Kotlin/AGP/SDK 版本、缺失 lib）
- [ ] 準備一部實體測試機或 emulator（arm64 image）

**風險**：Kotlin 2.3.0 + AGP 8.11.2 可能與 Compose 1.9.3 有版本相容性問題（scaffold 7 個月未更新）。若 sync 卡住 → 手動降級到 Kotlin 2.0.x + AGP 8.5.x。

---

### 階段 1：Native lib 交叉編譯（最痛的一關）

**目標**：產出 `libSDL2.so`、`libpng.so`、`libogg.so`、`libvorbis.so`（arm64-v8a）並整合進 Gradle build。

**任務**：
1. **SDL2 for Android**：
   - 從 <https://libsdl.org/download-2.0.php> 抓 SDL2 官方 source
   - 依官方 `docs/README-android.md` 用 NDK 交叉編譯出 arm64 `libSDL2.so`
   - 產物放到 `UQM-MegaMod/build/android/composeApp/src/main/jniLibs/arm64-v8a/`
2. **libpng, libogg, libvorbis, zlib**：
   - 選項 A：從 Android NDK prefab 找（`c++_shared` 已內建，其他不一定有）
   - 選項 B：用 <https://github.com/android/ndk-samples> 或社群 recipe 交叉編譯
   - 選項 C：把源碼加入主 `CMakeLists.txt` 一起 build（最單純但編譯時間長）
3. **修 CMakeLists.txt**（若 Android 條件下 include/link 路徑不完整）
4. 用 Android Studio Gradle 觸發 `:composeApp:assembleDebug`
5. 若失敗 → 逐一收集 CMake / ninja 錯誤到 `Android/research/04_native_build_errors.md`

**AC**：
- [ ] `./gradlew :composeApp:assembleDebug` 成功產出 debug APK
- [ ] APK 內含 `lib/arm64-v8a/libSDL2.so` + `libUrQuanMasters.so`
- [ ] `libUrQuanMasters.so` 內含 `SDL_main` symbol（用 `readelf -a` 檢查）

**風險**：這是最可能卡住的階段。預期會踩到多個 CMake 找不到 header / lib 的問題。

**Fallback**：若卡超過合理時間，改用 <https://github.com/pelya/commandergenius> 的 SDL2 build script 作為模板。

---

### 階段 2：套用 9 個引擎 patch

**目標**：在 MegaMod 主線上套用我們的所有 CJK patch，確認在 Android build 條件下仍可編譯。

**任務**：
1. 從 `uqm-work/patches/` 依序 apply：001, 002, 005, 006, 007, 003, 004, 009, 011
2. Rebuild Android target：`./gradlew :composeApp:assembleDebug`
3. 若某個 patch 破壞 Android build → 分析並隔離（可能 patch 用了 Windows-only header）
4. 特別注意 **patch 007（Zip64）**：Android arm64 是 64-bit off_t，需驗證 zip 結構讀取行為與 Windows i386 一致

**AC**：
- [ ] 9 個 patch 全部 apply 成功
- [ ] Debug APK 仍能 build
- [ ] `libUrQuanMasters.so` 增加合理大小（+ ~50 KB 左右）

**風險**：低。所有 patch 都是純 C 邏輯修改，沒有 Windows API 呼叫。

---

### 階段 3：Content 打包與載入

**目標**：把 content pack + 中文化 addon 部署到 APK / device，讓引擎啟動時能掛載。

**任務**：
1. **內容選擇**：
   - **必要**：`mm-0.8.5-content.uqm`（base game，官方 pack，~40 MB）
   - **必要**：`zh-TW.uqm`（SD 繁中，38 MB）
   - **選配**：`zh-TW-hd.uqm`（HD 繁中，77 MB）— 首發可先不含以壓 APK 到 <150 MB
2. **打包策略**：
   - 把上述 `.uqm` 檔複製到 `build/android/composeApp/src/main/assets/uqm-content/`
   - 在 `MainActivity.kt` 或首次啟動 hook 加入「解壓 assets → `getExternalFilesDir()`」邏輯
   - 或用 `AssetManager.openFd()` 讓 SDL2 直接讀 APK 內容（更輕量但需驗證）
3. **修改 `USERDIR`**：
   - 當前 `config_android.h.in` 硬編碼 `/storage/emulated/0/uqm-megamod/`
   - 改成 JNI 執行期取 `getExternalFilesDir()` 的路徑
   - 具體：新增 JNI helper `Java_org_megamod_uqm_EngineActivity_getUserDir()`，C 端在 `uqm.c` 主 `main` 前呼叫並填入 `options.contentDir`
4. **驗證 zh-TW addon**：
   - 遊戲啟動 log 應看到 `Successfully mounted 'zh-TW.uqm'`
   - 主選單 / 對話應顯示繁中

**AC**：
- [ ] APK 可安裝到裝置（`adb install`）
- [ ] 首次啟動能找到並掛載所有必要 `.uqm`
- [ ] game.log（若可啟用）不再有「Zip64 not supported」或「addon not found」
- [ ] 主選單顯示繁中「新遊戲/載入/設定」等字樣

**風險**：APK size 若超 150 MB Play 商店會擋（自 side-load 無影響但體驗差）。若超標 → 拆 HD addon 為 on-demand 下載。

---

### 階段 4：觸控 overlay 實作

**目標**：手指能操作 UQM 全部功能（星圖、對話選單、Melee 戰鬥、Setup 選單）。

**任務**：
1. 在 `EngineActivity.kt` 的 `engine_activity.xml` layout 上，於 `sdl_container` 之上加透明 `ComposeView`：
   - 左下角虛擬搖桿（4/8/16 方向可配置）
   - 右下角按鈕群組：A（射擊）、B（特殊武器）、Start（暫停）、Escape（返回）
   - 頂端可拉出隱藏工具列（切換 zoom、顯示 log、切 melee scaler）
2. 將 Compose 事件橋接到 SDL：
   - 搖桿位置 → 合成 `SDL_JOYAXISMOTION` 事件（沿用 `gameinp.c:670` 的方向搖桿演算法）
   - 按鈕 → 合成 `SDL_KEYDOWN`/`SDL_KEYUP` 事件（用 UQM keymap 預設鍵）
3. 支援 **透明度 slider**（讓玩家看到底下畫面）
4. 支援 **按鈕位置自訂**（存至 `SettingsManager`）

**參考**：
- `UQM-MegaMod/src/uqm/gameinp.c:670` 起的 `GetDirectionalJoystickInput()` 已內建 16 方向類比→數位轉換
- pelya commandergenius 的螢幕虛擬搖桿實作可作為 UI 佈局參考

**AC**：
- [ ] 星圖能移動游標
- [ ] 對話能選 response
- [ ] Melee 戰鬥能開槍 + 轉向 + 加速
- [ ] Setup 選單能上下移動 + Enter 確認 + Escape 返回

**風險**：Melee 戰鬥 16 方向轉向精度不足會讓玩家挫折。分階段驗收：先 4 方向能動，再優化到 16 方向。

---

### 階段 5：生命週期與穩定性

**目標**：切換應用、鎖屏、旋轉螢幕都不 crash。

**任務**：
1. 在 SDLActivity 監聽 pause/resume：
   - `SDL_APP_WILLENTERBACKGROUND`：儲存當前 GL state
   - `SDL_APP_DIDENTERFOREGROUND`：重載紋理
2. `AndroidManifest.xml` 中 `EngineActivity` 已設 `configChanges="keyboardHidden|orientation"` + `screenOrientation="landscape"` → OK
3. 加入 crash reporting（可選，用 Firebase Crashlytics 或本地 log）
4. 加入權限自動請求（`MANAGE_EXTERNAL_STORAGE` 若走硬編碼路徑，否則可省）
5. 若首次啟動需解壓 assets → 加 progress bar UI

**AC**：
- [ ] 遊戲中按 Home → 回來能繼續（無 crash）
- [ ] 螢幕轉正/橫向不 crash
- [ ] 存檔功能正常（save/load slot）

**風險**：中。UQM engine 對 GL context loss 沒有原生處理，可能需要在 SDL2 pause 事件時強制存檔。

---

### 階段 6：字型與 UI 縮放驗收

**目標**：Fusion Pixel 8/10/12 px 在手機螢幕上仍可讀。

**任務**：
1. 在測試機上實測所有種族對話
2. 星圖 hover 標籤、Setup 選單、cargo 面板逐一驗收
3. 若某些字型過小 → 從 addon 內替換為 12/14px 版本（重跑 rasterize）
4. HD mode 若啟用需一併驗收（`zh-TW-hd.uqm`）

**AC**：
- [ ] 星圖 hover 看得清
- [ ] 對話能讀完不感疲勞
- [ ] Setup 選單所有選項可辨識

**風險**：低。手機 DPI 通常高於桌面，反而字更清晰。

---

### 階段 7：簽章與部署

**目標**：產生可分發的 signed APK。

**任務**：
1. 用 Android Studio 建立 keystore（自用一輩子那把）
2. `./gradlew :composeApp:assembleRelease` 產出 signed APK
3. 用 `apksigner verify` 驗證簽章
4. `adb install release.apk` 實測
5. 打包到 `Q:\Dos_G\StarControl2\Android\release\` 存檔

**AC**：
- [ ] Release APK 可裝、可跑
- [ ] 檔案 <= 150 MB（若不含 HD addon）或 <= 300 MB（若含 HD addon）
- [ ] 存好 keystore 到 `Android/release/keystore/`（**加入 .gitignore！**）

---

## 第 2 章 · 建議實作順序與里程碑

```
Milestone A（能跑 hello world）：階段 0 → 1
    → 產出：能安裝、開啟不 crash 的 debug APK（畫面可能全黑）

Milestone B（能玩英文版）：階段 2 → 3（不含 zh-TW addon） → 5
    → 產出：能操作、能存讀檔的英文 UQM

Milestone C（能玩繁中版）：階段 3（+ zh-TW） → 6
    → 產出：全繁中對話可讀

Milestone D（可分發）：階段 4 → 7
    → 產出：手指能玩、signed release APK
```

**關鍵決策點**：
- 到 Milestone A 卡住 → 考慮轉向 pelya commandergenius 分支
- 到 Milestone B 但 addon 掛載失敗 → 深入 patch 007 除錯或改變 content 部署策略
- 到 Milestone C 但字太小 → 重跑 HD rasterize（不影響 build 系統）
- 到 Milestone D 但觸控體驗差 → 保留藍牙手把 fallback（SDL2 已支援）

---

## 第 3 章 · 工具鏈需求

### 3.1 主機環境（Windows）

| 元件 | 版本 | 安裝方式 |
|---|---|---|
| Android Studio | 2025.2 Meerkat 或後續 | <https://developer.android.com/studio> |
| Android SDK | Platform 24 + 36 | Android Studio SDK Manager |
| Android NDK | r27d LTS | Android Studio SDK Manager |
| CMake | 3.22.1+ | Android Studio SDK Manager |
| Java | JDK 17+ | Android Studio 內建或 <https://adoptium.net> |
| Git | 已有 | 已裝 |
| Python 3.11+ | 已有 | 已裝（用於 rasterize、patch apply script） |

### 3.2 額外元件（需要交叉編譯的原始碼）

| 元件 | 版本 | 位置 |
|---|---|---|
| SDL2 source | 2.30.x 或 2.32.x | <https://libsdl.org/download-2.0.php> |
| SDL2_mixer source | 2.8.x | <https://github.com/libsdl-org/SDL_mixer/releases> |
| libpng | 1.6.40+ | <http://www.libpng.org/pub/png/libpng.html> |
| libogg | 1.3.5+ | <https://xiph.org/downloads/> |
| libvorbis | 1.3.7+ | <https://xiph.org/downloads/> |

**放置位置**：`Q:\Dos_G\StarControl2\Android\references\src\`

### 3.3 測試裝置

- **必要**：一部 arm64 Android 10+ 實體手機（emulator arm64 image 也可但慢）
- **建議**：`adb` USB debugging 打開
- **選配**：藍牙手把測試（驗證非觸控輸入 fallback）

---

## 第 4 章 · 中文化資產如何注入 APK

### 4.1 檔案清單（依優先順序）

```
必要（隨 APK 一起）：
  install/content/packages/mm-0.8.5-content.uqm    (~40 MB, base game)
  install/content/addons/zh-TW.uqm                  (38 MB, SD 繁中)

選配（首次啟動時下載或分別安裝）：
  install/content/addons/zh-TW-hd.uqm               (77 MB, HD 繁中)
  install/content/addons/mm-hd/                     (HD 圖像 pack)
  install/content/addons/3do-mode-*                 (3DO 音樂/圖)
```

### 4.2 打包實作草案（Gradle）

```kotlin
// build.gradle.kts (composeApp/)
android {
    sourceSets {
        getByName("main") {
            assets.srcDirs("src/main/assets", "../../../../uqm-work/install/content")
        }
    }
}
```

或用 Copy task：

```kotlin
tasks.register<Copy>("copyContent") {
    from("../../../uqm-work/install/content") {
        include("packages/mm-0.8.5-content.uqm")
        include("addons/zh-TW.uqm")
    }
    into("src/main/assets/uqm-content")
}
tasks.named("preBuild") { dependsOn("copyContent") }
```

### 4.3 執行期路徑改寫

**方案 A（推薦）：首次啟動解壓 assets → external files dir**

```kotlin
// MainActivity.kt onCreate:
val userDir = File(getExternalFilesDir(null), "uqm-megamod")
if (!File(userDir, ".initialized").exists()) {
    // Extract assets/uqm-content/* to userDir/content/
    assets.list("uqm-content")?.forEach { copyAssetTree(it, userDir) }
    File(userDir, ".initialized").createNewFile()
}
// 把 userDir 路徑傳給 EngineActivity via Intent extra
intent.putExtra("user_dir", userDir.absolutePath)
```

**方案 B（進階）：JNI 直接讀 APK assets**

- 用 `AAssetManager` 讓 UIO 直接從 APK 讀 `.uqm`
- 好處：不佔 external 空間、首次啟動快
- 壞處：需修改 UIO 的 zip 掛載邏輯，工程量大

**建議先做方案 A**，穩定後再考慮 B。

### 4.4 字型 fallback 策略

- 若 zh-TW addon 掛載失敗 → 自動退回英文（不 crash）
- 若某個 CJK 字元 PNG 缺失 → 引擎現有 fallback（顯示白色小方塊，不 crash）
- 手機端不需要額外 fallback 邏輯，因為 Windows 端已驗證

---

## 第 5 章 · 未解問題與後續決策點

以下項目**在動手時**才有意義判斷，先列出來以便追蹤：

1. **Q1**：是否要一併打包 HD addon（`zh-TW-hd.uqm`, 77 MB）到首發 APK？
   - **暫定**：不。首發只有 SD。HD 之後做 asset pack。
2. **Q2**：APK 若超 150 MB 是否 side-load 有問題？
   - **暫定**：否，side-load 沒硬限，但拆 HD 為 optional download 較好。
3. **Q3**：需不需要支援藍牙手把？
   - **依 user 回答**：已回覆「螢幕虛擬搖桿為主」→ 藍牙手把當 bonus，SDL2 內建即用。
4. **Q4**：`SETUP MENU` 是否要保留桌面版所有選項？
   - **暫定**：保留所有選項（Android build 已在 setupmenu.c 有條件分支）。
5. **Q5**：存檔要不要能 export / import（避免卸載遺失）？
   - **暫定**：先不做。用 `getExternalFilesDir()` 卸載會清但比較「乾淨」。之後可加 export UI。
6. **Q6**：語系是否只鎖繁中，還是允許切英文？
   - **暫定**：允許。addon 是可選掛載，SETUP 中可關。

---

## 第 6 章 · 目錄結構（本工作區）

```
Q:\Dos_G\StarControl2\Android\
├── 00_Porting_Plan.md           # 本檔
├── plan/                        # 之後細部子計畫（觸控 UI 設計、Gradle patch 細節等）
├── research/
│   ├── 01_upstream_survey.md    # 上游 Android 移植現況（Web 調查）
│   ├── 02_local_findings.md     # 本地中文化專案盤點
│   └── (執行過程中補寫的錯誤記錄)
├── references/                  # 下載的 SDL2 / libpng 等 source
│   └── src/
└── release/                     # 最終 APK + keystore（keystore 加 .gitignore）
```

---

## 附錄 A · 重要引用

- MegaMod Android scaffold：`UQM-MegaMod/build/android/`
- MegaMod CMakeLists Android 分支：`UQM-MegaMod/CMakeLists.txt:27, 76`
- Android config template：`UQM-MegaMod/src/config_android.h.in`
- Android SDL_main override：`UQM-MegaMod/src/uqm.c:69`
- Android joystick 演算法：`UQM-MegaMod/src/uqm/gameinp.c:674` (upstream: pelya/commandergenius)
- Android melee zoom：`UQM-MegaMod/src/uqm/setupmenu.c:230`
- 引擎 patches：`uqm-work/patches/README.md`
- 字型與打包腳本：`uqm-work/build_zh-TW.ps1`, `package_zh-TW.ps1`
- 中文化技術筆記：`/memories/repo/uqm-*.md`

---

## 附錄 B · 本計畫的邊界

**本計畫不涵蓋**：
- Google Play 上架流程（自用 side-load 不需要）
- iOS 移植
- Netplay / online multiplayer 在 Android 的驗證
- Achievement / 雲存檔整合
- Xbox controller Bluetooth 特殊配對邏輯（SDL2 內建應該夠用）

**本計畫的假設**：
- 使用者現有 Windows 開發機能安裝 Android Studio 與 NDK（磁碟 ~10 GB）
- 使用者能提供一部 arm64 Android 10+ 的測試手機
- MegaMod 上游 v0.8.5 不會在移植期間有 breaking change（v0.8.5 是本次 baseline）

---

## 下一步

進到「動手」階段時，建議：

1. **先讀完本計畫全文 + `research/01_upstream_survey.md` + `research/02_local_findings.md`**
2. **確認第 5 章的 Q1–Q6 決策**（可直接回覆本 chat）
3. **從階段 0 開始執行**（安裝 Android Studio + NDK）
4. **一次只做一個階段，達成 AC 再往下**

若中途卡住，可以問我：
- 「幫我 debug 這個 Gradle 錯誤」
- 「怎麼把 patch 007 apply 到 Android build」
- 「觸控搖桿的 Compose overlay 怎麼寫」
- ……等等

**現在請確認**：
- 是否同意本計畫的整體方向與階段切分？
- 第 5 章 Q1–Q6 有任何要現在就先鎖定的嗎？
- 何時開始執行階段 0（可以隨時通知我）？
