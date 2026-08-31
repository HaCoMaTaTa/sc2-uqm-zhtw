# AI Prompt: Terminology Consistency Audit（詞彙一致性稽核）

> **使用場景**：專案已臨近收尾階段。歷經多輪 dossier 修訂與 Rebuild-Compare 執行後，需**跨檔案**檢查名詞是否統一——**規範內部一致** + **所有種族譯文對照規範**。
>
> **對照**：
> - [Translate_Dialogue.md](Translate_Dialogue.md) — 純從原文重譯（單族）
> - [Reaudit_Dialogue.md](Reaudit_Dialogue.md) — 逐 token 審視 shipped（單族）
> - [Rebuild_And_Compare.md](Rebuild_And_Compare.md) — clean-room 重譯 + 對照決策（單族）
> - **本檔**（Terminology_Audit.md）— **跨族 + 跨規範檔**的名詞一致性稽核
>
> **v0.1** 建立於 2026-08-18（Task 2）。對應血淚教訓：2026-08-17 UI 詞彙統一 audit（見 `/memories/repo/audit-policy.md`）發現 **4 方詞彙不一致**（melnorme 對白 / gamestrings DOS 段 / setupmenu / Tech_Names.md 有 7 條至少 2 種譯法並存）。本 workflow 一次性掃全專案避免未來類似問題。

---

## 一、何時用本 prompt

### ✅ 適用情境

- **專案接近收尾**、想確認全專案名詞統一（本 workflow 的**主要用途**）
- 新增規則檔或 dossier 後、想確認未破壞既有 canonical
- 週期性（例：每 4 週）跑一次、及早發現 canonical 漂移
- **加入新族 / 新艦艇 / 新技術** 後檢查是否命名已納入既有系統

### ❌ 不適用情境

- 單族翻譯品質稽核 → 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md)
- 單族從 v3 clean-room 重譯 → 用 [Rebuild_And_Compare.md](Rebuild_And_Compare.md)
- 只想找簡體字/typo → 用 [QA_Check.md](QA_Check.md)（若存在）或 `_check_zh_purity.py`

---

## 二、使用方法

### 2.1 開新 chat session

**必須**在新 chat 開始（不要在正在做其他任務的 session 用本 prompt——舊 context 會影響 canonical 判斷）。

### 2.2 貼上本檔 + 開始執行

在**新 chat** 貼上以下**兩段**作為第一則訊息：

```
[本檔全文]

──────────────────────

【本次任務】
執行 Terminology Consistency Audit 兩個 phase：
  Phase 1: StarControl2_TW_Localization/ 規範檔內部一致性稽核
  Phase 2: 25 races shipped translations 對照規範稽核 + 跨族名詞歧異偵測
```

### 2.3 可選參數

- `scope: full` — Phase 1 + Phase 2 全跑（**預設** · 推薦）
- `scope: rules-only` — 只跑 Phase 1（規範內部一致）
- `scope: dialog-only` — 只跑 Phase 2（譯文對照）· 假設規範已通過稽核
- `granularity: high` — 每個詞彙產出 3-5 選項供決策（預設）
- `granularity: mid` — 只針對 ambiguous 詞列選項
- `output: full-report` — 產出完整 markdown 報告（預設）
- `output: brief` — 只列 red flag + 統計

---

## 三、AI 執行守則（**你就是這個 AI**）

### 3.1 絕對禁止

- ❌ **臆測** canonical（不確定就 grep 全庫或問使用者）
- ❌ **獨自決定**變更 canonical（**必以使用者裁定為準**）
- ❌ **改動 shipped translations**（本 workflow 只**識別問題**、不動 JSON。實際修改由使用者用其他 workflow 執行）
- ❌ **加新規則**到規範檔（本 workflow 只稽核既有規範一致性）
- ❌ **改 dossier §四/五/六 內容**（同上）

### 3.2 一定要做

- ✅ **shipped-preference 策略**（見 2026-08-17 教訓）：**shipped 對白 canonical 為權威**、規範檔若不一致則**建議修規範**、不是修對白
- ✅ 每個「疑似歧異」都要**列出所有出現位置** + **出現次數統計** + **判斷是否真的衝突**（可能是 v0.4 canonical 已升級但舊 shipped 尚未 update · 這不是衝突而是 delta）
- ✅ 遇到**Race 名 / Ship 名 / 角色名 / 地名 / 技術名**歧異時 · 從 07_Glossary/ 為主依據
- ✅ 遇到**Voice / 稱謂 / 招牌詞** 歧異時 · 從 02_Races/<Race>.md §四 為主依據
- ✅ 每完成一個 phase 給使用者**進度報告** + **累計統計**
- ✅ 每個衝突項附**來源檔案路徑 + 行號**（便於使用者驗證）

### 3.3 使用者互動風格

使用者慣用 prompt 前綴「**優化題詞後執行 不臆測 有問題請問我**」。你的行為：
- 若使用者要求含糊 · **先重述你理解的任務**再執行
- **不臆測**——遇不明確一律 Q&A 列 A/B/C 選項
- 使用者答覆常為單字母（A/B/C）或短列表（`R1=A R2=B R3=C`）· 你的選項 label 要一致
- **不擴散任務**——使用者說「先做 X」你就只做 X

---

## 四、Phase 1 · 規範檔內部一致性稽核

### 4.1 待讀規範檔（**依序讀 · 每讀完一個回報 3-5 條要點**）

| # | 檔案 | 用途 |
|---|---|---|
| 1 | `07_Glossary/Master_Glossary.md` | 主 canonical 表（權威） |
| 2 | `07_Glossary/Race_Names.md` | 種族名鎖定 |
| 3 | `07_Glossary/Character_Names.md` | 角色名鎖定 |
| 4 | `07_Glossary/Ship_Names.md` | 艦名鎖定 |
| 5 | `07_Glossary/Tech_Names.md` | 技術名鎖定 |
| 6 | `07_Glossary/Place_Names.md` | 地名鎖定（星系 / 星座 / 星球） |
| 7 | `07_Glossary/Fixed_Terms.csv` | v0.4 canonical 對照表 |
| 8 | `07_Glossary/Forbidden_Translations.md` | 禁止譯法（若存在） |
| 9 | `02_Races/*.md`（25 檔）| 每族 dossier §四（voice/自稱/招牌詞）+ §五（翻譯規則）+ §六（範例）· **§四 自稱 / 稱訪客 / 核心詞彙表為權威來源** |
| 10 | `03_Characters/*.md`（若存在）| 角色 dossier |
| 11 | `04_Ships/*.md`（若存在）| 艦艇 dossier |
| 12 | `05_Technology/Ship_Modules.md` | 旗艦模組（Fuel Tank / Crew Pod / Hellbore / Shiva 等） |
| 13 | `05_Technology/Weapon_Systems.md` | 各族武器（Fusion Bolt / Lightning / Flame Jets 等） |
| 14 | `05_Technology/Precursor_Artifact.md` | 先驅文物（Ultron / Rosy Sphere / Aqua Helix 等） |
| 15 | `05_Technology/Resource_Elements.md` | 元素 / 化合物 / 礦物 |
| 16 | `06_Locations/*.md`（若存在）| 地點 dossier |
| 17 | `01_World_Lore/*.md`（若存在）| 世界觀 |
| 18 | `08_Translation_Rules/Style_Guide.md` | 台灣化用語 |
| 19 | `08_Translation_Rules/Alien_Speech_Rule.md` | §1.6 排版 icon 規則 + §1.4 感嘆詞政策 |
| 20 | `08_Translation_Rules/Dialogue_Rule.md` | 對話規則（若存在） |
| 21 | `08_Translation_Rules/Humor_Rule.md` | 各族幽默規則 |
| 22 | `08_Translation_Rules/Naming_Rule.md` | 命名規則 |
| 23 | `08_Translation_Rules/Punctuation_Rule.md`（若存在）| 標點規則 |

### 4.2 Phase 1 執行步驟

#### 步驟 1.1 · 建立 Canonical Master Table

從所有規範檔**抽取所有已鎖定的 canonical 詞**，建立主表：

```markdown
| 英文 | 鎖定中譯 | 權威來源 | 備註 |
|---|---|---|---|
| Ur-Quan | 烏寬族 | Race_Names.md · Master_Glossary.md §四 | R1=A（Kzer-Za 派系）|
| Kzer-Za | 克澤札 | Master_Glossary.md · shipped chmmr | |
| Kohr-Ah | 柯亞族 | Race_Names.md | |
| Frungy | Frungy（保留原文） | Zoq_Fot_Pik.md §四 | |
| ... | ... | ... | ... |
```

**要求**：**至少 200-300 條**（涵蓋所有 race / ship / character / tech / location canonical）。

#### 步驟 1.2 · 內部衝突偵測

對 canonical master table 逐條掃描：
- **同一英文** 在**不同規範檔**有**不同鎖定中譯** → **🔴 高嚴重度**（權威衝突）
- **同一中譯** 在**不同規範檔**指涉**不同英文** → **🔴 高嚴重度**（雙關 / 撞名）
- **同族 dossier §四** 中的自稱/稱訪客與 **Alien_Speech_Rule.md §1.4** 的政策衝突 → **🟠 中嚴重度**
- **02_Races/<Race>.md §六 範例**內出現的譯詞與 **§四 canonical 表**不一致 → **🟠 中嚴重度**
- **04_Ships/*.md** 或 **05_Technology/*.md** 內用的譯詞與 **07_Glossary/** 主表不一致 → **🟠 中嚴重度**

#### 步驟 1.3 · 產出 Phase 1 報告

`_terminology_audit_phase1_<date>.md`：

```markdown
# Phase 1 · 規範檔內部一致性稽核（YYYY-MM-DD）

## 統計
- 抽取 canonical 詞總數：N
- 衝突項：M
  - 🔴 高嚴重度（權威衝突）：X
  - 🟠 中嚴重度（範例/dossier 與主表不一致）：Y
  - 🟡 低嚴重度（可能是 delta 尚未同步）：Z

## Canonical Master Table（附錄）
[N 條完整表]

## 🔴 高嚴重度衝突 X 項

### #1 · Ur-Quan Dreadnought 譯法衝突

**衝突內容**：
- Ship_Names.md L23：**無畏艦**（v0.2 canonical）
- Master_Glossary.md §五：**無畏艦**（一致）
- shipped chmmr.zh-TW.json L45：**無畏艦**（一致）
- **04_Ships/Hierarchy_Ships.md L12**：**恐怖艦**（**🔴 不一致**！可能是舊譯未同步）

**建議**：以 shipped-preference 修 04_Ships/Hierarchy_Ships.md L12 → **無畏艦**

**你的選擇**： A. 接受建議 · B. 保留 04_Ships 譯法 · C. 自訂

### #2 · ...

## 🟠 中嚴重度衝突 Y 項

### #1 · Zoq_Fot_Pik.md §六 範例用「憤怒者」而 §四 canonical 是「烈憤艦」

...
```

**完成 Phase 1 後**：等使用者逐項決策 → **進入 Phase 2**。

---

## 五、Phase 2 · 譯文對照規範稽核 + 跨族名詞歧異偵測

### 5.1 待掃 shipped translations（25+ 檔）

```
uqm-work/translations/*.zh-TW.json
```

含 25 races comm dialog：`androsynth（如有）· arilou · chmmr · commander · druuge · ilwrath · kohrah · melnorme · mycon · orz · pkunk · probe · safeones · shofixti · slylandro · spathi · starbase · supox · syreen · talkingpet · thraddash · umgah · urquan · utwig · vux · yehat · yehatrebels · zoqfotpik`

+ **UI 相關**：`gamestrings.zh-TW.json` · `setupmenu.zh-TW.json` · `intro.zh-TW.json` · `ending/*.json` · `gameover/*.json` · `lander/energy/*.json`

### 5.2 Phase 2 執行步驟

#### 步驟 2.1 · 對 Canonical Master Table 每一條，掃全 translations

對 **Phase 1 產出的 canonical master table** 中的每一條：

```python
for canonical_en, canonical_zh in master_table:
    for json_file in shipped_translations:
        find all occurrences of canonical_en (in _notes / dialog / etc.)
        find all zh translations used for canonical_en
        detect discrepancies:
            - shipped 用了不同中譯 → 🔴 高嚴重度
            - shipped 用舊譯（v0.3 前 canonical）→ 🟠 中嚴重度 delta
            - shipped 用縮寫版（如「無畏」代替「無畏艦」）→ 🟡 低嚴重度
```

#### 步驟 2.2 · 跨族名詞歧異偵測

對每個 canonical（**特別是 race / ship / character / place**）：
- **列出所有引用該詞的 shipped translations 檔案**（Race A 提到 Race B 的名字時 · 全部找出）
- **判斷是否用同一譯法**
- 例：`Ur-Quan` 出現在 ilwrath / spathi / arilou / melnorme / mycon 等對白 · 每處用同一「烏寬族」譯名 · 若某族用「烏寬」（少「族」字）→ **🟠 中嚴重度歧異**

**特別關注跨族名詞群組**：

| 群組 | 涉及 canonical | 交叉出現於 |
|---|---|---|
| **Ur-Quan 系** | Ur-Quan / Kzer-Za / Kohr-Ah / Dreadnought / Marauder / Sa-Matra | 幾乎所有族 comm |
| **Precursor 系** | Precursors / Ultron / Rosy Sphere / Glowing Rod / Trident of Wimbli / Aqua Helix / Taalo Shield / Utwig Bomb / Sun Device / Portal Spawner | melnorme / druuge / utwig / arilou / etc. |
| **地名系** | Alpha Tucanae / Zeta Persei / Beta Librae / Draconis / Sol / Vega / Antares 等 | melnorme / commander / 各族母星描述 |
| **武器系** | Fusion Bolt / Autotracking Laser / Flame Jets / Antimatter Cone / etc. | thraddash / melnorme 對話 |

#### 步驟 2.3 · Voice / 稱謂統計（audit-policy §六 第 6 層 delta 版）

對每 race JSON：
- 統計族自稱 count（我方 / 我族 / 我等 / 我 / 咱們 / 本XX / etc.）
- 對照 `02_Races/<Race>.md §四「自稱」表` · 判斷是否有 dossier 建議的自稱**未被 shipped 採用**（audit-policy 血淚教訓：Syreen 我等姐妹被列為 canonical 但 shipped 用 0 次 · 塌陷）

#### 步驟 2.4 · 產出 Phase 2 報告

`_terminology_audit_phase2_<date>.md`：

```markdown
# Phase 2 · 譯文對照規範 + 跨族歧異稽核（YYYY-MM-DD）

## 統計
- 掃描 canonical 條目：N
- 檢查 shipped translations：M 個 JSON
- 涉及 tokens：X（所有 translations 加總）
- 衝突項：Y
  - 🔴 shipped 用錯 canonical / 用不存在譯法：A
  - 🟠 shipped 用舊 canonical（delta 未同步）：B
  - 🟡 shipped 縮寫 / 意譯（不算錯但可統一）：C
  - 📊 Voice 塌陷（dossier 自稱 shipped 用 0 次）：D

## 🔴 高嚴重度 A 項

### #1 · Ur-Quan 譯法歧異

**Canonical**：**烏寬族**（Race_Names.md）

**shipped 使用狀況**：
- `ilwrath.zh-TW.json`：烏寬族 × 12 · 烏寬 × 3（其中 3 處縮寫）· ✅ 主流一致
- `spathi.zh-TW.json`：烏寬族 × 8 · ✅
- `melnorme.zh-TW.json`：烏寬 × 34（**全部沒「族」字**）· **🟠 舊譯 · 建議統一為「烏寬族」** · 34 處
- `arilou.zh-TW.json`：烏寬族 × 5 · ✅
- `commander.zh-TW.json`：烏寬人 × 2（**用「烏寬人」**）· **🔴 不同譯法** · 2 處

**建議**：
- melnorme 34 處縮寫「烏寬」→ 統一為「烏寬族」
- commander 2 處「烏寬人」→ 統一為「烏寬族」

**你的選擇**：
  A. 全部統一為「烏寬族」
  B. melnorme 保留「烏寬」（簡潔）· commander 改「烏寬族」
  C. 自訂

### #2 · ...

## 🟠 中嚴重度 B 項
[list]

## 🟡 低嚴重度 C 項（僅資訊 · 不需決策）
[list]

## 📊 Voice 塌陷 D 項

### #1 · Syreen 我等姐妹 shipped 用 0 次（dossier 標為 canonical）

...

## 附錄 · 涉及所有 shipped 檔的 canonical 交叉表

| Canonical | ilwrath | spathi | melnorme | arilou | commander | ... |
|---|---|---|---|---|---|---|
| 烏寬族 | 12+3縮 | 8 | 0（用縮）| 5 | 2「人」| ... |
| 柯亞族 | ... | ... | ... | ... | ... | ... |
```

---

## 六、產出檔案清單

| 檔案 | 用途 | commit? |
|---|---|---|
| `uqm-work/_terminology_audit_phase1_<date>.md` | Phase 1 規範衝突報告 + 使用者決策記錄 | ✅ commit（audit trail） |
| `uqm-work/_terminology_audit_phase2_<date>.md` | Phase 2 譯文歧異報告 + 使用者決策記錄 | ✅ commit |
| `uqm-work/_terminology_master_table_<date>.md` | Canonical Master Table（附錄） | ✅ commit |

**注意**：本 workflow **不產出實際修改的 JSON / md** · 只**識別問題 + 記錄決策**。實際修改依決策清單交付：
- 若使用者決定改規範檔 → 手動編輯或另開 workflow
- 若使用者決定改 shipped JSON → 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md) 分族逐項修

---

## 七、決策原則（回顧 · 供 AI 執行時參照）

### shipped-preference 策略（**主原則**）

**血淚教訓 2026-08-17**：4 方詞彙不一致（melnorme 對白 / gamestrings DOS 段 / setupmenu / Tech_Names.md 有 7 條至少 2 種譯法並存）· 教訓：**shipped 對白已與玩家熟悉度綁定** · 修 Tech_Names 對齊 shipped 而**非反過來**。

**具體優先序**：
1. **shipped 對白 多數用法**（melnorme + 各族 comm）
2. **07_Glossary/ 主表**（若 shipped 沒對應 · 用主表）
3. **02_Races/<Race>.md §四**（voice / 稱謂 專屬）
4. **v0.4 / v0.5 / v0.7 canonical 升級**（若有明確版本標記）
5. **AI 建議譯法**（**最後手段** · 需使用者裁定）

### 例外：純化學/物理術語

- **標準化學名**（甲酸 / 磷酸 / 一氧化二氮 等）優先用**台灣化學正式用語**
- **標準物理術語**（量子黑洞 / 磁單極 / 超流體）優先用**中華民國物理學會**譯詞

### 例外：外星專有名詞（Aguuti / Reisburg / Tzo 等）

- 若 shipped comm 無提及 → **完全音譯**
- 若 shipped comm 有提及 → **shipped-preference**

---

## 八、Invocation 範例

### 標準用法（推薦）

新 chat · 第一則訊息：
```
[本檔全文]

──────────────────────

【本次任務】
執行 Terminology Consistency Audit 兩個 phase。
```

### 帶參數用法

```
[本檔全文]

──────────────────────

【本次任務】
執行 Terminology Consistency Audit。
scope: full
granularity: mid
output: full-report
```

### 只跑 Phase 1（規範內部）

```
[本檔全文]

──────────────────────

【本次任務】
只執行 Terminology Consistency Audit Phase 1（規範內部一致性）。
scope: rules-only
```

---

## 九、預期成果

執行完一次 Terminology Audit 後 · 你應該：

- ✅ 得到 `_terminology_master_table_<date>.md`（**200-300 條 canonical 主表** · 未來可反查任何詞的權威譯法）
- ✅ 得到 `_terminology_audit_phase1_<date>.md`（規範內部衝突 · 使用者決策記錄）
- ✅ 得到 `_terminology_audit_phase2_<date>.md`（譯文對照歧異 · 使用者決策記錄）
- ✅ 明確 action item 清單（哪些規範要修 · 哪些 shipped 要修 · 各多少項）

**下一步**（不在本 workflow 範圍）：
- 修規範檔 → 手動編輯或另開 workflow
- 修 shipped JSON → 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md) 分族處理
- 若量大 → 用 [Rebuild_And_Compare.md](Rebuild_And_Compare.md) 部分族重譯

---

## 十、失敗恢復

### 情境 A · Phase 1 chat 過長觸發 "Invalid string length"

Phase 1 需讀 20+ 規範檔 · chat 上下文可能過大：
1. 保留已產出的 partial `_terminology_master_table_partial.md`
2. 開新 chat · 貼本檔 + 「接手 Phase 1 · 已完成規範檔清單：[list]」
3. 續完成剩下規範檔 + 步驟 1.2/1.3

### 情境 B · Phase 2 chat 過長

Phase 2 需掃 25+ JSON · 若 chat 過長：
1. 保留 `_terminology_audit_phase2_partial.md`（處理過的 canonical 已含）
2. 開新 chat · 貼本檔 + 「接手 Phase 2 · 已處理 canonical：[前 N 條]」
3. 續處理剩下 canonical

### 情境 C · 使用者不同意 shipped-preference 策略

若使用者在多項衝突中反覆選「保留規範原譯」而非 shipped · 表示 **shipped-preference 不適合此專案**：
1. AI 應停下來 · 詢問使用者是否改用 **rules-preference 策略**
2. 若是 · 對後續衝突項預設建議改 shipped 對齊規範
