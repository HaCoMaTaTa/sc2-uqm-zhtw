# Cheat launch: try to jump directly to shofixti encounter via debug flags.
# UQM debug supports --loadsave to load a specific save, but we don't have one.
# Fallback: just launch and let user manually trigger.
# For now this is just a helper that launches then delays before screenshot.

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$exe = "Q:\Dos_G\StarControl2\uqm-work\install\UrQuanMasters.exe"
$cwd = "Q:\Dos_G\StarControl2\uqm-work\install"
$outPath = if ($env:UQM_SHOT_OUT) { $env:UQM_SHOT_OUT } else { "Q:\Dos_G\StarControl2\uqm-work\_shot.png" }
$delay = if ($env:UQM_DELAY_SEC) { [int]$env:UQM_DELAY_SEC } else { 8 }

$launchArgs = @("--windowed", "--addon", "zh-TW", "--logfile", "game_shot.log", "--skipintro")
Write-Host "Launching. Delay $delay s before screenshot (navigate manually in that window)..."
$p = Start-Process $exe -ArgumentList $launchArgs -WorkingDirectory $cwd -PassThru -WindowStyle Normal
Start-Sleep -Seconds $delay
if ($p.HasExited) {
    Write-Host "Game exited early" -ForegroundColor Red; exit 1
}
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen(0, 0, 0, 0, (New-Object System.Drawing.Size $screen.Width, $screen.Height))
$g.Dispose()
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Host "Saved: $outPath" -ForegroundColor Green
Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
