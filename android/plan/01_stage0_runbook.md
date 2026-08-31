# 階段 0 · Runbook（環境準備）

> 主計畫參照：[../00_Porting_Plan.md](../00_Porting_Plan.md) 第 1 章「階段 0：環境準備」
> 使用者決策（2026-08-22）：
> - Android Studio 用 winget 安裝
> - SDK 放 `Q:\Dos_G\StarControl2\Android\sdk\`（節省 C:）
> - 測試目標：Android Studio Emulator（AVD arm64）
> - 目標 Android：**14+ 必須跑得動**；10+ 加分

---

## 完成準則（AC）

- [ ] Android Studio 可啟動、通過首次 setup wizard
- [ ] Android SDK 安裝在 `Q:\Dos_G\StarControl2\Android\sdk\`
- [ ] SDK Manager 已安裝：Platform 34 + Platform 36 + Build-Tools + NDK r27d + CMake 3.22.1+
- [ ] 一個 arm64-v8a AVD 已建立且能開機
- [ ] `Q:\Dos_G\StarControl2\Android\_stage0_verify.ps1` 全綠 PASS
- [ ] 匯入 `UQM-MegaMod/build/android/` 為 Gradle project，Gradle sync 錯誤已記錄到 [../research/03_gradle_sync_errors.md](../research/03_gradle_sync_errors.md)

---

## 步驟 A · 用 winget 安裝 Android Studio

```powershell
# 會出現 UAC 彈窗，同意即可。約 4-5 GB 下載
winget install --exact --id Google.AndroidStudio --accept-source-agreements --accept-package-agreements
```

**預期時間**：10–20 分鐘（視網速）。
**成功徵象**：`C:\Program Files\Android\Android Studio\bin\studio64.exe` 存在。

若 winget 失敗 → fallback：
```powershell
# 從官網下載安裝
Start-Process 'https://developer.android.com/studio'
```

---

## 步驟 B · 首次啟動 Android Studio（Setup Wizard）

1. 開啟 Android Studio（開始選單搜「Android Studio」）
2. 若問 import settings → 選「Do not import」
3. Setup Wizard：
   - Install Type: **Custom**（不要 Standard，我們要挑元件）
   - UI Theme: 隨意
   - **SDK Components Setup**：
     - **Android SDK Location** → **改成 `Q:\Dos_G\StarControl2\Android\sdk\`** ⚠️（關鍵決策）
     - 勾選：
       - `Android SDK Platform` (最新版即可)
       - `Android SDK Build-Tools`
       - **不要**勾選 Android Emulator（此步驟版本可能過舊，稍後從 SDK Manager 裝）
4. 讓它下載完成（第一批 ~1-2 GB）

---

## 步驟 C · 透過 SDK Manager 補齊套件

Android Studio → 右下角 More Actions → SDK Manager
或：Tools → SDK Manager

### SDK Platforms tab
勾選以下並 Apply：
- **Android 14.0 (API 34)** — 基本測試目標
- **Android 15.0 (API 35)** — 若可用
- **Android 16.0 (API 36)** — MegaMod scaffold 用的 compileSdk

### SDK Tools tab
勾選以下（Show Package Details，然後精挑版本）：
- **Android SDK Build-Tools** — 最新版
- **Android SDK Platform-Tools** — 提供 `adb`
- **Android Emulator** — 最新版
- **NDK (Side by side)** — 選 **27.2.12479018**（r27d LTS）
  - 若沒有 r27d，選最接近的 r27.x LTS
- **CMake** — 選 **3.22.1**（MegaMod scaffold 指定版本）
- **Android SDK Command-line Tools** — 提供 `sdkmanager` CLI

Apply → 下載 ~5-8 GB。

---

## 步驟 D · 設定環境變數（PowerShell profile 或系統）

新開 pwsh 執行一次：

```powershell
$sdk = 'Q:\Dos_G\StarControl2\Android\sdk'
[Environment]::SetEnvironmentVariable('ANDROID_HOME', $sdk, 'User')
[Environment]::SetEnvironmentVariable('ANDROID_SDK_ROOT', $sdk, 'User')
$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$toAdd = @(
  "$sdk\platform-tools",
  "$sdk\cmdline-tools\latest\bin",
  "$sdk\emulator"
) | Where-Object { $currentPath -notlike "*$_*" }
if ($toAdd) {
  $newPath = ($currentPath.TrimEnd(';') + ';' + ($toAdd -join ';'))
  [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
  Write-Host "PATH updated. Restart terminal to activate." -ForegroundColor Green
}
```

**JAVA_HOME**：Android Studio 內建 JBR（`C:\Program Files\Android\Android Studio\jbr`）。若要在 CLI 用 `./gradlew`：

```powershell
$jbr = 'C:\Program Files\Android\Android Studio\jbr'
if (Test-Path "$jbr\bin\java.exe") {
  [Environment]::SetEnvironmentVariable('JAVA_HOME', $jbr, 'User')
  Write-Host "JAVA_HOME → $jbr" -ForegroundColor Green
}
```

**重開 pwsh** 讓變數生效。

---

## 步驟 E · 建立測試 AVD（Emulator）

Android Studio → Device Manager (右側工具列) → Create Virtual Device

**注意**：Windows on x86_64 host 跑 arm64 AVD 相對慢（需 translation），但 MegaMod 目前只有 arm64 build。

**推薦配置**：
- **Category**: Phone
- **Device**: Pixel 7 或 Pixel 8（螢幕比例接近現代手機）
- **System Image**:
  - Release: **UpsideDownCake (API 34, Android 14)** 或 **VanillaIceCream (API 35)**
  - ABI: **arm64-v8a** ⚠️（必選；x86_64 不會跑起來，除非 build.gradle 也加 x86_64）
- Emulated Performance: **Hardware — GLES 2.0**

若擔心 arm64 太慢，可另建一個 x86_64 image 作為 UI 除錯用（真正 gameplay 測試最好在**實機**上做——之後可再加）。

---

## 步驟 F · 匯入 UQM-MegaMod Android project

1. Android Studio → File → Open
2. 選 `Q:\Dos_G\StarControl2\UQM-MegaMod\build\android`
3. Trust project → OK
4. 讓 Gradle sync 跑（可能 5–15 分鐘）
5. **無論成功或失敗**，把結果記下來：
   - 成功 → 記在 [../research/03_gradle_sync_errors.md](../research/03_gradle_sync_errors.md) 標示 GREEN
   - 失敗 → 完整貼上錯誤訊息到同檔案

---

## 步驟 G · 執行驗證腳本

```powershell
cd Q:\Dos_G\StarControl2\Android
.\_stage0_verify.ps1
```

全綠即通過階段 0。

---

## 常見卡關與對策

| 徵狀 | 原因 | 對策 |
|---|---|---|
| `winget install` 卡住不下載 | winget source 快取 | `winget source reset --force` 再試 |
| Setup Wizard 卡在 SDK download | 網速太慢或防火牆擋 | 關掉、開 SDK Manager 手動裝 |
| Gradle sync 抓不到套件 | 缺 Kotlin/Compose plugin | 讓 IDE 提示 auto-install |
| Gradle sync 版本衝突 | Kotlin 2.3.0 太新 | 見 `研究 · 已知風險`：可降 Kotlin 2.0.x + AGP 8.5.x |
| AVD 開機黑屏 | GPU 加速未開 | Device Manager 邊上 wrench icon → Graphics → GLES 2.0 |
| adb 找不到裝置 | Emulator 未啟動或 USB debugging 未開 | `adb devices` 檢查 |

---

## 完成後往下

**階段 0 通過** → 進到 [階段 1 · Native lib 交叉編譯](02_stage1_native_libs.md)（尚未撰寫；卡到再寫）。
