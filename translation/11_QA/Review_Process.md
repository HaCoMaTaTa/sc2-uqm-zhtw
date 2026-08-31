# Review Process 人工審查流程

> **本檔功能**：**人工審查**翻譯的流程、責任分工、決策機制。
> **對照**：[Consistency_Check.md](Consistency_Check.md) 自動化 QA；本檔用於**人工判斷**。

---

## 一、審查流程總覽

```
    翻譯完成
        │
        ▼
[Step 1: 譯者自查]  ── Dialogue_Rule.md §十 16 項自查清單
        │
        ▼
[Step 2: CI 自動化] ── consistency_check.py 掃描
        │
        ├─ 若有高優先問題 → 回到 Step 1 修正
        └─ 若過關 → 繼續
        │
        ▼
[Step 3: 使用者審查] ── 人工檢查風格、幽默、玩家 response、跨族一致
        │
        ├─ 若有問題 → 回報 → 譯者修正
        └─ 若通過 → 合併／打包
        │
        ▼
[Step 4: In-game 測試] ── 打包後在遊戲中實際跑一遍
        │
        ├─ 若有 UI 問題（爆版、字寬） → 譯者調整
        └─ 若通過 → git commit + 發布
```

---

## 二、Step 1：譯者自查

### 2.1 使用的檢查清單

**權威版**：[Dialogue_Rule.md](../08_Translation_Rules/Dialogue_Rule.md) §十 十六項自查。

**執行時機**：**每個 JSON 檔翻完**、進 CI 之前。

### 2.2 自查工具

**手動 grep**（PowerShell）：

```powershell
# 找可能的簡體字（示例）
Select-String -Path uqm-work/translations/orz.zh-TW.json -Pattern '[龙华万义从会学]'

# 找 v0.4 舊譯殘留
Select-String -Path uqm-work/translations/orz.zh-TW.json `
  -Pattern '撒達許|蘇菲斯特|阿姆嘎|葉哈特|尼亞里|蘇波族|德魯族|梅爾諾'
```

**AI 自查**：貼 [QA_Check.md](../09_AI_Prompt/QA_Check.md) 提詞給另一個 chat session，讓 AI 檢查。

---

## 三、Step 2：CI 自動化

### 3.1 執行

```powershell
# 檢查單檔
python StarControl2_TW_Localization/11_QA/consistency_check.py `
  --file uqm-work/translations/orz.zh-TW.json

# 全域檢查（打包前）
python StarControl2_TW_Localization/11_QA/consistency_check.py --all
```

### 3.2 檢查項目

**高優先**（會阻止 build）：
- JSON 語法錯誤
- v0.4 舊譯殘留
- 簡體字混入
- Lua template 損壞

**中優先**（建議修正）：
- 日語漢字（Shofixti 例外）
- Orz 星號不成對
- v0.2 更舊譯殘留

**低優先**（可考慮）：
- 空格切分建議
- 星系名英文附註缺失

### 3.3 CI 未通過怎麼辦

**高優先問題** → **必修**，回到 Step 1。

**中優先問題** → **建議修**，但可用**譯註**說明保留原因。

**低優先問題** → **可選修**，通常不修。

---

## 四、Step 3：使用者審查

### 4.1 責任

**使用者**（主要譯者的品質把關者）需檢查：

- **風格一致性**（跨檔案，該族的說話方式一致嗎？）
- **幽默保留**（原文的笑點譯文有嗎？）
- **玩家 response 情境切換**（三情境自稱正確嗎？）
- **文化在地化**（英文生造俚語是否台灣情境對應？）
- **世界觀正確**（是否有誤導性譯法？）
- **命名決策**（新遇到的名詞候選是否合理？）

### 4.2 檢查方式

**方案 A：人工閱讀**（推薦）
- 打開 JSON，從頭讀到尾
- 對照該族 dossier `02_Races/[Race].md`
- 記錄疑問到 [Error_List.md](Error_List.md)

**方案 B：In-game 觀察**
- 打包後在遊戲中跑該族劇情
- 記錄不順口／爆版／出戲的地方

**方案 C：AI 交叉檢查**
- 給另一個 AI 貼 [QA_Check.md](../09_AI_Prompt/QA_Check.md) + 譯文
- 讓 AI 產生問題清單
- 使用者裁決哪些是真問題

### 4.3 決策原則

**修正方針**：
- **明確錯誤**（錯字、簡體字、v0.4 舊譯）→ **直接修正**
- **風格爭議**（風格好不好）→ **保留現譯**，記入 Error_List 供未來討論
- **命名爭議**（新名詞候選）→ **回報使用者**選擇

**新問題發現**：
- 補入 [Error_List.md](Error_List.md) 對應章節
- 若是系統性問題（如某個字類跨檔混用）→ 開新的 QA 議題

---

## 五、Step 4：In-game 測試

### 5.1 打包

```powershell
cd uqm-work
./package_zh-TW.ps1
```

**輸出**：`install/content/addons/zh-TW.uqm`

### 5.2 執行

**UQM 或 MegaMod 執行**：
- 語言選 zh-TW
- 進遊戲跑該族劇情

### 5.3 檢查項目

**UI**：
- 字寬（**每行 ≤ 30 中文字**確認未爆版）
- 對白框（是否被截斷）
- 字型清晰度（尤其 Chmmr 等 10px 字型）

**功能**：
- Lua template 正確替換（艦長名、艦名、聯盟名）
- 星系名可對星圖

**體驗**：
- 對話節奏是否自然
- 幽默是否傳達
- 角色人格是否鮮明

### 5.4 問題發現

**遊戲內截圖 + 位置** → 補入 [Error_List.md](Error_List.md)。

---

## 六、審查責任分工

| 職責 | 角色 | 檢查項 |
|---|---|---|
| **自查** | 譯者（AI 或人）| Dialogue_Rule §十 16 項 |
| **自動化** | CI 系統 | consistency_check.py 全項 |
| **風格審查** | 使用者 | 幽默／人格／台式順口 |
| **In-game 測試** | 使用者 | UI／功能／體驗 |
| **命名決策** | 使用者 | 新名詞候選裁決 |
| **記錄** | 譯者 + 使用者 | Error_List.md |

---

## 七、常見審查場景

### 7.1 場景 A：翻譯全新族

**流程**：
1. 譯者用 [Translate_Dialogue.md](../09_AI_Prompt/Translate_Dialogue.md) 翻譯
2. 譯者自查
3. CI 檢查
4. 使用者審查
5. In-game 測試

**注意**：**新族第一次翻譯**時，**新遇到的名詞可能會很多**。譯者應**每個新名詞回報**，等使用者裁決。

### 7.2 場景 B：審查已 shipped 族（v0.4 rename）

**流程**：
1. 譯者掃描該族 shipped JSON，找 v0.4 舊譯（用 §一 grep 命令）
2. 譯者用 `Fixed_Terms.csv` 對照，做批次替換
3. CI 檢查（重點：v0.4 canonical 是否已全部到位）
4. 使用者抽樣審查（重點對白 20-30 tokens）
5. In-game 測試（跑該族 dialog）

### 7.3 場景 C：CI 發現 shipped 有問題

**流程**：
1. CI 產生 report
2. 使用者評估報告，決定哪些**必修 vs 可 skip**
3. 譯者修正必修項
4. 補入 [Error_List.md](Error_List.md)
5. 重跑 CI 直到過關

---

## 八、決策記錄

**每個重大決策**（如「保留 v0.2 的『火炬艦』給撻伐族而不是普恩族」）都應記入 [Error_List.md](Error_List.md) §三「命名衝突／待決議」。

**理由**：**避免未來重複討論**、**保持可追溯性**。

---

## 九、審查失敗的補救

**若 in-game 測試發現嚴重問題**（例如某段對話完全無法讀）：

1. **回滾**到上一版（`git checkout` shipped 譯文）
2. **hotfix**（緊急修正該檔）
3. **重跑**完整流程
4. **記錄**教訓到 [Error_List.md](Error_List.md)

---

## 十、參考來源

- [Consistency_Check.md](Consistency_Check.md) 自動化 CI
- [Error_List.md](Error_List.md) 錯誤累積
- [Dialogue_Rule.md](../08_Translation_Rules/Dialogue_Rule.md) §十 自查清單
- [QA_Check.md](../09_AI_Prompt/QA_Check.md) AI 檢查提詞
