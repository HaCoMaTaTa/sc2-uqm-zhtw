# _repackage_hd_addon.ps1
# Fast repackage: use directory junction to avoid the slow 117k file copy.
# Structure needed:
#   _stage_hd_addon\zh-TW-hd\uqm.rmp
#   _stage_hd_addon\zh-TW-hd\shadow-content\addons\mm-hd\fonts  -> [JUNCTION] -> _stage_hd_fonts
#   _stage_hd_addon\zh-TW-hd\shadow-content\addons\mm-hd\nav\orbitbackground\orbitbackground-021.png
#   _stage_hd_addon\zh-TW-hd\shadow-content\addons\mm-hd\lander\fonteffect-000.png
#   _stage_hd_addon\zh-TW-hd\shadow-content\addons\mm-hd\lander\fonteffect-001.png
# The last three come from _scripts\make_zhhd_report_overrides.py which stages
# them under zh-TW-addon\_intermediate\zh-TW-hd-overrides\ (patch 032).

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$stageSrc = "$root\_stage_hd_fonts"
$stageBuild = "$root\_stage_hd_addon"
$reportOverrides = "$root\zh-TW-addon\_intermediate\zh-TW-hd-overrides"
$out = "$root\install\content\addons\zh-TW-hd.uqm"

if (-not (Test-Path $stageSrc)) {
    Write-Error "Stage $stageSrc not found."
    exit 1
}

Write-Host "=== Repackage zh-TW-hd.uqm (via junction) ===" -ForegroundColor Cyan

# Clean previous stage
if (Test-Path $stageBuild) { Remove-Item $stageBuild -Recurse -Force }

# Create nested structure up to mm-hd (but NOT fonts — that will be a junction)
$parentDir = "$stageBuild\zh-TW-hd\shadow-content\addons\mm-hd"
New-Item -ItemType Directory -Path $parentDir -Force | Out-Null

# Junction: fonts -> _stage_hd_fonts
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$junctionPath = "$parentDir\fonts"
& cmd /c mklink /J "$junctionPath" "$stageSrc" | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to create junction"
    exit 1
}
$sw.Stop()
Write-Host ("  Junction created ({0:N2}s)" -f $sw.Elapsed.TotalSeconds)

# zh-TW patch 032 report overrides (dark-grey grid + white fonteffect PNGs).
# Regenerate the stage on every packaging pass so the addon zip always
# reflects the current source scripts.
Write-Host "  Generating report override PNGs..." -ForegroundColor DarkGray
& python "$root\_scripts\make_zhhd_report_overrides.py" | ForEach-Object { "    $_" }
if ($LASTEXITCODE -ne 0) {
    Write-Error "make_zhhd_report_overrides.py failed"
    exit 1
}
if (-not (Test-Path $reportOverrides)) {
    Write-Error "Report override stage missing: $reportOverrides"
    exit 1
}
# Copy the override tree straight into the addon structure.
Copy-Item "$reportOverrides\*" $parentDir -Recurse -Force
$overrideCount = (Get-ChildItem $reportOverrides -Recurse -File).Count
Write-Host ("  Report overrides copied ({0} files)" -f $overrideCount)

# Write uqm.rmp
$rmp = @"
# zh-TW-hd addon — shadow-content overlays HD fonts with CJK glyphs plus
# lander discovery report readability overrides (patch 032).
# Requires --addon zh-TW (base gamestrings/comm dialog) AND
# --addon mm-hd (HD graphics) loaded together.
"@
[System.IO.File]::WriteAllText("$stageBuild\zh-TW-hd\uqm.rmp", $rmp, [System.Text.Encoding]::ASCII)

# 7z zip
$sw = [System.Diagnostics.Stopwatch]::StartNew()
if (Test-Path $out) { Remove-Item $out -Force }
Push-Location $stageBuild
try {
    & "C:\Program Files\7-Zip\7z.exe" a -tzip -mx=5 -mm=Deflate $out "zh-TW-hd" | Select-Object -Last 5
} finally {
    Pop-Location
}
$sw.Stop()
Write-Host ("  Zip complete ({0:N1}s)" -f $sw.Elapsed.TotalSeconds)

# Remove junction (important: don't Remove-Item -Recurse without care)
# Use `cmd /c rmdir` to remove junction without following it
& cmd /c rmdir "$junctionPath" | Out-Null
Remove-Item $stageBuild -Recurse -Force

Write-Host ""
if (Test-Path $out) {
    $size = (Get-Item $out).Length
    Write-Host "=== zh-TW-hd.uqm repackaged ===" -ForegroundColor Green
    Write-Host ("  Size : {0:N1} MB" -f ($size / 1MB))
} else {
    Write-Error "Output not created!"
}
