# Push UQM-MegaMod 到你的 GitHub Fork · 詳細步驟

> **這份文件是為了修好 `setup_upstream.ps1` 而生**。你必須把本地 `UQM-MegaMod/`
> 也 push 到 GitHub，變成你的 fork。這樣別人 clone `sc2-uqm-zhtw` 之後跑
> `setup_upstream.ps1` 才能拿到跟你本地一模一樣的 patched MegaMod。

---

## 為什麼要走 fork（背景）

- 你本地 `UQM-MegaMod/` 已把 34 個 zh-TW patch **committed 為分支歷史 commit**
  （例：`6311c53 zh-TW patches 001-006 applied state`、`f907715 zh-TW patch 009`）
- **但這些 commit 從未 push 回 JHGuitarFreak 官方** — 官方 repo 沒有這些 SHA
- 導致：別人 `git clone https://github.com/JHGuitarFreak/UQM-MegaMod` 拿不到 SHA `dc2a4e6`
- **解法**：把你本地整個 UQM-MegaMod 也 push 到你 GitHub，作為你的 fork
- 這樣 `setup_upstream.ps1` clone 你的 fork → 直接得到含所有 patch 的 state

## 需要在**有 GitHub 登入的電腦**執行

因為要 push，必須有 GitHub 帳號憑證（PAT / SSH / OAuth）。**目前的開發電腦不方便登入 GitHub**，所以流程是：

1. 【開發電腦】把本地 `UQM-MegaMod/` 打包成 git bundle
2. 【傳輸】把 bundle 帶到另一台有 GitHub 登入的電腦
3. 【登入電腦】從 bundle 恢復 → push 到你的 GitHub
4. 【傳回】更新 `sc2-uqm-zhtw/patches/UPSTREAM_COMMIT.txt` 內的 fork URL
5. 【commit + push】把 URL 更新也 push 到主 repo

---

## 步驟 1【開發電腦】打包 UQM-MegaMod 為 git bundle

```powershell
cd Q:\Dos_G\StarControl2\UQM-MegaMod

# 確認本地無 uncommitted changes
git status

# 若有 uncommitted，先 commit 或 stash
# git add -A; git commit -m "chore: pre-push snapshot"

# 打包所有 branch + tag 進單一 bundle 檔
git bundle create ..\UQM-MegaMod-fork.bundle --all

# 檢查 bundle 大小（應該 ~40-80 MB）
Get-Item ..\UQM-MegaMod-fork.bundle | Select-Object Length,LastWriteTime
```

**產出**：`Q:\Dos_G\StarControl2\UQM-MegaMod-fork.bundle`

## 步驟 2【開發電腦】把 bundle + GitHubRepo 一起傳到另一台

用你偏好的方式（USB / 內網 / 雲端）把以下**兩個東西**傳到有 GitHub 登入的電腦：

- `Q:\Dos_G\StarControl2\GitHubRepo\`（本主 repo，含 34 個 patches 說明檔）
- `Q:\Dos_G\StarControl2\UQM-MegaMod-fork.bundle`（本地 MegaMod state 打包）

## 步驟 3【登入電腦】在 GitHub 建立空 fork repo

**方法 A · 用 GitHub CLI**（推薦）：
```powershell
# 前置：gh auth login
gh repo create uqm-megamod-zhTW `
  --public `
  --description "SC2 繁中化 · MegaMod fork with CJK/Android patches (base of 激戰M星雲II)" `
  --no-clone
```

**方法 B · 用瀏覽器**：
1. 開 <https://github.com/new>
2. **Repository name**: `uqm-megamod-zhTW`
3. **Public**（若要別人能免登入 clone）
4. **不要** initialize with README/gitignore/license（保持完全空白）
5. Create

**注意 repo 命名**：可以叫 `uqm-megamod-zhTW` 或 `UQM-MegaMod-fork` 或 `激戰M星雲II-engine` 等。**你選什麼都行**，但要記下實際 URL。

## 步驟 4【登入電腦】從 bundle 恢復本地 clone 並 push

```powershell
# 假設 bundle 放在 D:\Downloads\
cd D:\Projects

# 從 bundle clone 出本地 repo
git clone D:\Downloads\UQM-MegaMod-fork.bundle UQM-MegaMod

cd UQM-MegaMod

# 檢查 log · 應該看到你本地的所有 commit（含 patches / Android feat 等）
git log --oneline -20

# 應該看到最新是 dc2a4e6 chore(android): v3.8 refresh
git log -1 --pretty=format:'%H %s'

# 設 remote 到你剛建的空 fork
git remote remove origin  # bundle 建的預設 remote 是 bundle 路徑，先移除
git remote add origin https://github.com/YOUR_USER/uqm-megamod-zhTW.git

# 決定分支名稱（本地可能叫 master · 建議改成 main）
git branch -M main

# push 全部（含 tags）到你的 fork
git push -u origin main --tags
```

**推送時 GitHub 會要驗證**：
- **HTTPS**：跳 GitHub OAuth 對話框，用瀏覽器登入
- **SSH**：改用 `git@github.com:YOUR_USER/uqm-megamod-zhTW.git`
- **PAT**：GitHub Settings → Developer settings → PAT · fine-grained token · push 時當密碼

## 步驟 5【登入電腦】更新 `UPSTREAM_COMMIT.txt` 內的 fork URL

前往 `sc2-uqm-zhtw` 主 repo 資料夾（也在這台電腦）：

```powershell
cd D:\Projects\sc2-uqm-zhtw

# 用 PowerShell 一鍵替換佔位符
$file = 'patches\UPSTREAM_COMMIT.txt'
$myUrl = 'https://github.com/YOUR_USER/uqm-megamod-zhTW.git'
(Get-Content $file -Raw) -replace `
  'https://github\.com/CHANGE_ME_TO_YOUR_GITHUB_USER/uqm-megamod-zhTW\.git', `
  $myUrl | Set-Content $file -NoNewline -Encoding utf8

# 驗證
Select-String -Path $file -Pattern 'https://github\.com/.*UQM-MegaMod' -SimpleMatch:$false
```

**同步替換 README 佔位符**（見 `docs/PUSH_FROM_ANOTHER_MACHINE.md`）：
```powershell
Get-ChildItem -Recurse -Include *.md -File | ForEach-Object {
  (Get-Content $_ -Raw) -replace '\[repo owner\]', 'YOUR_USER' | `
    Set-Content $_ -NoNewline -Encoding utf8
}
```

## 步驟 6【登入電腦】commit + push 主 repo 的 URL 更新

```powershell
git add patches\UPSTREAM_COMMIT.txt *.md docs\*.md .github\ISSUE_TEMPLATE\*.md
git commit -m "docs: point setup_upstream to my UQM-MegaMod fork · replace HaCoMaTaTa with YOUR_USER"
git push
```

## 步驟 7【任一電腦】驗證 setup_upstream.ps1 可用

```powershell
cd D:\Projects\sc2-uqm-zhtw

# DryRun 確認 URL 已對
.\scripts\setup_upstream.ps1
# 應該看到 "Fork URL: https://github.com/YOUR_USER/uqm-megamod-zhTW.git"

# 實跑（會 clone 到 ../UQM-MegaMod/）
Remove-Item ..\UQM-MegaMod -Recurse -Force -ErrorAction SilentlyContinue
.\scripts\setup_upstream.ps1 -Execute

# 驗證 checkout 正確 SHA
cd ..\UQM-MegaMod
git log -1 --pretty=format:'%H %s'
# 應該顯示 dc2a4e68... chore(android): v3.8 refresh
```

如果這步通過，你的 fork 就完全 ready 了。任何人 clone 主 repo 都能一鍵重建。

---

## 疑難排解

### 「Bundle 太大 push 不上 GitHub」
- GitHub 對單 push 有 2 GB 硬限、單檔 100 MB 建議上限
- 你本地 UQM-MegaMod 應該 <100 MB · 若超過，先跑 `git gc --aggressive` 壓縮

### 「HTTPS push 一直跳 auth failed」
- GitHub 已經廢除密碼登入，必須用 PAT
- Settings → Developer settings → Personal access tokens → Fine-grained token
- Repository access: 選你的 fork
- Permissions: `Contents: Read and write`
- 產生後複製 token，push 時當密碼貼

### 「setup_upstream.ps1 clone 失敗說 fork URL 錯誤」
1. 檢查 `patches/UPSTREAM_COMMIT.txt` 內 URL 是否指到實際存在的 repo
2. 用瀏覽器開 URL 對應網頁，若 404 表示 fork 沒建成功
3. 用 `gh repo view YOUR_USER/uqm-megamod-zhTW --web` 開啟

### 「checkout 失敗說 SHA 不存在」
1. 檢查你的 fork 是否 push 了最新 branch：`gh repo view YOUR_USER/uqm-megamod-zhTW --json defaultBranchRef`
2. 檢查 SHA 在 fork 內：`git ls-remote https://github.com/YOUR_USER/uqm-megamod-zhTW.git | Select-String 'dc2a4e6'`
3. 若沒 SHA，你可能忘了 `git push --tags` 或 branch 沒 push 完整

### 「網路不能連 GitHub」
- 可用 `-TargetPath` 指向本地已存在的 clone：
  ```powershell
  .\scripts\setup_upstream.ps1 -Execute -TargetPath 'C:\my\existing\UQM-MegaMod'
  ```

---

## 之後如何維護 fork

**跟上 JHGuitarFreak 官方更新**：

```powershell
cd D:\Projects\UQM-MegaMod

# 一次性加 official remote
git remote add official https://github.com/JHGuitarFreak/UQM-MegaMod.git

# 抓 official 最新
git fetch official

# 看有多少新 commit
git log --oneline HEAD..official/master

# 合併（或 rebase）
git merge official/master   # 若你偏好乾淨線性 log，用 rebase 但注意 conflict

# 解衝突（多發生在 src/uqm/planets/report.c · src/libs/uio/ · build/android/）
# ...

# 測 build（PC + Android）
# ...

# push 到你的 fork
git push origin main

# 更新主 repo 內的 SHA
cd D:\Projects\sc2-uqm-zhtw
# 手動編輯 patches/UPSTREAM_COMMIT.txt · 更新新 SHA + metadata
git add patches/UPSTREAM_COMMIT.txt
git commit -m "chore: bump upstream to $(cd ..\UQM-MegaMod; git rev-parse --short HEAD)"
git push
```

---

## 需要記住的 5 件事

1. **你的 fork = source of truth**，不是 JHGuitarFreak 官方
2. `setup_upstream.ps1` **不 apply patches** · patches 已在 fork 內 commit
3. `UPSTREAM_COMMIT.txt` 的 fork URL **必須**改成你的實際 GitHub URL
4. Push fork 之後**測一次 setup_upstream.ps1 -Execute**，確認能運作
5. 之後要跟上游更新時，先在 fork 內 merge official 再 push
