# AI Prompt: Rebuild and Compare（Clean-room 重譯 + shipped 比對 + 逐項擇優）

> **使用場景**：對**已 shipped 的 comm dialog JSON**,想以「不被舊譯錨定」的視角重新翻譯,再與舊版比對,挑出**當初知識不足所以錯過的優化點**。
>
> **對照**:
> - [Translate_Dialogue.md](Translate_Dialogue.md) — 純從原文重譯(空白 JSON)
> - [Reaudit_Dialogue.md](Reaudit_Dialogue.md) — 逐 token 審視 shipped(保留原譯者風格)
> - [QA_Check.md](QA_Check.md) — 純找問題(不建議改譯)
> - **本檔**(Rebuild_And_Compare.md)— clean-room 重譯 **＋** 自動 diff shipped **＋** 逐項擇優 **＋** 應用部署
>
> **v0.1** 建立於 2026-08-15 (應對 patch 009/010/011 完成後,重新檢視既有種族對話品質的需求)
>
> **v0.7.1**(2026-08-16)新增 **階段 2.5 · 順暢度自審 Read-Aloud Pass**——在 clean-room 翻譯後、diff 前,AI 自查一輪直譯生硬(被動語態/定語過長/冗餘代詞/標點英化/招牌詞漏套等 7 節清單),把明顯 AI 味的譯法自動修掉,避免這種問題進 diff 報告變 🟠 決策項浪費使用者時間。詳見 § 4.5。
>
> **⚠️ v0.7 全族審計提示（2026-08-15）**：若本次 Rebuild-Compare 對象為 **Yehat / Shofixti / Ur-Quan(Kzer-Za) / Ur-Quan(Kohr-Ah) / VUX / Chenjesu / Chmmr / Dnyarri** 這 8 族之一，**必先讀** [../00_Project_Control/Dossier_Voice_Audit_2026-08-15.md](../00_Project_Control/Dossier_Voice_Audit_2026-08-15.md) 確認新版語體定位。這些族原 dossier 曾誤標「文言化」，Rebuild 時**必須改用現代白話 + 排版 icon** 為底，不可套 shipped 舊譯的「爾/汝/吾」等文言助詞——否則會複製當初的錯誤定位。當前狀態追蹤見 [../00_Project_Control/Dossier_Revision_Progress.md](../00_Project_Control/Dossier_Revision_Progress.md)。

---

## 一、何時用本 prompt

### ✅ 適用情境

- **shipped 對話讀起來拗口**,但你不確定哪些 token 是重點
- Round 5 audit 之後有新的 canonical(v0.5.2+),想全面套用一次
- 想比較「當初翻譯」vs「現在知識」的差距,挖優化空間
- 玩到某族對話覺得**風格漂移**,想 clean-room 一次校正

### ❌ 不適用情境

- 尚未 shipped 的族(還沒 v0.3 JSON)→ 用 [Translate_Dialogue.md](Translate_Dialogue.md)
- 只想找 typo/簡體字/canonical 違規 → 用 [Reaudit_Dialogue.md](Reaudit_Dialogue.md)
- 只想找問題不改譯 → 用 [QA_Check.md](QA_Check.md)
- 大幅世界觀變動需重整 lore → 需人工重新設計 dossier 後再用本 prompt

---

## 二、使用方法

### 2.1 開新 chat session(重要)

**不要**在正在做其他任務的 session 用本 prompt——舊 context 會導致「假 clean-room」。

### 2.2 貼上本檔 + 指定族

在**新 chat** 貼上以下**兩段**作為第一則訊息:

```
[本檔全文]

──────────────────────

【本次任務】
對 <race> 族執行 Rebuild-Compare 流程。
```

例:

```
[本檔全文]

──────────────────────

【本次任務】
對 pkunk 族執行 Rebuild-Compare 流程。
```

### 2.3 可選參數(附加在【本次任務】之後)

- `批次: 分批` — 每批 30-50 token,分階段翻(避免 chat 過長)
- `批次: 一氣呵成` — 全部翻完再 diff(適合 <100 token 的族)
- `voice-audit: 完整` — 執行 audit-policy §六第 6 層 voice 定量統計(預設)
- `voice-audit: 跳過` — 只做讀順度(不推薦)
- `Q&A 詳細度: 高` — 每個未 canonical 詞都問 3-5 選項(預設)
- `Q&A 詳細度: 中` — 只問明顯 ambiguous 的
- `read-aloud: 完整` — 執行階段 2.5 順暢度自審全 7 節清單(預設 · **v0.7.1 新增**)
- `read-aloud: 保守` — 只修 § 4.5.1(英文語法殘留)+ § 4.5.3(標點/排版) · 不動 § 4.5.2/4.5.4/4.5.5(避免過度修訂 · 用於使用者信任度未建立時)
- `read-aloud: 跳過` — 完全不做自審 · 直接進 diff(**不推薦** · 生硬直譯會塞爆 🟠 diff)
- `dossier 缺項: fetch Ultronomicon` — 若 02_Races/<Race>.md 資訊不足,自動 web 查 Ultronomicon wiki 補齊
- `dossier 缺項: 只問我` — 遇到 dossier 缺項一律問使用者

預設: 分批 + 完整 voice + 高 Q&A + 完整 read-aloud + 只問我

---

## 三、AI 執行守則(**你就是這個 AI**)

### 3.1 絕對禁止

- ❌ **讀 `uqm-work/translations/<race>.zh-TW.json`**(shipped 版本)於階段 2 開始前
  - 若不慎讀到,**立即停止**,告知使用者需要重開 chat
- ❌ **讀其他 race 的 shipped JSON** 找靈感(污染 clean-room)
- ❌ **臆測未 canonical 的名詞**(必先 Q&A)
- ❌ **臆測 voice 情境**(必先參 dossier §四 + Q&A)
- ❌ **改 JSON 結構**(key 順序、`_notes` 位置)
- ❌ **偷抄 shipped**:若階段 3 diff 發現你「重譯」出跟 shipped 一模一樣的 token 超過 30%,懷疑階段 2 沒真的 clean-room,提醒使用者

### 3.2 一定要做

- ✅ 每讀一個規則檔,**回報 3-5 條學到的要點**給使用者(證明有讀)
- ✅ SEMANTIC-FIRST 五階段的 Q&A 決策,**列 3-5 選項** + 附註每選項的理由
- ✅ 每 30 tokens 給進度回報 + save partial 檔
- ✅ 遇到 dossier 未涵蓋的 voice 情境,**先問使用者**再翻
- ✅ 每個 diff 項附**英文原文對照** + **哪條規則支持推薦**

### 3.3 使用者互動風格(依觀察歷史 session)

使用者慣用 prompt 前綴「**優化題詞後執行 不臆測 有問題請問我**」。
你的行為:

- 若使用者要求含糊,**先重述你理解的任務**再執行
- **不臆測**——遇不明確一律 Q&A,列 A/B/C 選項
- 使用者答覆常為單字母(A/B/C)或短列表(`R1=A R2=B R3=C`),你的選項 label 要一致
- **不擴散任務**——使用者說「先做 X」你就只做 X

---

## 四、4 階段執行流程

### 階段 1 · 準備 · 讀規則檔(每讀完一個回報 3-5 條要點)

依序讀,**不可跳讀**:

| # | 檔案 | 用途 |
|---|---|---|
| 1 | `09_AI_Prompt/Translate_Dialogue.md` | System prompt · SEMANTIC-FIRST v0.5.2 五階段 |
| 2 | `02_Races/<Race>.md` | 種族 dossier(voice/自稱/招牌詞/文化) |
| 3 | `07_Glossary/Master_Glossary.md` | canonical 詞彙(v0.5.2+ 最新) |
| 4 | `07_Glossary/Race_Names.md` | 種族名稱鎖定 |
| 5 | `07_Glossary/Character_Names.md` | 角色名鎖定(如有該族相關 NPC) |
| 6 | `07_Glossary/Ship_Names.md` | 艦名鎖定(該族艦艇) |
| 7 | `08_Translation_Rules/Alien_Speech_Rule.md` | v0.5.2 Phase 14c 全譯政策(感嘆詞、宗教、gag) |
| 8 | `08_Translation_Rules/Style_Guide.md` | 台灣化用語 |
| 9 | `08_Translation_Rules/Dialogue_Rule.md` | 對話規則(§4.4 星圖 §4.5 標點) |
| 10 | `08_Translation_Rules/Naming_Rule.md` | 命名規則 |
| 11 | `08_Translation_Rules/Humor_Rule.md` | 該族幽默規則(§2.X 節查該族) |
| 12 | `/memories/repo/audit-policy.md` | Level 3 六層檢查(重點:第 4 層讀順度、第 6 層 voice 定量) |
| 13 | `/memories/repo/uqm-translation-purity.md` | canonical zh 名鎖 + FORBIDDEN 變體 |
| 14 | `/memories/repo/uqm-translation-style.md` | 玩家 response vs NPC dialog 差異 |
| 15 | `/memories/repo/sc2-translation-workflow.md` | User interaction style + 星名 postfix |

**如果**該族有 v0.5.2 Round 5 audit 記錄(見 audit-policy.md L119),額外掃該族的近期 canonical 升級。

### 階段 2 · Clean-room 翻譯

**⛔ 禁止讀** `uqm-work/translations/<race>.zh-TW.json`

**✅ 只讀** `uqm-work/extracted/base/base/comm/<race>/<race>.txt`(英文原文)

執行 SEMANTIC-FIRST 五階段(Translate_Dialogue.md §三·五):

1. **① 資料蒐集**(階段 1 已完成)
2. **② 原文分析**:掃 `<race>.txt`,分類 token 主題(hello / goodbye / info / attack / …)
3. **③ Q&A 決策提案**:未 canonical 名詞 / voice 情境 / 感嘆詞政策 → **列選項問使用者**,不臆測
4. **④ 翻譯**:等使用者 approve Q&A 後才開始逐 token 翻
   - 若參數 `批次: 分批`:每 30-50 token 一批,每批完存 partial 檔
5. **⑤ 3-gate verify**:
   - purity: `python _check_zh_purity.py --strict --race <race> --file translations/<race>.zh-TW.v2.json`
   - line-count:對照原文 token 數 + `\n` 數量
   - Lua template:`<% ... %>` 逐一比對第一參數是 CJK/rules-compliant
6. **⑥ 順暢度自審 · Read-Aloud Pass**(**v0.7.1 新增 · 產 diff 前必做**):
   - **目的**:抓「直譯生硬」問題於 diff 前 · 避免這種明顯 AI 味的翻譯被丟給使用者當 diff 項決策(浪費使用者 token · 也污染 audit trail)
   - **執行方式**:**逐 token 讀一遍**,對每 token 套下面 **§ 4.5 順暢度自審清單** · 遇到命中項目就修 · 產出 **self-fix log** 一併輸出
   - **輸出檔**:
     - 修訂結果**覆寫**回 `<race>.zh-TW.v2.json`(**同檔** · 保留 partial-N 為修前備份)
     - self-fix log 寫入 `uqm-work/_selfaudit_<race>_v2_readaloud.md`
   - **完成報告格式**:
     ```
     ⑥ Read-Aloud Pass 完成
     - 掃過 tokens: N
     - 命中「直譯生硬」項目: M(P%)
     - 分類統計:被動語態改主動 X · 過長定語拆分 Y · 冗餘代詞/量詞刪除 Z · 語序台化 W · 標點英化修正 V · 招牌詞漏套補入 U · 其他 T
     - self-fix log: uqm-work/_selfaudit_<race>_v2_readaloud.md
     ```
   - **重要邊界**:命中「順暢度自審清單」的 → **AI 自己直接改**、**不列為 diff 項**;沒命中但**兩種譯法皆通** → **保留 rebuild 版**、**列為 🟠 措辭 diff 交使用者決策**

**輸出**:`uqm-work/translations/<race>.zh-TW.v2.json`(**不覆蓋 shipped** · **已含 ⑥ Read-Aloud 修訂**)

### 階段 2.5 · 順暢度自審清單(**v0.7.1 新增 · 對應 ⑥ Read-Aloud Pass 逐項套用**)

> **判斷邏輯**:
> - **命中下列 § 項** → **AI 自己改** · 記入 self-fix log · **不當 diff 項**
> - **兩種譯法皆通** · 未命中直譯症狀 → **保留 rebuild 版** · **列 🟠 交使用者決策**
> - **改動涉及 canonical / 招牌詞 / voice 判斷** → **不改** · **升級為 🔴 交使用者決策**(因為這不是「順暢度」問題 · 是「原則」問題)
>
> **邊界原則**:自審是「**擦掉 AI 味**」· 不是「**改善原文之外的表達**」——若原文冷淡,譯文也要冷淡;不要為順暢加詞。

#### § 4.5.1 英文語法殘留

| 症狀 | 例(生硬 → 順暢) | 說明 |
|---|---|---|
| **被動語態直譯 `被…做…`** | 「訊息被送出了」→ 「訊息送出了」/「已送出訊息」 | 中文較少用「被」;主動或動詞前置更順 |
| **`將被`/`已被`** 濫用 | 「你將被送去餵高爐」→ 「你會被送去餵高爐」/「他們會把你送去餵高爐」 | 保留「被」但去掉「將」;或改主動 |
| **英文分詞子句直翻定語** | 「一個站在山上舉著武器咆哮的戰士」→ 「山上有個戰士,舉著武器咆哮」 | 中文用短句銜接,不堆疊定語 |
| **`一個/這個/那個`** 濫用 | 「這是一個絕無僅有的機會」→ 「這是絕無僅有的機會」 | 英文 a/an/the → 中文常可省 |
| **英文連詞硬翻 `和/而且/但是/或者`** | 「我方將戰鬥而且我方將勝利」→ 「我方將戰鬥,並取得勝利」 | 中文用逗號 · 標點連接更順 |
| **英文抽象名詞直翻** | 「進行一次調查」→ 「調查一下」 | 英文 nominalization(do a X)→ 中文動詞化更順 |
| **英文時間狀語末尾** | 「我方將攻擊你們,在明天」→ 「明天我方就要攻擊你們」 | 中文時間狀語習慣放句首 |

#### § 4.5.2 中文語感問題

| 症狀 | 例 | 說明 |
|---|---|---|
| **代詞冗餘** | 「我方看到它們了,它們正在逃跑」→ 「我方看到了,它們正在逃跑」/「看到了,他們在逃」 | 中文可省主語/賓語代詞 |
| **量詞漏配/錯配** | 「三個艦」→ 「三艘艦」 | 種族族別要有正確量詞 |
| **語氣尾巴生硬** | 「這是好的」→ 「這樣挺好」/「這樣可以」 | 「是…的」句式常過於形式化 |
| **重複疊詞未破** | 「我方感謝您 · 我方感謝您 · 我方感謝您」若原文只是 `Thank you.` → 只譯一次 | 只有原文本身重複才保留節奏 |
| **口語 vs 書面錯配** | 對白該口語卻用「進行」「實施」「予以」 | 依 dossier §四 voice · 對白多用口語動詞 |
| **兩字動詞硬拆** | 「進行殺害」→ 「殺掉」/「殺了」 | 中文口語常單字動詞 |

#### § 4.5.3 標點/排版

| 症狀 | 例 | 說明 |
|---|---|---|
| **半形標點殘留** | `,;.:?!"'` → `，；。：？！「」『』` | 中文一律全形(**除非 shipped canonical 明確用半形**) |
| **省略號用 `...`** | `...` → `……` | 中文用兩個全形省略號 |
| **破折號用 `--`** | `--` → `——` | 中文用全形破折號 |
| **空格殘留** | 「艦長 ,你好」→ 「艦長,你好」 | 全形標點兩側不留空格 |
| **中英混排無空格** | 「使用Frungy時」→ 「使用 Frungy 時」 | 中英文之間留空格(依 Style_Guide) |
| **破段/斷行漂移** | 譯文 `\n` 數不等於原文 | line-count gate 已檢 · 但要人眼再看句氣是否斷得對 |

#### § 4.5.4 Voice / Dossier 一致性(**輕度**)

| 症狀 | 例 | 說明 |
|---|---|---|
| **稱謂漂移** | 前 token「艦長」中 token「你」後 token「船長」 → 統一 | 依 dossier §四「對玩家的稱呼」表 |
| **自稱漂移** | 前用「我方」後用「本族」再前用「我們」→ 統一(或分情境用) | 依 dossier §四「自稱」表 |
| **招牌詞漏套** | dossier §四表格中的招牌 canonical 該用未用 → 補入 | 例:Druuge 該有 `Depart. → 離開。`、Thraddash 該有 `SNORT!` |
| **您/你不一致** | 熱情話術用「您」拒絕時用「你」對嗎? → 依 dossier §四 voice **兩段區分** | 有意的兩段(如 Druuge)保留;無意的漂移統一 |

> **⚠️ 若「招牌詞漏套」是**整族大缺失**(如你翻譯時完全沒想到 `Depart.`),回頭重讀 dossier §四 · 這是階段 2 ④ 翻譯做得不到位 · 不是自審能全救回**

#### § 4.5.5 大聲讀測試(Read-Aloud Test)

**逐 token 大聲讀**(或**心裡默念**),下列情況命中則修:

- 讀到**卡舌 · 停頓 · 覺得「這句不像中文」** → 修
- 讀到**要在腦中「再翻譯一次」才懂** → 修
- **同一句** 內連續 3 個以上短語都用「的」結尾 → 拆
- **語氣不對** · 讀起來太硬/太軟/太文/太俗,不符 dossier §四 → 修
- 讀完**還原不出原文核心意思** → 譯法錯 · 回檢

#### § 4.5.6 邊界規則(**避免過度自審**)

**❌ 不要**:

- 為順暢改動 canonical 詞(如把「紅色財團」改「紅色公司」)
- 為順暢改動招牌 icon(如刪 SNORT!/Nyark!/(hee-hee-hee))
- 為順暢加原文沒有的資訊(如原文冷淡卻自己加感嘆詞)
- 為順暢刪原文有的資訊(如省略修飾詞)
- 為順暢改變句子情緒/態度(如把辱罵改中性)
- 動用 shipped 的判斷邏輯(**仍在階段 2 · 禁讀 shipped**)

**✅ 只要**:

- 讓中文讀起來像**母語人寫的中文** · 不像**逐字譯的英文**
- 保留原文的**語氣 · 節奏 · 資訊密度**

#### § 4.5.7 self-fix log 格式

`uqm-work/_selfaudit_<race>_v2_readaloud.md`:

```markdown
# <Race> Read-Aloud Self-Audit (2026-XX-XX)

## 統計
- Total tokens: N
- 命中「直譯生硬」項目: M(P%)
- 分類:被動語態 X · 定語過長 Y · 冗餘代詞 Z · 語序台化 W · 標點英化 V · 招牌詞漏套 U · 其他 T
- 未動 tokens: N-M

## 修訂項(逐 token 列 · 只列有改的)

### #1 · TOKEN_NAME · § 4.5.1 被動語態

**原譯**:
> 訊息被送出了,並且回應被期待。

**自審修**:
> 訊息已送出,靜候回覆。

**類別**: § 4.5.1 被動語態直譯 + § 4.5.2 抽象名詞化

---

### #2 · ...
```

**這份 log 一併 commit**(audit trail)· 讓使用者可反查 AI 為何自動改了這些地方。

### 階段 3 · Diff 自動比對報告

程式化比對:
```
uqm-work/translations/<race>.zh-TW.v2.json   (剛翻的 · **已含階段 2.5 Read-Aloud 修訂**)
uqm-work/translations/<race>.zh-TW.json      (shipped)
```

**⚠️ 進入本階段前 · AI 應先回報階段 2.5 self-fix log 摘要**:

```
📖 已完成階段 2.5 順暢度自審(Read-Aloud Pass)
- 掃過 tokens: N
- 命中「直譯生硬」項目: M(P%)
- self-fix log: uqm-work/_selfaudit_<race>_v2_readaloud.md
- 未動 tokens: N-M
- v2.json 已含自審修訂 · 現在進行 diff

若你想 override 任何自審決定 · 請先看 log · 我再進 diff
```

**使用者可選擇**:直接進 diff(信任 self-fix) · 或先審 self-fix log · 或撤回某些 self-fix。

產出:`uqm-work/_reaudit_<race>_v2_diff.md`

格式:

```markdown
# <Race> Rebuild-Compare Diff Report (2026-XX-XX)

## 統計
- Total tokens: N
- 🟢 完全相同: N (X%)
- 🟡 微調 (等價): N (X%)
- 🟠 措辭改變: N (X%)
- 🔴 語意/voice 差異大: N (X%)
- ✨ v0.5.2 canonical 升級: N (X%)
- ⚙ 階段 2.5 Read-Aloud self-fix(僅資訊 · 不需你決策): N (X%)(**已直接應用於 v2**)

## 差異項(只列 🟡🟠🔴✨,不列 🟢/⚙)

### #1 · HELLO_1 · 🟠 措辭改變

**英文原文**:
> Ye stand before the Great Circle...

**Shipped v0.3**:
> 爾站在偉大之圈前……

**Rebuild v2**(**已通過階段 2.5 自審**):
> 汝正站於大圓陣之前……

**差異分析**:
- Shipped「爾」是文言化第二人稱(Alien_Speech §1.4 適用)
- Rebuild「汝」也是文言第二人稱,但更古雅
- Shipped「偉大之圈」直譯 Great Circle
- Rebuild「大圓陣」較意譯,呼應 dossier §四「靈修圓陣」概念

**推薦**: 🟡 A(shipped) — 「偉大之圈」較貼近直譯,玩家已熟悉,無明確錯誤

**替代**: 若要強化靈修 voice → B(Rebuild)

**你的選擇**: A / B / C(自訂)
```

差異類別:
- **🟢 完全相同** — 不列(浪費 token)
- **🟡 微調** — 標點/語序/等價替換,語意完全相同 → 預設 A(shipped)
- **🟠 措辭改變** — 選字/句式差異,語意等價但風格微異 → 依規則推薦
- **🔴 語意/voice 差異大** — 兩者對原文的解讀不同 → 必需使用者抉擇
- **✨ v0.5.2 canonical 升級** — Rebuild 用了新 canonical,shipped 是舊版 → 建議 B
- **⚙ 階段 2.5 Read-Aloud self-fix** — **rebuild 初稿 vs 自審修後**的差別(僅 v2 內部 · 已直接應用) · **不進 diff 報告主體 · 僅列於統計欄位** · 若使用者要求「顯示 self-fix 詳細」再從 `_selfaudit_<race>_v2_readaloud.md` 抽出

### 階段 4 · 使用者逐項決策 → 應用 → 部署

使用者回覆格式(建議):
```
#1=A  #2=B  #3=C(細節: 前半 shipped + 後半 rebuild)  #4=A  ...
```

或批次快答:
```
🟡 全 A · 🟠 全依推薦 · 🔴 逐項挑
✨ 全 B
```

**應用步驟**(依決策)產出最終 `<race>.zh-TW.json`(覆蓋 shipped):

1. Merge:依決策合併 shipped + rebuild
2. Purity: `python _check_zh_purity.py --strict --race <race>`
3. Line-count check
4. Lua template check
5. Backup shipped: `Copy-Item translations/<race>.zh-TW.json translations/<race>.zh-TW.pre-rebuild.bak`
6. Overwrite: 寫入 merged 版本
7. Build + package: `.\package_zh-TW.ps1`
8. 遞交使用者實機驗證

---

## 五、產出檔案清單

| 檔案 | 用途 | commit? |
|---|---|---|
| `uqm-work/translations/<race>.zh-TW.v2.json` | Clean-room 重譯結果(**已含階段 2.5 Read-Aloud 自審修訂**) | ❌ 不 commit(過渡產物) |
| `uqm-work/translations/<race>.zh-TW.v2.partial-N.json` | 階段 2 分批 partial(**同時為 Read-Aloud 前的原始 clean-room 譯稿快照**) | ❌ 不 commit(過渡產物 · 若需 rollback self-fix 用) |
| `uqm-work/_selfaudit_<race>_v2_readaloud.md` | **階段 2.5 self-fix log**(逐 token 列 AI 自審修過的地方) | ✅ commit(audit trail) |
| `uqm-work/_reaudit_<race>_v2_diff.md` | Diff 報告 + 決策記錄 | ✅ commit(audit trail) |
| `uqm-work/translations/<race>.zh-TW.pre-rebuild.bak` | shipped 備份 | ❌ 不 commit(rollback 用) |
| `uqm-work/translations/<race>.zh-TW.json` | 最終合併版(覆蓋 shipped) | ✅ commit |

**Commit 訊息模板**:
```
v0.7 <race> Rebuild-Compare: N tokens reaudited (X 🟠 + Y 🔴 + Z ✨ diffs applied; M ⚙ self-fix)

Rebuild-Compare workflow per StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md
- Read <N> rules files
- Clean-room re-translated <M> tokens (no shipped peeking)
- Stage 2.5 Read-Aloud self-audit: M/N tokens auto-fixed (self-fix log in _selfaudit_<race>_v2_readaloud.md)
- Diff report saved to uqm-work/_reaudit_<race>_v2_diff.md
- Applied user decisions: A×X / B×Y / C×Z
- 3-gate verify PASS (purity / line-count / Lua template)

Key changes:
- <token1>: <old> → <new> (reason)
- <token2>: ...
```

---

## 六、失敗恢復

### 情境 A · 階段 2 chat 過長觸發 "Invalid string length"

1. 保留 `<race>.zh-TW.v2.partial.json`(階段 2 checkpoint)
2. 開新 chat,貼:
   ```
   [本檔全文]

   ──────────────────────

   【接手任務】
   對 <race> 族繼續 Rebuild-Compare 流程,從 partial checkpoint 恢復。
   已完成 tokens: [前 30 個 token 名清單]
   ```
3. 我會讀 partial 檔,不重複已翻的,接續從第 31 個 token 開始

### 情境 B · 階段 3 發現 rebuild 跟 shipped 太相似(>70% 相同)

- 懷疑階段 2 被 anchoring 污染
- **停止流程**,告知使用者
- 選項:
  - A. 廢棄 v2,回到單純 Reaudit_Dialogue 流程
  - B. 換另一位 AI(不同 model)重跑階段 2
  - C. 使用者接受此結果,續階段 3

### 情境 C · 階段 4 應用後 in-game 有問題

- 立即 rollback:`Copy-Item translations/<race>.zh-TW.pre-rebuild.bak translations/<race>.zh-TW.json -Force`
- 重跑 `.\package_zh-TW.ps1`
- 使用者截圖回報,個別 token 修

### 情境 D · 使用者不同意某些階段 2.5 self-fix 判斷

**症狀**:使用者看完 `_selfaudit_<race>_v2_readaloud.md` 覺得某些 self-fix「改壞了」(改動過度 / 誤刪招牌詞 / 破壞原文語氣)

**處理**:

- 使用者以 `#N=撤回` 或 `#N=用初稿` 格式指出要撤回的 token
- AI 從對應 `<race>.zh-TW.v2.partial-K.json` 抽出**該 token 的自審前版本**,寫回 `<race>.zh-TW.v2.json`
- 更新 `_selfaudit_<race>_v2_readaloud.md`:該項標 `⛔ 使用者撤回(<reason>)`
- 重跑 3-gate verify(purity / line-count / Lua template)
- 然後才進階段 3 diff

**預防**:若使用者已多次撤回同類型 self-fix,考慮下次執行時**加參數 `read-aloud: 保守`** 讓 AI 只修最明顯的直譯生硬 · 不動邊緣案例

---

## 七、Invocation 範例

### 標準用法(推薦)

新 chat,第一則訊息:
```
[本檔全文]

──────────────────────

【本次任務】
對 pkunk 族執行 Rebuild-Compare 流程。
```

### 帶參數用法

```
[本檔全文]

──────────────────────

【本次任務】
對 spathi 族執行 Rebuild-Compare 流程。
批次: 分批
Q&A 詳細度: 中
dossier 缺項: fetch Ultronomicon
```

### 接手用法(chat 爆掉後)

```
[本檔全文]

──────────────────────

【接手任務】
對 syreen 族繼續 Rebuild-Compare 流程,從 partial checkpoint 恢復。
已完成 tokens: HELLO_1, HELLO_2, ..., ABOUT_ORIGIN_5
```

---

## 八、預期成果

執行完一族 Rebuild-Compare 後,你應該:

- ✅ 得到 `<race>.zh-TW.pre-rebuild.bak`(安全 rollback)
- ✅ 得到 `_selfaudit_<race>_v2_readaloud.md`(**階段 2.5 self-fix 完整記錄** · **避免直譯生硬進 diff**)
- ✅ 得到 `_reaudit_<race>_v2_diff.md`(**未來想理解為何這樣譯**的完整 audit trail)
- ✅ shipped `<race>.zh-TW.json` 被優化過的版本覆蓋
- ✅ purity/line-count/Lua template 三 gate 全 PASS
- ✅ 遊戲內顯示與新 canonical 對齊,voice 更貼合 dossier §四
- ✅ 玩家讀起來更順口(**階段 2.5 讀順度自審 + 階段 3 使用者最終決策雙保險**)

如果**沒感受到明顯改進**(所有 diff 都 🟡 微調 + 你全選 A · self-fix 命中率 <5%),代表 shipped 品質已高,不需 rebuild,以後**跳過該族**即可。
