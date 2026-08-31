# One-shot full build → package → .NET zip → HD repack pipeline
# Guarantees zh-TW.uqm + zh-TW-hd.uqm reflect latest translations/*.json
# without falling into the v1.0.7/8/9 build regression (stale _stage).
#
# Steps:
#   1. build_zh-TW.ps1     — JSON → content/ TXT (also runs 3-gate)
#   2. package -SkipBuild -NoZip
#                          — content/ → _stage/shadow-content/ + font redirects
#   3. .NET ZipFile        — _stage/zh-TW → zh-TW.uqm (SD, avoids Compress-Archive hang)
#   4. _repackage_hd_addon — HD repack with msys64 stripped from PATH
#
# Usage: .\_full_pipeline.ps1
#        .\_full_pipeline.ps1 -SkipBuild        # skip step 1 (use existing content/)
#        .\_full_pipeline.ps1 -SkipHybridUI     # forwarded to package
param(
  [switch]$SkipBuild,
  [switch]$SkipHybridUI
)
$ErrorActionPreference = 'Stop'
$root = 'Q:\Dos_G\StarControl2\uqm-work'
Set-Location $root

# Ensure Python310 (has PIL) — msys python does NOT
$env:Path = "C:\Users\v-nientzukao\AppData\Local\Programs\Python\Python310;C:\Users\v-nientzukao\AppData\Local\Programs\Python\Python310\Scripts;" + $env:Path
$env:PYTHONIOENCODING = 'utf-8'

Write-Host '========================================================================' -ForegroundColor Cyan
Write-Host ' Full pipeline: build → stage → SD zip → HD zip' -ForegroundColor Cyan
Write-Host '========================================================================' -ForegroundColor Cyan

if (-not $SkipBuild) {
  Write-Host "`n== Step 1: build_zh-TW.ps1 ==" -ForegroundColor Green
  & "$root\build_zh-TW.ps1"
  if ($LASTEXITCODE -ne 0) { throw "build_zh-TW.ps1 failed (exit=$LASTEXITCODE)" }
}

Write-Host "`n== Step 2: package -SkipBuild -NoZip (refresh _stage) ==" -ForegroundColor Green
# Note: direct invocation with named switches — splat with switch-args
# doesn't reliably bind in older pwsh; direct call ensures $SkipBuild/$NoZip = $true.
if ($SkipHybridUI) {
  & "$root\package_zh-TW.ps1" -SkipBuild -NoZip -SkipHybridUI
} else {
  & "$root\package_zh-TW.ps1" -SkipBuild -NoZip
}
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne $null) { throw "package_zh-TW.ps1 failed (exit=$LASTEXITCODE)" }

Write-Host "`n== Step 3: .NET zip SD zh-TW.uqm ==" -ForegroundColor Green
Add-Type -AssemblyName System.IO.Compression.FileSystem
$stage = "$root\zh-TW-addon\_stage\zh-TW"
$sdOut = "$root\zh-TW-addon\zh-TW.uqm"
$sdInstall = "$root\install\content\addons\zh-TW.uqm"
Remove-Item $sdOut -Force -ErrorAction SilentlyContinue
[IO.Compression.ZipFile]::CreateFromDirectory($stage, $sdOut, [IO.Compression.CompressionLevel]::Optimal, $true)
Copy-Item $sdOut $sdInstall -Force
$sd = Get-Item $sdInstall
Write-Host ("  SD zh-TW.uqm : {0:N1} MB  {1}" -f ($sd.Length/1MB), $sd.LastWriteTime)

Write-Host "`n== Step 4: HD repack (msys64 stripped) ==" -ForegroundColor Green
$env:Path = ($env:Path -split ';' | Where-Object { $_ -notlike '*msys64*' }) -join ';'
& "$root\_repackage_hd_addon.ps1" 2>&1 | Tee-Object -FilePath "$root\_hd_repack_log.txt" | Out-Null
$hd = Get-Item "$root\install\content\addons\zh-TW-hd.uqm"
Write-Host ("  HD zh-TW-hd.uqm : {0:N1} MB  {1}" -f ($hd.Length/1MB), $hd.LastWriteTime)

Write-Host "`n========================================================================" -ForegroundColor Cyan
Write-Host " Pipeline complete. Verify zip freshness with python _verify_zip_fresh.py" -ForegroundColor Cyan
Write-Host '========================================================================' -ForegroundColor Cyan
