# =====================================================================
# first_time_setup.ps1 — 新機器環境檢查（不改動系統，只回報）
#
# 檢查 clone repo 後這台機器是否具備：
#   - Git
#   - Python 3.10+
#   - MSYS2 MINGW32（給 PC build 用）
#   - Android SDK / NDK r27d（給 Android build 用）
#   - JDK 21（給 Android build 用）
#   - MegaMod 遊戲安裝（給 PC build 用）
#
# 用法：
#   .\scripts\first_time_setup.ps1
# =====================================================================

[CmdletBinding()]
param()

$ErrorActionPreference = 'Continue'

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir

Write-Host ""
Write-Host "=== First-Time Setup Checker ===" -ForegroundColor Cyan
Write-Host "Repo root: $repoRoot"
Write-Host ""

$results = @()
function Test-Item($name, $test, $installHint) {
    Write-Host "→ $name..." -NoNewline
    $ok = & $test
    if ($ok) {
        Write-Host " ✔" -ForegroundColor Green
        $script:results += [pscustomobject]@{ Item = $name; Status = 'OK'; Hint = '' }
    } else {
        Write-Host " ✗" -ForegroundColor Red
        $script:results += [pscustomobject]@{ Item = $name; Status = 'MISSING'; Hint = $installHint }
    }
}

# ---- 基本工具 -------------------------------------------------------
Test-Item 'Git' { [bool](Get-Command git -ErrorAction SilentlyContinue) } 'https://git-scm.com/download/win'
Test-Item 'Python 3.10+' {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { return $false }
    $v = (python -c 'import sys; print(sys.version_info.major*100+sys.version_info.minor)' 2>$null)
    return ([int]$v -ge 310)
} 'https://python.org/downloads/'

# ---- PC build tools ------------------------------------------------
Test-Item 'MSYS2 (C:\msys64)' { Test-Path 'C:\msys64\usr\bin\bash.exe' } 'https://www.msys2.org/'
Test-Item 'MinGW32 gcc' { Test-Path 'C:\msys64\mingw32\bin\gcc.exe' } 'MSYS2 安裝後跑: pacman -S mingw-w64-i686-toolchain'
Test-Item 'CMake (MinGW32)' { Test-Path 'C:\msys64\mingw32\bin\cmake.exe' } 'MSYS2: pacman -S mingw-w64-i686-cmake'
Test-Item 'Ninja (MinGW32)' { Test-Path 'C:\msys64\mingw32\bin\ninja.exe' } 'MSYS2: pacman -S mingw-w64-i686-ninja'

# ---- Android build tools -------------------------------------------
Test-Item 'JAVA_HOME (Adoptium Temurin 21)' {
    $jh = $env:JAVA_HOME
    if (-not $jh) { return $false }
    if (-not (Test-Path "$jh\bin\java.exe")) { return $false }
    $ver = & "$jh\bin\java.exe" -version 2>&1 | Out-String
    return ($ver -match '"21\.')
} 'https://adoptium.net/temurin/releases/?version=21'

Test-Item 'ANDROID_HOME (SDK)' {
    $sdk = $env:ANDROID_HOME
    return $sdk -and (Test-Path "$sdk\platform-tools\adb.exe")
} 'Android Studio SDK Manager 安裝 SDK, 設 ANDROID_HOME 環境變數'

Test-Item 'NDK r27d LTS' {
    $sdk = $env:ANDROID_HOME
    return $sdk -and (Test-Path "$sdk\ndk\27.2.12479018")
} 'Android SDK Manager → NDK 27.2.12479018'

# ---- Upstream MegaMod ----------------------------------------------
$upstream = Join-Path (Split-Path -Parent $repoRoot) 'UQM-MegaMod'
Test-Item "UQM-MegaMod ($upstream)" {
    (Test-Path $upstream) -and (Test-Path (Join-Path $upstream '.git'))
} "跑 .\scripts\setup_upstream.ps1 -Execute"

# ---- MegaMod 遊戲安裝（給 PC build）--------------------------------
$installDir = Join-Path $repoRoot 'pipeline\install'
Test-Item "MegaMod 遊戲安裝 ($installDir)" {
    Test-Path (Join-Path $installDir 'UrQuanMasters.exe')
} '下載 mm-0.8.5-installer.exe → 安裝到 pipeline/install/'

# ---- 總結 ----------------------------------------------------------
Write-Host ""
Write-Host "=== 總結 ===" -ForegroundColor Cyan
$results | Format-Table -AutoSize
$missing = $results | Where-Object Status -eq 'MISSING'
if ($missing.Count -eq 0) {
    Write-Host "全部通過！可以開始使用。" -ForegroundColor Green
    Write-Host ""
    Write-Host "PC build:      .\scripts\build_pc.ps1 -Execute"
    Write-Host "Android build: .\scripts\build_android.ps1"
} else {
    Write-Host "有 $($missing.Count) 個項目缺失。安裝指引：" -ForegroundColor Yellow
    Write-Host ""
    foreach ($m in $missing) {
        Write-Host "  ▸ $($m.Item)" -ForegroundColor Yellow
        Write-Host "    → $($m.Hint)"
    }
    Write-Host ""
    Write-Host "詳細 SOP: docs/SOP_Rebuild_And_Release.md"
}
