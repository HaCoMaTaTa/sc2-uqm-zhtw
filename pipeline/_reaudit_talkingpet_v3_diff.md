# Dnyarri Rebuild-Compare Diff Report (2026-08-16 · v0.7 v3 clean-room)

**族**：`talkingpet` (Dnyarri / Talking Pet · 雙重人格族 · 4 sub-modes)
**檔案**：`uqm-work/translations/talkingpet.zh-TW.json` (shipped v0.6, 112 tokens)
**v3**：`uqm-work/translations/talkingpet.zh-TW.v3.json` (clean-room · Dossier v0.7 A 案 純現代黑色 villain + `-<CAPS>-` 心控括號 icon + 4 sub-modes)
**規模**：112 tokens · shipped 29,961 bytes · v3 39,286 bytes
**3-gate**：purity=0 · Lua=0 · line-count=112/112 ✅

---

## 統計

| 類別 | 數量 | 占比 |
|---|---|---|
| 🟢 完全相同 | 3 | 3% |
| 🟡 微調（等價 · 標點/語氣） | 46 | 41% |
| 🟠 措辭改變（去文言污染 + dossier icon 採用） | 61 | 54% |
| 🔴 語意/voice 差異大 | 0 | 0% |
| ✨ v0.7 canonical 升級 | 2 | 2% |

**污染統計對照**：

| 項目 | shipped | v3 | 削減 |
|---|---|---|---|
| 吾 | 36 | 0 | -100% |
| 爾 | 71 | 0 | -100% |
| 吾等 | 16 | 0 | -100% |
| 之（純文言助詞）| 26 | 2 | -92% |
| **──合計文言助詞──** | **149** | **2** | **-99%** |

**canonical 保留**（未新增，皆繼承 shipped）：
蟾亞（族）/ 會話寵 / 烏寬 / 陰嘎（族）/ 塔洛（族）/ 塔洛盾 / 塔洛裝置 / 阿麗露 / 感知聯盟 / 薩瑪特拉 / 無畏艦 / 先驅者 / 智能閹割 / 奴役襲擊艦 / 苦刑器 / 尤普塔 / 柯亞（族）/ 憂特（族）

**新採用 canonical**（dossier §四 / Master_Glossary v0.7）：
- **本尊**（Mode 2/3/4 覺醒古老形態自我尊稱 · dossier §4.2 canonical · 廢除舊「吾等」/「小的」）
- **-<...>-**（心控括號 icon · dossier §4.2 招牌 · shipped 已有 15 處可繼承，v3 系統化 100% 保留）
- **猴子小子**（monkey-boy · dossier canonical · shipped 已有 4 處 · v3 EXPLAIN_NOTHING_MONKEY_BOY 全用）
- **骨軟叭嘰的馬屁蟲**（boneless (toady) dweeb · dossier §4.2 canonical · 兩處統一 Q5=A）
- **莫札特（Mozart）/ 伊基流行（Iggy Pop）**（保留原文名字 · dossier §4.3 canonical · shipped 已用可繼承）
- **本鐵佛克（Benteflork）**（Master_Glossary v0.5 canonical · ABOUT_HISTORY 首介英文）
- **阿麗露（Ariloulaleelay）**（Master_Glossary canonical · JUST_TALKING_PET 首介全稱英文）
- **渥啟基（Watchuki）少尉**（tentative NPC 名 · GENERAL_INFO_ONBOARD_2 首介英文 · **⚠️ 需使用者確認**）
- **霍利黛（Holiday）少尉**（沿用 shipped canonical · GENERAL_INFO_ONBOARD_2）

**Q&A 決策應用**（10 題全 A）：
- Q1=A `-<CAPS>-` 純括號 + 單感嘆號（無 markdown `**` · 感嘆號本身即強調）
- Q2=A Mode 1 用「我」/ Mode 2-4 用「本尊」（4 modes voice 明顯區別）
- Q3=A 心控 robotic 玩家台詞保留 dash `-` + CJK 全形空格（want_kill_2 / yes_flowers / wish_to_go_now）
- Q4 全 A 感嘆詞（YARRGH=呀啊！/ Argh=啊嘖！/ Aieee=哎呀！/ Bummer=真掃興 / Ha-ha-ha=哈-哈-哈！/ Heh-heh=嘿嘿 / Ouchy-oochy=唉喲喂啊 / Woof woof=汪汪！/ sner-Gee=呼──嘰──/ *sigh*=＊嘆氣＊ / Feh=呸！/ Hmph=哼。 / Boy=唉呦 / Hmmm=嗯？）
- Q5=A `boneless (toady) dweeb` 兩處統一「骨軟叭嘰的馬屁蟲」
- Q6 全 A 特殊詞（zombie-blobbies=殭屍膠團 / 又硬又突出的感應器官 / 濕黏的肉塊在四周脈動 / 智能閹割 / 黑暗且充滿敵意之地 / 外星噪音製造機 / 奴役襲擊艦 / 迫降 / 薩瑪特拉的護盾已消失）
- Q7=A Mode 4 假甦醒 gag：「謝謝你！」連呼 5 次半 + 破折號「謝謝——」打斷 + 破功 canonical
- Q8=A Hierarchy 情境化混用（玩家莊嚴用「烏寬戰奴階層」/ villain 短稱用「戰奴階層/階層」）
- Q9=A 特殊 tokens（HYPNO_TAIL 單空格保留 / SUGGESTION_7=8 相同 / Master of Universe 打斷「本尊…… 是…… 宇宙至——」）
- Q10=A 分批 4 partial × 28 tokens

---

## 🟢 完全相同（3 tokens · 不列細節）

`HYPNO_TAIL` · `what_now` · `enough_info`

---

## ✨ canonical 升級（2 tokens）

### #3 · `JUST_TALKING_PET` · ✨

**EN**：
```
I am, uh, a peaceful creature, a friendly alien life form. The Ur-Quan call us `talking pets'.
Until recently, I was employed on a Dreadnought starship as a translator.
Then, after the ship suffered severe damage in combat, we crashed at <% comm.getStarName("Alpha Pavonis", "urquan wreck") %>.
Miraculously, I survived, and was rescued by an Ariloulaleelay exploration vessel.
The Arilou, they could not heal my most severe injuries, so they brought me to the Umgah
who possess superior bio-engineering skills.
```
**Shipped**：
```
小的呀，呃，是個和平的生物，友善的外星生命體。 烏寬稱吾輩為『會話寵』。
不久前，小的還在一艘無畏艦星艦上擔任譯者。
然後，該艦在戰鬥中嚴重受損，我們墜毀於 <% comm.getStarName("孔雀座α", "urquan wreck") %> （Alpha Pavonis）。
奇蹟般地，小的倖存下來，被一艘阿麗露探索艦救起。
阿麗露無法治好小的最嚴重的傷勢，所以他們將小的送至陰嘎族
他們擁有卓越的生物工程技術。
```
**v3**：
```
我，呃，是一種和平的生物、友善的外星生命體。 烏寬把我們叫做「會話寵」。
直到最近，我還在一艘無畏艦上擔任翻譯員。
後來那艘艦在戰鬥中受到嚴重損傷，我們墜毀在 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）。
奇蹟似地，我活了下來，被一艘阿麗露（Ariloulaleelay）探索艦救起。
阿麗露沒辦法治好我最嚴重的傷勢，於是他們把我送到陰嘎族那裡——
他們擁有更高超的生物工程技術。
```
**推薦**：**B (v3)** — v3 採用新 canonical (Master_Glossary v0.7 / dossier v0.7)
**選擇**：A / B / C（自訂）

### #32 · `POOR_DNYARRI` · ✨

**EN**：
```
I will gladly tell you my story, Captain. Gladly!
I was indeed a Talking Pet aboard an Ur-Quan Dreadnought.
Those years are like a forgotten dream to me, because I was not sentient.
I was a dumb beast -- an unthinking slave to the heinous Ur-Quan!
Then there was a great battle... the ship was hit and severely damaged.
Slaves running down the corridors! Commands, counter-commands!
Then there was the scream of atmosphere ouside the hull.
There was a big explosion of light and thunder! We hit the surface of a planet, I'm pretty sure.
The next thing I can remember was the face of a creature you call the Arilou.
I was in great pain, but the creature was kind. It did what it could for me
by applying its own medicines to my alien form. I was transported off-planet.
I remember an all-pervading green light -- then we were at the homeworld of the Arilou.
Again, Captain, forgive me if I am not more clear, but I was not intelligent yet.  Give me a chance.
I presume my injuries were too severe for the Arilou to repair
or perhaps I reacted badly to their medicines or something,
because the next thing I remember was being moved back into a ship.
Things grow dim, my next memory was being on board an Umgah starship
Wet flesh throbbing all around me, the Umgah laughing as they worked on my body.
It was kind of unnerving.
Suddenly, like the explosion of a bomb, thought -- I mean REAL thought -- flooded my brain!
I don't know how or why, but the Umgah had discovered that my brain could be easily changed, improved to give me true intelligence!
What they didn't realize is that it also brought back a flood of memories.
Memories of my species' ancient past! From before the time the Ur-Quan castrated our thinking minds
and transformed my people into crude beasts.
I am the only intelligent Dnyarri left in this galaxy, Captain.
Now do you understand my lust for vengeance?
```
**Shipped**：
```
本座樂意告訴你本座的故事，艦長。 樂意之至！
本座確實曾是一隻烏寬無畏艦上的會話寵。
那些年對本座而言如遺忘的夢境，因為本座當時尚無感知能力。
本座是隻笨獸 —— 一個為那可惡烏寬服役的無心智奴隸！
然後有一場大戰…… 那艘船遭到擊中，嚴重損毀。
奴隸奔逃於走廊間！ 指令、反指令！
然後是艦體外大氣的尖嘯。
然後是一陣巨大的光與雷之爆炸！ 本座頗確定我們撞上了一顆行星的表面。
本座接下來能記得的是一張你們稱作阿麗露的生物的臉。
本座當時痛苦萬分，但那生物很仁慈。 它盡其所能對本座施用自身的醫療品
施於本座之異形之軀。 本座被運離了那顆行星。
本座記得一片瀰漫的綠光 —— 然後我們就到了阿麗露的家園。
再一次，艦長，若本座無法更清楚地描述請諒解，因為本座當時尚無智能。 請給本座一個機會。
本座猜想本座的傷勢對阿麗露而言太過嚴重無法修復
或者本座對他們的醫療品有不良反應之類的，
因為本座下一件記得的事是又被移回了一艘艦艇。
事情有點模糊了，本座下一段記憶是身處一艘陰嘎星艦上
濕潤的肉在本座周圍脈動，陰嘎族一邊在本座身上動手一邊笑。
那頗令人不安。
忽然間，如同炸彈爆炸般，思想 —— 本座指的是**真正的**思想 —— 湧入本座的腦海！
本座不知何以，但陰嘎族發現本座的腦部可被輕易地改變，使本座獲得真正的智能！
他們未曾意識到的是，這也帶回了洪水般的記憶。
本族遠古的記憶！ 從烏寬閹割吾等思想之心智之前
將吾族改造成粗鄙野獸之前的記憶。
本座是這銀河中僅存的清醒蟾亞，艦長。
如今爾可明白本座復仇之慾？
```
**v3**：
```
本尊很樂意告訴你本尊的故事，艦長。 樂意極了！
本尊確實曾經是烏寬無畏艦上的一隻會話寵。
那些年對本尊來說就像被遺忘的夢——因為當時本尊沒有智能。
本尊只是一頭蠢獸——一個沒有思想的奴隸，為邪惡的烏寬服役！
然後發生了一場大戰……那艘艦被擊中，嚴重損毀。
奴隸在走廊上四散奔逃！ 命令、反命令交錯！
然後外殼外的大氣開始尖嘯。
轟然一道光與雷的大爆炸！ 本尊很確定，我們撞上了某顆行星的表面。
本尊接下來記得的，是一張你們稱為阿麗露的生物的臉。
本尊當時痛得要命，但那個生物很仁慈。 它盡其所能——
用它自己的藥物治療本尊的外星身體。 本尊被送離那顆星球。
本尊記得一片瀰漫的綠光——然後我們就到了阿麗露的母星。
再說一次，艦長，如果本尊講得不夠清楚請原諒——因為本尊當時還沒有智能。 給本尊一個機會嘛。
本尊猜想本尊的傷勢對阿麗露來說太嚴重、沒辦法修復——
或者本尊對他們的藥物有不良反應之類的——
因為本尊接下來記得的，是又被搬上了一艘船。
事情變得朦朧，本尊下一段記憶是自己在陰嘎星艦上——
濕黏的肉塊在本尊四周脈動、陰嘎族在旁邊一邊笑一邊擺弄本尊的身體。
那感覺實在挺不舒服的。
然後突然間，像炸彈爆炸一樣，思想——本尊指真正的思想——湧入本尊的腦袋！
本尊不知道是怎麼發生的、為什麼，但陰嘎族發現本尊的大腦可以輕易被改造、被改良，賦予本尊真正的智能！
他們沒意識到的是——這也帶回了大量的記憶。
本尊族群遠古歷史的記憶！ 從烏寬把我族思考的心靈智能閹割掉之前——
把本尊的族人變成粗劣蠢獸之前的記憶。
本尊是這個銀河裡最後一個有智能的蟾亞，艦長。
現在你懂本尊為什麼渴望復仇了嗎？
```
**推薦**：**B (v3)** — v3 採用新 canonical (Master_Glossary v0.7 / dossier v0.7)
**選擇**：A / B / C（自訂）

---

## 🟠 措辭改變（61 tokens）

### #5 · `OH_NO_YOU_DONT` · 🟠

**EN**：
```
Oh... you know about that, do you?
Oh well, I guess that means I will have to kill you now.
I can't permit you to reveal my transformation
the Ur-Quan might find out, and then my plans for revenge will be ruined.
Well, I tried to spare your life, Captain, but you were just too curious
so now:
-<SEEK DEATH AT THE HANDS OF YOUR ENEMY!>-
```
**Shipped**：
```
喔…… 爾知道啦？
唉，那本座只好殺爾了。
本座不容爾洩漏本座之覺醒
烏寬若得知，本座的復仇大計便毀了。
唉，本座已試著饒爾一命，艦長，可爾實在太好奇
那如今：
-<去尋死於敵人之手！>-
```
**v3**：
```
喔……原來你知道啊，是吧？
好吧，那看來我得現在把你殺了了。
我不能讓你揭露我的轉變——
烏寬要是發現，本尊的復仇大計就毀了。
唉，本尊本來想放你一條生路的，艦長，但你就是太好奇了——
所以現在：
-<去死在敵人手裡吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #9 · `WORKS_LIKE_THIS` · 🟠

**EN**：
```
Argh! Why didn't you leave when you had the chance?
Now I've got to kill you in some really sneaky way
so that no one will guess I was the agent of your demise. *sigh*
-<GET LOST IN A BAD NEIGHBORHOOD!>-
```
**Shipped**：
```
啊！ 爾為何不在還有機會的時候離開？
如今本座只好用某種特別狡猾的方式殺爾
這樣就沒人會猜到本座是爾殞命的元兇。 （嘆氣）
-<迷失於險惡之地！>-
```
**v3**：
```
啊嘖！（Argh!） 有機會的時候你怎麼不走人呢？
現在本尊只好用某種真的很陰險的方式殺你——
這樣才沒人會猜到是本尊搞掉你的。 ＊嘆氣＊
-<在爛街區裡迷路吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #11 · `GOOD_FOR_YOU` · 🟠

**EN**：
```
Good idea! May I just say, I am behind you 100 percent!
But unfortunately, the Umgah are all too busy to come to the HyperWave 'Caster right now
so... er... come back later... much later.
```
**Shipped**：
```
好主意！ 容小的說一句，小的**百分之百**支持爾！
可惜陰嘎族現在全都太忙，無法過來超波廣播器
所以…… 呃…… 之後再來吧…… 很久很久之後。
```
**v3**：
```
好主意！ 容我表態，我可是百分之百支持你的！
不過很遺憾，陰嘎族現在全都忙得沒空過來超波播送器這邊——
所以……呃……晚點再來吧……很晚再來。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #13 · `EXPLAIN_NOTHING_MONKEY_BOY` · 🟠

**EN**：
```
YARRGH! I will explain NOTHING, monkey-boy!
Your stupid curiosity has sealed your doom!
You could have left well enough alone. You could have departed this planet alive
but NO!
I am afraid you have stuck your stiff, protruberant sensing organ into one too many dark holes, Captain,
and now you shall pay the price!
-<GO GET YOURSELF KILLED!>-
```
**Shipped**：
```
呀啊嗯！ 本座**啥都不會**解釋，猿猴子！
爾愚蠢的好奇心已封定爾的下場！
爾原本可以放過此事的。 爾原本可以活著離開此星球
可**偏偏不要**！
本座擔心爾把爾那僵硬突出的感應器官塞進太多黑洞了，艦長，
如今爾必須付出代價！
-<讓自己去送死！>-
```
**v3**：
```
呀啊！（YARRGH!） 本尊什麼都不會解釋，猴子小子！
你那愚蠢的好奇心已經葬送了你！
你原本可以放著不管的。 你原本可以活著離開這顆星球——
但是不行！
恐怕你已經把你那又硬又突出的感應器官伸進太多暗洞裡了，艦長——
現在你要付出代價！
-<去把自己搞死吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #15 · `GOODBYE_AT_UMGAH` · 🟠

**EN**：
```
Oh, I wish it were so simple.
I thought that perhaps I could let you live
but now I fear you know too much.
My plans for revenge are far too important
to be be ruined by a simple, interfering dolt like yourself.
-<GO KILL YOURSELF IN BATTLE!>-
```
**Shipped**：
```
喔，本座真希望有那麼簡單。
本座本以為或許可以讓爾活著
可如今本座擔心爾知道得太多。
本座的復仇大計太過重要
不容一個像爾這樣簡單、多管閒事的呆瓜毀了。
-<在戰鬥中送死去吧！>-
```
**v3**：
```
喔，本尊真希望有那麼簡單。
本尊本來以為，或許可以讓你活著——
但現在恐怕你知道得太多了。
本尊的復仇大計太過重要——
可不能被你這種頭腦簡單、又愛管閒事的笨蛋給毀了。
-<在戰鬥中把自己幹掉吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #16 · `HYPNOTIZE_AGAIN_1` · 🟠

**EN**：
```
Argh! Why aren't you dead? Oh, what a bummer.
I will remedy this situation
-<FIND SOMEONE WHO WILL KILL YOU!>-
```
**Shipped**：
```
啊！ 爾怎麼還沒死？ 喔，真煩。
本座來把這狀況矯正一下
-<尋一人願殺爾者！>-
```
**v3**：
```
啊嘖！（Argh!） 你怎麼還沒死？ 喔，真掃興。
本尊來修正這個狀況。
-<去找個人來殺了你吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #17 · `HYPNOTIZE_AGAIN_2` · 🟠

**EN**：
```
Argh! You are interfering with my plans of revenge against the Ur-Quan.
The penalty for this transgression is death. Specifically, yours!
-<NOW GO AWAY AND PICK A FIGHT!>-
```
**Shipped**：
```
啊！ 爾正在干擾本座對烏寬的復仇大計。
此罪之罰即死。 具體來說，爾之死！
-<即刻離去挑起爭端！>-
```
**v3**：
```
啊嘖！（Argh!） 你正在妨礙本尊對烏寬的復仇大計。
這種越界舉動的懲罰是死。 具體來說——是你的死！
-<馬上滾去找架打吧！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #18 · `HYPNOTIZE_AGAIN_3` · 🟠

**EN**：
```
Why do you keep returning!? Never mind, don't answer.
-<LEAVE AND FIND SOMEONE WHO WILL KILL YOU!>-
```
**Shipped**：
```
爾為何總是回來！？ 算了，別回答。
-<離去尋一人願殺爾者！>-
```
**v3**：
```
你怎麼一直回來啊！？ 算了，別回答。
-<滾遠一點去找人殺了你！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #19 · `HYPNOTIZE_AGAIN_4` · 🟠

**EN**：
```
You're back again!?
You are as durable as you are stupid!
Perhaps this time, you will accomplish your own demise.
-<GO KILL YOURSELF!>-
```
**Shipped**：
```
爾又回來啦！？
爾與爾之愚蠢一樣耐命！
或許此番，爾能自行完成爾之死。
-<去自我了斷！>-
```
**v3**：
```
你又回來了！？
你有多耐命就有多蠢！
或許這一次，你會親手完成你自己的死亡。
-<去把自己幹掉！>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #21 · `CANT_COMPEL` · 🟠

**EN**：
```
Aieee!  I cannot compel you!?
Your mind is closed to me -- how can this be?!
I am forced to resort to... more primitive measures
Umgah commander, summon your ten combat ships and attack this intruder instantly!
```
**Shipped**：
```
啊咦！（Aieee!） 本座竟無法操控爾！？
爾之心對本座封閉 —— 這怎麼可能？！
本座被迫訴諸…… 更原始之手段
陰嘎指揮官，即刻召集爾的十艘戰艦攻擊此入侵者！
```
**v3**：
```
哎呀！（Aieee!） 本尊竟然無法控制你！？
你的心靈對本尊關閉——這怎麼可能？！
本尊只好被迫訴諸……更原始的手段——
陰嘎指揮官，召集你的十艘戰艦，立刻攻擊這個闖入者！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #22 · `LETS_MAKE_A_DEAL` · 🟠

**EN**：
```
Uh, hi there, friendly starship Captain!
You will never believe this, but somehow, the injuries I suffered when the Ur-Quan crashed
triggered some kind of, uh... personality transformation
I became evil and spiteful! Cruel and nasty! Whimsically unpleasant!
You may also have noticed that I gained some kind of `temporary psychic powers'
Well I just wanted to let you know... I AM CURED!
Captain, I don't know exactly how, but when you were fighting those Umgah ships
a chunk of the ceiling fell upon my head and gave me quite a whack!
Ouchy-oochy.. it still hurts!
When I awoke, the universe had ceased to be the dark and hostile place I previously thought it to be.
Instead, I was overwhelmed, yes, even awed by the beauty and perfection of it all!
I also discovered that I had completely lost those wicked mental powers
and could now look forward to a NEW LIFE, filled with happiness, butterflies, and goodwill for all!
Your job is done, Captain! You have saved me! Now you can safely remove your psychic protection device, and leave.
THANK YOU! THANK YOU! THANK YOU! THANK YOU! THAN
Why are you looking at me like that, Captain?
Don't you believe me? You question my word?
Okay, okay... so I was lying.
Big deal! So what.
Boy, are you A PAIN, do you know that?
WHAT DO YOU WANT FROM ME, MY LIFE!?
Oh, you do?  Hmph.
Well, as an alternative, let me make this little suggestion
if you don't kill me, I'll help you do whatever you wish.
Is it a deal, Captain? Hmmm? Hmmm?
```
**Shipped**：
```
呃，嗨啊，友善的星艦艦長！
你絕對不會相信，但不知怎的，本座在烏寬艦墜毀時受的傷勢
觸發了某種，呃…… 人格轉變
本座變得邪惡又惡毒！ 殘忍又惡劣！ 隨心所欲地令人不快！
你或許也注意到本座獲得了某種『暫時性的心靈能力』
這個嘛，本座只想告訴你…… **我痊癒了！**
艦長，本座不確切知道怎麼回事，但當你在跟那些陰嘎戰艦打鬥時
一塊天花板碎片掉下來砸中本座的頭，狠狠地敲了一下！
哎唷呢喃…… 現在還在痛！
當本座醒來時，宇宙已不再是本座先前所以為的那個黑暗、充滿敵意之處。
反之，本座被壓倒了，是的，甚至被這一切的美與完美所震撼！
本座還發現本座完全失去了那些邪惡的心靈能力
如今可以期待一個**新生活**，充滿快樂、蝴蝶、以及對眾生的善意！
你的工作完成了，艦長！ 你救了本座！ 如今你可以安全地移除你的心靈保護裝置，然後離開。
感謝你！ 感謝你！ 感謝你！ 感謝你！ 感謝
你為什麼那樣看著我，艦長？
你不相信我？ 你質疑我的話？
好吧，好吧…… 我承認我剛剛在撒謊。
大不了！ 沒什麼。
真是的，你**很難纏**，你知道嗎？
**你到底要我怎樣，要我的命嗎？！**
喔，你**要**啊？ 哼。
這樣好了，容我做個小小的建議
如果你不殺我，我就幫你做你想做的任何事。
這樣成交嗎，艦長？ 嗯？ 嗯？
```
**v3**：
```
呃，嗨，友善的星艦艦長！
你絕對不會相信，但不知怎的，本尊在烏寬艦墜毀時受的傷——
觸發了某種，呃……人格轉變——
本尊變得邪惡又惡毒！ 殘忍又下流！ 隨性地令人不快！
你可能也注意到，本尊獲得了某種「暫時性心靈能力」——
嗯，本尊只是想讓你知道……本尊已經痊癒了！
艦長，本尊不確定到底是怎麼回事，但你在打那些陰嘎戰艦的時候——
一塊天花板碎片砸到本尊頭上，狠狠敲了一下！
唉喲喂啊（Ouchy-oochy）……到現在還在痛！
本尊醒來後，這個宇宙不再是本尊過去以為的那種黑暗且充滿敵意的地方。
取而代之的是，本尊被整個宇宙的美與完美深深震撼——是的，甚至為此心生敬畏！
本尊還發現，那些邪惡的心靈力量已經完全消失——
現在本尊可以迎接嶄新的生活，充滿快樂、蝴蝶，以及對所有人的善意！
你的任務完成了，艦長！ 你救了本尊！ 現在你可以安全地移除你的心靈防護裝置，然後離開了。
謝謝你！ 謝謝你！ 謝謝你！ 謝謝你！ 謝謝——
艦長，你為什麼那樣看著本尊？
你不相信本尊？ 你質疑本尊的話？
好啦好啦……本尊剛剛是在說謊。
那又怎樣？ 沒什麼大不了的。
唉呦，你真是個難搞的傢伙，你知道嗎？
你到底想從本尊身上得到什麼，把本尊的命都拿走嗎？！
喔，你想那樣？ 哼。
好吧，作為替代方案，讓本尊提個小小的建議——
如果你不殺本尊，本尊就幫你做任何你想做的事。
這樣算是達成協議了嗎，艦長？ 嗯？ 嗯？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #24 · `HELP_DEFEAT_URQUAN` · 🟠

**EN**：
```
I get the basic idea: you want to overthrow the Ur-Quan
Bravo! Good idea! Way to go!
I too wish to see the Ur-Quan beaten -- humiliated, destroyed
and I alone possess the unique ability that will help you achieve your goal
I can use my psychic powers to temporarily distract the Ur-Quan... confuse them for a few seconds.
Presumably you will use this moment to strike a lethal blow against the Ur-Quan.
Such a plan cannot fail, Captain. We must see to that.
```
**Shipped**：
```
我抓到基本意思了：你想推翻烏寬
好樣的！ 好主意！ 說得對！
本座**同樣**希望看到烏寬被打敗 —— 蒙羞、被消滅
而**唯有本座**擁有能助你達成目標的獨特能力
本座可用心靈能力暫時分散烏寬的注意力…… 讓他們困惑幾秒鐘。
預料你會利用這一刻對烏寬發動致命一擊。
此計不可能失敗，艦長。 我們必須確保這點。
```
**v3**：
```
本尊懂大概意思：你想推翻烏寬——
好極了！ 好主意！ 就是這樣！
本尊也希望看到烏寬被擊敗——羞辱、毀滅——
而且能助你達成這目標的獨門能力，本尊獨有——
本尊可以用心靈力量暫時分散烏寬的注意力……讓他們困惑個幾秒。
想必你會利用那一刻，對烏寬給出致命一擊。
這樣的計畫不可能失敗，艦長。 我們必須確保它成功。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #26 · `COMING_ABOARD` · 🟠

**EN**：
```
No tricks, Captain. No tricks.
I fear you cruelly misjudge me. I am on YOUR side now.
Together we will make a great team, Captain.
This day, this MOMENT shall go down forever in the history of our galaxy.
I am coming aboard your ship now. I will make a nest in the pressurized section of your ship's hold.
When you wish to talk with me, I will be there.
```
**Shipped**：
```
沒有花招，艦長。 沒有花招。
本座擔心你嚴重誤判我了。 我現在站在**你這邊**。
我們合作將成為一支好隊伍，艦長。
今日，這一**瞬間**將永遠載入我們銀河的史冊。
本座這就登上你的艦艇。 我會在你船艙加壓區裡築個窩。
當你想與我談時，我就在那裡。
```
**v3**：
```
不會耍花招，艦長。 不會的。
本尊擔心你太殘忍地誤會了本尊。 本尊現在是站在你這邊的。
我們會是絕佳的組合，艦長。
今天，這一刻，將永遠載入我們銀河的歷史。
本尊現在就登艦。 本尊會在你艦艙加壓區的貨艙裡築個窩。
你想跟本尊說話的時候，本尊就會在那裡。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #28 · `TRUST` · 🟠

**EN**：
```
Captain, Captain... calm down. Be reasonable. Listen to me.
I am nothing more than a single being, hardly larger than one of your Earth dogs.  Woof woof!
My only weapon -- my weak psychic abilities -- have been nullified by your protective device.
I am harmless.
But perhaps, I can be of some small service to you.
Consider this my hopeful attempt to compensate you for all the trouble I have caused you in the past.
In the Past, Captain... and now we look to the future! To victory over the evil Ur-Quan!
I am your secret weapon against these tyrants, Captain. Do not leave me here.
```
**Shipped**：
```
艦長，艦長…… 冷靜。 講點道理。 聽本座說。
我不過是個小小的生命，不比你們地球狗大多少。 汪汪！
我唯一的武器 —— 本座那微弱的心靈能力 —— 已被你的保護裝置抑制。
我是無害的。
可或許，我能為你效些小勞。
就當這是本座希望能對你過去所受麻煩作出一點補償。
過去已成過去，艦長…… 如今我們展望未來！ 勝過那邪惡的烏寬！
本座是你對抗這些暴君的秘密武器，艦長。 別把本座留在此地。
```
**v3**：
```
艦長，艦長……冷靜點。 講點道理。 聽本尊說。
本尊不過就是個小生物，體型頂多跟一隻你們地球狗差不多大。 汪汪！（Woof woof!）
本尊唯一的武器——微弱的心靈能力——已經被你的防護裝置抵銷了。
本尊無害。
但或許，本尊還能為你效點小勞。
就當作本尊懷抱希望，想彌補過去給你造成的所有麻煩吧。
那是過去的事了，艦長……現在我們把目光放到未來！ 放到擊敗邪惡烏寬的勝利上！
本尊就是你對抗那些暴君的秘密武器，艦長。 別把本尊留在這裡。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #29 · `boneless_dweeb` · 🟠

**EN**：
```
I know what you are, evil creature. You are a lying, boneless dweeb!
```
**Shipped**：
```
我知道你是什麼，邪惡的生物。 你就是個撒謊的軟骨呆瓜！
```
**v3**：
```
我知道你是什麼，邪惡的生物。 你就是個滿口謊言、骨軟叭嘰的馬屁蟲！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #30 · `YOUR_BONELESS_DWEEB` · 🟠

**EN**：
```
Yes, Captain. I am a lying, boneless, toady dweeb
but I am YOUR lying, boneless, toady dweeb!
```
**Shipped**：
```
沒錯，艦長。 本座是個撒謊的、軟骨的、諂媚的呆瓜
可本座是**你的**撒謊軟骨諂媚呆瓜！
```
**v3**：
```
沒錯，艦長。 本尊就是個滿口謊言、骨軟叭嘰的馬屁蟲——
但本尊是你的滿口謊言、骨軟叭嘰的馬屁蟲！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #34 · `ITS_TRUE` · 🟠

**EN**：
```
It's all true, Captain! Every word!
Now listen!... and I shall tell you why the Ur-Quan did this to us.
It was over twenty thousand of your years ago, Captain, when an Ur-Quan slave raider
landed on the surface of my world, and began capturing my people -- killing those that would not submit!
How can I know this, you ask? These memories are embedded deep in my genetic structure, they cannot be forgotten.
How we fought the Ur-Quan! Even then, they had a Hierarchy of combat thralls
though then, they called themselves by the absurd name, the Sentient Milieu!
Ha! They were nothing more than thugs, especially those hideous Taalo.
Those evil rocklike creatures were the worst of all!
For fun, they would take one of our children... and then... roll over it!... again and again, oh!
The war against the Ur-Quan and their Milieu lasted decades... millions of our people died
but with the forces of truth and justice at our side, we were prevailing.
Then the Taalo made their fateful discovery... a shield against our only weapon, our weak psychic powers.
With that shield, they were unstoppable... we had lost.
But the Ur-Quan, they were not satisfied merely with our defeat, our slavery
they wanted MORE! They wanted to punish us for our insolence at fighting back against them
so they devised the sickest, most cruel and perverse punishment ever imagined!...
they invaded our very genetic structure
and hacked out enough of our minds to lobotomize us for all eternity.
And then we were made their closest servants... their `Talking Pets'.
This was our punishment.
```
**Shipped**：
```
全都是真的，艦長！ 每字每句！
如今聽好！…… 本座將告訴爾為何烏寬對吾等做出此事。
那是兩萬多年前，艦長，一艘烏寬奴役襲擊艦
登陸吾等世界的表面，開始擄捕吾族 —— 殺害不肯屈服者！
爾問本座怎能知曉此事？ 這些記憶深植於吾等的基因結構，永難忘懷。
吾族當時如何與烏寬奮戰！ 那時他們就已擁有戰奴階層
只不過那時他們自稱一個荒謬名字，感知聯盟！
哈！ 他們不過是群暴徒，尤其那些醜惡的塔洛族。
那些邪惡的岩石狀生物是最糟的！
為了娛樂，他們會抓吾等的一個孩子…… 然後…… 從其上輾過！…… 一次又一次，喔！
對抗烏寬與其感知聯盟的戰爭持續了數十年…… 吾族數百萬人死去
但真理與正義站在吾族這邊，吾族本佔上風。
然後塔洛族做出了他們宿命性的發現…… 一種可抵擋吾等唯一武器 —— 吾等微弱心靈能力 —— 的護盾。
有了那護盾，他們變得不可阻擋…… 吾族戰敗。
然而烏寬並不滿足於僅僅擊敗吾族、僅僅奴役吾族
他們要**更多**！ 他們要懲罰吾族膽敢反抗
所以他們構思了有史以來最病態、最殘忍、最變態的懲罰！……
他們入侵吾等自身的基因結構
並將吾等心智砍去足夠份量，使吾族永世成為閹割之族。
然後吾族被派為他們最貼身的僕從…… 他們的『會話寵』。
這，就是吾族的懲罰。
```
**v3**：
```
全都是真的，艦長！ 一字不假！
現在聽好！……本尊來告訴你烏寬為什麼要對我族做這種事。
那是超過兩萬個你們的年頭之前，艦長，當時一艘烏寬奴役襲擊艦——
降落在我族的星球表面，開始抓捕我族的族人——不肯屈服的就殺！
你問本尊怎麼會知道？ 這些記憶深深烙印在本尊的基因結構裡，不可能被遺忘。
我族當年是怎麼奮力抵抗烏寬的啊！ 即使那時候，他們就已經有一支戰奴階層——
只不過那時候他們自稱那個荒謬的名字——感知聯盟！
哈！ 他們不過就是一群暴徒，尤其是那些醜陋的塔洛族。
那些邪惡的岩石狀生物，是所有裡面最壞的！
為了取樂，他們會抓一個我族的孩子……然後……在他身上翻滾！……一次又一次，噢！
對烏寬和他們感知聯盟的戰爭打了幾十年……我族死了幾百萬——
但真理與正義的力量站在我族這邊，我族當時可是佔上風。
然後塔洛族做出了他們那決定性的發現……一種能夠對付我族唯一武器——微弱心靈能力——的護盾。
有了那個護盾，他們變得不可阻擋……我族輸了。
但烏寬啊，他們不滿足於僅僅打敗我族、奴役我族——
他們要更多！ 他們要懲罰我族竟敢反抗——
所以他們設計出了想像中最病態、最殘忍、最變態的懲罰！……
他們入侵了我族的基因結構本身——
砍掉了我族大腦裡足夠的部分，讓我族被智能閹割到永遠。
然後我族就被變成了他們最貼身的僕人……他們的「會話寵」。
這就是我族受到的懲罰。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #36 · `WORTH_A_TRY` · 🟠

**EN**：
```
Dang! You are the most inconveniently well-informed creature, Captain!
*sigh* Well, it was worth a try.
```
**Shipped**：
```
靠！ 爾真是個令人不便地情報靈通的生物，艦長！
（嘆氣）唉，值得試試就試試唄。
```
**v3**：
```
該死！ 你真是本尊碰過情報最靈通的生物，艦長，煩死！
＊嘆氣＊ 好吧，反正試試也不虧。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #38 · `PLEASE_DONT` · 🟠

**EN**：
```
No! Please don't!
I am the last of my species! You cannot do this to me!
```
**Shipped**：
```
不！ 拜託不要！
本座是本族最後一個！ 爾不可對本座這麼做！
```
**v3**：
```
不！ 拜託不要！
本尊是本尊族群的最後一個！ 你不能這樣對本尊！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #40 · `DONT_KILL` · 🟠

**EN**：
```
Hmmm! How interesting! During that last little threat of yours, I noticed something WONDERFUL!
YOU DON'T HAVE THE TAALO SHIELD PROPERLY INSTALLED!
Ha-ha-ha! Fool! You could have fired on me.
Now, I fear, you will have to accept my offer.
I will join you on board your vessel. Together, we will exact MY revenge
and perhaps incidentally, realize your own plans as well.
```
**Shipped**：
```
嗯！ 有意思！ 在爾方才最後那小小的威脅時，本座注意到了一個**美妙**的事情！
**爾的塔洛盾沒有正確安裝！**
哈哈哈！ 蠢貨！ 爾原本可以對本座開火。
如今，恐怕，爾只能接受本座的提議了。
本座將登上爾的艦艇。 我們同行，將實現**本座**的復仇
附帶地，或許也能實現爾自己的計畫。
```
**v3**：
```
嗯！ 真有意思！ 剛才你那個小小的威脅期間，本尊注意到一件超棒的事！
你的塔洛盾根本沒好好裝上！
哈-哈-哈！（Ha-ha-ha!） 蠢材！ 你剛剛本來可以對本尊開火的。
現在，恐怕，你只能接受本尊的提議了。
本尊會登上你的艦艇。 我們一起去執行本尊的復仇——
或許順便，也把你自己的計畫實現了。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #44 · `GLAD_YOU_WONT_KILL` · 🟠

**EN**：
```
Wonderful, Captain. I am so glad you have seen the light of reason.
I shall gather my few possessions, and come aboard your vessel immediately.
When you wish to talk with me, I will be down in your ship's cargo hold.
That is all, Captain. For now, at least.
```
**Shipped**：
```
太好了，艦長。 本座真高興爾看見了理性之光。
本座將收拾我微薄的家當，即刻登上爾的艦艇。
當你想與我談時，我會在你船艦的貨艙裡。
就這樣，艦長。 至少暫時是這樣。
```
**v3**：
```
太好了，艦長。 本尊真高興你想通了、看清楚道理了。
本尊會把本尊那點微薄的家當收一收，馬上登上你的艦艇。
你想跟本尊說話時，本尊會在你艦艇的貨艙裡。
就這樣了，艦長。 目前是這樣。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #46 · `GENERAL_INFO_ONBOARD_1` · 🟠

**EN**：
```
It is cold and empty. I could use a thermal blanket.
Since it is incredibly boring down here
I am using the opportunity to try and get some sleep.
```
**Shipped**：
```
既冷又空。 本座可以用一條保暖毯。
既然下面極其無聊
本座正利用機會試著睡點覺。
```
**v3**：
```
又冷又空。 本尊需要條保溫毯。
既然這下面無聊透頂——
本尊就趁機睡個覺。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #47 · `GENERAL_INFO_ONBOARD_2` · 🟠

**EN**：
```
Much the same as the last time you asked me.
However, I have found a way to amuse myself.
I am listening in on the mental energies of your crew -- it's really quite fun!
For instance, did you know both ensigns Holiday and Watchuki want to reproduce with you?
Ha-ha! It's true!
```
**Shipped**：
```
跟你上次問差不多。
不過，本座找到自娛的方式了。
本座在偷聽你船員的心靈能量 —— 真的很好玩！
舉例來說，你知道嗎，霍利黛少尉與瓦楚基少尉**兩人**都想和你繁殖？
哈哈！ 是真的！
```
**v3**：
```
跟上次你問本尊的時候差不多。
不過，本尊找到自娛的方法了。
本尊在偷聽你們船員的心靈能量——真的挺有趣的！
舉例來說，你知道霍利黛（Holiday）少尉和渥啟基（Watchuki）少尉，兩個都想跟你繁殖後代嗎？
哈-哈！（Ha-ha!） 真的喔！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #48 · `GENERAL_INFO_ONBOARD_3` · 🟠

**EN**：
```
I suppose you told your crew about my little listening in on them, didn't you?
Now whenever I try to eavesdrop, they seem to detect my presence
and start visualizing my gruesome death in a multitude of repulsive though creative ways.
You had to go and spoil my fun, didn't you?
```
**Shipped**：
```
我想你把本座偷聽他們的事告訴船員了，對吧？
如今每當本座嘗試竊聽時，他們似乎都能察覺本座的存在
然後開始用各種嘔心卻富創意的方式想像本座的可怕死狀。
你**非要**去毀了本座的樂趣，是吧？
```
**v3**：
```
本尊猜你把本尊在偷聽的事告訴船員了，是不是？
現在本尊每次想偷聽，他們好像都會察覺本尊的存在——
然後開始想像本尊死狀有多噁心、方式又有多有創意。
你就非得毀了本尊的樂趣不可，是吧？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #49 · `GENERAL_INFO_ONBOARD_4` · 🟠

**EN**：
```
You know, I was just reliving some of my ancestors' stronger genetic memories
and I came upon something I thought you might be interested in hearing.
It seems that my race, the Dnyarri, once found a Precursor vessel like your own.
Well actually, it wasn't EXACTLY like yours.
It was a combat vessel -- bigger, much bigger, and it was loaded with tons of world-wrecking accoutrements.
Frankly, it made this vessel look like a tug... a real weenie. Ha-ha-ha!
Anyway, when the Ur-Quan so cruelly attacked us, they stole the ship
and I can only presume that they still have it in their possession.
Maybe you should find out more about that ship, Captain.
```
**Shipped**：
```
說到這個，本座剛剛在重溫本座祖先較強烈的基因記憶
偶然遇到一件本座想你會有興趣知道的事。
似乎吾等蟾亞族在遠古時曾發現過一艘和爾這艘類似的先驅者艦。
這個嘛，其實**沒那麼**像爾這艘啦。
那是艘戰鬥艦 —— 更大，**大得多**，還裝滿了幾噸重的世界毀滅級配件。
老實說，讓爾這艘看起來像艘拖船…… 真是根小雞雞。 哈哈哈！
總之，當烏寬如此殘忍地攻擊吾族時，他們奪走了那艘艦
本座只能推測他們如今仍持有著它。
或許爾該多打聽點那艘艦的下落，艦長。
```
**v3**：
```
你知道嗎，本尊剛才在重溫本尊祖先一些比較強烈的基因記憶——
本尊發現一件本尊覺得你或許會有興趣的事。
看起來本尊的族群、我族蟾亞，曾經找到過一艘先驅者艦艇——就像你這艘一樣。
嗯，其實吧，也不是跟你這艘完全一樣。
那是一艘戰鬥艦——更大、大很多，而且裝載了一堆能摧毀整顆行星的傢私。
說實話，那把你這艘艦襯得像艘小拖船……真是個弱雞。 哈-哈-哈！（Ha-ha-ha!）
總之，當烏寬那樣殘忍地攻擊我族時，他們把那艘艦搶走了——
本尊只能猜想他們現在還握有它。
或許你該多了解那艘艦，艦長。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #50 · `GENERAL_INFO_ONBOARD_5` · 🟠

**EN**：
```
I am slowly going insane, Captain!
I don't know if you are aware of this
but there are music loops which play down here, CEASELESSLY!
I presume this was some engineer's brilliant idea
on how to keep the simple-minded dock workers happy.
I would guess that the engineer didn't foresee someone ACTUALLY LIVING DOWN HERE!
I have heard the same songs AT LEAST FOUR HUNDRED TIMES!
I mean, Mozart and Iggy Pop are fine, for alien noise-makers
but PLEASE!... CHANGE THE MUSIC BEFORE I GO MAD!
```
**Shipped**：
```
本座快瘋了，艦長！
本座不知道你有沒有意識到這點
但下面有音樂循環播放，**無止盡地**！
本座猜這是某位工程師的天才主意
用來讓那些頭腦簡單的碼頭工人保持心情愉快。
本座猜想那位工程師沒料到會有人**真的住在下面**！
本座已經聽同幾首歌**至少四百遍**了！
本座是說，莫札特和伊基·帕普（Iggy Pop）作為外星人的噪音製造者是不錯
可**拜託**！…… 在本座發瘋之前**換首歌吧**！
```
**v3**：
```
艦長，本尊正在慢慢瘋掉！
本尊不知道你有沒有意識到——
但這下面有音樂循環在播——播個沒完沒了！
本尊猜這是哪個工程師的天才發想——
用來讓頭腦簡單的船塢工人開心。
本尊猜想那個工程師沒有預料到——會有人真的住在這下面！
同樣那幾首歌，本尊已經聽了至少四百遍了！
本尊是說啦，莫札特（Mozart）跟伊基流行（Iggy Pop）作為外星噪音製造機是還好——
但拜託！……在本尊發瘋之前，把音樂換掉！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #51 · `GENERAL_INFO_ONBOARD_6` · 🟠

**EN**：
```
Thank you, Captain, for changing the music down here.
Now, if I may, I would like to complain about the food.
It is grossly unappealing and flavorless. I deserve better.
My preference is for chunks of meat, well spiced, with a selection of fresh plant matter.
Please, no more of those sweet, doughy cylinders in the little foil pouches.
Space food... Feh!
```
**Shipped**：
```
感謝你，艦長，換了下面的音樂。
如今，容本座斗膽，本座想抱怨一下食物。
食物毫無食慾且平淡無味。 本座配得上更好的。
本座喜好的是肉塊，好好調味過的，再配上一些新鮮的植物。
拜託，別再送那些甜的、麵團狀的、裝在小錫箔袋裡的圓柱狀物了。
太空食物…… 啐！
```
**v3**：
```
感謝艦長把下面的音樂換掉。
那個，本尊想抱怨一下食物，可以吧。
那實在太難吃了，一點味道都沒有。 本尊該吃更好的。
本尊偏好調味豐富的肉塊，配上一些新鮮的植物。
拜託，不要再送那些鋁箔袋裡甜膩膩的麵團圓筒了。
太空食物……呸！（Feh!）
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #52 · `GENERAL_INFO_ONBOARD_7` · 🟠

**EN**：
```
I am bored.
Please send me a couple of your crew members to play with
preferably one male, and one female, though I won't be picky.
No!? You have no sense of fun, Captain.
You must have been a boring child.
```
**Shipped**：
```
本座無聊。
拜託派幾個你的船員來下面陪本座玩
最好一男一女，不過本座不挑。
不要！？ 你完全不懂樂趣，艦長。
你小時候一定是個很無聊的孩子。
```
**v3**：
```
本尊很無聊。
拜託送幾個船員下來陪本尊玩——
最好一男一女，不過本尊不挑。
不行！？ 你真沒情趣，艦長。
你小時候一定是個很無聊的小孩。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #53 · `GENERAL_INFO_ONBOARD_8` · 🟠

**EN**：
```
I sing. I dance. I have a wild, fun time.
My life is one endless party down here, Captain. Isn't that obvious?
```
**Shipped**：
```
本座唱歌。 本座跳舞。 本座過得瘋狂又快活。
本座下面的人生是無止盡的派對，艦長。 明顯得很不是嗎？
```
**v3**：
```
本尊唱歌。 本尊跳舞。 本尊過得又狂又爽。
本尊在這下面的生活就是一場無盡的派對，艦長。 這不明顯嗎？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #54 · `HELLO_AS_DEVICE_1` · 🟠

**EN**：
```
Captain. The Taalo device on board this vessel is, uh, giving me a headache, please remove it.
NOW, Captain! It is foolish to resist!...
Hmmm... it remains more effective than I had thought, you are still able to disobey.
Ah, well. What can I do for you, Captain?
```
**Shipped**：
```
艦長。 這艘艦上的塔洛裝置，呃，讓本座頭痛，請把它移走。
**立刻**，艦長！ 抵抗是愚蠢的！……
嗯…… 它仍比本座料想的更有效，爾依然能違抗。
啊，好吧。 本座能為你效什麼勞，艦長？
```
**v3**：
```
艦長。 這艘艦上的塔洛裝置，呃，讓本尊頭痛——請把它移除掉。
現在就撤，艦長！ 抵抗是愚蠢的！……
嗯……它比本尊想的還有效——你還是能違抗本尊。
啊，好吧。 本尊能為你做什麼，艦長？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #55 · `HELLO_AS_DEVICE_2` · 🟠

**EN**：
```
Hello Captain.
It is less than comfy down here in your ship's cargo hold.
Please send down some pillows.
Now, what can I do for you?
```
**Shipped**：
```
哈囉艦長。
本座在你船艦的貨艙裡沒那麼舒服。
請送幾個枕頭下來。
那，本座能為你效什麼勞？
```
**v3**：
```
哈囉艦長。
你艦上的貨艙裡實在算不上舒適。
拜託送幾個枕頭下來。
那個，本尊能為你做什麼？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #56 · `HELLO_AS_DEVICE_3` · 🟠

**EN**：
```
I was asleep, gathering strength for our confrontation with the Ur-Quan.
This little interruption here has set me back several days. Now what is it?
```
**Shipped**：
```
本座在睡覺，為我方對抗烏寬的對決積蓄力量。
這次的小小打斷讓本座耽誤了好幾天。 有什麼事？
```
**v3**：
```
本尊剛才在睡覺，為我們跟烏寬的正面對決儲備力量。
你這麼一打擾，本尊就退步了好幾天。 什麼事？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #57 · `HELLO_AS_DEVICE_4` · 🟠

**EN**：
```
Heeelllllllloooooo...
Echoooooo...
I... Am... the Master of the Univer...
Oh! Heh-heh. Hey Captain! I didn't notice you on the viewer there.
I was just, you know, entertaining myself in this lonesome, cold container.
How may I be of service to you?
```
**Shipped**：
```
哈囉囉囉囉囉囉囉囉……
迴音音音音音……
本…… 座…… 是…… 宇宙…… 之主……
喔！ 嘿嘿。 嘿艦長！ 本座沒注意到你在螢幕上。
本座只是，你知道，在這孤單又冷的容器裡自娛自樂。
本座能怎麼為你效勞？
```
**v3**：
```
哈──囉──……（Heeelllllllloooooo...）
迴──聲──……（Echoooooo...）
本尊…… 是…… 宇宙至——
喔！ 嘿嘿。（Heh-heh.） 嘿艦長！ 本尊剛剛沒注意到你在螢幕上。
本尊只是，你懂的，在這個孤單又寒冷的容器裡自娛自樂。
有什麼能為你效勞的？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #58 · `HELLO_AS_DEVICE_5` · 🟠

**EN**：
```
sner-Gee......  sner-Gee......  sner-Gee......  sner-Gee......
sner-Umph?!  Oh... it is you. I was sleeping. What do you want?
```
**Shipped**：
```
呼嚕—嗯……  呼嚕—嗯……  呼嚕—嗯……  呼嚕—嗯……
呼—嗯呃？！  喔…… 是你啊。 本座在睡覺。 幹嘛？
```
**v3**：
```
呼──嘰──……（sner-Gee......） 呼──嘰──……  呼──嘰──…… 呼──嘰──……
呼──嗯？！（sner-Umph?!） 喔……是你啊。 本尊剛才在睡覺。 有什麼事？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #59 · `HELLO_AS_DEVICE_6` · 🟠

**EN**：
```
Are you lonely, Captain?
Are you misunderstood by everybody else on the ship?
Is that why you KEEP CALLING ME WHEN I AM ASLEEP!?
```
**Shipped**：
```
你孤單嗎，艦長？
你在船上被大家誤解嗎？
**就是**因為這樣才會**本座睡覺時你一直叫本座嗎**！？
```
**v3**：
```
你很寂寞嗎，艦長？
艦上其他人都不懂你嗎？
所以你才會在本尊睡覺的時候一直叫本尊起來嗎！？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #60 · `HELLO_AS_DEVICE_7` · 🟠

**EN**：
```
Captain, I am not a particularly social creature.
I grow tired of your yammering, but since you already woke me up
What is it?
```
**Shipped**：
```
艦長，本座不是特別愛社交的生物。
本座對你的絮叨感到疲倦，但既然你已經吵醒本座了
那是什麼事？
```
**v3**：
```
艦長，本尊不是那種特別喜歡社交的生物。
本尊已經厭倦你的碎唸了，但既然你已經把本尊吵醒——
什麼事？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #62 · `CYBORG_PEP_TALK` · 🟠

**EN**：
```
You've made it, Captain! The Sa-Matra shields are down!
Now all you have to do is get your ship in there next to the Sa-Matra and initiate the bomb sequence.
In case you're wondering, I'm not going with you, Captain. I'm staying on board.
Why, you ask?
BECAUSE I'M LOCKED IN HERE!
HELP!!!  GET ME OUT!!!  HELP!!!
```
**Shipped**：
```
你成功了，艦長！ 薩瑪特拉的護盾已降下！
如今你只需將艦艇開進去，貼近薩瑪特拉，然後啟動炸彈引爆序列。
如果你在想的話，本座沒打算跟你去，艦長。 本座留在船上。
為什麼，你問？
**因為本座被鎖在這裡面！**
**救命！！！ 放本座出去！！！ 救命！！！**
```
**v3**：
```
你辦到了，艦長！ 薩瑪特拉的護盾已經消失！
現在你只需要把艦艇開到薩瑪特拉旁邊，啟動炸彈序列就行了。
如果你在想，本尊不跟你一起去，艦長。 本尊留在船上。
為什麼，你問？
因為本尊被鎖在這裡！
救命！！！ 把本尊放出去！！！ 救命！！！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #63 · `HUMAN_PEP_TALK` · 🟠

**EN**：
```
Okay, human, you've made it past the Sa-Matra's guards
and now you can attack the vessel itself, so listen closely.
The Sa-Matra is protected by a thick shell of fused asteroids reinforced with a weak stasis field.
You will never break through that.
The only opening through the asteroid shield is covered with a powerful force screen.
One touch of that screen, and you're history, Captain.
To destroy the Sa-Matra, you will have to destroy the shield generators embedded in the asteroid shell.
To drop the force screen, you will have to destroy all eight of them.
When the screen is down, bring in your flagship, move into the asteroid shell
and then press the Big Red Button on your controls
that starts the detonation sequence.
Your escape pod will eject automatically. Just hope you're far enough away before that ship blows.
Ok, human, this is it! The last battle, your final moment of triumph!
Don't screw up.
And in case you're wondering, I'm not going with you, Captain. I'm staying on board.
Why, you ask?
BECAUSE I'M LOCKED IN HERE YOU IDIOT!
GET ME OUT!!  HELP!!!  HELP!!!
```
**Shipped**：
```
好，人類，你已通過了薩瑪特拉的守衛
現在你可以攻擊船體本身，所以聽清楚了。
薩瑪特拉受到融合小行星構成的厚殼保護，以微弱的靜滯場強化。
爾絕對無法穿透那個。
穿過小行星護盾的唯一開口被強大的力場罩住。
只要碰一下那力場，你就完蛋了，艦長。
要摧毀薩瑪特拉，你必須摧毀嵌入小行星殼裡的護盾產生器。
要讓力場降下，你必須摧毀**全部八個**護盾產生器。
當力場降下時，將你的旗艦開進去，進入小行星殼
然後按下你控制台上的**紅色大按鈕**
那會啟動引爆序列。
你的逃生艙會自動彈射。 只希望在船爆炸之前你已離得夠遠。
好，人類，就是這個時刻！ 最後一戰，你勝利的最終時刻！
**別搞砸了。**
如果你在想的話，本座沒打算跟你去，艦長。 本座留在船上。
為什麼，你問？
**因為本座被鎖在這裡面你這白痴！**
**放本座出去！！ 救命！！ 救命！！**
```
**v3**：
```
好了，人類，你已經闖過薩瑪特拉的守衛——
現在你可以攻擊艦艇本身了，所以仔細聽好。
薩瑪特拉被一層厚厚的融合小行星外殼保護，還有微弱的滯凝場加固。
你絕對無法突破那個。
穿過小行星護盾的唯一開口，被一道強大的能量屏障覆蓋。
只要碰到那道屏障，你就完了，艦長。
要摧毀薩瑪特拉，你必須摧毀嵌在小行星外殼裡的護盾產生器。
要讓能量屏障降下，你必須把八個都摧毀。
屏障降下後，把旗艦開進來，進入小行星外殼——
然後按下你操控台上的紅色大按鈕——
那會啟動引爆序列。
你的逃生艙會自動彈射。 只希望你在那艘船爆炸前離得夠遠。
好了，人類，就是這一刻了！ 最後一戰、你勝利的最終時刻！
別搞砸了。
如果你在想，本尊不跟你一起去，艦長。 本尊留在船上。
為什麼，你問？
因為本尊被鎖在這裡——你這個蠢材！
把本尊放出去！！ 救命！！！ 救命！！！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #64 · `I_SENSE_MY_SLAVES` · 🟠

**EN**：
```
I sense the presence of my ancient slaves.
It is time, Captain.
```
**Shipped**：
```
本座感應到吾等古代奴隸之存在。
是時候了，艦長。
```
**v3**：
```
本尊感應到本尊的古代奴隸就在附近。
時候到了，艦長。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #72 · `DO_THIS` · 🟠

**EN**：
```
Oh gosh, gee! I don't know. Let's just sit here and talk a while
AND IGNORE THOSE THOUSANDS OF DREADNOUGHTS THAT ARE GOING TO CREAM US IN A FEW SECONDS!
```
**Shipped**：
```
喔哎唷，天啊！ 本座不知道啊。 我們就這樣坐在這聊個天吧
然後**忽視那幾千艘幾秒內就要輾爆我們的無畏艦**！
```
**v3**：
```
喔天啊，噢！ 本尊不知道欸。 我們就坐在這裡聊個天吧——
不要理那幾千艘幾秒內就要把我們碾碎的無畏艦！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #74 · `HERE_WE_GO` · 🟠

**EN**：
```
Okay. Now, whatever you do, once I've started
DON'T LEAVE THE STAR SYSTEM!
We've only got one chance at this, let's make it good!
Here I go...
```
**Shipped**：
```
好。 那，無論你做什麼，一旦本座開始了
**別離開這個星系**！
我們只有這一次機會，讓它成功吧！
本座上了……
```
**v3**：
```
好。 現在，本尊開始之後，不管你做什麼——
絕對不要離開這個恆星系！
這種事我們只有一次機會，好好把握吧！
本尊上囉……
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #76 · `STUPID_FOP` · 🟠

**EN**：
```
`I'm scared, Dnyarri. What if this doesn't work?'
My species have waited two hundred centuries for this moment
SO STOP BLUBBERING!
Let's get to work.
```
**Shipped**：
```
『我怕，蟾亞。 萬一這行不通怎麼辦？』
吾族已為此刻等待了兩百個世紀
所以**別嗯嗯啊啊哭夭啦**！
動起來吧。
```
**v3**：
```
『我好怕，蟾亞。 萬一沒成功怎麼辦？』
本尊族群為了這一刻等了兩百個世紀——
給本尊停止哭哭啼啼！
我們去幹活。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #78 · `SAVING_MY_POWER` · 🟠

**EN**：
```
I am saving my meager powers for our final confrontation with the Ur-Quan.
Sorry, Captain. You'll just have to deal with this one yourself.
```
**Shipped**：
```
本座正保留本座微薄的能力，為對抗烏寬的最終對決。
抱歉，艦長。 這一個你只能自己處理了。
```
**v3**：
```
本尊在為我們跟烏寬的最終對決保留本尊那點微薄的力量。
抱歉，艦長。 這個你只能自己處理了。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #80 · `SUGGESTION_1` · 🟠

**EN**：
```
The first thing I'd do is make sure I had a strong ship and fleet.
```
**Shipped**：
```
本座第一件會做的事是確保自己擁有一艘強大的艦艇與艦隊。
```
**v3**：
```
本尊第一件會做的事，是先確保本尊有一艘強艦、一支強艦隊。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #81 · `SUGGESTION_2` · 🟠

**EN**：
```
Once I was tough enough to survive in hostile space
I'd spend some time exploring, trying to make allies and gather information.
```
**Shipped**：
```
一旦本座強韌到足以在敵對太空中生存下來
本座會花點時間探索、試圖結交盟友、蒐集情報。
```
**v3**：
```
一旦本尊夠強、可以在充滿敵意的太空存活——
本尊會花點時間探索，試著結盟並收集情報。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #82 · `SUGGESTION_3` · 🟠

**EN**：
```
After I'd done a fair bit of exploration, I would try to find out what the Ur-Quan are up to.
Discover who they are fighting, and why.
```
**Shipped**：
```
在本座做了相當程度的探索之後，本座會試圖搞清楚烏寬在幹嘛。
查出他們在跟誰打仗，還有為什麼。
```
**v3**：
```
等本尊做了相當程度的探索之後，本尊會試著搞清楚烏寬在打什麼算盤。
查清楚他們在跟誰打仗、為什麼打。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #83 · `SUGGESTION_4` · 🟠

**EN**：
```
Once I knew some general information about the Ur-Quan
I'd probably try to find their weak spot. Every race has one.
```
**Shipped**：
```
一旦本座對烏寬有了一些基本資訊
本座大概會試著找他們的弱點。 每個種族都有弱點。
```
**v3**：
```
一旦本尊掌握了關於烏寬的大致情報——
本尊大概會試著找出他們的弱點。 每個種族都有一個。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #84 · `SUGGESTION_5` · 🟠

**EN**：
```
Once I knew the Ur-Quan's critical weakness
I would try to discover how to exploit this flaw.
I would learn what was necessary for the task, and then gather those materials and services.
```
**Shipped**：
```
一旦本座知道了烏寬的關鍵弱點
本座會試著發現如何利用這個缺陷。
本座會學習完成此任務所需之物，然後蒐集這些物資與服務。
```
**v3**：
```
一旦本尊得知烏寬的關鍵弱點——
本尊會試著找出如何利用這個缺陷。
本尊會學習任務所需的東西，然後收集那些物資和服務。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #86 · `SUGGESTION_7` · 🟠

**EN**：
```
Well for one, I would stop asking questions and get to work.
```
**Shipped**：
```
唔，第一件事，本座會停止問問題，開始工作。
```
**v3**：
```
呃這個嘛，首先，本尊會停止問問題，開始行動。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #87 · `SUGGESTION_8` · 🟠

**EN**：
```
Well for one, I would stop asking questions and get to work.
```
**Shipped**：
```
唔，第一件事，本座會停止問問題，開始工作。
```
**v3**：
```
呃這個嘛，首先，本尊會停止問問題，開始行動。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #89 · `WHAT_ABOUT_RACE` · 🟠

**EN**：
```
I consider such a question to be intrusive and impolite
but that is consistent with your behavior.
What do you want to know?
```
**Shipped**：
```
本座覺得這種問題頗為冒犯又無禮
不過這符合爾的一貫行為。
爾想知道什麼？
```
**v3**：
```
本尊認為這種問題既冒昧又無禮——
不過這倒是符合你的行為模式。
你想知道什麼？
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #91 · `SO_WHAT` · 🟠

**EN**：
```
So I lied a little! Big deal.
I thought that if I told you the truth, you wouldn't bring me on board.
Besides, it wasn't me who did that, it was my ancient ancestors.
Were all of YOUR ancestors sweet and kind, Captain?
I thought not.
```
**Shipped**：
```
所以本座撒了點小謊！ 大不了。
本座是覺得，如果本座告訴爾實情，爾就不會帶本座上船了。
再說，那也不是本座做的，那是本座的**古代**祖先。
難道**爾的**祖先個個都是善良親切嗎，艦長？
本座想也不是吧。
```
**v3**：
```
本尊是撒了個小謊嘛！ 沒什麼大不了的。
本尊當時覺得，如果本尊講實話，你就不會把本尊帶上船。
再說，那也不是本尊做的，是本尊那些遠古祖先做的。
你所有的祖先都可愛又善良嗎，艦長？
本尊猜也不是吧。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #95 · `NO_TALK_ABOUT_SELF` · 🟠

**EN**：
```
You mean my superior brain, my mental prowess?
I don't want to talk about it.
```
**Shipped**：
```
爾指的是本座那卓越的頭腦，本座的心靈能力嗎？
本座不想聊那個。
```
**v3**：
```
你是指本尊那優越的大腦、本尊那過人的心智能力嗎？
本尊不想談這個。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #97 · `NOT_POWERS_BUT_FLOWERS` · 🟠

**EN**：
```
Captain, I don't think you meant to ask about my powers.
-<DIDN'T YOU MEAN TO ASK ABOUT FLOWERS?>-
```
**Shipped**：
```
艦長，本座覺得爾並非有意詢問本座的能力。
-<爾意欲詢問花朵之事？>-
```
**v3**：
```
艦長，本尊覺得你不是想問本尊的能力吧。
-<你該問的難道不是花朵嗎？>-
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #103 · `ABOUT_HISTORY` · 🟠

**EN**：
```
Over twenty thousand years ago, my species was happy and carefree
living a life of peace and contentment on the surface of our world Benteflork.
We spent our time gathering foods, creating art, and compelling each other to do the boring chores.
Then a ship from the Sentient Milieu landed, and well, things got pretty complicated.
```
**Shipped**：
```
兩萬多年前，吾族快樂又無憂無慮
在吾等世界本鐵佛克（Benteflork）的表面上過著和平又滿足的生活。
吾等以蒐集食物、創造藝術、以及**心靈操控彼此**去做無聊雜務為時光。
然後一艘來自感知聯盟的艦艇登陸，然後嗯，事情就變得相當複雜了。
```
**v3**：
```
兩萬多年前，本尊族群過得又開心又無憂無慮——
住在我族的星球本鐵佛克（Benteflork）表面上，日子祥和又滿足。
我族當年花時間採集食物、創作藝術，還有——彼此心控對方去做無聊的雜活。
然後感知聯盟的一艘船降落了，嗯，事情就變得挺複雜了。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #105 · `ABOUT_SENTIENT_MILIEU` · 🟠

**EN**：
```
The Sentient Milieu were a blood-thirsty Empire that ruled a large section of the galaxy for thousands of years.
If you heard that the Milieu was a cooperative union of sentient species
it's LIES, all lies!
The Ur-Quan were just a part of the Milieu, but their dark and evil hearts
infused the entire association with a sinister ambience.
```
**Shipped**：
```
感知聯盟是個嗜血的帝國，統治了銀河一大片區域數千年之久。
若爾聽說感知聯盟是個合作性的智慧生物聯合體
那是**謊言**，全是謊言！
烏寬只是感知聯盟的一部分，可他們黑暗又邪惡的心
將整個聯合體浸染上一股陰森氣息。
```
**v3**：
```
感知聯盟是個嗜血的帝國，統治了銀河一大片區域好幾千年。
如果你聽說感知聯盟是各智慧物種的合作聯合體——
那是謊言，全都是謊言！
烏寬只是感知聯盟的一部分，但他們那黑暗又邪惡的心靈——
讓整個聯合體都染上了一種陰森的氣氛。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #107 · `ABOUT_WAR` · 🟠

**EN**：
```
Well, after we had been in contact with the Milieu for a while
they decided to kill all of my species!
Now does that sound like a reasonable, friendly bunch of aliens, Hmm?  Huh?  Does it Captain?
No! It does not!
Well the war was over pretty quickly, and my species lost.
Instead of just killing us, the Ur-Quan modified our genes
Our children were born non-sentient, dumb animals.
For the past twenty millennia, we Dnyarri have been serving the Ur-Quan
in the most demeaning way they could imagine
acting as mindless translators who communicate the words of inferior races.
```
**Shipped**：
```
這個嘛，在吾族與感知聯盟接觸了一段時間之後
他們決定要**殺光**吾等一族！
這聽起來像是一群講理、友善的外星人嗎，嗯？ 啊？ 是嗎，艦長？
不！ 才不像！
這個嘛，戰爭很快就結束了，吾族戰敗。
烏寬沒有直接殺了吾族，而是改造了吾等的基因
吾等的孩子出生時無感知能力，是笨獸。
過去兩萬年來，我方蟾亞一直在為烏寬服役
以他們能想像出的最卑賤方式
作為無心智的譯者，傳達次等種族之言語。
```
**v3**：
```
嗯，我族跟感知聯盟接觸了一陣子之後——
他們就決定把本尊族群全部殺光！
這聽起來像講理又友善的一群外星人嗎，嗯？ 啊？ 像嗎艦長？
不！ 一點也不像！
嗯，戰爭結束得挺快，我族輸了。
烏寬沒有直接殺掉我族——他們修改了我族的基因——
讓我族的孩子生下來就沒有智能，只是頭腦簡單的畜生。
過去這兩萬年來，我族蟾亞一直為烏寬服役——
用他們想像得到最貶低我族的方式——
當個沒有心智的翻譯員，傳達那些劣等種族的話。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #109 · `OK_ENOUGH_INFO` · 🟠

**EN**：
```
That's good, I was getting sleepy.
```
**Shipped**：
```
好，本座正睏著呢。
```
**v3**：
```
太好了，本尊剛好開始想睡了。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #110 · `UMGAH_ALL_GONE` · 🟠

**EN**：
```
Such great plans, such fine dreams... now, all ground to dust.
Hello, Captain. Pardon my lament, but I am feeling a bit depressed today.
You see, the black destroyers -- the Kohr-Ah -- passed through recently on a killing spree
and now my Umgah, the instruments of my revenge, are all pretty much dead.
In case you are confused about who I am, and what I'm doing here, I'll explain.
I am a called a `talking pet'
For many years I served as a translator aboard an Ur-Quan Dreadnought.
During this time though, I possessed less intelligence than an Earth swine, but this was soon to change.
The Dreadnought came under attack by the Kohr-Ah and was severely damaged.
We made a crash-landing at a planet orbiting <% comm.getStarName("Alpha Pavonis", "urquan wreck") %>. I was the only survivor.
The prospect of investigating a Dreadnought was sufficient to bring the Arilou down to the planet surface, where they found me.
They tried to nurse me back to health, but they could not repair all my damage.
So they turned to their neighbors, the Umgah, for assistance.
The Umgah saw that I had the potential for intelligence, and they proceeded to modify my brain.
When I came to my senses following the final operation, a flood of thought and memory filled my mind.
I knew who I was!
I was a Dnyarri -- a member of a peaceful alien race, whose intelligence the Ur-Quan had long ago `shut off'
via cruel biogenetic manipulation.
I convinced the Umgah to assist me in effecting a magnificent revenge against the Ur-Quan
and we were just a few months away from launching our strike
well, when the Kohr-Ah passed through and casually slaughtered the entire Umgah species.  Bummer.
But here YOU are, Captain!
I have an offer: instead of killing me, I will join you on your ship.
I can be of invaluable assistance when it comes time for your final confrontation with the Ur-Quan.
I see you are speechless with approval. I'll be right over.
```
**Shipped**：
```
如此宏偉的計畫，如此美好的夢想…… 如今，全都化為塵土。
哈囉，艦長。 恕本座哀嘆，本座今日感到有點沮喪。
爾看，那些黑色毀滅者 —— 柯亞 —— 最近經過並展開了大屠殺
如今本座那些陰嘎族 —— 本座復仇的工具 —— 都差不多死光了。
如果爾對本座是誰、本座在做什麼有點困惑，本座來說明。
本座被稱作『會話寵』
多年來本座在一艘烏寬無畏艦上擔任譯者。
在那段時間裡，本座擁有的智能還不如一頭地球豬，但這即將改變。
那艘無畏艦遭到柯亞攻擊，嚴重受損。
我們墜毀於一顆繞著 <% comm.getStarName("孔雀座α", "urquan wreck") %> （Alpha Pavonis）運行的行星。 本座是唯一倖存者。
調查一艘無畏艦的前景足以吸引阿麗露降臨到那顆行星表面，他們在那裡發現了本座。
他們試著治好本座，可他們無法修復本座所有的損傷。
所以他們求助於鄰居陰嘎族。
陰嘎族看出本座有智能的潛力，並著手改造本座的腦。
當本座在最後一次手術後恢復意識時，思想與記憶的洪流湧入本座的心靈。
本座知道自己是誰！
本座是**蟾亞** —— 一個和平外星種族的一員，其智能被烏寬於久遠之前『關閉』
藉由殘忍的生物基因操縱。
本座說服陰嘎族協助本座對烏寬進行華麗的復仇
我們距離發動打擊只差幾個月
這個嘛，然後柯亞經過並隨意屠殺了整個陰嘎族。 靠。
可**爾**就在這裡，艦長！
本座有個提議：與其殺了本座，本座加入爾的艦艇。
本座在爾與烏寬最終對決之時，能提供無價的協助。
本座見爾贊同得說不出話。 本座這就過去。
```
**v3**：
```
多麼宏大的計畫、多麼美好的夢想……如今全都化為塵土了。
你好，艦長。 原諒本尊的哀嘆，但今天本尊有點沮喪。
你瞧，那些黑色毀滅者——柯亞族——最近經過這裡大開殺戒——
本尊的陰嘎族，本尊復仇的工具，現在幾乎全都死光了。
如果你搞不清楚本尊是誰、本尊在這裡做什麼，本尊來解釋。
本尊被叫做「會話寵」——
本尊當年在一艘烏寬無畏艦上擔任翻譯員很多年。
不過那段時間，本尊智力比一頭地球豬還低，但這狀況很快就會改變。
那艘無畏艦遭到柯亞族攻擊，嚴重受損。
我們迫降在一顆繞著 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）運行的行星上。 本尊是唯一的生還者。
調查無畏艦的前景，吸引了阿麗露下到行星表面，他們就在那裡找到本尊。
他們試著把本尊救回健康，但沒辦法修復本尊所有的損傷。
所以他們轉向鄰居陰嘎族尋求協助。
陰嘎族看出本尊有智能的潛力，就著手改造本尊的大腦。
最後一次手術後，本尊恢復意識時，思想與記憶的洪流灌滿本尊的心智。
本尊知道自己是誰了！
本尊是一名蟾亞——一個和平外星種族的成員，他們的智能被烏寬很久以前——
透過殘忍的生物基因操控——「關掉」了。
本尊說服陰嘎族協助本尊，策劃一場對烏寬的華麗復仇——
我們距離發動攻擊只剩幾個月——
然後，柯亞族經過，隨手就把整個陰嘎族屠殺殆盡了。 真掃興。
但你在這裡啊，艦長！
本尊有個提議：與其殺了本尊，不如本尊登上你的船。
等到你跟烏寬做最終對決的時候，本尊會是無價的助力。
本尊看得出你贊同得說不出話。 本尊馬上過去。
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #111 · `HELLO_AFTER_COMPEL_URQUAN` · 🟠

**EN**：
```
WHAT ARE YOU DOING, IDIOT!!
DON'T TALK TO ME!
GO ATTACK THE SA-MATRA!!
```
**Shipped**：
```
**你在幹嘛啊，白痴！！**
**別跟本座講話！**
**去攻擊薩瑪特拉！！**
```
**v3**：
```
你在幹嘛啊，蠢材！！
別跟本尊說話！
快去攻擊薩瑪特拉！！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

### #112 · `OUT_TAKES` · 🟠

**EN**：
```
So! You probably thought I was dead... DIDN'T YOU!?
Well I'm not! I got away from the ship at the last second
and now I'm REALLY going to cause some trouble!
In fact, that's what the sequel is going to be about!
Yeah, that's the ticket! Me and my exciting adventures
as I conquer the galaxy for the greater glory of... ME!
It will have action! It will have drama!
It will have gratuitous alien sex scenes!
It's gonna be great!
```
**Shipped**：
```
嘿！ 爾大概以為本座死了…… **對不對**！？
哈，可惜沒有！ 本座在最後一秒鐘逃離了艦艇
現在本座**真的**要搞出點麻煩！
事實上，續集就是要講這個！
對嘛，就是這樣！ 本座與本座刺激的冒險
本座征服銀河系，為了…… **本座**更偉大的榮耀！
將有動作！ 將有戲劇！
將有多餘的外星性愛場面！
一定很棒！
```
**v3**：
```
哈！ 你八成以為本尊死了……是不是啊！？
嗯，本尊沒死！ 本尊在最後一秒逃出了那艘船——
現在本尊真的要來搞事了！
事實上，續集就是要拍這個！
對，就是這個！ 本尊跟本尊的刺激冒險——
本尊征服銀河，為了……本尊自己更偉大的榮光！
會有動作！ 會有戲劇！
還會有沒必要的外星人性愛場面！
一定會超讚的！
```
**推薦**：**B (v3)** — shipped 含文言污染 / 缺 dossier v0.7 icon · v3 採用招牌 icon + 現代語
**選擇**：A / B / C（自訂）

---

## 🟡 微調（46 tokens）

### #1 · `HELLO_AT_UMGAH` · 🟡

**EN**：
```
What do you want?
```
**Shipped**：
```
爾欲何為？
```
**v3**：
```
你想要什麼？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #2 · `what_are_you` · 🟡

**EN**：
```
I thought this was the Umgah homeworld. Who are you?
```
**Shipped**：
```
我以為這是陰嘎族的母星。 你到底是誰？
```
**v3**：
```
我以為這是陰嘎母星。 你是誰？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #4 · `talking_pets_dumb` · 🟡

**EN**：
```
But I thought Talking Pets weren't sentient? You seem smart enough.
```
**Shipped**：
```
但我以為會話寵沒有感知能力？ 你看起來夠聰明的。
```
**v3**：
```
可是我以為會話寵沒有智能？ 你看起來夠聰明嘛。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #6 · `what_do_to_umgah` · 🟡

**EN**：
```
Where are the Umgah? What have you done to them?
```
**Shipped**：
```
陰嘎族在哪裡？ 你對他們做了什麼？
```
**v3**：
```
陰嘎族在哪？ 你把他們怎麼樣了？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #7 · `DID_NOTHING` · 🟡

**EN**：
```
Uh, You are, um, imagining things! Uh, the Umgah are fine, just fine. Uh, just really busy.
That's why I am answering the HyperWave broadcaster today.
```
**Shipped**：
```
呃，爾這是在，嗯，胡思亂想！ 呃，陰嘎族都好好的，非常好。 呃，就是很忙罷了。
這就是為什麼今天由小的來接超波廣播器。
```
**v3**：
```
呃，你，那個，是在幻想吧！ 呃，陰嘎族好得很，好得不得了。 呃，只是他們超級忙。
所以今天才由我來接超波播送器。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #8 · `umgah_zombies` · 🟡

**EN**：
```
You don't fool me! You've turned them into zombie-blobbies!... or something.
```
**Shipped**：
```
別想騙我！ 你把他們變成殭屍黏團了！…… 之類的。
```
**v3**：
```
你騙不了我！ 你把他們變成殭屍膠團（zombie-blobbies）了！……之類的。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #10 · `we_are_vindicator` · 🟡

**EN**：
```
I am Captain of the starship <% state.sis.getShipName() %>. We have come in peace to talk with the Umgah leaders about overthrowing the Ur-Quan Hierarchy.
```
**Shipped**：
```
我是星艦 <% state.sis.getShipName() %> 號的艦長。 我方前來是為了跟陰嘎族領導層和平談論推翻烏寬戰奴階層的事。
```
**v3**：
```
我是星艦 <% state.sis.getShipName() %> 的艦長。 我方為和平而來，希望與陰嘎領袖商討推翻烏寬戰奴階層一事。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #12 · `must_explain_presence` · 🟡

**EN**：
```
Strange creature. Explain your presence here immediately.
```
**Shipped**：
```
怪東西。 立刻解釋你為何在此。
```
**v3**：
```
奇怪的生物。 立刻解釋你為什麼會在這裡。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #14 · `bye_at_umgah` · 🟡

**EN**：
```
Look, ah... whoever you are. I'll just be leaving now.
```
**Shipped**：
```
聽著，呃…… 不管你是誰。 我現在就走。
```
**v3**：
```
呃……不管你是誰。 我這就走。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #23 · `what_kind_of_deal` · 🟡

**EN**：
```
What kind of deal, Talking Pet? Provide details.
```
**Shipped**：
```
什麼樣的交易，會話寵？ 說詳細點。
```
**v3**：
```
什麼樣的協議，會話寵？ 說詳細一點。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #25 · `ok_lets_do_it` · 🟡

**EN**：
```
All right, I agree. But any tricks and you'll be sucking vacuum.
```
**Shipped**：
```
好，我同意。 但你要是耍花招，就等著吸真空吧。
```
**v3**：
```
好吧，我答應。 但你要是耍任何花招，就吸真空去吧。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #27 · `how_trust` · 🟡

**EN**：
```
You tried to kill me! Your words are lies! How can I possibly trust you?
```
**Shipped**：
```
你曾想殺我！ 你的話都是謊言！ 我怎麼可能信任你？
```
**v3**：
```
你想殺我！ 你說的都是謊話！ 我怎麼可能信得過你？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #31 · `what_are_you_really` · 🟡

**EN**：
```
Talking Pet. What are you... really?
```
**Shipped**：
```
會話寵。 你…… 到底是什麼？
```
**v3**：
```
會話寵。 你到底……是什麼？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #33 · `hard_to_believe` · 🟡

**EN**：
```
An amazing story, if true. Pardon me if I am a bit skeptical, but you are a proven liar.
```
**Shipped**：
```
若屬實，倒是個驚人的故事。 恕我有點懷疑，但你可是個經證實的騙子。
```
**v3**：
```
若是真的，倒是個了不起的故事。 抱歉我還是有點懷疑——畢竟你是個已知的騙子。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #35 · `bullshit` · 🟡

**EN**：
```
What a load of crap! YOUR species were the slavemasters, you lying, evil creature!!
```
**Shipped**：
```
根本一派胡言！ **你的**種族才是奴役者，你這撒謊的邪惡生物！！
```
**v3**：
```
胡說八道！ 明明是你們這個物種當年才是奴役主，你這個滿口謊言的邪惡生物！！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #37 · `kill_you` · 🟡

**EN**：
```
Heinous, brainy frog-monster. You must die!
```
**Shipped**：
```
邪惡有頭腦的青蛙怪物。 你必須死！
```
**v3**：
```
邪惡又聰明的青蛙怪。 你非死不可！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #39 · `must_kill` · 🟡

**EN**：
```
I will not be swayed from my path. Say your prayers.
```
**Shipped**：
```
我不會偏離我的道路。 說你的臨終禱告吧。
```
**v3**：
```
我不會動搖的。 你去禱告吧。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #41 · `want_kill_1` · 🟡

**EN**：
```
Must... resist! Can't... let... it... win! Must... not...
```
**Shipped**：
```
必須…… 抵抗！ 不能…… 讓…… 它…… 贏！ 絕不…… 能……
```
**v3**：
```
必須……抵抗！ 不能……讓……它……贏！ 必須……不……
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #42 · `want_kill_2` · 🟡

**EN**：
```
I - have - no - desire - to - kill - you. Welcome - aboard - our - vessel.
```
**Shipped**：
```
我 - 無 - 意 - 殺 - 你。 歡 - 迎 - 登 - 上 - 我方 - 艦艇。
```
**v3**：
```
我 - 沒有 - 想 - 殺 - 你 - 的 - 意思。 歡迎 - 登上 - 我們的 - 艦艇。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #43 · `want_kill_3` · 🟡

**EN**：
```
Kill? Kill? What is this `kill'? We love you!
```
**Shipped**：
```
殺？ 殺？ 這『殺』是何物？ 我方愛你！
```
**v3**：
```
殺？ 殺？ 什麼是「殺」？ 我們愛你！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #45 · `whats_up_onboard` · 🟡

**EN**：
```
How's it going, Dnyarri?  You okay down there in the cargo bay?
```
**Shipped**：
```
還好嗎，蟾亞？ 你在下面貨艙區還好吧？
```
**v3**：
```
怎麼樣，蟾亞？ 在下面貨艙裡還好嗎？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #61 · `HELLO_AS_DEVICE_8` · 🟡

**EN**：
```
This had better be important.
```
**Shipped**：
```
這事最好是很重要。
```
**v3**：
```
這件事最好是重要的。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #65 · `HAVENT_GOT_EVERYTHING` · 🟡

**EN**：
```
You are not yet ready to face the Ur-Quan in a final confrontation, Captain
```
**Shipped**：
```
你尚未準備好與烏寬進行最終對決，艦長
```
**v3**：
```
你還沒準備好跟烏寬做最後對決，艦長。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #66 · `NEED_BOMB` · 🟡

**EN**：
```
You still need a weapon of sufficient destructive force to destroy the Sa-Matra
```
**Shipped**：
```
你仍需一件足以摧毀薩瑪特拉的毀滅性武器
```
**v3**：
```
你還需要一件破壞力足以摧毀薩瑪特拉的武器。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #67 · `SOUP_UP_BOMB` · 🟡

**EN**：
```
The power of the Utwig's bomb must be increased
```
**Shipped**：
```
憂特族之炸彈的威力必須增強
```
**v3**：
```
憂特族炸彈的威力必須增強。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #68 · `SOUP_UP_FLEET` · 🟡

**EN**：
```
You must strengthen your fleet
```
**Shipped**：
```
你必須強化你的艦隊
```
**v3**：
```
你必須強化你的艦隊。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #69 · `SOUP_UP_FLAGSHIP` · 🟡

**EN**：
```
Your flagship needs additional improvements
```
**Shipped**：
```
你的旗艦需要額外的改良
```
**v3**：
```
你的旗艦需要額外的改良。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #70 · `COMEBACK_WHEN_READY` · 🟡

**EN**：
```
This must be done before you are ready to attack.
We must leave now, and return when you are fully prepared.
```
**Shipped**：
```
這必須在你準備發動攻擊之前完成。
我方現在必須離開，待你完全準備妥當後再回來。
```
**v3**：
```
這些必須在你準備發動攻擊之前完成。
我們現在必須離開，等你完全準備好再回來。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #73 · `compel_urquan` · 🟡

**EN**：
```
Employ your powers! Confuse the Ur-Quan!
```
**Shipped**：
```
施展你的能力！ 讓烏寬混亂！
```
**v3**：
```
發動你的能力！ 迷惑烏寬！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #75 · `im_scared` · 🟡

**EN**：
```
I'm scared, Dnyarri. What if this doesn't work?
```
**Shipped**：
```
我怕，蟾亞。 萬一這行不通怎麼辦？
```
**v3**：
```
我好怕，蟾亞。 萬一沒成功怎麼辦？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #77 · `compel_that_ship` · 🟡

**EN**：
```
Dnyarri. There is a nearby ship which is annoying me. Compel it to self-destruct.
```
**Shipped**：
```
蟾亞。 附近有艘船在惹本座。 讓它自毀。
```
**v3**：
```
蟾亞。 附近有一艘船讓我很煩。 逼它自我毀滅。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #79 · `any_suggestions` · 🟡

**EN**：
```
What do you suggest I do now, Dnyarri?
```
**Shipped**：
```
你建議我現在該怎麼做，蟾亞？
```
**v3**：
```
你建議我現在該做什麼，蟾亞？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #85 · `SUGGESTION_6` · 🟡

**EN**：
```
When I was finally prepared for the final confrontation with the Ur-Quan
I would use me, the Talking Pet, to distract the Ur-Quan for a single moment
thus permitting me, who is really you at this point
to make the death-strike against the Ur-Quan.
```
**Shipped**：
```
當本座終於為對抗烏寬的最終對決做好準備時
本座會利用本座 —— 這隻會話寵 —— 讓烏寬分心一瞬
這樣使本座 —— 在此刻其實就是爾 —— 得以
對烏寬發動致命一擊。
```
**v3**：
```
等本尊終於準備好跟烏寬做最終對決——
本尊會利用本尊——就是這隻會話寵——來分散烏寬的注意力一瞬間——
藉此讓本尊——在這個時間點其實就是你——
對烏寬給出致命一擊。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #88 · `about_your_race` · 🟡

**EN**：
```
What can you tell me about your race, the Dnyarri?
```
**Shipped**：
```
跟我說說你的種族吧，蟾亞族。
```
**v3**：
```
你能告訴我關於你們蟾亞這個種族的什麼事嗎？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #90 · `you_lied` · 🟡

**EN**：
```
I have learned that you lied to me, Dnyarri. It was your race that made slaves of the Ur-Quan!
```
**Shipped**：
```
我已經知道你對我撒謊了，蟾亞。 是**你們的**種族奴役了烏寬！
```
**v3**：
```
我發現你之前在說謊，蟾亞。 當年是你們這個種族奴役了烏寬！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #92 · `bye_onboard` · 🟡

**EN**：
```
Okay, Dnyarri, you can go back to sleep now.
```
**Shipped**：
```
好，蟾亞，你可以回去睡覺了。
```
**v3**：
```
好了，蟾亞，你可以回去睡覺了。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #93 · `GOODBYE_ONBOARD` · 🟡

**EN**：
```
Goodbye human.
```
**Shipped**：
```
再見，人類。
```
**v3**：
```
再會了人類。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #94 · `what_about_physiology` · 🟡

**EN**：
```
What can you tell me about your species biology?
```
**Shipped**：
```
跟我說說你們一族的生理吧。
```
**v3**：
```
關於你們這個物種的生物特性，你能告訴我什麼？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #96 · `what_about_powers` · 🟡

**EN**：
```
Come on, we're friends! Tell me about the scope of your psychic powers!
```
**Shipped**：
```
拜託，我們是朋友嘛！ 跟我說說你心靈能力的範圍！
```
**v3**：
```
別這樣嘛，我們是朋友！ 跟我說說你心靈能力的範圍！
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #98 · `yes_flowers` · 🟡

**EN**：
```
Yes - Dnyarri - I - wish - to - know - about - flowers.
```
**Shipped**：
```
是 - 的 - 蟾亞 - 我 - 想 - 知道 - 關於 - 花朵 - 的 - 事。
```
**v3**：
```
是的 - 蟾亞 - 我 - 想 - 知道 - 花朵 - 的事。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #99 · `GOOD_HUMAN` · 🟡

**EN**：
```
Flowers are beautiful, and smell nice.
Now be a good human and
-<LEAVE ME ALONE!>-
```
**Shipped**：
```
花朵美麗，且氣味芬芳。
如今做個乖人類然後
-<離本座遠去！>-
```
**v3**：
```
花朵很美，聞起來也香。
現在做個乖巧的人類——
-<別煩本尊！>-
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #100 · `wish_to_go_now` · 🟡

**EN**：
```
I - wish - to - go - now.
```
**Shipped**：
```
我 - 想 - 現在 - 就走。
```
**v3**：
```
我 - 想 - 現在 - 就 - 走。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #101 · `EXCELLENT_IDEA` · 🟡

**EN**：
```
An excellent idea, Captain. You must have a great deal of work to attend to.
Goodbye.
```
**Shipped**：
```
極佳的主意，艦長。 你想必有大量的工作要處理。
再見。
```
**v3**：
```
絕妙的主意，艦長。 你想必有很多工作要處理。
再會。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #102 · `what_about_your_history` · 🟡

**EN**：
```
What can you tell me about the history of your people?
```
**Shipped**：
```
跟我說說你們一族的歷史吧。
```
**v3**：
```
關於你們族群的歷史，你能告訴我什麼？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #104 · `sentient_milieu` · 🟡

**EN**：
```
I know so little about the Sentient Milieu. Can you describe it?
```
**Shipped**：
```
我對感知聯盟所知甚少。 你能描述一下嗎？
```
**v3**：
```
我對感知聯盟所知甚少。 可以描述一下嗎？
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

### #106 · `what_about_war` · 🟡

**EN**：
```
So tell me about the war between your species and the Sentient Milieu.
```
**Shipped**：
```
那，跟我說說你們一族與感知聯盟的戰爭吧。
```
**v3**：
```
那跟我說說你們物種跟感知聯盟之間的戰爭。
```
**推薦**：**A (shipped)** — 等價微調 · 保留原譯即可 · 除非明確 icon 差別
**選擇**：A / B / C（自訂）

---
