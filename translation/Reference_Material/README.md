# Reference Material 歷史參考資料

> **本目錄功能**：保存 SC2 繁中化專案的**歷史參考檔案**——原始提詞、手冊 OCR、v0.2/v0.3 詞彙表、分析報告、使用者敘事指南。
> **權威性**：**這些檔案是歷史參考、非權威**。權威名詞表在 [../07_Glossary/](../07_Glossary/)。翻譯時**不採用本目錄的舊譯**。

---

## 一、目錄結構

```
Reference_Material/
├── README.md（本檔）
├── SC2_繁中化_AI翻譯提詞.md    ── v0.4 使用者原提詞（reference only）
├── starcontrol2_中文手冊_OCR.md ── 1990 年代粉絲手抄本 OCR（reference only）
├── SC2-詞彙對照表.md            ── v0.2 舊詞彙表（reference only）
├── SC2-詞彙對照表-v0.3.md       ── v0.3 詞彙表整合（reference only）
├── SC2-中文化分析報告.md        ── 早期分析報告
├── SC2-種族名稱重新設計.md      ── 早期種族命名研究
├── SC2-種族專屬字型策略.md      ── 字型策略研究
├── star_control_2_translation_guidelines_zhTW.md ── 早期翻譯指南
└── 激戰MS星雲 II 繁體中文化敘事語言學與種族在地化翻譯全指南.md
                                 ── 使用者敘事語言學指南（供 persona 參考）
```

---

## 二、各檔用途說明

### 2.1 `SC2_繁中化_AI翻譯提詞.md`（v0.4 原提詞）

**用途**：**歷史文件**——記錄使用者最初給 AI 的翻譯提詞。

**現行取代**：[../09_AI_Prompt/Translate_Dialogue.md](../09_AI_Prompt/Translate_Dialogue.md) 是重構後的版本。

**參考時機**：想追溯**某個譯法為何如此決定**的原始理由。

**注意**：本檔的某些譯名（例如「蘇菲斯特族」）為 v0.3，已被 v0.4 使用者重設為「修烈士族」——**以 [Master_Glossary.md](../07_Glossary/Master_Glossary.md) 為準**。

---

### 2.2 `starcontrol2_中文手冊_OCR.md`（手冊 OCR）

**用途**：1990 年代粉絲翻譯手冊的 OCR 結果，提供**時代語感參考**與**故事背景**。

**⚠️ 翻譯時一律不採用手冊譯名**：

| 手冊舊譯 | dialogue 應改為 |
|---|---|
| 爾奎人 | 烏寬族 |
| 雌雄同體人 | 安卓辛族 |
| 守護神 | 守衛艦（Guardian） |
| 激戰M星雲Ⅱ | Star Control II（系列名保留原文）|

**參考時機**：
- 讀**開場敘事**（巴頓艦長 20 年前故事）
- 讀**技術背景**（Vindicator 建造、先驅者遺跡）
- 讀**世界觀鋪陳**（爾奎人歷史）

---

### 2.3 `SC2-詞彙對照表.md`（v0.2 舊詞彙表）

**用途**：**v0.2 時期**的名詞對照表——保留作為版本沿革參考。

**現行取代**：[../07_Glossary/Master_Glossary.md](../07_Glossary/Master_Glossary.md)、[../07_Glossary/Fixed_Terms.csv](../07_Glossary/Fixed_Terms.csv)。

**注意**：**已被 shipped v0.3 及 v0.4 取代**。翻譯時**不採用**。

---

### 2.4 `SC2-詞彙對照表-v0.3.md`（v0.3 整合）

**用途**：**v0.3 時期**的整合表——增補 v0.2 未涵蓋的名詞。

**現行取代**：[../07_Glossary/Master_Glossary.md](../07_Glossary/Master_Glossary.md)。

**注意**：**8 個 v0.4 使用者重設種族名**（撻伐族、修烈士族、陰嘎族、翼哈特族、蟾亞族、蘇菩族、毒賈族、梅諾商）**不在此表**——查 v0.4 canonical 到 Master_Glossary.md。

---

### 2.5 `SC2-中文化分析報告.md`

**用途**：早期**專案設計**的分析報告。

**現行取代**：[../00_Project_Control/](../00_Project_Control/) 系列。

---

### 2.6 `SC2-種族名稱重新設計.md`

**用途**：**v0.2 時期**的種族命名策略研究——記錄「≤3 字＋族」原則的建立過程。

**現行取代**：[../08_Translation_Rules/Naming_Rule.md](../08_Translation_Rules/Naming_Rule.md)。

**參考時機**：想理解**為何某個族名如此翻譯**的設計歷程。

---

### 2.7 `SC2-種族專屬字型策略.md`

**用途**：字型 rasterization 策略研究——記錄各族字型的字寬、字高、CJK 支援情況。

**現行使用**：`../../uqm-work/build_zh-TW.ps1` 仍使用此策略。

**未來取代計畫**：待整合到 [../08_Translation_Rules/](../08_Translation_Rules/) 或新的 `Font_Strategy.md`。

---

### 2.8 `star_control_2_translation_guidelines_zhTW.md`

**用途**：**早期**（Phase 1）的翻譯指南。

**現行取代**：[../08_Translation_Rules/](../08_Translation_Rules/) 5 個檔案。

---

### 2.9 `激戰MS星雲 II 繁體中文化敘事語言學與種族在地化翻譯全指南.md`（**使用者敘事語言學指南**）

**用途**：**使用者提供的敘事語言學研究**——各族的深度人格描述、口頭禪、情緒觸發雷區。

**使用原則**（**v0.4 使用者 Q1=A 決策**）：
- ✅ **採用**：persona 細節（自稱、稱呼玩家、情緒觸發雷區、對話範例）
- ❌ **拒絕**：譯名（如「奧茲族」「斯帕蒂族」「烏爾寬」——一律用 System B 譯名）

**現行整合**：本檔的**persona 資料**已吸收到 [../02_Races/*.md](../02_Races/) 各族 dossier。**譯名**依 [Master_Glossary.md](../07_Glossary/Master_Glossary.md)。

**參考時機**：想深入了解某族的**性格細節**時直接讀本檔對應章節。

---

## 三、Reference_Material vs 07_Glossary 差異

| 特徵 | Reference_Material/ | 07_Glossary/ |
|---|---|---|
| **權威** | ❌ 歷史參考 | ✅ 現行 canonical |
| **翻譯採用** | ❌ 不採用 | ✅ 採用 |
| **版本** | v0.1 ~ v0.3 | **v0.4** |
| **更新頻率** | 凍結（不再更新） | 持續更新 |

**規則**：**衝突時以 07_Glossary/ 為準**。

---

## 四、為什麼保留這些檔案

**目的**：
- **版本追溯**（未來想理解某個決策是為什麼）
- **歷史文獻**（1990 年代粉絲翻譯是重要文化資產）
- **設計理由**（種族命名為何如此翻譯）
- **persona 深度**（新指南的 persona 細節非常有價值）

**不刪除的原因**：
- git 歷史已有備份，但實體檔案便於查閱
- 使用者敘事語言學指南是**未來翻譯新族的重要參考**（persona 部分）
- 手冊 OCR 保留**時代語感**

---

## 五、參考來源

- [../README.md](../README.md) 專案總覽
- [../07_Glossary/Master_Glossary.md](../07_Glossary/Master_Glossary.md) 現行權威名詞表
- [../08_Translation_Rules/](../08_Translation_Rules/) 現行翻譯規則
