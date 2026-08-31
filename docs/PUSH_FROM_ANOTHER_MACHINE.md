# 從另一台電腦推送到 GitHub · Push From Another Machine

> **情境**：這次 clone 的開發電腦不方便登入你的 GitHub 帳號（例：公司電腦、共用電腦、無雙因素認證裝置等）。
> 你要把整個 `GitHubRepo/` 資料夾**帶到另一台有 GitHub 登入的電腦**，然後從那裡 push。

---

## 準備清單（開發電腦，即目前這台）

**已完成**：
- ✅ `GitHubRepo/` 資料夾已建立、內容齊全
- ✅ `git init` 已在 `GitHubRepo/` 內執行（見 Step 13 · 由本次 setup 完成）
- ✅ 初次 commit `chore: initial import` 已產生
- ✅ SHA256 sidecar 已產出（`scripts/verify_and_scan.ps1` 執行後）
- ⏳ **APK / PC zip 尚未上傳** — 要在另一台電腦連上 GitHub 後手動走 Release page

**還沒設但可以留空**：
- ❌ `git config user.name` / `user.email`（保持空白，另一台再設）
- ❌ `git remote add origin` 尚未執行

## 傳輸 · Transfer

### 方式 A：外接硬碟 / USB
```powershell
# 開發電腦
Compress-Archive -Path Q:\Dos_G\StarControl2\GitHubRepo -DestinationPath E:\GitHubRepo.zip
# 拷到 USB → 拿去另一台電腦
```

### 方式 B：內網 SMB / 私人雲
```powershell
Copy-Item Q:\Dos_G\StarControl2\GitHubRepo \\OtherPC\SharedFolder\ -Recurse
```

### 方式 C：私人 Git bundle
```powershell
cd Q:\Dos_G\StarControl2\GitHubRepo
git bundle create GitHubRepo.bundle --all
# 拷 GitHubRepo.bundle 到另一台電腦
```

**方式 A 最簡單**（走 zip · 保證所有文件都在）。方式 B 需內網。方式 C 適合已熟 git 的人（另一台可以 `git clone GitHubRepo.bundle` 建 fresh repo）。

## 另一台電腦（有 GitHub 登入的機器）

### 前置

- 已安裝 Git for Windows / macOS Git / Linux git
- 已用 `gh auth login` 登入 GitHub CLI（或用瀏覽器登入 github.com）
- 決定好 GitHub URL：`https://github.com/<你的帳號>/uqm-megamod-zhTW`

### 步驟 1 · 解壓與定位

```powershell
# 假設你把 zip 放在 D:\Projects\
Expand-Archive D:\Projects\GitHubRepo.zip -DestinationPath D:\Projects\
cd D:\Projects\GitHubRepo
```

### 步驟 2 · 設定 git 使用者身分

```powershell
git config user.name "你的名字"
git config user.email "your.email@example.com"
```

（若你想全機共用同一 identity，用 `--global`；本 repo 建議走 repo-local，避免污染其他 repo。）

### 步驟 3 · 在 GitHub 建立空 repo

**方法 A · 用 GitHub CLI**：
```powershell
gh repo create uqm-megamod-zhTW --public --description "繁體中文化 · UQM MegaMod 激戰M星雲II" --no-clone
```

**方法 B · 用瀏覽器**：
1. 開 <https://github.com/new>
2. Repository name: `uqm-megamod-zhTW`
3. Public
4. **不要** initialize with README / .gitignore / license（我們本地已有）
5. Create

### 步驟 4 · 加 remote 並 push

```powershell
git remote add origin https://github.com/<你的帳號>/uqm-megamod-zhTW.git
git branch -M main
git push -u origin main
```

推送時 GitHub 會要驗證：
- **HTTPS**：跳 GitHub OAuth 對話框 · 用瀏覽器登入
- **SSH**：改用 `git@github.com:<你>/uqm-megamod-zhTW.git`
- **PAT (Personal Access Token)**：GitHub Settings → Developer settings → PAT · 建 fine-grained token · push 時當密碼

### 步驟 5 · 上傳 APK / PC zip 到 Release Page

**方法 A · 用 GitHub CLI**：
```powershell
# 準備檔案（從開發電腦帶過來，或直接放在另一台）
# 假設檔案在 D:\Releases\

# 建 draft release
gh release create v1.0.12 --title "繁中版 v1.0.12 (激戰M星雲II Android v3.8)" --draft `
  --notes-file CHANGELOG.md

# 上傳附件
gh release upload v1.0.12 `
  D:\Releases\SC2-zhTW-v1.0.12.zip `
  D:\Releases\SC2-zhTW-v1.0.12.zip.sha256 `
  D:\Releases\激戰M星雲II-v3.8-release.apk `
  D:\Releases\激戰M星雲II-v3.8-release.apk.sha256 `
  D:\Releases\激戰M星雲II-v3.8-debug.apk `
  D:\Releases\激戰M星雲II-v3.8-debug.apk.sha256

# 檢視 draft
gh release view v1.0.12 --web

# 掃過 VirusTotal 且貼好 URL 後，發佈
gh release edit v1.0.12 --draft=false
```

**方法 B · 用瀏覽器**：
1. 進 <https://github.com/<你>/uqm-megamod-zhTW/releases/new>
2. Choose tag: `v1.0.12`（新建）
3. Release title: 「繁中版 v1.0.12 (激戰M星雲II Android v3.8)」
4. Description: 貼 CHANGELOG 內容
5. **勾 Set as pre-release** 直到 VirusTotal 掃完
6. Drag & drop APK/zip/sha256 檔上傳
7. Save draft
8. 掃完貼好 URL → Publish

### 步驟 6 · 更新 README 內下載連結

推送後回到 README 把 `[repo owner]` 替換為實際帳號：

```powershell
# 假設 GitHub 帳號叫 alice
$readme = 'D:\Projects\GitHubRepo\README.md'
(Get-Content $readme -Raw) -replace '\[repo owner\]', 'alice' | Set-Content $readme -Encoding utf8

git add README.md
git commit -m "docs: replace [repo owner] placeholder with actual GitHub handle"
git push
```

（同樣要處理 `docs/PC_Install_Guide.md`, `docs/Android_Install_Guide.md`, `AUTHORS.md`, `.github/ISSUE_TEMPLATE/*.md` — 用 grep 找所有 `[repo owner]` 位置。）

## 常見問題

### Q: push 到一半 GitHub 拒絕（file too large）
**A**: 檢查是否有 apk/zip 誤 commit 進 git 歷史。跑：
```powershell
git ls-files | ForEach-Object { [pscustomobject]@{ File = $_; Size = (Get-Item $_).Length } } | Sort-Object Size -Descending | Select-Object -First 20
```
超過 50 MB 的檔案要移出（GitHub 上限單檔 100 MB）。用 `git rm --cached <file>`。

### Q: push 顯示「fatal: refusing to merge unrelated histories」
**A**: 你在 GitHub 建 repo 時勾了 README/gitignore。刪掉 GitHub 上那個 repo 重建（不勾），或用 `git push -f origin main`（force）。

### Q: 我想改 branch 名稱從 master 改 main
**A**: 已在 Step 4 用 `git branch -M main`。若 push 已完成想改，去 GitHub Settings → Branches → Default branch。

### Q: CJK 檔名亂碼
**A**: 這台電腦的 git 沒設定 UTF-8。跑：
```powershell
git config core.quotepath false
git config core.precomposeunicode true
```
`.gitattributes` 已預設這些。

### Q: 我 push 一半電腦掛了，怎麼繼續？
**A**: 直接再 `git push -u origin main`。git 是 idempotent，會從中斷點繼續。

### Q: 我 push 上去發現忘記把 keystore 排除了怎麼辦？
**A**: **不要慌但要快**：
```powershell
# 1. 立即 rotate keystore（產新的，舊的作廢）
# 2. 從 git 歷史移除敏感檔
git filter-repo --path Android/keystore/uqm-zh-tw.jks --invert-paths
# 3. force push
git push --force origin main
# 4. 舊 keystore 檔 rotate（改 alias / 密碼 · 重新產）
```
**教訓**：本 repo `.gitignore` 已排除 `*.jks` `keystore/` `keystore.properties`，這個提前防護。

## 之後的 push 流程（第二次以後）

```powershell
cd D:\Projects\GitHubRepo
# 修改檔案
git status
git add <files>
git commit -m "描述"
git push
```

若你在**開發電腦**改了東西：
1. `git bundle create update.bundle main`（開發機）
2. 拷 bundle 到有 GitHub 登入的機器
3. `git fetch update.bundle main:incoming`
4. `git merge incoming`（或 rebase）
5. `git push`

或更簡單：**直接把兩台電腦的 git remote 都設成同一 GitHub URL**，開發電腦負責寫，登入電腦負責 push。

## 資源

- [GitHub CLI docs](https://cli.github.com/)
- [Git 官方文件](https://git-scm.com/docs)
- [GitHub Releases API](https://docs.github.com/rest/releases)
