# 階段 0 · Gradle sync 紀錄（首次成功）

> 日期：2026-08-22
> 環境：Windows 11 · PowerShell 7.6.5
> Gradle Wrapper：8.14.3
> Android Studio：Meerkat 2026.1.3.7 · Product 261.26222.65.0-AI
> Kotlin：2.3.0（`libs.versions.toml`）
> AGP：8.11.2
> Compose Multiplatform：1.9.3
> NDK：27.2.12479018（r27d LTS）· 27.0.12077973（bundled）
> CMake：3.22.1

---

## 首次 sync（失敗）

**Command**：
```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'  # ← JBR 25
.\gradlew.bat --no-daemon tasks --console=plain
```

**Result**：`BUILD FAILED in 31s`

**錯誤訊息**：
```
FAILURE: Build failed with an exception.

* What went wrong:
25.0.2
```

**診斷**：
- Android Studio Meerkat 內建的 JBR 版本是 **OpenJDK 25.0.2**
- Gradle 8.14.3 release notes 只寫「Java 24 support」→ Java 25 未被支援
- Gradle 拿到 Java 版本字串 `25.0.2` 直接當 exception message 拋出（訊息不友善但根因清楚）

**已考慮的解法**：

| 方案 | 優點 | 缺點 | 採用 |
|---|---|---|---|
| A. 升級 Gradle wrapper 到 9.x | 用 Studio JBR，環境簡單 | AGP 8.11.2 與 Gradle 9 相容性未驗證 | ✗ |
| B. 裝 JDK 21 LTS（winget） | 主流 Android build 環境 | winget 隱藏 UAC 卡住 | ✗ |
| **C. 裝 JDK 21（Adoptium zip）** | **免 UAC、可攜、隨資料夾走** | 需自設 JAVA_HOME | **✓** |

---

## 第二次 sync（成功）

**變更**：
1. 從 <https://api.adoptium.net/v3/binary/latest/21/ga/windows/x64/jdk/hotspot/normal/eclipse> 下載 Temurin 21 zip（195.6 MB）
2. 解壓到 `Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1\`
3. `[Environment]::SetEnvironmentVariable('JAVA_HOME', $jdk21, 'User')`

**Command**：
```powershell
$env:JAVA_HOME = 'Q:\Dos_G\StarControl2\Android\jdk21\jdk-21.0.12.1+1'
.\gradlew.bat --no-daemon tasks --console=plain
```

**Result**：`BUILD SUCCESSFUL in 2m 39s`

**產生的 tasks**（節錄關鍵項目）：
- `installDebug` — 安裝 debug APK 到裝置
- `installRelease` — 安裝 release APK
- `assembleDebug` / `assembleRelease` — 打包 APK
- `connectedAndroidTest` — 連線裝置測試
- `lint` / `lintDebug` / `lintRelease` — Lint 檢查
- `test` / `testDebugUnitTest` — 單元測試
- `dependencies` / `buildEnvironment` — 依賴顯示
- `javaToolchains` — 顯示偵測到的 JDK

**副產物**：
- `Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\.gradle\` 建立（Gradle cache）
- `Q:\Dos_G\StarControl2\UQM-MegaMod\build\android\local.properties` 已寫入：
  ```
  sdk.dir=Q:\\Dos_G\\StarControl2\\Android\\sdk
  ```

---

## 未觸發但已可用的下一步

Gradle sync 通過只代表 **project 結構、plugin 依賴、SDK 路徑都對**。**Native build（NDK CMake）尚未執行**。

執行 `./gradlew :composeApp:assembleDebug` 才會真的：
1. 下載並解壓 SDL2/其他 native deps（**尚無** — 這是階段 1 的工作）
2. 呼叫 CMake 用 NDK 交叉編譯 `libUrQuanMasters.so`
3. 打包 APK

**因此**：階段 0 已完成，但**尚未證明**引擎 native 端能 build。那是階段 1 的任務。

---

## 記錄到記憶

已將以下重要事實記到 `/memories/repo/uqm-build.md`（如果沒記過）：

- **Android Studio Meerkat 內建 JBR 25 不能跑 Gradle 8.14.x**（Gradle 上限 Java 24）
- **解法**：用 Adoptium Temurin 21 LTS zip，放 `Q:\...\Android\jdk21\`，設 `JAVA_HOME`
- **不要**設 `JAVA_HOME` 到 Studio 的 `jbr\`（雖然 IDE GUI 內建用它 OK，但 CLI Gradle 掛）

---

## 現在狀態

**Stage 0 AC 逐條檢查**：

- [x] Android Studio 可啟動（`studio64.exe` 已在 `Program Files\Android\Android Studio\`）
- [x] Android SDK 安裝在 `Q:\Dos_G\StarControl2\Android\sdk\`
- [x] SDK Manager 已安裝：Platform 34 + 36、Build-Tools 36、NDK r27d、CMake 3.22.1、Emulator
- [x] AVD `uqm_test_arm64` 已建立（Pixel 7 · API 34 · arm64-v8a · google_apis）
- [ ] AVD 已開機（未測試 — 可延到階段 4 首次跑 APK 時做）
- [x] Gradle sync 成功（`tasks` 目標通過）
- [x] `_stage0_verify.ps1` 全綠（除 AVD 開機測試外）

**可進入階段 1**。
