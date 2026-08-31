# =====================================================================
# verify_and_scan.ps1 — 產 SHA256 + 準備 VirusTotal 上傳
#
# 對每個指定檔案：
#   1. 計算 SHA256 → *.sha256 檔
#   2. 產出 docs/Security_Scan_Report.md 半成品（含 hash / 檔案大小 / VirusTotal 提示 URL）
#   3. 開啟瀏覽器到 VirusTotal upload 頁面（可 --NoOpen 略過）
#
# 用法：
#   .\scripts\verify_and_scan.ps1                                    # 掃預設清單
#   .\scripts\verify_and_scan.ps1 -Files 'path/to/foo.apk','bar.zip' # 自訂
# =====================================================================

[CmdletBinding()]
param(
    [string[]]$Files,
    [switch]$NoOpen,
    [string]$OutReport
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir
if (-not $OutReport) { $OutReport = Join-Path $repoRoot 'docs\Security_Scan_Report.md' }

# ---- 預設清單（可覆寫）---------------------------------------------
if (-not $Files -or $Files.Count -eq 0) {
    Write-Host "未指定 -Files。請提供要掃描的檔案：" -ForegroundColor Yellow
    Write-Host "  .\scripts\verify_and_scan.ps1 -Files 'C:\path\file.apk','C:\path\file.zip'"
    Write-Host ""
    Write-Host "常見位置："
    Write-Host "  Android APK: <workspace>\Android\release\激戰M星雲II-v3.8-release-*.apk"
    Write-Host "  PC ZIP:      <workspace>\uqm-work\release\output\SC2-zhTW-*.zip"
    exit 1
}

Write-Host ""
Write-Host "=== SHA256 + VirusTotal 準備 ===" -ForegroundColor Cyan

$results = @()
foreach ($f in $Files) {
    if (-not (Test-Path $f)) {
        Write-Host "✗ 檔案不存在: $f" -ForegroundColor Red
        continue
    }
    $item = Get-Item $f
    Write-Host ""
    Write-Host "→ $($item.Name)" -ForegroundColor Cyan
    Write-Host "  Path:  $($item.FullName)"
    Write-Host "  Size:  $([math]::Round($item.Length/1MB,2)) MB"

    $hash = (Get-FileHash $f -Algorithm SHA256).Hash.ToLower()
    Write-Host "  SHA256: $hash" -ForegroundColor Green

    # 寫 sidecar .sha256
    $sha256File = "$($item.FullName).sha256"
    "$hash *$($item.Name)" | Set-Content -Path $sha256File -Encoding ascii
    Write-Host "  Wrote:  $sha256File"

    # 打包成 result
    $results += [pscustomobject]@{
        Name = $item.Name
        Path = $item.FullName
        SizeMB = [math]::Round($item.Length/1MB, 2)
        SHA256 = $hash
        VirusTotalGui = "https://www.virustotal.com/gui/file/$hash"
    }
}

# ---- 寫 Security_Scan_Report 半成品 --------------------------------
$now = Get-Date -Format 'yyyy-MM-dd HH:mm'
$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("# APK / ZIP 安全掃描報告")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("> **掃描時間**: $now")
[void]$sb.AppendLine("> **掃描服務**: VirusTotal (<https://www.virustotal.com>)")
[void]$sb.AppendLine("> **報告狀態**: SHA256 已產生 · VirusTotal URL 待手動上傳確認")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## 檔案清單")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| 檔案 | 大小 (MB) | SHA256 | VirusTotal 報告 |")
[void]$sb.AppendLine("|---|---:|---|---|")
foreach ($r in $results) {
    [void]$sb.AppendLine("| $($r.Name) | $($r.SizeMB) | ``$($r.SHA256)`` | [檢視]($($r.VirusTotalGui)) |")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## 手動掃描步驟")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("1. 開啟 <https://www.virustotal.com/gui/home/upload>")
[void]$sb.AppendLine("2. 拖曳上表任一檔案上傳（若表格內 URL 已顯示掃過結果，直接檢視即可）")
[void]$sb.AppendLine("3. 等待掃描完成（每檔約 1 分鐘）")
[void]$sb.AppendLine("4. 複製結果頁 URL → 貼回本檔對應列的『VirusTotal 報告』欄")
[void]$sb.AppendLine("5. commit 本檔更新")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## APK 權限清單（僅供對照 · release 版）")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| 權限 | 用途 |")
[void]$sb.AppendLine("|---|---|")
[void]$sb.AppendLine("| `WAKE_LOCK` | 玩遊戲時螢幕不睡（`EngineActivity.setKeepScreenOn`）|")
[void]$sb.AppendLine("| `VIBRATE` | 未來 haptic 預留（目前未觸發）|")
[void]$sb.AppendLine("| `WRITE_EXTERNAL_STORAGE` (maxSdkVersion=29) | 舊 Android 相容（Android 10+ 自動忽略）|")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("**已移除**（過去版本曾有，v1.5 起清理）：`INTERNET`, `MANAGE_EXTERNAL_STORAGE`, `PACKAGE_USAGE_STATS`, `DUMP`, `READ_EXTERNAL_STORAGE`")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## 常見誤判說明")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("- **VirusTotal < 5 引擎警告**：屬正常範圍。自簽 APK + 大量 native lib (libSDL2/libpng/libvorbis) + Zip64 asset 常被啟發式引擎誤判")
[void]$sb.AppendLine("- **Windows Defender SmartScreen**：因 exe 未購買 Authenticode 簽章，右鍵 → 內容 → 解除封鎖即可")
[void]$sb.AppendLine("- **Android Play Protect 警告**：因非 Play Store 來源；設定裡明確 allow 即可")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("如發現任何真的可疑報告，請開 GitHub Issue 附上 VirusTotal 連結，我會第一時間查看。")

$outDir = Split-Path -Parent $OutReport
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }
$sb.ToString() | Set-Content -Path $OutReport -Encoding utf8
Write-Host ""
Write-Host "=== 完成 ===" -ForegroundColor Cyan
Write-Host "半成品報告: $OutReport" -ForegroundColor Green
Write-Host ""
Write-Host "下一步："
foreach ($r in $results) {
    Write-Host "  上傳 $($r.Name) 到 <https://www.virustotal.com/gui/home/upload>" -ForegroundColor Yellow
    Write-Host "    掃完後 URL 貼回：$OutReport"
}

# ---- 開瀏覽器 ------------------------------------------------------
if (-not $NoOpen) {
    Start-Process 'https://www.virustotal.com/gui/home/upload'
}
