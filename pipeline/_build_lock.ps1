# _build_lock.ps1 — Mutex-based coordination for concurrent build / package sessions.
#
# Purpose:
#   Two Copilot sessions (or human + AI) running build_zh-TW.ps1 or
#   package_zh-TW.ps1 simultaneously can trash each other's output:
#     - Session A deletes zh-TW-addon/content/ while B is writing it
#     - Both rasterize fonts into the same PNG dir → mixed / corrupt output
#     - Both Compress-Archive to zh-TW.uqm → file lock, partial zip
#
# Solution:
#   A Windows kernel-level named mutex named "SC2-zhTW-build" (Global scope
#   so it's visible across all terminals/sessions on the machine). Any script
#   that touches zh-TW-addon/ must:
#     . "$PSScriptRoot\_build_lock.ps1"
#     Enter-BuildLock
#     try { ... } finally { Exit-BuildLock }
#
#   The mutex handles all the tricky parts automatically:
#     - Race-free acquisition (kernel primitive, atomic)
#     - Auto-release on process crash (AbandonedMutexException recovered)
#     - Cross-session visibility (Global\ prefix)
#     - No stale lock files to clean up

$script:BuildMutex = $null
$script:MutexAcquired = $false
$script:MutexName = $null

function Enter-BuildLock {
    param(
        [string]$Name = "SC2-zhTW-build",
        [int]$TimeoutSeconds = 900
    )

    if ($script:MutexAcquired) {
        # Already in lock — allow re-entry (build.ps1 calls package.ps1 etc.)
        return
    }

    $mutexName = "Global\$Name"
    $script:MutexName = $mutexName
    $script:BuildMutex = New-Object System.Threading.Mutex($false, $mutexName)

    Write-Host "  [lock] acquiring $mutexName (PID $PID)... " -NoNewline -ForegroundColor Cyan
    $waitStart = Get-Date

    try {
        $script:MutexAcquired = $script:BuildMutex.WaitOne([TimeSpan]::FromSeconds($TimeoutSeconds))
    } catch [System.Threading.AbandonedMutexException] {
        # Previous holder crashed. Windows released the mutex and we now own it.
        # Any half-written stage/content is the caller's responsibility to clean.
        Write-Host "(recovered from abandoned) " -NoNewline -ForegroundColor Yellow
        $script:MutexAcquired = $true
    }

    if (-not $script:MutexAcquired) {
        Write-Host "TIMEOUT" -ForegroundColor Red
        throw "Failed to acquire build lock within $TimeoutSeconds seconds — another session may be stuck. Check other terminals or use Get-Process to find a hung powershell/python."
    }

    $elapsed = ((Get-Date) - $waitStart).TotalSeconds
    if ($elapsed -lt 0.5) {
        Write-Host "ok" -ForegroundColor Green
    } else {
        Write-Host "ok (waited $([math]::Round($elapsed, 1))s)" -ForegroundColor Green
    }
}

function Exit-BuildLock {
    if ($script:MutexAcquired -and $script:BuildMutex) {
        try {
            $script:BuildMutex.ReleaseMutex()
            Write-Host "  [lock] released $($script:MutexName) (PID $PID)" -ForegroundColor DarkGray
        } catch {
            Write-Host "  [lock] release warning: $_" -ForegroundColor Yellow
        }
        try {
            $script:BuildMutex.Dispose()
        } catch {}
        $script:MutexAcquired = $false
        $script:BuildMutex = $null
        $script:MutexName = $null
    }
}

# Register a script-scope cleanup so a Ctrl-C or exception still releases the lock.
# Note: for `. sourcing` scripts, the caller should also use try/finally.
$ExecutionContext.SessionState.PSVariable.Set("BuildLockLoaded", $true)
