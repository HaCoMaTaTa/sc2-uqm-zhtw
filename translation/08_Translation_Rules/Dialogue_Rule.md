# Dialogue Rule 對話翻譯技術規則

> **本檔功能**：SC2 對話翻譯的**技術規則**——token 保留、Lua template、換行、字寬、標點等格式要求。
> **權威來源**：使用者 v0.4 提詞 §7-8 + shipped v0.3 各族 JSON 實例。

---

## 一、Token 保留（絕對規則）

### 1.1 什麼是 Token

Token 是遊戲對話系統的**識別碼**，格式為 `#(TOKEN_NAME)`。例：

```
#(TALANA_1)
Welcome, Captain, to the Vault of the Syreen.
```

翻譯後：
```
#(TALANA_1)
歡迎您，艦長，蒞臨塞蓮的庇護所。
```

### 1.2 Token 保留規則

- **`#(TOKEN_NAME)` 必須原樣保留**，包括井號、括號、底線、大小寫
- **不要翻譯 token 名**（TALANA_1 不能翻成「泰蘭娜_1」）
- **不要**在 token 名旁邊加空格
- **token 之間的空行數要維持**原文一致

### 1.3 JSON 格式（shipped v0.3 已採用）

現行 shipped 使用 JSON 格式，token 名為 key：

```json
{
  "TALANA_1": "歡迎您，艦長，蒞臨塞蓮的庇護所。",
  "TALANA_2": "..."
}
```

**規則**：
- key（`TALANA_1`）**不翻譯**
- value（`"..."`）為譯文
- **`_notes`** key 為譯註（不會進遊戲）—— 詳見 §八

---

## 二、Lua Template 保留

### 2.1 常見 Lua template

`<% ... %>` 是 Lua 動態文字，運行時會替換為玩家設定或遊戲狀態。**必須保留**。

| 常見 template | 含意 |
|---|---|
| `<% state.sis.getCaptainName() %>` | 玩家艦長名字 |
| `<% state.sis.getShipName() %>` | 玩家旗艦名字 |
| `<% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>` | 玩家選定的聯盟別名 |
| `<% comm.getStarName("布拉赫β", "sun device") %>` | 動態星系名（帶回退譯名） |
| `<% comm.getConstellation("天龍座", "thraddash") %>` | 動態星座名 |

### 2.2 保留與空格

**Lua template 前後應加空格**（讓中文與英文區分）：

- ✅ 正確：`我是 <% state.sis.getCaptainName() %> 艦長`
- ❌ 錯誤：`我是<% state.sis.getCaptainName() %>艦長`（無空格）

### 2.3 動態譯名（CJK 化 star name）

**背景**：v0.3 已將部分 `getStarName` 的 fallback 譯名 CJK 化（如 `Zeta Persei` 的 fallback 從 `Zeta Persei` 改為 `英仙座ζ`）。

- 遇到 `<% comm.getStarName("...","...") %>` 若 fallback 為英文 → **改為中文譯名**（依 [Place_Names.md](../07_Glossary/Place_Names.md)）
- 例：`<% comm.getStarName("Zeta Persei", "..." ) %>` → `<% comm.getStarName("英仙座ζ", "..." ) %>`

---

## 三、換行（`\n`）處理

### 3.1 原文換行的意義

原文的 `\n` 是**節奏標記**——通常是句子停頓、換氣、下一句轉折的邊界。**保留**這些換行。

### 3.2 中文換行策略

- **原文一段一行**：中文譯文**一段一行**
- **原文短句多換行**（表達急促、興奮）：中文譯文**也短句多換行**
- **原文一句話 100 字**：中文不要拆成 20 行

### 3.3 例（Yehat 蘇格蘭騎士）

```
Ho, ye brave captain of Earth!
The winds of destiny bring us together!
Speak, and my ears shall drink thy words as parched soil drinks rain.
```

譯文：
```
啊哈，勇敢的地球艦長！
命運之風將吾等聚首於此！
講吧，吾之耳朵將如乾涸大地吸吮雨露般吸吮汝之話語。
```

**注意**：三行對三行、每行內部**不強行加換行**（會破壞戲劇節奏）。

---

## 四、字寬與換行硬約束

### 4.1 遊戲字寬

**shipped v0.3 patch 006 後**：`comm.c getLineWithinWidth` 把 CJK 視為 word boundary → **自動換行**。譯者**不再需要**手動插空格模擬換行。

### 4.2 建議行長

- **每行 ≤ 30 個中文字**（避免對白框爆版）
- **長句用 `\n`** 主動斷行到自然節奏處
- **避免**：一整段沒有 `\n`（讀者看不完）

### 4.3 字型限制

各族有專屬字型（`fonts/*.fon`），字寬像素固定。譯文若過長可能**擠壓**——建議：

- 保守：每行 15-20 個中文字
- 對白窄的族（如 Chmmr = 10px 字型）：更短

**詳細字型／字寬表**：見 `Reference_Material/` 未來的字型對照表（Phase 12）。

---

## 五、標點符號

### 5.1 全形 vs 半形

**規則**：中文文本用**全形**標點；混入的英文／變數用**半形**。

| 中文（全形）| 英文（半形）|
|---|---|
| 「」（引號）| " " |
| ，（逗號）| , |
| 。（句號）| . |
| ？（問號）| ? |
| ！（驚嘆號）| ! |
| ：（冒號）| : |
| ；（分號）| ; |
| ——（破折號）| -- |
| ……（刪節號）| ... |

#### 5.1.1 `——`（em dash）使用規範（v0.8 補訂，2026-08-18）

> **教訓**：v3 Rebuild-Compare 期（yehat/kohrah/talkingpet/yehatrebels 等）AI 譯者在清除文言助詞後，習慣以 `——` 承擔「同位語連接／語氣停頓／插入語」的功能，導致遊戲內大量出現無語意用途的破折號，玩家反映突兀。實證：中譯 `——` 用量 434 對 vs 英文原文 `--` 用量 73 → **中譯自加 +495 %**。

**核心規則**：
- ✅ **僅在英文原文對應位置有 `--` 時**，中譯才用 `——` 對應（1:1 對照）
- ✅ **允許保留的例外**（rhetorical break，非同位語）：
  - **強調中斷式重複**（原文有連續強調）：`我族——並未——戰敗`（`we are NOT defeated`）
  - **短促轉折宣言**：`但——且慢!`（`But—wait!`）/ `革命——已然掀起!`（`Revolution—has begun!`）
  - **hesitation 結巴**：`我族——是!……我族是!……我族是……`
  - **鳥鳴/情緒 icon 包夾**：`(嗚咽——吞嚥聲!)` 這類 alien icon 內部節奏
- ❌ **不主動加入**於下列情境（皆屬濫用，應改用「，」或全形空格）：
  - 同位語連接：`凱爾茲皮里普——女皇的高懸王座` → `凱爾茲皮里普，女皇的高懸王座`
  - 語氣停頓：`本騎士深知——今日此事...` → `本騎士深知，今日此事...`
  - 插入語包夾：`我族——女皇忠誠的僕從——絕不會...` → `我族，女皇忠誠的僕從，絕不會...`
  - 呼告後停頓：`人類——你可算是死定了` → `人類，你可算是死定了`
  - 條件行末：`若此屬實——(換行)` → 直接換行或 `，(換行)`

**技術補充**：`——` 佔 2 CJK 寬度 ≈ 30 px，會提高各族 `AlienTextWidth` 邊界風險；若鄰近 SplitSubPages `\n` 邊界，可能觸發 fullwidth-punct ispunct/isspace 例外。少用即減少此類風險。

#### 5.1.2 `**...**`（markdown 粗體）**禁用**規範（v0.8 補訂，2026-08-18）

> **關鍵事實**：SC2 引擎**不解析 markdown**。`**word**` 會被畫成**字面兩個星號**，玩家看到的是 `**神智混亂**` 而非高亮強調。

**引擎證據**（[UQM-MegaMod/src/uqm/comm.c:338-344](../../../UQM-MegaMod/src/uqm/comm.c)）：
```c
if (CommData.AlienConv == ORZ_CONVERSATION && optOrzCompFont)
    font_DrawTracedTextAlt (pText, ..., ComputerFont, '*');  // 只有 Orz
else
    font_DrawTracedText (pText, ...);  // 其他所有種族:無 * 特殊處理
```

**規則**：
- ❌ **絕對禁止**在非-Orz 種族翻譯中使用 `**...**` markdown 粗體
- ✅ **Orz 例外**：Orz 對話中的**單 `*text*`**（成對非雙星）觸發引擎 font-swap，讓被夾詞用 computer.fon 顯示，達成視覺高亮。這是**原作標誌性寫法**（`*happy campers*`, `*juice*`, `*many bubbles*`），**必須保留**。
- ✅ **Arilou 例外**：dossier §Alien_Speech_Rule §1 已定義 arilou 用 `*text*` 為念力聲響 icon（少數 tokens），依 dossier 保留。

**強調的替代方式**（原文用 CAPS / hyphen 節拍時）：

| 原文技巧 | 中文替代（推薦優先序） |
|---|---|
| **CAPS 詞強調** `**EVER**`, `**NEVER**` | ① 副詞升級：從未→**絕未** / 甚→**極** ② 疊字：**絕對絕對** ③ 感嘆密度：`絕未！` |
| **CAPS 句宣言** `IS OVER!`, `HAS BEGUN!` | ① 感嘆堆疊 `已然告終！！！` ② 頓號分格 `已、然、告、終！` |
| **hyphen 節拍字** `WE - WERE - NOT - DEFEATED` | ① **句號節拍** `我族。並未。戰敗。`（推薦，最貼合原文戲劇性）② 中間點 `我族·並未·戰敗` ③ 頓號 `我族、並未、戰敗` |
| **逗號重複強調** `dear, very dear` | 直接對譯 `慘重，極其慘重` |

**Shipped pre-existing 濫用清單**（v0.8 需清理）：
- yehat 70 對、yehatrebels 70 對、umgah 76 對、safeones 38 對 = 共 **254 對 `**` = 508 個字面星號** 目前顯示在遊戲中

### 5.2 常見錯誤

| ✗ 錯誤 | ○ 正確 |
|---|---|
| 我是艦長,我方 | 我是艦長，我方 |
| 你是誰? | 你是誰？ |
| 「引號" | 「引號」 |
| ... 停頓 | …… 停頓 |
| -- 說明 | ── 說明（or 「——」）|

### 5.3 例外：保留原文標點

- **感嘆詞 保留原文格式**：`Kyaiee!` `Aieee!` `SNORT!` 等——含**原英文驚嘆號**
- **Lua template 保留原格式**：`<% ... %>` 不改標點

---

## 六、換行 vs 空格

### 6.1 段落內用空格（非 `\n`）

同一句話內部分段，用**全形空格**（見 [Style_Guide.md](Style_Guide.md) §五）：

```
別打了—— 我不是烏寬！ 我是你的盟友！
```

（`——` 前後用**全形空格**，讀起來自然）

### 6.2 段落間用 `\n`

**多句對白**用 `\n` 分隔：

```
別打了—— 我不是烏寬！\n我是你的盟友！\n請住手！
```

### 6.3 Special：`hostile` 系列 token 常一句話多換行

`hostile` 系列 tokens 常用**多換行**表達**衝擊力**：

```
本人戰士武士刀在星海中遠行多年終於返鄉
卻親眼看到你把俺兄弟轟成原子塵！
受死吧！
```

譯文換行對應原文。

---

## 七、玩家 response 專屬規則

### 7.1 情境切換自稱

見 [Style_Guide.md](Style_Guide.md) §二。

### 7.2 短促、有力

玩家 response **不宜太長**——玩家看到選單要快速選：

- **建議**：**每選項 ≤ 20 中文字**
- **絕對上限**：40 字
- **超過**：拆成多個 `\n` 或改寫

### 7.3 例

```json
{
  "i_am_captain": "我是 <% state.sis.getCaptainName() %> 艦長，隸屬 <% comm.getPhrase(\"name_...\") %> 旗艦 <% state.sis.getShipName() %>。立刻住手！"
}
```

（雖然帶 template 顯得長，但實際玩家看到就是「我是 ○○○ 艦長，隸屬 ○○聯盟旗艦 ○○號。立刻住手！」——短促）

---

## 八、JSON `_notes` 譯註格式

### 8.1 用途

`_notes` 是**譯者專用**的譯註，**不會顯示在遊戲中**。用來：

- 記錄版本沿革（v0.1 → v0.2 → v0.3 變更）
- 記錄重要決策（e.g., Q1=A 情境切換人稱）
- 記錄鎖定詞彙（供下次翻譯者查閱）
- 記錄玩家 response 的手法

### 8.2 shipped v0.3 標準格式（範例來自 shofixti.zh-TW.json）

```json
{
  "_notes": [
    "v0.2 — 依 SC2_繁中化_AI翻譯提詞.md + SC2-詞彙對照表-v0.3.md 翻譯,並套用玩家 response 台式順口通則。",
    "91 tokens / Shofixti (蘇菲斯特族) 主線對話。字型 shofixti.fon 16px, AlienTextWidth=200px FULL, CJK 完全清晰。",
    "===== v0.2 重大變更 =====",
    "1) 排版:patch 006 已讓 comm.c getLineWithinWidth 把 CJK 視為 word boundary,故 CJK 之間不再需要 ASCII 空格 wrap。",
    "2) 田中人稱:所有『本人/我』→『俺』 (熱血 anime 武士戰士標配)。",
    "===== 玩家 response 台式順口通則(每族沿用)=====",
    "  A. 情境切換人稱: 正式=『我方』/對嗆=『老子』/平和=『我』",
    "  B. 遇英文生造俚語(roof-rabbit): 先找台灣情境對應詞",
    "===== v0.3 鎖定詞彙 =====",
    "  Ur-Quan = 烏寬族/烏寬 | Shofixti = 蘇菲斯特族 → v0.4 修烈士族",
    "  Kyaiee!/Hyai! = 保留原文 ★"
  ]
}
```

### 8.3 v0.4 應加的 `_notes` 內容

**每族 JSON 首次修改後應更新**：

```
===== v0.4 使用者重設種族名（Phase 8.5b）=====
- Shofixti = 修烈士族（原「蘇菲斯特族」）
- Yehat = 翼哈特族（原「葉哈特族」）
- Umgah = 陰嘎族（原「阿姆嘎族」）
- Thraddash = 撻伐族（原「撒達許族」）
- Dnyarri = 蟾亞族（原「尼亞里族」）
- Supox = 蘇菩族（原「蘇波族」）
- Druuge = 毒賈族（原「德魯族」）
- Melnorme = 梅諾商（原「梅爾諾」）
權威來源：../StarControl2_TW_Localization/07_Glossary/Master_Glossary.md
```

---

## 九、翻譯前檢查清單

翻譯**每個 JSON 檔前**，先做 3 分鐘準備：

- [ ] 讀該族 `../02_Races/[Race].md`（人格、自稱、口頭禪）
- [ ] 讀 `../07_Glossary/Master_Glossary.md` 該族 row（鎖定譯名）
- [ ] 確認該族**已鎖定的感嘆詞**（Kyaiee! 保留、SNORT! 保留 等）
- [ ] 確認遇到跨族名詞（其他族提及）用鎖定譯名
- [ ] 確認**玩家 response** 適用台式順口通則

---

## 十、翻譯後自查（v0.4 §8）

- [ ] 所有 `#(TOKEN)` 標記是否原樣保留？
- [ ] 這段對話讀起來，是否還是同一個角色（語氣、用詞習慣一致）？
- [ ] 有沒有把原文的言外之意、諷刺、雙關語遺漏或翻死？
- [ ] 有沒有不小心加入台灣當代網路用語，導致 1990 年代科幻感出戲？
- [ ] 中文句子長度是否大致對應原文（避免太長導致遊戲文字方塊爆版）？
- [ ] 專有名詞是否都對照 `07_Glossary/Master_Glossary.md`？
- [ ] **玩家 response 是否套用台式順口通則？**
- [ ] **有無英文生造俚語硬翻**（roof-rabbit 等）**未轉台灣情境對應？**
- [ ] **有無醫學／生物學／書面語混入口語罵詞**（陽痿、雌性個體、淌鼻涕）？
- [ ] **空格切分是否按語意單位**（名詞短語不能被空格拆兩半）？
- [ ] **有無簡體字混入？**
- [ ] `_notes` 是否更新 v0.4 使用者重設種族名部分？

---

## 十一、詞彙直譯陷阱 (Direct Translation Vocabulary Traps)

以下是 EN → CN **字典直譯後語感錯位**的常見陷阱。翻譯首譯與 audit 時都應對照本表核查。

| EN Word/Phrase | ✗ Bad (直譯) | ○ Good CN | Reason |
|---|---|---|---|
| `quality` (人的特徵) | 品質 | **特質** / 品格 / 天性 | CN「品質」= 產品優劣；人的 quality 是特質 |
| `personal endeavors` (physical intimacy 語境) | 私人的行動 | **貼身的作為** / 近距離的接觸 | `personal` 在 UFO 綁架語境指 physical intimacy |
| `represent + NP` | 代表 + NP | **構成** + NP / **成為** + NP | 「代表 + 抽象 NP」偏官式報告體 |
| `unfortunate complication` | 不幸的複雜情況 | **不幸的棘手因素** / 變數 | complication ≠ complicated situation |
| `broad thinker` | 廣泛的思想家 | **眼界較廣的思想家** | 「廣泛」不能修飾「思想家」 |
| `translation into HyperSpace` | 進入超空間的位移 | **躍入超空間的軌跡** | `translation` 為天文躍遷術語，非「位移」 |
| `well-being` | 福祉 | **安好** / 平安 | 溫柔口語感更適合對話 |
| `A most X species` | 一個最 X 的 Y | **最為 X 的 Y** | 「最為」比單「最」更自然 |
| `outside slave shield` (作定語) | 從奴役護盾之外 | **護盾之外的（人）** | 副詞句掛中間會誤讀為「從...來」 |
| `Farewell child.` (溫柔道別) | 永別了，孩子 | **再見了，孩子** / 再會 | Farewell 不含「永別」意 |

**Sources**:
- `品質→特質`、`私人的行動→近距離的接觸`、`代表→構成`、`複雜情況→棘手因素`、`廣泛的思想家→眼界較廣`、`從...之外→...之外的`: arilou v3.1 audit (2026-08-26)
- `進入→躍入超空間`: urquan v0.9 audit (2026-08-26, commit 90cff61, CAUGHT_YA)

---

## 十二、標點排版陷阱 (Punctuation & Layout Traps)

### §12.1 逗號位置

CN 標點慣例**不允許**逗號放段首。EN line-break 直接對應 CN line-break 時常會造成逗號掛頭尾錯位。

- ❌ 錯位（逗號在行首）：
  ```
  也曾為我們較近距離的接觸寫下書籍
  ，當我們允許你們回想起我們對你們的檢查時。
  ```
- ○ 正確（逗號在前行尾）：
  ```
  也曾為我們較近距離的接觸寫下書籍，
  當我們允許你們回想起我們對你們的檢查時。
  ```

**Source**: arilou v3.1 audit (GENERAL_INFO_2)

### §12.2 副詞句掛尾陷阱

當 EN `Subject, [ADV_PHRASE], VERB` 結構把副詞短語插入主語與動詞之間，直譯到 CN 常造成「主語從什麼地方來」的誤讀。改用**定語結構**更清晰。

- ❌ 直譯（副詞句打斷主謂）：
  「我很高興看到你**，從奴役護盾之外，**仍然活著。」
  （讀者困惑：你**從**奴役護盾之外**來**的？）
- ○ 定語化：
  「我很高興看到你這位**護盾之外的**倖存者。」
  （明確：你＝ shield-outside survivor）

**Source**: arilou v3.1 audit (HAPPY_RESPONSE)

### §12.3 量詞查表

| 名詞 | ○ Canonical 量詞 | ❌ 錯誤 | Source |
|---|---|---|---|
| 漩渦 | 一**片** / 一**個** | 一道漩渦 | arilou v3.1 (FRDLY_HOMEWORLD_HELLO_1) |
| 特質 | 一**項** / 一**種** | 一件特質 | arilou v3.1 (GENERAL_INFO_1) |
| 傳送門 | 一**扇** | — | Master_Glossary canonical |
| 護盾 | 一**道** / 一**面** | — | Master_Glossary canonical |
| 艦隊 | 一**支** | — | urquan/starbase canonical |
| 星系／星域 | 一**片** | — | Master_Glossary canonical |

### §12.4 「代表 + NP」堆疊陷阱

EN 常見 `X may represent an unfortunate Y` 結構，直譯「X 代表一個不幸的 Y」在 CN 中讀起來像官方報告書。改用**構成**／**成為**更自然。

- ❌ 「你或許**代表一個不幸的複雜情況**。」
- ○ 「你或許**構成了一個不幸的棘手因素**。」
- ○ 「你或許**已然成為**一個不幸的變數。」

**Source**: arilou v3.1 audit (GENERAL_INFO_4)

---

## 十三、從句連詞規則 (Connective Clause Rules)

EN 連詞連接兩子句時，CN 譯文**必須加逗號**斷句，否則兩子句黏連會讓讀者需要**重讀一次**才能理解。此規則為**通用中文語法**，適用所有正常語域種族。

| EN Pattern | CN Rule | 說明 |
|---|---|---|
| `if X, then Y` | 如果 X**，**那 Y | 條件從句必加逗號 |
| `X because Y` | X**，**因為 Y | 因果從句必加逗號 |
| `X so Y` | X**，**所以 Y | 順接從句必加逗號 |
| `X, and Y` (兩獨立子句) | X**，**Y | 對等連接必加逗號 |
| `X but Y` | X**，**但 Y | 轉折連接必加逗號 |
| `so X that Y` | X**，**Y | 結果從句必加逗號 |
| `X, or else Y` | X**，**否則 Y | 選擇從句必加逗號 |

**⚠️ 例外**：特定破碎英文角色（見 `Alien_Speech_Rule.md` §6 對應條目）刻意保留部分連詞黏連作為設計效果，本規則**不適用**該類種族。一般種族（史怕族／烏寬族／塞蓮族／阿麗露／梅諾商等）**強制**適用。

**Sources**:
- 通用中文語法規則
- Case verify: arilou v3.1 audit / urquan v0.9 audit

---

## 十四、參考來源

- 使用者原提詞 §7-8
- shipped v0.3 各族 zh-TW.json 實例
- [Style_Guide.md](Style_Guide.md) §五（空格切分）
- [Naming_Rule.md](Naming_Rule.md)（未鎖定名詞處理）
- arilou v3.1 audit (2026-08-26) · urquan v0.9 audit (commit 90cff61) · starbase v0.7 audit (commit db9b7ab) · spathi v0.7 audit (commit 15d84db)
