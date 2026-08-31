# Screenshot UQM game window. Move it to (0,0) first so terminal doesn't overlap,
# then use pure CopyFromScreen (works cleanly since game is now unobstructed).
# NOTE: run in a FRESH pwsh session (`pwsh -NoProfile -File ...`) to avoid
# PowerShell Add-Type class caching from prior runs.

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Text;
public class UqmShot {
    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);
    [DllImport("user32.dll")]
    public static extern int GetWindowText(IntPtr hWnd, StringBuilder text, int count);
    [DllImport("user32.dll")]
    public static extern bool EnumWindows(EnumWindowsProc enumProc, IntPtr lParam);
    public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);
    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint lpdwProcessId);
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool SetWindowPos(IntPtr hWnd, IntPtr hWndInsertAfter,
        int X, int Y, int cx, int cy, uint uFlags);
    public const uint SWP_NOSIZE = 0x0001;
    public const uint SWP_NOZORDER = 0x0004;
    public const uint SWP_SHOWWINDOW = 0x0040;
}
public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
"@

$exe = "Q:\Dos_G\StarControl2\uqm-work\install\UrQuanMasters.exe"
$cwd = "Q:\Dos_G\StarControl2\uqm-work\install"
$launchArgs = @("--windowed", "--logfile", "game_shot.log", "--skipintro")
if ($env:UQM_ADDON) { $launchArgs += @("--addon", $env:UQM_ADDON) }
$outPath = if ($env:UQM_SHOT_OUT) { $env:UQM_SHOT_OUT } else { "Q:\Dos_G\StarControl2\uqm-work\_shot.png" }

Write-Host "Launching: $exe $($launchArgs -join ' ')"
$p = Start-Process $exe -ArgumentList $launchArgs -WorkingDirectory $cwd -PassThru -WindowStyle Normal
Start-Sleep -Seconds 5
if ($p.HasExited) {
    Write-Host "  [FAIL] game exited early, ExitCode=$($p.ExitCode)" -ForegroundColor Red
    exit 1
}

$targetHwnd = [IntPtr]::Zero
$callback = [UqmShot+EnumWindowsProc]{
    param($hWnd, $lParam)
    $winPid = 0
    [UqmShot]::GetWindowThreadProcessId($hWnd, [ref]$winPid) | Out-Null
    if ($winPid -eq $p.Id) {
        $sb = New-Object System.Text.StringBuilder 256
        [UqmShot]::GetWindowText($hWnd, $sb, 256) | Out-Null
        if ($sb.Length -gt 0 -and $sb.ToString() -like "*Ur-Quan*") {
            $script:targetHwnd = $hWnd
            return $false
        }
    }
    return $true
}
[UqmShot]::EnumWindows($callback, [IntPtr]::Zero) | Out-Null

if ($targetHwnd -eq [IntPtr]::Zero) {
    Write-Host "  [FAIL] no game window" -ForegroundColor Red
    Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
    exit 1
}

# Move game to (0,0) so nothing overlaps
[UqmShot]::SetWindowPos($targetHwnd, [IntPtr]::Zero, 0, 0, 0, 0,
    [UqmShot]::SWP_NOSIZE -bor [UqmShot]::SWP_NOZORDER) | Out-Null
[UqmShot]::SetForegroundWindow($targetHwnd) | Out-Null
Start-Sleep -Milliseconds 800

# Capture entire primary screen (simpler, no window rect nonsense)
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
Write-Host "  screen: $($screen.Width) x $($screen.Height)"

$bmp = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen(0, 0, 0, 0, (New-Object System.Drawing.Size $screen.Width, $screen.Height))
$g.Dispose()
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Host "  saved: $outPath" -ForegroundColor Green

Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
Start-Sleep -Milliseconds 500  # let process fully release exe file lock
