# ============================================================
# _release_full_zh-TW.ps1
#
# 打包 Star Control II 繁體中文化 release zip (方案 C · 完整一鍵包)
#
# 產出:
#   release/output/SC2-zhTW-<version>.zip           (~200 MB 中型包)
#   release/output/SC2-zhTW-<version>.zip.sha256    (SHA256 checksum)
#
# 用法:
#   .\_release_full_zh-TW.ps1                       # DryRun (預設 · 只列清單不打包)
#   .\_release_full_zh-TW.ps1 -Execute              # 實際打包
#   .\_release_full_zh-TW.ps1 -Execute -Force       # 覆蓋已有 output
#   .\_release_full_zh-TW.ps1 -Version v1.0-rc2     # 指定版本號
#
# 版權:
#   本 release 依 CC BY-NC-SA 2.5 + GPL-2.0 授權
#   詳見 release/staging-<version>/LICENSES/
# ============================================================

[CmdletBinding()]
param(
    [string]$Version = "v1.0-rc1",
    [switch]$Execute,     # 若未指定 · 預設 DryRun (只列清單)
    [switch]$Force,       # 覆蓋已有 output zip
    [string]$Root = (Split-Path -Parent $PSCommandPath)
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"   # 避免 Compress-Archive 進度條 render 錯

Set-Location $Root

# ============================================================
# 路徑定義
# ============================================================
$installDir  = Join-Path $Root "install"
$stagingDir  = Join-Path $Root "release\staging-$Version"
$outputDir   = Join-Path $Root "release\output"
$tempPackage = Join-Path $outputDir "SC2-zhTW-$Version"
$outputZip   = Join-Path $outputDir "SC2-zhTW-$Version.zip"
$outputSha   = Join-Path $outputDir "SC2-zhTW-$Version.zip.sha256"

# ============================================================
# 打包清單 (whitelist)
# ============================================================

# install/ 根目錄要 include 的檔案 (whitelist)
$installFiles = @(
    # 主 exe (patched · 支援 CJK + Zip64)
    'UrQuanMasters-zip64.exe',

    # DLL 依賴
    'SDL2.dll',
    'SDL2_image.dll',
    'SDL2_mixer.dll',
    'SDL2_net.dll',
    'libSDL2_gfx-1-0-0.dll',
    'libpng16-16.dll',
    'zlib1.dll',
    'libogg-0.dll',
    'libvorbis-0.dll',
    'libvorbisfile-3.dll',
    'libgcc_s_dw2-1.dll',
    'libgcc_s_seh-1.dll',
    'libstdc++-6.dll',
    'libwinpthread-1.dll',
    'libiconv-2.dll',
    'libintl-8.dll',
    'libsystre-0.dll',
    'libtre-5.dll',

    # 遊戲設定 configs
    'mm-3do.cfg',
    'mm-kad.cfg',
    'mm-pc.cfg',
    'uqm-3do.cfg',
    'uqm-kad.cfg',
    'uqm-pc.cfg',

    # 原版說明檔
    'AUTHORS.txt',
    'COPYING.txt',
    'CHANGELOG.txt',
    'UQM-README.txt',
    'UQM-Manual.txt',
    'README-SDL.txt',

    # 手把資源
    'gamepad.png'
)

# install/content/ 要 include 的 (whitelist)
$contentFiles = @(
    'version',
    'gamecontrollerdb.txt'
)

# install/content/packages/ 要 include 的 (whitelist)
$packageFiles = @(
    'mm-0.8.5-content.uqm'
)

# install/content/addons/ 要 include 的 (whitelist)
$addonFiles = @(
    'zh-TW.uqm',
    'zh-TW-hd.uqm'
)
$addonDirs = @(
    'mm-hd',
    '3do-mode-hd',
    '3do-mode-sd',
    'dos-mode-hd',
    'dos-mode-sd',
    'sol-textures-hd',
    'sol-textures-sd',
    'patch-en-lander'
)

# staging 內要 include 的檔案 (全部)
$stagingFiles = @(
    '快速開始.txt',
    'README.md',
    'ATTRIBUTION.md',
    'SOURCE.md',
    'CHANGELOG-zh-TW.md',
    'Play_HD.bat',
    'Play_HD_windows.bat',
    'Play_SD.bat',
    'Setup.bat'
)
$stagingDirs = @(
    'LICENSES',
    'SOURCE'   # 含 patches/
)

# ============================================================
# Step 1: 前置檢查
# ============================================================
Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " SC2 繁體中文化 · Release Packaging · $Version" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

$mode = if ($Execute) { "EXECUTE (實際打包)" } else { "DryRun (預覽 · 未執行)" }
Write-Host "  模式        : $mode" -ForegroundColor $(if ($Execute) { 'Green' } else { 'Yellow' })
Write-Host "  版本        : $Version"
Write-Host "  Staging     : $stagingDir"
Write-Host "  Install src : $installDir"
Write-Host "  Output      : $outputZip"
Write-Host ""

# 檢查 staging 目錄存在
if (-not (Test-Path $stagingDir)) {
    Write-Host "[FAIL] Staging 目錄不存在: $stagingDir" -ForegroundColor Red
    Write-Host "       請先執行 staging 檔案建立步驟" -ForegroundColor Red
    exit 1
}

# 檢查 staging 必要檔案
$missingStaging = @()
foreach ($f in $stagingFiles) {
    if (-not (Test-Path (Join-Path $stagingDir $f))) {
        $missingStaging += $f
    }
}
foreach ($d in $stagingDirs) {
    if (-not (Test-Path (Join-Path $stagingDir $d))) {
        $missingStaging += "$d/"
    }
}
if ($missingStaging.Count -gt 0) {
    Write-Host "[FAIL] Staging 缺少檔案:" -ForegroundColor Red
    $missingStaging | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    exit 1
}

# 檢查 install 目錄存在
if (-not (Test-Path $installDir)) {
    Write-Host "[FAIL] Install 目錄不存在: $installDir" -ForegroundColor Red
    exit 1
}

# 檢查主 exe 存在
$mainExe = Join-Path $installDir 'UrQuanMasters-zip64.exe'
if (-not (Test-Path $mainExe)) {
    Write-Host "[FAIL] 主 exe 不存在: $mainExe" -ForegroundColor Red
    exit 1
}

# 檢查 output 是否已存在
if ((Test-Path $outputZip) -and -not $Force -and $Execute) {
    Write-Host "[FAIL] Output zip 已存在: $outputZip" -ForegroundColor Red
    Write-Host "       使用 -Force 覆蓋" -ForegroundColor Yellow
    exit 1
}

Write-Host "[OK] 前置檢查通過" -ForegroundColor Green
Write-Host ""

# ============================================================
# Step 2: 統計要打包的檔案 (DryRun 可以在此結束)
# ============================================================
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Step 2: 掃描要打包的檔案" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

$totalSize = 0
$totalCount = 0

function Add-ToPlan {
    param($SrcPath, $Category)
    if (Test-Path $SrcPath -PathType Leaf) {
        $sz = (Get-Item $SrcPath).Length
        $script:totalSize += $sz
        $script:totalCount++
        return @{ Path = $SrcPath; Size = $sz; Category = $Category; IsDir = $false }
    } elseif (Test-Path $SrcPath -PathType Container) {
        $items = Get-ChildItem $SrcPath -Recurse -File -ErrorAction SilentlyContinue
        $sz = ($items | Measure-Object -Property Length -Sum).Sum
        $cnt = $items.Count
        $script:totalSize += $sz
        $script:totalCount += $cnt
        return @{ Path = $SrcPath; Size = $sz; Count = $cnt; Category = $Category; IsDir = $true }
    }
    return $null
}

$plan = @()

# install/ 根層檔案
Write-Host "-- install/ 根層檔案 --" -ForegroundColor Yellow
foreach ($f in $installFiles) {
    $src = Join-Path $installDir $f
    $item = Add-ToPlan $src "install-root"
    if ($null -eq $item) {
        Write-Host ("  [MISS] {0}" -f $f) -ForegroundColor Red
    } else {
        $plan += $item
        Write-Host ("  [OK]   {0,-35} {1,10:N1} KB" -f $f, ($item.Size/1KB)) -ForegroundColor DarkGray
    }
}

# install/content 根層
Write-Host ""
Write-Host "-- install/content/ 根層 --" -ForegroundColor Yellow
foreach ($f in $contentFiles) {
    $src = Join-Path $installDir "content\$f"
    $item = Add-ToPlan $src "content-root"
    if ($item) { $plan += $item; Write-Host ("  [OK]   {0}" -f $f) -ForegroundColor DarkGray }
}

# install/content/packages/
Write-Host ""
Write-Host "-- install/content/packages/ --" -ForegroundColor Yellow
foreach ($f in $packageFiles) {
    $src = Join-Path $installDir "content\packages\$f"
    $item = Add-ToPlan $src "content-packages"
    if ($item) {
        $plan += $item
        Write-Host ("  [OK]   {0,-40} {1,10:N1} MB" -f $f, ($item.Size/1MB)) -ForegroundColor DarkGray
    } else {
        Write-Host ("  [MISS] {0}" -f $f) -ForegroundColor Red
    }
}

# install/content/addons/ 檔案
Write-Host ""
Write-Host "-- install/content/addons/ 檔案 --" -ForegroundColor Yellow
foreach ($f in $addonFiles) {
    $src = Join-Path $installDir "content\addons\$f"
    $item = Add-ToPlan $src "content-addons"
    if ($item) {
        $plan += $item
        Write-Host ("  [OK]   {0,-30} {1,10:N1} MB" -f $f, ($item.Size/1MB)) -ForegroundColor DarkGray
    } else {
        Write-Host ("  [MISS] {0}" -f $f) -ForegroundColor Red
    }
}

# install/content/addons/ 目錄 (recursive)
Write-Host ""
Write-Host "-- install/content/addons/ 目錄 --" -ForegroundColor Yellow
foreach ($d in $addonDirs) {
    $src = Join-Path $installDir "content\addons\$d"
    $item = Add-ToPlan $src "content-addons-dir"
    if ($item) {
        $plan += $item
        Write-Host ("  [OK]   {0,-25} {1,6} files {2,10:N1} MB" -f $d, $item.Count, ($item.Size/1MB)) -ForegroundColor DarkGray
    } else {
        Write-Host ("  [MISS] {0}/" -f $d) -ForegroundColor Red
    }
}

# staging 文件檔
Write-Host ""
Write-Host "-- staging (文件檔) --" -ForegroundColor Yellow
foreach ($f in $stagingFiles) {
    $src = Join-Path $stagingDir $f
    $item = Add-ToPlan $src "staging-file"
    if ($item) { $plan += $item; Write-Host ("  [OK]   {0}" -f $f) -ForegroundColor DarkGray }
}
foreach ($d in $stagingDirs) {
    $src = Join-Path $stagingDir $d
    $item = Add-ToPlan $src "staging-dir"
    if ($item) {
        $plan += $item
        Write-Host ("  [OK]   {0,-25} {1,6} files {2,10:N1} KB" -f $d, $item.Count, ($item.Size/1KB)) -ForegroundColor DarkGray
    }
}

Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Summary" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ("  總檔案數    : {0}" -f $totalCount) -ForegroundColor White
Write-Host ("  總大小 (未壓縮): {0:N2} MB" -f ($totalSize/1MB)) -ForegroundColor White
Write-Host ("  預估壓縮後  : ~{0:N0}-{1:N0} MB (30-70%%)" -f (($totalSize*0.3)/1MB), (($totalSize*0.7)/1MB)) -ForegroundColor White
Write-Host ""

if (-not $Execute) {
    Write-Host "[DryRun] 未實際打包。加 -Execute 參數執行實際打包。" -ForegroundColor Yellow
    Write-Host ""
    exit 0
}

# ============================================================
# Step 3: 複製檔案到 temp package 目錄
# ============================================================
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Step 3: 複製到 temp package 目錄" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

if (Test-Path $tempPackage) {
    Write-Host "  清除舊 temp: $tempPackage"
    Remove-Item $tempPackage -Recurse -Force
}
New-Item -ItemType Directory -Path $tempPackage | Out-Null

$copied = 0
foreach ($item in $plan) {
    $src = $item.Path
    # 計算目標相對路徑
    $rel = ""
    switch ($item.Category) {
        "install-root"       { $rel = Split-Path $src -Leaf }
        "content-root"       { $rel = "content\" + (Split-Path $src -Leaf) }
        "content-packages"   { $rel = "content\packages\" + (Split-Path $src -Leaf) }
        "content-addons"     { $rel = "content\addons\" + (Split-Path $src -Leaf) }
        "content-addons-dir" { $rel = "content\addons\" + (Split-Path $src -Leaf) }
        "staging-file"       { $rel = Split-Path $src -Leaf }
        "staging-dir"        { $rel = Split-Path $src -Leaf }
        default              { throw "Unknown category: $($item.Category)" }
    }
    $dst = Join-Path $tempPackage $rel

    if ($item.IsDir) {
        Copy-Item $src $dst -Recurse -Force
        $copied += $item.Count
    } else {
        $dstDir = Split-Path $dst -Parent
        if (-not (Test-Path $dstDir)) { New-Item -ItemType Directory -Path $dstDir -Force | Out-Null }
        Copy-Item $src $dst -Force
        $copied++
    }
}

Write-Host "  [OK] 已複製 $copied 個檔案" -ForegroundColor Green
Write-Host ""

# ============================================================
# Step 4: 打包成 zip
# ============================================================
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Step 4: 打包成 zip" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

if (Test-Path $outputZip) { Remove-Item $outputZip -Force }

Write-Host "  Compressing... (this may take a minute)"
$sw = [System.Diagnostics.Stopwatch]::StartNew()

# 用 System.IO.Compression 而非 Compress-Archive 以支援大檔
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory(
    $tempPackage,
    $outputZip,
    [System.IO.Compression.CompressionLevel]::Optimal,
    $true    # includeBaseDirectory
)

$sw.Stop()
$zipSize = (Get-Item $outputZip).Length
Write-Host ("  [OK] Zip: {0:N2} MB (壓縮率 {1:N1}%%) . {2:N1} 秒" -f `
    ($zipSize/1MB), (($zipSize/$totalSize)*100), $sw.Elapsed.TotalSeconds) -ForegroundColor Green
Write-Host ""

# ============================================================
# Step 5: SHA256 checksum
# ============================================================
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Step 5: SHA256 checksum" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

$hash = Get-FileHash -Path $outputZip -Algorithm SHA256
$hashLine = "$($hash.Hash.ToLower())  SC2-zhTW-$Version.zip"
$hashLine | Out-File -FilePath $outputSha -Encoding ascii -NoNewline

Write-Host "  [OK] $outputSha" -ForegroundColor Green
Write-Host "       $hashLine" -ForegroundColor DarkGray
Write-Host ""

# ============================================================
# Step 6: 清理 temp
# ============================================================
Write-Host "  清除 temp: $tempPackage"
Remove-Item $tempPackage -Recurse -Force

Write-Host ""
Write-Host "================================================================" -ForegroundColor Green
Write-Host " Release 打包完成" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Zip     : $outputZip" -ForegroundColor White
Write-Host ("  Size    : {0:N2} MB" -f ($zipSize/1MB)) -ForegroundColor White
Write-Host "  SHA256  : $outputSha" -ForegroundColor White
Write-Host ""
Write-Host "  下一步:" -ForegroundColor Cyan
Write-Host "   1. 手動測試: 解壓到 temp . 執行 Play_HD.bat 驗證可玩" -ForegroundColor White
Write-Host "   2. 上傳 GitHub Release: [填入你的 GitHub URL]/releases/new" -ForegroundColor White
Write-Host "   3. 上傳 Google Drive: 可分享連結" -ForegroundColor White
Write-Host "   4. 附上 SHA256 供玩家 verify 下載完整性" -ForegroundColor White
Write-Host ""
