# _package_hd_addon.ps1
# Package _stage_hd_fonts/ into zh-TW-hd.uqm addon.
# Addon structure:
#   zh-TW-hd/
#     uqm.rmp                            (empty passthrough)
#     shadow-content/
#       addons/mm-hd/fonts/<name>.fon/*  (overlays HD fonts with CJK)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$root = $PSScriptRoot
$stageSrc = "$root\_stage_hd_fonts"
$stageBuild = "$root\_stage_hd_addon"
$out = "$root\install\content\addons\zh-TW-hd.uqm"

if (-not (Test-Path $stageSrc)) {
    Write-Error "Stage $stageSrc not found — run _build_hd_fonts.ps1 first."
    exit 1
}

Write-Host "=== Building zh-TW-hd.uqm ===" -ForegroundColor Cyan

# Clean+recreate build stage
if (Test-Path $stageBuild) { Remove-Item $stageBuild -Recurse -Force }
$fontsTarget = "$stageBuild\zh-TW-hd\shadow-content\addons\mm-hd\fonts"
New-Item -ItemType Directory -Path $fontsTarget -Force | Out-Null

# Copy all HD font dirs into shadow-content
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$fontDirs = Get-ChildItem $stageSrc -Directory
foreach ($fd in $fontDirs) {
    Copy-Item $fd.FullName -Destination $fontsTarget -Recurse
}
$sw.Stop()
Write-Host ("  Copied $($fontDirs.Count) font dirs to shadow-content ({0:N1}s)" -f $sw.Elapsed.TotalSeconds)

# uqm.rmp (empty passthrough)
$rmp = @"
# zh-TW-hd addon — shadow-content overlays HD fonts with CJK glyphs.
# Requires --addon zh-TW (for base gamestrings/comm dialog) AND
# --addon mm-hd (for HD graphics) to be loaded together.
"@
[System.IO.File]::WriteAllText("$stageBuild\zh-TW-hd\uqm.rmp", $rmp, [System.Text.Encoding]::ASCII)

# Compress
$sw = [System.Diagnostics.Stopwatch]::StartNew()
if (Test-Path $out) { Remove-Item $out -Force }
Push-Location $stageBuild
try {
    Compress-Archive -Path "zh-TW-hd" -DestinationPath $out -Force -CompressionLevel Optimal
} finally {
    Pop-Location
}
$sw.Stop()
Write-Host ("  Compress ({0:N1}s)" -f $sw.Elapsed.TotalSeconds)

# Verify + report
$size = (Get-Item $out).Length
$entryCount = 0
try {
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $z = [System.IO.Compression.ZipFile]::OpenRead($out)
    $entryCount = $z.Entries.Count
    $z.Dispose()
} catch {
    Write-Host "  (ZIP read failed — may be Zip64)" -ForegroundColor Yellow
}

# Zip64 detection: scan for EOCD64 signature
$rawBytes = [System.IO.File]::ReadAllBytes($out)
$rawLen = $rawBytes.Length
$hasZip64 = $false
$scanStart = [Math]::Max(0, $rawLen - 65535 - 22)
for ($i = $scanStart; $i -lt $rawLen - 4; $i++) {
    if ($rawBytes[$i] -eq 0x50 -and $rawBytes[$i+1] -eq 0x4b -and $rawBytes[$i+2] -eq 0x06 -and $rawBytes[$i+3] -eq 0x06) {
        $hasZip64 = $true
        break
    }
}

Write-Host ""
Write-Host "=== zh-TW-hd.uqm packaged ===" -ForegroundColor Green
Write-Host ("  Path         : $out")
Write-Host ("  Size         : {0:N1} MB" -f ($size / 1MB))
Write-Host ("  Entries      : {0:N0}" -f $entryCount)
Write-Host ("  Zip64        : $hasZip64")
if ($hasZip64) {
    Write-Host "  Note         : Requires UrQuanMasters-zip64.exe (patched)" -ForegroundColor Yellow
}

# Cleanup temp stage
Remove-Item $stageBuild -Recurse -Force -ErrorAction SilentlyContinue
