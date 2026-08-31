# 版本管理 Version Control

## 一、Git 使用規範

本知識庫與 `../uqm-work/` 共用同一個 git repo（工作區根目錄：`Q:\Dos_G\StarControl2\`）。

### Commit 訊息格式

**知識庫更新**（改動 `StarControl2_TW_Localization/` 底下）：

```
docs(<area>): <一句話說明>

<area> 可為：
- races          種族 dossier 更新
- glossary       術語表增修
- rules          翻譯規則調整
- prompt         AI 提詞改動
- lore           世界觀補充
- qa             QA 清單／規則
- refactor       架構調整（大改動慎用）
```

範例：
- `docs(races): add Utwig Ultron restoration two-phase persona split`
- `docs(glossary): lock Sun Device → 太陽裝置`
- `docs(rules): tighten star-map cross-ref rule to include planet indices`

**翻譯輸出**（改動 `../uqm-work/translations/*.zh-TW.json`）：

```
translate(<race>) v0.X: <count> tokens — <一句話特色>
```

範例：
- `translate(spathi) v0.1: 156 tokens — 極度膽小結巴文明`
- `translate(druuge) v0.1: 105 tokens — 血紅集團極端資本主義`

**混合改動**：優先歸為 `translate` 若翻譯是主體、`docs` 若知識庫是主體。

## 二、分支策略

現階段直接在 `master` 上開發（單人專案，避免過度工程）。

**若之後有多人協作**，改用：
- `master` — 穩定版
- `translate/<race>` — 該族翻譯進行中
- `docs/<topic>` — 大規模文件重構

## 三、版本編號

### 翻譯輸出版本

每族翻譯有自己的 `vX.Y`：

- **v0.1**：AI 一輪翻完 + 基本自檢
- **v0.2**：使用者初次校對後
- **v0.5**：多族交叉一致性檢查後
- **v1.0**：全遊戲通關驗證後

### 知識庫版本

以 `README.md` 的「變更歷史」段落為準，語義化版本：

- **主版本**（v1 → v2）：架構重構、命名體系大改
- **次版本**（v1.0 → v1.1）：新增大量 dossier／規則
- **修訂版**（v1.1 → v1.1.1）：小修改、typo

## 四、回滾點

任何大改動前，先確保：

1. `git status` 乾淨（所有變更已 commit）
2. `git log --oneline -5` 記下 HEAD hash
3. 大重構之前另做 zip 備份（如本次重構的 `_pre_restructure_backup_YYYYMMDD_HHMMSS.zip`）

回滾命令：

```powershell
# 軟回滾：保留檔案改動，只回退 commit 指標
git reset --soft <hash>

# 硬回滾：連檔案都回到那一刻（會遺失未 commit 的改動）
git reset --hard <hash>

# 從 zip 恢復單一檔案
Expand-Archive -Path _pre_restructure_backup_XXX.zip -DestinationPath _restore -Force
```

## 五、禁止事項

- ❌ `git push --force` 到共用分支
- ❌ `git rebase` 已推送的 commit
- ❌ 未經確認就 `git reset --hard`（會丟失 uncommit 的翻譯進度）
- ❌ 用 `git rm -rf` 一次刪整個資料夾（先手動 review）
