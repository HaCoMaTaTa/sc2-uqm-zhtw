# =====================================================================
# replace_placeholders.ps1
# 一鍵替換 repo 內所有 GitHub 佔位符為你的實際帳號。
#
# 使用方式：
#   # DryRun 預覽會改哪些檔案（推薦先跑）
#   .\scripts\replace_placeholders.ps1 -GitHubUser alice
#
#   # 實際替換
#   .\scripts\replace_placeholders.ps1 -GitHubUser alice -Execute
#
# 會替換的佔位符（依 md/txt 檔案）：
#   [repo owner]                       → alice
#   CHANGE_ME_TO_YOUR_GITHUB_USER      → alice
#   <你>            （URL context）     → alice
#   <你的帳號>       （URL context）     → alice
#
# 不會動的：
#   AI_Handoff/memories/uqm-debugging.md 內的 CHANGE_ME 討論字串
#   PUSH_UQM_MEGAMOD_FORK.md 內作為「說明範例」的 YOUR_USER
# =====================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$GitHubUser,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot  = Split-Path -Parent $scriptDir

Write-Host ""
Write-Host "=== Replace GitHub Placeholders ===" -ForegroundColor Cyan
Write-Host "Repo root:   $repoRoot"
Write-Host "GitHub user: $GitHubUser"
if (-not $Execute) {
    Write-Host "Mode:        DryRun (加 -Execute 才實跑)" -ForegroundColor Yellow
} else {
    Write-Host "Mode:        Execute" -ForegroundColor Green
}
Write-Host ""

# ---- 檔案清單與對應的替換規則 --------------------------------------
# 用「檔案 → [ (pattern, replacement) 陣列 ]」形式明確指定，避免誤傷
$targets = @{
    'README.md' = @(
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
    )
    'AUTHORS.md' = @(
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
    )
    'docs\PC_Install_Guide.md' = @(
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
    )
    'docs\Android_Install_Guide.md' = @(
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
    )
    'docs\PUSH_FROM_ANOTHER_MACHINE.md' = @(
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
        @{ Pattern = '<你的帳號>';    Replacement = $GitHubUser }
        @{ Pattern = '<你>/';         Replacement = "$GitHubUser/" }
    )
    'docs\SOP_Rebuild_And_Release.md' = @(
        @{ Pattern = '<你>/';         Replacement = "$GitHubUser/" }
    )
    'docs\PUSH_UQM_MEGAMOD_FORK.md' = @(
        # 這檔內留一個 \[repo owner\] 在步驟示範，但實際 URL 我們也替換
        @{ Pattern = '\[repo owner\]'; Replacement = $GitHubUser }
    )
    'patches\UPSTREAM_COMMIT.txt' = @(
        @{ Pattern = 'CHANGE_ME_TO_YOUR_GITHUB_USER'; Replacement = $GitHubUser }
    )
}

# ---- 執行 -----------------------------------------------------------
$totalChanges = 0
$filesChanged = 0

foreach ($rel in ($targets.Keys | Sort-Object)) {
    $path = Join-Path $repoRoot $rel
    if (-not (Test-Path $path)) {
        Write-Host "  [MISS] $rel" -ForegroundColor Red
        continue
    }
    $content = Get-Content $path -Raw -Encoding utf8
    $originalContent = $content
    $fileChanges = 0
    foreach ($rule in $targets[$rel]) {
        $matches = [regex]::Matches($content, $rule.Pattern)
        if ($matches.Count -gt 0) {
            $content = [regex]::Replace($content, $rule.Pattern, $rule.Replacement)
            $fileChanges += $matches.Count
        }
    }
    if ($fileChanges -gt 0) {
        Write-Host ("  {0} : {1} replacements" -f $rel, $fileChanges) -ForegroundColor Green
        $filesChanged++
        $totalChanges += $fileChanges
        if ($Execute) {
            # 保留原檔行尾（若原是 CRLF 就寫 CRLF）
            $content | Set-Content -Path $path -NoNewline -Encoding utf8
        }
    } else {
        Write-Host ("  {0} : no match" -f $rel) -ForegroundColor DarkGray
    }
}

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Files changed: $filesChanged / $($targets.Count)"
Write-Host "Total replacements: $totalChanges"
if (-not $Execute) {
    Write-Host ""
    Write-Host "DryRun 完畢，未寫檔。實跑：" -ForegroundColor Yellow
    Write-Host "  .\scripts\replace_placeholders.ps1 -GitHubUser $GitHubUser -Execute"
} else {
    Write-Host ""
    Write-Host "完成。建議下一步：" -ForegroundColor Green
    Write-Host "  git status"
    Write-Host "  git diff --stat"
    Write-Host "  git commit -am `"docs: replace [repo owner] and CHANGE_ME placeholders with $GitHubUser`""
}
Write-Host ""
