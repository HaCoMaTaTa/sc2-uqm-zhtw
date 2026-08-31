# MegaMod v0.8.5 下載腳本
#
# 用法：
#   .\download_megamod.ps1                # 互動：選擇要下載的組合
#   .\download_megamod.ps1 -Preset Minimum  # 只下載主安裝檔 + 基本 content
#   .\download_megamod.ps1 -Preset Recommended  # 加上 HD、3DO 語音、3DO 音樂
#   .\download_megamod.ps1 -Preset All      # 全部下載
#   .\download_megamod.ps1 -DryRun          # 只顯示會下載什麼，不實際抓
#
# 檔案清單來源：SourceForge RSS 於 2026-08-04 實測驗證。

[CmdletBinding()]
param(
  [ValidateSet("Minimum","Recommended","All","Ask")]
  [string]$Preset = "Ask",
  [switch]$DryRun,
  [switch]$Force,
  [string]$OutDir = (Join-Path $PSScriptRoot "downloads")
)

$ErrorActionPreference = "Stop"
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

# 所有可下載檔案（實測自 SF RSS）
$catalog = @(
  # === 必需 ===
  @{ Group="Minimum"; File="mm-0.8.5-installer.exe";                     Path="MegaMod/0.8.5";         Desc="Windows 主安裝檔（含執行檔）" }
  @{ Group="Minimum"; File="mm-0.8.5-content.uqm";                       Path="MegaMod/0.8.5/content"; Desc="基本遊戲內容（必需）" }

  # === 強烈建議 ===
  @{ Group="Recommended"; File="mm-0.8.5-hd-content.uqm";                Path="MegaMod/0.8.5/content"; Desc="HD 圖形內容（MegaMod 主打功能）" }
  @{ Group="Recommended"; File="mm-0.8.5-hd-classic-pack.uqm";           Path="MegaMod/0.8.5/content"; Desc="HD Classic 風格套件" }
  @{ Group="Recommended"; File="mm-0.8.4-3dovoice.uqm";                  Path="MegaMod/0.8.5/content"; Desc="3DO 全語音包（SC2 名聲所在）" }
  @{ Group="Recommended"; File="uqm-0.8.0-3DOMusicRemastered.uqm";       Path="MegaMod/0.8.5/content"; Desc="3DO 音樂高清版" }
  @{ Group="Recommended"; File="mm-0.8.4-MelnormeVoiceFix.uqm";          Path="MegaMod/0.8.5/content"; Desc="Melnorme 語音修正" }
  @{ Group="Recommended"; File="mm-0.8.4-SyreenVoiceFix.uqm";            Path="MegaMod/0.8.5/content"; Desc="Syreen 語音修正" }

  # === 可選 ===
  @{ Group="Optional"; File="mm-0.8.5-3domode.uqm";                      Path="MegaMod/0.8.5/content"; Desc="3DO UI 風格模式" }
  @{ Group="Optional"; File="mm-0.8.5-dosmode.uqm";                      Path="MegaMod/0.8.5/content"; Desc="DOS UI 風格模式（懷舊）" }
  @{ Group="Optional"; File="uqm-0.8.0-3dovideo.uqm";                    Path="MegaMod/0.8.5/content"; Desc="3DO 影片段（結局動畫等）" }
  @{ Group="Optional"; File="mm-0.8.4-volasaurus-space-music.uqm";       Path="MegaMod/0.8.5/content"; Desc="Volasaurus 太空音樂" }
  @{ Group="Optional"; File="mm-0.8.4-volasaurus-remix-pack.uqm";        Path="MegaMod/0.8.5/content"; Desc="Volasaurus Remix 音樂" }
  @{ Group="Optional"; File="mm-0.8.4-sol-textures.uqm";                 Path="MegaMod/0.8.5/content"; Desc="Sol 星系高解析材質" }
  @{ Group="Optional"; File="mm-0.8.4-distorted-hayes-audio.uqm";        Path="MegaMod/0.8.5/content"; Desc="Cdr. Hayes 失真音效" }
  @{ Group="Optional"; File="mm-0.8.4-purple-urquan-background.uqm";     Path="MegaMod/0.8.5/content"; Desc="紫色 Ur-Quan 背景（懷舊 3DO）" }
  @{ Group="Optional"; File="mm-0.8.4-rmx-utwig.uqm";                    Path="MegaMod/0.8.5/content"; Desc="Utwig Remix 音樂" }
  @{ Group="Optional"; File="mm-remix-timing.uqm";                       Path="MegaMod/0.8.5/content"; Desc="Remix 時序修正" }
)

# === 互動選單 ===
if ($Preset -eq "Ask") {
  Write-Host ""
  Write-Host "==== MegaMod v0.8.5 下載清單 ====" -ForegroundColor Cyan
  Write-Host " 1) Minimum       主安裝 + 基本內容（最小可跑）" -ForegroundColor White
  Write-Host " 2) Recommended   Minimum + HD + 3DO 語音 + 3DO 音樂 + 語音修正（強烈建議）" -ForegroundColor Green
  Write-Host " 3) All           全部（含所有可選 remix / mode 檔）" -ForegroundColor White
  Write-Host " 4) Cancel        取消" -ForegroundColor White
  Write-Host ""
  $choice = Read-Host "選擇 (1/2/3/4)"
  switch ($choice) {
    "1" { $Preset = "Minimum" }
    "2" { $Preset = "Recommended" }
    "3" { $Preset = "All" }
    default { Write-Host "已取消。" -ForegroundColor Yellow; exit 0 }
  }
}

$selected = switch ($Preset) {
  "Minimum"     { $catalog | Where-Object { $_.Group -eq "Minimum" } }
  "Recommended" { $catalog | Where-Object { $_.Group -in @("Minimum","Recommended") } }
  "All"         { $catalog }
}

Write-Host ""
Write-Host "==== 將要下載 $($selected.Count) 個檔案到：$OutDir ====" -ForegroundColor Cyan
$selected | ForEach-Object { Write-Host ("  {0,-45} - {1}" -f $_.File, $_.Desc) }
Write-Host ""

if ($DryRun) { Write-Host "[DryRun] 未實際下載。" -ForegroundColor Yellow; exit 0 }

if (-not $Force) {
  $confirm = Read-Host "確認下載？(y/N)"
  if ($confirm -notmatch "^[yY]") { Write-Host "已取消。" -ForegroundColor Yellow; exit 0 }
}

# === 開始下載 ===
$success = 0; $skipped = 0; $failed = 0
foreach ($it in $selected) {
  $target = Join-Path $OutDir $it.File
  $url    = "https://sourceforge.net/projects/uqm-mods/files/$($it.Path)/$($it.File)/download"

  Write-Host ""
  Write-Host "-- $($it.File)" -ForegroundColor Yellow
  if ((Test-Path $target) -and (Get-Item $target).Length -gt 0) {
    Write-Host "   已存在 ($([math]::Round((Get-Item $target).Length / 1MB, 1)) MB)，略過" -ForegroundColor DarkGray
    $skipped++; continue
  }
  try {
    # 使用 curl.exe（Windows 10+ 內建）能更好處理 SF 的多次 302 redirect 與 mirror
    & curl.exe -L -o "$target" -A "Mozilla/5.0 UQM-zh-TW-downloader" -# "$url"
    if ($LASTEXITCODE -ne 0) { throw "curl exit $LASTEXITCODE" }
    $sz = [math]::Round((Get-Item $target).Length / 1MB, 1)
    # 簡單驗證：若下載到的是 HTML（SF 錯誤頁）而不是二進位檔，則刪除
    $head = [System.IO.File]::ReadAllBytes($target)[0..15]
    $ascii = -join ($head | ForEach-Object { if ($_ -ge 32 -and $_ -lt 127) { [char]$_ } else { "." } })
    if ($ascii -match "^<!DOCTYPE|^<html") {
      Remove-Item $target
      Write-Host "   [失敗] 下載到 HTML（可能是 SF 404）" -ForegroundColor Red
      $failed++
    } else {
      Write-Host "   [成功] $sz MB" -ForegroundColor Green
      $success++
    }
  } catch {
    Write-Host "   [錯誤] $($_.Exception.Message)" -ForegroundColor Red
    $failed++
  }
}

Write-Host ""
Write-Host "==== 完成：成功 $success / 略過 $skipped / 失敗 $failed ====" -ForegroundColor Cyan
Write-Host "下載目錄：$OutDir" -ForegroundColor Cyan
