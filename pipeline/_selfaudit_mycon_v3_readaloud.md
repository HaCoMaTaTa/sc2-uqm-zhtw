# Mycon Read-Aloud Self-Audit (2026-08-17)

**檔案**：`translations/mycon.zh-TW.v3.json`
**執行**：階段 2.5 Read-Aloud Pass (Rebuild_And_Compare workflow § 4.5)
**目的**：clean-room 翻譯後、diff 前，抓「直譯生硬」問題於自審修正，避免佔用使用者 diff 決策

## 統計

- Total tokens: 109
- 命中「直譯生硬」項目: 3 (2.8%)
- 分類：抽象名詞化 1 · 標點漂移 1 · 節奏標點 1
- 未動 tokens: 106

## 修訂項

### #1 · TELL_US_ABOUT_WORLD · § 4.5.1 抽象名詞化

**原譯 (clean-room 初稿)**：
> 我們希望知道更多，以進行適宜性評估。

**自審修**：
> 我們希望知道更多，以評估其適宜性。

**類別**：§ 4.5.1 英文抽象名詞化 → 中文動詞化
**理由**：`for our suitability assessment` (英文 nominalization) → 中文動詞前置更順。「進行適宜性評估」讀來抽象，「評估其適宜性」清爽直白。

---

### #2 · RAMBLE_5 · § 4.5.3 節奏標點

**原譯 (clean-room 初稿)**：
> 我於 57,283 年前，因總體故障而亡。

**自審修**：
> 我於 57,283 年前因總體故障而亡。

**類別**：§ 4.5.3 標點漂移 · 冗餘逗號拆句
**理由**：「我於 X 年前因 Y 而亡」是完整介詞短語，中間插逗號打斷節奏。原文 `I died of general misfunction 57,283 years ago` 無停頓，中譯亦不需。**深時獨白 icon 更精煉**。

---

### #3 · HELLO_HOMEWORLD_1 · § 4.5.3 標點用法

**原譯 (clean-room 初稿)**：
> 聖源（Juffo-Wup）即一切……無所不在，散布著、將異類轉化為聖源。

**自審修**：
> 聖源（Juffo-Wup）即一切……無所不在，散布著，將異類轉化為聖源。

**類別**：§ 4.5.3 頓號「、」誤作停頓逗號
**理由**：`spreading and changing the Non into Juffo-Wup` = 兩個連續動作，用停頓逗號「，」而非列舉頓號「、」。中文標點規範：「、」用於名詞列舉（A、B、C），「，」用於子句停頓。

---

## 未改項（讀來 OK · 不列為 self-fix）

- 系統廣播 icon `『……』` 8 處統一格式 OK
- 深時獨白 icon (Dugee/Shloosh/Gussh) 3 處保留原文名 + 中譯音譯 OK
- 祖父輩獨白節奏 (RAMBLE_3 5 次 / RAMBLE_11 3 次) 按原文 count OK
- `**` markdown 全清 · 3 處 (NEVER_LET_LAND / UNFORSEEN_DELAYS / WE_GO_TO_IMPLANT) 改短句斷句 icon OK
- 玩家 response 40 tokens 保留 shipped 微調 (Q12=A) 未動

## 邊界

**未自審修改**：
- Mycon voice 冷漠短句 icon 保留 (RAMBLE_30「黑暗即虛空 / 聖源即光」等極簡宣告句)
- 「盈滿於」(RAMBLE_3) 保留 · dossier §四 example 3 直接使用此表達為 canonical icon
- 「一具幼體的胎宮」(RAMBLE_6) 量詞「一具」保留 · 中文詩性用法允許（如「一具軀殼」）
- 「而亡」(RAMBLE_5) 保留 · 深時獨白訃告感 icon · 不改為口語「而死去」

## 結論

Read-Aloud Pass 命中率 2.8% (低 · 表示 clean-room 翻譯已相對通順)。3 個 fix 均為表面標點/措辭級別，不涉及 voice 或 canonical。
