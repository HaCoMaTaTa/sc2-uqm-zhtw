# SOP · 完整重建流程（從 clone 到 release）

> 對象：想在另一台電腦重現 PC/Android 中文版的開發者。
> 前置：先跑 [`scripts/first_time_setup.ps1`](../scripts/first_time_setup.ps1) 檢查環境。

---

## 0. 前置環境（Windows）

| 元件 | 版本 | 安裝來源 | 必要性 |
|---|---|---|---|
| Git for Windows | 2.40+ | <https://git-scm.com/> | 必要 |
| Python | 3.10+ | <https://python.org/> | 必要 |
| MSYS2 | 最新 | <https://www.msys2.org/> | PC build 需要 |
| MinGW32 toolchain | pacman: `mingw-w64-i686-{toolchain,cmake,ninja,pkgconf,SDL2,SDL2_mixer,SDL2_net,libpng,zlib,libvorbis,libogg}` | pacman | PC build |
| JDK 21 (Adoptium Temurin) | 21 LTS zip | <https://adoptium.net/> | Android build |
| Android SDK | 平台 34/36 · NDK r27d · CMake 3.22 · build-tools 36 | Android Studio SDK Manager | Android build |
| Android Studio | Meerkat 2026.1.3.7+ | <https://developer.android.com/studio> | Android build（可選）|

環境變數：

```powershell
$env:JAVA_HOME     = 'C:\path\to\jdk-21.0.12.1+1'
$env:ANDROID_HOME  = 'C:\path\to\Android\sdk'
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
```

## 1. Clone 本 repo + Upstream MegaMod

```powershell
git clone https://github.com/<你>/uqm-megamod-zhTW.git
cd uqm-megamod-zhTW
.\scripts\first_time_setup.ps1              # 檢查環境
.\scripts\setup_upstream.ps1 -Execute       # clone MegaMod fork（含全部 34 個 patch 已 commit）
```

`setup_upstream.ps1` 會：
- Clone **你的** UQM-MegaMod fork（URL 於 `patches/UPSTREAM_COMMIT.txt` 內）
- Checkout 該檔記錄的 pinned SHA
- **不套用** `patches/*.patch` — 因為 fork HEAD 已內建全部變動

**重要**：首次使用者若看到「Fork URL 是佔位符」警告，代表專案作者尚未 push
UQM-MegaMod 到 GitHub。見 [`PUSH_UQM_MEGAMOD_FORK.md`](PUSH_UQM_MEGAMOD_FORK.md)。

## 2. Build PC 中文化版

### 2.1 先 build UQM-MegaMod 引擎（一次性）

```powershell
& 'C:\msys64\usr\bin\bash.exe' -lc @"
export MSYSTEM=MINGW32
source /etc/profile
cd /q/path/to/UQM-MegaMod
rm -f CMakeCache.txt build.vars && rm -rf CMakeFiles
cmake . -G Ninja -DUQM_PLATFORM_ACCEL=OFF -DCMAKE_BUILD_TYPE=Release && ninja
"@
```

產出：`UQM-MegaMod/UrQuanMasters.exe`（i386 PE32, 2.6 MB）· `UQM-MegaMod/UrQuanMasters-zip64.exe`（patch 007 版）

### 2.2 下載 MegaMod content pack + 安裝

**下載**（見 [`../pipeline/downloads/README.md`](../pipeline/downloads/README.md)）：
```powershell
cd pipeline
.\download_megamod.ps1 -Preset Minimum       # 或 Recommended
```

**安裝到 install/**（見 [`../pipeline/install/README.md`](../pipeline/install/README.md)）：
```powershell
.\downloads\mm-0.8.5-installer.exe /D=Q:\path\to\uqm-megamod-zhTW\pipeline\install
```

**替換為 patched exe**：
```powershell
Copy-Item ..\UQM-MegaMod\UrQuanMasters-zip64.exe install\UrQuanMasters-zip64.exe -Force
```

### 2.3 解壓 content 到 extracted/

`build_zh-TW.ps1` 需要讀取英文原文（gamestrings.txt / comm/*/*.txt / fonts/*.fon）。
它們在 `mm-0.8.5-content.uqm` 內。

```powershell
# 從已安裝的 install/ 內拿
Expand-Archive -Path install\content\packages\mm-0.8.5-content.uqm -DestinationPath extracted -Force

# 驗證
Test-Path extracted\base\base\gamestrings.txt           # 應為 True
Test-Path extracted\base\base\comm\commander\commander.txt  # 應為 True
Test-Path extracted\base\base\fonts\slab.fon\kerndat.fnt    # 應為 True
```

見 [`../pipeline/extracted/README.md`](../pipeline/extracted/README.md) 完整說明。

### 2.4 一鍵 PC release

```powershell
cd ..  # 回到 repo 根
.\scripts\build_pc.ps1 -Version v1.0.13 -Execute
# → pipeline/release/output/SC2-zhTW-v1.0.13.zip + .sha256
```

腳本會依序：
1. `pipeline\build_zh-TW.ps1` — JSON → shadow content + rasterize 字型（含純度閘）
2. `pipeline\package_zh-TW.ps1` — 打包 zh-TW.uqm
3. `pipeline\_release_full_zh-TW.ps1` — 產最終 zip

## 3. Build Android APK

```powershell
.\scripts\build_android.ps1 -BuildType Release
# → UQM-MegaMod/build/android/composeApp/build/outputs/apk/release/激戰M星雲II-release.apk
```

前置：
- `.\android\keystore.properties.example` 複製為 `..\UQM-MegaMod\build\android\keystore.properties`（放在 UQM-MegaMod 內，因為 Gradle 讀這個路徑）
- 填入你的 keystore 位置 + 密碼（**不要 commit**）

Debug 版無須簽章：
```powershell
.\scripts\build_android.ps1 -BuildType Debug
```

## 4. 中文化改進工作流

### 4.1 修單一 token 譯文
```powershell
# 1. 編輯 pipeline/translations/<race>.zh-TW.json
# 2. 重新 build+package
cd pipeline
.\build_zh-TW.ps1
.\package_zh-TW.ps1
# 3. 遊戲內驗證
cd install
.\UrQuanMasters-zip64.exe --windowed --addon zh-TW --bubblewarp --infinitefuel --logfile game.log
```

### 4.2 深度審視某族
- 讀 `docs/AI_Handoff/memories/audit-policy.md` 6 層 checker
- 用 `docs/AI_Handoff/prompts/Reaudit_Dialogue.md` 開新 AI session

### 4.3 種族全面重譯（Rebuild-Compare）
- 讀 `docs/AI_Handoff/prompts/Rebuild_And_Compare.md`
- 讀 `docs/AI_Handoff/memories/dossier-revision-status.md`

## 5. Release Checklist

```powershell
# 產 SHA256 + 開 VirusTotal
.\scripts\verify_and_scan.ps1 -Files @(
  'C:\path\to\SC2-zhTW-v1.0.13.zip',
  'C:\path\to\激戰M星雲II-v3.8-release.apk'
)
```

半成品報告寫在 `docs/Security_Scan_Report.md`。上傳 VirusTotal 後貼回 URL。

### GitHub Release
```powershell
# 建 release
gh release create v1.0.13 --title '繁中版 v1.0.13' --notes-file CHANGELOG.md --draft

# 上傳附件
gh release upload v1.0.13 SC2-zhTW-v1.0.13.zip SC2-zhTW-v1.0.13.zip.sha256
gh release upload v1.0.13 激戰M星雲II-v3.8-release.apk

# 發佈
gh release edit v1.0.13 --draft=false
```

## 6. 疑難排解對照表

| 症狀 | 起點 |
|---|---|
| Build 失敗：找不到 SDL2 | 檢查 MSYS2 mingw32 pacman 套件 · [uqm-build.md](AI_Handoff/memories/uqm-build.md) |
| 遊戲跑起來全英文 | 檢查是否用 `-zip64.exe` 版本 · [uqm-font-hacks.md § MegaMod UIO Zip64](AI_Handoff/memories/uqm-font-hacks.md) |
| CJK 對話 crash 回主選單 | 空格 wrap 不足 · [uqm-font-hacks.md § comm.c _count_lines](AI_Handoff/memories/uqm-font-hacks.md) |
| lander 掃描報告 hang | patch 008 未套 · [uqm-font-hacks.md § CJK scan report](AI_Handoff/memories/uqm-font-hacks.md) |
| 主選單只有 3 個 item | patch 002 未套 · [uqm-build.md § gamestr.h](AI_Handoff/memories/uqm-build.md) |
| Android build: Java 25.0.2 錯誤 | 沒用 JDK 21 · [android-build.md § CRITICAL JBR 25](AI_Handoff/memories/android-build.md) |
| Android build: format-security 錯誤 | patch 012 未套 |
| APK late crash `TFB_Pure_ConfigureVideo` | patch 018 未套 |
| 星圖 F6 搜尋不吃中文 | patch 031 CJK 別名搜尋 |

更多詳見 [`docs/AI_Handoff/memories/uqm-debugging.md`](AI_Handoff/memories/uqm-debugging.md)。

## 7. Rebuild 完整流程時間估計

| 階段 | 首次 | 增量 |
|---|---|---|
| Clone repo | 30s | - |
| setup_upstream.ps1 | 2m（clone + patches）| 30s（fetch + patches）|
| UQM-MegaMod cmake + ninja | 3m | 30s |
| build_zh-TW.ps1（含 rasterize）| 3m | 30s |
| package_zh-TW.ps1 | 1m | 30s |
| _release_full_zh-TW.ps1 | 30s | 20s |
| **PC 總計** | ~10m | ~2m |
| Android gradle sync + build | 5-10m | ~30s |
| **總計（首次乾淨環境）** | ~20m | ~3m |
