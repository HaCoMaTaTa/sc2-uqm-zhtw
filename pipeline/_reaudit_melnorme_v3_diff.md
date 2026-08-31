# Melnorme Rebuild-Compare Diff Report (2026-08-18)

> v0.7 Rebuild-Compare · clean-room v3 vs shipped v0.1 (Round 3)

## 統計

- Total tokens: 281
- 🟢 完全相同: 89 (31.7%)
- 🟡 微調 (等價): 149 (53.0%)
- 🟠 措辭改變: 43 (15.3%)
- 🔴 語意/voice 差異大: 0 (0.0%)
- ✨ v0.7 canonical 升級: 0 (0.0%)
- ⚙ 階段 2.5 Read-Aloud self-fix: 4 (1.4%) · 已直接應用於 v3 · 詳見 `_selfaudit_melnorme_v3_readaloud.md`

## Voice diagnostics

**shipped v0.1 (2026-08-11 · Round 3) 文言污染統計**：

- 吾: 187 (dialog)
- 吾等: 185 (dialog)
- 乃: 37 (dialog)
- 之: 559 (dialog)
- **合計 ~972 處禁用文言助詞 → v3 全清 0**（僅保留 3 個 canonical 專名 `爾` 詞素：阿爾戈斯人 × 1 + 戈爾諾δ × 2）

**v3 canonical 保留**：

- 招牌開場：「問候您, 尊貴的顧客。」
- 拒議價定式：「本商行的報價即最終價。 敝方不接受議價。 好好考慮, 仔細考慮。」
- 色彩情緒：藍色艦橋(意外威脅) / 紫色艦橋(交易)
- 感嘆 icon：Presto!(變！) / LOOK OUT!(當心！) / Hoy!(喂！) / Ahhh-YING! / Fe-Fi-Fo-Fum!
- 艦名：於所有情境必勝之艦（`之` 保留於專名內）
- 帝國名：〈艦長〉之帝國（`之` 保留於專名內）
- v0.5.2 canonical 全套用：星幣 / 苦刑器 / 布維族 / 感知聯盟 / 永恆教條 / 現在與永恆之道 / 超時鐘 / 佐晶 / 免責同意書 / 跨維穿隙 / 火獄穿甲炮 / 濕婆熔爐 / 爆能砲 / 昏定波束槍 / 自動追蹤模組 / 赭黃副官 / 卓米雅 / Gg 族

**self-ref palette 分配**：

- Greenish 個體發言：**本人**（多用）
- 種族集體：**我方梅諾商** / **我方**（廢除 shipped v0.1『吾等梅諾商』185 處）
- 商業契約：**本商行** / **敝方** / **敝行**
- 對玩家：**您** 全 NPC 一致（包括 HATE_YOU / SLIGHTLY_ANGRY 段保商業距離冷諷刺）

## 🟠 措辭改變 (43 項)

### #1 · `HELLO_NOW_DOWN_TO_BUSINESS_3` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Hello again, human space captain. 
> Perhaps during this encounter, we will be able to establish a successful, businesslike relationship.

**Shipped v0.1**:

> 再次問候,人類太空艦長。
> 或許此番相遇,吾等可建立成功而正式之商業關係。

**Rebuild v3**（已通過階段 2.5 自審）:

> 再次問候, 人類太空艦長。
> 或許本次相遇, 我方能建立成功而正式的商業關係。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #2 · `KNOW_BECAUSE` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We gather information from a thousand secret sources in space and time.
> Our charge for revealing even one of these sources would be so high
> that your species would be in debt to us for centuries.

**Shipped v0.1**:

> 吾等自太空與時間中一千處秘密來源蒐集資訊。
> 光是揭示其中一處來源之費用便會如此高昂
> 您之物種將背負數世紀之債務。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方自太空與時間中一千處秘密來源蒐集情報。
> 光是揭示其中一處來源的費用
> 便會使您的物種背負數個世紀的債務。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #3 · `NO_TALK_ABOUT_OURSELVES` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Our origins and purposes are, frankly, mysterious and due to several unavoidable factors
> we are unable to discuss ourselves in any great detail.

**Shipped v0.1**:

> 吾等之起源與目的坦白說是神秘的,又由於幾項不可避免之因素
> 吾等無法詳細討論吾等自身之細節。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方的起源與目的, 坦白說, 是神秘的， 又由於幾項不可避免的因素
> 我方無法詳細討論自身的細節。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #4 · `what_about_universe` · 🟠 措辭改動

**英文原文**:

> Do you have any information which might be useful to us?

**Shipped v0.1**:

> 你們有什麼可能對我們有用的資訊嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 你們有什麼可能對我方有用的情報嗎？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #5 · `GIVING_IS_BAD_1` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> You are of course correct.
> We long ago abandoned currency,
> and now only deal with commodities that have intrinsic value, such as valuable information.

**Shipped v0.1**:

> 您所言當然正確。
> 吾等早於古時便捨棄貨幣,
> 如今僅與具有內在價值之商品交易,如寶貴資訊。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您所言當然正確。
> 我方早在遠古便捨棄了貨幣,
> 如今僅與具有內在價值的商品交易, 例如寶貴的情報。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #6 · `OK_NO_TRADE_NOW_BYE` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> When you wish to trade with us, seek any supergiant star system.
> We shall be there.

**Shipped v0.1**:

> 當您欲與吾等交易時,請尋找任何超巨星系。
> 吾等將於彼處。

**Rebuild v3**（已通過階段 2.5 自審）:

> 當您希望與我方交易時, 請前往任何超巨星系。
> 我方將在那裡。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #7 · `HELLO_AND_DOWN_TO_BUSINESS_1` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Yes, let us get down to business.

**Shipped v0.1**:

> 是的,吾等開始談生意吧。

**Rebuild v3**（已通過階段 2.5 自審）:

> 好的, 我方談生意吧。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #8 · `HELLO_AND_DOWN_TO_BUSINESS_5` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Once again we meet to exchange valuable tangibles.
> Isn't this fun?!

**Shipped v0.1**:

> 吾等又見面了以交換寶貴之實物。
> 此不有趣嗎？！

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方又見面了, 以交換寶貴的實物。
> 這不有趣嗎？！

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #9 · `HELLO_AND_DOWN_TO_BUSINESS_10` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Welcome back, Captain! You are our favorite customer.

**Shipped v0.1**:

> 歡迎回來,艦長！ 您是吾等最愛之顧客。

**Rebuild v3**（已通過階段 2.5 自審）:

> 歡迎回來, 艦長！ 您是我方最喜愛的顧客。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #10 · `HELLO_SLIGHTLY_ANGRY_1` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> So, the violent one has returned.
> Have you come back to seek our forgiveness
> or to attack our defenseless vessel once more?

**Shipped v0.1**:

> 哦,暴力之人回來了。
> 您是回來求吾等原諒
> 還是要再次攻擊吾等無防備之船艦？

**Rebuild v3**（已通過階段 2.5 自審）:

> 看啊, 暴力的人回來了。
> 您是回來尋求我方的原諒
> 還是要再次攻擊我方無防備的船艦？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #11 · `HELLO_SLIGHTLY_ANGRY_2` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> You have disappointed us
> though to be truthful
> we had some hints that our relationship would be difficult at first
> due to your species' emotional immaturity.

**Shipped v0.1**:

> 您使吾等失望了
> 不過老實說
> 吾等本有些預兆,吾等關係起初會很難
> 因您物種之情緒不成熟。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您使我方失望了
> 不過老實說
> 我方本有些預兆, 我方的關係起初會很難
> 因為您物種的情緒不成熟。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #12 · `HELLO_SLIGHTLY_ANGRY_3` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We require a formal apology.

**Shipped v0.1**:

> 吾等要求一次正式之道歉。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方要求一次正式的道歉。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #13 · `DECEITFUL_HUMAN` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Deceitful human!

**Shipped v0.1**:

> 詭詐之人類！

**Rebuild v3**（已通過階段 2.5 自審）:

> 詭詐的人類！

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #14 · `HELLO_HATE_YOU_1` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We thought you were a nice guy.
> Boy, were we wrong!
> Now go away and leave us alone.

**Shipped v0.1**:

> 吾等原以為您是好人。
> 哎,吾等大錯特錯！
> 如今您走遠一點,別再打擾吾等。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方原以為您是好人。
> 哎, 我方大錯特錯！
> 如今您走遠一點, 別再打擾我方。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #15 · `HELLO_HATE_YOU_3` · 🟠 文言助詞/之全清 + 現代化措辭

**英文原文**:

> We will hate you forever.
> It is no use coming back here in the hopes that we will ever change our minds.
> We won't!

**Shipped v0.1**:

> 吾等將永遠憎恨您。
> 您回來此地希望吾等改變心意乃無用之舉。
> 吾等不會！

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方將永遠憎恨您。
> 您回來這裡希望我方改變心意是徒勞的。
> 我方不會！

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #16 · `RESCUE_AGAIN_3` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We have come to help you once more, Captain.

**Shipped v0.1**:

> 吾等再次前來協助您,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方再次前來協助您, 艦長。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #17 · `CHANGED_MIND` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Have you changed your mind
> and decided to accept our offer of assistance?

**Shipped v0.1**:

> 您可改變心意
> 決定接受吾等之協助提議了？

**Rebuild v3**（已通過階段 2.5 自審）:

> 您已改變心意
> 決定接受我方的協助提議了？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #18 · `SHOULD_WE_HELP_YOU` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Would you like us to help you at this time?

**Shipped v0.1**:

> 您此時希望吾等協助嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 您此時希望我方協助嗎？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #19 · `RESCUE_OFFER` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> You have no Credit balance in our mercantile computer
> and our scanners show that you possess no useful trade goods
> but, perhaps we can work out a special deal.
> In exchange for our giving you enough fuel to

**Shipped v0.1**:

> 您於吾等之商業電腦中無星幣餘額
> 且吾等之感應器顯示您無有用之交易物
> 但,或許吾等可作一項特殊交易。
> 以敝方提供您足夠燃料為交換,以便

**Rebuild v3**（已通過階段 2.5 自審）:

> 您在我方的商業電腦中沒有星幣餘額
> 且我方的感應器顯示您沒有有用的交易物
> 但, 或許我方可以作一項特殊交易。
> 以敝方提供您足夠燃料為交換, 以便

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #20 · `RESCUE_TANKS` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> fill your tanks, we will take:

**Shipped v0.1**:

> 填滿您之油槽,吾等將取走:

**Rebuild v3**（已通過階段 2.5 自審）:

> 填滿您的油槽, 我方將取走:

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #21 · `RESCUE_HOME` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> get you home, we will take:

**Shipped v0.1**:

> 帶您回家,吾等將取走:

**Rebuild v3**（已通過階段 2.5 自審）:

> 帶您回家, 我方將取走:

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #22 · `GOODBYE_AND_GOODLUCK_AGAIN` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Until we meet again, Captain.

**Shipped v0.1**:

> 待吾等再會,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 期待我方再會, 艦長。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #23 · `HELLO_PISSED_OFF_1` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> The Human has returned.
> He hopes to either convince us of his sorrow over his past wrong-doings
> or he intends to compel us to give/render unreasonable bargains by force.

**Shipped v0.1**:

> 此人類回來了。
> 他希望能說服吾等他對過去錯行之悔恨
> 或欲以武力迫使吾等給予/提供不合理之交易。

**Rebuild v3**（已通過階段 2.5 自審）:

> 這個人類回來了。
> 他希望能說服我方他對過去錯行的悔恨
> 或想以武力迫使我方給予/提供不合理的交易。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #24 · `LOTS_TO_MAKE_UP_FOR` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Even if we were to accept your words as truth
> you have a lot to make up for.

**Shipped v0.1**:

> 即便吾等接受您之言為真
> 您仍有許多要彌補。

**Rebuild v3**（已通過階段 2.5 自審）:

> 即便我方接受您的話為真
> 您仍有許多要彌補的地方。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #25 · `YOU_NOT_STRONG_2` · 🟠 措辭改動

**英文原文**:

> Perhaps that is true, but you have only one ship.

**Shipped v0.1**:

> 或許此為真,但您僅有一艘艦艇。

**Rebuild v3**（已通過階段 2.5 自審）:

> 或許屬實, 但您只有一艘艦艇。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #26 · `REALLY_TESTING` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> You have an odd way of making friends, Captain.
> Are you certain that you aren't just tricking us
> so that you can attack us the moment our back is turned?

**Shipped v0.1**:

> 您有一套奇特之交友方式,艦長。
> 您確定您並非在誘騙吾等
> 以便在吾等背過身時攻擊吾等？

**Rebuild v3**（已通過階段 2.5 自審）:

> 您有一套奇特的交友方式, 艦長。
> 您確定您並非在誘騙我方
> 以便在我方背過身時攻擊我方？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #27 · `TEST_RESULTS` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We believe you.

**Shipped v0.1**:

> 吾等相信您。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方相信您。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #28 · `YOU_GIVE_US_NO_CHOICE` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> You give us no choice.

**Shipped v0.1**:

> 您給吾等別無選擇。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您使我方別無選擇。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #29 · `NOTHING_TO_SELL` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We appreciate your intentions, but you have nothing we wish to buy.

**Shipped v0.1**:

> 吾等感激您之意,但您無吾等欲購買之物。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方感激您的心意, 但您沒有我方想購買的東西。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #30 · `WHAT_TO_SELL` · 🟠 措辭改動

**英文原文**:

> What would you like to sell, Captain?

**Shipped v0.1**:

> 您欲賣什麼,艦長？

**Rebuild v3**（已通過階段 2.5 自審）:

> 您想賣什麼, 艦長？

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #31 · `SOLD_RAINBOW_LOCATIONS2` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

>  of the Rainbow worlds which so fascinate us.
> In exchange, we will give you 

**Shipped v0.1**:

>  個令吾等著迷之彩虹世界所在。
> 作為交換,吾等將給予您 

**Rebuild v3**（已通過階段 2.5 自審）:

>  個令我方著迷的彩虹世界所在。
> 作為交換, 我方將給予您 

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #32 · `FRIENDLY_GOODBYE` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> It has been a pleasure dealing with you, Captain.
> We look forward to your next visit.

**Shipped v0.1**:

> 與您做生意乃一件樂事,艦長。
> 吾等期待您之下次來訪。

**Rebuild v3**（已通過階段 2.5 自審）:

> 與您做生意是一件樂事, 艦長。
> 我方期待您的下次來訪。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #33 · `NEED_MORE_CREDIT0` · 🟠 措辭改動

**英文原文**:

> Unfortunately this purchase requires 

**Shipped v0.1**:

> 可惜此次購買需再多 

**Rebuild v3**（已通過階段 2.5 自審）:

> 可惜這次購買還需要 

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #34 · `BUY_FUEL_INTRO` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> As you know, we carry a large supply of fuel on board which is compatible with your engine system.
> We will be happy to sell this substance to you at a cost of 1 Credit per fuel unit.

**Shipped v0.1**:

> 如您所知,吾等艦上載有大量與您引擎系統相容之燃料。
> 吾等樂於以每單位燃料 1 星幣之價賣此物質予您。

**Rebuild v3**（已通過階段 2.5 自審）:

> 如您所知, 我方艦上載有大量與您引擎系統相容的燃料。
> 我方樂於以每單位燃料 1 星幣的價格賣這種物質給您。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #35 · `buy_info` · 🟠 措辭改動

**英文原文**:

> I wish to buy information.

**Shipped v0.1**:

> 我方想購買資訊。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方想購買情報。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #36 · `buy_current_events` · 🟠 措辭改動

**英文原文**:

> I wish to buy information about current events.

**Shipped v0.1**:

> 我方想購買關於當前情勢的資訊。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方想購買關於當前情勢的情報。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #37 · `buy_history` · 🟠 措辭改動

**英文原文**:

> Please sell us historical information.

**Shipped v0.1**:

> 請把歷史資訊賣給我方。

**Rebuild v3**（已通過階段 2.5 自審）:

> 請把歷史情報賣給我方。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #38 · `done_buying_info` · 🟠 措辭改動

**英文原文**:

> I am done buying information.

**Shipped v0.1**:

> 我方買完資訊了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方買完情報了。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #39 · `no_buy_info` · 🟠 措辭改動

**英文原文**:

> I do not wish to buy information at this time.

**Shipped v0.1**:

> 我方此時不欲購買資訊。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時不希望購買情報。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #40 · `OK_BUY_NEW_TECH` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Right now we are offering 

**Shipped v0.1**:

> 此時吾等提供 

**Rebuild v3**（已通過階段 2.5 自審）:

> 此時我方提供 

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #41 · `NEW_TECH_7` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> The technology we are now offering includes plans for improving the rate of fire
> on your lander's stunray bolt-beamer gun.

**Shipped v0.1**:

> 吾等此時提供之技術包括改進
> 登陸艇之昏定波束槍之射速藍圖。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括改進
> 登陸艇的昏定波束槍射速的藍圖。

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #42 · `NEW_TECH_ALL_GONE` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> Commander, that is the limit of the new technology we can offer you.
> If I may say so, you have been an excellent customer.
> Thank you!

**Shipped v0.1**:

> 指揮官,那乃吾等可提供予您之新技術之極限。
> 若本人可如此言,您一直是位絕佳之顧客。
> 感謝！

**Rebuild v3**（已通過階段 2.5 自審）:

> 指揮官, 那是我方可提供予您的新技術極限。
> 若本人可如此說, 您一直是位絕佳的顧客。
> 感謝！

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

### #43 · `STRIP_HEAD` · 🟠 文言/之清理 + 措辭調整

**英文原文**:

> We will take 

**Shipped v0.1**:

> 吾等將取走 

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方將取走 

**推薦**：🟠 B（v3 · 現代優雅商務語域 · 對齊 Utwig/Chmmr v3）

**你的選擇**：A / B / C(自訂)

---

## 🟡 微調(等價) (149 項)

### #1 · `HELLO_NOW_DOWN_TO_BUSINESS_1` · 🟡 細部文言/之清理

**英文原文**:

> I am Trade Master Greenish in command of the Melnorme starship
> `Inevitably Successful in All Circumstances.' 
> I bid you a formal welcome, Captain.
> Though we Melnorme have just recently arrived in this region of space
> we have long desired to make contact with your species 
> and look forward to an extended profitable relationship.

**Shipped v0.1**:

> 本人乃綠光貿易官,執掌梅諾商之星艦
> 「於所有情境必勝之艦」。
> 本人謹此正式歡迎您,艦長。
> 雖然吾等梅諾商剛抵達此星域
> 但吾等早已渴望與您之物種聯繫
> 並期待一段長久而有利可圖之關係。

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人即綠光貿易官, 執掌梅諾商的星艦
> 「於所有情境必勝之艦」。
> 本人謹此正式歡迎您, 艦長。
> 我方梅諾商雖剛抵達這片星域
> 卻早已渴望與您的物種聯繫
> 並期待一段長久而有利可圖的關係。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #2 · `HELLO_NOW_DOWN_TO_BUSINESS_2` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> As a master trader in the Melnorme merchant fleet, I greet you, Captain.
> News of your species and your unusual vessel has travelled quickly.
> I need not say how eager we are to trade with you and your kind! 
> Now, how can I be of service to you?

**Shipped v0.1**:

> 身為梅諾商商船隊之首席貿易官,本人致上問候,艦長。
> 關於您之物種與您那不尋常艦艇之消息傳得極快。
> 毋須贅言,吾等多麼渴望與您及您之族類交易！
> 如今,本人可如何為您效勞？

**Rebuild v3**（已通過階段 2.5 自審）:

> 身為梅諾商商船隊的首席貿易官, 本人向您致上問候, 艦長。
> 關於您的物種與您那艘不尋常艦艇的消息, 傳得極快。
> 毋須贅言, 我方多麼渴望與您以及您的族類交易！
> 如今, 本人可如何為您效勞？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #3 · `KNOW_OF_YOU` · 🟡 細部文言/之清理

**英文原文**:

> Even before our first meeting, we knew of you, Captain.
> Though your struggle to free Earth shall be a long and difficult challenge
> fraught with great danger and mystery
> we have great confidence in you and your abilities.

**Shipped v0.1**:

> 早於吾等首次會面之前,吾等便知曉您,艦長。
> 雖然您解放地球之奮鬥將是漫長艱困之挑戰
> 充滿危險與神秘
> 吾等對您與您之能力抱有極大信心。

**Rebuild v3**（已通過階段 2.5 自審）:

> 早在我方首次會面之前, 我方便已知曉您, 艦長。
> 雖然您解放地球的奮鬥將是漫長而艱困的挑戰
> 充滿危險與神秘
> 我方對您與您的能力抱有極大信心。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #4 · `how_know` · 🟡 細微措辭調整

**英文原文**:

> How did you know about us before meeting us?

**Shipped v0.1**:

> 你們在見到我們之前是怎麼知道我們的？

**Rebuild v3**（已通過階段 2.5 自審）:

> 你們在見到我方之前是怎麼知道我方的？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #5 · `what_about_yourselves` · 🟡 細微措辭調整

**英文原文**:

> What can you tell us about yourselves?

**Shipped v0.1**:

> 能告訴我們一些關於你們自己的事嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 能告訴我方一些關於你們自己的事嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #6 · `what_factors` · 🟡 細部文言/之清理

**英文原文**:

> What are these `unavoidable factors'?

**Shipped v0.1**:

> 什麼是這些「不可避免之因素」？

**Rebuild v3**（已通過階段 2.5 自審）:

> 什麼是這些「不可避免的因素」？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #7 · `FACTORS_ARE` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> First and foremost among these factors
> is our unwillingness to GIVE away information
> about our history, psychology and mental powers,
> our unique physiology,
> the exact locations of homeworlds,
> or our potentially ominous, long-range plans.
> However, these important and relevant pieces of information
> ARE available, for a nominal sum of Credits.

**Shipped v0.1**:

> 首要之因素
> 乃吾等不願「免費」贈予資訊
> 關於吾等之歷史、心理與心智能力,
> 吾等獨特之生理,
> 吾等母星之精確位置,
> 或吾等潛在不祥、長遠之計畫。
> 然而,這些重要而相關之資訊片段
> 若付出象徵性之星幣（Interstar Credits）數目,「是」可獲得的。

**Rebuild v3**（已通過階段 2.5 自審）:

> 首要的因素
> 即我方不願「免費」贈送情報
> 關於我方的歷史、心理與心智能力,
> 我方獨特的生理,
> 我方母星的精確位置,
> 或我方潛在不祥、長遠的計畫。
> 然而, 這些重要且相關的情報片段
> 只需付出象徵性的星幣（Interstar Credits）數目, 「是」可獲得的。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #8 · `NO_FREE_LUNCH` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Absolutely.
> Our primary trade good IS information.
> Why, right here on my display screen, I have something
> which I am certain would be of incalculable value to you!
> We can discuss the details of this VERY significant information
> later, when we have established normal trading procedures
> at which time we shall also discuss the nature of our fees.

**Shipped v0.1**:

> 絕對有。
> 吾等之主要交易品「即」資訊。
> 哎呀,此刻在本人之顯示器上,便有一項
> 本人確信對您具有無可估量價值之資訊！
> 吾等可稍後細談此「極」重要資訊之細節
> 屆時吾等亦將討論吾等費用之性質
> 此皆待雙方建立正常交易程序之後。

**Rebuild v3**（已通過階段 2.5 自審）:

> 絕對有。
> 我方的主要交易品「即」情報。
> 哎呀, 此刻在本人的顯示器上, 便有一項
> 本人確信對您具有無可估量價值的情報！
> 我方可稍後細談這項「極」重要情報的細節
> 屆時我方亦將討論費用的性質
> 此皆待雙方建立正常交易程序之後。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #9 · `giving_is_good_1` · 🟡 細部文言/之清理

**英文原文**:

> Fees! Surely your culture is far beyond such pettiness as money?

**Shipped v0.1**:

> 費用！ 貴文化之進步不早已超越金錢這等瑣事了嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 費用！ 貴文化的進步不早已超越金錢這等瑣事了嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #10 · `giving_is_good_2` · 🟡 細部文言/之清理

**英文原文**:

> But our cause is just! Isn't altruism the highest pinnacle of morality?

**Shipped v0.1**:

> 但我們的目標是正義的！ 難道利他不是道德之至高峰嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 但我方的目標是正義的！ 難道利他不是道德的至高峰嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #11 · `GIVING_IS_BAD_2` · 🟡 細部文言/之清理

**英文原文**:

> No, it is not.
> In fact, in our culture, `giving'
> with no fair exchange of goods or services,
> is considered vulgar and inappropriate.
> Please do not mention this subject again.

**Shipped v0.1**:

> 不,並非如此。
> 事實上,於吾等之文化中,「贈予」
> 若無公平之商品或服務交換,
> 乃粗鄙而不妥之舉。
> 請莫再提此話題。

**Rebuild v3**（已通過階段 2.5 自審）:

> 不, 並非如此。
> 事實上, 在我方的文化中, 「贈送」
> 若無公平的商品或服務交換,
> 是粗鄙而不妥的舉動。
> 請莫再提此話題。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #12 · `trade_is_for_the_weak` · 🟡 細部文言/之清理

**英文原文**:

> `Trade' is for the weak.  We TAKE what we want!

**Shipped v0.1**:

> 「交易」乃弱者之事。 我方要什麼便「拿」什麼！

**Rebuild v3**（已通過階段 2.5 自審）:

> 「交易」是弱者的事。 我方要什麼便「拿」什麼！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #13 · `WERE_NOT_AFRAID` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> We reel with inchoate fear, and are thrown into a sudden panic.
> Being peaceful by nature
> we would no doubt be unprepared for your sudden hostility
> were it not for the excellent weapon system we bought from the Keel-Verezy just last month.
> A weapon system which is fully locked on your command bridge, by the way.

**Shipped v0.1**:

> 吾等因未成形之恐懼而顫抖,並陷入突發之驚慌。
> 吾等本性和平
> 若非上月才向奇維瑞族購入之絕佳武器系統
> 吾等毫無疑問將對您突發之敵意毫無準備。
> 順帶一提,該武器系統已完全鎖定您之指揮艦橋。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方因未成形的恐懼而顫抖, 陷入突發的驚慌。
> 我方本性和平
> 若非上個月才向奇維瑞族購入的絕佳武器系統
> 我方毫無疑問將對您突發的敵意毫無準備。
> 順帶一提, 該武器系統已完全鎖定您的指揮艦橋。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #14 · `HELLO_AND_DOWN_TO_BUSINESS_2` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> How nice to see you again, Captain.
> Before we go on, I have a small announcement.
> As you may know, in our travels throughout the galaxy
> we Melnorme have found many strange and interesting alien artifacts.
> One of these devices is the MetaChron, a kind of trans-time alarm system.
> In a nutshell, it warns me of future dangers by predicting its own demise
> which is most likely linked to my own well being, since I keep it under my pillow.
> The unit is a small pyramid and, when all is well, white in color.
> But if we are proceeding along a timeline which will eventually result in the destruction of the MetaChron
> the unit slowly darkens. Presumably, it will be destroyed at the same time as it turns completely black.
> When we first entered this region of space, the MetaChron was white.
> Now it is light gray.
> At its present rate of change, something will destroy the MetaChron
> in the early part of the year 2159.
> In order to avoid this unpleasantness, we may be leaving just before this time
> so if you have business you wish to conduct with us
> I suggest you do so before January 2159, or February at the latest.

**Shipped v0.1**:

> 很高興再見到您,艦長。
> 在吾等繼續之前,本人有一小則公告。
> 如您所知,於吾等橫跨銀河之旅程中
> 吾等梅諾商發現了許多奇異而有趣之外星遺物。
> 其中一具裝置乃「超時鐘」(MetaChron),一種跨時間警報系統。
> 簡而言之,它以預測自身之毀滅來警示本人未來之危險
> 此毀滅最可能與本人自身之安危相關,因本人將它藏於枕下。
> 該裝置乃一小型金字塔,平時為白色。
> 但若吾等正沿著一條最終將導致超時鐘毀滅之時間線前進
> 該裝置將緩慢變暗。
> 推想它將於完全變黑之時同時毀滅。
> 吾等初入此星域時,超時鐘為白色。
> 如今它已是淺灰色。
> 以其當前之變色速率,將於 2159 年初有事物毀滅超時鐘。
> 為避免此不快之事,吾等可能會在此時之前離開
> 故若您有欲與吾等進行之交易
> 本人建議您於 2159 年 1 月之前完成,最晚不遲於 2 月。

**Rebuild v3**（已通過階段 2.5 自審）:

> 很高興再見到您, 艦長。
> 在我方繼續之前, 本人有一則小小的公告。
> 如您所知, 在我方橫跨銀河的旅程中
> 我方梅諾商發現了許多奇異而有趣的外星遺物。
> 其中一件裝置是「超時鐘」（MetaChron）, 一種跨時間警報系統。
> 簡而言之, 它藉由預測自身的毀滅來警示本人未來的危險
> 這毀滅最可能與本人自身的安危有關, 因為本人將它藏在枕頭下。
> 該裝置是一具小型金字塔, 平時為白色。
> 但如果我方正沿著一條最終將導致超時鐘毀滅的時間線前進
> 該裝置就會緩慢變暗。
> 推想它將在完全變黑的同時毀滅。
> 我方初入這片星域時, 超時鐘為白色。
> 如今已是淺灰色。
> 以目前的變色速率, 將於 2159 年初有某物毀滅超時鐘。
> 為避免這樁不快, 我方可能會在此之前離開
> 因此若您有希望與我方進行的交易
> 本人建議您在 2159 年 1 月之前完成, 最晚不遲於 2 月。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #15 · `HELLO_AND_DOWN_TO_BUSINESS_3` · 🟡 細微措辭調整

**英文原文**:

> I had itchy pods this morning, Captain, and here you are!

**Shipped v0.1**:

> 今早本人的孢子囊發癢,艦長,結果您就來了！

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人今早的孢子囊發癢, 艦長, 結果您就來了！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #16 · `HELLO_AND_DOWN_TO_BUSINESS_4` · 🟡 細部文言/之清理

**英文原文**:

> What a coincidence! I was just talking about you with a Keel-Verezy captain.
> They expressed great interest in your explorations and struggles against the Ur-Quan
> but, like all Verezy, I'm afraid they were hesitant to introduce themselves for fear of
> well, frightening you. 
> In any event, it is our pleasure to meet you once again.

**Shipped v0.1**:

> 多麼巧合！ 本人方才正與一位奇維瑞艦長談論您。
> 他們對您之探索與對抗烏寬之奮鬥深感興趣
> 但,如所有奇維瑞人,恐怕他們遲遲不敢自我介紹
> 擔心會,嗯,嚇著您。
> 無論如何,能再次與您相會是吾等之榮幸。

**Rebuild v3**（已通過階段 2.5 自審）:

> 多麼巧合！ 本人方才正與一位奇維瑞艦長談論您。
> 他們對您的探索與對抗烏寬的奮鬥深感興趣
> 但, 如同所有奇維瑞人, 恐怕他們遲遲不敢自我介紹
> 擔心會, 嗯, 嚇到您。
> 無論如何, 能再次與您相會是我方的榮幸。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #17 · `HELLO_AND_DOWN_TO_BUSINESS_6` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Your arrival was predicted by our Tzo crystal's vibrations.
> We already know why you are here and what you need from us; however
> etiquette requires that we act as though we are ignorant of your desires.

**Shipped v0.1**:

> 您之到來已由吾等佐晶（Tzo crystal）之震動所預測。
> 吾等已知您為何前來,以及您需要吾等提供什麼;然而
> 禮儀要求吾等表現得彷彿對您之欲求一無所知。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您的到來已由我方佐晶（Tzo crystal）的震動所預測。
> 我方已知您為何前來, 以及您需要我方提供什麼; 然而
> 禮儀要求我方表現得彷彿對您的欲求一無所知。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #18 · `HELLO_AND_DOWN_TO_BUSINESS_7` · 🟡 細部文言/之清理

**英文原文**:

> This very morning, I was just saying to subordinate Ochre
> `Fe-Fi-Fo-Fum! I smell the feet of a Hu-Hu-Man!'
> We laughed and laughed. What a synchronicity!

**Shipped v0.1**:

> 就在今晨,本人正對副官赭黃副官（Ochre）說
> 「Fe-Fi-Fo-Fum! I smell the feet of a Hu-Hu-Man!」（英國巨人童話台詞:「呸-啡-嗬-呸！ 我聞到人類的腳味！」）
> 吾等笑了又笑。 多麼同步之巧合！

**Rebuild v3**（已通過階段 2.5 自審）:

> 就在今晨, 本人正對副官赭黃副官（Ochre）說
> 「Fe-Fi-Fo-Fum! I smell the feet of a Hu-Hu-Man!」（英國巨人童話台詞:「呸-啡-嗬-呸！ 我聞到人類的腳味！」）
> 我方笑了又笑。 多麼同步的巧合！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #19 · `HELLO_AND_DOWN_TO_BUSINESS_8` · 🟡 細部文言/之清理

**英文原文**:

> I must warn you, Captain
> this is the time of the month we Melnorme drive exceptionally hard bargains.
> Beware!

**Shipped v0.1**:

> 本人必須警告您,艦長
> 這是每月之特定時期,吾等梅諾商此時特別強硬地討價還價。
> 當心！

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人必須警告您, 艦長
> 這是每月當中我方梅諾商特別強硬討價還價的時期。
> 當心！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #20 · `HELLO_AND_DOWN_TO_BUSINESS_9` · 🟡 細微措辭調整

**英文原文**:

> LOOK OUT!
> Hoy! What a close call!
> Captain, why did you try to run down that Keel-Verezy vessel!?
> You almost smashed it into flinders!
> What!? You didn't see it? Surely you -- oh
> Never mind.

**Shipped v0.1**:

> 當心！（LOOK OUT!）
> 喂！（Hoy!） 好險！
> 艦長,您為何要衝撞那艘奇維瑞艦艇！？
> 您差點將它撞成碎片！
> 什麼！？ 您沒看見它？ 明明就 —— 噢
> 算了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 當心！（LOOK OUT!）
> 喂！（Hoy!） 好險！
> 艦長, 您為何要衝撞那艘奇維瑞艦艇！？
> 您差點將它撞成碎片！
> 什麼！？ 您沒看見它？ 明明就 —— 噢
> 算了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #21 · `EXAMPLE_OF_RELATIONSHIP` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Your question reveals a certain lack of understanding
> about the nature of friendly, inter-species relationships. 
> We shall clarify the situation. 
> If you wish to be friends with someone
> never, EVER
> shoot wads of super-heated plasma at them. 
> Is this clear?

**Shipped v0.1**:

> 您之問題透露出對友好、跨物種關係之本質
> 某種程度之欠缺理解。
> 吾等將澄清此情況。
> 若您欲與人為友
> 永遠、絕對
> 不要向他們發射超高熱之電漿彈。
> 這清楚了嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 您的問題透露出對友好、跨物種關係本質
> 某種程度的欠缺理解。
> 我方將澄清這個情況。
> 若您希望與人為友
> 永遠、絕對
> 不要向他們發射超高熱的電漿彈。
> 這清楚了嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #22 · `excuse_1` · 🟡 細微措辭調整

**英文原文**:

> Look, mistakes happen.  Don't get so bent out of shape!

**Shipped v0.1**:

> 聽好,難免出錯嘛。 別這麼氣！

**Rebuild v3**（已通過階段 2.5 自審）:

> 聽好, 難免出錯嘛。 別這麼氣！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #23 · `NO_EXCUSE_1` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Spathi once used a similar excuse
> after an unfortunate incident at their base on <% comm.getStarName("Algol", "algolites") %> IV.
> They didn't like the climate there
> so they decided to make `just a few minor, climatic adjustments.'
> Their equipment went haywire, they panicked and fled
> and the entire atmosphere was stripped off the planet
> much to the native Algolites sincere,
> though short-lived, regret.

**Shipped v0.1**:

> 史怕族在他們 <% comm.getStarName("大陵五", "algolites") %>（Algol） IV 之基地
> 發生一起不幸事件後,曾用過類似之藉口。
> 他們不喜歡那裡之氣候
> 故決定進行「幾項小小的、氣候上的調整」。
> 他們的設備失控,他們慌亂逃走
> 整個大氣層被剝離該星球
> 讓當地之阿爾戈斯人（Algolites）真誠地
> 雖然短暫地,深表遺憾。

**Rebuild v3**（已通過階段 2.5 自審）:

> 史怕族在他們 <% comm.getStarName("大陵五", "algolites") %>（Algol） IV 的基地
> 發生一起不幸事件後, 曾用過類似的藉口。
> 他們不喜歡那裡的氣候
> 因此決定進行「幾項小小的、氣候上的調整」。
> 他們的設備失控, 他們慌亂逃走
> 整個大氣層被剝離出這顆星球
> 讓當地的阿爾戈斯人（Algolites）真誠地
> 雖然短暫地, 深表遺憾。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #24 · `excuse_2` · 🟡 細微措辭調整

**英文原文**:

> Let's just forget our battle ever happened, ok?

**Shipped v0.1**:

> 咱們就當先前的戰鬥從未發生過,好嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 咱們就當先前的戰鬥從未發生過, 好嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #25 · `excuse_3` · 🟡 細微措辭調整

**英文原文**:

> What do you want from me, a formal apology?

**Shipped v0.1**:

> 你們到底要什麼,一次正式的道歉嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 你們到底要什麼, 一次正式的道歉嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #26 · `NO_EXCUSE_3` · 🟡 細部文言/之清理

**英文原文**:

> There is a small possibility that an apology would set things right.
> But it would have to be genuine.

**Shipped v0.1**:

> 有極小之可能,道歉能弭平此事。
> 但那道歉必須是真心的。

**Rebuild v3**（已通過階段 2.5 自審）:

> 有極小的可能, 道歉能弭平這件事。
> 但那道歉必須是真心的。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #27 · `we_apologize` · 🟡 細微措辭調整

**英文原文**:

> I apologize. I'm sorry. Please forgive me, I beg you.

**Shipped v0.1**:

> 我方道歉。 我方很抱歉。 請你們原諒,懇請。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方道歉。 我方很抱歉。 請你們原諒, 懇請。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #28 · `APOLOGY_ACCEPTED` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Well, since you put it so nicely
> you seem so genuinely repentant
> we'll give you another chance to become trading partners with us.
> But don't ever attack us again
> Or the next time we won't be such nice guys.

**Shipped v0.1**:

> 既然您說得如此得體
> 您似乎如此真心悔改
> 吾等將再給您一次機會成為吾等之交易夥伴。
> 但別再攻擊吾等
> 否則下次吾等就不會這麼好說話了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 既然您說得如此得體
> 您似乎如此真心悔改
> 我方將再給您一次機會成為我方的交易夥伴。
> 但別再攻擊我方
> 否則下次我方就不會這麼好說話了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #29 · `MELNORME_SLIGHTLY_ANGRY_GOODBYE` · 🟡 細部文言/之清理

**英文原文**:

> Farewell, violent human.

**Shipped v0.1**:

> 別了,暴力之人類。

**Rebuild v3**（已通過階段 2.5 自審）:

> 別了, 暴力的人類。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #30 · `HELLO_HATE_YOU_2` · 🟡 細部文言/之清理

**英文原文**:

> So, the jerk is back.
> What do you want from us this time?
> Never mind, we don't want to know.

**Shipped v0.1**:

> 喔,混蛋回來了。
> 您這次要什麼？
> 算了,吾等不想知道。

**Rebuild v3**（已通過階段 2.5 自審）:

> 喔, 混蛋回來了。
> 您這次要什麼？
> 算了, 我方不想知道。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #31 · `well_if_thats_the_way_you_feel` · 🟡 細微措辭調整

**英文原文**:

> Die, eye-freak.

**Shipped v0.1**:

> 去死吧,獨眼怪。

**Rebuild v3**（已通過階段 2.5 自審）:

> 去死吧, 獨眼怪。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #32 · `WE_FIGHT_AGAIN` · 🟡 細部文言/之清理

**英文原文**:

> This time you shall pay for your transgressions!

**Shipped v0.1**:

> 此次您將為您之過犯付出代價！

**Rebuild v3**（已通過階段 2.5 自審）:

> 這次您將為您的過犯付出代價！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #33 · `RESCUE_EXPLANATION` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> According to our scanners and other sensitive devices
> you are immobile in HyperSpace with no fuel reserves.
> This is a serious situation.
> Without fuel you shall drift here until your batteries exhaust themselves
> then your life-support will fail
> and you will expire
> unless, of course
> a hostile alien vessel finds you here helpless
> and annihilates you mercilessly.
> This has been known to happen.
> However
> as a gesture of good will, and in the spirit of friendship, we offer our assistance!
> For a nominal fee.

**Shipped v0.1**:

> 根據吾等之感應器與其他敏感裝置
> 您正於超空間中停滯,無燃料儲備。
> 此乃嚴重之情況。
> 無燃料,您將於此漂流至電池耗盡
> 然後您之維生系統將失效
> 您將隕命
> 除非,當然
> 有敵對外星艦艇於此發現您無助之姿
> 並無情地殲滅您。
> 此事已有前例。
> 
> 然而
> 作為善意之表示,秉持友誼之精神,吾等提供協助！
> 只需象徵性費用。

**Rebuild v3**（已通過階段 2.5 自審）:

> 根據我方的感應器與其他敏感裝置
> 您正在超空間中停滯, 沒有燃料儲備。
> 這是嚴重的情況。
> 沒有燃料, 您將在此漂流至電池耗盡
> 然後您的維生系統將失效
> 您也將隕命
> 除非, 當然
> 有敵對外星艦艇在此發現您無助的姿態
> 並無情地殲滅您。
> 這種事已有前例。
> 
> 然而
> 作為善意的表示, 秉持友誼的精神, 我方提供協助！
> 只需象徵性費用。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #34 · `RESCUE_AGAIN_1` · 🟡 細部文言/之清理

**英文原文**:

> Once more we find ourselves in a position to help you.
> How wonderful.

**Shipped v0.1**:

> 吾等再次身處協助您之位置。
> 何等美妙。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方再次身處協助您的位置。
> 何等美妙。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #35 · `RESCUE_AGAIN_2` · 🟡 細部文言/之清理

**英文原文**:

> Have you ever considered buying more fuel tanks?
> Just a friendly suggestion, Captain.

**Shipped v0.1**:

> 您有考慮過購買更多燃料槽嗎？
> 只是友善之建議,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您有考慮過購買更多燃料槽嗎？
> 只是友善的建議, 艦長。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #36 · `RESCUE_AGAIN_4` · 🟡 細部文言/之清理

**英文原文**:

> We MUST stop meeting like this, Captain!
> Ha, ha, ha!

**Shipped v0.1**:

> 吾等「必須」停止以此方式相見,艦長！
> 哈,哈,哈！

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方「必須」停止以這種方式相見, 艦長！
> 哈, 哈, 哈！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #37 · `RESCUE_AGAIN_5` · 🟡 細微措辭調整

**英文原文**:

> Out of fuel again, eh, Captain?

**Shipped v0.1**:

> 又用光燃料了,啊,艦長？

**Rebuild v3**（已通過階段 2.5 自審）:

> 又用光燃料了, 啊, 艦長？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #38 · `no_changed_mind` · 🟡 細微措辭調整

**英文原文**:

> No thanks, I don't need your help right now.

**Shipped v0.1**:

> 不了謝謝,我方目前不需要幫助。

**Rebuild v3**（已通過階段 2.5 自審）:

> 不了謝謝, 我方目前不需要幫助。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #39 · `yes_help` · 🟡 細微措辭調整

**英文原文**:

> Yes, I would appreciate your assistance. What is your fee?

**Shipped v0.1**:

> 是的,我方很感激你們的協助。 收費為何？

**Rebuild v3**（已通過階段 2.5 自審）:

> 是的, 我方很感激你們的協助。 收費為何？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #40 · `leave_it` · 🟡 細微措辭調整

**英文原文**:

> This offer is absurd! I refuse.

**Shipped v0.1**:

> 此提議荒謬！ 我方拒絕。

**Rebuild v3**（已通過階段 2.5 自審）:

> 這項提議荒謬！ 我方拒絕。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #41 · `HAPPY_TO_HAVE_RESCUED` · 🟡 細部文言/之清理

**英文原文**:

> The exchange of fuel for equipment is complete.
> As always, it is a pleasure doing business with you.
> Goodbye, Captain.

**Shipped v0.1**:

> 燃料換裝備之交易已完成。
> 如常,與您做生意乃一件樂事。
> 再見,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 燃料換裝備的交易已完成。
> 如常, 與您做生意是一件樂事。
> 再見, 艦長。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #42 · `MAYBE_SEE_YOU_LATER` · 🟡 細部文言/之清理

**英文原文**:

> Well then, we bid you farewell.
> We hope to see you again
> though with you sitting here, dead in space
> vulnerable and alone
> we won't hold our breath.

**Shipped v0.1**:

> 既然如此,吾等向您道別。
> 吾等期待再次見到您
> 不過您坐在此處,死於太空之中
> 脆弱而孤獨
> 吾等就不抱期望了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 既然如此, 我方向您道別。
> 我方期待再次見到您
> 不過您坐在這裡, 死於太空之中
> 脆弱而孤獨
> 我方就不抱期望了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #43 · `GOODBYE_AND_GOODLUCK` · 🟡 細微措辭調整

**英文原文**:

> Good luck, Captain.

**Shipped v0.1**:

> 祝好運,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 祝好運, 艦長。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #44 · `HELLO_PISSED_OFF_2` · 🟡 細部文言/之清理

**英文原文**:

> Ahhh-YING!! Ahhh-YING! Ahhh-YING! Ahhh-Y
> Oh sorry, Captain. I was just meditating on the sorry state of your consciousness.
> Do you perceive any improvement?

**Shipped v0.1**:

> Ahhh-YING!! Ahhh-YING! Ahhh-YING! Ahhh-Y（梅諾商冥想咒語）
> 噢抱歉,艦長。 本人方才在冥想您意識之可悲狀態。
> 您察覺到任何改善嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> Ahhh-YING!! Ahhh-YING! Ahhh-YING! Ahhh-Y（梅諾商冥想咒語）
> 噢抱歉, 艦長。 本人方才在冥想您意識的可悲狀態。
> 您察覺到任何改善嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #45 · `HELLO_PISSED_OFF_3` · 🟡 細部文言/之清理

**英文原文**:

> Perhaps I can be of some assistance to you in this time of confusion and travail
> either make a sincere apology to us, or depart.

**Shipped v0.1**:

> 或許本人可在此困惑與艱辛之時對您有所幫助 ——
> 請對吾等作真誠之道歉,或離開。

**Rebuild v3**（已通過階段 2.5 自審）:

> 或許本人可在您困惑與艱辛的此刻對您有所幫助 ——
> 請對我方作真誠的道歉, 或離開。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #46 · `beg_forgiveness` · 🟡 細部文言/之清理

**英文原文**:

> We beg your forgiveness for our unwarranted aggression.

**Shipped v0.1**:

> 我方懇求你們原諒我方無端之侵略。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方懇求你們原諒我方無端的侵略。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #47 · `you_are_so_right` · 🟡 細部文言/之清理

**英文原文**:

> We stand prepared to make reparations for our previous conduct.

**Shipped v0.1**:

> 我方準備好為先前之行徑作出補償。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方準備好為先前的行徑作出補償。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #48 · `ONE_LAST_CHANCE` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Hmm
> hmm... hmm... hmm.
> Oh, very well then.
> We will give you a single opportunity to compensate us
> for the damages you have inflicted upon our mercantile fleet
> with your unreasonable attacks in the past.
> We will not make this offer a second time.
> You will give us all non-essential hardware from your vessel
> immediately!
> Do you accept?

**Shipped v0.1**:

> 嗯
> 嗯…… 嗯…… 嗯。
> 噢,那好吧。
> 吾等將給您一次單一之機會補償吾等
> 為您過去之不合理攻擊
> 對吾等商船隊所造成之損失。
> 吾等不會再作此提議第二次。
> 您將立即將您艦上所有非必要之硬體
> 交予吾等！
> 您接受嗎？

**Rebuild v3**（已通過階段 2.5 自審）:

> 嗯
> 嗯…… 嗯…… 嗯。
> 噢, 那好吧。
> 我方將給您一次單一的機會補償我方
> 以彌補您過去對我方商船隊
> 所造成的不合理攻擊損失。
> 我方不會再作出這項提議第二次。
> 您將立即將您艦上所有非必要的硬體
> 交予我方！
> 您接受嗎？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #49 · `ok_strip_me` · 🟡 細微措辭調整

**英文原文**:

> Ok, it's a deal, but ONLY the non-essentials!

**Shipped v0.1**:

> 好,成交,但「僅限」非必要的部分！

**Rebuild v3**（已通過階段 2.5 自審）:

> 好, 成交, 但「僅限」非必要的部分！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #50 · `FAIR_JUSTICE` · 🟡 細部文言/之清理

**英文原文**:

> Removal of non-essential equipment is complete.
> We are satisfied with the exchange, and believe that we can now pursue
> a productive business relationship.
> We shall forget the mistakes you made in the past. Mostly.

**Shipped v0.1**:

> 非必要裝備之取走已完成。
> 吾等對此交易感到滿意,並相信如今吾等可追求
> 一段富有成果之商業關係。
> 吾等將遺忘您過去所犯之錯誤。 大致上。

**Rebuild v3**（已通過階段 2.5 自審）:

> 非必要裝備的取走已完成。
> 我方對這項交易感到滿意, 並相信如今我方可追求
> 一段富有成果的商業關係。
> 我方將遺忘您過去所犯的錯誤。 大致上。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #51 · `OK_FIGHT_SOME_MORE` · 🟡 細微措辭調整

**英文原文**:

> No, YOU prepare to be destroyed!

**Shipped v0.1**:

> 不,是「您」該準備受死！

**Rebuild v3**（已通過階段 2.5 自審）:

> 不, 是「您」該準備受死！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #52 · `BLUE_IS_MAD` · 🟡 細部文言/之清理

**英文原文**:

> To us, blue ambience signifies a response to an unexpected threat
> it shows that we are under emotional distress
> and not incidentally
> it also lets us see our weapon consoles more clearly.

**Shipped v0.1**:

> 對吾等而言,藍色氛圍表示對意外威脅之反應
> 它顯示吾等正處於情緒困擾
> 且順帶一提
> 它亦讓吾等更清晰地看見武器控制台。

**Rebuild v3**（已通過階段 2.5 自審）:

> 對我方而言, 藍色氛圍代表對意外威脅的反應
> 它顯示我方正處於情緒困擾
> 且順帶一提
> 它也讓我方更清晰地看見武器控制台。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #53 · `we_strong_1` · 🟡 細微措辭調整

**英文原文**:

> We have no fear of you, Melnorme!

**Shipped v0.1**:

> 我方對你們無畏,梅諾商！

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方對你們無畏, 梅諾商！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #54 · `YOU_NOT_STRONG_1` · 🟡 細部文言/之清理

**英文原文**:

> Oh, you should.
> Once the Dramya thought they could steal from us.
> You don't see too many Dramya around these days, do you?

**Shipped v0.1**:

> 噢,您該畏才是。
> 卓米雅（Dramya）曾以為他們能偷竊吾等。
> 如今您可看不到多少卓米雅了,對吧？

**Rebuild v3**（已通過階段 2.5 自審）:

> 噢, 您該畏才是。
> 卓米雅（Dramya）曾以為他們能偷竊我方。
> 如今您看不到多少卓米雅了, 對吧？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #55 · `YOU_NOT_STRONG_3` · 🟡 細部文言/之清理

**英文原文**:

> Because it's against the law, and besides
> if you steal from us, the other Melnorme ships will have to raise their prices
> and other innocent space aliens will have to pay for your wrong-doing.
> Now that's not fair, is it?

**Shipped v0.1**:

> 因為那違法,再者
> 若您自吾等處偷竊,其他梅諾商艦艇便得抬高價格
> 其他無辜之外星人也將為您之過錯付出代價。
> 那可不公平,對吧？

**Rebuild v3**（已通過階段 2.5 自審）:

> 因為那違法, 再者
> 若您從我方這裡偷竊, 其他梅諾商艦艇便得抬高價格
> 其他無辜的外星人也將為您的過錯付出代價。
> 那可不公平, 對吧？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #56 · `just_testing` · 🟡 細微措辭調整

**英文原文**:

> Look, we were just testing your intentions.  We're actually peaceful and friendly.

**Shipped v0.1**:

> 聽好,我方只是在測試你們的意圖。 我方其實是和平又友善的。

**Rebuild v3**（已通過階段 2.5 自審）:

> 聽好, 我方只是在測試你們的意圖。 我方其實是和平又友善的。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #57 · `yes_really_testing` · 🟡 細微措辭調整

**英文原文**:

> I promise, we won't do anything sneaky like that.

**Shipped v0.1**:

> 我方保證,不會做那種偷雞摸狗的事。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方保證, 不會做那種偷雞摸狗的事。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #58 · `youre_on` · 🟡 細微措辭調整

**英文原文**:

> Let's just test out that weapon system, shall we?... IN COMBAT!

**Shipped v0.1**:

> 咱們就來測試一下你們的武器系統吧,如何？…… 就在戰場上！

**Rebuild v3**（已通過階段 2.5 自審）:

> 咱們就來測試一下你們的武器系統吧, 如何？…… 就在戰場上！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #59 · `TRADING_INFO` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Since this is your first time trading with us, let me explain how our system works.
> We are interested in purchasing certain items, specifically
> biological data on alien life forms
> and the coordinates of certain strange worlds whose radiant energies defy all scanners
> producing a rainbow-like image.
> In exchange, we have many interesting and valuable commodities, such as
> fuel compatible with your starship's HyperDrive thrusters,
> technological specifications, allowing you to build new devices for your ship
> and many important secrets which may help you in your travels.
> To facilitate trade, we translate all your sales into Interstar Credits
> with which you may make purchases.
> If you have any questions, don't hesitate to ask.

**Shipped v0.1**:

> 既然這是您首次與吾等交易,請容本人解釋吾等之系統如何運作。
> 吾等對特定物品有興趣購買,具體而言
> 關於外星生命形式之生物資料
> 以及某些奇異世界之座標,其輻射能量能擾亂所有感應器
> 產生彩虹般之圖像。
> 作為交換,吾等有許多有趣而寶貴之商品,例如
> 與您星艦之超空間推進器相容之燃料,
> 技術規格,讓您可為您之艦艇打造新裝置
> 以及許多可能助您旅行之重要秘密。
> 為便利交易,吾等將您所有之銷售轉換為星幣（Interstar Credits）
> 您可用以進行購買。
> 若您有任何問題,請不吝提出。

**Rebuild v3**（已通過階段 2.5 自審）:

> 既然這是您首次與我方交易, 請容本人解釋我方的系統如何運作。
> 我方對特定物品有興趣購買, 具體而言
> 關於外星生命形式的生物資料
> 以及某些奇異世界的座標, 其輻射能量能擾亂所有感應器
> 產生彩虹般的圖像。
> 作為交換, 我方有許多有趣而寶貴的商品, 例如
> 與您星艦超空間推進器相容的燃料,
> 技術規格, 讓您可為您的艦艇打造新裝置
> 以及許多可能助您旅行的重要秘密。
> 為便利交易, 我方將您所有的銷售轉換為星幣（Interstar Credits）
> 您可用來進行購買。
> 若您有任何問題, 請不吝提出。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #60 · `BUY_OR_SELL` · 🟡 細部文言/之清理

**英文原文**:

> Now, what can we do for you today?

**Shipped v0.1**:

> 如今,吾等今日可為您效勞什麼？

**Rebuild v3**（已通過階段 2.5 自審）:

> 如今, 我方今日可為您效勞什麼？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #61 · `goodbye` · 🟡 細微措辭調整

**英文原文**:

> Goodbye, Trade Master.

**Shipped v0.1**:

> 再見,貿易官。

**Rebuild v3**（已通過階段 2.5 自審）:

> 再見, 貿易官。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #62 · `TURNED_PURPLE_BECAUSE` · 🟡 細部文言/之清理

**英文原文**:

> That's a good question with a very interesting answer!
> The fee for this information is 12,000,000 Credits.

**Shipped v0.1**:

> 這是個好問題,有個非常有趣之答案！
> 此資訊之費用為 12,000,000 星幣。

**Rebuild v3**（已通過階段 2.5 自審）:

> 這是個好問題, 有個非常有趣的答案！
> 這項情報的費用為 12,000,000 星幣。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #63 · `SOLD_LIFE_DATA1` · 🟡 細部文言/之清理

**英文原文**:

> The 

**Shipped v0.1**:

> 自您艦上下載之 

**Rebuild v3**（已通過階段 2.5 自審）:

> 自您艦上下載的 

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #64 · `SOLD_RAINBOW_LOCATIONS1` · 🟡 細部文言/之清理

**英文原文**:

> Your ship's log indicates that you discovered the whereabouts of 

**Shipped v0.1**:

> 您艦艇之航行日誌顯示您發現了 

**Rebuild v3**（已通過階段 2.5 自審）:

> 您艦艇的航行日誌顯示您發現了 

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #65 · `SOLD_PRECURSOR_FIND` · 🟡 細部文言/之清理

**英文原文**:

> Always! Absolutely!
> In exchange we will give you
> N Credits

**Shipped v0.1**:

> 永遠要！ 絕對要！
> 作為交換,吾等將給予您
> N 星幣

**Rebuild v3**（已通過階段 2.5 自審）:

> 永遠要！ 絕對要！
> 作為交換, 我方將給予您
> N 星幣

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #66 · `changed_mind_no_sell` · 🟡 細微措辭調整

**英文原文**:

> On second thought, I don't think I want to sell anything.

**Shipped v0.1**:

> 轉念一想,我方不想賣任何東西了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 轉念一想, 我方不想賣任何東西了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #67 · `done_selling` · 🟡 細微措辭調整

**英文原文**:

> I am done selling, for now.

**Shipped v0.1**:

> 我方賣完了,目前為止。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方賣完了, 目前為止。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #68 · `NEED_CREDIT` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> You need Credits to purchase our trade items.
> To earn Credits you must sell us the items we desire, which are:
> biological data on alien lifeforms
> and the coordinates of certain strange worlds whose radiant energies defy all scanners
> producing a rainbow-like image.

**Shipped v0.1**:

> 您需要星幣以購買吾等之交易品。
> 為賺取星幣,您必須將吾等所欲之物品賣予吾等,即:
> 關於外星生命形式之生物資料
> 以及某些奇異世界之座標,其輻射能量能擾亂所有感應器
> 產生彩虹般之圖像。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您需要星幣才能購買我方的交易品。
> 為賺取星幣, 您必須將我方所需的物品賣給我方, 即:
> 關於外星生命形式的生物資料
> 以及某些奇異世界的座標, 其輻射能量能擾亂所有感應器
> 產生彩虹般的圖像。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #69 · `done_buying` · 🟡 細微措辭調整

**英文原文**:

> I am done buying, for now.

**Shipped v0.1**:

> 我方買完了,目前為止。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方買完了, 目前為止。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #70 · `GOT_FUEL` · 🟡 細部文言/之清理

**英文原文**:

> Fuel transferred to your vessel.

**Shipped v0.1**:

> 燃料已轉移至您之艦艇。

**Rebuild v3**（已通過階段 2.5 自審）:

> 燃料已轉移至您的艦艇。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #71 · `CREDIT_IS0` · 🟡 細部文言/之清理

**英文原文**:

> Your present balance is 

**Shipped v0.1**:

> 您目前之餘額為 

**Rebuild v3**（已通過階段 2.5 自審）:

> 您目前的餘額為 

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #72 · `NO_ROOM_FOR_FUEL` · 🟡 細部文言/之清理

**英文原文**:

> Your ship's capacity is insufficient to hold that much fuel.

**Shipped v0.1**:

> 您艦艇之容量不足以容納那麼多燃料。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您艦艇的容量不足以容納那麼多燃料。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #73 · `BUY_INFO_INTRO` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> As you know, in our many centuries of star-trading
> we Melnorme have come to learn much about what happens in our galaxy
> both now and in the ancient past.
> We have also kept records on the diverse alien races in your region of space.
> We will share this crucial knowledge with you for a fee of 75 Credits per informative fact.
> No refunds.

**Shipped v0.1**:

> 如您所知,於吾等歷經數世紀之星際貿易
> 吾等梅諾商已了解甚多關於吾等銀河所發生之事
> 無論當前或古代皆然。
> 吾等亦保存了您所在星域各異星族之紀錄。
> 吾等將以每條情資 75 星幣之費用與您分享此重要知識。
> 不接受退款。

**Rebuild v3**（已通過階段 2.5 自審）:

> 如您所知, 在我方歷經數個世紀的星際貿易之中
> 我方梅諾商已了解甚多關於銀河所發生之事
> 無論當前或古代皆然。
> 我方也保存了您所在星域各異星族的紀錄。
> 我方將以每條情資 75 星幣的費用與您分享這份重要知識。
> 不接受退款。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #74 · `OK_BUY_INFO` · 🟡 細微措辭調整

**英文原文**:

> How wonderful, Captain!

**Shipped v0.1**:

> 何等美妙,艦長！

**Rebuild v3**（已通過階段 2.5 自審）:

> 何等美妙, 艦長！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #75 · `OK_BUY_EVENT_1` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> While you probably believe that the Shofixti are extinct
> having caused their sun to flare with a device identical to the Utwig's super-bomb
> the truth is not so simple.
> There yet exists a chance to resuscitate this meta-marsupial species, though it will not be easy.
> The problem at hand seems simple: bring together two Shofixti of different sexes
> and the carnal gymnastics proceed. Given the short gestation and maturation time of the Shofixti
> you will have thousands of the creatures in ten years, and millions in twenty.
> Finding a male of the species is easier than flup
> simply visit the Shofixti's blasted star system at <% comm.getStarName("Delta Gorno", "shofixti") %>.
> Captain Tanaka or its sibling Katana shall greet you on your arrival.
> A warning! -- These warriors are old and fly in barely functional ships.
> If they mistakenly identify you as the enemy, do not return fire!
> Retreat and try to talk with them on their own level.
> The females of the species will be more difficult to obtain.
> The only supply of such remaining in the galaxy is at <% comm.getStarName("Alpha Cerenkov", "maidens") %> I
> included as part of General ZEX's bizarre and beloved menagerie.
> Fortunately for you, Captain, ZEX is considered... well... perverse, by his fellow VUX.
> This is because ZEX actually enjoys the presence of human beings.
> To acquire the Shofixti females, you will have to appease ZEX, or kill him.

**Shipped v0.1**:

> 雖然您可能相信修烈士族已滅絕
> 因他們以與憂特族超級炸彈相同之裝置引發了他們太陽之閃焰
> 真相並非如此簡單。
> 仍有一絲機會可使此超有袋類物種復甦,雖然那並不容易。
> 手頭上之問題看似簡單:將兩位不同性別之修烈士族聚在一起
> 肉體體操便會展開。 鑑於修烈士族短暫之妊娠與成熟時間
> 您將於十年內擁有數千隻此類生物,二十年內擁有數百萬。
> 找到雄性物種比拚下臭屁還容易
> 只需拜訪 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno） 之修烈士族被炸毀之星系。
> 田中艦長或其兄弟武士刀會於您抵達時問候您。
> 警告！ —— 這些戰士老了,駕駛著幾乎無法運作之艦艇。
> 若他們誤將您認作敵人,請勿還擊！
> 撤退並試著以他們之語言與其交談。
> 該物種之雌性將更難獲得。
> 銀河中此類餘存之唯一供應乃於 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） I
> 作為澤克斯上將之奇特而珍愛之珍藏館一部分。
> 幸運的是,對您而言,艦長,澤克斯被認為…… 嗯…… 變態,以其同儕 VUX 之標準。
> 這是因為澤克斯實際上「享受」人類之在場。
> 為獲得修烈士族雌性,您必須安撫澤克斯,或殺死他。

**Rebuild v3**（已通過階段 2.5 自審）:

> 雖然您可能相信修烈士族已滅絕
> 因他們以與憂特族超級炸彈相同的裝置引發了他們太陽的閃焰
> 真相並非如此簡單。
> 仍有一線機會可使這個超有袋類物種復甦, 雖然那並不容易。
> 手頭上的問題看似簡單: 將兩位不同性別的修烈士族湊在一起
> 肉體體操便會展開。 考慮到修烈士族短暫的妊娠與成熟時間
> 您將在十年內擁有數千隻這類生物, 二十年內擁有數百萬。
> 找到雄性物種比放個屁還容易
> 只需前往 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno） 之修烈士族被炸毀的星系。
> 田中艦長或其姊妹武士刀會在您抵達時問候您。
> 警告！ —— 這些戰士老了, 駕駛著幾乎無法運作的艦艇。
> 若他們誤將您認作敵人, 請勿還擊！
> 撤退並試著以他們的語言與他們交談。
> 該物種的雌性將更難獲得。
> 銀河中此類餘存的唯一供應在 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） I
> 作為澤克斯上將的奇特而珍愛的珍藏館的一部分。
> 幸運的是, 對您而言, 艦長, 澤克斯被認為…… 嗯…… 變態, 以其同儕 VUX 的標準。
> 這是因為澤克斯實際上「享受」人類的存在。
> 為獲得修烈士族雌性, 您必須安撫澤克斯, 或殺死他。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #76 · `OK_BUY_EVENT_2` · 🟡 細部文言/之清理

**英文原文**:

> The Ur-Quan are presently at war with a race called the Kohr-Ah.
> They are fighting within a large spherical region of space centered around the <% comm.getConstellation("Crateris", "samatra") %> star group.
> Although it is probably too early to tell, it would appear that the Kohr-Ah are winning.

**Shipped v0.1**:

> 烏寬目前正與一個名為柯亞之族類交戰。
> 他們正於一大片以 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris） 星群為中心之球形太空區域內作戰。
> 雖然現在斷言可能為時尚早,似乎柯亞正贏得上風。

**Rebuild v3**（已通過階段 2.5 自審）:

> 烏寬目前正與一個名為柯亞的族類交戰。
> 他們正在一大片以 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris） 星群為中心的球形太空區域內作戰。
> 雖然現在斷言可能為時尚早, 似乎柯亞正取得上風。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #77 · `OK_BUY_EVENT_3` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> No doubt you are familiar with an alien race called the Umgah who live in the <% comm.getConstellation("Orionis", "talking pet") %> constellation.
> While they are renowned for their potent and often cruel sense of humor
> they have outdone themselves in recent years.
> Specifically, they have used an unusual HyperWave 'Caster
> to impersonate the Ilwrath gods Dogar and Kazon.
> When the Ilwrath began tuning-in to `the voices of their gods' on their HyperWave receivers
> their priest caste was understandably skeptical
> and counselled their many followers to ignore the blasphemous signals.
> However, in a surprise move, the majority of the Ilwrath then rose up
> and slaughtered the entire priest caste.
> Their reasons for this ghastly move included over-taxation, lack of `quality death in ceremony'
> and the general feeling that the priests had made Dogar and Kazon's pronouncements overly complex.

**Shipped v0.1**:

> 毫無疑問您熟悉一種名為陰嘎族之外星種族,居於 <% comm.getConstellation("獵戶座", "talking pet") %>（Orionis） 星座。
> 雖然他們以強大而常殘忍之幽默感聞名
> 近年他們更是超越自我。
> 具體而言,他們用了一具不尋常之超波播送器
> 冒充蛛狂族之神祇多加與卡宗。
> 當蛛狂族開始於他們之超波接收器上收聽「他們神祇之聲」
> 他們之祭司階級可想而知起了疑心
> 並勸告他們眾多之信徒忽略此褻瀆之信號。
> 然而,出乎意料之舉,大多數之蛛狂族隨即起義
> 屠殺了整個祭司階級。
> 他們如此可怖行動之理由包括過度課稅、缺乏「儀式中之高品質死亡」
> 以及普遍認為祭司使多加與卡宗之神諭過於複雜之感受。

**Rebuild v3**（已通過階段 2.5 自審）:

> 毫無疑問您熟悉一種名為陰嘎族的外星種族, 居於 <% comm.getConstellation("獵戶座", "talking pet") %>（Orionis） 星座。
> 雖然他們以強大而常殘忍的幽默感聞名
> 近年他們更是超越自我。
> 具體而言, 他們用了一具不尋常的超波播送器
> 冒充蛛狂族的神祇多加與卡宗。
> 當蛛狂族開始在他們的超波接收器上收聽「他們神祇的聲音」
> 他們的祭司階級可想而知起了疑心
> 並勸告他們眾多的信徒忽略這種褻瀆的信號。
> 然而, 出乎意料的舉動, 大多數的蛛狂族隨即起義
> 屠殺了整個祭司階級。
> 他們如此可怖行動的理由包括過度課稅、缺乏「儀式中的高品質死亡」
> 以及普遍認為祭司使多加與卡宗的神諭過於複雜。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #78 · `OK_BUY_EVENT_4` · 🟡 細部文言/之清理

**英文原文**:

> As you know, there are weaknesses in the division between dimensions.
> For example, your vessel uses such weaknesses to enter HyperSpace.
> However, there are other weak spots in the galaxy which lead to yet different dimensions.
> One such portal exists nearby, <% comm.swapIfSeeded("between the ", "near the ") %><% comm.getConstellation("Chandrasekhar and Columbae", "arilou") %><% comm.swapIfSeeded(" constellations", " constellation") %>.
> The portal opens only a short time each month starting on the 17th.
> Since we have never entered the portal, we can give no more information on this subject.

**Shipped v0.1**:

> 如您所知,維度之間之分隔存在著弱點。
> 例如,您之艦艇便利用此類弱點進入超空間。
> 然而,銀河中還有其他弱點通往截然不同之維度。
> 其中一處入口存在於附近,<% comm.swapIfSeeded("位於 ", "靠近 ") %><% comm.getConstellation("錢德拉塞卡與天鴿座", "arilou") %>（Chandrasekhar and Columbae）<% comm.swapIfSeeded(" 星座之間", " 星座") %>。
> 此入口每月僅開啟短暫時間,自 17 日開始。
> 由於吾等從未進入該入口,吾等無法就此主題提供更多資訊。

**Rebuild v3**（已通過階段 2.5 自審）:

> 如您所知, 維度之間的分隔存在著弱點。
> 例如, 您的艦艇便利用這種弱點進入超空間。
> 然而, 銀河中還有其他弱點通往截然不同的維度。
> 其中一處入口存在於附近, <% comm.swapIfSeeded("位於 ", "靠近 ") %><% comm.getConstellation("錢德拉塞卡與天鴿座", "arilou") %>（Chandrasekhar and Columbae）<% comm.swapIfSeeded(" 星座之間", " 星座") %>。
> 這個入口每月只開啟短暫時間, 自 17 日開始。
> 由於我方從未進入該入口, 我方無法就這個主題提供更多情報。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #79 · `OK_BUY_EVENT_5` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> As you are probably aware, Ur-Quan starships -- you call them `Dreadnoughts', I believe
> possess effective self-annihilation circuits which prevent other races
> from reverse-engineering Ur-Quan technological secrets.
> However, we have become aware of a shipwrecked dreadnought which has remained largely intact.
> You will find the remains of the ship on the surface of a blue world orbiting <% comm.getStarName("Alpha Pavonis", "urquan wreck") %>.
> We suspect you will find at least one item of interest there, possibly two.

**Shipped v0.1**:

> 如您可能已知,烏寬星艦 —— 您稱之為「無畏艦」,本人相信
> 擁有有效之自毀電路,以防其他種族
> 逆向工程烏寬之科技秘密。
> 然而,吾等已察覺一艘失事之無畏艦仍大致完整。
> 您將於一顆環繞 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis） 之藍色世界表面上找到該艦之殘骸。
> 吾等懷疑您將於彼處找到至少一件感興趣之物,可能兩件。

**Rebuild v3**（已通過階段 2.5 自審）:

> 如您可能已知, 烏寬星艦 —— 您稱之為「無畏艦」, 本人相信
> 擁有有效的自毀電路, 以防其他種族
> 逆向工程烏寬的科技秘密。
> 然而, 我方已察覺一艘失事的無畏艦仍大致完整。
> 您將在一顆環繞 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis） 的藍色世界表面上找到該艦的殘骸。
> 我方懷疑您將在那裡找到至少一件感興趣的東西, 可能兩件。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #80 · `OK_BUY_EVENT_6` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> You may have noticed the presence of an increasingly large number of red probe vessels
> which move with great speed and attack relentlessly.
> We are sorry to say that this is our catalog item 2418-B.
> Do not blame us! We are not responsible for this violent folly!
> The product is not being used in a correct manner.
> Should you wish to confront the actual wrong-doers
> we suggest you search the planets in <% comm.getStarName("Beta Corvi", "slylandro") %> for the probes' owners.

**Shipped v0.1**:

> 您可能已注意到日益增多之紅色探測器
> 它們以極快速度移動,無情地攻擊。
> 吾等遺憾地告知,那乃吾等之目錄編號 2418-B。
> 莫怪吾等！ 吾等對此暴力愚行不負責任！
> 該產品未被以正確之方式使用。
> 您若欲對付真正之犯錯者
> 吾等建議您於 <% comm.getStarName("烏鴉座β", "slylandro") %>（Beta Corvi） 之行星中尋找此類探測器之主人。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您可能已注意到日益增多的紅色探測器
> 它們以極快速度移動, 無情地攻擊。
> 我方遺憾地告知, 那是我方的目錄編號 2418-B。
> 莫怪我方！ 我方對這樁暴力愚行不負責任！
> 這項產品未被以正確的方式使用。
> 您若想對付真正的犯錯者
> 我方建議您在 <% comm.getStarName("烏鴉座β", "slylandro") %>（Beta Corvi） 的行星中尋找這類探測器的主人。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #81 · `OK_BUY_EVENT_7` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Not more than fifty years ago
> the Druuge were informed by the now-extinct Burvixese race
> of a powerful alien nation called the Utwig.
> The Utwig, the Burvixese explained, were pleasant, sophisticated creatures
> but they were also terminally depressed and often spoke about ending their lives
> by activating a super-weapon, some kind of gigantic bomb
> which they had found on one of their worlds -- <% comm.getStarName("Zeta Hyades", "bomb") %> VI-B I think it was.
> The Druuge recognized the description of the bomb as a Precursor planeteering tool
> which indeed was an explosive device of unrivaled power, and they set out to make it their own.
> Though the revolting, criminal, insidious Druuge rarely leave their sphere of influence
> (it encompasses <% comm.swapIfSeeded("Algol, Almagest, and the ", "the ") %><% comm.getConstellation("Persei", "druuge") %> stars)
> they made a special trip on this occasion to the <% comm.getConstellation("Aquarii", "utwig") %> constellation, where they made contact with the Utwig.
> There is a device commonly known as the `Ultron'.
> Is it now in your possession? Ah... I see.
> The Druuge sold this device to the Utwig, explaining that it was a Precursor `Personal Magnifier'
> which would enrich the lives of their entire culture in too many ways to describe specifically.
> The Utwig, I am sorry to say, fell for the Druuge's foul ruse, and snapped up the Ultron immediately.
> Fortunately for us all, the Utwig did not pay the Druuge's requested price -- the super-bomb
> and instead gave them a collection of `historical oddments and genuine artifacts'
> which to this day, the Druuge are trying to unload on unwary buyers.

**Shipped v0.1**:

> 不到五十年前
> 毒賈族從如今已滅絕之布維族處得知
> 一個名為憂特族之強大異星國度。
> 布維族解釋,憂特族乃愉快、複雜之生物
> 但他們亦終極憂鬱,常談論如何結束自己之生命
> 藉由啟動一種超級武器,某種巨大之炸彈
> 那是他們於其一顆世界上找到的 —— <% comm.getStarName("畢宿星團ζ", "bomb") %>（Zeta Hyades） VI-B,本人以為。
> 毒賈族認出該炸彈之描述為先驅者之行星整地工具
> 那確實是一具威力無雙之爆炸裝置,他們遂決意將其占為己有。
> 儘管噁心、犯罪、陰險之毒賈族甚少離開其勢力範圍
> （那包含 <% comm.swapIfSeeded("大陵五、五車二與 ", "") %><% comm.getConstellation("英仙座", "druuge") %>（Persei）群星）
> 他們於此次為此特別出訪 <% comm.getConstellation("寶瓶座", "utwig") %>（Aquarii） 星座,於彼處與憂特族接觸。
> 有種裝置通稱為「厄創」。
> 它如今於您之持有？ 啊…… 本人明白了。
> 毒賈族將此裝置賣予憂特族,解釋那是一件先驅者之「個人增益器」
> 將以太多難以具體描述之方式豐富他們整個文化之生活。
> 憂特族,本人遺憾地說,中了毒賈族之骯髒詭計,立即搶購了厄創。
> 對吾等所有人而言之幸運,憂特族並未支付毒賈族要求之價格 —— 那超級炸彈
> 而是給予他們一批「歷史雜物與真跡古物」
> 毒賈族至今仍試圖將這些甩賣給不知情之買家。

**Rebuild v3**（已通過階段 2.5 自審）:

> 不到五十年前
> 毒賤族從如今已滅絕的布維族處得知
> 一個名為憂特族的強大異星國度。
> 布維族解釋, 憂特族是愉快、複雜的生物
> 但他們也終極憂鬱, 常談論如何結束自己的生命
> 藉由啟動一種超級武器, 某種巨大的炸彈
> 那是他們在其一顓世界上找到的 —— <% comm.getStarName("畢宿星團ζ", "bomb") %>（Zeta Hyades） VI-B, 本人以為。
> 毒賤族認出這炸彈的描述為先驅者的行星整地工具
> 那確實是一具威力無雙的爆炸裝置, 他們遂決意將其占為己有。
> 儘管噁心、犯罪、陰險的毒賤族甚少離開其勢力範圍
> （那包含 <% comm.swapIfSeeded("大陵五、五車二與 ", "") %><% comm.getConstellation("英仙座", "druuge") %>（Persei）群星）
> 他們在此次為此特別出訪 <% comm.getConstellation("寶瓶座", "utwig") %>（Aquarii） 星座, 在那裡與憂特族接觸。
> 有種裝置通稱為「厄創」。
> 它如今在您的持有中？ 啊…… 本人明白了。
> 毒賤族將這項裝置賣給憂特族, 解釋那是一件先驅者的「個人增益器」
> 將以太多難以具體描述的方式豐富他們整個文化的生活。
> 憂特族, 本人遺憾地說, 中了毒賤族的骷髝詭計, 立即搶購了厄創。
> 所幸對我方所有人而言, 憂特族並未支付毒賤族要求的價格 —— 那顆超級炸彈
> 而是給予他們一批「歷史雜物與真跡古物」
> 毒賤族至今仍試圖將這些甘賣給不知情的買家。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #82 · `OK_BUY_EVENT_8` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Utwig, who live in the <% comm.getConstellation("Aquarii", "utwig") %> constellation, have grown very depressed of late.
> They accidentally broke the supposed `Ultron' sold to them by the felonious Druuge.
> As a consequence, they are morose and melancholic
> and will probably be unwilling to help you fight the Ur-Quan.
> If you wish to gain them as allies, we recommend that you acquire the broken Ultron
> (as if it EVER worked)
> and find some suitable replacement parts.
> Our information indicates that you can find these items in three different places:
> a Rosy Sphere at the Druuge trade world
> an Aqua Helix somewhere in Thraddash space
> and a Clear Spindle, which is currently in the possession of the Pkunk.
> Captain, that was the last current event we have for sale.

**Shipped v0.1**:

> 居於 <% comm.getConstellation("寶瓶座", "utwig") %>（Aquarii） 星座之憂特族近來變得極為憂鬱。
> 他們不慎打壞了那件由重罪毒賈族賣予他們之所謂「厄創」。
> 因此,他們憂鬱且沉思
> 並可能不願協助您對抗烏寬。
> 若您欲爭取他們為盟友,吾等建議您取得那壞掉之厄創
> （假設它「曾經」運作過）
> 並找到一些合適之替換零件。
> 吾等之情報指示,您可於三個不同地方找到這些零件:
> 毒賈族貿易世界之玫瑰球體
> 某處撻伐族領空之蔚藍螺旋
> 以及一具目前由普恩族所擁有之澄澈紡錘。
> 艦長,那是吾等待售之最後一件當前事件。

**Rebuild v3**（已通過階段 2.5 自審）:

> 居於 <% comm.getConstellation("寶瓶座", "utwig") %>（Aquarii） 星座的憂特族近來變得極為憂鬱。
> 他們不慎打壞了那件由重罪毒賈族賣給他們的所謂「厄創」。
> 因此, 他們憂鬱且沉思
> 並可能不願協助您對抗烏寬。
> 若您想爭取他們為盟友, 我方建議您取得那件壞掉的厄創
> （假設它「曾經」運作過）
> 並找到一些合適的替換零件。
> 我方的情報指出, 您可在三個不同地方找到這些零件:
> 毒賈族貿易世界的玫瑰球體
> 某處撻伐族領空的蔚藍螺旋
> 以及一件目前由普恩族所擁有的澄澈紡錘。
> 艦長, 那是我方待售的最後一件當前事件。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #83 · `OK_BUY_ALIEN_RACE_1` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Zoq-Fot-Pik are a friendly co-op of three alien species all native to the same world.
> They are presently suffering severe collateral damage
> from the ritual combat between the Ur-Quan and the Kohr-Ah.
> While this is unfortunate for the Zoq-Fot-Pik -- they have been forced to abandon many of their worlds
> this close proximity to the inter-Ur-Quan war will give them insights into the conflict
> which will be of great use to you.
> In addition, the Zoq-Fot-Pik met the Chenjesu early on in the war, and are eager to make allies
> who can protect them from their enemies. 
> In case you are interested, the Zoq-Fot-Pik homeworld is at coordinates <% comm.getPoint("400.0:543.7", "zoqfot") %>, planet I.

**Shipped v0.1**:

> 佐-佛-皮乃三個共居於同世界之外星物種所組成之友善合作社。
> 他們目前遭受烏寬與柯亞儀式性戰鬥
> 之嚴重連帶傷害。
> 雖然此對佐-佛-皮而言是不幸的 —— 他們被迫放棄許多世界
> 此鄰近烏寬內部戰爭之地利將給予他們對此衝突之洞見
> 對您將大有用處。
> 此外,佐-佛-皮於戰爭早期便遇見晶智族,並渴望結交盟友
> 可保護他們免受敵人侵擾。
> 以防您感興趣,佐-佛-皮母星位於座標 <% comm.getPoint("400.0:543.7", "zoqfot") %> 之 I 號行星。

**Rebuild v3**（已通過階段 2.5 自審）:

> 佐-佛-皮是三個共居於同一世界的外星物種所組成的友善合作社。
> 他們目前遭受烏寬與柯亞儀式性戰鬥
> 的嚴重連帶傷害。
> 雖然這對佐-佛-皮而言是不幸的 —— 他們被迫放棄許多世界
> 這個鄰近烏寬內部戰爭的地利將給予他們對這場衝突的洞見
> 對您將大有用處。
> 此外, 佐-佛-皮在戰爭早期便遇見晶智族, 並渴望結交盟友
> 來保護他們免受敵人侵擾。
> 以防您感興趣, 佐-佛-皮母星位於座標 <% comm.getPoint("400.0:543.7", "zoqfot") %> 的 I 號行星。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #84 · `OK_BUY_ALIEN_RACE_2` · 🟡 細部文言/之清理

**英文原文**:

> The Ilwrath are presently attacking the Pkunk in the <% comm.getConstellation("Lacaille and Krueger", "pkunk") %><% comm.swapIfSeeded(" constellations", " constellation") %>.
> These beings have slavish devotion to their dark gods Dogar and Kazon
> which in the past few years has been used against them by the Umgah.
> If you need to manipulate the Ilwrath, we suggest you discover the Umgah's technique
> and duplicate it.

**Shipped v0.1**:

> 蛛狂族目前正於 <% comm.getConstellation("拉卡伊與克魯格", "pkunk") %>（Lacaille and Krueger）<% comm.swapIfSeeded(" 星座", " 星座") %> 攻擊普恩族。
> 這些生物對其黑暗神祇多加與卡宗有奴僕般之忠誠
> 過去幾年這被陰嘎族用來對付他們自身。
> 若您需要操縱蛛狂族,吾等建議您發現陰嘎族之技術
> 並複製之。

**Rebuild v3**（已通過階段 2.5 自審）:

> 蛛狂族目前正在 <% comm.getConstellation("拉卡伊與克魯格", "pkunk") %>（Lacaille and Krueger）<% comm.swapIfSeeded(" 星座", " 星座") %> 攻擊普恩族。
> 這些生物對他們的黑暗神祇多加與卡宗有奴僕般的忠誠
> 過去幾年這被陰嘎族用來對付他們自身。
> 若您需要操縱蛛狂族, 我方建議您找出陰嘎族的技術
> 並複製它。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #85 · `OK_BUY_ALIEN_RACE_3` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Pkunk are a mystical off-shoot of the Yehat species
> who left their bird-brothers long ago to found a peaceful enclave in the <% comm.getConstellation("Krueger and Giclas", "pkunk") %> stars.
> At the present time, the Pkunk are defending themselves against the Ilwrath
> who have been commanded to attack the happy birds by Dogar and Kazon. 
> The Pkunk may be unwilling to make a formal alliance with you
> but we have confidence that if you explain yourself honestly
> they will help your efforts against the Ur-Quan.

**Shipped v0.1**:

> 普恩族乃翼哈特族之神秘分支
> 他們於古時離開了他們之鳥兄弟,為了於 <% comm.getConstellation("克魯格與吉克拉斯", "pkunk") %>（Krueger and Giclas）群星建立一個和平之飛地。
> 目前,普恩族正抵禦蛛狂族
> 那些被多加與卡宗命令攻擊快樂鳥人之族群。
> 普恩族可能不願與您結成正式聯盟
> 但吾等有信心若您誠實地說明您自身
> 他們將協助您對抗烏寬之努力。

**Rebuild v3**（已通過階段 2.5 自審）:

> 普恩族是翼哈特族的神秘分支
> 他們早在古時離開了他們的鳥兄弟, 為了在 <% comm.getConstellation("克魯格與吉克拉斯", "pkunk") %>（Krueger and Giclas）群星建立一個和平的飛地。
> 目前, 普恩族正在抵禦蛛狂族
> 那些被多加與卡宗命令去攻擊快樂鳥人的族群。
> 普恩族可能不願與您結成正式聯盟
> 但我方有信心, 若您誠實地說明您自身
> 他們將協助您對抗烏寬的努力。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #86 · `OK_BUY_ALIEN_RACE_4` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The creatures presently fighting the Ur-Quan are called the Kohr-Ah.
> They are an Ur-Quan sub-species who split off from the main species many thousands of years ago.
> Their present fight is a ritual reenacting of a major difference of opinion
> between two, rival Ur-Quan leaders after the Ur-Quan overwhelmed their slave-masters, the Dnyarri.
> The Kohr-Ah are immune to reason, having long ago lost the ability to see their situation objectively.
> They live in a self-maintained paradox: to ensure their safety and security
> the Kohr-Ah fight an endless battle against all other sentient species.

**Shipped v0.1**:

> 目前與烏寬交戰之生物名為柯亞。
> 他們乃烏寬之亞種,於數千年前自主族分裂。
> 他們目前之戰鬥乃一次儀式性重演,兩位敵對之烏寬領袖
> 於烏寬推翻其奴役者蟾亞族後之重大意見分歧。
> 柯亞不接受任何理性,他們早已失去客觀看待自身處境之能力。
> 他們生活於一種自我維持之矛盾中:為確保其安全與保障
> 柯亞對所有其他智慧物種發動無盡之戰爭。

**Rebuild v3**（已通過階段 2.5 自審）:

> 目前與烏寬交戰的生物名為柯亞。
> 他們是烏寬的亞種, 在數千年前自主族分裂。
> 他們目前的戰鬥是一次儀式性重演, 兩位敵對的烏寬領袖
> 在烏寬推翻其奴役者蟾亞族後產生的重大意見分歧。
> 柯亞不接受任何理性, 他們早已失去客觀看待自身處境的能力。
> 他們生活在一種自我維持的矛盾中: 為確保他們的安全與保障
> 柯亞對所有其他智慧物種發動無盡的戰爭。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #87 · `OK_BUY_ALIEN_RACE_5` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> I must warn you about some very bad people.
> `Is this worth so many credits?' you ask yourself.
> I assure you, it is!
> The creatures are called the `Druuge' and they are a callous and evil race.
> They care for nothing but profit and personal gain through unfair mercantile exchanges..
> Why are you looking at me like that, Captain? It is not appropriate.
> As I was saying, these wicked creatures will try to sell you commodities at unreasonably low prices.
> Hoy! -- they almost give away fuel! 
> Do not fall for their tricks! There are hidden costs -- secret tariffs!
> So that you may avoid them, I will tell you that their main trade world is <% comm.getStarName("Zeta Persei", "druuge") %> I.
> Why are you smiling, Captain?

**Shipped v0.1**:

> 本人必須警告您關於一群非常壞之人。
> 「這值得那麼多星幣嗎？」您自問。
> 本人向您保證,值得！
> 那些生物名為「毒賈族」,他們乃一個冷酷而邪惡之種族。
> 他們除了透過不公平之商業交易獲取利潤與個人所得,無所關心。
> 您為何那樣看著本人,艦長？ 那不合適。
> 如本人所言,這些邪惡之生物將試圖以不合理之低價賣商品予您。
> 喂！ —— 他們幾乎是白送燃料！
> 莫上他們之當！ 那有隱藏成本 —— 秘密關稅！
> 為使您可避免之,本人將告訴您他們之主要貿易世界為 <% comm.getStarName("英仙座ζ", "druuge") %>（Zeta Persei） I。
> 您為何對本人微笑,艦長？

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人必須警告您關於一群非常壞的人。
> 「這值得那麼多星幣嗎？」您自問。
> 本人向您保證, 值得！
> 那些生物名為「毒賈族」, 他們是一個冷酷而邪惡的種族。
> 他們除了透過不公平的商業交易獲取利潤與個人所得, 別無所求。
> 您為何那樣看著本人, 艦長？ 那不合適。
> 如本人所言, 這些邪惡的生物將試圖以不合理的低價賣商品給您。
> 喂！ —— 他們幾乎是白送燃料！
> 莫上他們的當！ 那有隱藏成本 —— 秘密關稅！
> 為讓您可以避開他們, 本人將告訴您他們的主要貿易世界為 <% comm.getStarName("英仙座ζ", "druuge") %>（Zeta Persei） I。
> 您為何對本人微笑, 艦長？

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #88 · `OK_BUY_ALIEN_RACE_6` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Burvixese race evolved on the planet <% comm.getStarName("Arcturus", "burvixese") %> I.
> They lived there in a relatively benevolent manner
> until the Kohr-Ah came and destroyed them during the course of 2 or 3 unfortunate days.
> The Druuge were largely responsible for the Kohr-Ah finding the Burvixese.
> You see, the Burvixese were in long-distance HyperWave contact
> with a race known simply as the Gg.
> For decades the Gg and the Burvixese traded much valuable information
> until the Gg came under attack by an invading race who you may know as the Kohr-Ah.
> The Gg warned the Burvixese that the Kohr-Ah located races by their HyperWave transmissions
> and that they had already discovered the radiations from the Druuge.
> When the Burvixese were kind enough to warn the Druuge that a hostile alien race
> was homing in on their HyperWave radiations, the Druuge shut down all their transmitters
> and erected a powerful HyperWave beacon on the surface of the Burvixese moon.
> The Kohr-Ah changed course, attacked the poor Burvixese and sadly, destroyed them all.

**Shipped v0.1**:

> 布維族演化於 <% comm.getStarName("大角星", "burvixese") %>（Arcturus） I 之行星上。
> 他們於彼處以相對仁慈之方式居住
> 直至柯亞前來並於不幸之 2 或 3 天內將他們毀滅。
> 毒賈族大致對柯亞找到布維族一事負有責任。
> 您瞧,布維族與一個僅名為 Gg 族（Gg）之族類
> 進行遠距超波聯繫。
> 數十年來 Gg 族與布維族交易了許多寶貴資訊
> 直至 Gg 族遭到您可能認識之柯亞入侵。
>  Gg 族警告布維族柯亞是透過超波傳輸來定位種族
> 而他們已發現了毒賈族之輻射。
> 當布維族好心地警告毒賈族一支敵對外星種族
> 正歸引其超波輻射時,毒賈族關閉了所有傳送器
> 並在布維族月亮之表面豎起了一座強大之超波信標。
> 柯亞改變航線,攻擊了可憐之布維族並悲慘地將他們全數殲滅。

**Rebuild v3**（已通過階段 2.5 自審）:

> 布維族演化於 <% comm.getStarName("大角星", "burvixese") %>（Arcturus） I 的行星上。
> 他們在那裡以相對仁慈的方式居住
> 直到柯亞前來並在不幸的 2 或 3 天內將他們毀滅。
> 毒賈族對柯亞找到布維族一事負有很大的責任。
> 您瞧, 布維族與一個僅名為 Gg 族（Gg）的族類
> 進行遠距超波聯繫。
> 數十年來 Gg 族與布維族交易了許多寶貴情報
> 直到 Gg 族遭到您可能認識的柯亞入侵。
> Gg 族警告布維族, 柯亞是透過超波傳輸來定位種族
> 而他們已發現了毒賈族的輻射。
> 當布維族好心地警告毒賈族, 一支敵對外星種族
> 正歸引其超波輻射時, 毒賈族關閉了所有傳送器
> 並在布維族月亮的表面豎起了一座強大的超波信標。
> 柯亞改變航線, 攻擊了可憐的布維族, 悲慘地將他們全數殲滅。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #89 · `OK_BUY_ALIEN_RACE_7` · 🟡 細部文言/之清理

**英文原文**:

> The Thraddash are an arrogant, stubborn, and thick-skinned species
> who reside in the <% comm.getConstellation("Draconis and Apodis", "thraddash") %> star systems.
> They have little or no respect for anything but force, which they admire greatly.
> To make the Thraddash your friends, you should consider killing most, but not all of them.
> In addition, they guard some kind of sacred relic at the star system <% comm.getStarName("Zeta Draconis", "aqua helix") %>...
> ...though we do not know the true nature of this artifact.
> The Thraddash homeworld is at <% comm.getStarName("Delta Draconis", "thraddash") %>.

**Shipped v0.1**:

> 撻伐族乃一個傲慢、頑固、皮厚之物種
> 居於 <% comm.getConstellation("天龍座與天燕座", "thraddash") %>（Draconis and Apodis） 星系。
> 他們除武力外對任何事物幾無尊重,而武力乃他們所深愛。
> 若欲使撻伐族成為您之友,您應考慮殺死他們大多數,但非全部。
> 此外,他們於星系 <% comm.getStarName("天龍座ζ", "aqua helix") %>（Zeta Draconis） 守衛某種神聖遺物……
> ……不過吾等不知此遺物之真實本質。
> 撻伐族母星位於 <% comm.getStarName("天龍座δ", "thraddash") %>（Delta Draconis）。

**Rebuild v3**（已通過階段 2.5 自審）:

> 撻伐族是一個傲慢、頑固、皮厚的物種
> 居於 <% comm.getConstellation("天龍座與天燕座", "thraddash") %>（Draconis and Apodis） 星系。
> 他們除了武力之外對任何事物幾乎沒有尊重, 而武力是他們所深愛的。
> 若想使撻伐族成為您的朋友, 您應考慮殺死他們大多數, 但非全部。
> 此外, 他們在星系 <% comm.getStarName("天龍座ζ", "aqua helix") %>（Zeta Draconis） 守衛某種神聖遺物……
> ……不過我方不知這遺物真實的本質。
> 撻伐族母星位於 <% comm.getStarName("天龍座δ", "thraddash") %>（Delta Draconis）。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #90 · `OK_BUY_ALIEN_RACE_8` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> After the war, the Chenjesu and the Mmrnmhrm chose to be slave-shielded
> on the Chenjesu's homeworld at <% comm.getStarName("Procyon", "chmmr") %>.
> We suspect that they are melding their two species to form some kind of new, hybrid race
> a race which may well be powerful enough to destroy the Ur-Quan single-handedly.
> However, by our calculations, this process will take many decades, if not centuries.
> Should you wish to talk to them, we recommend you invest in a
> HyperWave broadcasting system which is powerful enough to penetrate the shield around their world.

**Shipped v0.1**:

> 戰後,晶智族與姆姆族選擇被奴役護盾保護
> 於晶智族母星 <% comm.getStarName("南河三", "chmmr") %>（Procyon）。
> 吾等懷疑他們正在融合兩物種以形成某種新之混種族
> 一個可能強大到足以獨力毀滅烏寬之種族。
> 然而,依吾等之計算,此過程將花費數十年,若非數世紀。
> 您若欲與他們交談,吾等建議您投資一具
> 強大到足以穿透其世界周圍護盾之超波廣播系統。

**Rebuild v3**（已通過階段 2.5 自審）:

> 戰後, 晶智族與姆姆族選擇被奴役護盾保護
> 在晶智族母星 <% comm.getStarName("南河三", "chmmr") %>（Procyon）。
> 我方懷疑他們正在融合兩個物種以形成某種新的混種族
> 一個可能強大到足以獨力毀滅烏寬的種族。
> 然而, 依我方的計算, 這個過程將花費數十年, 若非數個世紀。
> 您若想與他們交談, 我方建議您投資一具
> 強大到足以穿透其世界周圍護盾的超波廣播系統。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #91 · `OK_BUY_ALIEN_RACE_9` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Mycon are using this time while the Ur-Quan have their attention elsewhere
> to expand their sphere of influence as fast as possible.
> The Mycon colonize planets by launching tough spore-pods from orbit
> and injecting them under the planet's surface.
> Months later, after the spores have grown hundreds of thick, fibrous tendrils under the planet's crust
> the tendrils suddenly thrust up out of the planet and create huge calderas
> not incidentally filling the planet's atmosphere with the Mycon's preferred gases
> clouds of super-heated steam and sulphuric acid.

**Shipped v0.1**:

> 麥孔族正利用烏寬注意力被他處吸引之時
> 盡快擴展其勢力範圍。
> 麥孔族藉由自軌道發射堅韌之孢子莢殖民行星
> 並將其注入行星表面之下。
> 數月後,孢子已於行星之地殼下生長出數百根粗厚、纖維之觸鬚
> 觸鬚突然自行星鑽出並形成巨大之火山口
> 順帶將行星大氣層填滿麥孔族偏好之氣體
> 過熱蒸氣與硫酸之雲。

**Rebuild v3**（已通過階段 2.5 自審）:

> 麥孔族正利用烏寬注意力被他處吸引的時機
> 盡快擴展其勢力範圍。
> 麥孔族藉由從軌道發射堅韌的孢子莢殖民行星
> 並將其注入行星表面之下。
> 數月後, 孢子已在行星的地殼下生長出數百根粗厚、纖維狀的觸鬚
> 觸鬚突然從行星鑽出並形成巨大的火山口
> 順帶將行星大氣層填滿麥孔族偏好的氣體
> 過熱蒸氣與硫酸的雲。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #92 · `OK_BUY_ALIEN_RACE_10` · 🟡 細部文言/之清理

**英文原文**:

> Following the end of the War, the Androsynth began experimenting with Inter-Dimensional Fatigue
> a process which is related to your faster-than-light drive
> but involves dimensions far more alien than HyperSpace.
> They had just made a major breakthrough when they were suddenly wiped out by a race called the Orz
> who appeared seemingly out of nowhere.
> Actually, we don't know what the Orz did to the Androsynth -- they're just all gone.

**Shipped v0.1**:

> 戰爭結束後,安卓辛族開始實驗跨維穿隙（Inter-Dimensional Fatigue, IDF）
> 此過程與您之超光速引擎相關
> 但涉及之維度遠比超空間更為異形。
> 他們剛取得重大突破時就突然被一個名為歐茲之族類消滅
> 歐茲彷彿從無處冒出。
> 事實上,吾等不知歐茲對安卓辛族做了什麼 —— 他們就是全部消失了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 戰爭結束後, 安卓辛族開始實驗跨維穿隙（Inter-Dimensional Fatigue, IDF）
> 這個過程與您的超光速引擎相關
> 但涉及的維度遠比超空間更為異形。
> 他們剛取得重大突破時, 就突然被一個名為歐茲的族類消滅
> 歐茲彷彿從無處冒出。
> 事實上, 我方不知歐茲對安卓辛族做了什麼 —— 他們就是全部消失了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #93 · `OK_BUY_ALIEN_RACE_11` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Arilou Lalee'lay are a mysterious race of IDF beings
> IDF meaning, Inter-Dimensional Fatigue.
> They do not reside in this galaxy, or in fact, anywhere in this universe.
> While it is true that the Arilou are rarely seen far from the <% comm.getConstellation("Columbae", "arilou") %> star group
> they do make regular, secret visits to your world, and have done so for centuries.
> Ever since Earth was slave-shielded, they have focused their attention
> on the humans aboard the starbase, many of whom are now members of your crew.
> Though the Arilou Lalee'lay always smile and are never overtly hostile
> we believe that they have a secret agenda which somehow involves your planet, Earth.
> These secret plans may or may not cause grief and woe to you Earthlings.

**Shipped v0.1**:

> 阿麗露乃 IDF 生物之神秘物種
> IDF 意即「跨維穿隙」（Inter-Dimensional Fatigue）。
> 他們並不居於此銀河,實際上不居於此宇宙任何處。
> 雖然阿麗露鮮少於 <% comm.getConstellation("天鴿座", "arilou") %>（Columbae） 星群遠處出現屬實
> 他們卻對您之世界進行定期、秘密之訪問,並已如此做了數世紀。
> 自地球被奴役護盾包圍以來,他們將注意力集中於
> 星際基地上之人類,他們許多如今已為您船員之成員。
> 儘管阿麗露總是微笑且從不明顯有敵意
> 吾等相信他們有一項秘密議程,以某種方式涉及您之行星,地球。
> 這些秘密計畫可能造成或不造成您地球人之悲痛與哀愁。

**Rebuild v3**（已通過階段 2.5 自審）:

> 阿麗露是 IDF 生物的神秘物種
> IDF 意即「跨維穿隙」（Inter-Dimensional Fatigue）。
> 他們並不居於這個銀河, 實際上不居於這個宇宙中的任何地方。
> 雖然阿麗露鮮少在 <% comm.getConstellation("天鴿座", "arilou") %>（Columbae） 星群遠處出現屬實
> 他們卻對您的世界進行定期、秘密的訪問, 並已如此做了數個世紀。
> 自地球被奴役護盾包圍以來, 他們將注意力集中在
> 星際基地上的人類, 他們許多如今已為您船員的成員。
> 儘管阿麗露總是微笑且從不明顯有敵意
> 我方相信他們有一項秘密議程, 以某種方式涉及您的行星, 地球。
> 這些秘密計畫可能造成或不造成您地球人的悲痛與哀愁。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #94 · `OK_BUY_ALIEN_RACE_12` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Just under 20 years ago, the brave and suicidal Shofixti annihilated their species
> by exploding a Precursor device -- some kind of bomb -- in the interior of their sun.
> The resulting storm of solar flares cooked the life off the Shofixti homeworld
> and incinerated over a hundred Ur-Quan Dreadnoughts
> which had just entered the system to conquer the Shofixti.
> In actuality, there are still at least a dozen Shofixti left alive in the galaxy.
> One or two are at <% comm.getStarName("Delta Gorno", "shofixti") %>, guarding the dead hulk of their once beautiful world.
> Others can be found in VUX space.

**Shipped v0.1**:

> 不到 20 年前,勇敢而自殺之修烈士族
> 藉由於其太陽內部引爆一具先驅者裝置 —— 某種炸彈 —— 而滅絕其物種。
> 所產生之太陽閃焰風暴烤盡了修烈士族母星之生命
> 並焚燒了逾一百艘剛進入該星系來征服修烈士族之烏寬無畏艦。
> 實際上,銀河中仍至少有一打修烈士族存活。
> 一兩位於 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno）
> 守衛其曾美麗世界之死亡殘骸。
> 其他則可於 VUX 領空找到。

**Rebuild v3**（已通過階段 2.5 自審）:

> 不到 20 年前, 勇敢而自殺的修烈士族
> 藉由在其太陽內部引爆一具先驅者裝置 —— 某種炸彈 —— 而滅絕了自己的物種。
> 所產生的太陽閃焰風暴烤盡了修烈士族母星的生命
> 並焚燒了超過一百艘剛進入該星系來征服修烈士族的烏寬無畏艦。
> 實際上, 銀河中仍至少有一打修烈士族存活。
> 一兩位在 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno）
> 守衛他們曾美麗世界的死亡殘骸。
> 其他則可在 VUX 領空找到。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #95 · `OK_BUY_ALIEN_RACE_13` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Slylandro are a mostly non-solid, sentient race who live in a gas giant at <% comm.getStarName("Beta Corvi", "slylandro") %>.
> We recently sold them a self-replicating exploration probe
> which has somehow turned hostile and attacks everything it detects.
> If such encounters have angered you, Captain, please do NOT address your concerns to us.
> We possess a formal Waiver of Damages, authorized by a Slylandro Speaker
> and are in no way responsible for the situation.

**Shipped v0.1**:

> 斯萊族乃一個主要非固態之智慧種族,居於 <% comm.getStarName("烏鴉座β", "slylandro") %>（Beta Corvi） 之氣態巨行星。
> 吾等最近將一具自我複製之探索探測器賣予他們
> 那些探測器不知何故變得有敵意,並攻擊它偵測到之一切。
> 此類遭遇若已使您憤怒,艦長,請「勿」向吾等提出您之疑慮。
> 吾等擁有一份由一位斯萊族發言者授權之正式免責同意書
> 且對此情況絕無責任。

**Rebuild v3**（已通過階段 2.5 自審）:

> 斯萊族是一個主要非固態的智慧種族, 居於 <% comm.getStarName("烏鴉座β", "slylandro") %>（Beta Corvi） 的氣態巨行星。
> 我方最近將一具自我複製的探索探測器賣給他們
> 那些探測器不知何故變得有敵意, 並攻擊它偵測到的一切。
> 這類遭遇若已使您憤怒, 艦長, 請「勿」向我方提出您的疑慮。
> 我方擁有一份由一位斯萊族發言者授權的正式免責同意書
> 且對這個情況絕無責任。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #96 · `OK_BUY_ALIEN_RACE_14` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The cowardly Spathi live at the single planet orbiting <% comm.getStarName("Epsilon Gruis", "spathi") %>.
> They do not actually live on their world, rather they reside on its airless moon.
> The reason? A xenomorphic species, which craves the sweet-flavored flesh of the Spathi
> has been transported to the surface of their planet
> and makes every attempt to devour the poor Spathi.
> I am certain that the Spathi would be forever in your debt
> if you were to eliminate these creatures from their planet.
> What? You fear the alien creatures will find you a treat also?
> Fear not. Our data reveals the beasts are not interested in your species.
> Should you wish to consult with the Spathi Ruling Council
> you will need to know the Secret Spathi Cypher -- a password, which is
> `Huffi-Muffi-Guffi'.

**Shipped v0.1**:

> 怯懦之史怕族居於環繞 <% comm.getStarName("天鶴座ε", "spathi") %>（Epsilon Gruis） 之單一行星。
> 他們實際上並不住於其世界,而是居於其無空氣之月亮。
> 原因？ 一種渴望史怕族甘甜血肉之異形物種
> 已被運送至其行星表面
> 並竭盡所能吞食可憐之史怕族。
> 本人相信史怕族若您能為他們消滅其行星上之這些生物
> 將永遠對您感恩戴德。
> 什麼？ 您擔心那些外星生物也將把您當成美味？
> 莫怕。 吾等之資料顯示那些野獸對您之物種無興趣。
> 您若欲諮詢史怕族統治議會
> 您將需知道史怕族秘密密碼 —— 一組通關語,即
> 「呼夫姆夫古夫（Huffi-Muffi-Guffi）」。

**Rebuild v3**（已通過階段 2.5 自審）:

> 怯懦的史怕族居於環繞 <% comm.getStarName("天鶴座ε", "spathi") %>（Epsilon Gruis） 的單一行星。
> 他們實際上並不住於他們的世界, 而是居於其無空氣的月亮。
> 原因？ 一種渴望史怕族甘甜血肉的異形物種
> 已被運送至他們行星的表面
> 並竭盡所能吞食可憐的史怕族。
> 本人相信, 若您能為他們消滅這顆行星上的這些生物
> 史怕族將永遠對您感恩戴德。
> 什麼？ 您擔心那些外星生物也會把您當成美味？
> 莫怕。 我方的資料顯示那些野獸對您的物種沒興趣。
> 您若想諮詢史怕族統治議會
> 您將需要知道史怕族秘密密碼 —— 一組通關語, 即
> 「呼夫姆夫古夫（Huffi-Muffi-Guffi）」。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #97 · `OK_BUY_ALIEN_RACE_15` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Like you Earthlings, when the war with the Ur-Quan was lost
> the Syreen chose to be slave-shielded. Their new world is at <% comm.getStarName("Betelgeuse", "syreen") %>.
> The Syreen's starbase is crewed by the starship commanders and crew
> who were decommissioned at the end of the war.
> Though the Syreen hate the Ur-Quan with a vengeance, they are unlikely to offer you assistance
> unless you reveal to them the truth behind the tragedy of their original homeworld, Syra
> which was destroyed by the birth of a Mycon `Deep Child' a century ago.

**Shipped v0.1**:

> 如您地球人,當對烏寬之戰爭失利時
> 塞蓮族選擇被奴役護盾保護。 他們之新世界位於 <% comm.getStarName("參宿四", "syreen") %>（Betelgeuse）。
> 塞蓮族之星際基地由戰時結束後被退役之
> 星艦指揮官與船員擔任乘員。
> 儘管塞蓮族對烏寬懷有深仇大恨,他們不太可能提供您協助
> 除非您向他們揭露她們原始母星,賽拉,悲劇背後之真相
> 那顆星球一世紀前被一位麥孔族「深淵之子」之誕生所毀。

**Rebuild v3**（已通過階段 2.5 自審）:

> 如同您地球人一樣, 當對烏寬的戰爭失利時
> 塞蓮族選擇被奴役護盾保護。 他們的新世界位於 <% comm.getStarName("參宿四", "syreen") %>（Betelgeuse）。
> 塞蓮族的星際基地由戰爭結束後被退役的
> 星艦指揮官與船員擔任乘員。
> 儘管塞蓮族對烏寬懷有深仇大恨, 他們不太可能提供您協助
> 除非您向他們揭露她們原始母星, 賽拉, 悲劇背後的真相
> 那顆星球在一個世紀前被一位麥孔族「深淵之子」的誕生所毀。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #98 · `OK_BUY_ALIEN_RACE_16` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> When the Ur-Quan entered <% comm.getStarName("Gamma Serpentis", "yehat") %> -- the home star of the Yehat
> their Queen made a sudden change of allegiance and allied with the Ur-Quan Hierarchy.
> They became Ur-Quan combat thralls.
> This act was viewed by most Yehat starship officers as ultimately dishonorable
> the desperate act of a corrupt regent to maintain her throne.
> The Yehat's shame was greatly magnified by the Shofixti's show of courage
> when they destroyed their own star system to slow down the Ur-Quan Armada.
> Captain, you have heard all that we have to say about aliens indigenous to this region.
> Should we learn more in the near future, we shall be certain to sell it to you.

**Shipped v0.1**:

> 當烏寬進入 <% comm.getStarName("巨蛇座γ", "yehat") %>（Gamma Serpentis） —— 翼哈特族之母星時
> 他們之女王突然改變效忠並與烏寬階層結盟。
> 他們成為烏寬之戰奴。
> 此舉被大多數翼哈特族星艦軍官視為極端不名譽
> 那乃一位腐敗之攝政者為維持其王位之絕望之舉。
> 翼哈特族之恥辱被修烈士族之勇氣展示大幅放大
> 那時他們毀滅其自身之星系以拖延烏寬艦隊。
> 艦長,您已聽過吾等關於此區域原生外星人所需說之全部。
> 若吾等於近期學到更多,吾等必定會賣予您。

**Rebuild v3**（已通過階段 2.5 自審）:

> 當烏寬進入 <% comm.getStarName("巨蛇座γ", "yehat") %>（Gamma Serpentis） —— 翼哈特族的母星時
> 他們的女王突然改變效忠並與烏寬階層結盟。
> 他們成為烏寬的戰奴。
> 這件事被大多數翼哈特族星艦軍官視為極端不名譽
> 那是一位腐敗的攝政者為維持其王位的絕望之舉。
> 翼哈特族的恥辱被修烈士族的勇氣展示大幅放大
> 那時他們毀滅自己的星系來拖延烏寬艦隊。
> 艦長, 您已聽過我方關於這個區域原生外星人所要說的一切。
> 若我方在近期學到更多, 我方必定會賣給您。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #99 · `OK_BUY_HISTORY_1` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Almost twenty-five thousand of your years ago, there existed near this region of space
> an association of starfaring races called the `Sentient Milieu'.
> This group formed over several thousand years to mutually enrich their respective cultures
> to provide a safe creche for emerging sentient species
> and to afford themselves a degree of protection from external hostilities via military alliance.
> Of the seven most active Milieu members, the most famous race -- indeed you know them well, Captain
> were the Ur-Quan.

**Shipped v0.1**:

> 約在您年代之兩萬五千年前,於此星域附近
> 存在一個名為「感知聯盟」之星際旅行種族聯合體。
> 此團體歷經數千年形成
> 以相互豐富各自之文化,為新興之智慧物種提供安全之搖籃
> 並藉由軍事聯盟為自身提供對抗外來敵意之某種程度之保護。
> 感知聯盟七個最活躍成員中,最著名之族類 —— 您確實熟識他們,艦長
> 即烏寬。

**Rebuild v3**（已通過階段 2.5 自審）:

> 約在您年代的兩萬五千年前, 於這片星域附近
> 存在一個名為「感知聯盟」的星際旅行種族聯合體。
> 這個團體歷經數千年形成
> 以相互豐富各自的文化, 為新興的智慧物種提供安全的搖籃
> 並藉由軍事聯盟為自身提供對抗外來敵意的某種程度的保護。
> 感知聯盟七個最活躍的成員中, 最著名的族類 —— 您確實熟識他們, 艦長
> 即是烏寬。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #100 · `OK_BUY_HISTORY_2` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Ur-Quan evolved on a harsh planet orbiting a star outside this region of space.
> They were solitary predators, like your praying mantis, Captain, or polar bear
> who had a very limited set of social behaviors, most of which dealt with sex.
> Since they had to compete for survival against many physically superior species
> the Ur-Quan evolved intelligence and tool use, in much the same way as your own species.
> The Ur-Quan also learned to master their fierce territoriality to build a cooperative planetary culture.
> When the Ur-Quan were discovered by the Taalo, they had just begun exploring their solar system
> in crude atomic vehicles.
> Although the Ur-Quan attacked what they thought to be an invader, the Taalo were patient.
> They explained the purpose of the Sentient Milieu, and offered the Ur-Quan membership.
> The Ur-Quan recognized the benefits that such a system provided
> and once more conquered the hunting beast within themselves
> to become cooperative, productive members of the Milieu. This lasted for several thousands of years.

**Shipped v0.1**:

> 烏寬演化於此星域外一顆環繞恆星之嚴酷行星。
> 他們乃孤獨之掠食者,如您之螳螂,艦長,或北極熊
> 擁有極為有限之社交行為,其中大多與性有關。
> 由於他們必須與許多身體上優越之物種競爭生存
> 烏寬演化出智慧與工具使用,與您自身物種相同之方式。
> 烏寬亦學會了掌握其兇猛之領土性以建立合作之行星文化。
> 當烏寬被塔洛族發現時,他們剛以粗糙之原子載具
> 開始探索其太陽系。
> 雖然烏寬攻擊他們認為是入侵者之物,塔洛族有耐心。
> 他們解釋了感知聯盟之宗旨,並邀請烏寬加入。
> 烏寬認識到此制度所提供之利益
> 並再次征服自身內部之獵食野獸
> 以成為感知聯盟之合作、有生產力之成員。 此持續了數千年。

**Rebuild v3**（已通過階段 2.5 自審）:

> 烏寬演化於這片星域外一顆環繞恆星的嚴酷行星。
> 他們是孤獨的掠食者, 如同您的螳螂, 艦長, 或北極熊
> 擁有極為有限的社交行為, 其中大多與性有關。
> 由於他們必須與許多身體上優越的物種競爭生存
> 烏寬演化出智慧與工具使用, 與您自身物種相同的方式。
> 烏寬也學會了掌握自身兇猛的領土性, 以建立合作的行星文化。
> 當烏寬被塔洛族發現時, 他們才剛以粗糙的原子載具
> 開始探索自身的太陽系。
> 雖然烏寬攻擊他們認為是入侵者的對象, 塔洛族有耐心。
> 他們解釋了感知聯盟的宗旨, 並邀請烏寬加入。
> 烏寬認識到這種制度所提供的利益
> 並再次征服自身內部的獵食野獸
> 以成為感知聯盟的合作、有生產力的成員。 這種狀態持續了數千年。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #101 · `OK_BUY_HISTORY_3` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Just over twenty thousand years ago
> when your ancestors were learning to chart the course of the moon and stars on animal horns
> the Sentient Milieu spanned five hundred light years and included the membership of a hundred worlds.
> Like all other star-travellers, they had discovered ruins and relics of a far more ancient culture
> which your species calls the `Precursors'.
> Explorers from many species spent their lives trying to piece together this ancient mystery
> but of all races, the Ur-Quan were the most bold adventurers.
> Their scouts, flying single-ships, penetrated far into uncharted space, and landed on a million worlds.
> On one such mission, a young Ur-Quan made planetfall on a small, life-bearing alien world
> to identify some anomalous energy readings, occasionally a sign of Precursor installations.
> Instead the Ur-Quan found a small, hideous creature -- a Dnyarri.
> Before the scout was able to defend itself, the Dnyarri creature took control of the Ur-Quan's mind
> and commanded the scout to place the Dnyarri aboard the Ur-Quan's ship, along with hundreds of its evil brood.
> Then the Ur-Quan returned to the heart of the Milieu, landing on its capital planet.
> Within hours, every resident of the planet was a Dnyarri slave.
> Within a month, Dnyarri-compelled starships had spread the evil, psychic creatures across the entire Milieu.

**Shipped v0.1**:

> 剛過兩萬年前
> 當您祖先正在動物角上學習繪製月亮與星辰之航線時
> 感知聯盟橫跨五百光年,包括一百顆世界之成員。
> 如所有其他之星際旅行者,他們發現了遠古文化之廢墟與遺物
> 您之物種稱為「先驅者」。
> 來自多種族之探險家花費畢生時間試圖拼湊此古老之謎團
> 但於所有族類中,烏寬乃最大膽之冒險者。
> 他們之偵察兵,駕駛單人艦,深入未經標記之太空,並登陸於百萬顆世界。
> 於某次此類任務中,一位年輕之烏寬於一顆小小、有生命之外星世界降落
> 以識別某些異常之能量讀數,那有時是先驅者設施之徵兆。
> 然而烏寬找到了一個小、可憎之生物 —— 一位蟾亞。
> 偵察兵尚未能自衛之前,那蟾亞生物已控制了烏寬之心靈
> 並命令偵察兵將蟾亞連同其數百邪惡幼崽一同安置於烏寬之艦上。
> 然後烏寬回到了感知聯盟之心臟,登陸於其首都行星。
> 數小時內,該行星每一位居民都成了蟾亞之奴隸。
> 一個月內,由蟾亞控制之星艦已將邪惡之心靈生物散播至整個感知聯盟。

**Rebuild v3**（已通過階段 2.5 自審）:

> 剛過兩萬年前
> 當您的祖先正在動物角上學習繪製月亮與星辰的航線時
> 感知聯盟橫跨五百光年, 包括一百顆世界的成員。
> 如同所有其他的星際旅行者, 他們發現了遠古文化的廢墟與遺物
> 您的物種稱為「先驅者」。
> 來自多種族的探險家花費畢生時間試圖拼湊這個古老的謎團
> 但在所有族類中, 烏寬是最大膽的冒險者。
> 他們的偵察兵, 駕駛單人艦, 深入未經標記的太空, 並登陸在百萬顆世界。
> 在某次這類任務中, 一位年輕的烏寬在一顆小小、有生命的外星世界降落
> 為的是識別某些異常的能量讀數, 那有時是先驅者設施的徵兆。
> 然而烏寬找到的是一個小、可憎的生物 —— 一位蟾亞。
> 偵察兵尚未能自衛之前, 那蟾亞生物已控制了烏寬的心靈
> 並命令偵察兵將蟾亞連同其數百邪惡幼崽一同安置在烏寬的艦上。
> 然後烏寬回到了感知聯盟的心臟, 登陸在其首都行星。
> 數小時內, 該行星每一位居民都成了蟾亞的奴隸。
> 一個月內, 由蟾亞控制的星艦已將這種邪惡的心靈生物散播至整個感知聯盟。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #102 · `OK_BUY_HISTORY_4` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> When the Dnyarri took control over the Milieu, one race fought back -- the Taalo.
> These slow, quiet creatures were silicon-based life forms
> but bore little resemblance to the modern Chenjesu.
> The Taalo were natural immunes to the Dnyarri psychic compulsion; they were unaffected by the creatures' power
> and the Dnyarri would not permit anyone to exist outside their control
> so they ordered the remaining races of the Milieu to attack and destroy the Taalo home planet.
> This planet was one of the few Milieu worlds located in this region of space.
> I believe you call their star <% comm.getStarName("Delta Vulpeculae", "taalo protector") %>. Their home was a moon revolving about the second planet.
> I am sad to say that the Taalo were, indeed, eliminated.
> However, at the time of their devastation they had completed a device
> which they thought would give other races psychic immunity like their own.
> What happened to this device, this shield? It's hard to say.
> Maybe it was destroyed in the attack on their homeworld, maybe not.

**Shipped v0.1**:

> 當蟾亞取得感知聯盟之控制時,一族反擊 —— 塔洛族。
> 這些緩慢、安靜之生物乃矽基生命體
> 但與現代晶智族少有相似。
> 塔洛族天生免疫於蟾亞之心靈強迫;他們不受該生物力量之影響
> 而蟾亞不允許任何存在於其控制之外
> 故他們命令感知聯盟其餘之族類攻擊並毀滅塔洛族之母行星。
> 此行星乃感知聯盟少數位於此星域之世界之一。
> 本人相信您稱其星為 <% comm.getStarName("狐狸座δ", "taalo protector") %>（Delta Vulpeculae）。 他們之家園乃圍繞第二顆行星旋轉之衛星。
> 本人遺憾地說,塔洛族確實被消滅了。
> 然而,於其被毀滅之時,他們已完成了一具裝置
> 他們認為它將給予其他族類與其自身相同之心靈免疫。
> 此裝置,此護盾,發生了什麼事？ 難以斷言。
> 或許它於其母星之攻擊中被毀,或許沒有。

**Rebuild v3**（已通過階段 2.5 自審）:

> 當蟾亞取得感知聯盟的控制時, 只有一族反擊 —— 塔洛族。
> 這些緩慢、安靜的生物是矽基生命體
> 但與現代晶智族少有相似。
> 塔洛族天生免疫於蟾亞的心靈強迫; 他們不受該生物力量的影響
> 而蟾亞不允許任何存在於他們的控制之外
> 因此他們命令感知聯盟其餘的族類攻擊並毀滅塔洛族的母行星。
> 這個行星是感知聯盟少數位於這片星域的世界之一。
> 本人相信您稱其星為 <% comm.getStarName("狐狸座δ", "taalo protector") %>（Delta Vulpeculae）。 他們的家園是圍繞第二顆行星旋轉的衛星。
> 本人遺憾地說, 塔洛族確實被消滅了。
> 然而, 在他們被毀滅之時, 他們已完成了一具裝置
> 他們認為它將給予其他族類與其自身相同的心靈免疫。
> 這項裝置, 這面護盾, 發生了什麼事？ 難以斷言。
> 或許它在其母星的攻擊中被毀, 或許沒有。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #103 · `OK_BUY_HISTORY_5` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> In the Dnyarri's new empire, the Ur-Quan were the favored slaves.
> This is probably because the Ur-Quan were the most psychically sensitive, the most easily compelled.
> As the centuries of Dnyarri dominance passed, what was once the Sentient Milieu
> deteriorated and degenerated into a great galactic gulag.
> Alien races which did not serve with the efficiency and speed demanded by the Dnyarri
> were ruthlessly burned from the faces of their worlds.
> The agents of this genocide were inevitably the Dnyarri's favored pet, the Ur-Quan.
> After almost twenty-five hundred years of unrelenting Dnyarri control
> there were only four living member races of the once-great Sentient Milieu.
> By this point, the Dnyarri had used genetic manipulation to split the Ur-Quan into two sub-species:
> the Green Ur-Quan -- scientists, technicians, and administrators
> who were responsible for maintaining the limited infrastructure of the Dnyarri civilization
> and the Black Ur-Quan, who filled the ranks of basic laborer and combat soldier.
> Then, a chance discovery by an Ur-Quan named Kzer-Za
> led to the violent overthrow of the Dnyarri Slave Empire.

**Shipped v0.1**:

> 於蟾亞新之帝國中,烏寬乃最受寵之奴隸。
> 這大概因為烏寬乃最具心靈敏感之族類,最易被操控者。
> 隨著數世紀之蟾亞統治過去,曾經之感知聯盟
> 退化並淪為一座巨大之銀河集中營。
> 未以蟾亞所要求之效率與速度服役之外星族類
> 被無情地自其世界表面燒盡。
> 此種族滅絕之執行者無可避免是蟾亞最愛之寵物,烏寬。
> 經歷近乎兩千五百年之無情蟾亞控制
> 那曾偉大之感知聯盟僅剩四個活著之成員族類。
> 屆時,蟾亞已使用基因操控將烏寬分裂為兩亞種:
> 綠色烏寬 —— 科學家、技術人員與管理者
> 負責維持蟾亞文明之有限基礎設施
> 以及黑色烏寬,他們充當基層勞工與戰鬥士兵。
> 然後,一位名為克澤札之烏寬之偶然發現
> 引發了對蟾亞奴隸帝國之暴力推翻。

**Rebuild v3**（已通過階段 2.5 自審）:

> 在蟾亞新的帝國中, 烏寬是最受寵的奴隸。
> 這大概是因為烏寬是最具心靈敏感的族類, 最易被操控者。
> 隨著數個世紀的蟾亞統治過去, 曾經的感知聯盟
> 退化並淪為一座巨大的銀河集中營。
> 未以蟾亞所要求的效率與速度服役的外星族類
> 被無情地從他們的世界表面燒盡。
> 這種族滅絕的執行者無可避免是蟾亞最寵愛的寵物, 烏寬。
> 經歷近兩千五百年無情的蟾亞控制
> 那曾偉大的感知聯盟只剩下四個活著的成員族類。
> 屆時, 蟾亞已使用基因操控將烏寬分裂為兩個亞種:
> 綠色烏寬 —— 科學家、技術人員與管理者
> 負責維持蟾亞文明的有限基礎設施
> 以及黑色烏寬, 他們擔任基層勞工與戰鬥士兵。
> 然後, 一位名為克澤札的烏寬所做的偶然發現
> 引發了對蟾亞奴隸帝國的暴力推翻。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #104 · `OK_BUY_HISTORY_6` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The Ur-Quan named Kzer-Za was a Green, a researcher specializing in repairing the mental damage
> inflicted by long-term exposure to the Dnyarri's psychic compulsion.
> By this point in history, the Dnyarri had grown lax in their dominance
> and on occasion accidentally permitted their slaves moments of self-direction.
> Kzer-Za was able to use those few scattered minutes to compose a theory.
> From its observations, Kzer-Za realized that when a slave died
> the Dnyarri `disconnected' from the slave's mind, lest it too be dragged down to death.
> Further, the Ur-Quan scientist uncovered the fact that when a slave underwent great pain
> the Dnyarri temporarily disconnected -- but that the degree of pain had to be extreme, nearly lethal.
> Kzer-Za chose its moment carefully -- it waited until it was near an open transmission unit.
> Then, in a short moment of mental freedom, the Ur-Quan injected itself with a dose of acidic poison
> sending incredible waves of pain through its long body.
> In the few moments before its death, Kzer-Za was able to wrest control of the transmitter
> to send word of its discovery across the planet, and into space as well.
> Before the Dnyarri knew what was happening
> Ur-Quan everywhere were hacking at their own bodies with chunks of glass, burning themselves horribly
> doing anything that would give them the few seconds of freedom necessary to find the nearest Dnyarri
> and crush the bleating creature.
> As they gained longer and longer periods of control, the Ur-Quan developed new tools and weapons
> to destroy their evil masters. The most gruesome of these devices was the Excruciator
> a mechanism which was inserted directly into the brain, and generated a constant stream of agony.
> The Dnyarri could not bring themselves to make the necessary mental connection with these tortured Ur-Quan.
> They were slaughtered by the thousands.
> The Ur-Quan Slave revolt was won.

**Shipped v0.1**:

> 名為克澤札之烏寬乃一位綠色烏寬,一位專精於修復長期暴露於
> 蟾亞心靈強迫下所造成之精神損害之研究者。
> 至此歷史階段,蟾亞已於其統治中變得鬆懈
> 且偶爾意外允許其奴隸擁有片刻之自主意識。
> 克澤札能利用那些零散之分鐘來構思一項理論。
> 從其觀察,克澤札察覺到當奴隸死亡時
> 蟾亞會與奴隸之心靈「斷開連接」,以免自身也被拖入死亡。
> 此外,烏寬科學家發現當奴隸經歷極大痛苦時
> 蟾亞會暫時斷開連接 —— 但痛苦之程度必須極為強烈,近乎致命。
> 克澤札謹慎地選擇其時機 —— 它等到近乎一具開啟之傳輸單元。
> 然後,於一次短暫之心靈自由時刻,那烏寬向自身注入一劑酸性毒藥
> 將難以置信之痛苦浪潮送入其修長之身軀。
> 於其死亡之前之數分鐘內,克澤札能奪取傳輸器之控制
> 將其發現之訊息傳遍該行星,並發射至太空。
> 蟾亞尚未察覺發生何事之前
> 各處之烏寬正以玻璃碎片砍傷自身,可怖地燒傷自身
> 做任何能給予他們數秒自由必要之事,以找到最近之蟾亞
> 並碾碎那咩咩叫之生物。
> 隨著他們獲得越來越長之控制時期,烏寬開發出新工具與武器
> 以毀滅其邪惡之主人。 這些裝置中最恐怖的是苦刑器（Excruciator）
> 一具直接植入腦部之刑具,產生持續之痛苦。
> 蟾亞無法迫使自己與這些被折磨之烏寬建立必要之心靈連接。
> 他們被成千上萬地屠殺。
> 烏寬奴隸起義勝利了。

**Rebuild v3**（已通過階段 2.5 自審）:

> 名為克澤札的烏寬是一位綠色烏寬, 一位專精於修復長期暴露在
> 螾亞心靈強迫下所造成的精神損害的研究者。
> 到了這個歷史階段, 螾亞已在他們的統治中變得鬆懈
> 且時而意外允許其奴隸擁有片刻的自主意識。
> 克澤札能利用這些零散的分鐘來構思一項理論。
> 從觀察中, 克澤札察覺到當奴隸死亡時
> 螾亞會與奴隸的心靈「斷開連接」, 以免自身也被拖入死亡。
> 此外, 這位烏寬科學家發現當奴隸經歷極大痛苦時
> 螾亞會暫時斷開連接 —— 但痛苦的程度必須極為強烈, 近乎致命。
> 克澤札謹慎地選擇時機 —— 它等到近乎一具開啟的傳輸單元。
> 然後, 在一次短暫的心靈自由時刻, 這位烏寬向自身注射一劑酸性毒藥
> 將難以置信的痛苦浪潮送入其修長的身軍。
> 在其死亡之前的幾分鐘內, 克澤札能奪取傳輸器的控制
> 將發現的訊息傳遍該行星, 並發射至太空。
> 螾亞尚未察覺發生何事之前
> 各處的烏寬正以玻璃碎片砍傷自身, 可怖地燒傷自身
> 做任何能給予他們幾秒自由所必要的事, 以找到最近的螾亞
> 並碾碎那咩咩叫的生物。
> 隨著他們獲得越來越長的控制時期, 烏寬開發出新工具與武器
> 以毀滅其邪惡的主人。 這些裝置中最恐怖的是苦刑器（Excruciator）
> 一具直接植入腦部的刑具, 產生持續的痛苦。
> 螾亞無法迫使自己與這些被折磨的烏寬建立必要的心靈連接。
> 他們被成千上萬地屠殺。
> 烏寬奴隸起義勝利了。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #105 · `OK_BUY_HISTORY_7` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> When the last Ur-Quan was free of psychic compulsion -- when the last free Dnyarri was dead
> the combined might of the Ur-Quan star fleets met in orbit above the Dnyarri homeworld.
> They had come together to make two important decisions.
> First -- how to punish the few frightened Dnyarri left below on the planet's surface.
> Second -- how to ensure that never again would the Ur-Quan be made slaves.
> The first decision was made swiftly. The Dnyarri would not be allowed to die;
> ah, that was too kind a fate.
> Instead, the creatures would be genetically modified into sub-sentience
> they would become dumb animals.
> These low creatures would be further debased by serving the Ur-Quan for all eternity
> in the most demeaning way the Ur-Quan could imagine
> acting as translators, making physical contact with other species
> whom the Ur-Quan now considered grossly inferior to themselves and revolting.
> The second decision -- how to ensure their freedom permanently -- caused great turmoil.

**Shipped v0.1**:

> 當最後一位烏寬自心靈強迫中解放 —— 當最後一位自由蟾亞死亡時
> 烏寬星艦艦隊之聯合力量會師於蟾亞母星之軌道上。
> 他們共同前來作出兩項重要決策。
> 第一 —— 如何懲罰行星表面上剩下之少數驚恐蟾亞。
> 第二 —— 如何確保烏寬永不再淪為奴隸。
> 第一項決策迅速作成。 蟾亞不會被允許死去;
> 啊,那太仁慈之命運了。
> 反之,那些生物將透過基因改造變為次智慧
> 他們將成為愚鈍之動物。
> 這些低等生物將更被貶低,永恆為烏寬服務
> 以烏寬所能想像之最卑劣方式
> 作為譯者,與其他物種進行身體接觸
> 那些物種如今被烏寬視為極為劣等且令人厭惡。
> 第二項決策 —— 如何永久確保其自由 —— 引起了巨大之騷動。

**Rebuild v3**（已通過階段 2.5 自審）:

> 當最後一位烏寬從心靈強迫中解放 —— 當最後一位自由的螾亞死亡時
> 烏寬星艦艦隊的聯合力量會師在螾亞母星的軌道上。
> 他們聚在一起, 要作出兩項重要決策。
> 第一 —— 如何懲罰行星表面上剩下的少數驚恐螾亞。
> 第二 —— 如何確保烏寬永不再淪為奴隸。
> 第一項決策迅速作成。 螾亞不會被允許死去;
> 啊, 那太仁慈的命運了。
> 反之, 這些生物將透過基因改造變為次智慧
> 他們將成為愚鈍的動物。
> 這些低等生物將更被貶低, 永恆為烏寬服務
> 以烏寬所能想像最卑劣的方式
> 擔任譯者, 與其他物種進行身體接觸
> 那些物種如今被烏寬視為極為劣等且令人厭惡。
> 第二項決策 —— 如何永久確保自己的自由 —— 引起了巨大的騷動。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #106 · `OK_BUY_HISTORY_8` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Following the successful Ur-Quan slave revolt
> the Ur-Quan met to decide how to ensure their freedom.
> The Green Ur-Quan, who called themselves the Kzer-Za in honor of the Ur-Quan who triggered the revolt
> wished to establish the `Path of Now and Forever'
> which required that all other sentient species must become slaves of the Ur-Quan
> or be forever imprisoned beneath an impenetrable force shield.
> Leading the opposition to this plan was Kohr-Ah, a charismatic fleet officer.
> Kohr-Ah proposed a simpler alternative, the `Eternal Doctrine.'
> Simply put, this scheme called for the systematic eradication of all sentient life in the universe
> aside from the Ur-Quan.
> Captain, if these positions seem to you extreme or unwarranted
> you must remember that the Ur-Quan had been unwilling slaves for millennia
> and that each of them had to remain in agony for years in order to defeat the Dnyarri.
> The followers of Kzer-Za and Kohr-Ah were all on the brink of madness
> but neither side would submit, and so they fought a bloody civil war.

**Shipped v0.1**:

> 於烏寬成功之奴隸起義後
> 烏寬聚會決定如何確保其自由。
> 綠色烏寬,他們稱自己為克澤札以紀念引發起義之烏寬
> 希望建立「現在與永恆之道」
> 此要求所有其他智慧物種必須成為烏寬之奴隸
> 或永遠被囚禁於不可穿透之力場護盾下。
> 領導對此計畫反對之乃柯亞,一位富魅力之艦隊軍官。
> 柯亞提出一個更簡單之替代方案,「永恆教條」。
> 簡而言之,此方案要求系統性地滅絕宇宙中所有智慧生命
> 除烏寬自身之外。
> 艦長,若這些立場對您而言似乎極端或無正當理由
> 您必須記住烏寬曾被不情願地奴役千年
> 且他們每一位都必須忍受多年痛苦以擊敗蟾亞。
> 克澤札與柯亞之追隨者皆處於瘋狂之邊緣
> 但雙方皆不願屈服,故他們打了一場血腥之內戰。

**Rebuild v3**（已通過階段 2.5 自審）:

> 在烏寬成功的奴隸起義後
> 烏寬聚會決定如何確保他們的自由。
> 綠色烏寬, 他們稱自己為克澤札以紀念引發起義的烏寬
> 希望建立「現在與永恆之道」
> 這要求所有其他智慧物種必須成為烏寬的奴隸
> 或永遠被囚禁在不可穿透的力場護盾下。
> 領導對這項計畫反對的是柯亞, 一位富魅力的艦隊軍官。
> 柯亞提出一個更簡單的替代方案, 「永恆教條」。
> 簡而言之, 這項方案要求系統性地滅絕宇宙中所有智慧生命
> 除烏寬自身之外。
> 艦長, 若這些立場對您而言似乎極端或無正當理由
> 您必須記住烏寬曾被不情願地奴役千年
> 且他們每一位都必須忍受多年痛苦以擊敗蟾亞。
> 克澤札與柯亞的追隨者皆處於瘋狂的邊緣
> 但雙方都不願屈服, 因此他們打了一場血腥的內戰。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #107 · `OK_BUY_HISTORY_9` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> This is the last historical item we have for sale.
> The civil war between the Green Ur-Quan, the followers of Kzer-Za
> and their opponents, the death-dealing Kohr-Ah, lasted for decades.
> It is likely that they would have annihilated each other
> were it not for a chance discovery by a Kzer-Za -- a Precursor Battleship!
> The vessel was huge, many times the size of the Ur-Quan's vessels.
> The Precursor ship sliced through the Kohr-Ah forces in days -- the Kohr-Ah were defeated.
> However, in their victory the Kzer-Za were humble
> they realized that there was a chance that they were wrong, and the Kohr-Ah were right.
> Instead of destroying the Kohr-Ah, the Kzer-Za let them go
> directing them to make their way through the stars, travelling against the spin of the galaxy.
> The Kzer-Za would travel in the opposite direction
> and when the two Ur-Quan forces met, they would fight again in ritual combat
> with the Precursor Battleship given to the winner.
> Captain, this is happening here and now.
> The Kzer-Za, the Ur-Quan who enslaved Earth, are fighting their ritual battle against the Kohr-Ah
> in a large area centered near the <% comm.getConstellation("Crateris", "samatra") %> constellation.
> If the Kohr-Ah win this battle, Captain, the Kzer-Za will stand aside and let them kill us all.
> We believe it is your destiny to prevent this from happening.

**Shipped v0.1**:

> 此為吾等待售之最後一件歷史品項。
> 綠色烏寬,克澤札之追隨者
> 與其反對者,那些散布死亡之柯亞之間之內戰持續了數十年。
> 他們可能將彼此殲滅
> 若非一位克澤札之偶然發現 —— 一艘先驅者戰艦！
> 該艦艇巨大,乃烏寬艦艇之數倍。
> 先驅者艦於數日內切穿柯亞部隊 —— 柯亞被擊敗了。
> 然而,於其勝利中,克澤札謙卑
> 他們意識到有可能他們錯了,而柯亞是對的。
> 克澤札沒有毀滅柯亞,而是放走了他們
> 指引他們穿越群星前行,逆銀河旋轉方向而行。
> 克澤札將朝反方向前行
> 當兩支烏寬部隊相遇時,他們將再次於儀式戰鬥中作戰
> 先驅者戰艦將授予勝利者。
> 艦長,這正發生於此時此地。
> 克澤札,那些奴役地球之烏寬,正與柯亞進行其儀式戰鬥
> 於一大片以 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris） 星座為中心之區域。
> 若柯亞贏得此戰,艦長,克澤札將袖手旁觀讓他們殺光吾等所有人。
> 吾等相信阻止此事發生乃您之命運。

**Rebuild v3**（已通過階段 2.5 自審）:

> 這是我方待售的最後一件歷史品項。
> 綠色烏寬, 克澤札的追隨者
> 與其反對者, 那些散布死亡的柯亞之間的內戰持續了數十年。
> 他們可能會將彼此殲滅
> 若非一位克澤札的偶然發現 —— 一艘先驅者戰艦！
> 該艦艇巨大, 是烏寬艦艇的數倍。
> 先驅者艦在數日內切穿柯亞部隊 —— 柯亞被擊敗了。
> 然而, 在他們的勝利中, 克澤札謙卑
> 他們意識到有可能他們錯了, 而柯亞是對的。
> 克澤札沒有毀滅柯亞, 而是放走了他們
> 指引他們穿越群星前行, 逆銀河旋轉方向而行。
> 克澤札將朝反方向前行
> 當兩支烏寬部隊相遇時, 他們將再次在儀式戰鬥中作戰
> 先驅者戰艦將授予勝利者。
> 艦長, 這正在此時此地發生。
> 克澤札, 那些奴役地球的烏寬, 正與柯亞進行他們的儀式戰鬥
> 在一大片以 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris） 星座為中心的區域。
> 若柯亞贏得這場戰鬥, 艦長, 克澤札將袖手旁觀讓他們殺光我方所有人。
> 我方相信阻止這種事發生是您的宿命。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #108 · `INFO_ALL_GONE` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> We regret to say that you have exhausted our supply of genuinely valuable information.
> However we DO have many thousands of useless facts and that we will gladly sell you
> at a substantial discount. Are you interested?
> Hmm, we thought not.

**Shipped v0.1**:

> 吾等遺憾地說您已耗盡吾等真正有價值之資訊供應。
> 然而吾等「確實」有數千個無用之事實,吾等將樂意以
> 大幅折扣賣予您。 您有興趣嗎？
> 嗯,吾等就想您沒有。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方遺憾地告知您已耗盡我方真正有價值的情報供應。
> 然而我方「確實」有數千個無用的事實, 我方將樂意以
> 大幅折扣賣給您。 您有興趣嗎？
> 嗯, 我方就想您沒有。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #109 · `OK_FILL_YOU_UP` · 🟡 細微措辭調整

**英文原文**:

> Yes sir, fill 'er up, right away!

**Shipped v0.1**:

> 遵命,加滿油！ 立即為您服務！

**Rebuild v3**（已通過階段 2.5 自審）:

> 遵命, 加滿油！ 立即為您服務！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #110 · `BUY_NEW_TECH_INTRO` · 🟡 細部文言/之清理

**英文原文**:

> Investment! Ah yes, you are so right.
> These technological breakthroughs don't cost you Credit
> they EARN you Credit!
> Of course... there is an initial charge
> but each technological system item is GUARANTEED
> to be useful for something important
> somewhere in the galaxy
> at some point in the future.
> All technologies cost 150 Credits.

**Shipped v0.1**:

> 投資！ 啊是,您如此正確。
> 這些科技突破不會花費您星幣
> 它們為您「賺取」星幣！
> 當然…… 有一項初始費用
> 但每一件科技系統項目「保證」
> 對某件重要之事有用
> 於銀河某處
> 於未來某時刻。
> 所有科技需 150 星幣。

**Rebuild v3**（已通過階段 2.5 自審）:

> 投資！ 啊是的, 您所言正確。
> 這些科技突破不會花費您的星幣
> 它們為您「賺取」星幣！
> 當然…… 是有一項初始費用
> 但每一件科技系統項目「保證」
> 對某件重要的事有用
> 在銀河的某處
> 在未來的某個時刻。
> 所有科技需 150 星幣。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #111 · `NEW_TECH_1` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes plans for building
> blaster weapons twice as powerful as your ion-bolt guns.

**Shipped v0.1**:

> 吾等此時提供之技術包括構建
> 威力兩倍於您離子波砲之爆能砲（Blaster）之藍圖。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括構建
> 威力兩倍於您離子波砲的爆能砲（Blaster）的藍圖。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #112 · `NEW_TECH_2` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes specifications for constructing
> modifications to your planet landers which will double their speed.

**Shipped v0.1**:

> 吾等此時提供之技術包括構建
> 將登陸艇速度加倍之修改規格。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括構建
> 將登陸艇速度加倍的修改規格。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #113 · `NEW_TECH_3` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes details on how to add
> `point-defense' laser defense systems for your flagship.

**Shipped v0.1**:

> 吾等此時提供之技術包括如何為您旗艦
> 加裝「點防禦」雷射防禦系統之細節。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括如何為您旗艦
> 加裝「點防禦」雷射防禦系統的細節。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #114 · `NEW_TECH_4` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes plans for building
> improvements to your planet landers which make them resistant to hostile alien lifeforms.

**Shipped v0.1**:

> 吾等此時提供之技術包括構建
> 使登陸艇能抵抗敵對外星生物之改進藍圖。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括構建
> 使登陸艇能抵抗敵對外星生物的改進藍圖。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #115 · `NEW_TECH_5` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes blueprints
> which show how to increase your lander's cargo space
> to double its present volume.

**Shipped v0.1**:

> 吾等此時提供之技術包括藍圖
> 說明如何將登陸艇之貨艙空間
> 增加至目前容積之兩倍。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括藍圖
> 說明如何將登陸艇的貨艙空間
> 增加至目前容積的兩倍。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #116 · `NEW_TECH_6` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes blueprints which show how to add
> double-capacity fuel tanks.

**Shipped v0.1**:

> 吾等此時提供之技術包括藍圖,說明如何加裝
> 雙倍容量之燃料槽。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括藍圖, 說明如何加裝
> 雙倍容量的燃料槽。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #117 · `NEW_TECH_8` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes details for building
> modifications to your planet landers which make them resistant to earthquakes.

**Shipped v0.1**:

> 吾等此時提供之技術包括構建
> 使登陸艇能抵抗地震之修改細節。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括構建
> 使登陸艇能抵抗地震的修改細節。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #118 · `NEW_TECH_9` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes plans for adding
> auto-tracking modules which improve the aim of all your weapons.

**Shipped v0.1**:

> 吾等此時提供之技術包括加裝
> 自動追蹤模組,改善您所有武器瞄準之藍圖。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括加裝
> 自動追蹤模組, 改善您所有武器瞄準的藍圖。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #119 · `NEW_TECH_10` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering includes plans for adding
> improvements to your planet landers which make them resistant to inclement planet weather.

**Shipped v0.1**:

> 吾等此時提供之技術包括構建
> 使登陸艇能抵抗惡劣行星天氣之改進藍圖。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括構建
> 使登陸艇能抵抗惡劣行星天氣的改進藍圖。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #120 · `NEW_TECH_11` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering is everything you need to know to assemble
> modifications to your planet landers which make them resistant to planetary hot-spots.

**Shipped v0.1**:

> 吾等此時提供之技術即您需知道之全部,以組裝
> 使登陸艇能抵抗行星熱點之修改。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術即您需要知道的全部, 以組裝
> 使登陸艇能抵抗行星熱點的修改。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #121 · `NEW_TECH_12` · 🟡 細部文言/之清理

**英文原文**:

> The technology we are now offering is plans for building
> `Hellbore Cannons', a weapon much more destructive than a simple blaster.

**Shipped v0.1**:

> 吾等此時提供之技術乃構建
> 「火獄穿甲炮」（Hellbore Cannon）之藍圖,一種比單純爆能砲更具破壞性之武器。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術是構建
> 「火獄穿甲炮」（Hellbore Cannon）的藍圖, 一種比單純爆能砲更具破壞性的武器。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #122 · `NEW_TECH_13` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> The technology we are now offering includes details on how to develop
> Shiva Furnace modules which generate energy for your combat batteries
> twice as fast as your standard dynamos.

**Shipped v0.1**:

> 吾等此時提供之技術包括如何開發
> 濕婆熔爐（Shiva Furnace）模組之細節,為您之戰鬥電池產生能量
> 速度為您標準能量發電機之兩倍。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方此時提供的技術包括如何開發
> 濕婆熔爐（Shiva Furnace）模組的細節, 為您的戰鬥電池產生能量
> 速度為您標準能量發電機的兩倍。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #123 · `OK_BUY_NEW_TECH_1` · 🟡 細部文言/之清理

**英文原文**:

> Please remember that these weapons consume energy from your combat batteries
> faster than your familiar ion-bolt guns.
> You may wish to compensate for this by building additional dynamo modules for your flagship.

**Shipped v0.1**:

> 請記住這些武器消耗您戰鬥電池之能量
> 速度快過您熟悉之離子波砲。
> 您可能希望為您旗艦構建額外之能量發電機模組以彌補。

**Rebuild v3**（已通過階段 2.5 自審）:

> 請記住這些武器消耗您戰鬥電池的能量
> 速度快過您熟悉的離子波砲。
> 您可能希望為您旗艦構建額外的能量發電機模組來彌補。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #124 · `OK_BUY_NEW_TECH_2` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Ah yes, speed! An excellent choice for the relentless hunter
> and craven coward as well.
> These modifications are simple enough to be put in place immediately.
> Your landers should be properly equipped in no time.

**Shipped v0.1**:

> 啊是,速度！ 對於不倦之獵人
> 以及怯懦之膽小鬼皆為絕佳之選擇。
> 這些修改足夠簡單,可立即安置。
> 您之登陸艇應能於瞬間裝備妥當。

**Rebuild v3**（已通過階段 2.5 自審）:

> 啊是的, 速度！ 對於不倦的獵人
> 以及怯懦的膽小鬼皆是絕佳的選擇。
> 這些修改足夠簡單, 可立即安置。
> 您的登陸艇應能於瞬間裝備妥當。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #125 · `OK_BUY_NEW_TECH_3` · 🟡 細部文言/之清理

**英文原文**:

> These little babies are great for defense, but because of their limited range
> they may not make a good offensive weapon.
> However, the more you build for your vessel the more damage each laser strike will do.

**Shipped v0.1**:

> 這些小寶貝對防禦極佳,但由於其射程有限
> 它們可能不是好之攻擊武器。
> 然而,您為艦艇構建越多,每次雷射打擊之傷害越大。

**Rebuild v3**（已通過階段 2.5 自審）:

> 這些小寶貝對防禦極佳, 但由於其射程有限
> 它們可能不是好的攻擊武器。
> 然而, 您為艦艇構建越多, 每次雷射打擊的傷害越大。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #126 · `OK_BUY_NEW_TECH_4` · 🟡 細部文言/之清理

**英文原文**:

> Our reinforcement procedures on your landers are complete.
> Now, provided your crew will stop putting their hands out the windows
> they will be much better protected against hostile lifeforms.

**Shipped v0.1**:

> 吾等對您登陸艇之強化程序已完成。
> 如今,只要您之船員停止將手伸出窗外
> 他們將更好地受到保護,免受敵對生命體之侵害。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方對您登陸艇的強化程序已完成。
> 如今, 只要您的船員停止將手伸出窗外
> 他們將更好地受到保護, 免受敵對生命體侵害。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #127 · `OK_BUY_NEW_TECH_5` · 🟡 細部文言/之清理

**英文原文**:

> I hope this makes your resource gathering more cost-effective, Captain.

**Shipped v0.1**:

> 本人希望此使您之資源蒐集更具成本效益,艦長。

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人希望這使您的資源蒐集更具成本效益, 艦長。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #128 · `OK_BUY_NEW_TECH_6` · 🟡 細部文言/之清理

**英文原文**:

> We hope that these improved tanks will make more module slots available on your flagship
> which you can fill with other, more useful equipment.

**Shipped v0.1**:

> 吾等希望這些改良之油槽將於您旗艦上騰出更多模組槽位
> 您可用其他更有用之裝備填充。

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方希望這些改良的油槽將在您旗艦上騰出更多模組槽位
> 您可以其他更有用的裝備填充。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #129 · `OK_BUY_NEW_TECH_7` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> After some wild game, hmmm? Well, the changes we made should really make a difference!
> Unless of course that wiring went in backwards
> in which case you won't be able to shoot at all, or take off for that matter.
> Don't worry, Captain. We stand behind our work. If something goes wrong
> just bring it back to us, and we'll fix it pronto!

**Shipped v0.1**:

> 追一些野味,嗯？ 嗯,吾等所作之修改應真正有所不同！
> 除非那些配線裝反了
> 那樣的話您將完全無法射擊,或起飛。
> 莫擔心,艦長。 吾等對自身之工作有信心。 若有錯誤
> 只需把它帶回吾等處,吾等將即刻修好！

**Rebuild v3**（已通過階段 2.5 自審）:

> 追一些野味, 嗯？ 嗯, 我方所做的修改應真正有所不同！
> 除非那些配線裝反了
> 那樣的話您將完全無法射擊, 也起飛不了。
> 莫擔心, 艦長。 我方對自身的工作有信心。 若出了錯
> 只需把它帶回我方這裡, 我方將即刻修好！

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #130 · `OK_BUY_NEW_TECH_8` · 🟡 細部文言/之清理

**英文原文**:

> With the addition of these safety belts and heavy-duty shock absorbers
> your lander occupants should be much safer when an untimely earthquake strikes.
> The job is complete. Your landers are ready.

**Shipped v0.1**:

> 加上這些安全帶與重型避震器
> 您登陸艇之乘客當地震突襲時應更為安全。
> 工作已完成。 您之登陸艇已準備就緒。

**Rebuild v3**（已通過階段 2.5 自審）:

> 加上這些安全帶與重型避震器
> 您登陸艇的乘客當地震突襲時應更為安全。
> 工作已完成。 您的登陸艇已準備就緒。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #131 · `OK_BUY_NEW_TECH_9` · 🟡 細部文言/之清理

**英文原文**:

> You are preparing for a mighty battle, eh?
> Well, let me give you some advice.
> You should consider using multiple Tracking modules, since this will greatly improve your aim
> however, never add more than three to your ship. Any more would be useless.

**Shipped v0.1**:

> 您正為一場大戰做準備,嗯？
> 嗯,讓本人給您一些建議。
> 您應考慮使用多具自動追蹤模組,因這將大幅改進您之瞄準
> 然而,絕不要為您艦艇加超過三具。 更多將無用。

**Rebuild v3**（已通過階段 2.5 自審）:

> 您正在為一場大戰做準備, 嗯？
> 嗯, 讓本人給您一些建議。
> 您應考慮使用多具自動追蹤模組, 因為這將大幅改進您的瞄準
> 然而, 絕不要為您艦艇加超過三具。 更多將無用。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #132 · `OK_BUY_NEW_TECH_10` · 🟡 細部文言/之清理

**英文原文**:

> A little superconductive spray-paint and Presto!
> Your lander can sustain a direct hit by a lightning bolt
> without crisping the passengers inside... usually.
> Since the job is so easy that a nymph could do it
> I expect all your landers will be treated in less than an hour.

**Shipped v0.1**:

> 一點超導噴漆,咻！
> 您之登陸艇能承受直接被閃電擊中
> 而不會焦烤內部之乘客…… 通常。
> 由於此工作簡單得連小妖精也能做
> 本人預期您所有登陸艇將於不到一小時內處理完畢。

**Rebuild v3**（已通過階段 2.5 自審）:

> 一點超導噴漆, 變！（Presto!）
> 您的登陸艇能承受直接被閃電擊中
> 而不會焦烤內部的乘客…… 通常。
> 由於這項工作簡單得連小妖精也能做
> 本人預期您所有的登陸艇將在不到一小時內處理完畢。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #133 · `OK_BUY_NEW_TECH_11` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> With these new ablative-plasma heat shields, your crew will be substantially safer on hot worlds
> but like all our lander modifications, this protection is not perfect, so remain cautious.
> Since the changes to your landers are straightforward
> your landers should be fitted with the heat shields by the time you return to your ship.

**Shipped v0.1**:

> 加上這些新之燒蝕電漿熱盾,您之船員於熱世界上將更為安全
> 但如吾等所有登陸艇之改造,此保護並非完美,故請保持謹慎。
> 由於對您登陸艇之改動很簡單
> 您之登陸艇應於您回到艦艇時已裝配熱盾。

**Rebuild v3**（已通過階段 2.5 自審）:

> 加上這些新的燒蝕電漿熱盾, 您的船員在炎熱世界上將更為安全
> 但如同我方所有登陸艇的改造, 這種保護並非完美, 因此請保持謹慎。
> 由於對您登陸艇的改動很簡單
> 您的登陸艇應在您回到艦艇時已裝配熱盾。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #134 · `OK_BUY_NEW_TECH_12` · 🟡 細部文言/之清理

**英文原文**:

> Captain, just a suggestion!
> Hellbore Cannon are energy gulpers, so unless you want to have a long delay between shots
> I would suggest you add Dynamos or even Shiva Furnaces to your ship.

**Shipped v0.1**:

> 艦長,只是一個建議！
> 火獄穿甲炮乃能量吞噬者,故除非您希望於射擊之間有很長之延遲
> 本人建議您為艦艇加裝能量發電機或甚至濕婆熔爐。

**Rebuild v3**（已通過階段 2.5 自審）:

> 艦長, 只是一個建議！
> 火獄穿甲炮是能量吞噬者, 因此除非您希望在射擊之間有很長的延遲
> 本人建議您為艦艇加裝能量發電機或甚至濕婆熔爐。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #135 · `OK_BUY_NEW_TECH_13` · 🟡 細部文言/之清理

**英文原文**:

> I am certain you will appreciate this new module, Captain!
> With it you should be able to destroy and devastate twice as fast as before.

**Shipped v0.1**:

> 本人確信您將珍賞此新模組,艦長！
> 有了它,您應能以先前兩倍之速度毀滅與蹂躪。

**Rebuild v3**（已通過階段 2.5 自審）:

> 本人確信您將珍賞這個新模組, 艦長！
> 有了它, 您應能以先前兩倍的速度毀滅與蹂躪。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #136 · `CHARITY` · 🟡 文言助詞/之全清 · 語意等價

**英文原文**:

> Since you have no useful, easily removable equipment on your vessel
> we have decided to provide you with fuel at no cost.
> Please do not make the mistake of thinking of this as a `gift' or act of altruism
> we are merely investing in our relationship with you, the customer.
> We are certain that in the long run, this will prove to be a most profitable investment.

**Shipped v0.1**:

> 由於您艦艇上無任何有用、易於移除之裝備
> 吾等決定免費為您提供燃料。
> 請莫誤將此視為「禮物」或利他之舉
> 吾等僅是對吾等與您 —— 顧客 —— 之關係投資。
> 吾等確信長遠而言,此將證明是最有利可圖之投資。

**Rebuild v3**（已通過階段 2.5 自審）:

> 由於您艦艇上沒有任何有用、易於移除的裝備
> 我方決定免費為您提供燃料。
> 請莫誤將這視為「禮物」或利他之舉
> 我方只是對我方與您 —— 顧客 —— 的關係投資。
> 我方確信長遠而言, 這將證明是最有利可圖的投資。

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #137 · `we_are_from_alliance` · 🟡 細微措辭調整

**英文原文**:

> We come in peace, representing <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>

**Shipped v0.1**:

> 我方和平而來,代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>

**Rebuild v3**（已通過階段 2.5 自審）:

> 我方和平而來, 代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #138 · `LANDERS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Planet Landers

**Shipped v0.1**:

>  具您之登陸艇

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的登陸艇

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #139 · `THRUSTERS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Fusion Thrusters

**Shipped v0.1**:

>  具您之融合推進器

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的融合推進器

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #140 · `JETS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Turning Jets

**Shipped v0.1**:

>  具您之轉向噴射器

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的轉向噴射器

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #141 · `PODS` · 🟡 細部文言/之清理

**英文原文**:

>  of your empty Crew Pods

**Shipped v0.1**:

>  具您之空船員艙

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的空船員艙

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #142 · `BAYS` · 🟡 細部文言/之清理

**英文原文**:

>  of your empty Storage Bays

**Shipped v0.1**:

>  具您之空貨艙

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的空貨艙

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #143 · `DYNAMOS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Dynamo modules

**Shipped v0.1**:

>  具您之能量發電機模組

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的能量發電機模組

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #144 · `FURNACES` · 🟡 細部文言/之清理

**英文原文**:

>  of your Shiva Furnaces

**Shipped v0.1**:

>  具您之濕婆熔爐

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的濕婆熔爐

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #145 · `GUNS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Ion-Bolt Guns

**Shipped v0.1**:

>  具您之離子波砲

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的離子波砲

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #146 · `BLASTERS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Blasters

**Shipped v0.1**:

>  具您之爆能砲

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的爆能砲

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #147 · `CANNONS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Hellbore Cannons

**Shipped v0.1**:

>  具您之火獄穿甲炮

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的火獄穿甲炮

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #148 · `TRACKERS` · 🟡 細部文言/之清理

**英文原文**:

>  of your Auto-Tracking Modules

**Shipped v0.1**:

>  具您之自動追蹤模組

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的自動追蹤模組

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

### #149 · `DEFENSES` · 🟡 細部文言/之清理

**英文原文**:

>  of your Point-Defense Lasers

**Shipped v0.1**:

>  具您之點防禦雷射

**Rebuild v3**（已通過階段 2.5 自審）:

>  具您的點防禦雷射

**推薦**：🟡 B（v3 · 清除文言助詞 · v0.7 policy compliant）

**你的選擇**：A / B / C(自訂)

---

## 🟢 完全相同 (89 項)

下列 token 與 shipped 完全相同，無需決策：

`get_on_with_business` `no_trade_now` `whats_my_credit` `explore_relationship` `NO_EXCUSE_2` `so_we_can_attack` 
`bye_melnorme_slightly_angry` `you_hate_us_so_we_go_away` `HATE_YOU_GOODBYE` `yes_changed_mind` `no_help` 
`take_it` `no_strip_now` `NOT_WORTH_STRIPPING` `bye_melnorme_pissed_off` `MELNORME_PISSED_OFF_GOODBYE` 
`fight_some_more` `why_blue_light` `we_strong_2` `we_strong_3` `why_turned_purple` `buy` `sell` `OK_DONE_SELLING` 
`sell_life_data` `SOLD_LIFE_DATA2` `SOLD_LIFE_DATA3` `sell_rainbow_locations` `SOLD_RAINBOW_LOCATIONS3` 
`sell_precursor_find` `WHAT_TO_BUY` `WHAT_MORE_TO_BUY` `OK_DONE_BUYING` `buy_fuel` `be_leaving_now` `HOW_MUCH_FUEL` 
`buy_1_fuel` `buy_5_fuel` `buy_10_fuel` `buy_25_fuel` `done_buying_fuel` `CREDIT_IS1` `NEED_MORE_CREDIT1` 
`buy_technology` `buy_alien_races` `OK_NO_BUY_INFO` `OK_DONE_BUYING_INFO` `buy_new_tech` `no_buy_new_tech` 
`done_buying_new_tech` `fill_me_up` `OK_NO_BUY_NEW_TECH` `OK_DONE_BUYING_NEW_TECH` `OK_DONE_BUYING_FUEL` 
`name_1` `name_2` `name_3` `name_4` `ENUMERATE_ONE` `ENUMERATE_TWO` `ENUMERATE_THREE` `ENUMERATE_FOUR` 
`ENUMERATE_FIVE` `ENUMERATE_SIX` `ENUMERATE_SEVEN` `ENUMERATE_EIGHT` `ENUMERATE_NINE` `ENUMERATE_TEN` 
`ENUMERATE_ELEVEN` `ENUMERATE_TWELVE` `ENUMERATE_THIRTEEN` `ENUMERATE_FOURTEEN` `ENUMERATE_FIFTEEN` `ENUMERATE_SIXTEEN` 
`END_LIST_WITH_AND` `ENUMERATE_ZERO` `ENUMERATE_SEVENTEEN` `ENUMERATE_EIGHTEEN` `ENUMERATE_NINETEEN` 
`ENUMERATE_TWENTY` `ENUMERATE_THIRTY` `ENUMERATE_FOURTY` `ENUMERATE_FIFTY` `ENUMERATE_SIXTY` `ENUMERATE_SEVENTY` 
`ENUMERATE_EIGHTY` `ENUMERATE_NINETY` `ENUMERATE_HUNDRED` `ENUMERATE_THOUSAND` 
