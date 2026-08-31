# Launch, navigate to moonbase report screen, then screenshot.
# Skill hack: use debug jump via GLOBAL flags... too complex. Instead we launch
# and screenshot after user manually navigates.

# For automated: use cheats + starting position to speed-jump.
# Simpler: rely on --skipintro + moonbase auto-encounter behavior isn't possible.

# For now: user will manually navigate; this script just captures the screen.
# Usage: run this while game is showing report. Or use param $env:UQM_DELAY.

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$outPath = if ($env:UQM_SHOT_OUT) { $env:UQM_SHOT_OUT } else { "Q:\Dos_G\StarControl2\uqm-work\_shot.png" }
$delaySec = if ($env:UQM_DELAY) { [int]$env:UQM_DELAY } else { 5 }

Write-Host "Waiting $delaySec seconds before screenshot..."
Start-Sleep -Seconds $delaySec

$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen(0, 0, 0, 0, (New-Object System.Drawing.Size $screen.Width, $screen.Height))
$g.Dispose()
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()

Write-Host "Saved: $outPath" -ForegroundColor Green
