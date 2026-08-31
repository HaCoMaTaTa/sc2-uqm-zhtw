# 翻譯工作流程 Workflow

## 一、單一 token 翻譯流程

每次拿到一個 `#(TOKEN_NAME)` 或一段文本，AI 應遵循以下 6 步：

```
Step 1  讀 World Lore    → 01_World_Lore/
Step 2  查 Glossary       → 07_Glossary/Master_Glossary.md
Step 3  確認角色身份     → 02_Races/<Race>.md 或 03_Characters/<NPC>.md
Step 4  分析原文意思     → 語意、語氣、潛台詞、雙關、諷刺
Step 5  翻譯             → 依 08_Translation_Rules/ 各規則產出
Step 6  QA 檢查          → 依 11_QA/ 自檢清單
```

## 二、種族分批工作流程

若你要一次翻一整個種族的對話檔（例如整個 `spathi.txt`）：

1. **開場**：把主提詞（`09_AI_Prompt/Translate_Dialogue.md`）+ 主 Glossary（`07_Glossary/Master_Glossary.md`）+ 該族 dossier（`02_Races/Spathi.md`）貼給 AI 當 system prompt
2. **分段**：每次貼 3–8 個 token 給 AI（避免上下文過長品質下降）
3. **邊翻邊補術語**：翻譯過程中若遇到新專有名詞（武器名、星球名、口頭禪），即時補進 Glossary 並提醒 AI
4. **每族結束**：跑 QA 檢查（`11_QA/Consistency_Check.md`）；把已翻譯詞條補入 `10_Translation_Memory/Translation_Memory.csv`
5. **提交**：`git commit -m "translate(<race>) v0.X: <count> tokens — <一句話特色>"`

## 三、跨族一致性檢查

每完成 3–5 個種族，做一次跨族檢查：

- 有沒有同一個外星名詞在不同 dossier 裡被翻成不同中文？
- 有沒有種族名混用（例如某處寫「烏寬」某處寫「烏爾寬」）？
- 星系名的英文括號有沒有全部帶上？

跑 `11_QA/Consistency_Check.md` 的檢查腳本。

## 四、遇到疑點時

| 情境 | 處理方式 |
|---|---|
| 對白有意象／哏不確定文化背景 | 查 `Reference_Material/` 底下的 RPG Resource Guide 對應章節縮圖／中文手冊 OCR |
| 遇到未鎖定的專有名詞 | 依 `08_Translation_Rules/Naming_Rule.md` 產出建議名，加註「〔新詞，待確認〕」等使用者確認後鎖進 Glossary |
| 角色語氣跟 dossier 描述有落差 | **以實際原文為準**，並回報使用者更新該族 dossier |
| 兩個 lore 來源說法衝突 | 遊戲對話 > RPG Resource Guide > 中文手冊；用戶最終仲裁 |

## 五、Session 開頭 checklist

在新 AI 對話中開始翻譯前，AI 應確認：

- [ ] 已讀過 `09_AI_Prompt/Translate_Dialogue.md`（主提詞）
- [ ] 已讀過 `07_Glossary/Master_Glossary.md`（術語鎖定表）
- [ ] 已讀過 `02_Races/<Race>.md`（目前翻譯的族 dossier）
- [ ] 知道 `#(TOKEN_NAME)` 要原樣保留
- [ ] 知道星系名需附英文原文
- [ ] 知道不用中國大陸用語、不加當代網路哏
