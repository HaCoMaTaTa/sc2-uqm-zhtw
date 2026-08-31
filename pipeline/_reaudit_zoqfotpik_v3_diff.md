# Zoq-Fot-Pik Rebuild-Compare Diff Report (2026-08-17)

**v0.7 clean-room v3 vs shipped v0.5.2 (Round 3, 2026-08-11)**

**產出**：`uqm-work/translations/zoqfotpik.zh-TW.v3.json` (334 tokens)
**Backup**：`uqm-work/translations/zoqfotpik.zh-TW.pre-rebuild.bak`

## 統計

- Total tokens: 334
- 🟢 完全相同: 70 (21.0%)
- 🟡 微調（等價 / voice cleanup）: 90 (26.9%)
- 🟠 措辭改變: 53 (15.9%)
- 🔴 語意/voice 差異大: 11 (3.3%)
- ✨ voice/canonical 升級（文言→白話等）: 110 (32.9%)
- ⚙ 階段 2.5 Read-Aloud self-fix（僅資訊）: 7 (2.1%) （**已直接應用於 v3** · 詳 `_selfaudit_zoqfotpik_v3_readaloud.md`）

## Q&A 決策鎖 (使用者已回覆 2026-08-17)

| # | 決策 | 內容 |
|---|---|---|
| Q1 | **A** | canonical 全採 Master_Glossary v0.5.2 (=shipped): 芙戎奇/嘿嘿嘿(Nyark)/澤布蘭基/刺針號/尊貴至極的波霸大人/葉普-屯-哈菲-吉夫-佛德-羅吉-布波/森林朱克獸-樹頂納夫獸-多爾夫 |
| Q2 | **A** | 集體自稱 palette 分配 (我們/我們佐-佛-皮/咱們/佐-佛-皮) |
| Q3 | **A/B=我** | 單方一律「我」 |
| Q4 | **全依規則** | 全清吾/吾等/爾/之/乃/哉/兒（不含 modern 之前/之後/canonical 諸王之運動/哥兒們等） |
| Q5 | **OK** | 三方拌嘴 icon = 無前綴換行 (shipped 已符合) |
| Q6 | **A** | Fortunately/Unfortunately 保留「幸運的是……/不幸的是……」 |
| Q7 | **全保留** | Alliance name_1-4 全繼承 shipped |
| Q8 | **A** | we_are_vindicator = 「我方是 X 旗艦『Y』」正式感 |
| Q9 | **B** | 玩家 response 情境切換 (嗆聲=老子/正式=我方/提問=我) |
| Q10 | **A** | OUT_TAKES Did not/Did too 保留「才沒有！/就有！」 |
| Q11 | **B** | quiet_toadies = 老子語氣嗆聲 |
| Q12 | **A** | Frungy 錦標賽段落結構保留 shipped |
| Q13 | **A** | SCOUT_HELLO1 座標系笑話保留 shipped canonical |
| Q14 | **A** | 「偉大晶智族」保留 |
| Q15 | **A** | 7 批 × ~48 tokens 分批 clean-room |
| Q16 | **A** | Read-Aloud 完整自審（7 self-fix 已直接應用） |

## 3-Gate Verify (2026-08-17)

- **Gate 1 Purity**: PASS (race=0, simp=0, variant=0, tokens=0)
- **Gate 2 Line-count**: PASS (334/334 tokens match EN source)
- **Gate 3 Lua template**: PASS (0 English residual)

## 污染清除量化

| 文言助詞 | shipped v0.5.2 | v3 | Δ |
|---|---|---|---|
| 吾 | 157 | 0 | -157 |
| 吾等 | 155 | 0 | -155 |
| 爾 | 5 | 3 | -2 |
| 汝 | 0 | 0 | +0 |
| 之 | 43 | 16 | -27 |
| 乃 | 6 | 0 | -6 |
| 矣 | 0 | 0 | +0 |
| 哉 | 1 | 0 | -1 |
| 焉 | 0 | 0 | +0 |
| 兒 | 1 | 1 | +0 |
| 此等 | 0 | 0 | +0 |
| 爾等 | 0 | 0 | +0 |

**總污染**: shipped 約 373 → v3 全清為 **modern-usage-only**（之前/之後/之時/之間 · 諸王之運動 canonical · 哥兒們 · 葛爾爾努音譯 gag · 多爾夫 canonical 音譯）

## 差異項（🟡 🟠 🔴 ✨；🟢 identical 不列以節省 review 時間）

以下為 264 項需你逐項決策的 diff。使用者回覆格式：`#1=A / #2=B / #3=C(細節)` 或批次快答 `🟡 全 B · 🟠 全依推薦 · 🔴 逐項挑 · ✨ 全 B`。

### #1 · `WE_ARE0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.75)

**英文原文**：
> Attention starship!\nWe are the Zoq-Fot-Pik.

**Shipped v0.5.2 (A)**：
> 注意,星艦！\n吾等乃佐-佛-皮。

**Rebuild v3 (B)**：
> 注意，星艦！\n我們是佐-佛-皮。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #2 · `WE_ARE1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.53)

**英文原文**：
> Make no hostile actions!

**Shipped v0.5.2 (A)**：
> 莫作任何敵意行為！

**Rebuild v3 (B)**：
> 別做出任何敵意舉動！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #3 · `WE_ARE2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.42)

**英文原文**：
> We come in peace, and with good will.

**Shipped v0.5.2 (A)**：
> 吾等和平而來,懷抱善意。

**Rebuild v3 (B)**：
> 我們懷抱和平與善意而來。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #4 · `WE_ARE3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.45)

**英文原文**：
> But if you make one false move, you're vapor!

**Shipped v0.5.2 (A)**：
> 但爾若動一絲歪腦筋,爾就變蒸氣了！

**Rebuild v3 (B)**：
> 但你只要走錯一步，就變蒸氣！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #5 · `WE_ARE4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.82)

**英文原文**：
> Don't worry, my companion is just a bit nervous...

**Shipped v0.5.2 (A)**：
> 別擔心,吾之同伴只是有點神經質……

**Rebuild v3 (B)**：
> 別擔心，我的同伴只是有點神經質……

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #6 · `WE_ARE5` · 🟡 微調 (ratio=0.86)

**英文原文**：
> No, I'm not!

**Shipped v0.5.2 (A)**：
> 不,我才沒有！

**Rebuild v3 (B)**：
> 不，我才沒有！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #7 · `WE_ARE7` · 🟡 微調 (ratio=0.86)

**英文原文**：
> No, I'm not.

**Shipped v0.5.2 (A)**：
> 不,我才沒有。

**Rebuild v3 (B)**：
> 不，我才沒有。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #8 · `SCOUT_HELLO0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.56)

**英文原文**：
> We are a scout vessel\ndispatched from our homeworld.

**Shipped v0.5.2 (A)**：
> 吾等乃偵察艦\n自吾等母星派出。

**Rebuild v3 (B)**：
> 我們是偵察艦\n從我們母星派遣出來。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #9 · `SCOUT_HELLO1` · 🟡 minor voice cleanup (ratio=0.87)

**英文原文**：
> We have travelled far\nthrough hostile, uncharted space\nto find you.\nWe hail from the <% comm.getColor("green", "zoqfot") %> dwarf star at coordinates\nziggerfau-gerrrnuf, Ah-ah, Pahoy-hoy.

**Shipped v0.5.2 (A)**：
> 吾等自極遠而來\n穿越充滿敵意、未經標記之太空\n方能尋得您。\n吾等來自座標為\n〔齊格佛-葛爾爾努,阿-阿,帕霍伊-霍伊〕（佐-佛-皮自造座標系）之 <% comm.getColor("綠色", "zoqfot") %>矮星。

**Rebuild v3 (B)**：
> 我們遠道而來\n穿越充滿敵意、未經標記的太空\n才找到你。\n我們來自座標為\n〔齊格佛-葛爾爾努，阿-阿，帕霍伊-霍伊〕（佐-佛-皮自造座標系）的 <% comm.getColor("綠色", "zoqfot") %>矮星。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #10 · `SCOUT_HELLO2` · 🟡 微調 (ratio=0.82)

**英文原文**：
> No, you idiot, in their coordinate system!

**Shipped v0.5.2 (A)**：
> 不,你這蠢材,是要說對方的座標系！

**Rebuild v3 (B)**：
> 不，你這蠢材，是要用對方的座標系！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #11 · `INIT_HOME_HELLO0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> You have arrived at our homeworld.

**Shipped v0.5.2 (A)**：
> 您已抵達吾等母星。

**Rebuild v3 (B)**：
> 你已抵達我們母星。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #12 · `INIT_HOME_HELLO1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.64)

**英文原文**：
> And we've got a billion ships here!

**Shipped v0.5.2 (A)**：
> 而吾等在此有十億艘戰艦！

**Rebuild v3 (B)**：
> 而且我們這裡有十億艘戰艦！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #13 · `INIT_HOME_HELLO2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.50)

**英文原文**：
> We are fortunate that you have found us in our time of need.

**Shipped v0.5.2 (A)**：
> 吾等真幸運,您在吾等急需之時尋獲吾等。

**Rebuild v3 (B)**：
> 真幸運，你在我們急需之時找到我們。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #14 · `INIT_HOME_HELLO3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.82)

**英文原文**：
> So don't even think of trying to attack us!

**Shipped v0.5.2 (A)**：
> 所以想都別想攻擊吾等！

**Rebuild v3 (B)**：
> 所以想都別想攻擊我們！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #15 · `HE_IS1` · 🟡 微調 (ratio=0.88)

**英文原文**：
> No, she is!

**Shipped v0.5.2 (A)**：
> 不,是「她」啦！

**Rebuild v3 (B)**：
> 不，是「她」啦！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #16 · `HE_IS2` · 🟡 微調 (ratio=0.86)

**英文原文**：
> No, I'm not!

**Shipped v0.5.2 (A)**：
> 不,我才不是！

**Rebuild v3 (B)**：
> 不，我才不是！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #17 · `HE_IS3` · 🟡 微調 (ratio=0.83)

**英文原文**：
> Yes, you are.

**Shipped v0.5.2 (A)**：
> 是,你就是。

**Rebuild v3 (B)**：
> 是，你就是。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #18 · `HE_IS4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.80)

**英文原文**：
> Cripes! We've been through this a million times!

**Shipped v0.5.2 (A)**：
> 要命！（Cripes!） 這爭論吾等已經歷過上百萬次了！

**Rebuild v3 (B)**：
> 要命！（Cripes!） 這事我們已經吵過一百萬次了！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #19 · `HE_IS5` · 🟡 微調 (ratio=0.85)

**英文原文**：
> That doesn't change anything. You're the Fot!

**Shipped v0.5.2 (A)**：
> 這改變不了什麼。 你就是佛特！

**Rebuild v3 (B)**：
> 吵幾次都改變不了什麼。 你就是佛特！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #20 · `HE_IS6` · 🟡 微調 (ratio=0.76)

**英文原文**：
> Faugh!\nWell, Captain, as you can see, this is a point of some contention.

**Shipped v0.5.2 (A)**：
> 呸！（Faugh!）\n呃,艦長,如您所見,這是一個略有爭議之點。

**Rebuild v3 (B)**：
> 呸！（Faugh!）\n呃，艦長，如你所見，這是有點爭議的一點。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #21 · `we_are_vindicator` · 🟡 minor voice cleanup (ratio=0.98)

**英文原文**：
> We are <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> flagship <% state.sis.getShipName() %> from Earth. What are your intentions?

**Shipped v0.5.2 (A)**：
> 我方乃 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> 之旗艦「<% state.sis.getShipName() %>」,來自地球。 你們有何意圖？

**Rebuild v3 (B)**：
> 我方是 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> 旗艦「<% state.sis.getShipName() %>」，來自地球。 你們有何意圖？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #22 · `WE_GLAD0` · 🟡 minor voice cleanup (ratio=0.92)

**英文原文**：
> Hurrah!\nThen we've finally found our saviors!

**Shipped v0.5.2 (A)**：
> 萬歲！（Hurrah!）\n吾等終於找到救世主了！

**Rebuild v3 (B)**：
> 萬歲！（Hurrah!）\n我們終於找到救世主了！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #23 · `WE_GLAD2` · 🟡 minor voice cleanup (ratio=0.86)

**英文原文**：
> At last, our search is over!\nIt is just as the great Crystal ones promised!

**Shipped v0.5.2 (A)**：
> 終於,吾等之尋覓有了盡頭！\n正如偉大晶智族所應允的那樣！

**Rebuild v3 (B)**：
> 終於，我們的尋覓有了盡頭！\n正如偉大晶智族所應允的那樣！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #24 · `WE_GLAD4` · 🟡 minor voice cleanup (ratio=0.86)

**英文原文**：
> Quiet, fool!\nCan't you see our nightmare is over!?\nThis ship is from the Great Crystal One's fabled Alliance\nthe Alliance of Free Stars!

**Shipped v0.5.2 (A)**：
> 閉嘴,笨蛋！\n你看不見吾等的噩夢終於結束了嗎！？\n此艦來自偉大晶智族所傳頌之聯盟\n那自由星系聯盟！

**Rebuild v3 (B)**：
> 閉嘴，笨蛋！\n你看不出來我們的噩夢終於結束了嗎！？\n這艘艦來自偉大晶智族所傳頌的聯盟\n那自由星系聯盟！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #25 · `quiet_toadies` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.62)

**英文原文**：
> SILENCE BLATHERING TOADIES! We are your new masters.

**Shipped v0.5.2 (A)**：
> 閉嘴,胡言亂語的舔屁蟲！ 我方乃你等新主人。

**Rebuild v3 (B)**：
> 閉嘴，胡說八道的舔屁蟲！ 老子是你們的新主人。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #26 · `TOLD_YOU0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> We are disappointed.

**Shipped v0.5.2 (A)**：
> 吾等很失望。

**Rebuild v3 (B)**：
> 我們很失望。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #27 · `TOLD_YOU2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.56)

**英文原文**：
> We had hoped that our species could be friends.

**Shipped v0.5.2 (A)**：
> 吾等原希望吾等物種可成為朋友。

**Rebuild v3 (B)**：
> 我們原希望我們兩個物種可以做朋友。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #28 · `TOLD_YOU3` · 🟡 微調 (ratio=0.98)

**英文原文**：
> Never in a million years! Just look at their beady eyes!

**Shipped v0.5.2 (A)**：
> 作夢一百萬年也不可能！ 光看他們那小豆子眼！

**Rebuild v3 (B)**：
> 作夢一百萬年也不可能！ 光看他那小豆子眼！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #29 · `TOLD_YOU4` · 🟡 微調 (ratio=0.90)

**英文原文**：
> But in the spirit of understanding...

**Shipped v0.5.2 (A)**：
> 但本著理解之精神……

**Rebuild v3 (B)**：
> 但本著理解的精神……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #30 · `TOLD_YOU6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.69)

**英文原文**：
> ...We will forgive you this transgression.

**Shipped v0.5.2 (A)**：
> ……吾等將原諒您此次冒犯。

**Rebuild v3 (B)**：
> ……我們將原諒你這次冒犯。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #31 · `your_race` · 🟡 微調 (ratio=0.89)

**英文原文**：
> Before we go on, can you tell us more about your species?

**Shipped v0.5.2 (A)**：
> 在我方繼續之前,能多告訴我方關於你等物種的事嗎？

**Rebuild v3 (B)**：
> 我方繼續之前，能多告訴我方關於你們物種的事嗎？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #32 · `YEARS_AGO0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> In our ancient past, four species evolved intelligence on our homeworld.

**Shipped v0.5.2 (A)**：
> 遠古時代,四種物種於吾等母星上演化出智慧。

**Rebuild v3 (B)**：
> 遠古時代，我們母星上有四種物種演化出智慧。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #33 · `YEARS_AGO6` · 🟡 minor voice cleanup (ratio=0.87)

**英文原文**：
> We three, the Zoq, Fot, and Pik evolved in such a way\nas to acquire sustenance from many sources...

**Shipped v0.5.2 (A)**：
> 吾等三方,佐格、佛特與皮克如此演化\n得以從多種來源獲得養分……

**Rebuild v3 (B)**：
> 我們三方，佐格、佛特、皮克如此演化\n得以從多種來源獲得養分……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #34 · `YEARS_AGO7` · 🟡 微調 (ratio=0.88)

**英文原文**：
> ...from airborne zooplankton...

**Shipped v0.5.2 (A)**：
> ……來自空中的浮游生物……

**Rebuild v3 (B)**：
> ……從空中的浮游生物……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #35 · `YEARS_AGO8` · 🟡 微調 (ratio=0.90)

**英文原文**：
> ...from solar and ambient energies...

**Shipped v0.5.2 (A)**：
> ……來自陽光與空氣裡的能量……

**Rebuild v3 (B)**：
> ……從陽光與空氣裡的能量……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #36 · `YEARS_AGO9` · 🟡 微調 (ratio=0.96)

**英文原文**：
> ...and from rocky fungal clingers.

**Shipped v0.5.2 (A)**：
> ……以及岩壁上的黏菌。

**Rebuild v3 (B)**：
> ……以及從岩壁上的黏菌。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #37 · `YEARS_AGO10` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> Our favorite!

**Shipped v0.5.2 (A)**：
> 吾等的最愛！

**Rebuild v3 (B)**：
> 我們的最愛！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #38 · `YEARS_AGO11` · 🟡 微調 (ratio=0.90)

**英文原文**：
> The Zebranky also consumed a variety of foods\nnamely: the Zoq\nthe Fot\nand the Pik.

**Shipped v0.5.2 (A)**：
> 澤布蘭基則以多種食物為生\n即:佐格、\n佛特、\n以及皮克。

**Rebuild v3 (B)**：
> 澤布蘭基則以多種食物為生\n分別是：佐格、\n佛特、\n以及皮克。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #39 · `YEARS_AGO12` · 🟡 minor voice cleanup (ratio=0.87)

**英文原文**：
> To survive the predations of the Zebranky\nwe banded together\nannihilated the Zebranky...

**Shipped v0.5.2 (A)**：
> 為了在澤布蘭基之獵殺下生存\n吾等聯合起來\n消滅了澤布蘭基……

**Rebuild v3 (B)**：
> 為了在澤布蘭基的獵殺下存活\n我們聯合起來\n消滅了澤布蘭基……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #40 · `YEARS_AGO13` · 🟡 微調 (ratio=0.94)

**英文原文**：
> ...and formed the cooperative union you now encounter.

**Shipped v0.5.2 (A)**：
> ……並形成您如今所見的合作聯盟。

**Rebuild v3 (B)**：
> ……並形成你如今所見的合作聯盟。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #41 · `TRAVELED_FAR0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.81)

**英文原文**：
> We are a relatively peaceful group of species.

**Shipped v0.5.2 (A)**：
> 吾等是相對愛好和平的物種群。

**Rebuild v3 (B)**：
> 我們是相對愛好和平的物種。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #42 · `TRAVELED_FAR1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> Unless we're angry.

**Shipped v0.5.2 (A)**：
> 除非吾等生氣時。

**Rebuild v3 (B)**：
> 除非我們生氣。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #43 · `TRAVELED_FAR2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.85)

**英文原文**：
> So we find ourselves in need of help.

**Shipped v0.5.2 (A)**：
> 所以吾等發現自己需要幫助。

**Rebuild v3 (B)**：
> 所以我們發現自己需要幫助。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #44 · `TRAVELED_FAR3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.82)

**英文原文**：
> We only need a LITTLE!

**Shipped v0.5.2 (A)**：
> 吾等只需要「一點點」！

**Rebuild v3 (B)**：
> 我們只需要「一點點」！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #45 · `TRAVELED_FAR4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.78)

**英文原文**：
> Because of our desperate situation.

**Shipped v0.5.2 (A)**：
> 因為吾等處境絕望。

**Rebuild v3 (B)**：
> 因為我們處境絕望。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #46 · `UNDER_ATTACK0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.81)

**英文原文**：
> Our planets are under attack from an invading horde!

**Shipped v0.5.2 (A)**：
> 吾等之行星正遭一群入侵大軍攻擊！

**Rebuild v3 (B)**：
> 我們的行星正遭一群入侵大軍攻擊！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #47 · `UNDER_ATTACK1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.68)

**英文原文**：
> We do not know who they are, or why they are here.

**Shipped v0.5.2 (A)**：
> 吾等不知他們是誰,亦不知為何而來。

**Rebuild v3 (B)**：
> 我們不知道他們是誰，也不知道他們為何而來。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #48 · `UNDER_ATTACK2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.78)

**英文原文**：
> We are being blown to bits.

**Shipped v0.5.2 (A)**：
> 吾等正被炸得粉碎。

**Rebuild v3 (B)**：
> 我們正被炸得粉碎。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #49 · `UNDER_ATTACK5` · 🟡 微調 (ratio=0.94)

**英文原文**：
> ...they release these energies on each other.

**Shipped v0.5.2 (A)**：
> ……他們是把那能量釋放在彼此身上。

**Rebuild v3 (B)**：
> ……他們把能量釋放在彼此身上。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #50 · `UNDER_ATTACK7` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.75)

**英文原文**：
> ...they favor combat near strong gravity wells.\nTheir stray shots regularly strike the surface of our planets\noften with tragic results.

**Shipped v0.5.2 (A)**：
> ……他們偏好在強重力井附近作戰。\n他們散亂的擊發常擊中吾等行星表面\n通常造成悲慘後果。

**Rebuild v3 (B)**：
> ……他們偏好在強重力井附近作戰。\n他們的流彈常打中我們的行星表面\n通常後果慘不忍睹。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #51 · `UNDER_ATTACK9` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.76)

**英文原文**：
> ...they have never found our homeworld, only our colony planets.

**Shipped v0.5.2 (A)**：
> ……他們從未找到吾等母星,只找到吾等殖民地。

**Rebuild v3 (B)**：
> ……他們從未找到我們母星，只找到我們的殖民地。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #52 · `UNDER_ATTACK11` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.75)

**英文原文**：
> ...all of our colonies have perished as a consequence.

**Shipped v0.5.2 (A)**：
> ……吾等所有殖民地皆因此覆滅。

**Rebuild v3 (B)**：
> ……我們所有的殖民地都因此覆滅了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #53 · `tough_luck` · 🟡 微調 (ratio=0.77)

**英文原文**：
> Hey, space is a tough place where wimps eat flaming plasma death.

**Shipped v0.5.2 (A)**：
> 嘿,太空是個殘酷的地方,弱者就吃火焰電漿死。

**Rebuild v3 (B)**：
> 喂，太空是個殘酷的地方，孬種就吃火焰電漿死。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #54 · `NOT_HELPFUL0` · 🟡 微調 (ratio=0.80)

**英文原文**：
> Oh, dear.

**Shipped v0.5.2 (A)**：
> 噢,天啊。

**Rebuild v3 (B)**：
> 噢，天啊。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #55 · `NOT_HELPFUL1` · 🟡 微調 (ratio=0.86)

**英文原文**：
> I told you he looked like a creep!

**Shipped v0.5.2 (A)**：
> 我就跟你說他看起來像個混蛋！

**Rebuild v3 (B)**：
> 我就跟你說他看起來像個爛人！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #56 · `NOT_HELPFUL2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.69)

**英文原文**：
> No! We must try to understand.\nHis ways are not like our own.

**Shipped v0.5.2 (A)**：
> 不！ 吾等必須試著理解。\n他的方式與吾等不同。

**Rebuild v3 (B)**：
> 不！ 我們必須試著理解。\n他做事的方式跟我們不一樣。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #57 · `NOT_HELPFUL4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.82)

**英文原文**：
> Let us give him one more chance.

**Shipped v0.5.2 (A)**：
> 讓吾等再給他一次機會。

**Rebuild v3 (B)**：
> 讓我們再給他一次機會。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #58 · `NOT_HELPFUL5` · 🟠 措辭改變 短句 (ratio=0.72)

**英文原文**：
> Just look at him! He's a killer, I tell you!

**Shipped v0.5.2 (A)**：
> 你看看他！ 他就是個殺手,我告訴你！

**Rebuild v3 (B)**：
> 你看看他！ 我告訴你，他就是個殺手！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #59 · `LOOK_LIKE1` · 🟡 微調 (ratio=0.89)

**英文原文**：
> The other ships are black as space\nand their hulls are carved with strange alien writing.

**Shipped v0.5.2 (A)**：
> 另一些艦艇黑如太空\n其船殼刻著詭異的異族文字。

**Rebuild v3 (B)**：
> 另一些艦艇黑得像太空\n船殼上刻著詭異的異族文字。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #60 · `LOOK_LIKE2` · 🟡 微調 (ratio=0.93)

**英文原文**：
> In combat the two ships seem evenly matched.

**Shipped v0.5.2 (A)**：
> 戰鬥中兩方艦艇似乎勢均力敵。

**Rebuild v3 (B)**：
> 戰鬥中兩方艦艇看似勢均力敵。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #61 · `GOODBYE0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.65)

**英文原文**：
> If you must go now, we understand.

**Shipped v0.5.2 (A)**：
> 如果您現在必須離去,吾等能理解。

**Rebuild v3 (B)**：
> 如果你現在必須離開，我們理解。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #62 · `GOODBYE2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.78)

**英文原文**：
> We hope that on your next visit\nwe can establish a mutual assistance pact.

**Shipped v0.5.2 (A)**：
> 吾等希望您下次來訪時\n吾等能建立一項互助協定。

**Rebuild v3 (B)**：
> 我們希望你下次來訪時\n我們能建立一項互助協定。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #63 · `GOODBYE3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.85)

**英文原文**：
> I can't believe that he's just leaving us here!\n...what a jerk.

**Shipped v0.5.2 (A)**：
> 我不敢相信他就這樣把吾等丟在這裡！\n……真是個混蛋。

**Rebuild v3 (B)**：
> 我不敢相信他就這樣把我們丟在這裡！\n……真是個爛人。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #64 · `all_very_interesting` · 🟡 微調 (ratio=0.83)

**英文原文**：
> Yes, yes, that's all very interesting, but now we are going to attack you!

**Shipped v0.5.2 (A)**：
> 對對對,一切都非常有趣,但現在我方要攻擊你們了！

**Rebuild v3 (B)**：
> 對對對，一切都非常有趣，但老子現在要攻擊你們了！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #65 · `SEE_TOLD_YOU1` · 🟡 微調 (ratio=0.98)

**英文原文**：
> See! I told you.!...\n...but would you listen... NO!

**Shipped v0.5.2 (A)**：
> 看吧！ 我早就告訴過你！……\n……但你就是不聽…… 就不聽！

**Rebuild v3 (B)**：
> 看吧！ 我早就告訴過你了！……\n……但你就是不聽…… 就不聽！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #66 · `SEE_TOLD_YOU2` · 🟠 措辭改變 短句 (ratio=0.67)

**英文原文**：
> I don't understand!

**Shipped v0.5.2 (A)**：
> 我不明白！

**Rebuild v3 (B)**：
> 我不懂！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #67 · `SEE_TOLD_YOU3` · 🟡 minor voice cleanup (ratio=0.94)

**英文原文**：
> So what does all your nicey-nice to the alien get us?\nNothing! That's what!\nYou should have done what I said\nand told him we were the Precursors.

**Shipped v0.5.2 (A)**：
> 所以你對外星人搞這一套禮貌到底得到什麼？\n什麼也沒有！ 就是這樣！\n你就該照我說的做\n告訴他吾等就是先驅者。

**Rebuild v3 (B)**：
> 所以你對外星人搞這一套禮貌到底得到什麼？\n什麼也沒有！ 就是這樣！\n你就該照我說的做\n告訴他我們才是先驅者。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #68 · `ALLY_WITH_US0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.78)

**英文原文**：
> We would like to establish\na formal mutual-assistance pact\nwith your species.

**Shipped v0.5.2 (A)**：
> 吾等想\n與您的物種\n建立正式的互助協定。

**Rebuild v3 (B)**：
> 我們想\n跟你們的物種\n建立正式的互助協定。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #69 · `ALLY_WITH_US2` · 🟡 minor voice cleanup (ratio=0.90)

**英文原文**：
> And as a sign of our good faith\nwe will provide you with skilled Captains\nand plans for building our `Stinger' starships.

**Shipped v0.5.2 (A)**：
> 作為誠意的表示\n吾等將為您提供技術精湛的艦長\n以及吾等「刺針號」（Stinger）星艦的建造圖。

**Rebuild v3 (B)**：
> 作為誠意的表示\n我們將為你提供技術精湛的艦長\n以及我們「刺針號」（Stinger）星艦的建造圖。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #70 · `ALLY_WITH_US3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.74)

**英文原文**：
> In return, if the bad guys find our homeworld\nyou'll rush over here and vaporize 'em.

**Shipped v0.5.2 (A)**：
> 作為交換,若壞人找到吾等母星\n您得火速趕來,把他們汽化。

**Rebuild v3 (B)**：
> 作為交換，如果壞人找到我們母星\n你要火速趕來，把他們汽化。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #71 · `ALLY_WITH_US5` · 🟠 措辭改變 (ratio=0.74)

**英文原文**：
> Great deal, eh?\nYou can't afford to pass it up!\nSo what do you say?

**Shipped v0.5.2 (A)**：
> 多好的交易,對吧？\n您絕對不能錯過！\n所以您意下如何？

**Rebuild v3 (B)**：
> 多好的交易，對吧？\n你錯過就虧大了！\n所以你意下如何？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #72 · `decide_later` · 🟡 微調 (ratio=0.98)

**英文原文**：
> Uh... I need to consult with our, er... our Grand-High Poobah!

**Shipped v0.5.2 (A)**：
> 呃…… 我方得先請示我方的,呃…… 尊貴至極的波霸大人（Grand-High Poobah）！

**Rebuild v3 (B)**：
> 呃…… 我方得先請示我方的，呃…… 尊貴至極的波霸大人（Grand-High Poobah）！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #73 · `PLEASE_HURRY0` · 🟡 微調 (ratio=0.96)

**英文原文**：
> Please hurry back with word from your Poobah.\nMillions of lives are at stake!

**Shipped v0.5.2 (A)**：
> 請帶著您波霸大人的話快點回來。\n數百萬條生命危在旦夕！

**Rebuild v3 (B)**：
> 請帶著你波霸大人的話快點回來。\n數百萬條生命危在旦夕！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #74 · `PLEASE_HURRY1` · 🟡 微調 (ratio=0.92)

**英文原文**：
> Not the least of which is mine.

**Shipped v0.5.2 (A)**：
> 其中最重要的一條就是我的。

**Rebuild v3 (B)**：
> 其中最要緊的一條就是我的。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #75 · `EMMISSARIES0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> These are the words we have prayed for!

**Shipped v0.5.2 (A)**：
> 這正是吾等日夜祈禱之言！

**Rebuild v3 (B)**：
> 這正是我們日夜祈禱的話！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #76 · `EMMISSARIES1` · 🟡 微調 (ratio=0.88)

**英文原文**：
> Hey! This trip's not a waste after all!

**Shipped v0.5.2 (A)**：
> 嘿！ 這趟不是白跑一趟嘛！

**Rebuild v3 (B)**：
> 嘿！ 這趟不是白跑了嘛！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #77 · `EMMISSARIES2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.49)

**英文原文**：
> More than anything, we seek an ally\nto help us survive in this hostile universe.

**Shipped v0.5.2 (A)**：
> 吾等所求的莫過於一位盟友\n協助吾等於此充滿敵意之宇宙中生存。

**Rebuild v3 (B)**：
> 我們最渴望的就是一個盟友\n幫我們在這充滿敵意的宇宙中生存下去。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #78 · `EMMISSARIES3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.80)

**英文原文**：
> We are having some problems of that general nature.

**Shipped v0.5.2 (A)**：
> 吾等正遇到那類問題。

**Rebuild v3 (B)**：
> 我們正遇到那類問題。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #79 · `EMMISSARIES4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.70)

**英文原文**：
> But we are only emissaries.\nYou must meet with our leaders.\nThey are wiser... more powerful beings!

**Shipped v0.5.2 (A)**：
> 但吾等只是使者。\n您必須與吾等領導會晤。\n他們更有智慧……更強大！

**Rebuild v3 (B)**：
> 但我們只是使者。\n你必須見我們的領袖。\n他們更有智慧…… 力量也更強大！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #80 · `EMMISSARIES5` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.77)

**英文原文**：
> They look just like us, though.

**Shipped v0.5.2 (A)**：
> 不過他們長得跟吾等一模一樣。

**Rebuild v3 (B)**：
> 不過他們長得跟我們一模一樣就是了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #81 · `EMMISSARIES6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.74)

**英文原文**：
> Fly to the star called <% comm.getStarName("Alpha Tucanae", "zoqfot") %>.\nThe planet closest to the sun is our home.

**Shipped v0.5.2 (A)**：
> 飛往名為 <% comm.getStarName("杜鵑座α", "zoqfot") %>（Alpha Tucanae） 之星。\n最靠近太陽的行星就是吾等母星。

**Rebuild v3 (B)**：
> 飛到叫做 <% comm.getStarName("杜鵑座α", "zoqfot") %> 的恆星。\n離太陽最近的行星就是我們的家。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #82 · `EMMISSARIES7` · 🔴 語意/voice 差異大 (ratio=0.26)

**英文原文**：
> And if possible, hurry.

**Shipped v0.5.2 (A)**：
> 如果可以,請快點。

**Rebuild v3 (B)**：
> 還有，方便的話，麻煩快一點。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #83 · `sure` · 🟠 措辭改變 (ratio=0.72)

**英文原文**：
> You are under attack by the Ur-Quan, our enemy as well.  Therefore, speaking for all the People of Earth, I accept your offer.

**Shipped v0.5.2 (A)**：
> 你們正遭烏寬攻擊,而烏寬也是我方之敵。 因此,我謹代表全地球人民,接受你等提議。

**Rebuild v3 (B)**：
> 你們正遭到烏寬攻擊，牠們也是我方的敵人。 因此，我方代表全體地球子民，接受你們的提議。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #84 · `WE_ALLY0` · 🟠 措辭改變 短句 (ratio=0.67)

**英文原文**：
> How wonderful!

**Shipped v0.5.2 (A)**：
> 太美妙了！

**Rebuild v3 (B)**：
> 太好了！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #85 · `WE_ALLY1` · 🟡 微調 (ratio=0.92)

**英文原文**：
> Hurray!

**Shipped v0.5.2 (A)**：
> 萬歲！（Hurrah!）

**Rebuild v3 (B)**：
> 萬歲！（Hurray!）

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #86 · `WE_ALLY2` · 🔴 語意/voice 差異大 (ratio=0.22)

**英文原文**：
> How marvelous!

**Shipped v0.5.2 (A)**：
> 何等壯麗！

**Rebuild v3 (B)**：
> 太棒了！

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #87 · `WE_ALLY4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.54)

**英文原文**：
> Captain, we shall begin fulfilling our commitment at once!\nWe will begin transporting our officers to your base immediately!

**Shipped v0.5.2 (A)**：
> 艦長,吾等將立即開始履行承諾！\n吾等將立即開始把吾等的軍官運送到您的基地！

**Rebuild v3 (B)**：
> 艦長，我們馬上開始履行約定！\n我們馬上把軍官運送到你的基地！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #88 · `WE_ALLY5` · 🟡 微調 (ratio=0.76)

**英文原文**：
> Why, heck!\nMaybe I'll even make the trip to your planet!\nI'd make a good starship captain, Captain!\nI'm pretty darn mean in a fight\nand there ain't nobody better than me\nwith a thrusting stinger tongue attack!

**Shipped v0.5.2 (A)**：
> 嘿,可惡！\n說不定我也會親自跑一趟到您的星球！\n我一定會是個好星艦艦長,艦長！\n打起架來我可兇了\n而且沒人比我更擅長\n突進刺針舌攻擊！

**Rebuild v3 (B)**：
> 哎唷！\n說不定我還要親自跑一趟你的星球！\n我會是個好星艦艦長的，艦長！\n我打起架來還挺兇的\n而且沒人比得過我的\n突進刺針舌攻擊！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #89 · `never` · 🟡 微調 (ratio=0.88)

**英文原文**：
> What? Protect you failures? No way! You're too lame!

**Shipped v0.5.2 (A)**：
> 什麼？ 保護你們這些廢物？ 免談！ 你們太遜了！

**Rebuild v3 (B)**：
> 什麼？ 保護你們這些廢柴？ 沒門！ 你們太遜了！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #90 · `WE_ENEMIES0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.60)

**英文原文**：
> We have revealed ourselves to you.\nWe have held out our appendages to you in friendship!...\n...and you have treated us like dead Zebrankys.\nIt takes a great deal to anger one of my species, Captain\nBUT YOU HAVE JUST SUCCEEDED!\nAttention Shipmates! Man the spray gun! Hoist the tongue!\nPREPARE FOR BATTLE!

**Shipped v0.5.2 (A)**：
> 吾等已對您坦露自己。\n吾等已伸出附肢與您示好！……\n……然而您卻把吾等當作死澤布蘭基一般對待。\n要激怒吾等物種需要很多事,艦長\n但您剛剛做到了！\n注意,同伴們！ 上噴射砲！ 升起舌頭！\n備戰！

**Rebuild v3 (B)**：
> 我們已經向你敞開心扉。\n我們對你伸出附肢表示友好！……\n……而你卻把我們當死掉的澤布蘭基那樣對待。\n要惹怒我這個物種可不容易，艦長\n可是你剛剛做到了！\n各位船員！ 準備噴射砲！ 升起舌頭！\n備戰！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #91 · `WE_ENEMIES1` · 🟠 措辭改變 短句 (ratio=0.48)

**英文原文**：
> Yeah.\nLet's toast those creeps!

**Shipped v0.5.2 (A)**：
> 耶。\n烤了這些混蛋！

**Rebuild v3 (B)**：
> 是啊。\n烤那些爛人去！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #92 · `HOSTILE_HELLO_10` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.59)

**英文原文**：
> Coming here was pointless, human.\nOur species are at war.

**Shipped v0.5.2 (A)**：
> 來這裡毫無意義,人類。\n吾等物種正處於戰爭。

**Rebuild v3 (B)**：
> 來這裡沒意義，人類。\n我們兩個物種正在打仗。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #93 · `HOSTILE_HELLO_11` · 🟠 措辭改變 短句 (ratio=0.67)

**英文原文**：
> Right!\nPrepare to die, alien scum!

**Shipped v0.5.2 (A)**：
> 沒錯！\n受死吧,異族渣滓！

**Rebuild v3 (B)**：
> 沒錯！\n準備受死吧，外星渣！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #94 · `HOSTILE_HELLO_20` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.32)

**英文原文**：
> If you had allied with us, Captain

**Shipped v0.5.2 (A)**：
> 若您當初與吾等結盟,艦長

**Rebuild v3 (B)**：
> 艦長，你當初要是跟我們結盟

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #95 · `HOSTILE_HELLO_21` · 🟠 措辭改變 短句 (ratio=0.55)

**英文原文**：
> Which you didn't!

**Shipped v0.5.2 (A)**：
> 但您沒有！

**Rebuild v3 (B)**：
> 你就是沒有！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #96 · `HOSTILE_HELLO_22` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.40)

**英文原文**：
> We would gladly tell you what we have learned

**Shipped v0.5.2 (A)**：
> 吾等會樂意告訴您吾等所知之事

**Rebuild v3 (B)**：
> 我們會很樂意告訴你我們探聽到的事

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #97 · `HOSTILE_HELLO_23` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.63)

**英文原文**：
> Which we won't!

**Shipped v0.5.2 (A)**：
> 但吾等不會告訴你！

**Rebuild v3 (B)**：
> 而我們才不會告訴你！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #98 · `HOSTILE_HELLO_24` · 🟠 措辭改變 (ratio=0.68)

**英文原文**：
> Regarding the two warring alien factions\nthe Ur-Quan and their siblings, the Kohr-Ah.

**Shipped v0.5.2 (A)**：
> 關於那兩個交戰的異族陣營\n即烏寬與其兄弟柯亞。

**Rebuild v3 (B)**：
> 關於那兩個交戰的外星陣營\n烏寬跟他們的手足柯亞。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #99 · `HOSTILE_HELLO_25` · 🟡 微調 (ratio=0.79)

**英文原文**：
> But now you'll NEVER know!

**Shipped v0.5.2 (A)**：
> 但如今您「永遠」不會知道了！

**Rebuild v3 (B)**：
> 但你現在「永遠」不會知道了！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #100 · `HOSTILE_HELLO_30` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.43)

**英文原文**：
> With whatever remaining forces we have\nwe will do our best to destroy you.

**Shipped v0.5.2 (A)**：
> 以吾等尚存之力\n吾等將盡力毀滅您。

**Rebuild v3 (B)**：
> 以我們所剩不多的兵力\n我們會盡力毀滅你。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #101 · `HOSTILE_HELLO_31` · 🟠 措辭改變 短句 (ratio=0.52)

**英文原文**：
> Yeah! And she means it too!

**Shipped v0.5.2 (A)**：
> 耶！ 而且她是認真的！

**Rebuild v3 (B)**：
> 沒錯！ 而且她說到做到！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #102 · `HOSTILE_HELLO_40` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.46)

**英文原文**：
> Your villainy is beyond possible forgiveness!\nWe are compelled by our anger to destroy you.

**Shipped v0.5.2 (A)**：
> 您的惡行不可饒恕！\n吾等被憤怒所迫,必須毀滅您。

**Rebuild v3 (B)**：
> 你的惡行罄竹難書！\n我們被憤怒逼得非毀滅你不可。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #103 · `HOSTILE_HELLO_41` · 🟡 微調 (ratio=0.87)

**英文原文**：
> He's probably just gonna run away again.\nThe coward!

**Shipped v0.5.2 (A)**：
> 他大概又要跑掉了。\n膽小鬼！

**Rebuild v3 (B)**：
> 他大概又要落跑了。\n那個膽小鬼！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #104 · `NEUTRAL_HOME_HELLO_10` · 🟠 措辭改變 短句 (ratio=0.62)

**英文原文**：
> Ah! It is the alien from the Chenjesu's Alliance!

**Shipped v0.5.2 (A)**：
> 啊！ 是那位來自晶智族聯盟的異族！

**Rebuild v3 (B)**：
> 啊！ 是晶智族聯盟那個外星人！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #105 · `NEUTRAL_HOME_HELLO_11` · 🟡 微調 (ratio=0.91)

**英文原文**：
> Just look at those weapon pods on his ship.

**Shipped v0.5.2 (A)**：
> 光看他艦上那些武器艙。

**Rebuild v3 (B)**：
> 看看他艦上那些武器艙。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #106 · `NEUTRAL_HOME_HELLO_12` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.61)

**英文原文**：
> We hope that during this visit\nwe can make clear to your species\nthe benefits of a mutual-assistance pact.

**Shipped v0.5.2 (A)**：
> 吾等希望這次訪問\n吾等能向您的物種說清楚\n一份互助協定的種種好處。

**Rebuild v3 (B)**：
> 我們希望這次來訪\n能讓你們物種明白\n互助協定的好處。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #107 · `NEUTRAL_HOME_HELLO_13` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> But we're also armed to the teeth\nso don't try stealing our atmosphere or anything sneaky like that!

**Shipped v0.5.2 (A)**：
> 但吾等也武裝到牙齒\n所以別想偷吾等的大氣層或是搞什麼小把戲！

**Rebuild v3 (B)**：
> 不過我們也是全副武裝\n所以別想偷我們的大氣層或搞什麼鬼把戲！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #108 · `NEUTRAL_HOME_HELLO_20` · 🟡 微調 (ratio=0.89)

**英文原文**：
> Once more, the Alliance starship has returned.

**Shipped v0.5.2 (A)**：
> 聯盟星艦又來了。

**Rebuild v3 (B)**：
> 聯盟的星艦又回來了。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #109 · `NEUTRAL_HOME_HELLO_21` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.75)

**英文原文**：
> Yeah. I bet THIS is the time they try to trick us.

**Shipped v0.5.2 (A)**：
> 耶。 我打賭「這次」他們就要騙吾等了。

**Rebuild v3 (B)**：
> 是啊。 我打賭「這次」他們就要來耍我們了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #110 · `NEUTRAL_HOME_HELLO_22` · 🟠 措辭改變 短句 (ratio=0.42)

**英文原文**：
> Alien Captain, do you bring word from your Leaders?

**Shipped v0.5.2 (A)**：
> 異族艦長,您帶來領導的口信了嗎？

**Rebuild v3 (B)**：
> 外星艦長，你帶著你領袖的話來了嗎？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #111 · `NEUTRAL_HOME_HELLO_23` · 🟠 措辭改變 (ratio=0.57)

**英文原文**：
> If he does, I bet it's something like\n`Submit or be Eaten'!

**Shipped v0.5.2 (A)**：
> 他要是有,我打賭是類似\n「屈服或被吃」之類的！

**Rebuild v3 (B)**：
> 他如果有帶，我打賭肯定是像\n「投降或被吃掉」！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #112 · `ALLIED_HOME_HELLO_10` · 🟠 措辭改變 短句 (ratio=0.74)

**英文原文**：
> Hello friend and ally!

**Shipped v0.5.2 (A)**：
> 您好,朋友兼盟友！

**Rebuild v3 (B)**：
> 你好啊，朋友兼盟友！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #113 · `ALLIED_HOME_HELLO_11` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.38)

**英文原文**：
> Got any presents for us?

**Shipped v0.5.2 (A)**：
> 有給吾等的禮物嗎？

**Rebuild v3 (B)**：
> 有沒有帶什麼禮物給咱們？

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #114 · `ALLIED_HOME_HELLO_12` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.79)

**英文原文**：
> We hope your struggle against the Ur-Quan goes well!

**Shipped v0.5.2 (A)**：
> 吾等希望您對抗烏寬的鬥爭順利！

**Rebuild v3 (B)**：
> 希望你對抗烏寬的戰鬥順利！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #115 · `ALLIED_HOME_HELLO_13` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.73)

**英文原文**：
> Darn! He never gives us anything.

**Shipped v0.5.2 (A)**：
> 可惡！（Darn!） 他從不給吾等任何東西。

**Rebuild v3 (B)**：
> 可惡！（Darn!） 他從來都不給咱們什麼。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #116 · `ALLIED_HOME_HELLO_20` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.74)

**英文原文**：
> Welcome back to our world.

**Shipped v0.5.2 (A)**：
> 歡迎回到吾等世界。

**Rebuild v3 (B)**：
> 歡迎回到我們的世界。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #117 · `ALLIED_HOME_HELLO_21` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.58)

**英文原文**：
> Yeah, welcome back to our world!

**Shipped v0.5.2 (A)**：
> 耶,歡迎回到吾等世界！

**Rebuild v3 (B)**：
> 是啊，歡迎回到我們的世界！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #118 · `ALLIED_HOME_HELLO_22` · 🟠 措辭改變 短句 (ratio=0.50)

**英文原文**：
> I just said that.

**Shipped v0.5.2 (A)**：
> 我剛剛才說過。

**Rebuild v3 (B)**：
> 我剛剛就那樣講了。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #119 · `ALLIED_HOME_HELLO_23` · 🟡 微調 (ratio=0.80)

**英文原文**：
> So? It doesn't mean I can't say it too.\nBesides, you always get to talk first.\nThat's not fair!

**Shipped v0.5.2 (A)**：
> 那又怎樣？ 不代表我不能也說。\n再說,總是輪你先講。\n這不公平！

**Rebuild v3 (B)**：
> 那又怎樣？ 又不表示我不能也講。\n再說，每次都你先講。\n這不公平！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #120 · `ALLIED_HOME_HELLO_24` · 🟡 微調 (ratio=0.78)

**英文原文**：
> Sorry, that's just the way it is.

**Shipped v0.5.2 (A)**：
> 抱歉,事情就是這樣。

**Rebuild v3 (B)**：
> 抱歉，就是這樣。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #121 · `ALLIED_HOME_HELLO_25` · 🟡 微調 (ratio=0.91)

**英文原文**：
> Well why?! That doesn't make sense.

**Shipped v0.5.2 (A)**：
> 為什麼？！ 這不合理。

**Rebuild v3 (B)**：
> 為什麼啊？ 這不合理。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #122 · `ALLIED_HOME_HELLO_26` · 🟠 措辭改變 短句 (ratio=0.54)

**英文原文**：
> Look, don't ask me.\nI think it's something technical.

**Shipped v0.5.2 (A)**：
> 聽好,別問我。\n我想這是技術性問題。

**Rebuild v3 (B)**：
> 喂，別問我。\n我覺得是什麼技術上的事。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #123 · `ALLIED_HOME_HELLO_27` · 🟠 措辭改變 (ratio=0.68)

**英文原文**：
> Yeah, right. I'm so sure.\nWhat a lame excuse.

**Shipped v0.5.2 (A)**：
> 是喔,對啦。 我信你才有鬼。\n什麼爛藉口。

**Rebuild v3 (B)**：
> 是啊，才怪。 我信才有鬼。\n真是爛藉口。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #124 · `ALLIED_HOME_HELLO_30` · 🟠 措辭改變 短句 (ratio=0.69)

**英文原文**：
> Greetings Captain.\nWhat can your allies do for you?

**Shipped v0.5.2 (A)**：
> 問候,艦長。\n您的盟友能為您做些什麼？

**Rebuild v3 (B)**：
> 你好，艦長。\n盟友能為你做什麼？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #125 · `ALLIED_HOME_HELLO_31` · 🟡 微調 (ratio=0.86)

**英文原文**：
> Your favorite allies!

**Shipped v0.5.2 (A)**：
> 您最愛的盟友！

**Rebuild v3 (B)**：
> 你最愛的盟友！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #126 · `ALLIED_HOME_HELLO_40` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.50)

**英文原文**：
> Hello human ally.\nWe are at your service.

**Shipped v0.5.2 (A)**：
> 您好,人類盟友。\n吾等聽候差遣。

**Rebuild v3 (B)**：
> 你好，人類盟友。\n我們為你效勞。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #127 · `ALLIED_HOME_HELLO_41` · 🟡 微調 (ratio=0.83)

**英文原文**：
> What do you want?

**Shipped v0.5.2 (A)**：
> 您想要什麼？

**Rebuild v3 (B)**：
> 你想要什麼？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #128 · `THANKS_FOR_RESCUE0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.74)

**英文原文**：
> Our Savior! Our Savior!\nYou have rescued us from certain destruction!

**Shipped v0.5.2 (A)**：
> 吾等的救世主！ 吾等的救世主！\n您將吾等從必死的命運中拯救出來了！

**Rebuild v3 (B)**：
> 救世主！ 我們的救世主！\n你把我們從必死的命運中救出來了！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #129 · `THANKS_FOR_RESCUE1` · 🟡 微調 (ratio=0.75)

**英文原文**：
> Howee-baby! That was a close one!

**Shipped v0.5.2 (A)**：
> 好耶寶貝！（Howee-baby!） 剛剛真是好險！

**Rebuild v3 (B)**：
> 好耶寶貝！（Howee-baby!） 差一點就完蛋了！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #130 · `THANKS_FOR_RESCUE2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> The black ship appeared in orbit several days ago\nand began raining down bolts of destructive energy\non the surface of our planet!

**Shipped v0.5.2 (A)**：
> 那艘黑艦數日前出現於軌道\n開始向吾等行星表面\n傾瀉毀滅性能量爆擊！

**Rebuild v3 (B)**：
> 那艘黑船幾天前出現在軌道上\n然後開始朝我們星球表面\n傾瀉毀滅能量！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #131 · `THANKS_FOR_RESCUE4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.53)

**英文原文**：
> ...we were able to focus our planetary shields\nto deflect the energy blasts away from our cities.

**Shipped v0.5.2 (A)**：
> ……吾等得以集中吾等的行星護盾\n將能量爆擊自吾等城市偏轉開來。

**Rebuild v3 (B)**：
> ……我們能夠聚焦我們的行星護盾\n把能量爆擊從我們的城市那邊偏折開。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #132 · `THANKS_FOR_RESCUE6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.66)

**英文原文**：
> Large sections of our planet's beautiful wilderness\nhave been annihilated... entire ecosystems destroyed.

**Shipped v0.5.2 (A)**：
> 吾等星球美麗荒野的大片區域\n遭到殲滅…… 整個生態系被毀。

**Rebuild v3 (B)**：
> 我們星球上大片美麗的原野\n已被殲滅…… 整個生態系被摧毀。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #133 · `THANKS_FOR_RESCUE7` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.77)

**英文原文**：
> Oh! That makes me REALLY mad!\nI mean, attacking helpless, intelligent, alien species\nthat's one thing,\nbut toasting our cute little wood Jukes and tree Narfs\nthat is really low!

**Shipped v0.5.2 (A)**：
> 噢！ 那讓我「真的」很生氣！\n我是說,攻擊無助的、有智慧的異族物種\n那是一回事,\n但烤了吾等可愛的森林朱克獸（wood Jukes）與樹頂納夫獸（tree Narfs）\n那就太過份了！

**Rebuild v3 (B)**：
> 噢！ 這讓我「非常」火大！\n我是說，攻擊手無寸鐵、有智慧的外星物種\n是一回事，\n但把咱們可愛的森林朱克獸（wood Jukes）跟樹頂納夫獸（tree Narfs）都烤了\n那真的太過分！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #134 · `THANKS_FOR_RESCUE8` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.49)

**英文原文**：
> If the black ship had been accompanied by others of its kind\nwe wouldn't have been able stop the rain of destruction.\nThey would have killed us all.

**Shipped v0.5.2 (A)**：
> 若那艘黑艦當時有同類伴隨\n吾等本無法阻止那毀滅之雨。\n他們會殺光吾等所有人。

**Rebuild v3 (B)**：
> 如果那艘黑船有其他同伴一起來\n我們就沒辦法擋下那波毀滅之雨了。\n他們早就把我們全殺光了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #135 · `THANKS_FOR_RESCUE9` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.50)

**英文原文**：
> Well in that case, better those Jukes and Narfs than us, right?

**Shipped v0.5.2 (A)**：
> 那樣的話,寧可他們烤朱克獸和納夫獸也好過烤吾等,對吧？

**Rebuild v3 (B)**：
> 好啦，這樣的話，寧可牽牲那些朱克獸跟納夫獸，也不要牽牲我們，對吧？

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #136 · `THANKS_FOR_RESCUE10` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.58)

**英文原文**：
> Captain, it is clear that in matters of war\nyou are more capable than ourselves.\nWith this in mind, we would like to give you\nour four finest starships and crew.\nI hope they bring you many victories.

**Shipped v0.5.2 (A)**：
> 艦長,顯然於戰爭之事\n您比吾等更有能力。\n為此,吾等願獻上\n吾等最精良的四艘星艦與船員。\n希望它們為您帶來許多勝利。

**Rebuild v3 (B)**：
> 艦長，很明顯，在戰爭這方面\n你比我們更有本事。\n有鑑於此，我們想給你\n我們最精良的四艘星艦跟艦員。\n希望它們為你帶來很多勝利。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #137 · `THANKS_FOR_RESCUE11` · 🟠 措辭改變 短句 (ratio=0.42)

**英文原文**：
> Try not to lose them all right away.

**Shipped v0.5.2 (A)**：
> 盡量別馬上就損失掉全部。

**Rebuild v3 (B)**：
> 盡量別一下子就都弄丟了。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #138 · `bye_homeworld` · 🟠 措辭改變 (ratio=0.59)

**英文原文**：
> Bye Zoq. Bye Fot. Bye Pik.

**Shipped v0.5.2 (A)**：
> 再見,佐格。 再見,佛特。 再見,皮克。

**Rebuild v3 (B)**：
> 掰囉佐格。 掰囉佛特。 掰囉皮克。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #139 · `GOODBYE_HOME0` · 🟡 微調 (ratio=0.83)

**英文原文**：
> Goodbye Captain.

**Shipped v0.5.2 (A)**：
> 再見,艦長。

**Rebuild v3 (B)**：
> 再見，艦長。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #140 · `GOODBYE_HOME1` · 🔴 語意/voice 差異大 (ratio=0.29)

**英文原文**：
> See ya.

**Shipped v0.5.2 (A)**：
> 掰啦。

**Rebuild v3 (B)**：
> 回見囉。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #141 · `whats_up_homeworld` · 🔴 語意/voice 差異大 (ratio=0.27)

**英文原文**：
> So, what's happening around here?

**Shipped v0.5.2 (A)**：
> 所以這一帶最近如何？

**Rebuild v3 (B)**：
> 那，最近這裡有什麼事嗎？

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #142 · `GENERAL_INFO_10` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.38)

**英文原文**：
> We had a close call last week.

**Shipped v0.5.2 (A)**：
> 吾等上週差點出事。

**Rebuild v3 (B)**：
> 上禮拜我們差點就完蛋了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #143 · `GENERAL_INFO_11` · 🟠 措辭改變 短句 (ratio=0.56)

**英文原文**：
> One of those black ships was snooping around the system.

**Shipped v0.5.2 (A)**：
> 其中一艘黑艦在星系裡到處嗅探。

**Rebuild v3 (B)**：
> 有艘那種黑船在系統裡到處探頭探腦。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #144 · `GENERAL_INFO_12` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.46)

**英文原文**：
> But before it got to our world\nsome of the Green ships warped in\ndestroyed the black vessel\nand then left immediately.

**Shipped v0.5.2 (A)**：
> 但在它抵達吾等世界前\n有些綠色艦艇曲速跳入\n摧毀了那艘黑艦\n然後立即離開。

**Rebuild v3 (B)**：
> 但在它抵達我們星球之前\n幾艘綠船超空間跳進來\n把黑船打爆了\n然後馬上離開。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #145 · `GENERAL_INFO_13` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.31)

**英文原文**：
> We got lucky.

**Shipped v0.5.2 (A)**：
> 吾等真幸運。

**Rebuild v3 (B)**：
> 我們運氣不錯。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #146 · `GENERAL_INFO_20` · 🟠 措辭改變 (ratio=0.68)

**英文原文**：
> It's been pretty quiet, Captain.\nNothing new to report.

**Shipped v0.5.2 (A)**：
> 一切都很安靜,艦長。\n沒什麼新消息可報告。

**Rebuild v3 (B)**：
> 最近挺安靜的，艦長。\n沒什麼新的可報告。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #147 · `GENERAL_INFO_22` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.72)

**英文原文**：
> Why should we tell the Earth Captain about that?\nHe wouldn't be interested.

**Shipped v0.5.2 (A)**：
> 吾等為何要跟地球艦長講那件事？\n他才不會有興趣。

**Rebuild v3 (B)**：
> 我們幹嘛要跟地球艦長講那個？\n他不會有興趣的。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #148 · `GENERAL_INFO_23` · 🟡 微調 (ratio=0.91)

**英文原文**：
> Oh, yeah? How do you know?

**Shipped v0.5.2 (A)**：
> 喔是喔？ 你怎麼知道？

**Rebuild v3 (B)**：
> 喔是嗎？ 你怎麼知道？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #149 · `GENERAL_INFO_24` · 🟡 微調 (ratio=0.96)

**英文原文**：
> Because I'M not even interested.\nNobody with any brains is interested in Frungy!

**Shipped v0.5.2 (A)**：
> 因為連「我」都沒興趣。\n有點腦的都不會對芙戎奇有興趣！

**Rebuild v3 (B)**：
> 因為連「我」都沒興趣。\n有腦袋的都不會對芙戎奇有興趣！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #150 · `GENERAL_INFO_25` · 🟡 微調 (ratio=0.96)

**英文原文**：
> Well what about me, huh?\nI LOVE Frungy! It's the Sport of Kings!

**Shipped v0.5.2 (A)**：
> 那我呢,啊？\n我「愛」芙戎奇！ 它是諸王之運動！

**Rebuild v3 (B)**：
> 那我呢，啊？\n我「愛」芙戎奇！ 它是諸王之運動！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #151 · `GENERAL_INFO_26` · 🟠 措辭改變 短句 (ratio=0.40)

**英文原文**：
> Sheesh!

**Shipped v0.5.2 (A)**：
> 唉喲！

**Rebuild v3 (B)**：
> 唉喲！（Sheesh!）

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #152 · `GENERAL_INFO_27` · 🟡 微調 (ratio=0.86)

**英文原文**：
> Oh, all right\nhe wouldn't know any of the teams anyway.

**Shipped v0.5.2 (A)**：
> 噢,好啦\n反正他也不認識任何隊伍。

**Rebuild v3 (B)**：
> 喔，好啦\n反正他也不會認識任何隊伍。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #153 · `GENERAL_INFO_30` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.51)

**英文原文**：
> Although this may not pertain to the Ur-Quan\nwe have received an interesting report\nfrom one of our deep space scouts.

**Shipped v0.5.2 (A)**：
> 雖然這可能與烏寬無關\n吾等收到一份有趣的報告\n來自吾等一位深空偵察兵。

**Rebuild v3 (B)**：
> 雖然這可能跟烏寬無關\n我們從一位深空偵察兵那裡\n收到一份有意思的報告。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #154 · `GENERAL_INFO_31` · 🟡 微調 (ratio=0.76)

**英文原文**：
> She found a strange metal door-thing\nembedded in the surface of an alien planet.

**Shipped v0.5.2 (A)**：
> 她發現了一扇奇異的金屬門狀物\n嵌在一顆異星星球表面。

**Rebuild v3 (B)**：
> 她發現一種奇怪的金屬門\n嵌在一顆外星行星的表面。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #155 · `GENERAL_INFO_32` · 🟠 措辭改變 短句 (ratio=0.68)

**英文原文**：
> Although she and her crew spent many days\ntrying to open the door

**Shipped v0.5.2 (A)**：
> 雖然她與船員花了好幾天\n試著打開那扇門

**Rebuild v3 (B)**：
> 雖然她跟艦員花了好幾天\n想把那扇門打開

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #156 · `GENERAL_INFO_33` · 🟠 措辭改變 (ratio=0.59)

**英文原文**：
> they failed utterly to so much as budge it.

**Shipped v0.5.2 (A)**：
> 他們完全連推動它一寸都做不到。

**Rebuild v3 (B)**：
> 他們完全搞不定，甚至連推動它一絲一毫都失敗。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #157 · `GENERAL_INFO_34` · 🟠 措辭改變 (ratio=0.72)

**英文原文**：
> The reported location of this alien artifact\nis <% comm.getStarName("Epsilon Camelopardalis", "ship vault") %> I-A.

**Shipped v0.5.2 (A)**：
> 該異族遺物之位置\n位於 <% comm.getStarName("鹿豹座ε", "ship vault") %>（Epsilon Camelopardalis） I-A。

**Rebuild v3 (B)**：
> 那件外星文物的位置\n據報是在 <% comm.getStarName("鹿豹座ε", "ship vault") %> I-A。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #158 · `GENERAL_INFO_35` · 🟡 微調 (ratio=0.92)

**英文原文**：
> Go open it!\nI bet there's something cool inside!

**Shipped v0.5.2 (A)**：
> 去打開它吧！\n我打賭裡面有酷炫的東西！

**Rebuild v3 (B)**：
> 去打開它！\n我打賭裡面有很酷的東西！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #159 · `GENERAL_INFO_40` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.53)

**英文原文**：
> We may not have told you this before, Captain\nbut my species is somewhat sensitive\nto certain meta-psychic vibrations.

**Shipped v0.5.2 (A)**：
> 吾等或許從未告訴您這件事,艦長\n但我這物種對某類超心靈震盪\n有些感應能力。

**Rebuild v3 (B)**：
> 我們之前可能沒告訴過你，艦長\n但我這個物種\n對某些超心靈震盪還算敏感。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #160 · `GENERAL_INFO_41` · 🟠 措辭改變 短句 (ratio=0.57)

**英文原文**：
> Oh, no! Not this mental stuff again!

**Shipped v0.5.2 (A)**：
> 噢不！ 又來這套心靈的鬼扯！

**Rebuild v3 (B)**：
> 喔不！ 又是這個心靈那一套！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #161 · `GENERAL_INFO_42` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.72)

**英文原文**：
> Although my friend's species\nhas difficulty understanding our powers\nI can guarantee you, Captain\nthat our limited abilities are quite real.

**Shipped v0.5.2 (A)**：
> 雖然我朋友那物種\n難以理解吾等的能力\n我可以向您保證,艦長\n吾等有限的能力是真實存在的。

**Rebuild v3 (B)**：
> 雖然我朋友這個物種\n很難理解我們的力量\n我可以跟你保證，艦長\n我們有限的能力是相當真實的。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #162 · `GENERAL_INFO_43` · 🟡 minor voice cleanup (ratio=0.97)

**英文原文**：
> Oh, yeah! Remember that time\nyou said you could fix our broken chronometers\nwith your `sympathetic psionic waves'?\nMore like `pathetic waves' if you ask me!\nNyark! Nyark! Nyark!

**Shipped v0.5.2 (A)**：
> 喔對啊！ 記得那次\n你說你用你的「共感靈能波」\n可以修好吾等故障的計時器嗎？\n要我說根本是「可悲能波」！\n嘿嘿嘿！（Nyark! Nyark! Nyark!）

**Rebuild v3 (B)**：
> 喔對啊！ 記得那次\n你說你用你的「共感靈能波」\n可以修好我們故障的計時器嗎？\n要我說根本是「可悲能波」！\n嘿嘿嘿！（Nyark! Nyark! Nyark!）

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #163 · `GENERAL_INFO_44` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.62)

**英文原文**：
> Even through all this negative energy, Captain\nwe have discovered that...

**Shipped v0.5.2 (A)**：
> 即便穿過所有這些負面能量,艦長\n吾等發現了……

**Rebuild v3 (B)**：
> 就算隔著這些負面能量，艦長\n我們也發現了……

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #164 · `GENERAL_INFO_45` · 🟡 微調 (ratio=0.78)

**英文原文**：
> ...and THEN there was the time\nyou said you could bend dorfs with just your...

**Shipped v0.5.2 (A)**：
> ……然後還有那次\n你說你可以只用……彎折多爾夫（dorfs）……

**Rebuild v3 (B)**：
> ……然「後」還有那次\n你說你可以只靠意志力就把多爾夫（dorfs）彎折……

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #165 · `GENERAL_INFO_48` · 🟠 措辭改變 (ratio=0.68)

**英文原文**：
> As I was saying, before I was so RUDELY interrupted!...

**Shipped v0.5.2 (A)**：
> 如我方才所說,在我被如此「無禮」地打斷之前！……

**Rebuild v3 (B)**：
> 如我剛剛所說，在我被人「粗魯地」打斷之前！……

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #166 · `GENERAL_INFO_49` · 🟡 微調 (ratio=0.92)

**英文原文**：
> I said I was sorry.

**Shipped v0.5.2 (A)**：
> 我說了抱歉了。

**Rebuild v3 (B)**：
> 我說了抱歉。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #167 · `GENERAL_INFO_410` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.71)

**英文原文**：
> Our most talented Seers have detected\nsome ominous and powerful meta-psychic signals\nfrom the direction of the <% comm.getConstellation("Orionis", "talking pet") %> constellation.

**Shipped v0.5.2 (A)**：
> 吾等最有天份的占卜者已偵測到\n一些不祥而強大的超心靈訊號\n來自 <% comm.getConstellation("獵戶座", "talking pet") %>（Orionis） 星座方向。

**Rebuild v3 (B)**：
> 我們最厲害的占卜者偵測到\n從 <% comm.getConstellation("獵戶座", "talking pet") %> 星座方向\n傳來一些不祥又強大的超心靈訊號。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #168 · `GENERAL_INFO_411` · 🟠 措辭改變 短句 (ratio=0.43)

**英文原文**：
> Faker.

**Shipped v0.5.2 (A)**：
> 騙子。

**Rebuild v3 (B)**：
> 騙子。（Faker.）

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #169 · `any_war_news` · 🟠 措辭改變 短句 (ratio=0.69)

**英文原文**：
> Any news about the war between the two alien races?

**Shipped v0.5.2 (A)**：
> 有兩個異族之間戰爭的任何消息嗎？

**Rebuild v3 (B)**：
> 有沒有關於兩個外星種族之間戰爭的消息？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #170 · `UTWIG_DELAY0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.70)

**英文原文**：
> Our scouts have witnessed an exciting event\nin the <% comm.getConstellation("Horologii", "samatra") %> star system.

**Shipped v0.5.2 (A)**：
> 吾等偵察兵目睹了一場令人振奮的事件\n於 <% comm.getConstellation("時鐘座", "samatra") %>（Horologii） 星系中。

**Rebuild v3 (B)**：
> 我們的偵察兵在 <% comm.getConstellation("時鐘座", "samatra") %> 星系裡\n目擊了一件令人興奮的事。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #171 · `UTWIG_DELAY1` · 🟡 微調 (ratio=0.80)

**英文原文**：
> Yeah! Big news!

**Shipped v0.5.2 (A)**：
> 耶！ 大新聞！

**Rebuild v3 (B)**：
> 沒錯！ 大新聞！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #172 · `UTWIG_DELAY2` · 🔴 語意/voice 差異大 (ratio=0.31)

**英文原文**：
> Two alien races have entered that region of space\nfrom the <% comm.getConstellation("coreward", "utwig") %> direction.

**Shipped v0.5.2 (A)**：
> 有兩支異族自銀核方向（coreward）\n進入了那片太空區域。

**Rebuild v3 (B)**：
> 兩個外星種族從 <% comm.getConstellation("銀核方向", "utwig") %>\n進入那片星域。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #173 · `UTWIG_DELAY3` · 🟡 微調 (ratio=0.84)

**英文原文**：
> One of the races look like big talkin' weeds\nand the other wears a funny mask.

**Shipped v0.5.2 (A)**：
> 其中一族看起來像會說話的大雜草\n另一族則戴著怪異面具。

**Rebuild v3 (B)**：
> 其中一族看起來像會講話的巨大雜草\n另一族戴著搞笑的面具。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #174 · `UTWIG_DELAY4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.77)

**英文原文**：
> And they are attacking our enemies!

**Shipped v0.5.2 (A)**：
> 而他們正攻擊吾等的敵人！

**Rebuild v3 (B)**：
> 而且他們正在攻擊我們的敵人！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #175 · `UTWIG_DELAY5` · 🟡 微調 (ratio=0.81)

**英文原文**：
> Well, ONE of our enemies, anyway.

**Shipped v0.5.2 (A)**：
> 呃,反正是「其中一個」敵人。

**Rebuild v3 (B)**：
> 呃，反正是其中一個敵人啦。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #176 · `UTWIG_DELAY6` · 🔴 語意/voice 差異大 (ratio=0.38)

**英文原文**：
> Yes, the new aliens seem to be confining their hostilities\nto the sinister Kohr-Ah.

**Shipped v0.5.2 (A)**：
> 是的,這批新異族似乎將敵意\n限縮於陰森的柯亞。

**Rebuild v3 (B)**：
> 是啊，這些新來的外星人似乎只針對\n那個陰險的柯亞展開攻擊。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #177 · `UTWIG_DELAY7` · 🟠 措辭改變 短句 (ratio=0.74)

**英文原文**：
> Actually, that's good news.

**Shipped v0.5.2 (A)**：
> 其實這是好消息。

**Rebuild v3 (B)**：
> 說實在的，這是好消息。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #178 · `UTWIG_DELAY8` · 🔴 語意/voice 差異大 (ratio=0.39)

**英文原文**：
> By focusing on the Kohr-Ah\nwho have been winning their war up to this point...

**Shipped v0.5.2 (A)**：
> 因為專攻柯亞\n那些至今為止一直在打贏戰爭之族……

**Rebuild v3 (B)**：
> 他們專打柯亞\n目前為止在戰爭中一直佔上風的正是柯亞……

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #179 · `UTWIG_DELAY9` · 🟡 微調 (ratio=0.90)

**英文原文**：
> They've been plastering the Ur-Quan.

**Shipped v0.5.2 (A)**：
> 他們一直在痛擊烏寬。

**Rebuild v3 (B)**：
> 他們一直在痛扁烏寬。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #180 · `UTWIG_DELAY10` · 🟠 措辭改變 短句 (ratio=0.52)

**英文原文**：
> The balance of power has been equalized somewhat...

**Shipped v0.5.2 (A)**：
> 戰爭力量的平衡稍微被拉回了……

**Rebuild v3 (B)**：
> 這樣力量平衡就多少扳回一些了……

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #181 · `UTWIG_DELAY11` · 🟠 措辭改變 短句 (ratio=0.72)

**英文原文**：
> But the Kohr-Ah will STILL probably win!

**Shipped v0.5.2 (A)**：
> 但柯亞「大概」還是會贏！

**Rebuild v3 (B)**：
> 但柯亞「還是」很可能會贏！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #182 · `UTWIG_DELAY12` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.71)

**英文原文**：
> But we estimate that the efforts of these new alien races\nhas delayed the Kohr-Ah's eventual victory\nby nine to twelve months.

**Shipped v0.5.2 (A)**：
> 但吾等估計這批新異族的努力\n將柯亞最終的勝利\n延遲了九到十二個月。

**Rebuild v3 (B)**：
> 不過我們估計，這些新來的外星種族的努力\n把柯亞最終的勝利\n往後延了九到十二個月。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #183 · `UTWIG_DELAY13` · 🟡 微調 (ratio=0.86)

**英文原文**：
> Still, it's better than nothing!

**Shipped v0.5.2 (A)**：
> 但總比沒有好！

**Rebuild v3 (B)**：
> 有總比沒有好！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #184 · `KOHRAH_WINNING0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.68)

**英文原文**：
> We have modified a few of our Stinger starships\nfor long-range reconnaissance missions.

**Shipped v0.5.2 (A)**：
> 吾等改裝了幾艘刺針號\n用於長程偵察任務。

**Rebuild v3 (B)**：
> 我們改裝了幾艘「刺針號」星艦\n讓它們執行長程偵察任務。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #185 · `KOHRAH_WINNING1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.79)

**英文原文**：
> We strapped a bunch of fuel tanks on their hulls.

**Shipped v0.5.2 (A)**：
> 吾等在其船殼綁了一堆燃料罐。

**Rebuild v3 (B)**：
> 我們在船殼上綁了一堆燃料罐。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #186 · `KOHRAH_WINNING2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.47)

**英文原文**：
> The scouts were ordered to investigate the progress of the war\nbetween the green ships, who we now know as the `Ur-Quan'\nand the black ships, flown by the `Kohr-Ah'.

**Shipped v0.5.2 (A)**：
> 偵察兵奉命調查\n綠色艦艇(吾等現稱為「烏寬」)\n與黑色艦艇(駕駛者為「柯亞」)之間的戰情進展。

**Rebuild v3 (B)**：
> 偵察兵奉命調查那場戰爭的進展\n綠船一方，我們現在知道叫「烏寬」\n黑船那邊，是「柯亞」駕駛的。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #187 · `KOHRAH_WINNING3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.55)

**英文原文**：
> We sent out ten... two came back

**Shipped v0.5.2 (A)**：
> 吾等派出十艘…… 兩艘回來

**Rebuild v3 (B)**：
> 我們派了十艘出去…… 回來了兩艘

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #188 · `KOHRAH_WINNING4` · 🟠 措辭改變 短句 (ratio=0.67)

**英文原文**：
> But the information they gathered was worth the cost.

**Shipped v0.5.2 (A)**：
> 但他們蒐集的情報值得付出這代價。

**Rebuild v3 (B)**：
> 但他們收集到的情報值回票價。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #189 · `KOHRAH_WINNING5` · 🟡 微調 (ratio=0.98)

**英文原文**：
> Unless you were one of the scouts, I suppose?\nNyark! Nyark! Nyark!

**Shipped v0.5.2 (A)**：
> 除非你就是那些偵察兵之一,我猜？\n嘿嘿嘿！（Nyark! Nyark! Nyark!）

**Rebuild v3 (B)**：
> 除非你就是那些偵察兵之一，我猜？\n嘿嘿嘿！（Nyark! Nyark! Nyark!）

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #190 · `KOHRAH_WINNING8` · 🟠 措辭改變 (ratio=0.63)

**英文原文**：
> Anyway, as I was saying, the intelligence they gathered\nindicates that the Kohr-Ah will win their war\nsometime near the beginning of the year 2158.

**Shipped v0.5.2 (A)**：
> 無論如何,如我所說的,他們蒐集的情報\n指出柯亞將在 2158 年年初\n贏得他們的戰爭。

**Rebuild v3 (B)**：
> 總之，如我剛剛所說，他們收集到的情報\n顯示柯亞會在\n2158 年年初左右贏得那場戰爭。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #191 · `KOHRAH_WINNING9` · 🔴 語意/voice 差異大 (ratio=0.42)

**英文原文**：
> Unless someone evens up the alien forces\nby destroying about a bazillion Kohr-Ah ships.

**Shipped v0.5.2 (A)**：
> 除非有人挺身而出\n炸毀大約幾十億艘柯亞戰艦來扳平雙方戰力。

**Rebuild v3 (B)**：
> 除非有人幫忙扳平外星勢力\n把大概一萬億艘柯亞的艦艇打爆。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #192 · `URQUAN_NEARLY_GONE0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.64)

**英文原文**：
> Our reconnaissance ships have returned once more

**Shipped v0.5.2 (A)**：
> 吾等偵察艦又一次歸來

**Rebuild v3 (B)**：
> 我們的偵察艦又一次回來了

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #193 · `URQUAN_NEARLY_GONE2` · 🟡 微調 (ratio=0.94)

**英文原文**：
> Based on what they have seen\nthe Kohr-Ah will defeat the Ur-Quan\nin less than six months.

**Shipped v0.5.2 (A)**：
> 根據他們所見\n柯亞將在不到六個月內\n擊敗烏寬。

**Rebuild v3 (B)**：
> 根據他們的所見\n柯亞會在不到六個月內\n擊敗烏寬。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #194 · `URQUAN_NEARLY_GONE3` · 🟠 措辭改變 短句 (ratio=0.40)

**英文原文**：
> Bummer.

**Shipped v0.5.2 (A)**：
> 糟啊。

**Rebuild v3 (B)**：
> 糟啊。（Bummer.）

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #195 · `URQUAN_NEARLY_GONE4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.70)

**英文原文**：
> And based on our last encounter with the Kohr-Ah\nwe expect that when they win their war with the Ur-Quan\nthe Kohr-Ah will move through this entire region of space\ndestroying all intelligent life.

**Shipped v0.5.2 (A)**：
> 而根據吾等上次與柯亞遭遇的經驗\n吾等預期他們一贏了與烏寬的戰爭\n柯亞就會橫掃這整片太空區域\n毀滅所有智慧生命。

**Rebuild v3 (B)**：
> 而且根據我們上次跟柯亞的接觸\n我們預估他們贏得跟烏寬的戰爭後\n柯亞會橫掃這整片星域\n毀滅所有有智慧的生命。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #196 · `URQUAN_NEARLY_GONE5` · 🟡 微調 (ratio=0.97)

**英文原文**：
> Major bummer!

**Shipped v0.5.2 (A)**：
> 大糟糕！（Major bummer!）

**Rebuild v3 (B)**：
> 大糟糕啦！（Major bummer!）

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #197 · `KOHRAH_FRENZY0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.51)

**英文原文**：
> I fear we have received our last scouting reports, Captain.

**Shipped v0.5.2 (A)**：
> 恐怕吾等已收到最後一批偵察報告了,艦長。

**Rebuild v3 (B)**：
> 艦長，恐怕我們收到偵察兵最後的報告了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #198 · `KOHRAH_FRENZY1` · 🟠 措辭改變 (ratio=0.60)

**英文原文**：
> Poor Yip, Tun and Haffy! I'll really miss those guys!

**Shipped v0.5.2 (A)**：
> 可憐的葉普（Yip）、屯（Tun）和哈菲（Haffy）！ 我真的會很想念他們！

**Rebuild v3 (B)**：
> 可憐的葉普、屯跟哈菲！ 我真的會很想念那些傢伙！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #199 · `KOHRAH_FRENZY2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.46)

**英文原文**：
> Although none of our scouts returned home alive

**Shipped v0.5.2 (A)**：
> 雖然吾等偵察兵無一活著回來

**Rebuild v3 (B)**：
> 我們沒有一個偵察兵活著回家

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #200 · `KOHRAH_FRENZY3` · 🟠 措辭改變 (ratio=0.67)

**英文原文**：
> ...and Jiff... and Fod... and (sniff!)...\n...and my best pal, Rogi!

**Shipped v0.5.2 (A)**：
> ……還有吉夫（Jiff）……還有佛德（Fod）……還有（啜泣！）……\n……以及我最好的哥們,羅吉（Rogi）！

**Rebuild v3 (B)**：
> ……還有吉夫…… 還有佛德…… 還有（啜泣！）（sniff!）……\n……還有我最好的哥兒們，羅吉！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #201 · `KOHRAH_FRENZY4` · 🟠 措辭改變 (ratio=0.72)

**英文原文**：
> They were able to send a last message.\nThe Kohr-Ah have won their war against the Ur-Quan\nand they have begun their hideous death march.

**Shipped v0.5.2 (A)**：
> 他們送出了最後一則訊息。\n柯亞贏得對抗烏寬的戰爭\n且他們已開始其恐怖的死亡進軍。

**Rebuild v3 (B)**：
> 他們終究是送出了最後一則訊息。\n柯亞打贏了對烏寬的戰爭\n然後展開了他們醜惡的死亡行軍。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #202 · `KOHRAH_FRENZY6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.66)

**英文原文**：
> The only piece of knowledge we have\nthat may help you defeat them\nis a fragment of a transmission we received\nfrom our agent Buppo who was in the <% comm.getConstellation("Crateris", "samatra") %> constellation.

**Shipped v0.5.2 (A)**：
> 吾等所知能幫您擊敗他們的\n唯一情報片段\n乃是吾等收到的一段傳訊片段\n來自吾等派駐 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris） 星座之特工布波（Buppo）。

**Rebuild v3 (B)**：
> 我們僅有的一項知識\n或許能助你擊敗他們\n那是一段殘破的訊息，來自我們駐 <% comm.getConstellation("巨爵座", "samatra") %> 星座\n那位特工布波所發送。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #203 · `KOHRAH_FRENZY7` · 🟠 措辭改變 (ratio=0.73)

**英文原文**：
> They got Buppo too?!...(SOB!)

**Shipped v0.5.2 (A)**：
> 他們把布波也解決了？！……（嗚咽！）

**Rebuild v3 (B)**：
> 他們連布波也殺了？！……（嗚咽！）（SOB!）

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #204 · `KOHRAH_FRENZY8` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.71)

**英文原文**：
> He reported that the Kohr-Ah had something\n`big, dangerous and important as hell'\nin one of the nearby star systems.\nThat was all we got before Buppo's signal was cut off.

**Shipped v0.5.2 (A)**：
> 他回報柯亞擁有一件\n「巨大、危險又要命重要之物」\n就在附近某星系裡。\n那是布波訊號中斷前吾等收到的所有內容。

**Rebuild v3 (B)**：
> 他報告說柯亞有樣東西\n「又大又危險又重要得要命」\n就在附近某個恆星系裡。\n這是布波訊號中斷前我們收到的全部內容。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #205 · `KOHRAH_FRENZY10` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.62)

**英文原文**：
> You have got to stop the Kohr-Ah, Captain!...\n...before they kill us all.

**Shipped v0.5.2 (A)**：
> 您必須阻止柯亞,艦長！……\n……在他們殺光吾等所有人之前。

**Rebuild v3 (B)**：
> 艦長，你一定要阻止柯亞！……\n……在他們把我們全殺光之前。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #206 · `NO_WAR_NEWS0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.55)

**英文原文**：
> No. We have nothing new to report.

**Shipped v0.5.2 (A)**：
> 沒有。 吾等沒有新消息可報。

**Rebuild v3 (B)**：
> 沒。 我們沒什麼新的可以報告。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #207 · `NO_WAR_NEWS1` · 🟠 措辭改變 短句 (ratio=0.67)

**英文原文**：
> Nope! Not a thing.

**Shipped v0.5.2 (A)**：
> 沒！ 一件也沒有。

**Rebuild v3 (B)**：
> 沒有！ 完全沒有。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #208 · `i_want_alliance` · 🟡 微調 (ratio=0.77)

**英文原文**：
> I have travelled here to seek an alliance between our peoples.

**Shipped v0.5.2 (A)**：
> 我方遠道而來,是為在我方兩族之間尋求聯盟。

**Rebuild v3 (B)**：
> 我方遠道而來，是要在我們兩個民族之間尋求結盟。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #209 · `GOOD0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> How wonderful! We accept!

**Shipped v0.5.2 (A)**：
> 太美妙了！ 吾等接受！

**Rebuild v3 (B)**：
> 太好了！ 我們接受！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #210 · `GOOD2` · 🔴 語意/voice 差異大 (ratio=0.22)

**英文原文**：
> How marvelous!

**Shipped v0.5.2 (A)**：
> 何等壯麗！

**Rebuild v3 (B)**：
> 太棒了！

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #211 · `GOOD4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.42)

**英文原文**：
> Captain, we are delighted that your people have made this choice!

**Shipped v0.5.2 (A)**：
> 艦長,吾等很欣慰您的族類做了此選擇！

**Rebuild v3 (B)**：
> 艦長，我們很高興你們的人民做出這個選擇！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #212 · `GOOD5` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> Now WE won't get slaughtered!

**Shipped v0.5.2 (A)**：
> 這下「吾等」就不會被屠殺了！

**Rebuild v3 (B)**：
> 現在「我們」不會被屠殺了！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #213 · `GOOD6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.54)

**英文原文**：
> In exchange for our cooperation helping you with captains and ship designs\nall that we ask for is your protection.

**Shipped v0.5.2 (A)**：
> 作為協助您提供艦長與艦艇設計的交換\n吾等所求的僅是您的保護。

**Rebuild v3 (B)**：
> 作為交換，我們合作提供艦長跟艦艇設計\n我們只要求你的保護。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #214 · `GOOD7` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.70)

**英文原文**：
> So we don't get slaughtered!

**Shipped v0.5.2 (A)**：
> 這樣吾等就不會被屠殺了！

**Rebuild v3 (B)**：
> 這樣我們才不會被屠殺！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #215 · `GOOD8` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.54)

**英文原文**：
> We shall begin fulfilling our commitment at once!\nWe will transport officers and our Stinger design to your base immediately!

**Shipped v0.5.2 (A)**：
> 吾等將立即開始履行承諾！\n吾等將立即將軍官與刺針號設計送至您的基地！

**Rebuild v3 (B)**：
> 我們馬上開始履行約定！\n我們馬上把軍官跟刺針號設計運送到你的基地！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #216 · `GOOD9` · 🟡 微調 (ratio=0.76)

**英文原文**：
> Why, heck!\nMaybe I'll even make the trip to your planet!\nI'd make a good starship captain, Captain!\nI'm pretty darn mean in a fight\nand there ain't nobody better than me\nwith a thrusting stinger tongue attack!

**Shipped v0.5.2 (A)**：
> 嘿,可惡！\n說不定我也會親自跑一趟到您的星球！\n我一定會是個好星艦艦長,艦長！\n打起架來我可兇了\n而且沒人比我更擅長\n突進刺針舌攻擊！

**Rebuild v3 (B)**：
> 哎唷！\n說不定我還要親自跑一趟你的星球！\n我會是個好星艦艦長的，艦長！\n我打起架來還挺兇的\n而且沒人比得過我的\n突進刺針舌攻擊！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #217 · `want_specific_info` · 🟡 微調 (ratio=0.78)

**英文原文**：
> I would like some specific information.

**Shipped v0.5.2 (A)**：
> 我方想要一些具體資訊。

**Rebuild v3 (B)**：
> 我方想要一些具體的情報。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #218 · `WHAT_SPECIFIC_INFO0` · 🟡 微調 (ratio=0.91)

**英文原文**：
> Sure. What do you want to know?

**Shipped v0.5.2 (A)**：
> 當然。 您想知道什麼？

**Rebuild v3 (B)**：
> 當然。 你想知道什麼？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #219 · `enough_info` · 🟠 措辭改變 短句 (ratio=0.44)

**英文原文**：
> That's enough info for now, thanks!

**Shipped v0.5.2 (A)**：
> 現在資訊夠了,謝了！

**Rebuild v3 (B)**：
> 情報夠了，謝啦！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #220 · `OK_ENOUGH_INFO` · 🟠 措辭改變 短句 (ratio=0.46)

**英文原文**：
> Anything else?

**Shipped v0.5.2 (A)**：
> 還需要什麼嗎？

**Rebuild v3 (B)**：
> 還有別的嗎？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #221 · `what_about_others` · 🟡 微調 (ratio=0.79)

**英文原文**：
> What do you know about other alien races?

**Shipped v0.5.2 (A)**：
> 你們對其他異族物種了解多少？

**Rebuild v3 (B)**：
> 你們對其他外星種族了解多少？

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #222 · `ABOUT_OTHERS0` · 🟡 微調 (ratio=0.86)

**英文原文**：
> Not much, to tell the truth.

**Shipped v0.5.2 (A)**：
> 老實說,不多。

**Rebuild v3 (B)**：
> 老實說，不多。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #223 · `ABOUT_OTHERS1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.56)

**英文原文**：
> This space exploration stuff is kinda new to us.

**Shipped v0.5.2 (A)**：
> 這太空探索的事對吾等而言是新鮮事。

**Rebuild v3 (B)**：
> 這種太空探索的事情對我們來說還挺新的。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #224 · `ABOUT_OTHERS2` · 🟠 措辭改變 短句 (ratio=0.70)

**英文原文**：
> Besides the green alien ships...

**Shipped v0.5.2 (A)**：
> 除了綠色異族艦艇……

**Rebuild v3 (B)**：
> 除了綠色的外星艦……

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #225 · `ABOUT_OTHERS3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.75)

**英文原文**：
> Which have only tried to kill us.

**Shipped v0.5.2 (A)**：
> 他們只想殺吾等。

**Rebuild v3 (B)**：
> 他們只想殺我們。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #226 · `ABOUT_OTHERS4` · 🟠 措辭改變 短句 (ratio=0.61)

**英文原文**：
> ...and the black alien ships...

**Shipped v0.5.2 (A)**：
> ……以及黑色異族艦艇……

**Rebuild v3 (B)**：
> ……跟黑色的外星艦……

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #227 · `ABOUT_OTHERS5` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.53)

**英文原文**：
> Which have actually been QUITE SUCCESSFUL at killing us.

**Shipped v0.5.2 (A)**：
> 他們在殺吾等這事上「相當成功」。

**Rebuild v3 (B)**：
> 他們殺我們殺得「非常成功」。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #228 · `ABOUT_OTHERS6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.65)

**英文原文**：
> The only other starships we have encountered\nare strange tumbling red probes\nwhich profess to be on a peaceful mission...

**Shipped v0.5.2 (A)**：
> 吾等唯一遭遇過的其他星艦\n是奇怪的翻滾紅色探測器\n聲稱它們的任務是和平的……

**Rebuild v3 (B)**：
> 我們遇過的唯一其他星艦\n是些奇怪、翻滾著的紅色探測器\n口口聲聲說是和平任務……

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #229 · `ABOUT_OTHERS7` · 🟡 微調 (ratio=0.88)

**英文原文**：
> ...but then attack like slavering Zebrankys.

**Shipped v0.5.2 (A)**：
> ……但接著就像流著口水的澤布蘭基一樣攻擊。

**Rebuild v3 (B)**：
> ……然後就像流著口水的澤布蘭基一樣攻擊。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #230 · `ABOUT_OTHERS8` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.71)

**英文原文**：
> We believe that the probes are actually robotic scouts\nwhich have suffered some kind of malfunction\nresulting in their aberrant behavior.

**Shipped v0.5.2 (A)**：
> 吾等相信這些探測器實為機器人偵察兵\n遭遇了某種故障\n導致其異常行為。

**Rebuild v3 (B)**：
> 我們相信那些探測器其實是機器人偵察兵\n出了某種故障\n才導致它們行為異常。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #231 · `ABOUT_OTHERS9` · 🟡 微調 (ratio=0.88)

**英文原文**：
> And what's worse, they are multiplying.

**Shipped v0.5.2 (A)**：
> 而更糟的是,它們正在繁殖。

**Rebuild v3 (B)**：
> 更糟的是，它們正在繁殖。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #232 · `ABOUT_OTHERS10` · 🟡 微調 (ratio=0.83)

**英文原文**：
> Yes, that's true.\nThe probes seem to be replicating at a geometric rate.

**Shipped v0.5.2 (A)**：
> 是的,那是真的。\n那些探測器似乎正以幾何級數複製。

**Rebuild v3 (B)**：
> 是啊，這是真的。\n探測器似乎正以幾何級數複製。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #233 · `ABOUT_OTHERS11` · 🟡 微調 (ratio=0.78)

**英文原文**：
> AIEE! That means if there was only one last week\nthen next month... ah\nwait a minute... let me calculate\nuh\nThat means, next month there will be\n...A WHOLE MESS OF THOSE THINGS!

**Shipped v0.5.2 (A)**：
> 啊咦！（AIEE!） 那表示如果上週只有一個\n那下個月…… 啊\n等一下…… 讓我算算\n呃\n那表示下個月會有\n……「一大堆那玩意兒」！

**Rebuild v3 (B)**：
> 啊咦！（AIEE!） 那意思是如果上禮拜只有一台\n那下個月…… 啊\n等等…… 讓我算算\n呃\n意思是，下個月會有\n……「一整片那種東西」！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #234 · `ABOUT_OTHERS12` · 🟡 minor voice cleanup (ratio=0.87)

**英文原文**：
> By back-tracing the probes' course paths\nwe have been able to calculate\nthat the source of the probes\nis somewhere <% comm.swapIfSeeded("on a direct line", "in the") %>...\n...<% comm.getConstellation("that includes our star, and", "slylandro") %><%comm.swapIfSeeded(" Epsilon Muscae", " system") %>.

**Shipped v0.5.2 (A)**：
> 透過回溯探測器的航跡\n吾等已能計算出\n那些探測器的來源\n在某處 <% comm.swapIfSeeded("就在一條直線上", "就在") %>……\n……<% comm.getConstellation("包括吾等之星,以及", "slylandro") %><%comm.swapIfSeeded(" 蒼蠅座ε", " 星系") %>。

**Rebuild v3 (B)**：
> 藉由回溯探測器的航跡\n我們算得出來\n探測器的來源\n是在 <% comm.swapIfSeeded("直線通向", "在") %>……\n……<% comm.getConstellation("包含我們恆星系，還有", "slylandro") %><%comm.swapIfSeeded(" 蒼蠅座ε", " 星系裡") %>。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #235 · `ABOUT_OTHERS13` · 🟠 措辭改變 短句 (ratio=0.56)

**英文原文**：
> Go get 'em, Captain!

**Shipped v0.5.2 (A)**：
> 去解決它們,艦長！

**Rebuild v3 (B)**：
> 去修理他們，艦長！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #236 · `what_about_zebranky` · 🟠 措辭改變 短句 (ratio=0.74)

**英文原文**：
> Tell me more about your people.

**Shipped v0.5.2 (A)**：
> 多告訴我方關於你們族類的事。

**Rebuild v3 (B)**：
> 多告訴我一點你們民族的事。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #237 · `ABOUT_ZEBRANKY2` · 🟡 微調 (ratio=0.97)

**英文原文**：
> Be quiet, you fool! He asked a serious question!\nHe doesn't want to know about Frungy.

**Shipped v0.5.2 (A)**：
> 閉嘴,笨蛋！ 他問了個嚴肅的問題！\n他不會想知道芙戎奇的事。

**Rebuild v3 (B)**：
> 閉嘴，笨蛋！ 他問了個嚴肅的問題！\n他不會想知道芙戎奇的事。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #238 · `ABOUT_ZEBRANKY3` · 🟡 微調 (ratio=0.99)

**英文原文**：
> How do you know? What makes you so smart?\nYou never even asked him if he wants to know about Frungy.\nWhy, I'll bet right now he's wondering\n`What is this wonderful sport, Frungy?', `How is it played?'\n`What kind of equipment do you need to play Frungy?'\nand `I wonder who's ahead in the Frungy Championships?'

**Shipped v0.5.2 (A)**：
> 你怎麼知道？ 你哪來的自信這麼聰明？\n你根本沒問過他想不想知道芙戎奇的事。\n哎呀,我打賭他現在正在想\n「什麼是芙戎奇這奇妙的運動？」「怎麼玩？」\n「玩芙戎奇需要什麼裝備？」\n以及「芙戎奇錦標賽現在誰領先啊？」

**Rebuild v3 (B)**：
> 你怎麼知道？ 你哪來的自信這麼聰明？\n你根本沒問過他想不想知道芙戎奇的事。\n哎呀，我打賭他現在正在想\n「什麼是芙戎奇這奇妙的運動？」「怎麼玩？」\n「玩芙戎奇需要什麼裝備？」\n以及「芙戎奇錦標賽現在誰領先啊？」

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #239 · `ABOUT_ZEBRANKY4` · 🟡 微調 (ratio=0.98)

**英文原文**：
> AUGH! Will you SHUT UP ABOUT FRUNGY?!\nIf you say another word about that STUPID GAME\nI'm going to lose control and blow a cloud of spores at you!

**Shipped v0.5.2 (A)**：
> 噁啊！（AUGH!） 你能不能「閉嘴不談芙戎奇」？！\n你要是再說一個字關於那「愚蠢遊戲」\n我就要失控,朝你噴一團孢子雲！

**Rebuild v3 (B)**：
> 噁啊！（AUGH!） 你能不能「閉嘴不談芙戎奇」？！\n你要是再說一個字關於那「愚蠢遊戲」\n我就要失控，朝你噴一團孢子雲！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #240 · `ABOUT_ZEBRANKY5` · 🟡 微調 (ratio=0.88)

**英文原文**：
> Yech! Okay, okay. Don't blow your sac.\nI won't mention Frungy again, I promise.

**Shipped v0.5.2 (A)**：
> 噁心！（Yech!） 好啦,好啦。 別搞爆你的孢子囊。\n我不再提芙戎奇了,我保證。

**Rebuild v3 (B)**：
> 噁心！（Yech!） 好啦，好啦。 別把你的孢子囊搞爆了。\n我不再提芙戎奇了，我保證。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #241 · `ABOUT_ZEBRANKY6` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.56)

**英文原文**：
> Well, Captain, as you can probably see\nour culture's predominant trait\nits greatest strength AND weakness\nis the diverse interactions between Zoq, Fot, and Pik.

**Shipped v0.5.2 (A)**：
> 呃,艦長,如您可能已看出的\n吾等文化的主要特徵\n其最大的長處「與」弱點\n即是佐格、佛特與皮克之間的多樣互動。

**Rebuild v3 (B)**：
> 呃，艦長，如你大概也看得出來\n我們文化最主要的特質\n也就是它最大的優點跟缺點\n就是佐格、佛特、皮克三方之間各式各樣的互動。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #242 · `what_about_past` · 🟠 措辭改變 短句 (ratio=0.57)

**英文原文**：
> What was your history like?

**Shipped v0.5.2 (A)**：
> 你們的歷史是怎樣的？

**Rebuild v3 (B)**：
> 你們的過去是什麼樣子？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #243 · `ABOUT_PAST0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.55)

**英文原文**：
> Our past? Quite a broad topic for this short conversation\nbut we'll share a key piece of our history with you.

**Shipped v0.5.2 (A)**：
> 吾等的過去？ 對這短短的對話而言題目太大\n但吾等會與您分享吾等歷史的一個關鍵片段。

**Rebuild v3 (B)**：
> 我們的過去？ 這麼短的對話講不完\n但我們會跟你分享一段我們歷史上的關鍵。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #244 · `ABOUT_PAST1` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.74)

**英文原文**：
> After we killed off the last Zebranky\nwe faced an interesting question.

**Shipped v0.5.2 (A)**：
> 在吾等殺光最後一隻澤布蘭基之後\n吾等面臨一個有趣的問題。

**Rebuild v3 (B)**：
> 我們宰掉最後一隻澤布蘭基之後\n面臨一個有意思的問題。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #245 · `ABOUT_PAST2` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.67)

**英文原文**：
> Should we proceed, and establish a culture\nwhich would advance in art, technology and social sophistication?...

**Shipped v0.5.2 (A)**：
> 吾等該不該前進,建立一個文化\n在藝術、科技與社會複雜度上進步？……

**Rebuild v3 (B)**：
> 我們該繼續前進，建立一個\n在藝術、科技、社會複雜度上都有發展的文化？……

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #246 · `ABOUT_PAST3` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.63)

**英文原文**：
> ...Or should we just go back into the forest\nand kick back and enjoy ourselves\nknowing that a Zebranky wasn't gonna jump out of the bush and eat us!

**Shipped v0.5.2 (A)**：
> ……還是吾等該直接回森林裡\n悠哉躺著享受自己\n知道不會有澤布蘭基從草叢跳出來吃吾等！

**Rebuild v3 (B)**：
> ……還是我們該回到森林\n放輕鬆好好享受一下\n因為知道再也不會有澤布蘭基從灌木叢裡跳出來吃我們！

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #247 · `ABOUT_PAST4` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.66)

**英文原文**：
> Well, we DID go back into the forest.\nWe stayed there for about five thousand years and had a great time...

**Shipped v0.5.2 (A)**：
> 嗯,吾等「確實」回森林去了。\n吾等在那裡待了大約五千年,過得很快樂……

**Rebuild v3 (B)**：
> 呃，我們「確實」回到森林了。\n我們在那裡待了大約五千年，玩得可爽了……

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #248 · `ABOUT_PAST5` · 🟠 措辭改變 (ratio=0.67)

**英文原文**：
> ...then, one stormy day, a Zoq, a Fot, and a Pik were walking up a steep path\nlooking for something good to eat, when a bolt of lightning struck nearby.\nWith a huge flash of light, the bolt of energy\ncarved a strangely-shaped chunk of granite out of a cliff.

**Shipped v0.5.2 (A)**：
> ……然後,某個暴風雨日,一位佐格、一位佛特、一位皮克正走上陡峭小徑\n尋找可口的食物,附近突然打下一道閃電。\n伴隨著巨大閃光,那道能量束\n從懸崖鑿出一塊形狀奇特的花崗岩。

**Rebuild v3 (B)**：
> ……然後，某個下著暴風雨的日子，一隻佐格、一隻佛特、還有一隻皮克正沿著一條陡峭的小徑往上走\n想找些好吃的東西，這時附近打下一道閃電。\n伴隨一道巨大的閃光，那道能量\n從斷崖上切下一塊形狀怪異的花崗岩。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #249 · `ABOUT_PAST6` · 🟠 措辭改變 (ratio=0.63)

**英文原文**：
> It was a disk, with a hole in the middle!\nAs the rock began to roll down the hill, toward the three terrified beings\nsome dry grass got caught in its hole, and since the rock was still hot\nthe grass caught on fire.

**Shipped v0.5.2 (A)**：
> 那是一片圓盤,中間有個洞！\n當那石塊開始朝山下滾動,朝那三位驚恐的生物滾去\n有些乾草被卡進洞裡,而由於石塊仍熾熱\n乾草便著了火。

**Rebuild v3 (B)**：
> 那是個圓盤，中間有個洞！\n當那塊石頭開始滾下山，朝三隻被嚇壞的生物滾去\n有些乾草卡進了它的洞裡，而由於那石頭還熱著\n那些草就燒起來了。

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #250 · `ABOUT_PAST7` · 🟡 微調 (ratio=0.78)

**英文原文**：
> When the rock finally got to the Zoq, the Fot, and the Pik\nthey simultaneously discovered the Wheel, Fire, and Religion\nthus catapulting them on to the road of progress.

**Shipped v0.5.2 (A)**：
> 當石塊終於滾到那佐格、佛特與皮克面前\n他們同時發現了「輪子」、「火」與「宗教」\n就此推向了進步之路。

**Rebuild v3 (B)**：
> 當那塊石頭終於滾到佐格、佛特、皮克面前時\n他們同時發現了「輪子」、「火」，以及「宗教」\n因而把他們推上了進步的道路。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #251 · `ABOUT_PAST8` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.51)

**英文原文**：
> Which has led us to this day, Captain.\nOh! How did the flaming wheel give religion to our Culture, you ask?

**Shipped v0.5.2 (A)**：
> 這一路引領吾等來到今日,艦長。\n噢！ 您問那燃燒之輪如何賜予吾等文化以宗教？

**Rebuild v3 (B)**：
> 而這一路把我們帶到了今天，艦長。\n喔！ 你問燃燒的輪子是怎麼為我們文化帶來宗教的？

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #252 · `ABOUT_PAST9` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.52)

**英文原文**：
> I will explain.\nYou see, when it got to the threesome, the flaming wheel was going at a pretty good clip\nand it ran smack into the Zoq, killing him.

**Shipped v0.5.2 (A)**：
> 吾將解釋。\n您瞧,當它滾到那三位面前時,燃燒之輪速度已相當快\n並直接撞上那位佐格,將他撞死了。

**Rebuild v3 (B)**：
> 我來說明。\n你看，當它到達三個小傢伙面前時，燃燒的輪子跑得挺快\n然後就直直撞上那隻佐格，把他撞死了。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #253 · `ABOUT_PAST10` · 🟡 微調 (ratio=0.79)

**英文原文**：
> The Fot and the Pik felt so bad\nthey really liked that Zoq!...\n...that they decided the Zoq hadn't really died when the wheel flattened him\nhe had just gone to `a better place.'

**Shipped v0.5.2 (A)**：
> 佛特與皮克覺得非常難過\n他們真的很喜歡那位佐格！……\n……於是他們決定,佐格並沒有真的因輪子輾過而死\n他只是去了「一個更好的地方」。

**Rebuild v3 (B)**：
> 那隻佛特跟那隻皮克覺得非常難過\n他們真的很喜歡那隻佐格！……\n……他們就認定那隻佐格被輪子壓扁時並沒有真的死掉\n他只是去了「一個更好的地方」。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #254 · `ABOUT_PAST11` · 🟡 微調 (ratio=0.79)

**英文原文**：
> Presumably one without lethal flaming wheels.

**Shipped v0.5.2 (A)**：
> 推想那是個沒有致命燃燒之輪的地方。

**Rebuild v3 (B)**：
> 大概是個沒有致命燃燒輪子的地方。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #255 · `what_about_stinger` · 🟠 措辭改變 (ratio=0.64)

**英文原文**：
> Can you describe your `Stinger' starship?

**Shipped v0.5.2 (A)**：
> 能形容一下你們的「刺針號」星艦嗎？

**Rebuild v3 (B)**：
> 可以描述一下你們的「刺針號」（Stinger）星艦嗎？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #256 · `ABOUT_STINGER0` · ✨ voice/canonical upgrade (吾/爾/之/莫→我/你/的/別; ratio=0.64)

**英文原文**：
> The Stinger is the peak of our technological prowess.

**Shipped v0.5.2 (A)**：
> 刺針號乃吾等科技實力之巔峰。

**Rebuild v3 (B)**：
> 刺針號是我們技術實力的巔峰。

**推薦**：**B (v3)** — voice/canonical dossier v0.7 §四 統一升級

**你的選擇**：A / B / C（自訂）

---

### #257 · `ABOUT_STINGER2` · 🔴 語意/voice 差異大 (ratio=0.54)

**英文原文**：
> These vessels are cheap to build\nand can be quite effective in short range combat.

**Shipped v0.5.2 (A)**：
> 這種艦艇建造便宜\n在近距離戰鬥中可相當有效。

**Rebuild v3 (B)**：
> 這些艦艇造起來便宜\n短程作戰也挺有效。

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #258 · `ABOUT_STINGER3` · 🔴 語意/voice 差異大 (ratio=0.48)

**英文原文**：
> They turn on a... on a\nwell a small round thing that's REAL small!

**Shipped v0.5.2 (A)**：
> 它們可以在一個…… 一個上面轉彎\n嗯就是一個「非常小」的小圓東西上！

**Rebuild v3 (B)**：
> 它們的迴轉半徑就像…… 就像\n呃，某個「非常」小的圓形東西那樣小！

**推薦**：**依語意檢視選 A 或 B**

**你的選擇**：A / B / C（自訂）

---

### #259 · `ABOUT_STINGER4` · 🟡 微調 (ratio=0.79)

**英文原文**：
> Remember though, against most ships\nthe Stinger must close distance immediately\nand give unrelenting tongue attacks\nuntil either the enemy or the Stinger are destroyed.

**Shipped v0.5.2 (A)**：
> 但要記住,面對大多數艦艇\n刺針號必須立即拉近距離\n並不斷施展舌尖攻擊\n直到敵艦或刺針號被摧毀。

**Rebuild v3 (B)**：
> 但要記住，面對大多數艦艇\n刺針號必須立刻拉近距離\n然後不斷發動舌攻擊\n直到敵人或刺針號其中一方被毀為止。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #260 · `ABOUT_STINGER5` · 🟡 微調 (ratio=0.79)

**英文原文**：
> Yeah! The tonguing is the best part!

**Shipped v0.5.2 (A)**：
> 耶！ 用舌頭是最爽的部分！

**Rebuild v3 (B)**：
> 沒錯！ 用舌頭捅是最讚的部分！

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #261 · `what_about_guy_in_back` · 🟠 措辭改變 短句 (ratio=0.53)

**英文原文**：
> Does that guy in back ever say anything?

**Shipped v0.5.2 (A)**：
> 後面那位傢伙從來都沒說過話嗎？

**Rebuild v3 (B)**：
> 那後面那位到底有沒有講過話啊？

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---

### #262 · `ABOUT_GUY0` · 🟡 微調 (ratio=0.80)

**英文原文**：
> Nope.

**Shipped v0.5.2 (A)**：
> 沒有。

**Rebuild v3 (B)**：
> 沒。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #263 · `ABOUT_GUY1` · 🟡 微調 (ratio=0.92)

**英文原文**：
> Not a word.

**Shipped v0.5.2 (A)**：
> 一個字都沒。

**Rebuild v3 (B)**：
> 一個字都沒有。

**推薦**：**B (v3)** — voice cleanup 為主 · 意義等價

**你的選擇**：A / B / C（自訂）

---

### #264 · `OUT_TAKES4` · 🟠 措辭改變 (ratio=0.71)

**英文原文**：
> Frungy had nothing to do with it!\nThis game was about war, slavery, intolerance\nheroism, justice, and the inevitable triumph of Good over Evil!

**Shipped v0.5.2 (A)**：
> 芙戎奇跟本遊戲一點關係也沒有！\n本遊戲主題是戰爭、奴役、不寬容\n英雄主義、正義,以及正義必勝之必然！

**Rebuild v3 (B)**：
> 苙戎奇跟本遊戲一點關係也沒有！\n本遊戲主題是戰爭、奴役、偏執\n英雄氣概、正義，還有善終將戰勝惡！

**推薦**：**B (v3)** — voice + 台化順暢 · 讀順度更佳

**你的選擇**：A / B / C（自訂）

---


## 附錄 · 全 Green (identical) 清單

`WE_ARE6`, `SCOUT_HELLO3`, `which_fot`, `HE_IS0`, `HE_IS7`, `WE_GLAD1`, `WE_GLAD3`, `WE_GLAD5`, `TOLD_YOU1`, `TOLD_YOU5`, `TOLD_YOU7`, `YEARS_AGO1`, `YEARS_AGO2`, `YEARS_AGO3`, `YEARS_AGO4`, `YEARS_AGO5`, `where_from`, `TRAVELED_FAR5`, `what_emergency`, `UNDER_ATTACK3`, `UNDER_ATTACK4`, `UNDER_ATTACK6`, `UNDER_ATTACK8`, `UNDER_ATTACK10`, `NOT_HELPFUL3`, `what_look_like`, `LOOK_LIKE0`, `LOOK_LIKE3`, `valuable_info`, `GOODBYE1`, `SEE_TOLD_YOU0`, `how_can_i_help`, `ALLY_WITH_US1`, `ALLY_WITH_US4`, `WE_ALLY3`, `THANKS_FOR_RESCUE3`, `THANKS_FOR_RESCUE5`, `GENERAL_INFO_21`, `GENERAL_INFO_46`, `GENERAL_INFO_47`, `KOHRAH_WINNING6`, `KOHRAH_WINNING7`, `URQUAN_NEARLY_GONE1`, `KOHRAH_FRENZY5`, `KOHRAH_FRENZY9`, `KOHRAH_FRENZY11`, `GOOD1`, `GOOD3`, `WHAT_SPECIFIC_INFO1`, `ABOUT_ZEBRANKY0`, `ABOUT_ZEBRANKY1`, `ABOUT_ZEBRANKY7`, `ABOUT_STINGER1`, `name_1`, `name_2`, `name_3`, `name_4`, `OUT_TAKES0`, `OUT_TAKES1`, `OUT_TAKES2`, `OUT_TAKES3`, `OUT_TAKES5`, `OUT_TAKES6`, `OUT_TAKES7`, `OUT_TAKES8`, `OUT_TAKES9`, `OUT_TAKES10`, `OUT_TAKES11`, `OUT_TAKES12`, `OUT_TAKES13`
