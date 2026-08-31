# _build_hd_fonts.ps1
# Batch-rasterize all HD Chinese fonts for zh-TW-hd.uqm addon.
# Each font uses its native HD height (from install/content/addons/mm-hd/fonts/<name>.fon).
# Skip: pt13/pt17/pt45 (no kerndat, special format).
# Special: computer.fon (no kerndat, use label.fon as reference).

$ErrorActionPreference = 'Continue'
$root = $PSScriptRoot
$mmhdFonts = "$root\install\content\addons\mm-hd\fonts"
$stage = "$root\_stage_hd_fonts"
$ttf = "C:\Windows\Fonts\NotoSansTC-VF.ttf"
$charsFile = "$root\translations\_used_chars.txt"

# Delete + recreate stage
if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage | Out-Null

# List fonts to rasterize
$skipNoKerndat = @('pt13.fon', 'pt17.fon', 'pt45.fon')
$specialComputer = 'computer.fon'

$fontDirs = Get-ChildItem $mmhdFonts -Directory | Where-Object {
    ($_.Name -notin $skipNoKerndat)
}

$total = $fontDirs.Count
$done = 0
$failed = 0
$totalGlyphs = 0
$sw = [System.Diagnostics.Stopwatch]::StartNew()

Write-Host "Rasterizing $total fonts to $stage" -ForegroundColor Cyan
Write-Host ""

foreach ($fd in $fontDirs) {
    $name = $fd.Name
    $refPath = $fd.FullName
    $outPath = "$stage\$name"

    # Special: computer.fon has empty kerndat -> use label.fon as reference
    if ($name -eq $specialComputer) {
        $refPath = "$mmhdFonts\label.fon"
        Write-Host "  [special] $name  ref=label.fon (HD 44px)" -ForegroundColor Yellow
    }

    $done++
    $tsw = [System.Diagnostics.Stopwatch]::StartNew()
    # UI-heavy fonts get CJK slightly shrunk (85%) to fit tight text-boxes
    # in outfit stats, planet info, cargo/devices panels, etc. Prevents the
    # bottom-clipping that made e.g. '首' visually resemble '苦'.
    $uiHeavyFonts = @('label.fon','micro.fon','micro.thin.fon',
                      'tiny.fon','tiny.bold.fon','tiny.cond.fon',
                      'module.fon','square.fon','probe.fon')
    $cjkScale = if ($uiHeavyFonts -contains $name) { '0.85' } else { '1.0' }
    # HD baseline shift per font — fixes dialog top-clipping without
    # changing glyph size. Positive N adds N to kerndat VertAlign, which
    # decreases HotSpot.y and shifts every glyph N rows LOWER on-screen.
    # Verified 2026-08-13: pkunk dialog frame is unusually tight vs Hayes;
    # +10 gives roughly Hayes-comparable top padding at HD scale.
    $vertShift = switch ($name) {
        'pkunk.fon' { '10' }
        default     { '0' }
    }
    $vertArgs = if ($vertShift -eq '0') { @() } else { @('--vertalign-adjust', $vertShift) }
    $output = python "$root\rasterize_font.py" `
        --ref-font $refPath `
        --ttf $ttf `
        --chars-file $charsFile `
        --out $outPath `
        --cjk-scale $cjkScale `
        @vertArgs 2>&1
    $tsw.Stop()

    $rasterLine = $output | Select-String -Pattern 'Rasterized:' | Select-Object -First 1
    if ($LASTEXITCODE -eq 0 -and $rasterLine) {
        # Parse "Rasterized: 2919 new PNGs, ..."
        if ($rasterLine.Line -match 'Rasterized:\s+(\d+)') {
            $totalGlyphs += [int]$Matches[1]
        }
        Write-Host ("  [{0,2}/{1}] {2,-22}  {3,7:N1}s  {4}" -f $done, $total, $name, $tsw.Elapsed.TotalSeconds, $rasterLine.Line) -ForegroundColor Green
    } else {
        $failed++
        Write-Host ("  [{0,2}/{1}] {2,-22}  FAILED" -f $done, $total, $name) -ForegroundColor Red
        $output | Select-Object -Last 3 | ForEach-Object { Write-Host "        $_" -ForegroundColor DarkGray }
    }
}

# For computer.fon: fix kerndat.fnt first-line name (was "label.fon", must be "computer.fon")
$computerKern = "$stage\computer.fon\kerndat.fnt"
if (Test-Path $computerKern) {
    $lines = Get-Content $computerKern -Encoding ASCII
    if ($lines[0] -match '^label\.fon\s+(.+)$') {
        $lines[0] = "computer.fon $($Matches[1])"
        [System.IO.File]::WriteAllText($computerKern, ($lines -join "`n") + "`n", [System.Text.Encoding]::ASCII)
        Write-Host "  Fixed computer.fon kerndat name (was 'label.fon')" -ForegroundColor DarkYellow
    }
}

$sw.Stop()
Write-Host ""
Write-Host ("=== Summary ===") -ForegroundColor Cyan
Write-Host ("  Total fonts        : $total")
Write-Host ("  Succeeded          : $($done - $failed)")
Write-Host ("  Failed             : $failed")
Write-Host ("  Total glyphs       : {0:N0}" -f $totalGlyphs)
Write-Host ("  Elapsed            : {0:N1}s" -f $sw.Elapsed.TotalSeconds)
$stageSize = ((Get-ChildItem $stage -Recurse -File | Measure-Object Length -Sum).Sum / 1MB)
Write-Host ("  Stage size         : {0:N1} MB" -f $stageSize)
