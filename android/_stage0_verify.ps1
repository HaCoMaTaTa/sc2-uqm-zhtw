# Stage 0 environment verification script.
# Usage: cd Q:\Dos_G\StarControl2\Android; .\_stage0_verify.ps1
#
# Checks every requirement from plan/01_stage0_runbook.md and prints
# a colored PASS/FAIL matrix. Exit code 0 = all pass, 1 = something missing.

$ErrorActionPreference = 'Continue'
$script:pass = 0
$script:fail = 0

function Test-Item {
    param(
        [string]$Name,
        [scriptblock]$Check,
        [string]$Detail = ''
    )
    try {
        $ok = & $Check
    } catch {
        $ok = $false
    }
    $status = if ($ok) { '[ OK ]' } else { '[FAIL]' }
    $color = if ($ok) { 'Green' } else { 'Red' }
    Write-Host ('  {0}  {1}' -f $status, $Name) -ForegroundColor $color -NoNewline
    if ($Detail) { Write-Host ('  · ' + $Detail) -ForegroundColor DarkGray } else { Write-Host '' }
    if ($ok) { $script:pass++ } else { $script:fail++ }
    return $ok
}

Write-Host '=== Stage 0 verification ===' -ForegroundColor Cyan
Write-Host ''

Write-Host '-- 1. Android Studio installation --' -ForegroundColor Cyan
$studioExe = 'C:\Program Files\Android\Android Studio\bin\studio64.exe'
$jbrPath   = 'C:\Program Files\Android\Android Studio\jbr'
# Build tools JDK: Temurin 21 (Gradle 8.14.3 doesn't support Studio's bundled JBR 25).
$buildJdk  = (Get-ChildItem 'Q:\Dos_G\StarControl2\Android\jdk21' -Directory -ErrorAction SilentlyContinue | Select-Object -First 1).FullName
Test-Item 'Android Studio installed'  { Test-Path $studioExe } $studioExe | Out-Null
Test-Item 'Bundled JBR present'       { Test-Path (Join-Path $jbrPath 'bin\java.exe') } $jbrPath | Out-Null
Test-Item 'Build JDK 21 present'      { $buildJdk -and (Test-Path (Join-Path $buildJdk 'bin\java.exe')) } $buildJdk | Out-Null

Write-Host ''
Write-Host '-- 2. SDK layout (Q:\...\Android\sdk) --' -ForegroundColor Cyan
$sdk = 'Q:\Dos_G\StarControl2\Android\sdk'
Test-Item 'SDK root exists'           { Test-Path $sdk } $sdk | Out-Null
Test-Item 'platform-tools\adb.exe'    { Test-Path "$sdk\platform-tools\adb.exe" } | Out-Null
Test-Item 'cmdline-tools\latest'      { Test-Path "$sdk\cmdline-tools\latest\bin\sdkmanager.bat" } | Out-Null
Test-Item 'emulator\emulator.exe'     { Test-Path "$sdk\emulator\emulator.exe" } | Out-Null

# Platform check: any of API 34/35/36 acceptable, prefer 34+36
$plats = @()
if (Test-Path "$sdk\platforms") {
    $plats = (Get-ChildItem "$sdk\platforms" -Directory -ErrorAction SilentlyContinue).Name
}
Test-Item 'Platform API 34 (Android 14 baseline)' { $plats -contains 'android-34' } "installed: $($plats -join ', ')" | Out-Null
Test-Item 'Platform API 36 (compileSdk)'          { $plats -contains 'android-36' } | Out-Null

# NDK: prefer r27.x
$ndks = @()
if (Test-Path "$sdk\ndk") {
    $ndks = (Get-ChildItem "$sdk\ndk" -Directory -ErrorAction SilentlyContinue).Name
}
Test-Item 'NDK r27.x installed' { ($ndks | Where-Object { $_ -match '^27\.' }).Count -gt 0 } "installed: $($ndks -join ', ')" | Out-Null

# CMake: prefer 3.22.1 (MegaMod scaffold requested)
$cmakes = @()
if (Test-Path "$sdk\cmake") {
    $cmakes = (Get-ChildItem "$sdk\cmake" -Directory -ErrorAction SilentlyContinue).Name
}
Test-Item 'CMake 3.22.x installed' { ($cmakes | Where-Object { $_ -match '^3\.22' }).Count -gt 0 } "installed: $($cmakes -join ', ')" | Out-Null

# Build-Tools
$bt = @()
if (Test-Path "$sdk\build-tools") {
    $bt = (Get-ChildItem "$sdk\build-tools" -Directory -ErrorAction SilentlyContinue).Name
}
Test-Item 'Build-Tools present' { $bt.Count -gt 0 } "installed: $($bt -join ', ')" | Out-Null

Write-Host ''
Write-Host '-- 3. Environment variables --' -ForegroundColor Cyan
Test-Item 'ANDROID_HOME set'   { $env:ANDROID_HOME -eq $sdk -or [Environment]::GetEnvironmentVariable('ANDROID_HOME','User') -eq $sdk } "want: $sdk" | Out-Null
Test-Item 'JAVA_HOME set (JDK 21)' {
    $u = [Environment]::GetEnvironmentVariable('JAVA_HOME','User')
    ($env:JAVA_HOME -eq $buildJdk) -or ($u -eq $buildJdk)
} "want: $buildJdk" | Out-Null

# PATH check (User scope)
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
Test-Item 'PATH has platform-tools' { $userPath -like "*$sdk\platform-tools*" } | Out-Null
Test-Item 'PATH has cmdline-tools'  { $userPath -like "*$sdk\cmdline-tools\latest\bin*" } | Out-Null

Write-Host ''
Write-Host '-- 4. Live tool check (fresh PATH after restart) --' -ForegroundColor Cyan
foreach ($tool in @('adb','sdkmanager','emulator')) {
    $g = Get-Command $tool -ErrorAction SilentlyContinue
    Test-Item ('{0} on PATH' -f $tool) { $null -ne $g } $(if($g){$g.Source}) | Out-Null
}

Write-Host ''
Write-Host '-- 5. AVDs --' -ForegroundColor Cyan
$avds = @()
try {
    $emu = "$sdk\emulator\emulator.exe"
    if (Test-Path $emu) {
        $avds = & $emu -list-avds 2>$null
    }
} catch { }
Test-Item 'At least one AVD created' { $avds.Count -gt 0 } "avds: $($avds -join ', ')" | Out-Null

Write-Host ''
Write-Host '-- 6. Gradle project sync (MegaMod build/android) --' -ForegroundColor Cyan
$gradleRoot = 'Q:\Dos_G\StarControl2\UQM-MegaMod\build\android'
Test-Item 'MegaMod Android project exists'   { Test-Path "$gradleRoot\build.gradle.kts" } $gradleRoot | Out-Null
Test-Item 'Gradle wrapper present'            { Test-Path "$gradleRoot\gradlew.bat" } | Out-Null
# Sync artifact hint: after first sync, .gradle/ dir appears with cache
Test-Item 'Gradle project has synced (once)' {
    (Test-Path "$gradleRoot\.gradle") -or (Test-Path "$gradleRoot\.idea")
} 'exists after first Android Studio Open+Sync' | Out-Null

Write-Host ''
Write-Host '=== Summary ===' -ForegroundColor Cyan
Write-Host ("  Passed: {0}   Failed: {1}" -f $script:pass, $script:fail) -ForegroundColor $(if($script:fail -eq 0){'Green'}else{'Yellow'})
if ($script:fail -eq 0) {
    Write-Host '  Stage 0 COMPLETE.' -ForegroundColor Green
    exit 0
} else {
    Write-Host '  Stage 0 not yet complete. See plan/01_stage0_runbook.md.' -ForegroundColor Yellow
    exit 1
}
