# =====================================================================
# setup_upstream.ps1
# 一鍵準備 UQM-MegaMod upstream source tree，並套用本 repo 的引擎 patches。
#
# 使用方式：
#   .\scripts\setup_upstream.ps1                 # 預設 DryRun（只列出動作）
#   .\scripts\setup_upstream.ps1 -Execute        # 實跑
#   .\scripts\setup_upstream.ps1 -Execute -Force # 已存在 UQM-MegaMod 也強制重跑（重置本地變更）
#   .\scripts\setup_upstream.ps1 -Execute -TargetPath 'D:\my\path\UQM-MegaMod'
#
# 產物：<repo_root>/../UQM-MegaMod/ 或 -TargetPath 指定路徑
#       內容 = upstream commit (見 patches/UPSTREAM_COMMIT.txt) + 本 repo 34 個 patch
# =====================================================================

[CmdletBinding()]
param(
    [switch]$Execute,
    [switch]$Force,
    [string]$TargetPath,
    [string]$UpstreamUrl = 'https://github.com/JHGuitarFreak/UQM-MegaMod.git'
)

$ErrorActionPreference = 'Stop'

# ---- 定位路徑 -------------------------------------------------------
$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir
if (-not $TargetPath) {
    $TargetPath = Join-Path (Split-Path -Parent $repoRoot) 'UQM-MegaMod'
}

Write-Host ""
Write-Host "=== UQM-MegaMod upstream setup ===" -ForegroundColor Cyan
Write-Host "Repo root:    $repoRoot"
Write-Host "Target path:  $TargetPath"
Write-Host "Upstream URL: $UpstreamUrl"
if (-not $Execute) {
    Write-Host "Mode:         DryRun (加 -Execute 才實跑)" -ForegroundColor Yellow
} else {
    Write-Host "Mode:         Execute" -ForegroundColor Green
}
Write-Host ""

# ---- 檢查 git 可用 --------------------------------------------------
$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Write-Error "找不到 git。請先安裝 Git for Windows: https://git-scm.com/download/win"
    exit 1
}
Write-Host "✔ git found: $($git.Source)" -ForegroundColor Green

# ---- 讀 pinned SHA --------------------------------------------------
$pinnedFile = Join-Path $repoRoot 'patches\UPSTREAM_COMMIT.txt'
if (-not (Test-Path $pinnedFile)) {
    Write-Error "找不到 $pinnedFile"
    exit 1
}
$content = Get-Content $pinnedFile -Raw
$match = [regex]::Match($content, '(?m)^([a-f0-9]{40})\s*$')
if (-not $match.Success) {
    Write-Error "無法從 UPSTREAM_COMMIT.txt 解析 SHA"
    exit 1
}
$pinnedSha = $match.Groups[1].Value
Write-Host "✔ Pinned SHA: $pinnedSha" -ForegroundColor Green

# ---- 蒐集 patches ---------------------------------------------------
$patches = Get-ChildItem (Join-Path $repoRoot 'patches\*.patch') | Sort-Object Name
Write-Host "✔ Found $($patches.Count) patches" -ForegroundColor Green
foreach ($p in $patches) { Write-Host "    $($p.Name)" -ForegroundColor DarkGray }
Write-Host ""

if (-not $Execute) {
    Write-Host "DryRun 完畢。加 -Execute 執行以下動作：" -ForegroundColor Yellow
    Write-Host "  1. $(if (Test-Path $TargetPath) { 'git fetch existing' } else { 'git clone new' }) → $TargetPath"
    Write-Host "  2. git checkout $pinnedSha"
    if ($Force -and (Test-Path $TargetPath)) { Write-Host "  (-Force) 3. git reset --hard + git clean -fd" }
    Write-Host "  4. 逐一套用 $($patches.Count) 個 patch"
    Write-Host ""
    exit 0
}

# ---- 執行階段 -------------------------------------------------------
if (Test-Path $TargetPath) {
    Write-Host "→ 目標已存在，執行 git fetch..." -ForegroundColor Cyan
    Push-Location $TargetPath
    try {
        if ($Force) {
            Write-Host "  -Force: git reset --hard + git clean -fd" -ForegroundColor Yellow
            git reset --hard HEAD 2>&1 | Out-Host
            git clean -fdx 2>&1 | Out-Host
        }
        git fetch origin 2>&1 | Out-Host
        if ($LASTEXITCODE -ne 0) { throw "git fetch failed" }
    } finally { Pop-Location }
} else {
    Write-Host "→ Clone $UpstreamUrl → $TargetPath ..." -ForegroundColor Cyan
    $parent = Split-Path -Parent $TargetPath
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    git clone $UpstreamUrl $TargetPath 2>&1 | Out-Host
    if ($LASTEXITCODE -ne 0) { throw "git clone failed" }
}

Write-Host "→ Checkout $pinnedSha ..." -ForegroundColor Cyan
Push-Location $TargetPath
try {
    git checkout $pinnedSha 2>&1 | Out-Host
    if ($LASTEXITCODE -ne 0) { throw "git checkout failed (SHA 不存在？跑 git fetch 後重試)" }

    # ---- 套用 patches -----------------------------------------------
    Write-Host ""
    Write-Host "→ 套用 $($patches.Count) 個 patches..." -ForegroundColor Cyan
    $applied = 0
    $failed  = @()
    foreach ($p in $patches) {
        # 先 check 再 apply
        git apply --check $p.FullName 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "  ✗ $($p.Name) — apply --check 失敗（可能已 upstream 或衝突）" -ForegroundColor Yellow
            $failed += $p.Name
            continue
        }
        git apply $p.FullName 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✔ $($p.Name)" -ForegroundColor Green
            $applied++
        } else {
            Write-Host "  ✗ $($p.Name) — apply 失敗" -ForegroundColor Red
            $failed += $p.Name
        }
    }
} finally { Pop-Location }

# ---- 結果報告 -------------------------------------------------------
Write-Host ""
Write-Host "=== 完成 ===" -ForegroundColor Cyan
Write-Host "套用成功: $applied / $($patches.Count)" -ForegroundColor $(if ($failed.Count -eq 0) { 'Green' } else { 'Yellow' })
if ($failed.Count -gt 0) {
    Write-Host "失敗 patches:" -ForegroundColor Yellow
    $failed | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
    Write-Host ""
    Write-Host "可能原因：" -ForegroundColor Yellow
    Write-Host "  1. Patch 已被 upstream 合併（正常，可略過）"
    Write-Host "  2. UPSTREAM_COMMIT.txt SHA 過舊，upstream 已改動同一區域（需更新 SHA 或 patch）"
    Write-Host ""
}
Write-Host "MegaMod ready at: $TargetPath" -ForegroundColor Green
Write-Host ""
Write-Host "下一步："
Write-Host "  cd $repoRoot\pipeline"
Write-Host "  .\build_zh-TW.ps1 && .\package_zh-TW.ps1"
Write-Host ""
