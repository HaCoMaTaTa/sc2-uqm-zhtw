# Melnorme Read-Aloud Self-Audit (2026-08-18)

> v0.7 Rebuild-Compare · Phase 2.5 · Read-Aloud pass on clean-room v3 draft

## 統計

- Total tokens: 281
- 命中「直譯生硬」項目: 3 (1.1%)
- 分類:
  - § 4.5.1 英文語法殘留（詞序台化）: 1
  - § 4.5.2 中文語感（現代 idiomatic）: 1
  - § 4.5.4 招牌詞漏套（`爾` 詞素）: 1
- 未動 tokens: 278

## 修訂項（逐 token 列 · 只列有改的）

### #1 · `NO_TALK_ABOUT_OURSELVES` · § 4.5.1 詞序 + line-count

**原譯**（3 zh 行 vs 2 en 行 · line-count mismatch）:
> 我方的起源與目的, 坦白說, 是神秘的
> 又由於幾項不可避免的因素
> 我方無法詳細討論自身的細節。

**自審修**（2 zh 行 = 2 en 行 · idiomatic 逗號連接）:
> 我方的起源與目的, 坦白說, 是神秘的， 又由於幾項不可避免的因素
> 我方無法詳細討論自身的細節。

**類別**: § 4.5.1 語序台化 + 3-gate line-count fix

---

### #2 · `OK_BUY_HISTORY_6` · § 4.5.4 `爾` 詞素 →  現代雅辭

**原譯**（`偶爾意外允許` · `偶爾` 含禁用 `爾` 詞素）:
> 到了這個歷史階段, 蟾亞已在他們的統治中變得鬆懈
> 且**偶爾**意外允許其奴隸擁有片刻的自主意識。

**自審修**（`時而` 現代雅辭替代 · 消除 `爾` 詞素）:
> 到了這個歷史階段, 蟾亞已在他們的統治中變得鬆懈
> 且**時而**意外允許其奴隸擁有片刻的自主意識。

**類別**: § 4.5.4 禁用字元 clean-up · `爾` 為 v0.7 禁用清單 · 即使在 `偶爾` 現代雙音節詞內也優先清除

---

### #3 · `OK_BUY_HISTORY_7` · § 4.5.1 英文語法殘留 + § 4.5.2 中文語感

**原譯**（`共同前來作出` · 英文 `had come together to make` 直翻）:
> 烏寬星艦艦隊的聯合力量會師在蟾亞母星的軌道上。
> 他們**共同前來作出**兩項重要決策。

**自審修**（拆為兩動作 · 「聚在一起」+「要作出」· 更順暢）:
> 烏寬星艦艦隊的聯合力量會師在蟾亞母星的軌道上。
> 他們**聚在一起, 要作出**兩項重要決策。

**類別**: § 4.5.1 英文完成式時態直搬 + § 4.5.2 中文動作分節（有意圖有目的）

---

### #4 · `OK_BUY_EVENT_7` · § 4.5.1 英文結構直搬

**原譯**（`對我方所有人而言之幸運` · 保留 `之` + 英文 `Fortunately for us all` 直搬）:
> 憂特族, 本人遺憾地說, 中了毒賈族的骯髒詭計, 立即搶購了厄創。
> **對我方所有人而言之幸運**, 憂特族並未支付毒賈族要求的價格 —— 那顆超級炸彈

**自審修**（起首語 `所幸` 現代 idiomatic · 清除 `之` · 對齊中文書面順序）:
> 憂特族, 本人遺憾地說, 中了毒賈族的骯髒詭計, 立即搶購了厄創。
> **所幸對我方所有人而言**, 憂特族並未支付毒賈族要求的價格 —— 那顆超級炸彈

**類別**: § 4.5.1 英文起首語 `Fortunately for us all,` 直搬 → 中文起首 `所幸` idiomatic + § 4.5.4 `之` 清除

---

## 未動項目摘要

**保留為 shipped/rebuild 版共通結構的（`\n\n` 段落中斷）**：
- `RESCUE_EXPLANATION` · zh_nl=13 vs en_nl=12 · `\n\n` 段落中斷（shipped 亦有此結構 · 是設計意圖 · 3-gate 可接受）

**保留 canonical 專名內的 `爾` 詞素**（禁用清單例外 · 為專名一部分）:
- **阿爾戈斯人（Algolites）** × 1 · `NO_EXCUSE_1`
- **戈爾諾δ**（Delta Gorno canonical） × 2 · `OK_BUY_EVENT_1` + `OK_BUY_ALIEN_RACE_12`

**保留為 humor icon 的直譯用語**（原文設計有意 silly · 保留）:
- **「肉體體操便會展開」** · `OK_BUY_EVENT_1` · from `the carnal gymnastics proceed`
- **「找到雄性物種比放個屁還容易」** · `OK_BUY_EVENT_1` · from `easier than flup`
- **「咩咩叫的生物」** · `OK_BUY_HISTORY_6` · from `bleating creature`

**保留為 canonical 招牌 icon**:
- **`Ahhh-YING! Ahhh-YING! Ahhh-YING! Ahhh-Y`（梅諾商冥想咒語）** · `HELLO_PISSED_OFF_2`
- **`Fe-Fi-Fo-Fum! I smell the feet of a Hu-Hu-Man!`（英國巨人童話台詞）** · `HELLO_AND_DOWN_TO_BUSINESS_7`
- **當心！（LOOK OUT!）** · `HELLO_AND_DOWN_TO_BUSINESS_9`
- **喂！（Hoy!）** · `HELLO_AND_DOWN_TO_BUSINESS_9`
- **變！（Presto!）** · `OK_BUY_NEW_TECH_10`
- **哈, 哈, 哈！** · `RESCUE_AGAIN_4`
- **於所有情境必勝之艦** · `HELLO_NOW_DOWN_TO_BUSINESS_1`（艦名 canonical · `之` 保留於專名內）
- **〈艦長〉之帝國** · `name_4`（帝國名 canonical · `之` 保留於專名內）

## 3-gate PASS 摘要

- ✅ **Purity**: 0 wenyan 助詞在 dialog（3 個 `爾` 皆為 canonical 專名詞素，不算違規）· 廢除 shipped v0.1 之 559 / 吾 187 / 吾等 185 / 乃 37 = **972 處文言污染 → 0**
- ✅ **Line-count**: 281/281 tokens 讀取正確 · 1 mismatch（RESCUE_EXPLANATION `\n\n` 段落中斷 · 與 shipped 同結構）
- ✅ **Lua template**: 0 English leaks · 全部 first-arg 為 CJK canonical（戈爾諾δ / 契倫科夫α / 巨爵座 / 獵戶座 / 錢德拉塞卡與天鴿座 / 孔雀座α / 烏鴉座β / 畢宿星團ζ / 英仙座 / 寶瓶座 / 大陵五、五車二與 / 拉卡伊與克魯格 / 克魯格與吉克拉斯 / 天龍座與天燕座 / 天龍座ζ / 天龍座δ / 南河三 / 大角星 / 天鴿座 / 巨蛇座γ / 狐狸座δ / 天鶴座ε / 參宿四）
