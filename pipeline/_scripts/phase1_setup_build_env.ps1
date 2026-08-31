# Phase 1: MSYS2 + MinGW-w64 + SDL2 build environment setup for UQM MegaMod
# ---------------------------------------------------------------------------
# Goal: enable rebuilding UrQuanMasters.exe with our report.c UTF-8 patch.
# Run this manually (needs UAC for winget install). ~1-2 hours total.
# All output is ASCII to avoid PowerShell 5.x ANSI-vs-UTF-8 parsing issues.
# ---------------------------------------------------------------------------

$ErrorActionPreference = "Stop"

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host " UQM MegaMod build environment setup -- Phase 1" -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# ---------------------------------------------------------------------------
# Step 1: Check / install MSYS2
# ---------------------------------------------------------------------------
$msys2Root = "C:\msys64"
$msys2Bash = "$msys2Root\usr\bin\bash.exe"

Write-Host "== Step 1: MSYS2 =====================================" -ForegroundColor Yellow
if (Test-Path $msys2Bash) {
    Write-Host "  [OK] MSYS2 already installed at $msys2Root" -ForegroundColor Green
}
else {
    Write-Host "  Installing MSYS2 via winget (~200 MB download, needs UAC)..." -ForegroundColor White
    winget install --id MSYS2.MSYS2 --accept-source-agreements --accept-package-agreements
    if (-not (Test-Path $msys2Bash)) {
        Write-Host "  [FAIL] MSYS2 install failed. Manual download: https://www.msys2.org/" -ForegroundColor Red
        exit 1
    }
    Write-Host "  [OK] MSYS2 installed" -ForegroundColor Green
}
Write-Host ""

# ---------------------------------------------------------------------------
# Step 2: Update MSYS2 & install UCRT64 toolchain + SDL2 stack
# ---------------------------------------------------------------------------
Write-Host "== Step 2: Update MSYS2 + install packages ===========" -ForegroundColor Yellow
Write-Host "  This runs pacman inside MSYS2 shell (may take 10-20 min)." -ForegroundColor White
Write-Host ""

# Packages we need for UQM-MegaMod build:
#   - Toolchain: gcc, make, cmake, pkg-config
#   - SDL2 stack: SDL2, SDL2_image, SDL2_mixer (with vorbis/ogg support)
#   - Support libs: zlib, libpng, libvorbis, libogg
# UCRT64 subsystem (modern Windows CRT) is recommended over MinGW64.
$pkgs = @(
    "mingw-w64-ucrt-x86_64-toolchain",
    "mingw-w64-ucrt-x86_64-cmake",
    "mingw-w64-ucrt-x86_64-make",
    "mingw-w64-ucrt-x86_64-pkgconf",
    "mingw-w64-ucrt-x86_64-SDL2",
    "mingw-w64-ucrt-x86_64-SDL2_image",
    "mingw-w64-ucrt-x86_64-SDL2_mixer",
    "mingw-w64-ucrt-x86_64-SDL2_net",
    "mingw-w64-ucrt-x86_64-libpng",
    "mingw-w64-ucrt-x86_64-zlib",
    "mingw-w64-ucrt-x86_64-libvorbis",
    "mingw-w64-ucrt-x86_64-libogg"
)

# First update package DB (may require rerun after keyring update)
& $msys2Bash -lc "pacman -Syu --noconfirm" 2>&1 | Select-Object -Last 5

# Then install our packages
$pkgList = $pkgs -join " "
Write-Host "  Installing: $pkgList" -ForegroundColor White
& $msys2Bash -lc "pacman -S --needed --noconfirm $pkgList" 2>&1 | Select-Object -Last 10
Write-Host ""

# ---------------------------------------------------------------------------
# Step 3: Verify tools present
# ---------------------------------------------------------------------------
Write-Host "== Step 3: Verify toolchain ==========================" -ForegroundColor Yellow
$checks = @(
    @{ Cmd = "gcc --version"; Label = "GCC (UCRT64)" },
    @{ Cmd = "cmake --version"; Label = "CMake" },
    @{ Cmd = "make --version"; Label = "Make" },
    @{ Cmd = "pkg-config --modversion sdl2"; Label = "SDL2 pkg" }
)
foreach ($c in $checks) {
    # Run inside UCRT64 login shell to get correct PATH
    $result = & $msys2Bash -lc "export MSYSTEM=UCRT64; source /etc/profile; $($c.Cmd) 2>&1 | head -1"
    if ($LASTEXITCODE -eq 0) {
        Write-Host ("  [OK]   {0,-16}: {1}" -f $c.Label, $result) -ForegroundColor Green
    }
    else {
        Write-Host ("  [FAIL] {0,-16}: MISSING" -f $c.Label) -ForegroundColor Red
    }
}
Write-Host ""

# ---------------------------------------------------------------------------
# Step 4: Try VANILLA build first (no patch) to confirm environment
# ---------------------------------------------------------------------------
Write-Host "== Step 4: Vanilla build test ========================" -ForegroundColor Yellow
Write-Host "  Attempting to build unpatched MegaMod to verify environment..." -ForegroundColor White
Write-Host "  (This may take 5-15 min for first build)" -ForegroundColor White
Write-Host ""

$srcDirUnix = "/q/Dos_G/StarControl2/UQM-MegaMod"

$buildCmd = @"
export MSYSTEM=UCRT64
source /etc/profile
cd $srcDirUnix
if [ -f cmake-build.sh ]; then
  bash cmake-build.sh 2>&1 | tail -30
else
  echo 'cmake-build.sh not found; falling back to build.sh'
  bash build.sh uqm 2>&1 | tail -30
fi
"@
& $msys2Bash -lc $buildCmd

Write-Host ""
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host " Phase 1 done. If Step 4 succeeded, report back -- Phase 2" -ForegroundColor Cyan
Write-Host " will apply the report.c UTF-8 patch and rebuild." -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
