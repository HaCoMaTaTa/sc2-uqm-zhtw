# =====================================================================
# build_pc.ps1 — 一鍵產生 PC 中文化 zip
#
# 前置條件：
#   1. 已跑過 setup_upstream.ps1（../UQM-MegaMod/ 內含 patched source）
#   2. UQM-MegaMod exe 已 build 過（見 ../docs/SOP_Rebuild_And_Release.md）
#   3. MegaMod 已安裝到 ../uqm-work/install/（或指定 -InstallDir）
#
# 用法：
#   .\scripts\build_pc.ps1                       # 預設版本 = 今天日期
#   .\scripts\build_pc.ps1 -Version v1.0.13 -Execute
# =====================================================================

[CmdletBinding()]
param(
    [string]$Version = ("v" + (Get-Date -Format 'yyyyMMdd')),
    [string]$InstallDir,
    [switch]$Execute,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir
$pipeline  = Join-Path $repoRoot 'pipeline'

Write-Host ""
Write-Host "=== Build PC release ===" -ForegroundColor Cyan
Write-Host "Repo root:    $repoRoot"
Write-Host "Pipeline:     $pipeline"
Write-Host "Version:      $Version"

# ---- 檢查 pipeline 存在 ---------------------------------------------
if (-not (Test-Path $pipeline)) {
    Write-Error "找不到 pipeline/。請確認 repo 結構正確。"
    exit 1
}

# ---- 檢查 install/ 存在（相對於 pipeline）---------------------------
Push-Location $pipeline
try {
    if (-not $InstallDir) { $InstallDir = Join-Path $pipeline 'install' }
    if (-not (Test-Path $InstallDir)) {
        Write-Host ""
        Write-Host "⚠ 找不到 install/ 目錄: $InstallDir" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "首次使用請先："
        Write-Host "  1. 從 https://github.com/JHGuitarFreak/UQM-MegaMod/releases 下載 mm-0.8.5-installer.exe"
        Write-Host "  2. 執行安裝，目標指向 $InstallDir"
        Write-Host "  3. 或用 pipeline/download_megamod.ps1（若你有本地 tool）"
        Write-Host ""
        exit 1
    }

    # ---- Step 0/1: build + package -----------------------------------
    Write-Host ""
    Write-Host "→ Step 1: build_zh-TW.ps1 (JSON → shadow content + rasterize)" -ForegroundColor Cyan
    if ($Execute) {
        & (Join-Path $pipeline 'build_zh-TW.ps1')
        if ($LASTEXITCODE -ne 0) { throw "build_zh-TW.ps1 失敗" }
    } else {
        Write-Host "  (DryRun) 未執行" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "→ Step 2: package_zh-TW.ps1 (shadow content → zh-TW.uqm)" -ForegroundColor Cyan
    if ($Execute) {
        & (Join-Path $pipeline 'package_zh-TW.ps1') -SkipBuild
        if ($LASTEXITCODE -ne 0) { throw "package_zh-TW.ps1 失敗" }
    } else {
        Write-Host "  (DryRun) 未執行" -ForegroundColor Yellow
    }

    # ---- Step 3: 完整 release zip ------------------------------------
    Write-Host ""
    Write-Host "→ Step 3: _release_full_zh-TW.ps1 -Version $Version" -ForegroundColor Cyan
    $releaseArgs = @('-Version', $Version)
    if ($Execute) { $releaseArgs += '-Execute' }
    if ($Force)   { $releaseArgs += '-Force' }
    & (Join-Path $pipeline '_release_full_zh-TW.ps1') @releaseArgs
    if ($LASTEXITCODE -ne 0) { throw "_release_full_zh-TW.ps1 失敗" }
} finally { Pop-Location }

# ---- Step 4: 顯示產物 -----------------------------------------------
$outputDir = Join-Path $pipeline 'release\output'
if (Test-Path $outputDir) {
    Write-Host ""
    Write-Host "=== 產物 ===" -ForegroundColor Cyan
    Get-ChildItem $outputDir -Filter "SC2-zhTW-$Version*" | Select-Object Name, @{n='MB';e={[math]::Round($_.Length/1MB,2)}}, LastWriteTime | Format-Table -AutoSize
    Write-Host ""
    Write-Host "上傳到 GitHub Releases："
    Write-Host "  gh release create $Version --title '繁中版 $Version' --draft"
    Write-Host "  gh release upload $Version $outputDir\SC2-zhTW-$Version.zip $outputDir\SC2-zhTW-$Version.zip.sha256"
}
