# =====================================================================
# build_android.ps1 — 一鍵 build Android APK
#
# 前置條件（見 ../docs/AI_Handoff/memories/android-build.md）：
#   1. 已跑過 setup_upstream.ps1（../UQM-MegaMod/ 內含 patched source）
#   2. Android SDK 已安裝（含 NDK r27d, platform-tools, build-tools 36, platforms 34/36）
#   3. JDK 21 已安裝（Adoptium Temurin 21）
#   4. MSYS2 已安裝於 C:\msys64（bash 需在 PATH）
#   5. keystore.properties 已設好（複製 ../android/keystore.properties.example）
#
# 用法：
#   .\scripts\build_android.ps1                          # release + debug 雙產出
#   .\scripts\build_android.ps1 -BuildType Release
#   .\scripts\build_android.ps1 -Clean                   # 加 clean
# =====================================================================

[CmdletBinding()]
param(
    [ValidateSet('Debug','Release','Both')]
    [string]$BuildType = 'Both',
    [switch]$Execute,      # 未指定則 DryRun
    [switch]$Clean,
    [string]$UqmMegaModPath,
    [string]$AndroidSdk,
    [string]$JavaHome,
    [string]$Msys64 = 'C:\msys64'
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir

if (-not $UqmMegaModPath) {
    $UqmMegaModPath = Join-Path (Split-Path -Parent $repoRoot) 'UQM-MegaMod'
}
if (-not $AndroidSdk) { $AndroidSdk = $env:ANDROID_HOME }
if (-not $JavaHome)   { $JavaHome   = $env:JAVA_HOME }

Write-Host ""
Write-Host "=== Build Android APK ===" -ForegroundColor Cyan
Write-Host "UQM-MegaMod:   $UqmMegaModPath"
Write-Host "ANDROID_HOME:  $AndroidSdk"
Write-Host "JAVA_HOME:     $JavaHome"
Write-Host "MSYS2:         $Msys64"
Write-Host "BuildType:     $BuildType"
if (-not $Execute) {
    Write-Host "Mode:          DryRun (加 -Execute 才實跑)" -ForegroundColor Yellow
} else {
    Write-Host "Mode:          Execute" -ForegroundColor Green
}
Write-Host ""

# ---- 檢查 ----------------------------------------------------------
if (-not (Test-Path $UqmMegaModPath)) {
    Write-Error "找不到 UQM-MegaMod 路徑：$UqmMegaModPath`n請先跑 setup_upstream.ps1"
    exit 1
}
if (-not $AndroidSdk -or -not (Test-Path $AndroidSdk)) {
    Write-Error "找不到 Android SDK。請設 -AndroidSdk 或環境變數 ANDROID_HOME"
    exit 1
}
if (-not $JavaHome -or -not (Test-Path $JavaHome)) {
    Write-Error "找不到 Java 21。請設 -JavaHome 或環境變數 JAVA_HOME"
    exit 1
}
$msysBash = Join-Path $Msys64 'usr\bin\bash.exe'
if (-not (Test-Path $msysBash)) {
    Write-Host "⚠ MSYS2 bash 不在 $msysBash — CMake 呼叫 sh 可能失敗" -ForegroundColor Yellow
}

# ---- 設環境變數 ----------------------------------------------------
$env:ANDROID_HOME     = $AndroidSdk
$env:ANDROID_SDK_ROOT = $AndroidSdk
$env:JAVA_HOME        = $JavaHome
$paths = @(
    "$env:JAVA_HOME\bin",
    "$env:ANDROID_HOME\platform-tools",
    "$env:ANDROID_HOME\cmdline-tools\latest\bin",
    "$env:ANDROID_HOME\emulator",
    "$Msys64\usr\bin"
)
$env:Path = ($paths -join ';') + ";$env:Path"

# ---- Gradle build -------------------------------------------------
$androidProj = Join-Path $UqmMegaModPath 'build\android'
if (-not (Test-Path $androidProj)) {
    Write-Error "找不到 Android project：$androidProj"
    exit 1
}

Push-Location $androidProj
try {
    $tasks = @()
    if ($BuildType -in 'Debug','Both')   { $tasks += ':composeApp:assembleDebug' }
    if ($BuildType -in 'Release','Both') { $tasks += ':composeApp:assembleRelease' }

    if (-not $Execute) {
        Write-Host "(DryRun) 略過 gradle 執行。真跑會做以下動作：" -ForegroundColor Yellow
        if ($Clean) { Write-Host "  gradlew clean --console=plain" }
        Write-Host "  gradlew --no-daemon $($tasks -join ' ') --console=plain"
        Write-Host ""
        Write-Host "（首次執行約 5-10 分鐘 · 增量 rebuild ~30 秒）"
        Pop-Location
        return
    }

    if ($Clean) {
        Write-Host "→ gradlew clean" -ForegroundColor Cyan
        .\gradlew.bat clean --console=plain
    }

    Write-Host "→ gradlew $($tasks -join ' ')" -ForegroundColor Cyan
    .\gradlew.bat --no-daemon @tasks --console=plain
    if ($LASTEXITCODE -ne 0) { throw "gradle build 失敗" }
} finally { Pop-Location }

# ---- 產物 ---------------------------------------------------------
$stamp = Get-Date -Format 'yyyyMMdd_HHmm'
$outDir = "$repoRoot\..\release"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

Write-Host ""
Write-Host "=== 產物 ===" -ForegroundColor Cyan
$apkGlob = Join-Path $androidProj 'composeApp\build\outputs\apk\*\*.apk'
$apks = Get-ChildItem $apkGlob -ErrorAction SilentlyContinue
if ($apks) {
    foreach ($apk in $apks) {
        Write-Host ("  {0,-60} {1,8:N1} MB" -f $apk.Name, ($apk.Length/1MB)) -ForegroundColor Green
    }
    Write-Host ""
    Write-Host "上傳到 GitHub Releases：" -ForegroundColor Yellow
    Write-Host "  gh release upload <tag> $($apks[0].FullName)"
} else {
    Write-Host "⚠ 找不到 APK 產物" -ForegroundColor Yellow
}
