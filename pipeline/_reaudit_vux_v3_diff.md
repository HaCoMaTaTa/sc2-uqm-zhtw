# VUX Rebuild-Compare Diff Report v3

**日期**：2026-08-16
**方法**：v0.7 dossier-based clean-room rebuild 完成後，程式化 diff shipped v0.5.1
**Workflow**：[Rebuild_And_Compare.md](../StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md)
**v3 file**：`translations/vux.zh-TW.v3.json`（102 tokens）
**shipped**：`translations/vux.zh-TW.json`（重度污染：吾 128 / 爾 137 / 之 174 / 吾等 84 / 爾等 136 / 本官 37 —— P0 最重）

## 統計

| 類別 | Emoji | 意義 | Count | % |
|---|---|---|---:|---:|
| 完全相同 | 🟢 | v3 vs shipped | 1 | 1.0% |
| 微調（等價） | 🟡 | v3 vs shipped | 7 | 6.9% |
| 措辭改變 | 🟠 | v3 vs shipped | 91 | 89.2% |
| 語意/voice 差異大 | 🔴 | v3 vs shipped | 3 | 2.9% |
| canonical 升級 | ✨ | v3 vs shipped | 0 | 0.0% |
| **總計** | | | **102** | 100.0% |

## Q&A 決策鎖（v3 依此執行）

- Q1=A 感嘆詞 dossier v0.7 (Hee!→嘿嘿嘿！/(urp!)→（噁——！）/(urk!)→（噎——！）/Mmmmmm!→嗯～～～～/AUGH!→噁！/(sob!)→（嗚——！）/AIEEE!→啊咦咦咦咦──！！！首介)
- Q2=A VUX 主族自稱: 我族 VUX(主) + 我方(少) + 我(單人)
- Q3=A ZEX 自稱: 本官(~85%) + 本上將澤克斯(首介 ZEX_HELLO_1) + 我(親密調情 GOODBYE_ZEX)
- Q4=A 主族稱玩家: 你/你們 + 情境辱罵詞（腐肉袋/蠕蟲/會嘔吐的東西/醜八怪）
- Q5=A ZEX 稱玩家: 艦長(預設) + 光滑迷人的朋友/美麗豐潤的人類/心愛的人類(詩意)
- Q6=A silatious/phlagrant melons: 嬉哩語/明目張膽的西瓜/第三次可就真的痛了
- Q7=A menagerie=珍禽異獸收藏館 / my children=我的孩子們 / new child=我的新孩子（覆蓋 Master_Glossary L232 舊 canonical）
- Q8=A ZEX chiton rasps: 本官的甲殼因興奮而摩挲、滲潤
- Q9=A+B CAPS 用短句+句號+\n（不加 **）; AIEEEEE! 首介中譯
- Q10=A player apology 台灣口語+情境切換
- Q11=A smooth-skinned friend=光滑迷人的朋友
- Q12=A 4 批 partial (25/16/22/39)

## 3-gate verify 結果

- ✅ **Gate 1 純度**：race=0, simp=0, variant=0（**shipped 之 174/爾 137/吾 128 等 P0 污染全部清除**）
- ✅ **Gate 2 行數**：0 mismatch（102/102 tokens 對齊 EN 原文）
- ✅ **Gate 3 Lua template**：0 English leak first-arg（getStarName/getConstellation/getColor/swapIfSeeded 皆已 zh-TW 化）

## 主要 canonical 修正 vs shipped v0.5.1

| 舊（shipped v0.5.1） | 新（v3 依 v0.7 dossier + Master_Glossary） | 影響 |
|---|---|---|
| 本將軍 (37×) | **本官** (ZEX only) / **本上將澤克斯** (首介 ZEX_HELLO_1) | ZEX 語體轉現代貴族氣（Master_Glossary L152 canonical） |
| 吾/爾/之/爾等/吾等（600+ 次） | **我族 VUX / 我 / 你 / 你們** (主族) / **本官** (ZEX 專用) | 全數清除文言污染，符合 dossier v0.7 |
| 嘻！嘻！嘻！ | **嘿嘿嘿！（Hee! Hee! Hee!）** | 感嘆詞 dossier v0.7 canonical |
| 呃啊！/嗝！ | **（噁——！）（urp!）** | 感嘆詞 dossier v0.7 canonical |
| 呃咳！ | **（噎——！）（urk!）** | 感嘆詞 dossier v0.7 canonical |
| 唔唔唔唔唔──！ | **嗯～～～～（Mmmmmm!）** | 感嘆詞 dossier v0.7 canonical |
| 噁啊！ | **噁！（Augh!）** / **噁——！（AGGH!）** | 感嘆詞 dossier v0.7 canonical |
| 珍藏館 (Master_Glossary L232) | **珍禽異獸收藏館** (dossier v0.7 §4.6.4) | **⚠️ Master_Glossary 待更新** |
| 光滑肌膚之友 | **光滑迷人的朋友** | dossier v0.7 §4.6.3 |

## ⚠️ Master_Glossary 待補登 canonical 提醒

| 位置 | 舊 | 建議新增 | 出處 |
|---|---|---|---|
| L232 menagerie | 珍藏館/醜陋珍藏/怪物館 | 增補 **珍禽異獸收藏館** (dossier v0.7 primary) | Q7=A + VUX.md §4.6.4 |
| ZEX 自稱 | 未登記 | **本官** (單人) / **本上將澤克斯** (首介) / **我** (親密調情) | Q3=A + VUX.md §4.6.2 |
| 感嘆詞 icon | shipped v0.5.1 Q8 | 更新 hee=嘿嘿嘿 / urp=噁—— / urk=噎—— / Mmmmmm=嗯～～～～ / AUGH=噁 | Q1=A + VUX.md §4.4/4.6.4 |

## 差異項（只列 🟡🟠🔴，🟢 不列）

### #1 · `ZEX_HELLO_1` · 🟠 rewording · sim=0.613; 文言助詞清除=30

**英文原文**：
```
Ah! Human visitors! What a treat!
I am Admiral ZEX. Please do not be frightened. Unlike the rest of my species, I... enjoy humans.
You may know me by my reputation, my leadership of VUX forces during the war with your Alliance.
I assure you that this behavior, a sad necessity of those times, belies a much kinder, gentler being.
Please be welcome! We can get to know one another... expand our interspecies relationship.
But wait. How silly of me. You aren't here for polite repartee.
You have come for my Shofixti Maidens.
```

**Shipped v0.5.1**：
```
啊！ 人類訪客！ 何等難得的享受！
本將軍乃澤克斯上將（Admiral ZEX）。 請莫驚慌。 有別於吾之族類，本將軍…… 是喜好人類的。
爾等或許聽聞過本將軍之聲名，即戰時率領 VUX 大軍對抗爾等聯盟之人。
本將軍向爾等保證，那些行為乃時勢所迫之悲哀必要，掩蓋了一個更加溫柔和藹之存在。
歡迎光臨！ 吾等可以彼此認識……擴展吾等異族間之情誼。
不過等等。 本將軍真是失禮。 爾等並非為了禮尚往來之交談而來。
爾等是為了本將軍的修烈士族少女而來。
```

**Rebuild v3 (clean-room v0.7)**：
```
啊——人類訪客！ 真是難得的驚喜！
本官是澤克斯上將（Admiral ZEX）。 請不要害怕。 與族內其他成員不同—— 本官…… 很享受人類。
各位或許聽過本官的名號—— 戰時率領 VUX 大軍對抗你們聯盟的那位。
本官向你們保證，那些行為只是那個時代的悲哀必然，掩蓋了一個更加溫柔和藹的存在。
請進、請進！ 我們可以彼此認識…… 拓展我們兩個物種間的情誼。
不過等等。 本官真是失禮。 各位並非為了禮貌的閒聊而來。
各位是為了本官的修烈士族少女而來。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×5 / 之×7 / 乃×2 / 吾等×2 / 爾等×5 / 將軍×6

**你的選擇**：`ZEX_HELLO_1=A`（shipped）/ `ZEX_HELLO_1=B`（v3）/ `ZEX_HELLO_1=C自訂:...`

---

### #2 · `ZEX_HELLO_2` · 🟠 rewording · sim=0.776; 文言助詞清除=12

**英文原文**：
```
Why I am so blessed! My favorite friends, the humans, are back.
Captain, it is good to see you again.
You Humans are so interesting, so... beautiful.
You know, I have many pictures of your species!
I keep them on my walls to... inspire me.
```

**Shipped v0.5.1**：
```
本將軍何其有幸！ 吾最愛之友人，人類，回來了。
艦長，能再見到您真好。
爾等人類是如此有趣，如此……美麗。
您知道嗎，本將軍收藏了眾多爾等物種之圖像！
本將軍將它們掛於牆上以……啟發吾之靈感。
```

**Rebuild v3 (clean-room v0.7)**：
```
本官何其有幸！ 本官最愛的朋友、人類，回來了。
艦長，能再見到您，真好。
你們人類是如此有趣，如此…… 美麗。
您知道嗎，本官收藏了許多你們物種的圖像！
本官將它們掛在牆上，用來…… 啟發本官的靈感。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 之×3 / 爾等×2 / 將軍×3

**你的選擇**：`ZEX_HELLO_2=A`（shipped）/ `ZEX_HELLO_2=B`（v3）/ `ZEX_HELLO_2=C自訂:...`

---

### #3 · `ZEX_HELLO_3` · 🟠 rewording · sim=0.689; 文言助詞清除=7

**英文原文**：
```
Captain! You are back so soon!
We had better be discreet (hee! hee!), or my countrymen will begin whispering about us.
```

**Shipped v0.5.1**：
```
艦長！ 您這麼快就回來了！
吾等最好謹慎低調（嘻！嘻！（Hee! Hee!）），否則本將軍之同胞將開始議論吾等之情事。
```

**Rebuild v3 (clean-room v0.7)**：
```
艦長！ 您這麼快就回來了！
我們最好低調一點（嘿嘿！（hee! hee!））—— 否則本官的同胞就要開始議論我們的事了。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 之×2 / 吾等×2 / 將軍×1

**你的選擇**：`ZEX_HELLO_3=A`（shipped）/ `ZEX_HELLO_3=B`（v3）/ `ZEX_HELLO_3=C自訂:...`

---

### #4 · `ZEX_HELLO_4` · 🟠 rewording · sim=0.792; 文言助詞清除=1

**英文原文**：
```
Luscious, robust human... I have eagerly awaited your return.
```

**Shipped v0.5.1**：
```
豐美的、健壯的人類…… 本將軍熱切地等候您的歸來。
```

**Rebuild v3 (clean-room v0.7)**：
```
豐潤的、結實的人類…… 本官熱切等候您的歸來。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 將軍×1

**你的選擇**：`ZEX_HELLO_4=A`（shipped）/ `ZEX_HELLO_4=B`（v3）/ `ZEX_HELLO_4=C自訂:...`

---

### #5 · `FIGHT_OR_TRADE_1` · 🟠 rewording · sim=0.683; 文言助詞清除=0

**英文原文**：
```
Captain! You escaped after all! How remarkable!
```

**Shipped v0.5.1**：
```
艦長！ 您終究還是逃出來了！ 何等出眾！
```

**Rebuild v3 (clean-room v0.7)**：
```
艦長！ 您到底還是逃出來了！ 真是了不起！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`FIGHT_OR_TRADE_1=A`（shipped）/ `FIGHT_OR_TRADE_1=B`（v3）/ `FIGHT_OR_TRADE_1=C自訂:...`

---

### #6 · `FIGHT_OR_TRADE_2` · 🟠 rewording · sim=0.541; 文言助詞清除=5

**英文原文**：
```
Human... we should be friends, not enemies!
The scope of our relationship can grow as close as you wish.
```

**Shipped v0.5.1**：
```
人類…… 吾等該是朋友，而非仇敵！
吾等關係之範圍可依您所願親密無間。
```

**Rebuild v3 (clean-room v0.7)**：
```
人類…… 我們應該是朋友，而非敵人！
我們的關係，可以親近到您希望的任何程度。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 之×1 / 吾等×2

**你的選擇**：`FIGHT_OR_TRADE_2=A`（shipped）/ `FIGHT_OR_TRADE_2=B`（v3）/ `FIGHT_OR_TRADE_2=C自訂:...`

---

### #7 · `what_you_do_here` · 🟠 rewording · sim=0.571; 文言助詞清除=0

**英文原文**：
```
What are you doing here, Admiral ZEX?
```

**Shipped v0.5.1**：
```
你在這裡做什麼，澤克斯上將？
```

**Rebuild v3 (clean-room v0.7)**：
```
澤克斯上將，你在這裡做什麼？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`what_you_do_here=A`（shipped）/ `what_you_do_here=B`（v3）/ `what_you_do_here=C自訂:...`

---

### #8 · `MY_MENAGERIE` · 🟠 rewording · sim=0.536; 文言助詞清除=14

**英文原文**：
```
Ah, such a good question! But you always were a bright species.
I will explain.
After the Great War, in which I played some small part
the VUX high council, in recognition for my services
granted me this planet, so that I might pursue my... hobby
without disturbing the general VUX populace.
I am a collector, you see.
I have the finest menagerie of... beautiful... creatures in all space.
```

**Shipped v0.5.1**：
```
啊，好問題！ 不過爾等物種向來聰穎。
本將軍將解釋一切。
於那場大戰之後，即本將軍略盡綿薄之戰役
VUX 高階議會，為表彰吾之功績
賜予本將軍此星球，使吾得以追求吾之……嗜好
而不擾亂一般 VUX 大眾。
您瞧，本將軍是個收藏家。
本將軍擁有全宇宙最極品的……美麗……生物珍藏館。
```

**Rebuild v3 (clean-room v0.7)**：
```
啊，真是個好問題！ 您果然是個聰明的物種。
本官這就解釋。
在那場大戰結束後—— 本官也出過一份力——
VUX 最高議會為表彰本官的功勳，
賜給本官這顆行星，讓本官能夠追求本官的…… 嗜好，
而不會打擾到一般 VUX 民眾。
您看，本官其實是個收藏家。
本官擁有全宇宙最精美的珍禽異獸收藏館…… 收藏的都是最…… 美麗的…… 生物。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×1 / 之×4 / 爾等×1 / 將軍×5

**你的選擇**：`MY_MENAGERIE=A`（shipped）/ `MY_MENAGERIE=B`（v3）/ `MY_MENAGERIE=C自訂:...`

---

### #9 · `what_about_menagerie` · 🟠 rewording · sim=0.558; 文言助詞清除=0

**英文原文**：
```
A menagerie? Is this a collection of animals, like a zoo?
```

**Shipped v0.5.1**：
```
珍藏館？ 這是類似動物園那種動物收藏嗎？
```

**Rebuild v3 (clean-room v0.7)**：
```
珍禽異獸收藏館？ 是動物收藏，像動物園那樣嗎？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`what_about_menagerie=A`（shipped）/ `what_about_menagerie=B`（v3）/ `what_about_menagerie=C自訂:...`

---

### #10 · `NEED_NEW_CREATURE` · 🟠 rewording · sim=0.655; 文言助詞清除=17

**英文原文**：
```
Animals? Hee! Hee! Hee! Oh, no, Captain! Not mere animals!
My menagerie contains only the most... beautiful... creatures in the galaxy!
Each of my children, as I like to call them, has a wonderful set of traits
which make them unique and special... especially to me!
I have a complete variety of beasts from as far away as <% comm.getConstellation("Procyon", "chmmr") %> and <% comm.getConstellation("Vega", "destroyed starbase") %>.
No, this is not just some `zoo'!
I have worked diligently for many years to craft my menagerie, to gradually improve it.
Perhaps you can't tell, but I am rather proud of it!
Alas, there is one creature, one GORGEOUS animal which I do not yet possess.
I would give almost ANYTHING for that creature, Captain.
```

**Shipped v0.5.1**：
```
動物？ 嘻！嘻！嘻！（Hee! Hee! Hee!） 噢不，艦長！ 絕非尋常動物！
本將軍之珍藏館僅收藏全銀河系最……美麗……之生物！
吾之每一個孩子，本將軍樂於這麼稱呼牠們，都擁有獨一無二之特質
使牠們特別而珍貴……尤其是對本將軍而言！
本將軍擁有遠自 <% comm.getConstellation("南河三", "chmmr") %>（Procyon） 與 <% comm.getConstellation("織女星", "destroyed starbase") %>（Vega） 之各色野獸。
不，這絕非什麼「動物園」！
本將軍多年來勤勤懇懇打造這座珍藏館，逐步完善它。
或許爾等看不出來，但本將軍對此頗感自豪！
可惜，有一頭生物，一頭華美之獸，本將軍至今尚未擁有。
本將軍願付出幾乎任何代價換取那頭生物，艦長。
```

**Rebuild v3 (clean-room v0.7)**：
```
動物？ 嘿嘿嘿！（Hee! Hee! Hee!） 喔，不，艦長！ 不是普通的動物！
本官的珍禽異獸收藏館裡，只收藏銀河系中最…… 美麗的…… 生物！
本官喜歡稱牠們為「我的孩子們」—— 每一個都有一組獨特的特質，
讓牠們獨一無二…… 尤其對本官而言更是如此！
本官擁有各式各樣的珍獸—— 從遠至 <% comm.getConstellation("南河三", "chmmr") %>（Procyon） 到 <% comm.getConstellation("織女星", "destroyed starbase") %>（Vega） 都有。
不，這絕不只是什麼「動物園」！
本官多年來勤勉不懈，打造這座收藏館，逐步精進它。
或許您看不出來—— 但本官對此頗為自豪！
唉，只可惜還有一種生物、一頭美到令人屏息的動物，本官至今仍未擁有。
為了那頭生物，艦長，本官幾乎願意付出任何代價。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×1 / 之×6 / 爾等×1 / 將軍×8

**你的選擇**：`NEED_NEW_CREATURE=A`（shipped）/ `NEED_NEW_CREATURE=B`（v3）/ `NEED_NEW_CREATURE=C自訂:...`

---

### #11 · `what_about_creature` · 🟠 rewording · sim=0.780; 文言助詞清除=0

**英文原文**：
```
If we went and got this little critter for you, would you give us the Shofixti Maidens?
```

**Shipped v0.5.1**：
```
如果我們去幫你抓那頭小怪物，你願意把修烈士族少女交出來嗎？
```

**Rebuild v3 (clean-room v0.7)**：
```
如果我們去幫你抓回那隻小生物，你會把修烈士族少女交給我們嗎？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`what_about_creature=A`（shipped）/ `what_about_creature=B`（v3）/ `what_about_creature=C自訂:...`

---

### #12 · `ABOUT_CREATURE` · 🟠 rewording · sim=0.676; 文言助詞清除=26

**英文原文**：
```
Hmmm... what an interesting proposal!
I never would have thought of such a wonderful idea myself.
You are a genius, Captain!
In answer to your question, yes! I accept your offer.
Deliver the creature to me, and I shall give you the Shofixti Maidens.
I will even provide you with a clue to finding the creature's native planet!
My source for this information is an ancient wildlife handbook
written millennia ago by some unknown alien author. The pertinent passage goes as follows
`... demise, It(!) basks in <% comm.getColor("yellow", "vux beast") %> light within the constellation Linch-Nas-Ploh.'
We have translated `Linch-Nas-Ploh' <% comm.swapIfSeeded("to mean approximately", "to mean") %>
`<% comm.getConstellation("the long, thin creature who has swallowed the huge beast", "vux beast") %>.'
I am afraid this is all that I know.
I hope it is sufficient.
```

**Shipped v0.5.1**：
```
嗯……多麼有趣的提議！
本將軍自己絕想不出如此妙計。
您真是天才，艦長！
以回覆爾等之問，是的！ 本將軍接受爾等之提議。
將那頭生物送至本將軍手中，吾將把修烈士族少女交予爾等。
本將軍甚至願意提供爾等一條線索，指引尋獲該生物母星之路！
吾之情報來源乃一本古老之野生生物手冊
數千年前由某位無名異族作者所著。 相關段落如下
『……之終焉，牠(!) 沐浴於 <% comm.getColor("黃色", "vux beast") %> 光芒之中，位於 蟒-噬-獸（Linch-Nas-Ploh） 星群。』
吾等已將『蟒-噬-獸（Linch-Nas-Ploh）』<% comm.swapIfSeeded("大致翻譯為", "翻譯為") %>
『<% comm.getConstellation("吞下巨獸的細長生物", "vux beast") %>（the long, thin creature who has swallowed the huge beast）』。
本將軍所知僅此。
希望這已足夠。
```

**Rebuild v3 (clean-room v0.7)**：
```
嗯嗯…… 真是個有趣的提議！
本官自己絕對想不到這麼美妙的點子。
您真是天才，艦長！
回答您的問題—— 沒錯！ 本官接受您的提議。
把那頭生物交給本官，本官就把修烈士族少女交給您。
本官甚至可以提供一條線索，幫您找到那生物的母星！
本官這條資訊的出處，是一本古老的野生生物圖鑑，
數千年前由某位不知名的外星作者所寫。 相關段落如下——
「……的消亡。 牠（!）沐浴在 <% comm.getColor("黃色", "vux beast") %> 光芒中，就在 蟒-噬-獸（Linch-Nas-Ploh） 星群裡。」
本官的部屬已將「Linch-Nas-Ploh」<% comm.swapIfSeeded("大致翻譯為", "翻譯為") %>
「<% comm.getConstellation("吞下巨獸的細長生物", "vux beast") %>」。
恐怕本官所知就這麼多了。
希望這足以幫上忙。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×4 / 之×7 / 乃×1 / 焉×1 / 吾等×1 / 爾等×4 / 將軍×5

**你的選擇**：`ABOUT_CREATURE=A`（shipped）/ `ABOUT_CREATURE=B`（v3）/ `ABOUT_CREATURE=C自訂:...`

---

### #13 · `about_creature_again` · 🟠 rewording · sim=0.640; 文言助詞清除=0

**英文原文**：
```
Would you tell me again where I can find that creature you want so badly?
```

**Shipped v0.5.1**：
```
可以再告訴我一次那頭你想要的生物在哪裡嗎？
```

**Rebuild v3 (clean-room v0.7)**：
```
可以再告訴我一次，我到哪裡才能找到你這麼想要的那頭生物嗎？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`about_creature_again=A`（shipped）/ `about_creature_again=B`（v3）/ `about_creature_again=C自訂:...`

---

### #14 · `CREATURE_AGAIN` · 🟠 rewording · sim=0.732; 文言助詞清除=11

**英文原文**：
```
Certainly, my smooth-skinned friend!
My source for this information is an ancient wildlife handbook
written millennia ago by some unknown alien author. The pertinent passage goes as follows
`... demise, It(!) basks in <% comm.getColor("yellow", "vux beast") %> light within the constellation Linch-Nas-Ploh.'
We have translated `Linch-Nas-Ploh' <% comm.swapIfSeeded("to mean approximately", "to mean") %>
`<% comm.getConstellation("the long, thin creature who has swallowed the huge beast", "vux beast") %>.'
I am afraid this is all that I know.
I hope it is sufficient.
```

**Shipped v0.5.1**：
```
當然，本將軍那位光滑肌膚的友人！
吾之情報來源乃一本古老之野生生物手冊
數千年前由某位無名異族作者所著。 相關段落如下
『……之終焉，牠(!) 沐浴於 <% comm.getColor("黃色", "vux beast") %> 光芒之中，位於 蟒-噬-獸 星群。』
吾等已將『蟒-噬-獸』<% comm.swapIfSeeded("大致翻譯為", "翻譯為") %>
『<% comm.getConstellation("吞下巨獸的細長生物", "vux beast") %>』。
本將軍所知僅此。
希望這已足夠。
```

**Rebuild v3 (clean-room v0.7)**：
```
當然可以，本官那位光滑迷人的朋友！
本官這條資訊的出處，是一本古老的野生生物圖鑑，
數千年前由某位不知名的外星作者所寫。 相關段落如下——
「……的消亡。 牠（!）沐浴在 <% comm.getColor("黃色", "vux beast") %> 光芒中，就在 蟒-噬-獸 星群裡。」
本官的部屬已將「Linch-Nas-Ploh」<% comm.swapIfSeeded("大致翻譯為", "翻譯為") %>
「<% comm.getConstellation("吞下巨獸的細長生物", "vux beast") %>」。
恐怕本官所知就這麼多了。
希望這足以幫上忙。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 之×4 / 乃×1 / 焉×1 / 吾等×1 / 將軍×2

**你的選擇**：`CREATURE_AGAIN=A`（shipped）/ `CREATURE_AGAIN=B`（v3）/ `CREATURE_AGAIN=C自訂:...`

---

### #15 · `i_have_beast` · 🟡 micro-adjust (equivalent) · sim=0.886; 文言助詞清除=0

**英文原文**：
```
Admiral ZEX, we have captured the hideous monster from <% comm.getStarName("Delta Lyncis", "vux beast") %>. Let us make an exchange.
```

**Shipped v0.5.1**：
```
澤克斯上將，我方已在 <% comm.getStarName("天貓座δ", "vux beast") %>（Delta Lyncis） 捕獲那頭醜陋怪獸。 咱們來做交易吧。
```

**Rebuild v3 (clean-room v0.7)**：
```
澤克斯上將，我們已經從 <% comm.getStarName("天貓座δ", "vux beast") %>（Delta Lyncis） 抓到那隻醜陋的怪物了。 我們來交換吧。
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`i_have_beast=A`（shipped）/ `i_have_beast=B`（v3）/ `i_have_beast=C自訂:...`

---

### #16 · `GIVE_BEAST` · 🟠 rewording · sim=0.522; 文言助詞清除=12

**英文原文**：
```
Ah, a most excellent piece of news! My chiton rasps and moistens with excitement!
I have been looking forward to this for so long! Hee! Hee! Hee!
My subordinates stand ready to receive the beast from your ship, Captain.
Effect its transfer and then... we shall give you the Maidens you desire.
```

**Shipped v0.5.1**：
```
啊，何等絕妙之消息！ 本將軍之甲殼因興奮而摩挲、滲潤！
本將軍已期盼此刻多時！ 嘻！嘻！嘻！
吾之部屬已備妥從您艦上接收此獸，艦長。
完成移交後……吾將把爾等渴望之少女交予爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
啊，真是絕妙的好消息！ 本官的甲殼因興奮而摩挲、滲潤！
本官期待這一刻已經好久了！ 嘿嘿嘿！（Hee! Hee! Hee!）
本官的部屬已就位，準備從您的艦上接收那頭生物，艦長。
完成傳送，然後…… 本官就把您想要的少女交給您。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 之×4 / 爾等×2 / 將軍×2

**你的選擇**：`GIVE_BEAST=A`（shipped）/ `GIVE_BEAST=B`（v3）/ `GIVE_BEAST=C自訂:...`

---

### #17 · `ok_take_beast` · 🟠 rewording · sim=0.808; 文言助詞清除=0

**英文原文**：
```
Okay, the beast is ALL yours! But be careful, it's a killer!
```

**Shipped v0.5.1**：
```
好，那頭獸全歸你！ 不過小心點，牠可是頭殺手！
```

**Rebuild v3 (clean-room v0.7)**：
```
好啦，那頭生物「全部」歸你了！ 不過小心點，牠可是個殺手！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`ok_take_beast=A`（shipped）/ `ok_take_beast=B`（v3）/ `ok_take_beast=C自訂:...`

---

### #18 · `FOOL_AIEE0` · 🟠 rewording · sim=0.474; 文言助詞清除=37

**英文原文**：
```
Ah! My new child is on board. Such a big one, isn't he!?...
...and so frisky!
I am delighted beyond words that you have given me the beast, Captain
but I am afraid that there has been a slight change in our plans. Regrettable, but necessary.
Oh, my beautiful, luscious human, I had thought that the hideous, violent monster you have given me
would complete my collection of Ugliness, my Menagerie of Monsters... I was wrong!
YOU, my human love, are the most vile, the most fierce and wretched!
My collection could never be complete without you. I need you, Captain.
But alas, I fear you will not give your consent willingly. Am I right?
Therefore, sub-commander DAX, terminate communications... warm up my modified Intruder.
Engage the Precursor warp nullifier. Hee! Hee! Hee!... prepare for battle!
```

**Shipped v0.5.1**：
```
啊！ 吾之新孩子已在艦上。 好大一個，不是嗎！？……
……而且如此活潑！
本將軍高興得無以言表爾等將此獸送與吾，艦長
但恐怕吾等之計畫略有變動。 令人遺憾，但實屬必要。
噢，本將軍那豐美之人類，吾原以為爾等送來的這頭醜陋、暴烈之怪物
將會完善吾之醜陋珍藏，吾之怪物館……本將軍錯了！
爾等，本將軍摯愛之人類，方才是最卑劣、最狂猛、最悲慘之存在！
沒有爾等，吾之珍藏永難完備。 本將軍需要爾等，艦長。
但，唉，本將軍恐怕爾等不會自願應允。 對吧？
故此，副指揮官達克斯（Sub-commander DAX），中斷通訊……啟動吾之改造入侵者。
啟用先驅者曲速抑制場。 嘻！嘻！嘻！……備戰！
```

**Rebuild v3 (clean-room v0.7)**：
```
啊！ 本官的新孩子上船了。 好大一頭，是不是！？……
……而且好活潑！
本官對您把這頭生物送給本官一事，喜悅得無以言表，艦長——
但恐怕，我們的計畫略有變動。 令人遺憾，卻不得不為。
喔，本官那美麗、豐潤的人類，本官原以為您所送來的那頭醜陋兇暴的怪物
將會使本官的醜陋收藏、本官的怪物珍藏館圓滿…… 本官錯了！
是「您」，本官心愛的人類，才是最卑劣、最兇猛、最悲慘的！
沒有您，本官的收藏永遠無法圓滿。 本官需要您，艦長。
只可惜，本官擔心您不會心甘情願地同意。 本官說得對嗎？
所以—— 達克斯副指揮官，切斷通訊…… 讓本官改造過的入侵者暖機。
啟動先驅者曲速抑制器。 嘿嘿嘿！（Hee! Hee! Hee!）…… 準備開戰！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×8 / 爾×6 / 之×10 / 吾等×1 / 爾等×6 / 將軍×6

**你的選擇**：`FOOL_AIEE0=A`（shipped）/ `FOOL_AIEE0=B`（v3）/ `FOOL_AIEE0=C自訂:...`

---

### #19 · `FOOL_AIEE1` · 🟠 rewording · sim=0.618; 文言助詞清除=8

**英文原文**：
```
Sub-commander? Why has my main console become inoperative?
The transmit mode is locked!
What do you mean the central system computer is damaged? How!?...
...the Beast!?... Escaped!!
No, Sub-Commander, this is impossible. It couldn't escape from our strongest containment system
IT'S WHAT?!! Decks five and six?! Eleven Crewmen!!
Sound the alarms, you fool! Where is it now?! Engineering, report!... Engineering?!
Sub-Commander, seal Bulkhe-- Sub-Commander... are you listening to me? What are you staring at?
PAY ATTENTION, Sub-Commander! Give me a report on its posit-- WHAT ARE YOU STARING AT!...
behind me?
WH- Wh- what- wh- AIEEEEE!!!!!...
```

**Shipped v0.5.1**：
```
副指揮官？ 為何吾之主控台失去反應？
發送模式被鎖定！
你說中央系統電腦受損是什麼意思？ 怎會如此！？……
……那頭獸！？……脫逃了！！
不，副指揮官，這不可能。 牠不可能從吾等最強之收容系統脫逃
牠什麼？！！ 五、六甲板？！ 十一名船員！！
拉警報，你這蠢材！ 現在牠在哪裡？！ 工程部門，回報！……工程部門？！
副指揮官，封鎖艙壁—— 副指揮官……你聽見本將軍說話嗎？ 你在盯著什麼看？
專心點，副指揮官！ 向本將軍回報牠的位—— 你到底在盯著什麼看！……
在本將軍身後？
呃- 呃- 呃- 呃- 啊咦咦咦咦──！！！！！（AIEEEEE!!!!!）……
```

**Rebuild v3 (clean-room v0.7)**：
```
副指揮官？ 為何本官的主控台失效了？
發射模式被鎖住了！
您說中央系統電腦損毀是什麼意思？ 怎麼會！？……
……那頭生物！？…… 逃了！！
不，副指揮官，這不可能。 牠不可能逃出本官最堅固的收容系統
牠什麼？！！ 五號、六號甲板？！ 十一名船員！！
拉警報，你這蠢貨！ 牠現在在哪！？ 動力室，回報！…… 動力室？！
副指揮官，密封艙門—— 副指揮官…… 您在聽本官說話嗎？ 您在盯什麼看？
注意聽，副指揮官！ 給本官報告牠的位置—— 您到底在盯什麼看！……
在本官後面嗎？
什—什—什麼—— 啊咦咦咦咦──！！！（AIEEEEE!!!）……
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 之×2 / 吾等×1 / 將軍×3

**你的選擇**：`FOOL_AIEE1=A`（shipped）/ `FOOL_AIEE1=B`（v3）/ `FOOL_AIEE1=C自訂:...`

---

### #20 · `why_trust_1` · 🟡 micro-adjust (equivalent) · sim=0.962; 文言助詞清除=0

**英文原文**：
```
Ah, Admiral ZEX, aren't you forgetting something? The Shofixti Maidens?
```

**Shipped v0.5.1**：
```
呃，澤克斯上將，你是不是忘了什麼？ 修烈士族少女呢？
```

**Rebuild v3 (clean-room v0.7)**：
```
啊，澤克斯上將，你是不是忘了什麼？ 修烈士族少女呢？
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`why_trust_1=A`（shipped）/ `why_trust_1=B`（v3）/ `why_trust_1=C自訂:...`

---

### #21 · `TRUST_1` · 🟠 rewording · sim=0.692; 文言助詞清除=2

**英文原文**：
```
Oh yes, no problem. Even now my subordinates are bringing them up from the surface.
So let's not waste time. Send that delightful beast over, immediately!
```

**Shipped v0.5.1**：
```
噢，那當然，沒問題。 吾之部屬此刻正將她們自地面帶上來。
所以咱們別浪費時間。 立刻將那頭可愛的獸送過來！
```

**Rebuild v3 (clean-room v0.7)**：
```
喔，是啊，沒問題。 此刻本官的部屬正把她們從地面帶上來。
所以別浪費時間了。 把那頭可愛的生物送過來，馬上！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 之×1

**你的選擇**：`TRUST_1=A`（shipped）/ `TRUST_1=B`（v3）/ `TRUST_1=C自訂:...`

---

### #22 · `why_trust_2` · 🟠 rewording · sim=0.562; 文言助詞清除=0

**英文原文**：
```
Look, we believe in 1 for 1 trades. We will transfer the beast when we see the Maidens.
```

**Shipped v0.5.1**：
```
聽好，我方講究一手交錢一手交貨。 看到少女我們才會移交那頭獸。
```

**Rebuild v3 (clean-room v0.7)**：
```
聽著，我們相信一手交錢一手交貨。 等我們看到少女，就把生物送過去。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`why_trust_2=A`（shipped）/ `why_trust_2=B`（v3）/ `why_trust_2=C自訂:...`

---

### #23 · `TRUST_2` · 🟠 rewording · sim=0.709; 文言助詞清除=5

**英文原文**：
```
Captain, Captain, we are both creatures of honor.
If I say that the Shofixti Maidens are on their way up from the surface, then they are.
You will have them shortly, accept my word... now please, Captain, the beast?
```

**Shipped v0.5.1**：
```
艦長，艦長，吾等皆為榮譽之生物。
若本將軍說修烈士族少女正從地面上來，那她們就是正在上來。
您很快就會拿到她們，請相信本將軍……現在請，艦長，那頭獸呢？
```

**Rebuild v3 (clean-room v0.7)**：
```
艦長、艦長，我們都是講究榮譽的生物。
本官既然說修烈士族少女正從地面上來，那就是正在上來。
您很快就能得到她們—— 請相信本官的話…… 那麼現在，艦長，那頭生物呢？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 之×1 / 吾等×1 / 將軍×2

**你的選擇**：`TRUST_2=A`（shipped）/ `TRUST_2=B`（v3）/ `TRUST_2=C自訂:...`

---

### #24 · `why_trust_3` · 🟠 rewording · sim=0.750; 文言助詞清除=0

**英文原文**：
```
Now see here ZEX! Humans and VUX have had a pretty stormy relationship. Why should we trust you?
```

**Shipped v0.5.1**：
```
澤克斯，聽好！ 人類和 VUX 的關係一直很糟。 我們憑什麼相信你？
```

**Rebuild v3 (clean-room v0.7)**：
```
給我聽好，澤克斯！ 人類和 VUX 的關係從來都不平順。 我們憑什麼相信你？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`why_trust_3=A`（shipped）/ `why_trust_3=B`（v3）/ `why_trust_3=C自訂:...`

---

### #25 · `TRUST_3` · 🟠 rewording · sim=0.625; 文言助詞清除=17

**英文原文**：
```
Really, Captain! My honor is impugned!
You have maligned me and I am deeply hurt.
I thought we had built some trust between us, different though we may be
but no, I perceive now the same bigotry and misunderstanding
which brought our two species to war!
This was our chance to cement a good relationship between Human and VUX.
With my influence, the High Council could easily have been swayed to view
the Human cause in a more favorable light.
```

**Shipped v0.5.1**：
```
真是的，艦長！ 吾之榮譽受到質疑！
您玷污了本將軍，吾深感受傷。
本將軍以為吾等之間已建立了些許信任，儘管吾等如此不同
但不，本將軍此刻察覺，正是同樣的偏見與誤解
將吾兩族推向戰爭！
這本可是締結人類與 VUX 良好關係之契機。
以本將軍之影響力，高階議會本可輕易被說服
以更善意之眼光看待人類之立場。
```

**Rebuild v3 (clean-room v0.7)**：
```
真是的，艦長！ 本官的榮譽受到玷污了！
您毀謗本官，本官深深受傷。
本官原以為彼此已經建立了一些信任—— 縱使我們有所不同——
但不，本官現在看得出來，同樣的偏見與誤解仍然存在，
正是這樣的偏見，把我們兩個物種帶進了戰爭！
這本是本官締結人類與 VUX 良好關係的機會。
藉本官的影響力，最高議會本可輕易被說服，
以更善意的眼光看待人類的訴求。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×5 / 之×6 / 吾等×2 / 將軍×4

**你的選擇**：`TRUST_3=A`（shipped）/ `TRUST_3=B`（v3）/ `TRUST_3=C自訂:...`

---

### #26 · `LIKE_YOU` · 🟠 rewording · sim=0.593; 文言助詞清除=7

**英文原文**：
```
Because I like Humans, Captain. I respect and admire your species.
I do not share the bigoted views of most of my people.
```

**Shipped v0.5.1**：
```
因為本將軍喜好人類，艦長。 吾尊敬並仰慕爾等物種。
吾不認同吾族大多數同胞之偏見。
```

**Rebuild v3 (clean-room v0.7)**：
```
因為本官喜歡人類，艦長。 本官敬重、也欣賞你們這個物種。
本官並不認同族內大多數同胞那種偏執的看法。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×1 / 之×1 / 爾等×1 / 將軍×1

**你的選擇**：`LIKE_YOU=A`（shipped）/ `LIKE_YOU=B`（v3）/ `LIKE_YOU=C自訂:...`

---

### #27 · `why_like_me` · 🟡 micro-adjust (equivalent) · sim=0.944; 文言助詞清除=0

**英文原文**：
```
Ah, Admiral ZEX? Why do you like us? We thought all VUX hated humans.
```

**Shipped v0.5.1**：
```
呃，澤克斯上將？ 你為什麼喜歡我們？ 我們以為所有 VUX 都恨人類。
```

**Rebuild v3 (clean-room v0.7)**：
```
啊，澤克斯上將？ 你為什麼喜歡我們？ 我們還以為所有 VUX 都恨人類呢。
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`why_like_me=A`（shipped）/ `why_like_me=B`（v3）/ `why_like_me=C自訂:...`

---

### #28 · `LIKE_BECAUSE` · 🟠 rewording · sim=0.492; 文言助詞清除=48

**英文原文**：
```
No, No, not all VUX, Captain! Most... but not all.
It is true when the majority of my people view one of your species
they are forced to regurgitate
but there are those among us who have grown beyond such childishness to take a more liberal view.
We, the few sophisticates, are not subject to the whims and fads of current fashion.
Our likes and dislikes are strictly based on personal preference.
We see the... beauty in you Humans. The value in a long-term... relationship.
You are different, yes. But personally, I like difference.
In fact, I ADORE it.
Your physique is so wonderfully varied! Your multitudinous rigid appendages, your tiny double eyes
your varied skin coloration, and the delightful patchwork of hair covering only parts of your bodies
leaving other parts bare and smooth! Mmmmmm!
I value your species, Captain. I see you as just `people'... like us VUX.
```

**Shipped v0.5.1**：
```
不、不，並非所有 VUX 皆然，艦長！ 大多數……但非全部。
確實，當本將軍之族類多數見到爾等物種
他們會被迫嘔吐
但吾等之中亦有些人已成長超越如此幼稚之見，採取更開明之立場。
吾等，少數之雅士，並不受當今時尚潮流之左右。
吾等之好惡完全基於個人偏好。
吾等看見爾等人類之……美。 見到長期……關係之價值。
爾等確實不同，是的。 但本將軍個人偏好差異。
事實上，吾對此極為著迷。
爾等之體格是如此奇妙多變！ 爾等多枝之堅硬肢體、爾等一對小小之雙眼
爾等各色之膚色，還有僅覆蓋身體某些部位之毛髮拼貼
其餘部位裸露光滑！ 唔唔唔唔唔──！（Mmmmmm!）
本將軍珍視爾等物種，艦長。 吾視爾等為單純之「人」……如同吾等 VUX。
```

**Rebuild v3 (clean-room v0.7)**：
```
不、不，不是全部的 VUX，艦長！ 大多數…… 但並非全部。
的確，本官族內大多數同胞每當看見你們這個物種，
都會忍不住嘔吐——
但我們當中，也有些人已超越那樣的幼稚，抱持更開放的觀點。
我們這些少數的高雅人士，並不隨當代流行的風潮起舞。
我們的喜惡，純粹奠基於個人偏好。
我們看得見…… 你們人類身上的美。 也看得見長久…… 關係的價值。
你們是與眾不同，沒錯。 而本官恰恰喜愛這種不同。
事實上，本官「熱愛」不同。
你們的體格是如此奇妙多變！ 你們那眾多堅硬的附肢、那雙小小的眼睛，
你們多彩多姿的膚色，還有那令人愉悅的、只覆蓋身體某些部位的毛髮拼貼——
讓其他部位裸露而光滑！ 嗯～～～～（Mmmmmm!）
本官珍視你們這個物種，艦長。 本官視你們為「人」…… 就像我們 VUX 一樣。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×7 / 爾×9 / 之×15 / 吾等×5 / 爾等×9 / 將軍×3

**你的選擇**：`LIKE_BECAUSE=A`（shipped）/ `LIKE_BECAUSE=B`（v3）/ `LIKE_BECAUSE=C自訂:...`

---

### #29 · `are_you_a_pervert` · 🟠 rewording · sim=0.605; 文言助詞清除=1

**英文原文**：
```
Whoa, Admiral ZEX! This is just a bit too weird. Are you some kind of perv-- er... aesthete?
```

**Shipped v0.5.1**：
```
喂，澤克斯上將！ 這感覺有點怪。 你該不會是那種變… 呃… 好惡趣之人吧？
```

**Rebuild v3 (clean-room v0.7)**：
```
喔喔，澤克斯上將！ 這有點太怪了吧。 你是某種變態—— 呃…… 唯美主義者嗎？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 之×1

**你的選擇**：`are_you_a_pervert=A`（shipped）/ `are_you_a_pervert=B`（v3）/ `are_you_a_pervert=C自訂:...`

---

### #30 · `CALL_ME_WHAT_YOU_WISH` · 🟠 rewording · sim=0.576; 文言助詞清除=27

**英文原文**：
```
You have talked with my VUX countrymen, haven't you?
They are closed-minded fools... bigoted in all ways.
Call me what you wish, Captain. I choose to view myself as, well
simply open-minded... free to experience the full range of life's possibilities.
The VUX rulers could not refuse my military genius, couldn't ignore the many victories I gave them.
But they would not tolerate my behavior, accept my desires as natural
so they sent me out here... a hero's exile! Where  I won't `poison' the minds of youth
with my `bizarre' ideas and `perverted' lifestyle. Hmmph... bigoted fools.
You see, Captain, we are not all that different, you and I.
We are different from the majority of VUX, and so we, in VUX eyes, are both monsters.
```

**Shipped v0.5.1**：
```
您跟本將軍之 VUX 同胞談過話了，對吧？
他們是心胸狹隘之愚人……全然偏頗。
您愛怎麼稱呼本將軍都行，艦長。 本將軍選擇看待自己為，這麼說吧
單純心胸開明……自由地體驗生命所有可能性。
VUX 統治者無法拒絕吾之軍事天才，無法忽視吾為他們贏來之無數勝利。
但他們無法容忍吾之行為，無法接受吾之慾望為自然
故此他們將吾放逐至此……英雄之流亡！ 使吾無法「毒害」年輕人之心智
以吾之「怪異」思想與「變態」生活方式。 哼……偏頗之愚人。
您瞧，艦長，吾等其實並非那麼不同，您與本將軍。
吾等皆與 VUX 大多數不同，故在 VUX 眼中，吾等皆為怪物。
```

**Rebuild v3 (clean-room v0.7)**：
```
您和本官那些 VUX 同胞談過話了，對吧？
他們就是一群封閉狹隘的蠢貨…… 每一方面都充滿偏見。
您想怎麼叫本官都行，艦長。 本官選擇這樣看待自己——
就是心胸開闊…… 自由地體驗生命所有的可能。
VUX 統治者無法否定本官的軍事天才，無法忽視本官為他們贏得的無數勝利。
但他們無法容忍本官的行為、無法接受本官的欲望是天性使然——
於是他們把本官流放到這裡…… 英雄的放逐！ 讓本官無法毒害年輕一代的心靈——
用本官那些「怪異」的想法和「變態」的生活方式。 哼…… 一群偏執的蠢貨。
您瞧，艦長，我們並沒有那麼不同，您和本官。
我們都與絕大多數 VUX 不同—— 所以在 VUX 眼中，我們都是怪物。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×10 / 之×10 / 吾等×3 / 將軍×4

**你的選擇**：`CALL_ME_WHAT_YOU_WISH=A`（shipped）/ `CALL_ME_WHAT_YOU_WISH=B`（v3）/ `CALL_ME_WHAT_YOU_WISH=C自訂:...`

---

### #31 · `take_by_force` · 🟠 rewording · sim=0.773; 文言助詞清除=0

**英文原文**：
```
We require the Shofixti Maidens. We are prepared to use force if necessary.
```

**Shipped v0.5.1**：
```
我方需要修烈士族少女。 必要時我方不惜動武。
```

**Rebuild v3 (clean-room v0.7)**：
```
我們要修烈士族少女。 必要時，我們準備動武。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`take_by_force=A`（shipped）/ `take_by_force=B`（v3）/ `take_by_force=C自訂:...`

---

### #32 · `PRECURSOR_DEVICE` · 🟠 rewording · sim=0.482; 文言助詞清除=44

**英文原文**：
```
Hee! Hee! Hee! Oh, Captain, that would be such an unfortunate mistake
a grave error on both our parts.
We have so much to learn from each other, so much to give each other.
It would be such a sad loss if we were to fall back to the mindless blasting and killing
that has marred our two species' relationship up to this point.
Admittedly, as THE acknowledged VUX military genius
I would find it interesting to face your ONE powerful, alien starship
with my huge personal fleet of Intruders, but oh! What a mistake it would be.
Also... I think it only fair to warn you, Captain
that in my campaigns I collected many interesting items.
Amongst these treasures is a Precursor artifact, a warp nullification field
that prevents nearby ships from making emergency HyperSpace maneuvers... from running away.
I note by the scars on the rear of your vessel that you have made many such escapes.
So you see, Captain, if you attack me, you will face the greatest military tactician in VUX history
commanding an almost infinite number of enemy combat ships
and the battle will be to the Death!
Surely we can find an alternative.
```

**Shipped v0.5.1**：
```
嘻！嘻！嘻！ 噢，艦長，那將是何等不幸之錯誤
一場吾等雙方之嚴重錯誤。
吾等有太多可互相學習之處，太多可互相給予之處。
若吾等倒退回無腦之爆擊與殺戮，將會是何等悲哀之損失
──那正是傷害吾兩族關係之元凶。
本將軍必須承認，作為 VUX 公認之首席軍事天才
面對爾等一艘強大異形星艦
以吾龐大之個人入侵者艦隊，本將軍確會覺得饒有興味，噢，但那將會是何等錯誤。
另外……本將軍認為應公平警告爾等，艦長
於吾之征戰中，本將軍收集了許多有趣之物品。
其中一件珍寶乃先驅者遺物，一具曲速抑制場
能阻止附近艦艇進行緊急超空間閃避……無法逃跑。
本將軍注意到爾等艦艇尾部之疤痕，顯示爾等曾多次逃遁。
所以爾等瞧，艦長，若爾等攻擊本將軍，將面對 VUX 史上最偉大之軍事戰術家
指揮幾近無限之敵艦
且戰鬥將是至死方休！
吾等定能找到替代方案。
```

**Rebuild v3 (clean-room v0.7)**：
```
嘿嘿嘿！（Hee! Hee! Hee!） 喔，艦長，那將會是多麼不幸的錯誤——
對我們雙方而言，都是一場重大失誤。
我們彼此有太多可以學習、太多可以給予。
若我們退回到那種盲目的轟炸與殺戮，實在會是一場悲哀的損失——
過去正是這一切，玷污了我們兩個物種的關係。
說實在，作為公認的 VUX 頂級軍事天才，
本官倒是覺得面對您那「一艘」強大的外星艦艇，
以本官龐大的入侵者私人艦隊迎戰，會挺有意思—— 不過喔！ 那真是個大錯特錯的決定。
還有…… 本官覺得該公平地警告您一聲，艦長，
本官在多次征戰中收集了許多有趣的物件。
在這些珍寶當中，有一件先驅者的遺物—— 一具曲速抑制場，
能夠阻止附近的艦艇進行緊急超空間跳躍…… 阻止您逃跑。
本官注意到您艦艇尾端的傷痕，看得出您逃過許多次。
所以您瞧，艦長，如果您攻擊本官，您將面對 VUX 歷史上最偉大的軍事戰略家，
指揮著近乎無限的敵方戰艦艦隊——
而這場戰鬥，將會是「殊死戰」！
相信我們一定能找到別的辦法。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×7 / 爾×6 / 之×14 / 乃×1 / 吾等×4 / 爾等×6 / 將軍×6

**你的選擇**：`PRECURSOR_DEVICE=A`（shipped）/ `PRECURSOR_DEVICE=B`（v3）/ `PRECURSOR_DEVICE=C自訂:...`

---

### #33 · `regardless` · 🟠 rewording · sim=0.650; 文言助詞清除=0

**英文原文**：
```
We will fight you regardless of your Precursor Artifact!
```

**Shipped v0.5.1**：
```
我方不管你的先驅者遺物是什麼，我們照打！
```

**Rebuild v3 (clean-room v0.7)**：
```
不管你有沒有先驅者遺物，我們都要跟你打！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`regardless=A`（shipped）/ `regardless=B`（v3）/ `regardless=C自訂:...`

---

### #34 · `THEN_FIGHT` · 🟠 rewording · sim=0.476; 文言助詞清除=0

**英文原文**：
```
Very well... to the Death!
```

**Shipped v0.5.1**：
```
那好……戰至死方休！
```

**Rebuild v3 (clean-room v0.7)**：
```
好吧…… 那就殊死戰！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`THEN_FIGHT=A`（shipped）/ `THEN_FIGHT=B`（v3）/ `THEN_FIGHT=C自訂:...`

---

### #35 · `you_lied` · 🟡 micro-adjust (equivalent) · sim=0.921; 文言助詞清除=0

**英文原文**：
```
You lied, Admiral ZEX!!! There was no `warp nullification field'! Cheater!
```

**Shipped v0.5.1**：
```
你在說謊，澤克斯上將！！！ 根本沒有什麼「曲速抑制場」！ 騙子！
```

**Rebuild v3 (clean-room v0.7)**：
```
你騙人，澤克斯上將！！！ 根本沒有什麼「曲速抑制場」！ 騙子！
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`you_lied=A`（shipped）/ `you_lied=B`（v3）/ `you_lied=C自訂:...`

---

### #36 · `YUP_LIED` · 🟠 rewording · sim=0.578; 文言助詞清除=12

**英文原文**：
```
Yes, I lied.
Surely, if a small falsehood can prevent hundreds of unnecessary deaths, this is acceptable.
Unfortunately, you saw through my falsehood and no doubt lives were lost.
Let us cease this mindless aggression, before it is our undoing.
```

**Shipped v0.5.1**：
```
是的，本將軍說了謊。
既然一個小謊言能避免數百條無謂性命之損失，這應是可以接受的。
可惜，爾等識破了吾之謊言，無疑有性命因此喪失。
讓吾等停止這無意義之攻擊，以免它成為吾等之毀滅。
```

**Rebuild v3 (clean-room v0.7)**：
```
是，本官撒了謊。
若一個小小的謊言能夠避免數百條不必要的性命喪失，這當然是可以接受的。
可惜您識破了本官的謊，無疑已有性命因此逝去。
在我們都毀滅以前，讓我們停止這場盲目的侵略吧。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×1 / 之×4 / 吾等×2 / 爾等×1 / 將軍×1

**你的選擇**：`YUP_LIED=A`（shipped）/ `YUP_LIED=B`（v3）/ `YUP_LIED=C自訂:...`

---

### #37 · `kill_you` · 🟠 rewording · sim=0.533; 文言助詞清除=0

**英文原文**：
```
We have no fear of any of your `devices'. Now we kill you!
```

**Shipped v0.5.1**：
```
我方對你的『裝置』毫無畏懼。 現在我們就殺了你！
```

**Rebuild v3 (clean-room v0.7)**：
```
我們才不怕你那些「裝置」。 現在就宰了你！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`kill_you=A`（shipped）/ `kill_you=B`（v3）/ `kill_you=C自訂:...`

---

### #38 · `FIGHT_AGAIN` · 🟠 rewording · sim=0.486; 文言助詞清除=11

**英文原文**：
```
Unfortunate. Dreary... and unfortunate.
Captain, even without such a device, you must understand the overwhelming forces I have at my command!
You cannot beat me here. It is impossible.
But... if a fight is what you demand, so be it.
```

**Shipped v0.5.1**：
```
無趣。 沉悶……且無趣。
艦長，即便沒有那件裝置，爾等亦必須明白吾麾下之壓倒性力量！
爾等於此地不可能擊敗本將軍。 這是不可能的。
但……若爾等執意一戰，那便如爾等所願。
```

**Rebuild v3 (clean-room v0.7)**：
```
不幸。 淒涼…… 又不幸。
艦長，就算沒有那樣的裝置，您也必須明白本官所指揮的兵力有多壓倒性！
您在這裡是打不贏本官的。 那是不可能的。
不過…… 若您堅持要打，那就悉聽尊便。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×4 / 之×1 / 爾等×4 / 將軍×1

**你的選擇**：`FIGHT_AGAIN=A`（shipped）/ `FIGHT_AGAIN=B`（v3）/ `FIGHT_AGAIN=C自訂:...`

---

### #39 · `bye_zex` · 🟡 micro-adjust (equivalent) · sim=0.947; 文言助詞清除=0

**英文原文**：
```
Goodbye, Admiral ZEX.
```

**Shipped v0.5.1**：
```
再見了，澤克斯上將。
```

**Rebuild v3 (clean-room v0.7)**：
```
再見，澤克斯上將。
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`bye_zex=A`（shipped）/ `bye_zex=B`（v3）/ `bye_zex=C自訂:...`

---

### #40 · `GOODBYE_ZEX` · 🟠 rewording · sim=0.600; 文言助詞清除=3

**英文原文**：
```
Goodbye, beautiful human. I hope we can meet someday as friends... perhaps even more.
```

**Shipped v0.5.1**：
```
再見了，美妙的人類。 願吾等他日能以朋友之姿相見……或許更甚。
```

**Rebuild v3 (clean-room v0.7)**：
```
再見，美麗的人類。 希望有朝一日我們能以朋友的身分再見…… 或許還能更進一步。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 之×1 / 吾等×1

**你的選擇**：`GOODBYE_ZEX=A`（shipped）/ `GOODBYE_ZEX=B`（v3）/ `GOODBYE_ZEX=C自訂:...`

---

### #41 · `HOMEWORLD_HELLO_1` · 🟠 rewording · sim=0.616; 文言助詞清除=15

**英文原文**：
```
Welcome to the end of your life, courtesy of VUX technology.
Our infinite supply of Intruder vessels are even now locking their vaporizers onto your position
and we shall end your painful, grotesque existence for you as soon as possible.
In the meantime, here is a little music...
```

**Shipped v0.5.1**：
```
歡迎爾等踏入生命之終點，此乃 VUX 科技之奉送。
吾等無窮無盡之入侵者艦隊此刻正將汽化炮鎖定爾等位置
吾等將盡快終結爾等痛苦而畸形之存在。
在此同時，聽點音樂吧……
```

**Rebuild v3 (clean-room v0.7)**：
```
歡迎來到你們生命的終點—— 由 VUX 科技榮譽提供。
我族 VUX 那無窮無盡的入侵者艦隊，此刻正將汽化炮鎖定在你們的位置上，
我族將盡快為你們終結那痛苦、詭異畸形的存在。
在此期間，請享受一點音樂……
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×3 / 之×4 / 乃×1 / 吾等×2 / 爾等×3

**你的選擇**：`HOMEWORLD_HELLO_1=A`（shipped）/ `HOMEWORLD_HELLO_1=B`（v3）/ `HOMEWORLD_HELLO_1=C自訂:...`

---

### #42 · `HOMEWORLD_HELLO_2` · 🟠 rewording · sim=0.437; 文言助詞清除=19

**英文原文**：
```
Hello again.  We trust you are enjoying trespassing in VUX space
and look forward to removing you from existence at our earliest possible convenience.
If you believe you can fight your way past our invincible forces to our surface, you are correct.
Some ash and a few wisps of pungent vapor are sure to make it at least that far.
Our special today is particle fragmentation!
So if you will kindly open your feeding orifice and start screaming, we will begin.
```

**Shipped v0.5.1**：
```
再度歡迎光臨。 吾等相信爾等享受於 VUX 領空之擅闖
並期待於最早之便將爾等自存在中抹除。
若爾等相信可殺出一條血路穿過吾等無敵之艦隊抵達地表，那爾等說對了。
一些灰燼與幾縷刺鼻煙霧倒是有機會抵達那裡。
本日特惠：粒子碎裂術！
故若爾等願張開進食孔並開始尖叫，吾等即可開始。
```

**Rebuild v3 (clean-room v0.7)**：
```
您好，我們又見面了。 我族 VUX 相信你們一定很享受非法闖入 VUX 領空的過程，
也期待能在最方便的時機，將你們從這個宇宙中移除。
如果你們認為能一路殺過我族 VUX 無敵的艦隊、抵達地表—— 恭喜答對了。
幾團灰燼和幾縷刺鼻的蒸氣，肯定至少能抵達那麼遠。
我族本日的特餐是：粒子碎裂術！
所以請你們親切地張開進食用的孔洞，開始尖叫—— 我族這就上菜。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×5 / 之×3 / 吾等×3 / 爾等×5

**你的選擇**：`HOMEWORLD_HELLO_2=A`（shipped）/ `HOMEWORLD_HELLO_2=B`（v3）/ `HOMEWORLD_HELLO_2=C自訂:...`

---

### #43 · `HOMEWORLD_HELLO_3` · 🟠 rewording · sim=0.647; 文言助詞清除=6

**英文原文**：
```
Welcome back to total annihilation, where, as they say
once is silatious, twice is phlagrant melons
but the third time is when it really hurts.
Please stay seated until your vessel starts smoking
then feel free to dash your head painfully against the floor.
```

**Shipped v0.5.1**：
```
歡迎回到全面殲滅，正如俗諺所云
一次乃謔語，二次是明目張膽的西瓜
但第三次可就真的痛了。
請保持座位，直至爾等艦艇開始冒煙
然後隨意將爾等之頭撞向地板享受痛楚。
```

**Rebuild v3 (clean-room v0.7)**：
```
歡迎再度光臨全面殲滅—— 正如俗話所說，
一次是嬉哩語，二次是明目張膽的西瓜，
但第三次可就真的痛了。
請乖乖坐好，直到你們的艦艇開始冒煙——
然後歡迎痛快地把頭往地板上撞。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×2 / 之×1 / 乃×1 / 爾等×2

**你的選擇**：`HOMEWORLD_HELLO_3=A`（shipped）/ `HOMEWORLD_HELLO_3=B`（v3）/ `HOMEWORLD_HELLO_3=C自訂:...`

---

### #44 · `HOMEWORLD_HELLO_4` · 🟠 rewording · sim=0.518; 文言助詞清除=10

**英文原文**：
```
Congratulations for exhausting the VUX vocabulary of greetings to despicable life-forms.
May we take this opportunity to lock our femoral scrapers onto your ship
and to wish you an unpleasant afterlife.
```

**Shipped v0.5.1**：
```
恭喜爾等耗盡了 VUX 對卑劣生命體之全部問候詞彙。
藉此機緣，容吾等將股節刮刀鎖定於爾等艦上
並祝爾等擁有一個不愉快之來世。
```

**Rebuild v3 (clean-room v0.7)**：
```
恭喜你們，把 VUX 用來問候卑劣生命形態的詞彙全部耗盡了。
藉此機會，讓我族 VUX 把股節刮刀鎖定在你們的艦艇上，
並祝各位有個不甚愉快的死後生活。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×3 / 之×2 / 吾等×1 / 爾等×3

**你的選擇**：`HOMEWORLD_HELLO_4=A`（shipped）/ `HOMEWORLD_HELLO_4=B`（v3）/ `HOMEWORLD_HELLO_4=C自訂:...`

---

### #45 · `SPACE_HELLO_1` · 🔴 semantic/voice rewrite · sim=0.339; 文言助詞清除=5

**英文原文**：
```
Greetings from VUX!... the last word in life form destruction!
To gain an intimate knowledge of our engines of war
simply place both hands over your eyes and count to three.
```

**Shipped v0.5.1**：
```
來自 VUX 之問候！……生命體毀滅之最終定義！
欲親密體驗吾等之戰爭引擎
只需雙手蒙眼並數到三。
```

**Rebuild v3 (clean-room v0.7)**：
```
VUX 向你們問好！…… 生命形態毀滅界的終極品牌！
若想深入了解我族 VUX 的戰爭引擎，
只要把雙手蒙住眼睛，數到三就好。
```

**推薦**：B (v3) — shipped 語體徹底錯位，v3 依 v0.7 dossier 重建，必採 v3

**說明**：shipped 含文言污染: 吾×1 / 之×3 / 吾等×1

**你的選擇**：`SPACE_HELLO_1=A`（shipped）/ `SPACE_HELLO_1=B`（v3）/ `SPACE_HELLO_1=C自訂:...`

---

### #46 · `SPACE_HELLO_2` · 🟠 rewording · sim=0.494; 文言助詞清除=13

**英文原文**：
```
Salutations, and may your sense of self-preservation always be so dim.
As our Intruders surround your vessel, you may care to raise both hands into the air above you
and practice the ancient chant of the prancing oowee master, ZEN DUX, which begins...
`AAAAAAAAA AAAAAAHH!!!'
```

**Shipped v0.5.1**：
```
致意，願爾等之自保直覺永如今日昏昧。
當吾等之入侵者包圍爾等艦艇之時，爾等或可高舉雙手於頭頂之上
並演練舞動嗷嗚大師禪·杜克斯（ZEN DUX）之古老禱唸，起句為……
『啊啊啊啊啊 啊啊啊嗨──！！！（AAAAAAAAA AAAAAAHH!!!）』
```

**Rebuild v3 (clean-room v0.7)**：
```
恭祝各位安好，願你們的求生本能永遠都這麼遲鈍。
當我族 VUX 的入侵者艦圍住你們艦艇時，各位不妨將雙手高舉過頭，
練習一段那位嬉戲跳躍的舞動嗷嗚大師禪·杜克斯（ZEN DUX） 傳下的古老咒語，起頭是——
「AAAAAAAAA AAAAAAHH！！！」
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×3 / 之×5 / 吾等×1 / 爾等×3

**你的選擇**：`SPACE_HELLO_2=A`（shipped）/ `SPACE_HELLO_2=B`（v3）/ `SPACE_HELLO_2=C自訂:...`

---

### #47 · `SPACE_HELLO_3` · 🟠 rewording · sim=0.412; 文言助詞清除=11

**英文原文**：
```
This is VUX Commander YAX.  On behalf of the team here
I would like to say how very much we have all enjoyed taunting you
and to congratulate you on plumbing the limits of VUX courtesy
which you have now exhausted. Therefore, let me just say
Die, you two-eyed loathsome faceless slug!
```

**Shipped v0.5.1**：
```
本官乃 VUX 指揮官雅克斯（YAX）。 謹代表此地團隊
本官欲表示吾等所有人多麼享受嘲弄爾等之過程
並恭賀爾等已達 VUX 禮儀之極限
此刻已然耗盡。 故此，容本官直說吧
去死，爾這雙眼、令人厭惡、無臉之肉蛞蝓！
```

**Rebuild v3 (clean-room v0.7)**：
```
這裡是 VUX 指揮官雅克斯（YAX）。 代表艦上全體同仁，
我想說我族 VUX 這幾天嘲弄你們，實在玩得很開心，
也恭喜你們把 VUX 的禮貌極限給探底了——
現在你們已經徹底把它耗完。 所以，容我直說——
去死吧，你們這些兩眼、噁心、沒臉的鼻涕蟲！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×3 / 之×3 / 乃×1 / 吾等×1 / 爾等×2

**你的選擇**：`SPACE_HELLO_3=A`（shipped）/ `SPACE_HELLO_3=B`（v3）/ `SPACE_HELLO_3=C自訂:...`

---

### #48 · `SPACE_HELLO_4` · 🟠 rewording · sim=0.547; 文言助詞清除=7

**英文原文**：
```
Welcome back. All our coherent destructors are currently off-line
but if you'd care to hold your present course and speed
one will be free to annihilate you shortly.
```

**Shipped v0.5.1**：
```
歡迎回來。 吾等所有之相干湮滅炮此刻皆已離線
但若爾等願保持當前航向與速度
稍後便會有一具湮滅炮空出來將爾等殲滅。
```

**Rebuild v3 (clean-room v0.7)**：
```
歡迎回來。 我族 VUX 所有的相干湮滅炮目前都處於離線狀態，
但如果各位願意保持目前的航向和速度，
很快就會有一具空出來，可以把你們湮滅了。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×2 / 之×1 / 吾等×1 / 爾等×2

**你的選擇**：`SPACE_HELLO_4=A`（shipped）/ `SPACE_HELLO_4=B`（v3）/ `SPACE_HELLO_4=C自訂:...`

---

### #49 · `kill_you_squids_1` · 🟠 rewording · sim=0.612; 文言助詞清除=0

**英文原文**：
```
You grotesque squids! We will kill you for your insolence!
```

**Shipped v0.5.1**：
```
你這噁心的章魚！ 我方將為你的無禮而殺了你！
```

**Rebuild v3 (clean-room v0.7)**：
```
你們這些詭異畸形的烏賊！ 我方要為你們的無禮宰了你們！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`kill_you_squids_1=A`（shipped）/ `kill_you_squids_1=B`（v3）/ `kill_you_squids_1=C自訂:...`

---

### #50 · `kill_you_squids_2` · 🟠 rewording · sim=0.829; 文言助詞清除=0

**英文原文**：
```
You are the most vile, repulsive creature I've ever seen!
```

**Shipped v0.5.1**：
```
你是我這輩子見過最卑劣、最令人反胃的生物！
```

**Rebuild v3 (clean-room v0.7)**：
```
你們是我這輩子見過最卑劣、最噁心的生物！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`kill_you_squids_2=A`（shipped）/ `kill_you_squids_2=B`（v3）/ `kill_you_squids_2=C自訂:...`

---

### #51 · `kill_you_squids_3` · 🟠 rewording · sim=0.711; 文言助詞清除=0

**英文原文**：
```
I must say, your rating on the vomit-meter would be AT LEAST ninety six.
```

**Shipped v0.5.1**：
```
我得說，你在嘔吐計上至少能拿到九十六分。
```

**Rebuild v3 (clean-room v0.7)**：
```
我必須說，你們在嘔吐計上的評分「至少」有九十六分。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`kill_you_squids_3=A`（shipped）/ `kill_you_squids_3=B`（v3）/ `kill_you_squids_3=C自訂:...`

---

### #52 · `kill_you_squids_4` · 🟠 rewording · sim=0.562; 文言助詞清除=0

**英文原文**：
```
You bloated bag of protoplasm! You worm!
```

**Shipped v0.5.1**：
```
你這膨脹的原生質袋！ 你這條蟲！
```

**Rebuild v3 (clean-room v0.7)**：
```
你們這些腐肉袋！ 你們這些蠕蟲！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`kill_you_squids_4=A`（shipped）/ `kill_you_squids_4=B`（v3）/ `kill_you_squids_4=C自訂:...`

---

### #53 · `WE_FIGHT` · 🟠 rewording · sim=0.360; 文言助詞清除=3

**英文原文**：
```
Watch everybody! We're going to kill the repulsive little monster now!
```

**Shipped v0.5.1**：
```
大家看！ 吾等即將宰殺這頭令人反胃之小怪物！
```

**Rebuild v3 (clean-room v0.7)**：
```
各位看好囉！ 我族 VUX 這就要宰了這隻噁心的小怪物！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 之×1 / 吾等×1

**你的選擇**：`WE_FIGHT=A`（shipped）/ `WE_FIGHT=B`（v3）/ `WE_FIGHT=C自訂:...`

---

### #54 · `why_so_mean` · 🟠 rewording · sim=0.588; 文言助詞清除=0

**英文原文**：
```
Why are you so hostile toward our species?
```

**Shipped v0.5.1**：
```
你們為何對我方物種如此充滿敵意？
```

**Rebuild v3 (clean-room v0.7)**：
```
你們為什麼對我們這個物種這麼有敵意？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`why_so_mean=A`（shipped）/ `why_so_mean=B`（v3）/ `why_so_mean=C自訂:...`

---

### #55 · `URQUAN_SLAVES` · 🟠 rewording · sim=0.531; 文言助詞清除=32

**英文原文**：
```
Augh! You are even uglier than I had thought possible!
Can't you see you are making me sick?
Please, foul creature, turn your head, or better yet, put a sack over it.
Never mind, I have adjusted my display so it is dim enough to be tolerable.
In answer to your question, our response is simple.
We must attack you because our masters the Ur-Quan wish it so!
Now if you don't mind, stop nodding your head like that.
We VUX do not share this range of motion
and it appears as though your neck is broken
and you are a jabbering corpse. Ugh.
```

**Shipped v0.5.1**：
```
噁啊！（AUGH!） 爾等比本官所能想像的還要醜陋！
爾等看不出爾等使本官反胃嗎？
拜託，卑劣之物，請轉開爾等之頭，或者更好，蒙個袋子上去。
算了，本官已調暗顯示器，勉強可以忍受。
以回答爾等之問，吾等之答覆很簡單。
吾等必須攻擊爾等，因為吾等之主宰烏寬希望如此！
現在若爾等不介意，請別再那樣點頭。
吾等 VUX 沒有此範圍之動作
看起來就像爾等的脖子斷了
爾等成了一具喋喋不休的屍體。 呃（Ugh）。
```

**Rebuild v3 (clean-room v0.7)**：
```
噁！（Augh!） 你比我想像的還醜！
你難道看不出你正在讓我噁心嗎？
拜託，噁心的東西，把頭轉過去；或者更好—— 用袋子套住它。
算了，我把顯示螢幕調暗了—— 現在總算勉強能忍受。
回答你的問題，我方答案很簡單。
我族 VUX 必須攻擊你，因為我們的主人烏寬要求如此！
順道一提，麻煩不要那樣點頭。
我族 VUX 沒有那樣的動作範圍，
看起來就像你的脖子斷了、
你是一具嘰哩呱啦的屍體。 呃。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×4 / 爾×9 / 之×6 / 吾等×4 / 爾等×9

**你的選擇**：`URQUAN_SLAVES=A`（shipped）/ `URQUAN_SLAVES=B`（v3）/ `URQUAN_SLAVES=C自訂:...`

---

### #56 · `deeper_reason` · 🟠 rewording · sim=0.609; 文言助詞清除=0

**英文原文**：
```
Is there another reason you hate us? Come on, tell me the truth.
```

**Shipped v0.5.1**：
```
你們還有其他理由恨我方嗎？ 拜託，告訴我真相。
```

**Rebuild v3 (clean-room v0.7)**：
```
你們恨我們還有別的理由嗎？ 拜託，跟我說實話。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`deeper_reason=A`（shipped）/ `deeper_reason=B`（v3）/ `deeper_reason=C自訂:...`

---

### #57 · `OLD_INSULT` · 🟠 rewording · sim=0.466; 文言助詞清除=27

**英文原文**：
```
Do we need another reason?
Ah! I understand. You refer to the First Human Encounter
the Insult!
What more can be said? On that day, your species proved its true crass nature.
You see, we VUX pride ourselves on our open-mindedness
our ability to see beyond even the most bizarre and disgusting face like yours
but that insult was so low, so totally reprehensible that we will never forget it.
Yes, to be honest, that event pretty much fixed our attitude setting at `ABHOR'.
I suspect we will despise you forever.
```

**Shipped v0.5.1**：
```
吾等需要其他理由嗎？
啊！ 本官明白了。 爾等指的是首次人類接觸
那次侮辱！
還有什麼好說的？ 於那一日，爾等物種證明了其真實粗鄙之本質。
瞧瞧，吾等 VUX 為吾等心胸開明感到自豪
吾等能看透最古怪、最令人厭惡之面孔，如爾等的
但那次侮辱如此卑劣，如此徹底可鄙，吾等永難遺忘。
是的，坦白說，那次事件幾乎就此固定了吾等對爾等之態度為「厭惡」。
本官懷疑吾等將永遠鄙視爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
還需要別的理由嗎？
啊！ 我懂了。 你在說首次人類接觸——
那次侮辱！
還能說什麼？ 那一天，你們這個物種就顯露了真正粗鄙的本性。
你要知道，我族 VUX 一向自豪於自己的開明態度，
自豪於能看穿那些像你這種怪異又噁心的臉——
但那句侮辱實在太低級、太罪不可恕，我族 VUX 永遠不會忘記。
是的，說老實話，那件事幾乎把我族的態度設定固定在「厭惡」上了。
我想我族 VUX 會永遠鄙視你們。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×7 / 爾×5 / 之×3 / 吾等×7 / 爾等×5

**你的選擇**：`OLD_INSULT=A`（shipped）/ `OLD_INSULT=B`（v3）/ `OLD_INSULT=C自訂:...`

---

### #58 · `if_we_apologize` · 🟠 rewording · sim=0.629; 文言助詞清除=1

**英文原文**：
```
What if we apologized? Could we talk truce then?
```

**Shipped v0.5.1**：
```
如果我們道歉呢？ 之後就能談和平嗎？
```

**Rebuild v3 (clean-room v0.7)**：
```
如果我方道歉呢？ 那能不能談停戰？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 之×1

**你的選擇**：`if_we_apologize=A`（shipped）/ `if_we_apologize=B`（v3）/ `if_we_apologize=C自訂:...`

---

### #59 · `PROBABLY_NOT` · 🟠 rewording · sim=0.528; 文言助詞清除=11

**英文原文**：
```
Er... probably not. You see, although we VUX are highly reasonable beings
who would never judge a race solely on its (urk!) appearance
the magnitude of your Captain Rand's insult was such that we will probably never forgive your species.
```

**Shipped v0.5.1**：
```
呃……大概不行。 您瞧，儘管吾等 VUX 是極度講理之生物
從不會單憑一個族類之（呃咳！（urk!））外貌就定其罪
但爾等蘭德艦長之侮辱程度如此嚴重，恐怕吾等永難原諒爾等物種。
```

**Rebuild v3 (clean-room v0.7)**：
```
呃…… 大概不行。 你要知道，雖然我族 VUX 是非常理性的存在，
絕不會單憑一個種族的（噎——！）（urk!） 外表就對它下判斷——
但你們的蘭德艦長那句侮辱的嚴重程度，我族 VUX 大概永遠也不會原諒你們這個物種。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 之×3 / 吾等×2 / 爾等×2

**你的選擇**：`PROBABLY_NOT=A`（shipped）/ `PROBABLY_NOT=B`（v3）/ `PROBABLY_NOT=C自訂:...`

---

### #60 · `try_any_way` · 🟠 rewording · sim=0.585; 文言助詞清除=0

**英文原文**：
```
Well, I'll try anyway. The People of Earth Hereby Apologize To The VUX!
```

**Shipped v0.5.1**：
```
好吧，我還是試試。 地球人在此正式向 VUX 道歉！
```

**Rebuild v3 (clean-room v0.7)**：
```
不管怎樣，我還是試試看。 地—球—全—體—人—民—在—此—向—VUX—致—歉！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`try_any_way=A`（shipped）/ `try_any_way=B`（v3）/ `try_any_way=C自訂:...`

---

### #61 · `NOPE` · 🟠 rewording · sim=0.649; 文言助詞清除=4

**英文原文**：
```
Nope. I didn't think that would be sufficient. It lacked conviction.
Sorry, but I'm afraid we'll just have to kill you now.
```

**Shipped v0.5.1**：
```
不行。 本官早覺得那不夠。 缺乏誠意。
抱歉，恐怕吾等現在只能宰了爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
不行。 我早就覺得那不夠格。 誠意太少。
抱歉，恐怕我族 VUX 只好把你們宰了。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×1 / 吾等×1 / 爾等×1

**你的選擇**：`NOPE=A`（shipped）/ `NOPE=B`（v3）/ `NOPE=C自訂:...`

---

### #62 · `APOLOGIZE_IN_SPACE` · 🟠 rewording · sim=0.479; 文言助詞清除=11

**英文原文**：
```
Because the Human named Rand offended one of our starship commanders
apologizing here at the Homeworld is useless.
Besides, we have decided that you are just too disgusting to live
so we have decided to vaporize you.
```

**Shipped v0.5.1**：
```
因為那個叫蘭德的人類冒犯了吾等之一位星艦指揮官
在此於母星道歉毫無意義。
再者，吾等已判定爾等實在太過噁心不宜苟活
故吾等已決定將爾等汽化。
```

**Rebuild v3 (clean-room v0.7)**：
```
因為那個叫蘭德的人類冒犯的，是我族 VUX 其中一位艦長，
所以在母星這裡道歉根本沒用。
況且，我族 VUX 已經決定—— 你們實在太噁心，不配活著，
所以我族 VUX 決定把你們汽化。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×3 / 爾×2 / 之×1 / 吾等×3 / 爾等×2

**你的選擇**：`APOLOGIZE_IN_SPACE=A`（shipped）/ `APOLOGIZE_IN_SPACE=B`（v3）/ `APOLOGIZE_IN_SPACE=C自訂:...`

---

### #63 · `apology_1` · 🟠 rewording · sim=0.659; 文言助詞清除=0

**英文原文**：
```
Let's try that again. We, The People Of Earth, Really Truly Apologize For The Stupid Insult Made By Captain Rand!
```

**Shipped v0.5.1**：
```
再試一次。 我地球人民，真心誠意地為蘭德艦長那句愚蠢的侮辱道歉！
```

**Rebuild v3 (clean-room v0.7)**：
```
我們再試一次。 我—們—地—球—全—體—人—民，為蘭德艦長那句愚蠢的侮辱，「真—心—誠—意」地道歉！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_1=A`（shipped）/ `apology_1=B`（v3）/ `apology_1=C自訂:...`

---

### #64 · `NOT_ACCEPTED_1` · 🟠 rewording · sim=0.842; 文言助詞清除=0

**英文原文**：
```
No. That didn't cut it either.
```

**Shipped v0.5.1**：
```
不。 這也不合格。
```

**Rebuild v3 (clean-room v0.7)**：
```
不行。 這也不夠格。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`NOT_ACCEPTED_1=A`（shipped）/ `NOT_ACCEPTED_1=B`（v3）/ `NOT_ACCEPTED_1=C自訂:...`

---

### #65 · `apology_2` · 🟠 rewording · sim=0.808; 文言助詞清除=0

**英文原文**：
```
You were RIGHT! We WERE wrong. We see it all so clearly now!
```

**Shipped v0.5.1**：
```
你們是對的！ 是我方錯了。 我方現在全都看清了！
```

**Rebuild v3 (clean-room v0.7)**：
```
你們「說得對」！ 我方「錯了」。 我方現在全都看清楚了！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_2=A`（shipped）/ `apology_2=B`（v3）/ `apology_2=C自訂:...`

---

### #66 · `NOT_ACCEPTED_2` · 🔴 semantic/voice rewrite · sim=0.348; 文言助詞清除=2

**英文原文**：
```
I don't think your heart is in it.
```

**Shipped v0.5.1**：
```
本官覺得爾等心口不一。
```

**Rebuild v3 (clean-room v0.7)**：
```
我覺得你們沒有真心誠意。
```

**推薦**：B (v3) — shipped 語體徹底錯位，v3 依 v0.7 dossier 重建，必採 v3

**說明**：shipped 含文言污染: 爾×1 / 爾等×1

**你的選擇**：`NOT_ACCEPTED_2=A`（shipped）/ `NOT_ACCEPTED_2=B`（v3）/ `NOT_ACCEPTED_2=C自訂:...`

---

### #67 · `apology_3` · 🔴 semantic/voice rewrite · sim=0.300; 文言助詞清除=0

**英文原文**：
```
Pleeeeeeeeease forgive us!
```

**Shipped v0.5.1**：
```
求求你們原諒！！！
```

**Rebuild v3 (clean-room v0.7)**：
```
拜——託——原諒我方！
```

**推薦**：B (v3) — shipped 語體徹底錯位，v3 依 v0.7 dossier 重建，必採 v3

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_3=A`（shipped）/ `apology_3=B`（v3）/ `apology_3=C自訂:...`

---

### #68 · `NOT_ACCEPTED_3` · 🟠 rewording · sim=0.554; 文言助詞清除=6

**英文原文**：
```
You said that just because you want stuff from us VUX. You didn't really mean it.
```

**Shipped v0.5.1**：
```
爾等這麼說只是因為想從吾等 VUX 這裡拿東西。 爾等並非真心。
```

**Rebuild v3 (clean-room v0.7)**：
```
你們只是想從我族 VUX 這裡要東西才這麼說的。 根本不是真心話。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×2 / 吾等×1 / 爾等×2

**你的選擇**：`NOT_ACCEPTED_3=A`（shipped）/ `NOT_ACCEPTED_3=B`（v3）/ `NOT_ACCEPTED_3=C自訂:...`

---

### #69 · `apology_4` · 🟠 rewording · sim=0.523; 文言助詞清除=1

**英文原文**：
```
We - are - sorry! May a thousand insects sting my softest parts if I lie!
```

**Shipped v0.5.1**：
```
我 - 們 - 錯 - 了！ 若我方說謊，願千蟲叮我方最軟嫩之處！
```

**Rebuild v3 (clean-room v0.7)**：
```
我—方—錯—了！ 如果我方說謊，就讓一千隻昆蟲叮遍我最軟的地方！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 之×1

**你的選擇**：`apology_4=A`（shipped）/ `apology_4=B`（v3）/ `apology_4=C自訂:...`

---

### #70 · `NOT_ACCEPTED_4` · 🟠 rewording · sim=0.609; 文言助詞清除=0

**英文原文**：
```
It's pointless. Why even bother trying again?
```

**Shipped v0.5.1**：
```
毫無意義。 何必再試？
```

**Rebuild v3 (clean-room v0.7)**：
```
沒意義。 幹嘛還要再試？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`NOT_ACCEPTED_4=A`（shipped）/ `NOT_ACCEPTED_4=B`（v3）/ `NOT_ACCEPTED_4=C自訂:...`

---

### #71 · `apology_5` · 🟠 rewording · sim=0.746; 文言助詞清除=0

**英文原文**：
```
We would like to present a petition of 1 million signatures! Each one says, `I'm sorry!'
```

**Shipped v0.5.1**：
```
我方要呈上一份百萬人聯署書！ 每份都寫著『對不起』！
```

**Rebuild v3 (clean-room v0.7)**：
```
我方想呈上一份有一百萬人連署的請願書！ 每一份都寫著：「對不起！」
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_5=A`（shipped）/ `apology_5=B`（v3）/ `apology_5=C自訂:...`

---

### #72 · `NOT_ACCEPTED_5` · 🟠 rewording · sim=0.733; 文言助詞清除=0

**英文原文**：
```
A good try, Captain... but not good enough.
```

**Shipped v0.5.1**：
```
好嘗試，艦長……但仍不夠。
```

**Rebuild v3 (clean-room v0.7)**：
```
不錯的嘗試，艦長…… 但還不夠好。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`NOT_ACCEPTED_5=A`（shipped）/ `NOT_ACCEPTED_5=B`（v3）/ `NOT_ACCEPTED_5=C自訂:...`

---

### #73 · `apology_6` · 🟠 rewording · sim=0.658; 文言助詞清除=0

**英文原文**：
```
Wrong? Yes we were wrong. Oh, so wrong! Boy, were we wrong! The wrongest.
```

**Shipped v0.5.1**：
```
錯了嗎？ 沒錯，我方是錯了。 噢，錯得離譜！ 天啊，我們錯了！ 錯得徹底透頂。
```

**Rebuild v3 (clean-room v0.7)**：
```
錯了？ 是的，我方錯了。 喔，錯到不行！ 天啊，我方真是錯了！ 錯到極致。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_6=A`（shipped）/ `apology_6=B`（v3）/ `apology_6=C自訂:...`

---

### #74 · `NOT_ACCEPTED_6` · 🟠 rewording · sim=0.560; 文言助詞清除=4

**英文原文**：
```
We detect a hint of genuine regret, but not enough to forgive you.
```

**Shipped v0.5.1**：
```
吾等察覺一絲真誠悔意，但仍不足以原諒爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
我族 VUX 有感覺到一絲真心的悔意，但還不足以原諒你們。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×1 / 吾等×1 / 爾等×1

**你的選擇**：`NOT_ACCEPTED_6=A`（shipped）/ `NOT_ACCEPTED_6=B`（v3）/ `NOT_ACCEPTED_6=C自訂:...`

---

### #75 · `apology_7` · 🟠 rewording · sim=0.756; 文言助詞清除=0

**英文原文**：
```
(Let's try reverse psychology) Listen VUX! You are right! We cannot ever atone for Rand's cruel barb!
```

**Shipped v0.5.1**：
```
（來試試反向心理）聽好 VUX！ 你們是對的！ 我方永遠無法補救蘭德那殘忍的一句！
```

**Rebuild v3 (clean-room v0.7)**：
```
（試試反向心理）聽好了 VUX！ 你們說得對！ 我方永遠彌補不了蘭德那句狠毒的話！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_7=A`（shipped）/ `apology_7=B`（v3）/ `apology_7=C自訂:...`

---

### #76 · `NOT_ACCEPTED_7` · 🟠 rewording · sim=0.488; 文言助詞清除=6

**英文原文**：
```
Oh? I was just thinking that maybe we should consider forgiving you
but I guess you're right.
There's no going back.
```

**Shipped v0.5.1**：
```
噢？ 本官正在想或許吾等應該考慮原諒爾等
但看來爾等自己說對了。
沒有回頭路了。
```

**Rebuild v3 (clean-room v0.7)**：
```
喔？ 我方本來還在想，或許我族該考慮原諒你們——
但看來你們說得對。
確實回不去了。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×2 / 吾等×1 / 爾等×2

**你的選擇**：`NOT_ACCEPTED_7=A`（shipped）/ `NOT_ACCEPTED_7=B`（v3）/ `NOT_ACCEPTED_7=C自訂:...`

---

### #77 · `apology_8` · 🟠 rewording · sim=0.696; 文言助詞清除=1

**英文原文**：
```
If sorrow were a pebble, our remorse would be... would be!... a great big boulder!
```

**Shipped v0.5.1**：
```
若哀傷是一顆卵石，我方之悔恨便是……便是！……一顆巨大的巨石！
```

**Rebuild v3 (clean-room v0.7)**：
```
如果悲傷是一顆小石頭，那我方的悔恨就會是…… 就會是！…… 一顆超大的巨石！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 之×1

**你的選擇**：`apology_8=A`（shipped）/ `apology_8=B`（v3）/ `apology_8=C自訂:...`

---

### #78 · `NOT_ACCEPTED_8` · 🟠 rewording · sim=0.485; 文言助詞清除=5

**英文原文**：
```
Hey! That was pretty good!
I could sense the true sadness in your voice for your species' past stupidity.
Unfortunately, it was not good enough.
```

**Shipped v0.5.1**：
```
喂！ 那還挺好的！
本官感受到爾等聲音中對爾等物種過往愚行之真實哀傷。
可惜，仍不夠好。
```

**Rebuild v3 (clean-room v0.7)**：
```
欸！ 剛才那個還不錯！
我族 VUX 能感受到你們聲音裡真正的悲傷—— 為你們物種過去的愚蠢而悲傷。
可惜，還不夠好。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×2 / 之×1 / 爾等×2

**你的選擇**：`NOT_ACCEPTED_8=A`（shipped）/ `NOT_ACCEPTED_8=B`（v3）/ `NOT_ACCEPTED_8=C自訂:...`

---

### #79 · `apology_9` · 🟠 rewording · sim=0.604; 文言助詞清除=0

**英文原文**：
```
If there is ANYTHING we can do to gain your forgiveness, we shall do it a thousand times.
```

**Shipped v0.5.1**：
```
若有任何事我方能做以獲得你們原諒，我方將做上千遍。
```

**Rebuild v3 (clean-room v0.7)**：
```
如果有「任何」事情可以換得你們的原諒，我方願意做一千次。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_9=A`（shipped）/ `apology_9=B`（v3）/ `apology_9=C自訂:...`

---

### #80 · `NOT_ACCEPTED_9` · 🟠 rewording · sim=0.540; 文言助詞清除=2

**英文原文**：
```
Um..., er... that was about as good as it gets, I think
but we don't accept it because... because... well, just BECAUSE!
```

**Shipped v0.5.1**：
```
嗯……呃……那已經是極致了，本官認為
但吾等不接受，因為……因為……嗯，就是不行！
```

**Rebuild v3 (clean-room v0.7)**：
```
嗯…… 呃…… 我想那大概是能講到的最好版本了——
但我族 VUX 就是不接受，因為…… 因為…… 呃，「就是因為」！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 吾等×1

**你的選擇**：`NOT_ACCEPTED_9=A`（shipped）/ `NOT_ACCEPTED_9=B`（v3）/ `NOT_ACCEPTED_9=C自訂:...`

---

### #81 · `apology_10` · 🟠 rewording · sim=0.784; 文言助詞清除=0

**英文原文**：
```
Please, for the love of reason. Heed these words: We, the People of Earth Apologize To The VUX.
```

**Shipped v0.5.1**：
```
拜託，看在理性的份上。 請聽好這句話：我地球人民向 VUX 道歉。
```

**Rebuild v3 (clean-room v0.7)**：
```
拜託，行行好，看在理智的份上，請聽好這句話：我們—地球全體人民—向 VUX 致歉。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`apology_10=A`（shipped）/ `apology_10=B`（v3）/ `apology_10=C自訂:...`

---

### #82 · `TRUTH` · 🟠 rewording · sim=0.459; 文言助詞清除=81

**英文原文**：
```
AIEEE! Human! You have hounded and hounded and hounded us with your pitiful apologies!
It's driving us crazy! STOP! Please STOP!
We give up. We accept! We accept! We will no longer hold Rand's insult against your species.
You are forgiven for all eternity, just stop apologizing!
But now you have forced us to reveal our REAL reason for hating you humans
an embarrassing reason with no acceptable justification, but nonetheless undeniable!
Human! You are SOOO ugly, SOOO hideous to us that we will NEVER be able to find peace with your species!
Whenever we see your kind, we just want to kick you!... stomp on you!... squish you!...
...vaporize your ugly faces from the entire universe!
We know its unreasonable! We know that you had no choice about how you look!
We know that it is cruel fate that the Creator made you appear like putrid excretion
but WE JUST CAN'T HANDLE IT!
Why right now, because of your insufferable wretchedness
I am faced with a grotesque choice: keep talking to you and regurgitate uncontrollably
or break off communication and attack your vessel...
```

**Shipped v0.5.1**：
```
啊咦咦咦咦──！！！！！（AIEEE!!!） 人類！ 爾等以爾等可憐之道歉糾纏、糾纏、又糾纏吾等！
這快把吾等逼瘋了！ 停下！ 求求爾等停下！
吾等投降。 吾等接受！ 吾等接受！ 吾等將不再懷恨蘭德對爾等物種之侮辱。
爾等永被寬恕，只求爾等停止道歉！
但現在爾等逼吾等揭露對爾等人類真正之恨意
一個難堪之理由，一個毫無正當性之理由，卻無可否認！
人類！ 爾等對吾等而言是如此醜陋，如此可怖，吾等永遠無法與爾等物種求得和平！
每當吾等見到爾等族類，吾等只想踹爾等！……踩踏爾等！……擠爆爾等！
……將爾等醜陋之臉自宇宙中汽化！
吾等知道這不合理！ 吾等知道爾等對自己之外貌別無選擇！
吾等知道這是命運之殘酷，造物主使爾等看似腐爛之排泄物
但吾等就是無法忍受！
為何此刻，因爾等難以忍受之卑劣
本官面臨一個怪異之抉擇：繼續與爾等交談並無法自控地嘔吐
或中斷通訊並攻擊爾等艦艇……
```

**Rebuild v3 (clean-room v0.7)**：
```
啊咦咦咦咦──！！！（AIEEE!!!） 人類！ 你不停地、不停地、不停地拿你們那可悲的道歉煩我族 VUX！
快讓我族 VUX 發瘋了！ 停！ 拜託停下來！
我族 VUX 投降。 我族 VUX 接受！ 我族 VUX 接受！ 我族 VUX 不再拿蘭德那句侮辱記恨你們這個物種。
你們永遠都被原諒了，拜託不要再道歉了！
但現在你們逼得我族 VUX 不得不揭露「真正」恨你們人類的理由——
一個難堪的理由、一個沒有正當理由的理由，卻無可否認！
人類！ 你們對我族 VUX 而言「太—醜—了」、「太—可—怖—了」，我族 VUX 「永遠」無法與你們這個物種和平共處！
每當我族 VUX 看見你們，就只想踹你們！…… 踩爛你們！…… 擠扁你們！……
…… 把你們醜陋的臉，從整個宇宙裡汽化！
我族 VUX 知道這不合理！ 我族 VUX 知道你們對自己的長相無從選擇！
我族 VUX 知道這是命運的殘酷—— 造物主讓你們長得像腐爛的排泄物——
但我族 VUX 「就是無法忍受」！
就在此刻，因為你們令人難以忍受的卑劣，
我面臨一個詭異的抉擇：繼續跟你們談下去、忍不住嘔吐出來，
還是切斷通訊、攻擊你們的艦艇……
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×15 / 爾×20 / 之×11 / 吾等×15 / 爾等×20

**你的選擇**：`TRUTH=A`（shipped）/ `TRUTH=B`（v3）/ `TRUTH=C自訂:...`

---

### #83 · `whats_up_hostile` · 🟠 rewording · sim=0.684; 文言助詞清除=0

**英文原文**：
```
VUX. We seek to learn more about you. Maybe then we can see eye to... eyes.
```

**Shipped v0.5.1**：
```
VUX 們。 我方想多了解你們一些。 或許屆時我方能與你們……眼對眼地相看。
```

**Rebuild v3 (clean-room v0.7)**：
```
VUX。 我方想多了解你們一點。 或許這樣我們才能「眼對……眼」互相看清楚。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`whats_up_hostile=A`（shipped）/ `whats_up_hostile=B`（v3）/ `whats_up_hostile=C自訂:...`

---

### #84 · `GENERAL_INFO_HOSTILE_1` · 🟠 rewording · sim=0.745; 文言助詞清除=6

**英文原文**：
```
Look, vomitous alien. If you want to talk to one of our species
without making them sick
why don't you go see Admiral ZEX at his world in <% comm.getStarName("Alpha Cerenkov", "maidens") %>.
He (urp!) likes humans.
```

**Shipped v0.5.1**：
```
聽好，令人作嘔之異形。 若爾等想跟吾等物種之一位交談
而不讓他反胃
何不去 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） 拜訪澤克斯上將。
他（呃啊！（urp!））喜好人類。
```

**Rebuild v3 (clean-room v0.7)**：
```
聽著，會嘔吐的東西。 如果你想跟我族 VUX 的成員談，
又不想讓他們感到噁心，
不如去 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） 找澤克斯上將吧。
他（噁——！）（urp!） 喜歡人類。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×1 / 之×2 / 吾等×1 / 爾等×1

**你的選擇**：`GENERAL_INFO_HOSTILE_1=A`（shipped）/ `GENERAL_INFO_HOSTILE_1=B`（v3）/ `GENERAL_INFO_HOSTILE_1=C自訂:...`

---

### #85 · `GENERAL_INFO_HOSTILE_2` · 🟠 rewording · sim=0.476; 文言助詞清除=5

**英文原文**：
```
Look at those yellowish-white hard things in your mouth!
How do you keep from biting off that pulpy organ... Gross!
```

**Shipped v0.5.1**：
```
看看爾等嘴裡那些黃白色之堅硬物！
爾等如何避免咬斷那條軟糊糊的器官……真噁！
```

**Rebuild v3 (clean-room v0.7)**：
```
看看你嘴巴裡那些黃黃白白的堅硬東西！
你到底是怎麼做到不把那團肉呼呼的器官咬斷的…… 噁心！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×2 / 之×1 / 爾等×2

**你的選擇**：`GENERAL_INFO_HOSTILE_2=A`（shipped）/ `GENERAL_INFO_HOSTILE_2=B`（v3）/ `GENERAL_INFO_HOSTILE_2=C自訂:...`

---

### #86 · `GENERAL_INFO_HOSTILE_3` · 🟠 rewording · sim=0.636; 文言助詞清除=2

**英文原文**：
```
Yuck! Don't show your tongue like that. It makes me sick.
```

**Shipped v0.5.1**：
```
噁！ 別那樣秀出爾等的舌頭。 使本官反胃。
```

**Rebuild v3 (clean-room v0.7)**：
```
噁心！ 不要那樣露出你的舌頭。 讓我覺得反胃。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×1 / 爾等×1

**你的選擇**：`GENERAL_INFO_HOSTILE_3=A`（shipped）/ `GENERAL_INFO_HOSTILE_3=B`（v3）/ `GENERAL_INFO_HOSTILE_3=C自訂:...`

---

### #87 · `GENERAL_INFO_HOSTILE_4` · 🟠 rewording · sim=0.775; 文言助詞清除=6

**英文原文**：
```
Forget it, human. We can't think straight when we have to look at you.
If you're lonely, go to <% comm.getStarName("Alpha Cerenkov", "maidens") %> and talk with that pervert, Admiral ZEX.
```

**Shipped v0.5.1**：
```
算了吧，人類。 看著爾等吾等無法思考。
若爾等寂寞，去 <% comm.getStarName("契倫科夫α", "maidens") %> 找那個變態，澤克斯上將，跟他聊聊。
```

**Rebuild v3 (clean-room v0.7)**：
```
算了吧，人類。 我族 VUX 一看到你就沒辦法好好思考。
你要是覺得寂寞，就去 <% comm.getStarName("契倫科夫α", "maidens") %> 找那個變態—— 澤克斯上將—— 聊天吧。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×2 / 吾等×1 / 爾等×2

**你的選擇**：`GENERAL_INFO_HOSTILE_4=A`（shipped）/ `GENERAL_INFO_HOSTILE_4=B`（v3）/ `GENERAL_INFO_HOSTILE_4=C自訂:...`

---

### #88 · `cant_we_be_friends_1` · 🟠 rewording · sim=0.757; 文言助詞清除=0

**英文原文**：
```
Why can't we be friends? I like YOU.
```

**Shipped v0.5.1**：
```
為何我方不能當朋友？ 我方喜歡你。
```

**Rebuild v3 (clean-room v0.7)**：
```
為什麼我們不能當朋友？ 我喜歡「你們」。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`cant_we_be_friends_1=A`（shipped）/ `cant_we_be_friends_1=B`（v3）/ `cant_we_be_friends_1=C自訂:...`

---

### #89 · `NEVER_UGLY_HUMANS_1` · 🟠 rewording · sim=0.516; 文言助詞清除=8

**英文原文**：
```
I listened. I heard. I know you like ME.
But the problem is, I DESPISE you!
Which is why I am attacking, in case you were wondering.
```

**Shipped v0.5.1**：
```
本官聽了。 本官聽見了。 本官知道爾等喜歡本官。
但問題是，本官鄙視爾等！
順帶一提，這就是本官為何正在攻擊爾等，若爾等好奇的話。
```

**Rebuild v3 (clean-room v0.7)**：
```
我聽了。 我聽清楚了。 我知道你喜歡「我」。
但問題是，我「鄙視」你！
你要是還在納悶，這就是我為什麼要攻擊你的原因。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×4 / 爾等×4

**你的選擇**：`NEVER_UGLY_HUMANS_1=A`（shipped）/ `NEVER_UGLY_HUMANS_1=B`（v3）/ `NEVER_UGLY_HUMANS_1=C自訂:...`

---

### #90 · `cant_we_be_friends_2` · 🟠 rewording · sim=0.564; 文言助詞清除=0

**英文原文**：
```
We have too much to gain through cooperation. Just try.
```

**Shipped v0.5.1**：
```
我方能經由合作獲得太多。 就試試看吧。
```

**Rebuild v3 (clean-room v0.7)**：
```
合作能讓我方得到太多好處了。 試試看嘛。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`cant_we_be_friends_2=A`（shipped）/ `cant_we_be_friends_2=B`（v3）/ `cant_we_be_friends_2=C自訂:...`

---

### #91 · `NEVER_UGLY_HUMANS_2` · 🟠 rewording · sim=0.575; 文言助詞清除=8

**英文原文**：
```
Okay, I'll try to like you.
I'm really trying.
Naw! This is never going to work.
Every time I try to think of your friendly smiling face
(urp!) I want to blow chunks.
I have a better idea. I'll just kill you.
```

**Shipped v0.5.1**：
```
好，本官試試喜歡爾等。
本官真的在努力。
不行！ 這永遠行不通。
每當本官想到爾等友善之笑臉
（呃啊！）本官就想大吐特吐。
本官有個更好之主意。 直接殺了爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
好啦，我試著喜歡你。
我真的很努力在試。
不行！ 這永遠行不通。
每次我想試著想像你那張友善的笑臉，
（噁——！）（urp!） 我就想吐得亂七八糟。
我有個更好的主意。 我還是把你宰了吧。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×3 / 之×2 / 爾等×3

**你的選擇**：`NEVER_UGLY_HUMANS_2=A`（shipped）/ `NEVER_UGLY_HUMANS_2=B`（v3）/ `NEVER_UGLY_HUMANS_2=C自訂:...`

---

### #92 · `cant_we_be_friends_3` · 🟠 rewording · sim=0.684; 文言助詞清除=0

**英文原文**：
```
Didn't anyone ever tell you, `you can't judge a book by its cover?'
```

**Shipped v0.5.1**：
```
沒人告訴過你嗎？「不要以貌取人」？
```

**Rebuild v3 (clean-room v0.7)**：
```
難道沒人告訴過你們—— 「別以貌取人」嗎？
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`cant_we_be_friends_3=A`（shipped）/ `cant_we_be_friends_3=B`（v3）/ `cant_we_be_friends_3=C自訂:...`

---

### #93 · `NEVER_UGLY_HUMANS_3` · 🟠 rewording · sim=0.561; 文言助詞清除=15

**英文原文**：
```
Do you want to know how ugly you are to us VUX? I'll tell you.
You humans are SO ugly, that I get my kids to behave by holding a picture of you behind my back
and I tell the kids that if they aren't good, I'll show it to them!
I am such a bad father (sob!) I must destroy you... for the children!
```

**Shipped v0.5.1**：
```
爾等想知道爾等對吾等 VUX 有多醜嗎？ 本官告訴爾等。
爾等人類醜到本官要小孩守規矩就把一張爾等之照片藏在背後
本官告訴小孩若他們不乖，本官就把它拿出來給他們看！
本官真是個糟糕父親（嗚嗚！）本官必須毀滅爾等……為了孩子們！
```

**Rebuild v3 (clean-room v0.7)**：
```
你想知道你對我族 VUX 而言有多醜嗎？ 我告訴你。
你們人類醜成這樣—— 我在家管小孩都是這樣：手裡藏一張你們的照片在背後，
跟小孩說：「你們不乖，我就把照片拿出來給你們看！」
我真是個爛老爸（嗚——！）（sob!） 我必須毀滅你們…… 為了孩子們！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×1 / 爾×6 / 之×1 / 吾等×1 / 爾等×6

**你的選擇**：`NEVER_UGLY_HUMANS_3=A`（shipped）/ `NEVER_UGLY_HUMANS_3=B`（v3）/ `NEVER_UGLY_HUMANS_3=C自訂:...`

---

### #94 · `cant_we_be_friends_4` · 🟡 micro-adjust (equivalent) · sim=0.875; 文言助詞清除=0

**英文原文**：
```
You are just a bunch of bigots. I thought you were better than that.
```

**Shipped v0.5.1**：
```
你們就是一群偏執狂。 我還以為你們比這個更好。
```

**Rebuild v3 (clean-room v0.7)**：
```
你們就只是一群偏執狂。 我還以為你們比這樣好一點。
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`cant_we_be_friends_4=A`（shipped）/ `cant_we_be_friends_4=B`（v3）/ `cant_we_be_friends_4=C自訂:...`

---

### #95 · `NEVER_UGLY_HUMANS_4` · 🟠 rewording · sim=0.434; 文言助詞清除=9

**英文原文**：
```
This IS embarrassing. We pride ourselves on being rational!
But you are so disgusting that we feel we just HAVE to kill you!
Like right now!
```

**Shipped v0.5.1**：
```
這真是難堪。 吾等自豪為講理之族類！
但爾等如此噁心，吾等覺得就是「必須」殺了爾等！
就像現在！
```

**Rebuild v3 (clean-room v0.7)**：
```
這確實有點難堪。 我族 VUX 一向自詡理性！
但你們實在太噁心了，我族 VUX 覺得非殺你們不可！
就像現在這樣！
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 之×1 / 吾等×2 / 爾等×2

**你的選擇**：`NEVER_UGLY_HUMANS_4=A`（shipped）/ `NEVER_UGLY_HUMANS_4=B`（v3）/ `NEVER_UGLY_HUMANS_4=C自訂:...`

---

### #96 · `bye_hostile_space` · 🟠 rewording · sim=0.625; 文言助詞清除=0

**英文原文**：
```
Well, THIS has been useless. Goodbye.
```

**Shipped v0.5.1**：
```
呃，這對話毫無意義。 再見。
```

**Rebuild v3 (clean-room v0.7)**：
```
好吧，這次談話「毫無用處」。 再見。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 無

**你的選擇**：`bye_hostile_space=A`（shipped）/ `bye_hostile_space=B`（v3）/ `bye_hostile_space=C自訂:...`

---

### #97 · `GOODBYE_AND_DIE_HOSTILE_SPACE_1` · 🟠 rewording · sim=0.404; 文言助詞清除=10

**英文原文**：
```
Human, based upon our commitment to the Ur-Quan
and your general disgusting demeanor, we have decided to blow you to bits.
```

**Shipped v0.5.1**：
```
人類，基於吾等對烏寬之承諾
以及爾等一般令人反胃之舉止，吾等已決定將爾等炸成碎片。
```

**Rebuild v3 (clean-room v0.7)**：
```
人類，基於我族 VUX 對烏寬的承諾，
再加上你們那副噁心的德性，我族 VUX 決定—— 把你們炸成碎片。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 之×2 / 吾等×2 / 爾等×2

**你的選擇**：`GOODBYE_AND_DIE_HOSTILE_SPACE_1=A`（shipped）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_1=B`（v3）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_1=C自訂:...`

---

### #98 · `GOODBYE_AND_DIE_HOSTILE_SPACE_2` · 🟡 micro-adjust (equivalent) · sim=0.850; 文言助詞清除=0

**英文原文**：
```
Wait! I have one last thing to say
Die!
```

**Shipped v0.5.1**：
```
等等！ 本官還有最後一句話要說
去死吧！
```

**Rebuild v3 (clean-room v0.7)**：
```
等等！ 我還有最後一句話要說——
去死！
```

**推薦**：B (v3) — 兩版接近，但 v3 微調更符 dossier；可選 A (shipped) 保留熟悉感

**說明**：shipped 含文言污染: 無

**你的選擇**：`GOODBYE_AND_DIE_HOSTILE_SPACE_2=A`（shipped）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_2=B`（v3）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_2=C自訂:...`

---

### #99 · `GOODBYE_AND_DIE_HOSTILE_SPACE_3` · 🟠 rewording · sim=0.375; 文言助詞清除=4

**英文原文**：
```
For the good of the whole, I will now erase your putrid presence.
```

**Shipped v0.5.1**：
```
為了整體之利益，本官將現在抹除爾等腐臭之存在。
```

**Rebuild v3 (clean-room v0.7)**：
```
為了全體的福祉，我現在就把你們那腐爛的存在給抹除。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 爾×1 / 之×2 / 爾等×1

**你的選擇**：`GOODBYE_AND_DIE_HOSTILE_SPACE_3=A`（shipped）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_3=B`（v3）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_3=C自訂:...`

---

### #100 · `GOODBYE_AND_DIE_HOSTILE_SPACE_4` · 🟠 rewording · sim=0.375; 文言助詞清除=8

**英文原文**：
```
We have no choice. You are too wretched. We shall eliminate you.
```

**Shipped v0.5.1**：
```
吾等別無選擇。 爾等太過悲慘。 吾等將消滅爾等。
```

**Rebuild v3 (clean-room v0.7)**：
```
我族 VUX 沒有選擇。 你們太悲慘、太可鄙了。 我族 VUX 必須把你們消滅。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 吾×2 / 爾×2 / 吾等×2 / 爾等×2

**你的選擇**：`GOODBYE_AND_DIE_HOSTILE_SPACE_4=A`（shipped）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_4=B`（v3）/ `GOODBYE_AND_DIE_HOSTILE_SPACE_4=C自訂:...`

---

### #101 · `OUT_TAKES` · 🟠 rewording · sim=0.716; 文言助詞清除=2

**英文原文**：
```
Oh no! It's one of those ultra-gross humans again!
Quick, hide your eye!
AGGH! Look at the pulpy red thing in its mouth
how it wriggles and writhes like a wet blood worm
and plays over the hard white nubs that protrude from its headbone!
I think I'm going to be sick.
```

**Shipped v0.5.1**：
```
噢不！ 又是那些超級噁心的人類之一！
快點，遮住你的眼睛！
噁啊！（AGGH!） 看看牠嘴裡那軟糊糊的紅東西
牠如何像條濕漉漉的血蟲一樣扭動蠕動
還在那些從牠頭骨突出之堅硬的白色小凸起上上下滾動！
本官覺得本官要吐了。
```

**Rebuild v3 (clean-room v0.7)**：
```
喔不！ 又是那些超級噁心的人類！
快點，把眼睛藏起來！
噁——！（AGGH!） 看看牠嘴裡那團軟糊糊的紅東西——
它扭來扭去、蠕動個不停，就像濕漉漉的血蟲，
還在那頭骨突出的堅硬白色小凸起上滑來滑去！
我覺得我要吐了。
```

**推薦**：B (v3) — v3 已清除文言污染 + 符合 dossier v0.7 canonical，建議採用

**說明**：shipped 含文言污染: 之×2

**你的選擇**：`OUT_TAKES=A`（shipped）/ `OUT_TAKES=B`（v3）/ `OUT_TAKES=C自訂:...`

---

## 批次快答格式建議

```
🟠 全依推薦（=全 B）
🔴 逐項挑（列出各 token 選擇）
🟡 全 A（保留 shipped）或全 B（採 v3）
特殊自訂: TOKEN_NAME=C[自訂內容]
```

**Rebuild-Compare 執行者**：GitHub Copilot（Claude Opus 4.7）
**執行日期**：2026-08-16