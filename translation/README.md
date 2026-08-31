# Star Control II 繁體中文化 AI 知識庫

> **專案代號**：`SC2_TW_LOC`
> **目標遊戲**：Star Control II（The Ur-Quan Masters / UQM MegaMod）
> **目標語言**：**繁體中文（台灣用語）**
> **版本**：v1.0（2026-08-07 重構）

---

## 一、這個資料夾是做什麼的

這是一套**給 AI 翻譯用的長期維護知識庫**，不是遊戲檔案、不是翻譯輸出、不是編譯資源。

- **編譯與遊戲檔案**在 `../uqm-work/`（不歸本資料庫管）
- **翻譯 JSON 輸出**在 `../uqm-work/translations/`（不歸本資料庫管）
- **這個資料夾**只放：世界觀 lore、種族人格、術語鎖定表、AI 翻譯規則、AI 提詞範本、QA 清單、參考素材

## 二、資料庫組織

| 目錄 | 內容 | 何時讀 |
|---|---|---|
| `00_Project_Control/` | 專案目標、工作流程、版本管理、AI 工作流程 | 每次開新翻譯 session 開始 |
| `01_World_Lore/` | 宇宙觀、時間線、銀河史、科技水平、政治、人類陣營 | 翻譯前要理解時空背景時 |
| `02_Races/` | 每個種族一份 dossier（27 族） | 翻譯該族對話時 |
| `03_Characters/` | 重要 NPC 個人 dossier（艦長、Fwiffo、Talana 等） | 翻譯有該 NPC 出現的對話時 |
| `04_Ships/` | 艦艇級別與戰術描述 | 翻譯戰鬥或艦艇介紹時 |
| `05_Technology/` | 武器、裝置、資源、神器（Ultron 等） | 翻譯任務物品／科技相關時 |
| `06_Locations/` | 星系、行星、星圖 | 翻譯地名時 |
| `07_Glossary/` | 主術語鎖定表 + 分類子表 + CSV | **每次翻譯前必查** |
| `08_Translation_Rules/` | 風格指引、命名規則、對話規則、幽默規則、外星語規則 | 翻譯規則參考 |
| `09_AI_Prompt/` | 各類翻譯任務的 AI 提詞範本 | 開翻譯 session 時複製貼給 AI |
| `10_Translation_Memory/` | 已翻譯 TM、禁止的譯法 | AI 遇到相似句子時參考 |
| `11_QA/` | 一致性檢查、錯誤清單、審核流程 | 翻譯完自檢時 |
| `Reference_Material/` | 中文手冊 OCR、原著指南、分析報告等**參考素材**（不是 AI 直接讀的） | 遇到疑點需要深挖時 |

## 三、給 AI 翻譯的最短使用方式

**開一個新的翻譯 session，只要三步**：

1. 貼上 `09_AI_Prompt/Translate_Dialogue.md`（主提詞，設定 AI 為 SC2 翻譯總監）
2. 貼上 `07_Glossary/Master_Glossary.md`（術語鎖定表，含 27 族名 + 80+ 專有名詞）
3. 開始貼原文段落，AI 就會依規則翻譯

若翻譯的是特定種族，可**額外**貼該族的 `02_Races/<Race>.md` 給 AI 補人格細節。

## 四、關鍵規範（讀之前先知道）

- **繁體中文（台灣用語）**：不使用中國大陸用語（如「宇宙船」「能量包」「船長」→ 一律用「星艦」「能源」「艦長」）
- **1990 年代科幻感**：不加台灣當代網路流行語、不加時事哏
- **種族名採 System B**：≤3 字＋族，性格暗示優先（如 Spathi → 史怕族的「怕」、Utwig → 憂特族的「憂」）
- **星圖交叉參照規則**：對話中提到星系／星座／恆星／行星／星群時，中譯後**必須**在全形括號附上英文原文（例：`參宿四（Betelgeuse）`），因為星圖 UI 是英文
- **`#(TOKEN_NAME)` 原樣保留**：不翻譯、不刪除、不更動大小寫

詳細規則見 `08_Translation_Rules/`。

## 五、回滾機制

若本次重構出問題，可用兩個機制恢復：

1. **Git**：回到 pre-restructure commit
   ```powershell
   cd Q:\Dos_G\StarControl2
   git log --oneline --all | Select-String "pre-restructure"
   git reset --hard <commit-hash>
   ```
2. **Zip 快照**：`../\_pre_restructure_backup_20260807_154625.zip` 內含 8 個原始 md 檔

## 六、變更歷史

| 版本 | 日期 | 說明 |
|---|---|---|
| v1.0 | 2026-08-07 | 從 `_analysis/`、`Star Control II GUS - Manual/` 散裝檔案重構為結構化 12 目錄知識庫，整合《敘事語言學指南》人格細節到 System B 命名體系 |
