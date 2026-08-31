# =====================================================================
# setup_upstream.ps1
# 一鍵準備 UQM-MegaMod upstream source tree（含全部 34 個 patch 已 commit 的 state）。
#
# 使用方式：
#   .\scripts\setup_upstream.ps1                 # 預設 DryRun（只列出動作）
#   .\scripts\setup_upstream.ps1 -Execute        # 實跑
#   .\scripts\setup_upstream.ps1 -Execute -Force # 已存在也強制重跑（重置本地變更）
#   .\scripts\setup_upstream.ps1 -Execute -TargetPath 'D:\my\path\UQM-MegaMod'
#   .\scripts\setup_upstream.ps1 -Execute -ForkUrl 'https://github.com/USER/uqm-megamod-zhTW.git'
#
# 這個腳本 **不** apply patches/*.patch。
# 原因見 patches/UPSTREAM_COMMIT.txt § patches/*.patch 的角色。
#
# 產物：<repo_root>/../UQM-MegaMod/ 或 -TargetPath 指定路徑
#       內容 = fork 於指定 SHA（等同於作者本地 UQM-MegaMod state）
# =====================================================================

[CmdletBinding()]
param(
    [switch]$Execute,
    [switch]$Force,
    [string]$TargetPath,
    [string]$ForkUrl
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
Write-Host "OK  git found: $($git.Source)" -ForegroundColor Green

# ---- 讀 pinned SHA + Fork URL --------------------------------------
$pinnedFile = Join-Path $repoRoot 'patches\UPSTREAM_COMMIT.txt'
if (-not (Test-Path $pinnedFile)) {
    Write-Error "找不到 $pinnedFile"
    exit 1
}
$content = Get-Content $pinnedFile -Raw

# SHA
$shaMatch = [regex]::Match($content, '(?m)^([a-f0-9]{40})\s*$')
if (-not $shaMatch.Success) {
    Write-Error "無法從 UPSTREAM_COMMIT.txt 解析 SHA"
    exit 1
}
$pinnedSha = $shaMatch.Groups[1].Value
Write-Host "OK  Pinned SHA: $pinnedSha" -ForegroundColor Green

# Fork URL（若命令列未傳，從 UPSTREAM_COMMIT.txt 讀）
if (-not $ForkUrl) {
    $urlMatch = [regex]::Match($content, '(?m)^https://github\.com/[^\s`)]+UQM-MegaMod[^\s`)]*\.git')
    if ($urlMatch.Success) {
        $ForkUrl = $urlMatch.Value
    }
}

# 檢查 URL 是否還是佔位符
if ($ForkUrl -match 'CHANGE_ME_TO_YOUR_GITHUB_USER') {
    Write-Host ""
    Write-Host "警告：Fork URL 是佔位符：" -ForegroundColor Yellow
    Write-Host "  $ForkUrl" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "專案作者尚未把 UQM-MegaMod push 到 GitHub。請完成以下之一：" -ForegroundColor Yellow
    Write-Host "  1. 依 docs/PUSH_UQM_MEGAMOD_FORK.md 建立 fork · 更新 UPSTREAM_COMMIT.txt"
    Write-Host "  2. 或用 -ForkUrl 手動指定 URL：" -ForegroundColor Yellow
    Write-Host "     .\scripts\setup_upstream.ps1 -Execute -ForkUrl 'https://github.com/YOUR_USER/uqm-megamod-zhTW.git'"
    Write-Host ""
    if (-not $Execute) {
        Write-Host "（DryRun 允許繼續往下印剩餘檢查步驟）" -ForegroundColor DarkGray
    } else {
        exit 1
    }
}
Write-Host "OK  Fork URL: $ForkUrl" -ForegroundColor Green

# ---- DryRun 出口 ---------------------------------------------------
if (-not $Execute) {
    Write-Host ""
    Write-Host "DryRun 完畢。加 -Execute 執行以下動作：" -ForegroundColor Yellow
    if (Test-Path $TargetPath) {
        Write-Host "  1. git fetch existing → $TargetPath"
        if ($Force) { Write-Host "     (-Force) git reset --hard + git clean -fdx" }
    } else {
        Write-Host "  1. git clone $ForkUrl → $TargetPath"
    }
    Write-Host "  2. git checkout $pinnedSha"
    Write-Host "  3. （不套 patches——patches 已被 committed 到 fork branch）"
    Write-Host ""
    exit 0
}

# ---- 執行階段 -------------------------------------------------------
if (Test-Path $TargetPath) {
    Write-Host "→ 目標已存在，執行 git fetch..." -ForegroundColor Cyan
    Push-Location $TargetPath
    try {
        if ($Force) {
            Write-Host "  -Force: git reset --hard + git clean -fdx" -ForegroundColor Yellow
            git reset --hard HEAD 2>&1 | Out-Host
            git clean -fdx 2>&1 | Out-Host
        }
        # 確保 remote 指向 fork
        $currentRemote = git remote get-url origin 2>&1
        if ($currentRemote -ne $ForkUrl) {
            Write-Host "  Remote origin 目前指向: $currentRemote" -ForegroundColor DarkGray
            Write-Host "  改指向 fork: $ForkUrl" -ForegroundColor DarkGray
            git remote set-url origin $ForkUrl 2>&1 | Out-Host
        }
        git fetch origin 2>&1 | Out-Host
        if ($LASTEXITCODE -ne 0) { throw "git fetch failed" }
    } finally { Pop-Location }
} else {
    Write-Host "→ Clone $ForkUrl → $TargetPath ..." -ForegroundColor Cyan
    $parent = Split-Path -Parent $TargetPath
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    git clone $ForkUrl $TargetPath 2>&1 | Out-Host
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "Clone 失敗。可能原因：" -ForegroundColor Red
        Write-Host "  1. Fork URL 錯誤或該 repo 尚未建立"
        Write-Host "  2. 網路連不到 GitHub"
        Write-Host "  3. 需要驗證（private repo？）"
        Write-Host ""
        Write-Host "詳見 docs/PUSH_UQM_MEGAMOD_FORK.md § 疑難排解"
        throw "git clone failed"
    }
}

Write-Host "→ Checkout $pinnedSha ..." -ForegroundColor Cyan
Push-Location $TargetPath
try {
    git checkout $pinnedSha 2>&1 | Out-Host
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "Checkout 失敗。SHA $pinnedSha 不在 fork 內。" -ForegroundColor Red
        Write-Host "可能原因：" -ForegroundColor Yellow
        Write-Host "  1. Fork 尚未 push 到最新（作者本地有這個 commit，但 GitHub 上沒）"
        Write-Host "  2. UPSTREAM_COMMIT.txt 的 SHA 過期"
        Write-Host ""
        Write-Host "解法：見 docs/PUSH_UQM_MEGAMOD_FORK.md § 疑難排解"
        throw "git checkout failed"
    }
} finally { Pop-Location }

# ---- 結果 ----------------------------------------------------------
Write-Host ""
Write-Host "=== 完成 ===" -ForegroundColor Cyan
Write-Host "MegaMod ready at: $TargetPath" -ForegroundColor Green
Write-Host "Commit: $pinnedSha" -ForegroundColor Green
Write-Host ""
Write-Host "此時 $TargetPath 內含："
Write-Host "  - JHGuitarFreak/UQM-MegaMod 官方源碼"
Write-Host "  - 34 個 CJK/Android 引擎 patch（已 committed 為分支歷史）"
Write-Host "  - Android build scaffold + 觸控 UI + 虛擬 joystick"
Write-Host "  - 品牌化資產（icon / manifest）"
Write-Host ""
Write-Host "下一步："
Write-Host "  cd $repoRoot\pipeline"
Write-Host "  .\build_zh-TW.ps1 && .\package_zh-TW.ps1"
Write-Host ""
