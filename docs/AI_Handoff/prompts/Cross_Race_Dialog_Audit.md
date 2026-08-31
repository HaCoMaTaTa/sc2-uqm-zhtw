# AI Prompt: Cross-Race Dialog Consistency Audit（跨族對話一致性稽核）

> **使用場景**：已翻譯好的 25+ 種族 shipped comm dialog JSON · 要**跨檔案掃描**所有名詞（族名 / 艦名 / 角色名 / 地名 / 技術名 / 招牌詞）· 找出**同一英文原文在不同族對白中被譯成不同中文**的所有歧異 · 讓玩家看到的譯法一致。
>
> **對照**：
> - [Translate_Dialogue.md](Translate_Dialogue.md) — 純從原文重譯（單族）
> - [Reaudit_Dialogue.md](Reaudit_Dialogue.md) — 逐 token 審視 shipped（單族）
> - [Rebuild_And_Compare.md](Rebuild_And_Compare.md) — clean-room 重譯 + 對照決策（單族）
> - [Terminology_Audit.md](Terminology_Audit.md) — **兩 phase 大稽核**：Phase 1 規範檔一致 + Phase 2 譯文對照規範
> - **本檔**（Cross_Race_Dialog_Audit.md）— **只掃譯文** · **不依賴** Phase 1 canonical master table · **可獨立執行**
>
> **v0.1** 建立於 2026-08-18（Task 2 · 專為「所有種族對白 JSON 跨檔案統一」情境設計）。

---

## 一、何時用本 prompt

### ✅ 適用情境

- 25+ 族對白 JSON 都翻譯完成 · 想確認**跨族**譯法一致（**主要用途**）
- 每次新增 / 修改一族對白後 · 快速檢查新譯法是否與其他族一致
- Terminology_Audit.md 的 Phase 1（規範檔一致）**太費時** · 想直接做 Phase 2（譯文一致）
- 週期性（例：每 2 週）跑一次 · 及早發現譯法漂移

### ❌ 不適用情境

- 單族翻譯品質稽核 → 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md)
- 想同時修規範檔 → 用 [Terminology_Audit.md](Terminology_Audit.md)（含 Phase 1）
- 只想找簡體字/typo → 用 `_check_zh_purity.py`

---

## 二、使用方法

### 2.1 開新 chat session

**必須**在新 chat 開始（舊 context 影響 canonical 判斷）。

### 2.2 貼上本檔 + 開始執行

在**新 chat** 貼上以下**兩段**作為第一則訊息：

```
[本檔全文]

──────────────────────

【本次任務】
執行 Cross-Race Dialog Consistency Audit：
掃 uqm-work/translations/*.zh-TW.json 所有已翻譯種族對白 ·
找出跨族名詞譯法歧異 · 產出決策報告。
```

### 2.3 可選參數

- `scope: all-races` — 掃所有 25+ races comm JSON（**預設** · 推薦）
- `scope: races=A,B,C` — 只掃指定 races（用於快速回歸）
- `focus: names-only` — 只掃 proper nouns（race/ship/character/place 名字）· 忽略 tech / 招牌詞
- `focus: full` — 掃所有名詞 + 招牌詞 + 稱謂（**預設**）
- `focus: voice` — 只掃 voice（自稱 / 稱訪客）跨族撞名（例：兩族都用「本座」）
- `min-races: N` — 一詞至少要出現在 N+ 族才報告（預設 2 · 即 2 族起）
- `output: full-report` — 完整報告 + 交叉表 + 決策清單（**預設**）
- `output: brief` — 只列衝突項 + 統計

---

## 三、AI 執行守則（**你就是這個 AI**）

### 3.1 絕對禁止

- ❌ **臆測** canonical（不確定就統計 shipped 用法或問使用者）
- ❌ **獨自決定**變更譯法（**必以使用者裁定為準**）
- ❌ **改動 shipped translations JSON**（本 workflow 只**識別問題** · 實際修改用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md) 分族處理）
- ❌ **改 dossier 或規範檔**（本 workflow 只掃譯文 · 不動規範）
- ❌ 因為某族 shipped 用 A 就認定 A 是 canonical（**要 統計比例 + 對照 Race_Names.md**）

### 3.2 一定要做

- ✅ **shipped-preference 策略**（見血淚教訓 2026-08-17）：**shipped 對白多數用法為權威候選** · 但要對照 `07_Glossary/Race_Names.md` / `Ship_Names.md` / `Character_Names.md` 主表確認方向
- ✅ 每個「疑似歧異」都要**列出所有出現位置**（檔案路徑 + 行號）+ **出現次數統計**
- ✅ 每個歧異都要**判斷是否真的衝突** — 可能是：
  - **舊譯 delta**（v0.4 前 canonical · shipped 尚未 update）· 這不是衝突而是待更新
  - **縮寫**（「烏寬」代替「烏寬族」）· 可能是 shipped 為了字數限制而縮寫
  - **對白角色情境**（如某族 NPC 對 Ur-Quan 用蔑稱「烏寬崽子」而非中性「烏寬族」）· 這是 voice 而非錯譯
- ✅ 每 phase 完成給使用者**進度報告** + **累計統計**
- ✅ 產出報告要**便於使用者驗證**（含檔案 + 行號 + 前後文）

### 3.3 使用者互動風格

使用者慣用 prompt 前綴「**優化題詞後執行 不臆測 有問題請問我**」· 你的行為：
- 若使用者要求含糊 · **先重述你理解的任務**再執行
- **不臆測**——遇不明確一律 Q&A 列 A/B/C 選項
- 使用者答覆常為單字母（A/B/C）或短列表（`R1=A R2=B R3=C`）· 你的選項 label 要一致
- **不擴散任務**——使用者說「先做跨族 JSON」你就只做跨族 JSON · 不主動去改規範

---

## 四、Phase A · 待掃 shipped translations 清單

### 4.1 主戰場（25+ races comm dialog · 必掃）

```
uqm-work/translations/<race>.zh-TW.json
```

依當前狀態（2026-08）· 涵蓋：

| # | Race | JSON 檔 | 備註 |
|---|---|---|---|
| 1 | Arilou | arilou.zh-TW.json | |
| 2 | Chmmr | chmmr.zh-TW.json | |
| 3 | Commander | commander.zh-TW.json | Human Commander |
| 4 | Druuge | druuge.zh-TW.json | |
| 5 | Ilwrath | ilwrath.zh-TW.json | |
| 6 | Kohr-Ah | kohrah.zh-TW.json | |
| 7 | Melnorme | melnorme.zh-TW.json | **含大量 tech/artifact 詞** |
| 8 | Mycon | mycon.zh-TW.json | |
| 9 | Orz | orz.zh-TW.json | `*` 標記 |
| 10 | Pkunk | pkunk.zh-TW.json | |
| 11 | Slylandro Probe | probe.zh-TW.json | |
| 12 | Safe Ones | safeones.zh-TW.json | Umgah subrace |
| 13 | Shofixti | shofixti.zh-TW.json | |
| 14 | Slylandro | slylandro.zh-TW.json | Home world |
| 15 | Spathi | spathi.zh-TW.json | |
| 16 | Starbase | starbase.zh-TW.json | Starbase Commander |
| 17 | Supox | supox.zh-TW.json | |
| 18 | Syreen | syreen.zh-TW.json | |
| 19 | Talking Pet | talkingpet.zh-TW.json | Dnyarri 系 |
| 20 | Thraddash | thraddash.zh-TW.json | |
| 21 | Umgah | umgah.zh-TW.json | |
| 22 | Ur-Quan | urquan.zh-TW.json | Kzer-Za 派 |
| 23 | Utwig | utwig.zh-TW.json | |
| 24 | Vux | vux.zh-TW.json | |
| 25 | Yehat | yehat.zh-TW.json | |
| 26 | Yehat Rebels | yehatrebels.zh-TW.json | |
| 27 | Zoq-Fot-Pik | zoqfotpik.zh-TW.json | |

**執行前**：`Get-ChildItem uqm-work/translations/*.zh-TW.json` 確認實際存在的檔案清單（可能有增減）。

### 4.2 副戰場（UI / narrative · 可選掃）

```
uqm-work/translations/gamestrings.zh-TW.json  # UI 大宗
uqm-work/translations/setupmenu.zh-TW.json    # 設定選單
uqm-work/translations/intro.zh-TW.json        # 開場
uqm-work/translations/ending/*.zh-TW.json     # 結局
uqm-work/translations/gameover/*.zh-TW.json   # 死亡結局
uqm-work/translations/lander/energy/*.zh-TW.json  # 生命偵測
```

**建議**：預設**先只掃主戰場**（4.1）· 若使用者要求 `scope: include-ui` 才加副戰場。

### 4.3 參考檔案（**只讀 · 不掃衝突**）

僅用作 canonical 對照 · 不視為譯文：

```
StarControl2_TW_Localization/07_Glossary/Race_Names.md
StarControl2_TW_Localization/07_Glossary/Ship_Names.md
StarControl2_TW_Localization/07_Glossary/Character_Names.md
StarControl2_TW_Localization/07_Glossary/Tech_Names.md
StarControl2_TW_Localization/07_Glossary/Place_Names.md
StarControl2_TW_Localization/07_Glossary/Master_Glossary.md
StarControl2_TW_Localization/07_Glossary/Fixed_Terms.csv  # 若存在
```

**用途**：當 shipped 內有歧異時 · 用來判斷「哪個譯法接近規範主表」· 幫助你在報告中標註「建議候選」。

---

## 五、Phase B · 執行步驟

### 步驟 B.1 · 建立跨族名詞索引

對每個主戰場 JSON · 抽取：

```python
for json_file in shipped_dialog_files:
    for entry in json_file.entries:
        english_text = entry["en"]      # 或 entry["_original"] / entry["source"]
        chinese_text = entry["zh"]      # 或 entry["translation"]

        # 抽取專有名詞（大寫開頭 · 或已知名詞清單）
        proper_nouns_en = extract_proper_nouns(english_text)

        for noun_en in proper_nouns_en:
            noun_zh = find_translation_in(chinese_text, noun_en)
            index[noun_en].add({
                "race": race_name,
                "file": json_file,
                "en_line": ...,
                "en_context": english_text[±30 chars],
                "zh_variant": noun_zh,
                "zh_context": chinese_text[±30 chars],
            })
```

**抽取的專有名詞類別**：

| 類別 | 例 | 特徵 |
|---|---|---|
| **Race 名** | Ur-Quan / Kohr-Ah / Kzer-Za / Yehat / Spathi | 常有連字號 · 大寫開頭 |
| **Ship 名** | Dreadnought / Marauder / Sa-Matra / Precursor Battleship | 大寫 · 常配動物/兵器意象 |
| **Character 名** | Fwiffo / Zex / Talana / ZEBRANKY / ZEX | 唯一人名 · 大寫 |
| **Place 名** | Alpha Tucanae / Sol / Vega / Antares / Groombridge | 星系 / 恆星 / 星座 |
| **Tech / Artifact 名** | Ultron / Aqua Helix / Rosy Sphere / Utwig Bomb | 文物 / 武器 · 大寫 |
| **招牌詞** | Frungy / Nyark / SNORT | 種族口頭禪 · 常保留原文 |
| **群體名** | Elders / Ancient Ones / Councilors / High Priest | 對某族內部階層的稱呼 |

**索引最終形式**：

```json
{
  "Ur-Quan": {
    "arilou.zh-TW.json": [{"line": 12, "zh": "烏寬族", "context": "..."}, ...],
    "ilwrath.zh-TW.json": [{"line": 34, "zh": "烏寬族", "context": "..."}, ...],
    "melnorme.zh-TW.json": [{"line": 8, "zh": "烏寬", "context": "..."}, ...],   // 34 處縮寫
    "commander.zh-TW.json": [{"line": 5, "zh": "烏寬人", "context": "..."}, ...] // 2 處異譯
  },
  "Kohr-Ah": { ... },
  "Dreadnought": { ... },
  ...
}
```

### 步驟 B.2 · 歧異偵測

對索引中的**每個英文詞**：

```python
for noun_en, occurrences in index.items():
    zh_variants = Counter(o["zh_variant"] for race_list in occurrences.values() for o in race_list)

    if len(zh_variants) > 1:
        # 有歧異
        canonical_candidate = zh_variants.most_common(1)[0][0]  # shipped-preference
        canonical_from_glossary = lookup_glossary(noun_en)      # 對照主表

        severity = classify_severity(zh_variants, canonical_from_glossary)
        # 🔴 高 · 用完全不同的譯法（如烏寬族 vs 烏寬人）
        # 🟠 中 · 縮寫變體（烏寬族 vs 烏寬）
        # 🟡 低 · 字數 delta 或標點差異
        # 📊 資訊 · voice 專屬歧異（不同族用不同蔑稱 vs 中性稱）

        report_conflict(noun_en, zh_variants, canonical_candidate, canonical_from_glossary, severity, occurrences)
```

### 步驟 B.3 · 特殊 pass — Voice 撞名偵測

**背景**：不同族有各自 voice canonical（見 dossier §四）· 若**兩族 dossier 都指定「本座」自稱** · 玩家會無法分辨誰在說話。

**執行**：
- 對每族 shipped JSON · 統計自稱詞（我 / 我方 / 我族 / 我等 / 本座 / 本尊 / 咱們 / 咱 / 吾 / etc.）· 出現次數
- 對每族 · 統計稱訪客詞（你 / 汝 / 爾 / 你們 / 諸君 / 貴族 / 客卿 / 陌生人 / etc.）
- 找**兩族+**都主要用同一自稱 → **📊 voice 撞名**

**特別關注 v0.7 政策**：
- 廢除文言助詞（吾 / 爾 / 汝 / 之 / 乃 / 矣 / 哉 / 焉 / 兒）
- 用「我方」/ 「我等」不用「吾等」
- 若 shipped 仍有廢字 → 標 **⚠️ v0.7 政策違反**

### 步驟 B.4 · 特殊 pass — 招牌詞保留檢查

**背景**：Alien_Speech_Rule §1.4 有招牌詞政策：某些外星招牌詞（Frungy / Nyark / SNORT / Aieee / etc.）**保留原文**或**保留原文 + 註解**。

**執行**：
- 對每族 · 對照 dossier §四「招牌詞」清單 · 檢查 shipped 是否遵守
- 若 shipped 直接翻譯（如 `Nyark!` → 「呲！」）· 標 **🟠 招牌詞被翻譯了**

### 步驟 B.5 · 產出主報告

`uqm-work/_cross_race_dialog_audit_<date>.md`：

```markdown
# Cross-Race Dialog Consistency Audit（YYYY-MM-DD）

## 統計

- 掃描 races 對白 JSON：N 個檔
- 索引 proper nouns：M 個唯一英文詞
- 總 occurrences：X 處
- 歧異項：Y
  - 🔴 高（完全不同譯法）：A
  - 🟠 中（縮寫 / 舊譯 / 招牌詞被翻）：B
  - 🟡 低（字數 delta / 標點）：C
  - 📊 資訊（voice 撞名 / 文言廢字）：D

## 🔴 高嚴重度衝突 A 項

### #1 · Ur-Quan（4 檔 · 3 種譯法 · 44 處）

| 譯法 | 出現族 | 次數 | 佔比 |
|---|---|---|---|
| **烏寬族** | arilou / ilwrath / spathi / chmmr / mycon / etc. | 87 | 66% |
| **烏寬**（縮寫）| melnorme | 34 | 26% |
| **烏寬人** | commander | 2 | 2% |
| **烏寬崽子** | ilwrath（僅蔑稱情境）| 8 | 6% |

**Glossary 主表**：Race_Names.md L23 = **烏寬族**（v0.4）
**推薦候選**：**烏寬族**（shipped 66% + glossary 一致）· melnorme 34 處**縮寫**建議統一（除非 dossier §四 melnorme voice 有規範縮寫）· commander 2 處**異譯**建議改。
**保留例外**：ilwrath 蔑稱情境 8 處「烏寬崽子」是 voice 特色 · **不動**。

**所有 occurrences 位置**（附錄有完整清單）：
- `arilou.zh-TW.json` L12 · L45 · L67 · ...（12 處）
- `melnorme.zh-TW.json` L8 · L23 · L56 · ...（34 處）
- `commander.zh-TW.json` L5 · L88（2 處）
- ...

**你的決策**：
  A. 全部統一為「烏寬族」（除 ilwrath 蔑稱）
  B. melnorme 34 處保留「烏寬」（simple form） · 只改 commander
  C. 全保留現狀 · 只加註解
  D. 自訂

### #2 · Dreadnought（3 檔 · 2 種譯法）
...

### #3 · Sa-Matra（3 檔 · 3 種譯法）
...

## 🟠 中嚴重度歧異 B 項

### #1 · Precursor（縮寫變體）
- 先驅族 / 先驅人 / 先驅（縮）· 建議統一「先驅族」

...

## 🟡 低嚴重度歧異 C 項（僅資訊 · 不需決策）
...

## 📊 Voice 撞名 · D 項

### #1 · 兩族+都主要用「本座」自稱

- `talkingpet.zh-TW.json` 本座 × 45（Dnyarri canonical）
- `xxx.zh-TW.json` 本座 × 12（可能 canonical 撞名）

**建議**：Dnyarri 保留 · xxx 換用其他自稱（見 dossier §四）

### #2 · v0.7 政策違反 · 文言助詞殘留

- `xxx.zh-TW.json` 「吾等」× 3 → 應為「我等 / 我方」
- `yyy.zh-TW.json` 「爾」× 8 → 應為「你」
...

## 附錄 A · 完整 occurrences 表（可 grep）

[每個 conflict noun 列全部 file:line]

## 附錄 B · 未衝突名詞清單（供資訊）

[所有 zh_variants == 1 的 noun · 表示全族一致 · 可以放心]
```

### 步驟 B.6 · 產出「應用清單」（供後續 workflow 使用）

`uqm-work/_cross_race_dialog_audit_<date>_actions.json`：

```json
{
  "audit_date": "2026-08-18",
  "decisions": [
    {
      "conflict_id": "#1",
      "noun_en": "Ur-Quan",
      "user_decision": "A",
      "canonical_zh": "烏寬族",
      "except": {
        "ilwrath.zh-TW.json": {
          "voice_variant": "烏寬崽子",
          "context": "蔑稱情境",
          "keep_lines": [45, 67, 89, ...]
        }
      },
      "actions": [
        {
          "file": "melnorme.zh-TW.json",
          "line": 8,
          "before": "烏寬",
          "after": "烏寬族"
        },
        ...
      ]
    },
    ...
  ]
}
```

**用途**：
- 使用者確認後 · 可交給另一個 workflow 或 Python 腳本自動 apply
- audit trail · commit 進 repo · 供未來查證

---

## 六、產出檔案清單

| 檔案 | 用途 | commit? |
|---|---|---|
| `uqm-work/_cross_race_dialog_audit_<date>.md` | 主報告（衝突 + 決策記錄） | ✅ commit（audit trail） |
| `uqm-work/_cross_race_dialog_audit_<date>_actions.json` | 應用清單（供後續 apply 腳本用） | ✅ commit |
| `uqm-work/_cross_race_dialog_audit_<date>_index.json`（可選）| 完整 noun index（供未來反查） | ✅ commit |

**注意**：本 workflow **不修改實際 shipped JSON** · 只**識別問題 + 記錄決策**。實際修改交付：
- 若少量（<20 項）· 使用者手動編輯 shipped JSON
- 若中量（20-100 項）· 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md) 分族處理
- 若大量（>100 項）· 寫 Python apply 腳本讀 `_actions.json` 自動 patch

---

## 七、決策原則（回顧 · 供 AI 執行時參照）

### shipped-preference 策略（**主原則**）

**血淚教訓 2026-08-17**：多方詞彙不一致時 · 修 Tech_Names 對齊 shipped **而非反過來**。

**具體優先序**：
1. **shipped 對白 多數用法**（統計 · > 50% 為權威候選）
2. **07_Glossary/ 主表**（若 shipped 多數與主表一致 · 完美；不一致時 · 對照 dossier § 四 決定）
3. **02_Races/<Race>.md §四**（voice / 稱謂 / 招牌詞 專屬）
4. **v0.7 政策**（廢除文言助詞 / 我方我等替代吾等 / 招牌詞保留原文）

### 何時保留歧異

**voice 特色**：某族 NPC 對某族用蔑稱（如 ilwrath 稱 Ur-Quan 「烏寬崽子」）· 而**中性情境**用「烏寬族」· 這是**dossier §四 canonical voice 特色** · **不動**。

**縮寫合理**：若 shipped 某段對白因**字數限制**（UI 有寬度）而縮寫 · 且**該處為玩家實際看到的**（例：戰鬥中戰報 · 需短）· 可保留縮寫 · 但要在報告中標註「字數限制」。

### 何時要問使用者

- 某詞在 07_Glossary 主表中**未定義**（沒 canonical 依據）· 但在 3+ 族被譯成 3+ 種譯法 → 必問
- 某詞的**多數譯法**與主表**不一致**（例：shipped 66% 「烏寬族」· 但主表寫「烏寬人」）→ 必問是否 shipped 或主表為準
- 招牌詞違反 dossier §四 政策時 · 是否修 shipped 還是修 dossier → 必問

---

## 八、Invocation 範例

### 標準用法（推薦）

新 chat · 第一則訊息：
```
[本檔全文]

──────────────────────

【本次任務】
執行 Cross-Race Dialog Consistency Audit：
掃 uqm-work/translations/*.zh-TW.json 所有已翻譯種族對白 ·
找出跨族名詞譯法歧異 · 產出決策報告。
```

### 帶參數用法

```
[本檔全文]

──────────────────────

【本次任務】
執行 Cross-Race Dialog Consistency Audit。
scope: all-races
focus: full
min-races: 2
output: full-report
```

### 只掃 voice 撞名（快速）

```
[本檔全文]

──────────────────────

【本次任務】
執行 Cross-Race Dialog Consistency Audit。
focus: voice
```

### 只掃前幾族回歸測試

```
[本檔全文]

──────────────────────

【本次任務】
執行 Cross-Race Dialog Consistency Audit。
scope: races=melnorme,commander,starbase,ilwrath,arilou
```

---

## 九、預期成果

執行完一次 Cross-Race Dialog Audit · 你應該：

- ✅ 得到 `_cross_race_dialog_audit_<date>.md`（主報告 · 所有衝突 + 使用者決策）
- ✅ 得到 `_cross_race_dialog_audit_<date>_actions.json`（可交付 apply 的清單）
- ✅ 明確 action item 清單（哪些 JSON 要改 · 各多少項）
- ✅ Voice 撞名報告（哪些族的 canonical 需要重新設計）
- ✅ v0.7 政策違反報告（哪些檔還有文言助詞）

**下一步**（不在本 workflow 範圍）：
- 少量修改 → 手動編輯
- 中量 → [Reaudit_Dialogue.md](Reaudit_Dialogue.md) 分族處理
- 大量 → 寫 Python 腳本讀 `_actions.json` batch apply
- 修完後 → `build_zh-TW.ps1` 重新打包 → 遞交實機驗證

---

## 十、失敗恢復

### 情境 A · Chat 過長（讀 25+ JSON 觸發 "Invalid string length"）

- 保留已產出的 partial `_cross_race_dialog_audit_partial.md`（含目前處理過的族 index）
- 開新 chat · 貼本檔 + 「接手 Audit · 已處理 races：[list]」
- 續處理剩下 races（步驟 B.1）
- 全部處理完後合併統計 · 進步驟 B.2 起

### 情境 B · Index 過大（10000+ occurrences）

- 分批處理：先掃 race 名 → 出報告 → 再掃 ship 名 → 出報告 → ...
- 每批獨立輸出 `_cross_race_dialog_audit_<date>_<category>.md`

### 情境 C · 使用者決策時間差過大

若使用者一次只決策幾項 · 剩下留待下次：
- 在 `_actions.json` 標記 `"status": "pending"` / `"decided"` / `"applied"`
- 下次執行時**只掃未決策項**（讀 `_actions.json` 過濾）
