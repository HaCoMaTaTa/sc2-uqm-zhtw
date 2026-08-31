# Release 上傳 · 保姆級步驟

> **對象**：你已經在另一台電腦、有 GitHub 登入了，準備把 apk + zip 上傳到 GitHub Releases。
> **前提**：本 repo（`uqm-megamod-zhTW`）已 push 到 GitHub（見 [`PUSH_FROM_ANOTHER_MACHINE.md`](PUSH_FROM_ANOTHER_MACHINE.md)）。

---

## 你手上應該有的 3 個 release 檔（加 3 個 sha256 sidecar）

從開發電腦帶過來的：

| 檔案 | 大小 | 用途 |
|---|---:|---|
| `激戰M星雲II-v3.8-release.apk` | 387 MB | Android **一般玩家版**（release keystore 簽章）|
| `激戰M星雲II-v3.8-debug.apk` | 393 MB | Android **除錯版**（給幫忙抓 bug 的玩家）|
| `SC2-zhTW-v1.0.12.zip` | 350 MB | **PC Windows 中文化版**（含 patched exe）|
| `激戰M星雲II-v3.8-release.apk.sha256` | 100 byte | 對應 hash |
| `激戰M星雲II-v3.8-debug.apk.sha256` | 100 byte | 對應 hash |
| `SC2-zhTW-v1.0.12.zip.sha256` | 100 byte | 對應 hash |

**傳到有 GitHub 登入的電腦**（例：放 `D:\Releases\` 資料夾）。

---

# 方法一 · 用 GitHub 網頁上傳（最直觀 · 推薦新手）

## 步驟 1 · 開 GitHub Release 建立頁

在瀏覽器打開：
```
https://github.com/YOUR_USER/uqm-megamod-zhTW/releases/new
```
（把 `YOUR_USER` 換成你的實際 GitHub 帳號）

## 步驟 2 · 填 Tag 與 Title

- **Choose a tag** 欄位：打 `v1.0.12`（或你 release 版本號）→ 下拉會問 `+ Create new tag: v1.0.12 on publish` → 點選
- **Target** 欄位：選 `main`（預設就是）
- **Release title** 欄位：貼 `繁中版 v1.0.12 · 激戰M星雲II Android v3.8`

## 步驟 3 · 填 Description

貼下面這段（你可依需要調整）：

```markdown
## Star Control II · The Ur-Quan Masters · 繁體中文化 v1.0.12

- **PC Windows**：SC2-zhTW-v1.0.12.zip（350 MB）
- **Android release**：激戰M星雲II-v3.8-release.apk（387 MB · 一般玩家）
- **Android debug**：激戰M星雲II-v3.8-debug.apk（393 MB · 除錯用）

### 涵蓋範圍
- 3547 tokens 全對白繁中翻譯 · 26 族 Level 3 audit 完成
- 34 個引擎 patch（Zip64 / CJK / lander / Android touch UI ...）
- HD / SD 兩模式 · 全套繁中字型

### 安裝
- **PC**：[docs/PC_Install_Guide.md](../blob/main/docs/PC_Install_Guide.md)
- **Android**：[docs/Android_Install_Guide.md](../blob/main/docs/Android_Install_Guide.md)

### 安全性掃描
所有 apk / zip 已通過 VirusTotal 掃描，報告見 [docs/Security_Scan_Report.md](../blob/main/docs/Security_Scan_Report.md)。

### SHA256
每個檔案都附 `.sha256` sidecar，下載後可自行驗證：
```powershell
Get-FileHash SC2-zhTW-v1.0.12.zip -Algorithm SHA256
# 對照 SC2-zhTW-v1.0.12.zip.sha256 內的 hash
```

### 授權
- 引擎源碼：GPL-2.0
- 內容資產：CC BY-NC-SA 2.5
詳見 [LICENSE](../blob/main/LICENSE) / [LICENSE.CONTENT](../blob/main/LICENSE.CONTENT)。

### 致謝
Toys for Bob (Fred Ford, Paul Reiche III) · UQM Team · JHGuitarFreak (MegaMod)
```

## 步驟 4 · 拖曳 6 個檔案上傳

看到 **`Attach binaries by dropping them here or selecting them.`** 這行灰色提示區：

- 打開檔案總管，找到你放 release 檔的資料夾（例 `D:\Releases\`）
- **一次選 6 個檔案**（3 個 release + 3 個 .sha256），拖到那個灰色區域
- 每個檔案會出現進度條 · **等進度條全部到 100%** 才進下一步

**大檔上傳時間估計**（依你網速）：
- 100 Mbps 上行 → 每檔 ~30 秒 · 全部約 3-5 分鐘
- 10 Mbps 上行 → 每檔 ~5 分鐘 · 全部約 30 分鐘

**中途不要關瀏覽器分頁**！關掉會中斷。

## 步驟 5 · 決定是否標 pre-release

- 若你想先給少數朋友測 → 勾 **`Set as a pre-release`**
- 若已充分測、想公開 → 不勾（預設）

## 步驟 6 · Publish

點 **`Publish release`** 綠色按鈕。頁面會跳到 release page，你會看到 6 個附件、tag、description。

## 步驟 7 · 分享連結

Release page URL 例如：
```
https://github.com/YOUR_USER/uqm-megamod-zhTW/releases/tag/v1.0.12
```

複製這個 URL，任何人開瀏覽器打開都能看到 6 個附件、可直接下載。

---

# 方法二 · 用 GitHub CLI（快 · 適合已裝 gh）

## 步驟 A · 一次性設定（首次用 gh）

```powershell
# 安裝 gh CLI (若還沒裝)
winget install --id GitHub.cli
# 或到 https://cli.github.com 下載

# 首次登入
gh auth login
# 依提示：
#   ? What account do you want to log into?  → GitHub.com
#   ? Preferred protocol for Git operations? → HTTPS
#   ? Authenticate Git with your GitHub credentials? → Yes
#   ? How would you like to authenticate?    → Login with a web browser
# 會給你一個 8 位數 one-time code，複製 → 瀏覽器開 https://github.com/login/device 貼

# 驗證登入成功
gh auth status
```

## 步驟 B · 建 release 並上傳（一氣呵成）

```powershell
# 進入你 clone 的 uqm-megamod-zhTW 資料夾
cd D:\Projects\uqm-megamod-zhTW

# 建 release（先 draft，還沒公開）
gh release create v1.0.12 `
    --title "繁中版 v1.0.12 · 激戰M星雲II Android v3.8" `
    --notes-file CHANGELOG.md `
    --draft

# 上傳 6 個檔案（一行搞定）
gh release upload v1.0.12 `
    "D:\Releases\SC2-zhTW-v1.0.12.zip" `
    "D:\Releases\SC2-zhTW-v1.0.12.zip.sha256" `
    "D:\Releases\激戰M星雲II-v3.8-release-20260831_1114.apk" `
    "D:\Releases\激戰M星雲II-v3.8-release-20260831_1114.apk.sha256" `
    "D:\Releases\激戰M星雲II-v3.8-debug-20260831_1114.apk" `
    "D:\Releases\激戰M星雲II-v3.8-debug-20260831_1114.apk.sha256"

# 網頁預覽（會開瀏覽器）
gh release view v1.0.12 --web

# 檢查沒問題後，發佈（從 draft 變 published）
gh release edit v1.0.12 --draft=false
```

---

# 上傳前建議先做的事

## A. 補 VirusTotal 掃描 URL

上傳前建議先掃 VirusTotal（免費，任何人可看報告）：

1. 開 <https://www.virustotal.com/gui/home/upload>
2. **每個檔案**上傳掃一次（apk 兩個 + zip 一個 = 3 次）
3. 掃完會得到 URL，例：`https://www.virustotal.com/gui/file/d64dc857.../detection`
4. 複製 URL 貼到 `docs/Security_Scan_Report.md` 對應列
5. commit + push：
   ```powershell
   git add docs/Security_Scan_Report.md
   git commit -m "docs: add VirusTotal scan URLs for v1.0.12/v3.8"
   git push
   ```

## B. 檢查 SHA256 sidecar 內容

3 個 `.sha256` 檔內容應該像這樣：
```
d64dc8577b7ce66432453bd836ddc8b1d405aa05347ce96e6eef68baf45a0962 *激戰M星雲II-v3.8-release-20260831_1114.apk
```

若你不確定，重新產生一次：
```powershell
cd D:\Releases
Get-FileHash *.apk, *.zip -Algorithm SHA256 | ForEach-Object {
    $hashLine = "$($_.Hash.ToLower()) *$([System.IO.Path]::GetFileName($_.Path))"
    $sidecarPath = "$($_.Path).sha256"
    Set-Content -Path $sidecarPath -Value $hashLine -Encoding ascii
    Write-Host "Wrote $sidecarPath"
}
```

## C. 檔案完整性快掃

上傳前確認 3 個 release 檔還沒損壞：

```powershell
cd D:\Releases
Get-ChildItem *.apk, *.zip | ForEach-Object {
    Write-Host "$($_.Name) - $([math]::Round($_.Length/1MB,1)) MB"
}
```

大小應該符合：
- Release APK ≈ 387 MB
- Debug APK ≈ 393 MB
- PC ZIP ≈ 350 MB

---

# 疑難排解

## 「Upload 中斷 / 網頁 timeout」
- **原因**：單檔 >200 MB 建議走 gh CLI，網頁 upload 對慢速網易 timeout
- **解**：改用方法二 · gh CLI；或分兩次 release，先建 release、逐個上傳

## 「gh release create 說 tag 已存在」
- **原因**：你之前 push 過同名 tag
- **解**：
  ```powershell
  # 若要重來，刪 tag
  git tag -d v1.0.12
  git push --delete origin v1.0.12
  gh release delete v1.0.12
  # 再從步驟 B 開始
  ```

## 「Upload 慢到不合理」
- GitHub 對 release 附件單檔 2 GB 上限、無總量限制
- 上行網速決定：100 Mbps ≈ 12.5 MB/s → 400 MB 需 32 秒
- 若持續掉速：關其他上傳 tab、跳到有線網、或改凌晨上傳

## 「別人下載 apk 後 Android 說『解析套件時發生問題』」
- APK 損壞或簽章不完整
- 讓下載者比對 SHA256：
  ```
  # Android Termux 內
  sha256sum 激戰M星雲II-v3.8-release-*.apk
  ```
- 若 hash 不對 → 重下載
- 若 hash 對但仍安裝失敗 → Android 版本太舊（需 7.0+ / API 24+）

## 「我想改 release 內某個檔案」
- 網頁：進 release page → 「Edit release」→ 底部檔案列旁邊 `x` 刪掉、重新上傳
- gh CLI：
  ```powershell
  gh release delete-asset v1.0.12 "檔名.apk"
  gh release upload v1.0.12 "D:\Releases\檔名.apk" --clobber
  ```

## 「我想收回一整個 release」
```powershell
gh release delete v1.0.12
# 或改為 draft 隱藏
gh release edit v1.0.12 --draft=true
```

---

# 上傳後 checklist

- [ ] Release page 打開能看到 6 個附件、tag、description
- [ ] 每個附件檔案大小顯示正確（不是 0 KB 或誤傳）
- [ ] README 內的 Releases 連結能正確跳到最新版
- [ ] 從 Release page 下載一次驗證能拿到完整檔案
- [ ] 分享給至少一個朋友試裝，確認能運作
- [ ] （可選）發布時間**避開睡覺時段**——若有問題你能立刻收 issue 修

---

# 之後更新新版本時的流程

```powershell
# 假設你新 build 好 v1.0.13 + Android v3.9
gh release create v1.0.13 `
    --title "繁中版 v1.0.13 · 激戰M星雲II Android v3.9" `
    --notes "改動：<新功能/修正>"

gh release upload v1.0.13 `
    "D:\Releases\SC2-zhTW-v1.0.13.zip" `
    "D:\Releases\SC2-zhTW-v1.0.13.zip.sha256" `
    "D:\Releases\激戰M星雲II-v3.9-release.apk" `
    "D:\Releases\激戰M星雲II-v3.9-release.apk.sha256"

# 更新 README 內的下載連結（若你有寫最新版本號在裡面）
# 更新 CHANGELOG.md
git add README.md CHANGELOG.md
git commit -m "docs: bump to v1.0.13 / Android v3.9"
git push
```

**建議節奏**：每個 minor bug fix commit 到 main、每 3-5 個 fixes 出一次新 release。
