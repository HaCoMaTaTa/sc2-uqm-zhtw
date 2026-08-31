# Final v0.1 packaging
# MegaMod addon override mechanism: files in <addon>/shadow-content/ get
# mounted with uio_MOUNT_ABOVE on top of the base content mount.
# (Source: src/options.c prepareShadowAddons in UQM-MegaMod)
#
# Params:
#   -SkipBuild       Skip auto-invoking build_zh-TW.ps1 (default: run build first
#                    so staged .txt reflects the latest translations/*.json).
#   -SkipHybridUI    Skip hybrid UI font redirects (starcon/tiny/micro/label/lander)
#                    to keep addon under ZIP32's 65,535 entry limit (Zip64 fix).
#                    Impact: cargo/devices/planet-info/lander UI panels revert
#                    to English but dialog + main menu remain Chinese. Use this
#                    while ZIP64 support is not available in MegaMod's UIO.
param(
  [switch]$SkipBuild,
  [switch]$SkipHybridUI,
  [switch]$NoZip
)

# --- Bug fixes 2026-08-08 (Phase 14c) ---
# 1. $ProgressPreference = 'SilentlyContinue' — Compress-Archive's progress bar
#    triggers a host-rendering error in some PowerShell hosts that appears as
#    "The archive file 'Q:\...zh-TW-add[...]" and aborts the pipeline. Silencing
#    progress avoids the render path.
# 2. Auto-invoke build_zh-TW.ps1 before packaging — the pipeline is 2-stage
#    (JSON→.txt via build, .txt→.uqm via package). Running package without
#    build first would zip stale staged .txt files. Skip with -SkipBuild.
$ProgressPreference = 'SilentlyContinue'

$root = $PSScriptRoot                          # pipeline/ (see docs/SOP_Rebuild_And_Release.md)
$stage = "$root\zh-TW-addon\_stage\zh-TW"

# Auto-run build to guarantee staged .txt is fresh from JSON.
if (-not $SkipBuild) {
  Write-Host "== Step -1: auto-invoke build_zh-TW.ps1 (use -SkipBuild to skip) ==" -ForegroundColor Cyan
  & "$root\build_zh-TW.ps1"
  if ($LASTEXITCODE -ne 0) {
    Write-Error "build_zh-TW.ps1 failed (exit=$LASTEXITCODE) — aborting package."
    exit 1
  }
  Write-Host ""
}

# Coordinate with other sessions — same mutex as build_zh-TW.ps1.
# Without this, a concurrent build (or another translate_ui.py writing
# into content/) races us: Copy-Item base sees a half-written tree and
# the resulting zh-TW.uqm is truncated (was seen at 84 KB vs full ~300+ KB).
. "$root\_build_lock.ps1"
Enter-BuildLock

try {

# Clean stage
Remove-Item "$root\zh-TW-addon\_stage" -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$stage\shadow-content" -Force | Out-Null

# Copy base tree into shadow-content (this is the override layer)
Copy-Item "$root\zh-TW-addon\content\base" "$stage\shadow-content\base" -Recurse

# Font size hack: some CJK-needing speakers use fonts < 14 px.
# We shadow-copy a CJK-viable font's directory content into the target
# font's directory. Base game reads e.g. "commander.fon" folder — we now
# supply computer.fon's PNGs+kerndat there, effectively re-sizing.
#
# After copying, we also REWRITE kerndat.fnt so its first-line font-name
# token matches the destination directory name (the engine keys the font
# by that name; a mismatch causes lookup failures + crashes).
#
# Mode = "full"   → replace entire target font (ASCII+CJK become 15px)
# Mode = "hybrid" → keep target's original ASCII glyphs (small), only
#                    add CJK glyphs (>= 0x0080). By default takes CJK from
#                    `From` font; override with `CjkSource` for smaller CJK
#                    (e.g. 11px playmenu-based, so menu items don't overlap).
$fontRedirects = @(
  @{ From = "computer.fon"; To = "commander.fon"; Mode = "full"   },  # Hayes NPC dialog (native 9px → 15px, all CJK)
  @{ From = "computer.fon"; To = "player.fon";    Mode = "full"   },  # Player response menu (native 10px → 15px)
  @{ From = "computer.fon"; To = "arilou.fon";    Mode = "full"   },  # Arilou dialog (native 9px → 15px, L3+ audit)
  @{ From = "computer.fon"; To = "chmmr.fon";     Mode = "full"   },  # Chmmr dialog (native 10px → 15px, L3+ audit)
  @{ From = "computer.fon"; To = "umgah.fon";     Mode = "full"   },  # Umgah dialog (native 8px → 15px, Round 1 v0.1)
  @{ From = "computer.fon"; To = "talkingpet.fon"; Mode = "full"  },  # Talking Pet / neo-Dnyarri (native 11px → 15px, Round 1 v0.1)
  @{ From = "computer.fon"; To = "thraddash.fon"; Mode = "full"   },  # Thraddash dialog (native 11px → 15px, Round 3 v0.1)
  @{ From = "computer.fon"; To = "zoqfotpik.fon"; Mode = "full"   },  # Zoq-Fot-Pik dialog (native 10px → 15px, Round 3 v0.1)
  @{ From = "computer.fon"; To = "druuge.fon";    Mode = "full"   }   # Druuge dialog (native 11px → 15px, v0.5.2 D2 audit 2026-08-11 修復缺字 bug)
)
# Hybrid UI font redirects — conditionally added (skipped with -SkipHybridUI).
# These push total addon entry count > 65,535 which triggers Zip64 format,
# and MegaMod's UIO does NOT support Zip64 → addon fails to mount.
# Skipping = UI panels (cargo/devices/planet-info/lander) show English but
# dialog + main menu remain Chinese. Long-term fix: patch UIO for Zip64.
if (-not $SkipHybridUI) {
  $fontRedirects += @(
    @{ From = "computer.fon"; To = "starcon.fon";   Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # PC 選單 & 頂部標題: 英文 7px + CJK 8px Fusion Pixel
    @{ From = "computer.fon"; To = "tiny.fon";      Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # cargo/devices/lander body text
    @{ From = "computer.fon"; To = "tiny.bold.fon"; Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # cargo/devices/lander bold text
    @{ From = "computer.fon"; To = "tiny.cond.fon"; Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # planet scan condensed
    @{ From = "computer.fon"; To = "micro.fon";     Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # planet info panel labels (Orbit: 等)
    @{ From = "computer.fon"; To = "label.fon";     Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" },  # 面板標題 CARGO/DEVICES/CAPTAIN 等 (hybrid 只加 CJK 不動英文尺寸)
    @{ From = "computer.fon"; To = "lander.fon";    Mode = "hybrid";
       CjkSource = "$root\zh-TW-addon\_intermediate\cjk-fusion-gap" }   # lander/energy 報告螢幕 (Phase 2 patched exe 已修 CJK strlen bug)
    # 停用：playmenu.fon (只用於 3DO 選單模式)
  )
} else {
  Write-Host "  [SkipHybridUI] 略過 7 個 hybrid UI 字型 (省 ~20K files)，UI 面板將顯示英文" -ForegroundColor Yellow
}
foreach ($fr in $fontRedirects) {
  $src = "$stage\shadow-content\base\fonts\$($fr.From)"
  $dst = "$stage\shadow-content\base\fonts\$($fr.To)"
  if (-not (Test-Path $src)) { continue }

  if ($fr.Mode -eq "hybrid") {
    # Hybrid: keep TARGET's original ASCII (from extracted base pack),
    # overlay CJK from either $CjkSource (if provided) or $src.
    $origTarget = "$root\extracted\base\base\fonts\$($fr.To)"
    if (-not (Test-Path $origTarget)) {
      Write-Host "  WARN: original $($fr.To) not found at $origTarget, falling back to full copy" -ForegroundColor Yellow
      if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
      Copy-Item $src $dst -Recurse
      continue
    }
    if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
    # Step 1: seed with the ORIGINAL small font (ASCII glyphs + original kerndat)
    Copy-Item $origTarget $dst -Recurse
    # Step 2: choose CJK source (dedicated smaller-CJK dir if provided)
    $cjkSrc = if ($fr.CjkSource -and (Test-Path $fr.CjkSource)) { $fr.CjkSource } else { $src }
    # Step 3: overlay CJK PNGs (>= 0x80) from CJK source onto TARGET
    $cjkCount = 0
    Get-ChildItem $cjkSrc -Filter "*.png" | Where-Object {
      $_.BaseName -match "^[0-9a-f]+$" -and
      [Convert]::ToInt32($_.BaseName, 16) -ge 128
    } | ForEach-Object {
      Copy-Item $_.FullName $dst -Force
      $cjkCount++
    }
    # Keep target's ORIGINAL kerndat.fnt (do NOT overwrite).
    $tkern = "$dst\kerndat.fnt"
    if (Test-Path $tkern) {
      $firstLine = (Get-Content $tkern -First 1 -Encoding ASCII)
      $cjkSrcName = Split-Path $cjkSrc -Leaf
      Write-Host "Font redirect (hybrid): $($fr.To) = original ASCII + $cjkCount CJK from $cjkSrcName (kerndat: $firstLine)" -ForegroundColor DarkYellow
    }
    continue
  }

  # Mode = "full": completely replace target with source (default old behavior)
  if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
  Copy-Item $src $dst -Recurse
  # Fix kerndat.fnt name field so it matches destination directory.
  $kern = "$dst\kerndat.fnt"
  if (Test-Path $kern) {
    $raw = [System.IO.File]::ReadAllText($kern, [System.Text.Encoding]::ASCII)
    $lines = $raw -split "`r?`n"
    $firstParts = $lines[0] -split ' ', 2
    # Replace the font-name token (first token) with destination filename.
    if ($firstParts.Length -ge 2) {
      $lines[0] = "$($fr.To) $($firstParts[1])"
      [System.IO.File]::WriteAllText($kern, ($lines -join "`n"), [System.Text.Encoding]::ASCII)
    }
  }
  Write-Host "Font redirect (full): $($fr.To) <- $($fr.From)  (+ kerndat name fixed)" -ForegroundColor DarkCyan
}

# Addon RMP:
#   Present at zh-TW/uqm.rmp so loadAddon() reports it (no "No RMP index files"
#   warning). Content is a passthrough — no key remaps because font redirects
#   are handled by shadow-content directory replacement above.
$rmp = @"
# zh-TW addon — shadow-content overrides files by path.
# Font size hacks (small font -> larger font) are done by copying the
# larger font's PNGs+kerndat into the small font's directory in
# shadow-content. See package_zh-TW.ps1 `$fontRedirects.
"@
[System.IO.File]::WriteAllText("$stage\uqm.rmp", $rmp, [System.Text.Encoding]::ASCII)

# Package
$out = "$root\zh-TW-addon\zh-TW.uqm"
$installOut = "$root\install\content\addons\zh-TW.uqm"

if ($NoZip) {
  Write-Host "  [NoZip] Stage prepared at $stage; skipping Compress-Archive." -ForegroundColor Yellow
  Write-Host "  Caller must .NET-zip $stage → $out." -ForegroundColor Yellow
  return
}

Remove-Item $out -Force -ErrorAction SilentlyContinue
Remove-Item $installOut -Force -ErrorAction SilentlyContinue
# Small wait to let any file lock (from previous build) release
Start-Sleep -Milliseconds 200
Push-Location "$root\zh-TW-addon\_stage"
Compress-Archive -Path "zh-TW" -DestinationPath $out -Force -CompressionLevel Optimal
Pop-Location

# Sanity check: archive must contain fresh stage content, not stale.
# Compare a marker file's size in the archive vs on disk.
Add-Type -AssemblyName System.IO.Compression.FileSystem
$stageMarker = Get-ChildItem "$root\zh-TW-addon\_stage\zh-TW\shadow-content\base\comm" -Recurse -Filter "*.txt" -File | Select-Object -First 1
if ($stageMarker) {
  # Compress-Archive with Push-Location _stage packs entries as zh-TW/... .
  # stageMarker.FullName starts with $_stage_prefix which itself ends at zh-TW\;
  # so substring after $_stage_prefix + "zh-TW\" gives shadow-content/... .
  # Correct archive path = "zh-TW/" + relative-below-_stage/zh-TW.
  $stageZhPrefix = "$root\zh-TW-addon\_stage\zh-TW\"
  $relBelowZh = $stageMarker.FullName.Substring($stageZhPrefix.Length).Replace("\", "/")
  $stageRelPath = "zh-TW/" + $relBelowZh
  $archive = [System.IO.Compression.ZipFile]::OpenRead($out)
  $entry = $archive.Entries | Where-Object { $_.FullName -eq $stageRelPath } | Select-Object -First 1
  $entrySize = if ($entry) { $entry.Length } else { -1 }
  $archive.Dispose()
  if ($entrySize -ne $stageMarker.Length) {
    Write-Host "  !!! STALE PACKAGE DETECTED !!!" -ForegroundColor Red
    Write-Host "  Marker: $stageRelPath"
    Write-Host "  Stage size: $($stageMarker.Length)  Archive size: $entrySize"
    Write-Host "  Retrying package after 1s..." -ForegroundColor Yellow
    Remove-Item $out -Force
    Start-Sleep -Seconds 1
    Push-Location "$root\zh-TW-addon\_stage"
    try {
      Compress-Archive -Path "zh-TW" -DestinationPath $out -Force -CompressionLevel Optimal
    } finally {
      Pop-Location
    }
  }
}

Copy-Item $out $installOut -Force

# Zip64 detection — MegaMod's UIO does NOT support Zip64 format.
# Compress-Archive silently switches to Zip64 when entry count > 65,535 or
# archive > 4GB, and the addon then fails to mount with:
#   Error: Zip64 .zip files are not supported.
#   Warning: Could not mount 'zh-TW.uqm': Function not implemented.
# We check the archive's EOCD signature (0x06064b50 for Zip64 EOCD) and warn.
$rawBytes = [System.IO.File]::ReadAllBytes($installOut)
$rawLen = $rawBytes.Length
$hasZip64 = $false
$scanStart = [Math]::Max(0, $rawLen - 65535 - 22)
for ($i = $scanStart; $i -lt $rawLen - 4; $i++) {
  if ($rawBytes[$i] -eq 0x50 -and $rawBytes[$i+1] -eq 0x4b -and $rawBytes[$i+2] -eq 0x06 -and $rawBytes[$i+3] -eq 0x06) {
    $hasZip64 = $true
    break
  }
}
$entryCount = ((& "C:\Program Files\7-Zip\7z.exe" l $installOut 2>&1 | Select-String "(\d+) files, \d+ folders$" | Select-Object -First 1).Matches.Groups[1].Value)
if ($hasZip64) {
  Write-Host ""
  Write-Host "  ⚠️ Addon is Zip64 format (entries=$entryCount, > 65,535 limit)" -ForegroundColor Yellow
  Write-Host "  Original UrQuanMasters.exe does NOT support Zip64 — must use PATCHED exe:" -ForegroundColor Yellow
  Write-Host "    .\install\UrQuanMasters-zip64.exe --windowed --addon zh-TW" -ForegroundColor Cyan
  Write-Host "  (Patch: uqm-work/patches/007-uio-zip64-eocd.patch;" -ForegroundColor DarkGray
  Write-Host "   Applied on UQM-MegaMod source + built as UrQuanMasters-zip64.exe)" -ForegroundColor DarkGray
  Write-Host "  Fallback: rerun with -SkipHybridUI to keep ZIP32 (UI panels revert to English)." -ForegroundColor DarkGray
} else {
  Write-Host ""
  Write-Host "  ✅ ZIP32 format (entries=$entryCount, limit=65535) — 相容原版 exe" -ForegroundColor Green
}

$size = (Get-Item $out).Length
Write-Host ""
Write-Host "==== v0.1 zh-TW addon 完成 (shadow-content 版) ====" -ForegroundColor Green
Write-Host "檔案：$out"
Write-Host "大小：$([math]::Round($size/1KB,1)) KB"
Write-Host ""
Write-Host "==== ZIP 結構檢查 ====" -ForegroundColor Cyan
& "C:\Program Files\7-Zip\7z.exe" l $out | Select-String -Pattern "uqm\.rmp|gamestrings\.txt|setupmenu\.txt|slab\.fon\\00041" | Select-Object -First 6
Write-Host ""
Write-Host "==== 執行測試 ====" -ForegroundColor Yellow
Write-Host ""
Write-Host "  cd $root\install"
Write-Host "  .\UrQuanMasters.exe --windowed --addon zh-TW"
Write-Host ""
Write-Host "  v0.3 範圍："
Write-Host "    ✓ 主選單：新遊戲 / 讀取存檔 / 設定 / 離開（Bold 中文）"
Write-Host "    ✓ 開場動畫：戰役無數，浩瀚無比…（slides.fon 20px 中文）"
Write-Host "    ✓ Ur-Quan 警告：入侵者請注意…（urquan.fon 16px 中文）"
Write-Host "    ✓ Cdr. Hayes 首見對白 17 條（RMP 重導 → computer.fon 15px）"
Write-Host "    ✗ Setup 選單：保留英文（字型太小）"

} finally {
    Exit-BuildLock
}
