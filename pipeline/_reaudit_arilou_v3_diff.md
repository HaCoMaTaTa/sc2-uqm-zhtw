# Arilou (阿麗露) Rebuild-Compare Diff Report v3.0

**日期**: 2026-08-17
**Rebuild-Compare workflow**: `StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md`
**目標檔案**: `uqm-work/translations/arilou.zh-TW.v3.json`
**Shipped 備份**: `uqm-work/translations/arilou.zh-TW.pre-rebuild.bak`
**Read-Aloud self-fix log**: `uqm-work/_selfaudit_arilou_v3_readaloud.md`

## 統計

- Total tokens: 97
- 🟢 完全相同: **8** (8.2%)
- 🟡 微調 (等價): **27** (27.8%)
- 🟠 措辭改變: **50** (51.5%)
- 🔴 語意/voice 差異大: **0** (0.0%)
- ✨ v0.7 canonical 升級: **12** (12.4%)
- ⚙ 階段 2.5 Read-Aloud self-fix: **4** (4.1%) — 已直接應用 v3 · 詳見 self-audit log

---

## 🎯 使用者決策方式

對每項 diff：
- **A** = 保留 shipped
- **B** = 採用 v3（依推薦）
- **C** = 客製化（請說明）

批次快答格式：
```
🟡 全 A · 🟠 全依推薦（B）· 🔴 逐項挑
✨ 全 B
例外覆蓋: #6=B #35=B #97 sub-item 3=C(黑衣人保留)
```

---

## 🟢 完全相同（8 tokens · 無需決策）

- `ARILOU_HINTS_4`
- `bye_friendly_space`
- `what_about_war`
- `WICKED_HUMAN`
- `what_do_about_tpet`
- `bye_friendly_homeworld`
- `lets_fight`
- `bye_angry_space`

---

## ✨ v0.7 canonical 升級 · 12 tokens

**shipped 用舊 canonical / 缺 canonical · v3 已升級對齊 Master_Glossary 或 dossier v0.7** · 強烈推薦 B

### #3 · `CONFUSED_RESPONSE` · ✨ Q1=A voice reform + ✨ 恩澤伐特 canonical + ✨ Celts 首介英文

**EN**:
```
I forget myself. Of course you don't know me. You are from Unzervalt, not Earth.
We are, however, how shall I say, related.
It has been many of your years since I have been to our planet Earth.
We are known among your kind by many names... some of them flattering, some of them not.
The one we use most often was given to us by the children of the Celts. A wonderful culture!
They called us the Arilou... the Arilou Lalee'lay.
More recently we were part of the Alliance of Free Stars, along with your kind
until we decided to return to our own....oh, how would you say... reality
when it became clear that your people would be safe enough under the Ur-Quan slave shield.
```

**Shipped**:
```
是我忘記自己了。 你當然不認識我。 你來自溫澤瓦特，不是地球。
然而，我方…… 該怎麼說呢，是有淵源的。
距我上次到訪我方的地球，已過了你們許多年。
我方在你們一族之中有許多名字…… 有些讚美，有些不然。
我方最常用的那個名字，是凱爾特的孩子們給的。 多麼美妙的文化！
他們稱我方為阿麗露…… 阿麗露·萊蕾 （Arilou Lalee'lay）。
較近期，我方曾與貴族同為自由星系聯盟的一員
直到我方決定回歸我方自己的…… 喔，該怎麼形容呢…… 現實
當我方見到你們一族在烏寬奴役護盾下能夠安全無虞的時候。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
是我忘了自己。 你當然不認識我。 你來自恩澤伐特，不是地球。
不過，我們……該怎麼說呢，是有淵源的。
距我上次造訪我們的地球，你們算來已過了許多年。
在你們一族之中，我們有著許多名字…… 有些是讚美，有些則不然。
我們最常用的那個名字，是凱爾特人（Celts）的孩子們送給我們的。 多麼美好的文化！
他們稱我們為阿麗露…… 阿麗露·萊蕾（Arilou Lalee'lay）。
不久之前，我們曾與你們一族同為自由星系聯盟的一員
直到我們決定回歸我們自己的……喔，你們會怎麼形容呢…… 現實
那時已經看清，你們的族人在烏寬奴役護盾之下能夠安全無虞。
```

**推薦**: ✨ **B** — ✨ Master_Glossary v0.2 §4 canonical: 溫澤瓦特→**恩澤伐特** · ✨ Q4=A UFO 迷因 canonical: 凱爾特→凱爾特人（Celts）· Q1=A 我方 6 處→我們 · 「阿麗露·萊蕾」全形括號→半形括號 gloss（v3 移除全形空格）。

**你的選擇**: A / B / C(自訂)

---

### #8 · `FRIENDLY_SPACE_HELLO_1` · ✨ Q1=A voice + ✨ 恩澤伐特 + ✨ Falayalaralfali 首介英文

**EN**:
```
Ah... our human friend. Please, let us chat a while.
It has been so many years since I last visited your Earth
so long since I glided across your open fields under the light of a full moon.
Tell me of Earth. Tell me what I have... oh, I forget myself... how silly.
You were born on the distant world Unzervalt.
I have visited there much more recently.
```

**Shipped**:
```
啊…… 我方的人類朋友。 請，讓我方聊一會兒。
距我上次造訪你們地球已這麼多年
那麼久沒在滿月下滑過你們的曠野了。
跟我說說地球。 告訴我我曾…… 喔，我又忘了自己…… 真傻。
你出生在遙遠的溫澤瓦特。
我最近去過那裡。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
啊…… 我們的人類朋友。 來，讓我們聊一會吧。
距我上次造訪你們地球，已經過了這麼多年
距我在滿月之下滑過你們遼闊的田野，也已過了這麼久。
跟我說說地球吧。 告訴我我曾經…… 喔，我又忘了自己…… 真是傻。
你出生在遙遠的恩澤伐特（Unzervalt）。
最近一次我倒是去過那裡。
```

**推薦**: ✨ **B** — ✨ Master_Glossary canonical: 溫澤瓦特→**恩澤伐特（Unzervalt）** + 英文首介 · Q1=A 我方 2 處→我們 · v3「滿月之下滑過你們遼闊的田野」對應 "glided across your open fields under the light of a full moon" 更飄渺 · self-fix: 兒→無（一會兒→一會 TW natural）。

**你的選擇**: A / B / C(自訂)

---

### #12 · `FRDLY_HOMEWORLD_HELLO_1` · ✨ Q1=A + ✨ 真實空間（TrueSpace） + ✨ Falayalaralfali 英文首介

**EN**:
```
Ha-ha! Our clever ward has found our nook in *time*!
You are the first, brave human! No others have made the trip.
This is our homeworld, Falayalaralfali, nestled safe in this TrueSpace eddy.
The portal you passed through is a rarity, a natural point of interdimensional fatigue.
We use these phenomena to speed our transit through the realities.
We are wondering, have you met with the Umgah recently?
We entrusted an injured Talking Pet into their care
and we were curious about its progress.
```

**Shipped**:
```
哈哈！ 我方聰明的門徒找到了我方在 *時* 中的隱居處！
你是第一個，勇敢的人類！ 沒有別人做過這趟旅程。
這是我方的母星，法拉雅拉拉法利 （Falayalaralfali），安穩地窩在這處真空間漩渦中。
你通過的傳送門很罕見，是次元疲勞的自然點。
我方利用這些現象加速穿越現實之間的移動。
我方好奇，你最近見過陰嘎族嗎？
我方託付了一隻受傷的會話寵給他們照料
對牠的狀況我方十分好奇。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
哈哈！ 我們聰明的受託之孩找到了我們在 *時* 中的角落！
你是第一個，勇敢的人類！ 沒有其他人做過這趟旅程。
這是我們的母星，法拉雅拉拉法利（Falayalaralfali），安穩地嵌在這道真實空間（TrueSpace）的漩渦之中。
你所穿越的那扇傳送門非常罕見，是一處自然生成的次元疲勞節點。
我們利用這類現象來加速穿越諸現實之間的旅程。
我們正在好奇—— 你最近見過陰嘎族嗎？
我們曾託付一隻受傷的會話寵給他們照料
對牠的狀況我們始終掛心。
```

**推薦**: ✨ **B** — ✨ Master_Glossary L246 canonical: **真空間→真實空間（TrueSpace）** + 英文首介 · Q1=A 我方 4 處→我們 · v3「聰明的受託之孩找到了我們在 *時* 中的角落」對應 "clever ward has found our nook in *time*" 較 shipped「隱居處」貼原文 nook（角落）· 「始終掛心」對應 "curious about its progress" 較 shipped「十分好奇」溫柔。

**你的選擇**: A / B / C(自訂)

---

### #19 · `GENERAL_INFO_2` · ✨ Q1=A + ✨ 麥田圈 canonical

**EN**:
```
You have painted our pictures on cave walls, erected standing stones and pyramids for us.
You have wondered at our signs to each other in your wheat fields
and written books about our more personal endeavors
when we allowed you to recall our examinations.
We have a history together, Captain, and you have come a long way.
But I must tread carefully. You are not ready for everything
and I fear that you would not understand what was best for you.
```

**Shipped**:
```
你們曾在洞穴牆上畫下我方的形象，為我方立起巨石與金字塔。
你們曾對我方在你們麥田中留下的相互記號感到好奇
並曾為我方較私人的事跡寫下書籍
當我方允許你們回想起我方對你們的檢查時。
我方共同擁有一段歷史，艦長，你已走過漫長的路。
但我必須謹慎前行。 你尚未準備好接受一切
我擔心你會不理解什麼才對你最好。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們曾在洞穴的牆上繪下我們的圖像，為我們立起巨石陣與金字塔。
你們曾對我們在你們麥田圈中留給彼此的訊號感到好奇
也曾為我們較私人的行動寫下書籍
——當我們允許你們回想起我們對你們的檢查時。
我們共同擁有一段歷史，艦長，你已走過漫長的路。
但我必須小心前行。 你尚未準備好接受一切
我擔心你不會理解什麼才對你最好。
```

**推薦**: ✨ **B** — ✨ Q6=A dossier canonical: shipped「麥田中留下的相互記號」→ v3「**麥田圈**中留給彼此的訊號」（UFO 迷因 canonical 保留）· Q1=A 我方 5 處→我們 · v3「巨石陣」對應 "standing stones" 較 shipped「巨石」貼 UFO 迷因（Stonehenge canonical）。

**你的選擇**: A / B / C(自訂)

---

### #52 · `ABOUT_WAR` · ✨ Q1=A + ✨ Falayalaralfali/Delta Gorno 首介英文格式統一

**EN**:
```
Forgive us if we forget the importance you attach to such events as this.
Our... context, is infinitely broader than yours in scope, both in space and *time*.
Nevertheless, to please you I shall try to recall.
Yes, now I remember. Here is the sequence:
The Ur-Quan fleets have moved through your solar system and you are defeated.
Your people make the choice not to fight with and for the Ur-Quan.
A shield is cast about your world. Your people are now safe. This makes us happy.
The Armada departs your star system and moves toward the remaining Alliance members
ourselves, the Syreen, the Yehat and their adopted Shofixti.
The Yehat and Shofixti withdraw to <% comm.getStarName("Delta Gorno", "shofixti") %>, but they do not permit the Syreen to follow.
We are content with the flow of events and leave the area to return here.
From our perspective, this sequence of events ends here.
```

**Shipped**:
```
請原諒我方若忘了你們對這類事件所賦予的重要性。
我方的…… 脈絡，在空間與 *時* 上都比你們的無限廣大。
然而為了取悅你，我會嘗試回想。
是的，我現在想起來了。 順序是這樣的:
烏寬族艦隊已穿過你們的太陽系，你們戰敗。
你們族人選擇不與、也不為烏寬族而戰。
奴役護盾罩住了你們的世界。 你們族人如今安全。 這讓我方欣慰。
艦隊離開你們的星系，前往剩下的聯盟成員
我方、塞蓮族、翼哈特族與他們收養的修烈士族。
翼哈特族與修烈士族撤退至 <% comm.getStarName("戈爾諾δ", "shofixti") %> （Delta Gorno），但他們不允許塞蓮族跟隨。
我方對事件的發展感到滿意，離開該區回到此處。
從我方的視角，這系列事件到此結束。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
請原諒我們，若我們遺忘了你們對這類事件所賦予的重要性。
我們的……脈絡，在空間與 *時* 之上都比你們的無限廣大。
儘管如此，為了讓你滿意，我會試著回想。
是的，我現在想起來了。 順序是這樣的：
烏寬族的艦隊穿越了你們的太陽系，你們戰敗。
你們的族人選擇不與烏寬族交戰、也不為烏寬族而戰。
一道護盾罩住了你們的世界。 你們的族人如今安全了。 這令我們欣慰。
艦隊離開了你們的星系，向剩餘的聯盟成員推進
我們自己、塞蓮族、翼哈特族與他們收養的修烈士族。
翼哈特族與修烈士族撤退至 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno），但他們不允許塞蓮族跟隨。
我們對事件的走向感到滿足，離開了那片區域回到這裡。
從我們的視角，這一連串事件就在這裡告終。
```

**推薦**: ✨ **B** — ✨ Q8=A 星名首介格式統一：shipped「戈爾諾δ （Delta Gorno）」全形空格→ v3「戈爾諾δ（Delta Gorno）」（無全形空格 · dossier §五 canonical）· Q1=A 我方 5 處→我們 · 「向剩餘的聯盟成員推進」較 shipped「前往剩下的聯盟成員」較貼「Armada departs and moves toward」。

**你的選擇**: A / B / C(自訂)

---

### #54 · `ABOUT_URQUAN` · ✨ ✨ 教義戰爭 canonical + 首介英文格式

**EN**:
```
Soon after the Ur-Quan defeated the Yehat and imprisoned the Syreen in <% comm.getStarName("Betelgeuse", "syreen") %>...
...their siblings arrived to initiate the Doctrinal Conflict.
This battle continues as we speak.
```

**Shipped**:
```
烏寬族擊敗翼哈特族並把塞蓮族囚禁於 <% comm.getStarName("參宿四", "syreen") %> （Betelgeuse） 不久後……
……他們的兄弟族抵達，展開教義衝突。
此戰至今仍在進行。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
烏寬族擊敗翼哈特族並將塞蓮族囚禁於 <% comm.getStarName("參宿四", "syreen") %>（Betelgeuse）不久之後……
……他們的兄弟族抵達，展開了教義戰爭。
這場戰役至今仍在進行。
```

**推薦**: ✨ **B** — ✨ Q9=A **Master_Glossary L280 canonical**: shipped「教義衝突」→ v3「教義戰爭」（v0.2 對齊 Kzer-Za/Kohr-Ah/Chmmr shipped 全 5 族 canonical）· ✨ 「參宿四 （Betelgeuse）」全形空格→無全形空格。

**你的選擇**: A / B / C(自訂)

---

### #67 · `UMGAH_UNDER_COMPULSION` · ✨ Q1=A + ✨ Beta Orionis 首介英文格式

**EN**:
```
We have discovered something strange and frightening about the Umgah
When we approached their vessels, we were instantly attacked
and the Umgah made no attempts to contact our ships or respond to our hails.
Using our own psionic sensitivities, we determined that they are under some form of psychic compulsion.
The source of psionic control commands appears to be <% comm.getStarName("Beta Orionis", "talking pet") %>, the Umgah's home star.
We sent vessels to investigate this location, but none have returned... we fear they are destroyed.
```

**Shipped**:
```
我方對陰嘎族發現了奇怪又可怕的事
當我方接近他們的艦艇時，我方立刻遭到攻擊
陰嘎族沒有嘗試與我方艦艇聯繫，也沒回應我方的呼叫。
運用我方自身的心靈感應能力，我方判定他們正受某種精神控制。
心靈控制指令的源頭似乎是 <% comm.getStarName("獵戶座β", "talking pet") %> （Beta Orionis），陰嘎族的母星系。
我方派了艦艇去該處調查，但無一返航…… 我方擔心他們已被摧毀。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們對陰嘎族發現了既奇怪又可怕的事情
當我們接近他們的艦艇時，我們立刻遭到攻擊
而陰嘎族並未嘗試與我們的艦艇聯繫，也未回應我們的呼叫。
運用我們自身的心靈感應能力，我們判定他們正處在某種形式的精神脅迫之下。
心靈控制指令的來源，看來是 <% comm.getStarName("獵戶座β", "talking pet") %>（Beta Orionis），陰嘎族的母星系。
我們派了艦艇前往那處調查，但無一返航…… 我們擔心他們已被摧毀。
```

**推薦**: ✨ **B** — ✨ Q8=A 星名首介格式統一：「獵戶座β （Beta Orionis）」全形空格→無全形空格 · Q1=A 我方 5 處→我們 · 「脅迫」/「精神控制」對應 "compulsion" 皆通 · 「來源」/「源頭」對應 "source" 皆通。

**你的選擇**: A / B / C(自訂)

---

### #69 · `GO_FIND_OUT` · ✨ Q1=A + ✨ Beta Orionis 首介英文

**EN**:
```
We have had no success with our own investigations.
Whatever controls the Umgah is a threat, but we seem unprepared to deal with it.
Perhaps you and your crew are better suited to this mission.
If you choose to go to <% comm.getStarName("Beta Orionis", "talking pet") %>, take care, child.
Whatever controls the Umgah now knows of our presence
and it may take measures against us.
```

**Shipped**:
```
我方自身的調查毫無進展。
控制陰嘎族的無論何物皆是威脅，但我方似乎沒有能力應付。
或許你與你的船員更適合這項任務。
若你選擇前往獵戶座β，請小心，親愛的孩子。
如今控制陰嘎族之物已知曉我方存在
它可能會對我方採取行動。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們自己的調查毫無成果。
無論是何物在控制陰嘎族，那都是一種威脅，但我們似乎無力應付。
或許你和你的船員更適合這項任務。
若你選擇前往 <% comm.getStarName("獵戶座β", "talking pet") %>（Beta Orionis），請小心，我親愛的孩子。
如今控制陰嘎族的那個東西已經察覺我們的存在
它可能會對我們採取行動。
```

**推薦**: ✨ **B** — ✨ Q8=A shipped「獵戶座β」缺英文首介 → v3「<% ... %>（Beta Orionis）」補英文首介 · Q1=A 我方 2 處→我們 · 「察覺我們的存在」較 shipped「知曉我方存在」自然。

**你的選擇**: A / B / C(自訂)

---

### #75 · `ABOUT_PORTAL` · ✨ Q1=A + ✨ HyperSpace/QuasiSpace 首介英文

**EN**:
```
As you know, we live in a dimension adjacent to HyperSpace which we call QuasiSpace.
Our ships move between these dimensions through weaknesses in the inter-dimensional fabric.
Although many such weaknesses, or Portals, exist which lead from our dimension, QuasiSpace
to various locations in HyperSpace, there is only one naturally occurring Portal
which will transport a ship from HyperSpace to QuasiSpace.
We therefore find it convenient to generate our own Portals artificially
with focused dimensional fatigue rays.
As a sign of our long-standing relationship with your species
we would happily fit your vessel with a Portal Spawner of its own
but your ship is so massive, our units would be ineffective. However
we suspect you may find a sufficiently powerful warp pod, the key element in a Portal Spawner
in the wreck of the Ur-Quan Dreadnought on the seventh world at <% comm.getStarName("Alpha Pavonis", "urquan wreck") %>.
Bring that warp pod back here, and we will prepare a Portal Spawner for your vessel.
```

**Shipped**:
```
如你所知，我方居於一個與超空間相鄰的次元，我方稱之為準空間 （QuasiSpace）。
我方的艦艇透過次元織理的薄弱處在這些次元間移動。
儘管有許多這類薄弱處，或稱傳送門，能從我方的次元準空間
通往超空間中的各個位置，只有一個天然生成的傳送門
能將艦艇從超空間送往準空間。
因此我方發現以人工方式生成我方自己的傳送門較為便利
藉由聚焦的次元疲勞射線。
作為我方與你們一族長久友誼的表徵
我方樂於為你的艦艇裝設專屬的傳送門生成器
但你的艦艇如此巨大，我方的機組會無效。 然而
我方懷疑你可能會找到足夠強大的曲速艙，那是傳送門生成器的關鍵元件
就在 <% comm.getStarName("孔雀座α", "urquan wreck") %> （Alpha Pavonis） 第七顆世界上的烏寬無畏艦殘骸。
把那顆曲速艙帶回這裡，我方就會為你的艦艇準備一套傳送門生成器。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
如你所知，我們居於一個與超空間（HyperSpace）比鄰的次元，我們稱之為準空間（QuasiSpace）。
我們的艦艇穿越這些次元，是透過次元織理之間的薄弱之處。
雖然存在許多這類薄弱點，或稱傳送門，能從我們的次元、準空間
通往超空間中的各種位置，但只有一扇天然生成的傳送門
能把艦艇從超空間送往準空間。
因此，我們覺得以人工方式生成我們自己的傳送門較為方便
藉由聚焦的次元疲勞射線。
作為我們與你們一族長久情誼的一個象徵
我們樂於為你的艦艇裝配一具屬於它自己的傳送門生成器
但你的艦艇如此龐大，我們的機組不會奏效。 然而
我們懷疑你可能找得到一顆足夠強大的曲速艙—— 那是傳送門生成器的關鍵零件
就在 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）第七顆世界上的烏寬無畏艦殘骸之中。
把那顆曲速艙帶回這裡，我們就會為你的艦艇準備好一具傳送門生成器。
```

**推薦**: ✨ **B** — ✨ Q8=A shipped「超空間」/「準空間 （QuasiSpace）」→ v3「超空間（HyperSpace）」+「準空間（QuasiSpace）」（三者首介英文一次 · 統一維度地名 icon）· Q1=A 我方 7 處→我們 · 「比鄰」/「相鄰」皆通 · 「一具屬於它自己的傳送門生成器」對應 "a Portal Spawner of its own" 貼原文 of its own。

**你的選擇**: A / B / C(自訂)

---

### #77 · `ABOUT_TPET` · ✨ Q1=A + ✨ Alpha Pavonis 首介英文格式

**EN**:
```
We are an endlessly curious species, and we spend much of our time on
how should I say, reconnaissance missions.
During one such trip, we witnessed the crash landing of an Ur-Quan Dreadnought
on the surface of <% comm.getStarName("Alpha Pavonis", "urquan wreck") %> VII.
Normally, when an Ur-Quan vessel is disabled, it automatically engages self-annihilation circuits
to prevent other species from learning the Ur-Quan's technological secrets.
In this case, however, these circuits must have failed. The Dreadnought did not disintegrate on impact.
We landed to explore the wreckage, and were amazed to find a survivor... a Talking Pet!
As you may know, the Ur-Quan use these non-sentient creatures for the task of inter-species translation
a task the Ur-Quan find ultimately demeaning.
The Talking Pet was severely injured, and we did what we could for the poor creature
but it grew clear that without superior measures, the Talking Pet would die.
We turned to the Umgah, whom we have known for many centuries.
Their bioscience skills are far superior to our own.
The Umgah promised to do what they could, and let us know how the Pet fared.
We have not heard from the Umgah since.
Perhaps, if you are travelling through their stars, you can ask them for us.
```

**Shipped**:
```
我方是個無止盡好奇的物種，我方大部分時間都花在
該怎麼說呢，偵察任務上。
某次這樣的行程中，我方目擊一艘烏寬無畏艦墜毀
在孔雀座α （Alpha Pavonis） VII 表面。
通常烏寬艦艇失去功能時，會自動啟動自毀電路
以防其他物種學會烏寬族的科技秘密。
然而此案例中，這些電路必然失效了。 無畏艦撞擊時未解體。
我方登陸探索殘骸，驚訝地發現一位倖存者…… 一隻會話寵！
如你所知，烏寬族用這些非智慧生物從事跨物種翻譯的工作
這任務烏寬族自己覺得極為屈辱。
那會話寵傷勢嚴重，我方盡力照料這可憐的生物
但清楚可見的是若無更高階手段，這會話寵會死。
我方轉向陰嘎族，我方認識他們數個世紀了。
他們的生物科學技術遠優於我方。
陰嘎族承諾盡力而為，並讓我方知悉那寵的狀況。
自此以來我方沒再收到陰嘎族的消息。
或許，若你穿越他們的星域，你能替我方問問他們。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們是個無止盡好奇的物種，我們大部分的時光都花在
——該怎麼說呢，偵察任務上。
在一次這樣的行程之中，我們目擊了一艘烏寬無畏艦墜毀
就在 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）VII 的地表。
通常來說，當烏寬艦艇失去功能時，它會自動啟動自毀電路
以防其他物種學會烏寬族的科技秘密。
然而在這次的情況中，這些電路必然失效了。 無畏艦撞擊時並未解體。
我們著陸探索殘骸，驚訝地發現一位倖存者…… 一隻會話寵！
如你所知，烏寬族用這些非智慧生物從事跨物種翻譯的工作
而這項工作，烏寬族自己覺得極為屈辱。
那會話寵傷勢嚴重，我們盡力照料這隻可憐的生物
但情況清楚地顯示—— 若無更高階的手段，這隻會話寵就會死。
我們轉而尋求陰嘎族的幫助，我們認識他們已有數個世紀之久。
他們的生物科學技術遠優於我們自己。
陰嘎族承諾會盡其所能，並讓我們知悉那寵的狀況。
自那時起，我們就沒再收到陰嘎族的消息。
或許，若你穿越他們的星域，你能替我們問問他們。
```

**推薦**: ✨ **B** — ✨ Q8=A 星名首介格式統一：「孔雀座α （Alpha Pavonis）」全形空格→ v3「<% ... %>（Alpha Pavonis）」（無全形空格 + Lua template 保留）· Q1=A 我方 8 處→我們 · 「數個世紀之久」對應 "many centuries" 較 shipped「數個世紀了」貼原文 · 「盡其所能」/「盡力而為」皆通。

**你的選擇**: A / B / C(自訂)

---

### #79 · `PORTAL_AGAIN` · ✨ Q1=A + ✨ Alpha Pavonis Lua template + 首介英文

**EN**:
```
Certainly. As a sign of our long-standing friendship with your species
we would be happy to fit your vessel with a Portal Spawner
allowing you to jump from place to place in HyperSpace, without travelling the intervening distance.
However, your ship is so massive, our normal warp pod units are insufficient
but you will find a sufficiently powerful warp pod in the wreck of the Ur-Quan Dreadnought
on <% comm.getStarName("Alpha Pavonis", "urquan wreck") %> VII. Bring that warp pod back here, and we will prepare a Portal Spawner for your vessel.
```

**Shipped**:
```
當然。 作為我方與你們一族長久友誼的表徵
我方樂於為你的艦艇裝設傳送門生成器
讓你能在超空間中從一處跳躍到另一處，無需經過中間的距離。
然而，你的艦艇如此巨大，我方標準的曲速艙機組不足以應付
但你可以在 <% comm.getStarName("孔雀座α", "urquan wreck") %> （Alpha Pavonis） VII 的烏寬無畏艦殘骸中
找到足夠強大的曲速艙。 把那顆曲速艙帶回這裡，我方會替你的艦艇準備一套傳送門生成器。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
當然可以。 作為我們與你們一族長久友誼的一個象徵
我們樂於為你的艦艇裝配一具傳送門生成器
讓你能夠在超空間中從一處跳到另一處，無需真的走過那段距離。
然而，你的艦艇如此龐大，我們一般的曲速艙機組並不足以應付
但你將在 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）VII 的烏寬無畏艦殘骸中
找到一顆足夠強大的曲速艙。 把那顆曲速艙帶回這裡，我們就會為你的艦艇準備好一具傳送門生成器。
```

**推薦**: ✨ **B** — ✨ Q8=A 星名 Lua template：shipped 直接寫「<% comm.getStarName("孔雀座α", "urquan wreck") %> （Alpha Pavonis）」→ v3 同格式但無全形空格 · Q1=A 我方 3 處→我們 · 「走過那段距離」對應 "travelling the intervening distance" 較 shipped「經過中間的距離」貼原文。

**你的選擇**: A / B / C(自訂)

---

### #97 · `OUT_TAKES` · ✨ ✨ UFO 迷因 canonical 全補 + Q4=A 台灣電影名

**EN**:
```
Do you really believe Project Bluebook revealed EVERYTHING the Army Air Corps knew?
Do you know what REALLY happened at Roswell, New Mexico in the late 1940's?
Have you even heard about the Men in Black?
Do you have any friends who have `missing days'?
Do you sleep with your window unlocked?
Be seeing you...
```

**Shipped**:
```
你真的相信藍皮書計畫揭露了陸軍航空隊所知的『一切』嗎？
你知道 1940 年代末新墨西哥州羅斯威爾『真正』發生了什麼嗎？
你聽過黑衣人嗎？
你有沒有朋友『失蹤過幾天』？
你睡覺時窗戶開著嗎？
再見……
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你真的相信藍皮書計畫（Project Bluebook）揭露了美國陸軍航空隊所知的『一切』嗎？
你知道 1940 年代末，在新墨西哥州的羅斯威爾（Roswell）『真正』發生了什麼嗎？
你甚至有沒有聽過那些 MIB 星際戰警（Men in Black）？
你身邊有沒有那種擁有『失憶的日子』（missing days）的朋友？
你睡覺的時候，會不會鎖上你的窗戶？
我們會再見的……（Be seeing you...）
```

**推薦**: ✨ **B** — **✨ 招牌 OUT_TAKES 全補 canonical (v0.7 dossier §六 例 1)**：

1. ✨ **Q4=A + freetext**: `Men in Black` → **MIB 星際戰警（Men in Black）**（1997 台灣譯名 · 使用者 freetext 指定）· shipped「黑衣人」廢除
2. ✨ **Q4=A**: `Project Bluebook` → 藍皮書計畫（**Project Bluebook**）· shipped 缺英文首介
3. ✨ **Q4=A**: `Roswell, New Mexico` → 新墨西哥州的**羅斯威爾（Roswell）**· shipped 缺英文首介
4. ✨ **Q6=A**: `missing days` → 『**失憶的日子**』（**missing days**）· shipped「失蹤過幾天」（UFO 綁架迷因意譯偏差）廢除
5. ✨ **Q5=A dossier canonical**: `Be seeing you...` → **我們會再見的……（Be seeing you...）**· shipped「再見……」（弱化為普通道別 · 失去 The Prisoner gag）廢除
6. 補「美國陸軍航空隊」對應 "Army Air Corps" 較 shipped「陸軍航空隊」明確
7. 「你睡覺的時候，會不會鎖上你的窗戶」對應 "Do you sleep with your window unlocked" 較 shipped「你睡覺時窗戶開著嗎」貼原文 unlocked（鎖）

**這是本次 Rebuild-Compare 最重要的招牌 icon 修訂 · 招牌 UFO 迷因 canonical 完全還原**。

**你的選擇**: A / B / C(自訂)

---

## 🟠 措辭改變 · 50 tokens

**主要為 Q1=A 我方→我/我們 voice reform + Q12=A 妳→你** · 皆依 dossier v0.7 canonical 與 Q&A 決策 · 推薦 B（v3）

### #2 · `confused_by_hello` · 🟠 Q1=A 我方→我們 + Q12=A 妳→你

**EN**:
```
You sound as if you know me. Have we met?
```

**Shipped**:
```
妳說話像認識我。 我方見過嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你說話像是認識我。 我們見過嗎？
```

**推薦**: 🟠 **B** — Q1=A shipped「我方見過嗎？」→ v3「我們見過嗎？」（個體遇見 · 非 Alliance 政治） + Q12=A shipped「妳說話」→ v3「你說話」（中性 · 對齊其他外星族 shipped canonical）。

**你的選擇**: A / B / C(自訂)

---

### #4 · `happy_by_hello` · 🟠 Q1=A + Q12=A

**EN**:
```
I know who you are! You're Arilou!! We've wondered what happened to your people for a long time.
```

**Shipped**:
```
我知道妳是誰！ 妳是阿麗露！！ 我方一直好奇你們一族後來如何了。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我知道你是誰！ 你就是阿麗露！！ 我們好久以來一直好奇你們一族後來怎麼了。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 + Q12=A 妳→你 · v3「好久以來一直好奇」對應 "wondered for a long time" 保留原文 for a long time 語感。

**你的選擇**: A / B / C(自訂)

---

### #5 · `HAPPY_RESPONSE` · 🟠 Q1=A voice reform

**EN**:
```
You are very clever!
Yes, I am Arilou Lalee'lay and I suppose it has been a very long time since you've met one of my kind.
I imagine you humans are still very short lived. How sad.
Ah well. To answer your question, we chose to cease our efforts with the Alliance of Free Stars
when it seemed that there was no longer any threat to our Earthlings.
I am pleased to see that you, from outside the slave shield, survived. You seem healthy.
```

**Shipped**:
```
你真聰明！
是的，我是阿麗露·萊蕾，我猜距你上次遇到我這一族已很久了。
我想你們人類仍是短命的物種。 多麼令人惋惜。
啊，好吧。 回答你的問題，我方選擇停止在自由星系聯盟的活動
是因為那時似乎已不再有威脅我方地球人的東西了。
我很高興看到你，來自奴役護盾之外，還活著。 你看起來很健康。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你真聰明！
是的，我就是阿麗露·萊蕾，我猜距你上次遇見我這一族，已經是很久很久以前的事了。
我想你們人類還是那麼短命。 多麼令人惋惜。
嗯，好吧。 回答你的問題—— 我們選擇停止在自由星系聯盟裡的努力
是因為那時看來，我們的地球人已不再面對任何威脅了。
我很高興看到你，從奴役護盾之外，仍然活著。 你看起來很健康。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們（2 處）· 語序微調（「已很久了」→「已經是很久很久以前的事了」對應 "very long time" 疊字加強）· 「短命的物種」→「還是那麼短命」更口語。

**你的選擇**: A / B / C(自訂)

---

### #7 · `MIFFED_RESPONSE` · 🟠 Q1=A voice reform

**EN**:
```
You're annoyed. How interesting.
It has been so long since I dealt with Humans. I had forgotten what it was like.
Now let's see, how shall I best appease you? Yes, if I remember, an honest answer would help.
We didn't exactly `run out' on the Alliance.
We chose to leave when there was no longer a reason to stay.
You humans seemed safe enough under the Ur-Quan slave shield.
In fact, we rather liked the idea and wished we had thought of it ourselves.
For your safety of course.
```

**Shipped**:
```
你惱火了。 多有意思。
我方好久沒跟人類打交道了。 我都忘了那是什麼感覺。
來看看，該怎麼撫平你才好？ 對了，我記得了，坦誠的回答會有幫助。
我方並非真的『離開』聯盟。
我方選擇離開，是因為沒有留下的理由了。
你們人類在烏寬奴役護盾下似乎足夠安全。
事實上，我方相當欣賞那想法，還希望自己也想到過。
當然是為了你們的安全。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你惱火了。 多麼有趣。
我已經好久沒跟人類打交道了。 我都忘了那是什麼樣的感覺。
來想想看，該怎麼撫平你才好？ 對了，我記起來了，坦誠的回答會有幫助。
我們並不是真的『拋下』了聯盟。
我們選擇離開，是因為已經沒有留下的理由了。
你們人類在烏寬奴役護盾之下看來已足夠安全。
事實上，我們相當欣賞那個點子，只希望是我們自己想到的。
當然，這一切都是為了你們的安全。
```

**推薦**: 🟠 **B** — Q1=A 我方 4 處→我 / 我們 · 「拋下」對應 "run out on" 較直譯 · shipped「離開」較弱。

**你的選擇**: A / B / C(自訂)

---

### #9 · `FRIENDLY_SPACE_HELLO_2` · 🟠 Q1=A + 招牌詩意升級

**EN**:
```
Hello my clever child. We have met again and I am pleased.
Your people are so beautiful... so unspoiled.
Your instincts are like perfume... your motives a shimmering crystal.
```

**Shipped**:
```
哈囉，我親愛的聰明孩子。 我方又相遇了，我很高興。
你的族人如此美麗…… 如此純真。
你們的本能像香氛…… 你們的動機像閃爍的水晶。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
哈囉，我親愛的聰明孩子。 我們又相遇了，我很高興。
你們的族人如此美麗…… 如此純真未染。
你的本能宛如香氣…… 你的動機宛如閃爍的水晶。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · v3「純真未染」對應 "unspoiled" 較 shipped「純真」貼原文 · 「宛如香氣/閃爍的水晶」對應 "like perfume/shimmering crystal" 較 shipped「像香氛/像閃爍的水晶」文雅 · 招牌 UFO 玄學讚美詩意 icon 升級。

**你的選擇**: A / B / C(自訂)

---

### #11 · `FRIENDLY_SPACE_HELLO_4` · 🟠 Q1=A 我方→我們

**EN**:
```
Did you desire this meeting, Captain, or did we?
```

**Shipped**:
```
艦長，是你渴望這次相會，還是我方？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
艦長，是你渴望這次相會，還是我們？
```

**推薦**: 🟠 **B** — Q1=A shipped「我方」→ v3「我們」個體 voice。

**你的選擇**: A / B / C(自訂)

---

### #13 · `FRDLY_HOMEWORLD_HELLO_2` · 🟠 Q1=A voice reform

**EN**:
```
Welcome back to Falayalaralfali, Captain.
Perhaps, in the fullness of time we will let you visit the surface of our world.
There are many beauties here unmatched anywhere... the Mountain Clouds of Thought
the Tangible Wish... the Dark. Unfortunately, you are not yet... acclimated.
Premature exposure to these would render you... numb.
```

**Shipped**:
```
歡迎回到法拉雅拉拉法利，艦長。
也許某日時機成熟時，我方會讓你參觀我方世界的地表。
這裡有無處可比擬的許多美景…… 思念之雲山
具形之願…… 幽暗。 只可惜，你尚未…… 適應。
過早接觸這些會使你…… 麻痺。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
歡迎回到法拉雅拉拉法利，艦長。
或許某一天，時機成熟之時，我們會讓你參觀我們世界的地表。
這裡有無處可及的許多美景…… 思念之雲山
具形之願…… 幽暗。 只可惜，你尚未……適應。
過早接觸這些景物，會令你……麻痺。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · v3 微調「時機成熟之時」/「無處可及」/「景物，會令你」較 shipped 順口。

**你的選擇**: A / B / C(自訂)

---

### #18 · `GENERAL_INFO_1` · 🟠 Q1=A voice reform

**EN**:
```
You are curious. That is a promising quality.
How can I describe our relation to Humans?...
Never doubt our motives, Captain. Your well-being is of paramount concern to every Arilou.
Surely you know, that it was the day after Humanity joined the Alliance Of Free Stars
that we appeared in the open for the first time. This was no coincidence.
We wanted to protect you. Once we saw that you were...well, safe
we decided to tend to other business for a short while.
Believe me, Captain, we have known each other for a very long time.
You might even say that we knew the first human.
```

**Shipped**:
```
你充滿好奇。 這是難得的品質。
該怎麼描述我方與人類的關係呢……
請絕不要懷疑我方的動機，艦長。 你的安好是每一位阿麗露最關心的事。
你肯定知道，人類加入自由星系聯盟的隔日
我方就首次公開現身。 這絕非巧合。
我方想保護你們。 當我方看到你們……嗯，安全了
就決定去處理其他事情一陣子。
相信我，艦長，我方認識彼此已非常非常久了。
甚至可以說，我方認識了第一個人類。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你充滿好奇。 這是一項難得的品質。
我該怎麼描述我們與人類的關係呢？……
永遠不要懷疑我們的動機，艦長。 你的安好，是每一位阿麗露最放在心上的事。
你必然知道，就在人類加入自由星系聯盟的隔日
我們才首次公開現身。 這絕非巧合。
我們想保護你們。 當我們看見你們……嗯，安全了
我們就決定去處理其他事情一陣子。
相信我，艦長，我們認識彼此已經非常、非常久了。
你甚至可以說，我們認識了第一個人類。
```

**推薦**: 🟠 **B** — Q1=A 我方 6 處→我們 · v3「你必然知道」對應 "Surely you know" 較 shipped「你肯定知道」略正式 · 「非常、非常久」保留 "very very long" 疊字節奏 · 「你的安好，是每一位阿麗露最放在心上的事」較 shipped「最關心的事」溫柔（放在心上/掛心）。

**你的選擇**: A / B / C(自訂)

---

### #20 · `GENERAL_INFO_3` · 🟠 Q1=A voice reform

**EN**:
```
As you know, we never revealed where in the galaxy one could find our homeworld.
There was a good reason. We are not from your space, or your... *time*.
Some of your more broad thinkers refer to such realms as other dimensions.
Though trivialized, this is a suitable metaphor for your intellect.
Perhaps you know of the Orz. Like us, they are dimensional travellers
but that is where our similarity ends.
Do not trust the Orz, my Human Captain. They are dangerous.
But as to your question... our relationship
To call our interaction with your kind an experiment would be much too simple and impersonal.
Let us just say that we have a vested interest in your... development.
You are one of our... extended family, just as other sentients in other dimensions
have their extended families.
We are proud of you as you would be of your children, and some day
well, I have said too much already.
```

**Shipped**:
```
如你所知，我方從未透露在銀河何處能找到我方的母星。
這有充分的理由。 我方不來自你們的空間，也不來自你們的…… *時*。
你們有些較廣泛的思想家把這類領域稱為其他次元。
雖然過於簡化，這對你們的智識而言仍是個合適的比喻。
也許你聽過歐茲族。 跟我方一樣，他們是次元旅人
但我方相似之處止於此。
別信任歐茲族，我的人類艦長。 他們很危險。
至於你的問題…… 我方之間的關係
把我方對你們一族的互動稱作實驗實在太過簡略、太過冷漠。
就這麼說吧，我方對你們的…… 發展，有著切身的關注。
你是我方的…… 遠親家族之一，正如其他次元的其他有情生靈
也有他們的遠親家族。
我方以你為榮，如你會以子女為榮，而總有一天
嗯，我已經說得太多了。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
如你所知，我們從未透露在銀河之中何處能找到我們的母星。
這其中自有充分的理由。 我們不來自你們的空間，也不來自你們的…… *時*。
你們之中某些較為廣泛的思想家把這類疆域稱為其他次元。
雖然過於簡化，但這對你們的智識而言仍是個合宜的比喻。
或許你聽過歐茲族。 跟我們一樣，他們是次元旅人
但我們的相似之處就到此為止。
別信任歐茲族，我的人類艦長。 他們很危險。
至於你的問題…… 我們之間的關係
把我們與你們一族的互動稱作實驗—— 實在太過簡單、太過冷漠。
就這麼說吧，我們對你們的……發展，懷有切身的關切。
你們是我們……延伸家族的一員，正如其他次元中的其他有情生靈
也有他們的延伸家族。
我們以你們為榮，就如你會以你的孩子為榮，而總有一天
嗯，我已經說得太多了。
```

**推薦**: 🟠 **B** — Q1=A 我方 8 處→我 / 我們（Arilou 個體發言者最集中的段落）· 「延伸家族」/「遠親家族」皆通 · v3 保留「你們是我們……延伸家族的一員」與 shipped「你是我方的……遠親家族之一」等價 · v3 更飄渺留白節奏。

**你的選擇**: A / B / C(自訂)

---

### #22 · `why_you_here` · 🟠 Q12=A 妳→你

**EN**:
```
What are you doing here, in this region of space?
```

**Shipped**:
```
妳們在這片星域做什麼？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們在這片星域裡究竟在做什麼？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性 · v3 加「究竟」（對應 "exactly")。

**你的選擇**: A / B / C(自訂)

---

### #23 · `LEARN_THINGS` · 🟠 Q1=A + 「容易之地」canonical 統一

**EN**:
```
We are many places, at many *times*. This place is an easy place... one of the ten easy places.
At different times, we explore different easy places. That is our way.
Oh! I can see from the look in your eyes that I have confused you.  I am silly.
Please disregard my words.
```

**Shipped**:
```
我方存在於許多地方，於許多 *時* 中。 此處是簡易之地…… 十處簡易之地之一。
在不同的時候，我方探索不同的簡易之地。 這是我方之道。
喔！ 從你眼中的神情，我看得出我讓你困惑了。 我真傻。
請忽略我的話。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們身在許多地方，於許多 *時* 之中。 這裡是一處容易之地…… 十處容易之地當中的一處。
在不同的時候，我們探索不同的容易之地。 這是我們的方式。
喔！ 從你眼中的神情我看得出，我讓你困惑了。 是我傻。
請不要在意我的話。
```

**推薦**: 🟠 **B** — Q1=A 我方 3 處→我們 · v3「容易之地」更貼原文 "easy places"（shipped「簡易之地」文言味較重）· 「請不要在意我的話」較 shipped「請忽略我的話」溫柔。

**你的選擇**: A / B / C(自訂)

---

### #24 · `what_things` · 🟠 「容易之地」canonical + Q12

**EN**:
```
What are you exploring for in these `easy places'?
```

**Shipped**:
```
你們在這些『簡易之地』尋找什麼？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們在這些『容易之地』裡究竟在探索什麼？
```

**推薦**: 🟠 **B** — v3「容易之地」對齊 LEARN_THINGS canonical · shipped「簡易之地」廢除。

**你的選擇**: A / B / C(自訂)

---

### #25 · `THESE_THINGS` · 🟠 Q1=A + self-fix「試圖」

**EN**:
```
We seek to trap *Nnngn*, but they dart and leap.
YOU cannot trap *Nnngn*... do not even try.
I do not think you can even touch them; you are not quite solid enough.
```

**Shipped**:
```
我方尋覓要捕捉 *Nnngn*，但他們敏捷跳躍。
『你』無法捕捉 *Nnngn*…… 別想試。
我不認為你能觸碰他們;你還不夠有實體。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們試圖捕捉 *Nnngn*，但牠們敏捷跳躍。
『你』無法捕捉 *Nnngn*…… 甚至別去嘗試。
我認為你甚至無法碰觸到牠們；你還不夠……堅實。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · self-fix「追求捕捉」→「試圖捕捉」（seek 對應 · 詳見 self-audit log #2）· 「牠們」代詞（動物）較 shipped「他們」精準 · 「甚至別去嘗試」對應 "do not even try" 較 shipped「別想試」貼原文。

**你的選擇**: A / B / C(自訂)

---

### #27 · `DO_IT_BECAUSE` · 🟠 Q1=A + 代詞精準

**EN**:
```
Why we let them go, of course! *Nnngn* do not like to be confined!
Captain, these things we talk about... they are unimportant to you... they are as dreams.
Our words should address your universe... not ours.
```

**Shipped**:
```
為什麼，當然是把他們放走！ *Nnngn* 不喜歡被拘束！
艦長，我方談的這些東西…… 對你並不重要…… 它們就像夢。
我方的話應該面向你的宇宙…… 而非我方的。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
當然是把牠們放走啊！ *Nnngn* 不喜歡被拘束！
艦長，我們談論的這些事情…… 對你並不重要…… 它們如同夢境。
我們的話語應該面向你的宇宙…… 而非我們的宇宙。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「牠們」（Nnngn 是生物 · 動物代詞）較 shipped「他們」精準 · 「事情」/「東西」皆對應 "things" 皆通。

**你的選擇**: A / B / C(自訂)

---

### #28 · `give_me_info_1` · 🟠 Q12=A 妳→你

**EN**:
```
We still struggle against the Ur-Quan. Can you help us?
```

**Shipped**:
```
我方仍在對抗烏寬族。 妳們能幫我方嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我方仍在對抗烏寬族。 你們能幫我方嗎？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性 · 保留 shipped「我方」（Alliance 對抗烏寬 · 政治語境 · 我方合理保留）。

**你的選擇**: A / B / C(自訂)

---

### #29 · `ARILOU_HINTS_1` · 🟠 Q1=A + self-fix「鮮血與骨骼」

**EN**:
```
With ships and weapons... blood and bones... no.
Too many shipmates were forcibly... discorporated.. in the last conflict.
Our cooperation is not necessary. You are the focus.
However, knowledge transcends reality perimeters, and this we can share with you.
An example: to discover the nature of the red probes
seek creatures who inhabit a world with no surface.
```

**Shipped**:
```
用船艦和武器…… 血與骨頭…… 不能。
上場衝突中，太多船員被強行…… 離身……。
我方的合作並非必要。 你才是焦點。
然而，知識超越現實的界線，這我方能與你分享。
舉個例子:要探究紅色探測機的本質
就去尋找居住在無地表世界上的生物。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
用艦艇與武器…… 鮮血與骨骼…… 不行。
上一場衝突中，太多同袍被強行……離身……了。
我們的合作並非必要。 你才是這個焦點。
然而，知識能超越現實的邊界，這一點我們能與你分享。
舉個例子：想探究紅色探測機的本質
就去尋找那些棲居於無地表世界之上的生物吧。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · self-fix「血肉與骨骼」→「鮮血與骨骼」（blood≠flesh · 詳見 self-audit log #3）· 「艦艇/同袍/棲居」較 shipped「船艦/船員/居住」正式軍事語感 · 半形冒號「:」→ v3 全形「：」。

**你的選擇**: A / B / C(自訂)

---

### #30 · `give_me_info_2` · 🟠 Q12=A 妳→你

**EN**:
```
Can you give us any more information?
```

**Shipped**:
```
妳們還能給我方更多情報嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們還能給我方更多情報嗎？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性。

**你的選擇**: A / B / C(自訂)

---

### #32 · `ARILOU_HINTS_3` · 🟠 Q1=A voice reform

**EN**:
```
The carnate forces of Ur-Quan and Kohr-Ah are twined about the memory of pain.
They respond to these words:
`Hold! What you are doing to us is wrong! Why do you do this thing?'
```

**Shipped**:
```
烏寬族與柯亞族的肉身之力纏繞於痛苦的記憶之中。
他們對這些話有反應:
『住手！ 你們對我方所做的是錯的！ 為何為此？』
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
烏寬族與柯亞族那具形之軍力，緊緊纏繞於痛苦的記憶之中。
他們對這些話語會有反應：
『住手！ 你們對我們所做的事情是錯的！ 為何要做這樣的事？』
```

**推薦**: 🟠 **B** — Q1=A shipped「你們對我方所做的是錯的」→ v3「你們對我們所做的事情是錯的」· 「具形之軍力」/「肉身之力」皆對應 "carnate forces" · v3「具形」較 shipped「肉身」抽象 fit Arilou 詩意voice · 半形冒號→全形。

**你的選擇**: A / B / C(自訂)

---

### #36 · `GOT_PART_YET_1` · 🟠 Q1=A + 語序自然化

**EN**:
```
The prospect of sharing the easy way with you excites us.
If you have found the Ur-Quan Warp Pod, this prospect can be made a reality.
```

**Shipped**:
```
與你分享簡易之道的前景令我方振奮。
若你已找到烏寬曲速艙，這前景就能實現。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
能將這條容易之道與你分享的前景，令我們振奮。
若你已找到那顆烏寬曲速艙，這樣的前景便能成真。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · v3「能將這條容易之道與你分享的前景」較 shipped「與你分享簡易之道的前景」自然 · 「這樣的前景便能成真」對應 "prospect can be made a reality"。

**你的選擇**: A / B / C(自訂)

---

### #37 · `GOT_PART_YET_2` · 🟠 Q1=A voice reform

**EN**:
```
We are so eager to give you our means to traverse reality.
Have you obtained the Warp Pod yet?
```

**Shipped**:
```
我方渴望把穿越現實的方法交給你。
你取得曲速艙了嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們是那麼渴望把我們穿越現實的方法交到你手上。
你取得那顆曲速艙了嗎？
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · v3「是那麼渴望」對應 "so eager to" · 「交到你手上」對應 "give you" 較口語 · 「那顆曲速艙」加量詞（原文 the Warp Pod 定冠詞）。

**你的選擇**: A / B / C(自訂)

---

### #38 · `INIT_ANGRY_HWLD_HELLO` · 🟠 Q1=A voice reform

**EN**:
```
You have found our world. We did not see this
and now it is too late to adjust without damage
but perhaps the situation can be resolved in another way.
The answer lies within your next statement.
```

**Shipped**:
```
你找到我方的世界了。 我方未預見此事
如今要無傷調整已太遲
但也許情況可以另尋他法解決。
答案在你下一句話中。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你找到我們的世界了。 這一切我們並未預見
如今要無傷調整已太遲
但或許，情勢還能以另一種方式化解。
答案，就在你下一句話之中。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「這一切我們並未預見」較 shipped「我方未預見此事」拆解定語 · 「情勢還能以另一種方式化解」較 shipped「另尋他法解決」新時代玄學味。

**你的選擇**: A / B / C(自訂)

---

### #40 · `HAD_OUR_REASONS` · 🟠 Q1=A + 「追求」對應 "seek"

**EN**:
```
No. We seek not to invade, but to pervade. There is a difference.
Your stories of evil creatures... these are just... side effects.
Pay them no heed.
```

**Shipped**:
```
不。 我方尋求的不是入侵，而是滲透。 這是有分別的。
你們那些邪惡生物的故事…… 那些只是…… 副作用。
不要在意它們。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
不。 我們追求的不是入侵，而是滲透。 這是有區別的。
你們那些邪惡生物的故事…… 那些只是…… 副作用而已。
別去在意它們。
```

**推薦**: 🟠 **B** — Q1=A shipped「我方尋求」→ v3「我們追求」（意思相同 · seek 動詞選擇差異）· 「別去在意」/「不要在意」皆通。 A 亦可。

**你的選擇**: A / B / C(自訂)

---

### #42 · `WE_NEVER_FRIENDS` · 🟠 Q1=A + self-fix 語序台化

**EN**:
```
We have sought amiable companionship with you, Captain
when we just as easily could have performed such experiments on you.
We shall not fight with our children. Goodbye.
```

**Shipped**:
```
我方曾試著與你友善為伴，艦長
儘管我方本可輕易對你進行那類實驗。
我方不會與我方的孩子交戰。 再見。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
艦長，我們一直尋求與你友善相伴
儘管我們原本可以輕易地就對你進行那類實驗。
我們不會與我們的孩子交戰。 再見。
```

**推薦**: 🟠 **B** — Q1=A 我方 3 處→我們 · self-fix「與你追求友善的相伴」→「尋求與你友善相伴」（詳見 self-audit log #4）· 「輕易地就對你進行」對應 "just as easily could have"。

**你的選擇**: A / B / C(自訂)

---

### #43 · `ok_lets_be_friends` · 🟠 Q1=A 我方→我 + Q12=A 妳→你

**EN**:
```
Look, I'm sorry. I made some mistakes. We need you as allies, not as enemies.
```

**Shipped**:
```
我方很抱歉。 我犯了些錯誤。 我方需要妳們是盟友，不是敵人。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
聽著，我很抱歉。 我犯了一些錯誤。 我方需要你們是盟友，而不是敵人。
```

**推薦**: 🟠 **B** — Q1=A shipped 玩家「我方很抱歉」→ v3「我很抱歉」（個人道歉非 Alliance）· 加「聽著」對應 "Look" · Q12=A 妳→你 · 保留「我方需要你們是盟友」（Alliance 政治語境）。

**你的選擇**: A / B / C(自訂)

---

### #44 · `NO_ALLY_BUT_MUCH_GIVE` · 🟠 Q1=A voice reform

**EN**:
```
We have never been your enemy, though your people may once have thought so.
But we are also not your ally. That would require a degree of involvement in this *time*
which is not presently permissible.
For now, we are simply your friends... who have much to give.
```

**Shipped**:
```
我方從來不是你的敵人，儘管你的族人可能一度那樣以為。
但我方也不是你的盟友。 那需要在此 *時* 中一定程度的介入
這在目前是不被允許的。
此刻，我方僅是你的朋友…… 而且有許多可以給予。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們從來都不是你們的敵人，雖然你的族人可能一度那樣以為。
但我們也不是你們的盟友。 那需要在此 *時* 之中投入一定程度
而這在目前是不被允許的。
此刻，我們僅是你們的朋友…… 而我們有許多可以給予。
```

**推薦**: 🟠 **B** — Q1=A 我方 4 處→我們 · 「你們的敵人/盟友」（複數 your people）較 shipped「你的敵人/盟友」對應 "your enemy/ally" 兩者可 · v3 較貼原文複數。

**你的選擇**: A / B / C(自訂)

---

### #46 · `TRUST_BECAUSE` · 🟠 Q1=A voice reform

**EN**:
```
We do many things, few of them funny... at least by our standards.
You do not, CANNOT understand some of what we do, or why.
Therefore, it may be best if you simply consider us... quirky.
```

**Shipped**:
```
我方做了許多事，其中好玩的很少…… 至少以我方的標準而言。
你不會，也不『可能』理解我方做的一些事，或原因。
因此，最好你就把我方當作…… 古怪。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們做了許多事，其中有趣的很少…… 至少以我們的標準而言。
你不會、也『不可能』理解我們所做的一些事，或其原因。
因此，最好你就把我們看作…… 古怪。
```

**推薦**: 🟠 **B** — Q1=A 我方 4 處→我們 · 「不『可能』」加頓號 · 「看作」/「當作」皆通。

**你的選擇**: A / B / C(自訂)

---

### #47 · `what_about_interference` · 🟠 Q12=A 妳→你 + 主詞明確

**EN**:
```
What gives your people the right to interfere with mine?
```

**Shipped**:
```
妳們憑什麼干預我方的族人？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們的族人憑什麼干預我方的族人？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們的族人」（原文 "your people"）· 保留「我方的族人」（Alliance 政治）。

**你的選擇**: A / B / C(自訂)

---

### #55 · `best_if_i_killed_you` · 🟠 Q12=A 妳→你

**EN**:
```
I think it would be best if I killed you now.
```

**Shipped**:
```
我想現在把妳們殺掉是最好的。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我想現在把你們殺掉，或許才是最好的做法。
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性 · v3「或許才是最好的做法」較 shipped「是最好的」貼原文 "would be best"。

**你的選擇**: A / B / C(自訂)

---

### #57 · `what_did_on_earth` · 🟠 Q12=A 妳→你

**EN**:
```
What, exactly, have you been doing on Earth?
```

**Shipped**:
```
妳們到底在地球上做了什麼？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們到底在地球上做了些什麼？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性 · 「做了些什麼」對應 "have been doing" 過去進行時。

**你的選擇**: A / B / C(自訂)

---

### #58 · `DID_THIS` · 🟠 Q1=A voice reform

**EN**:
```
You desire honesty. It is given.
We have visited your world for many thousands of years into your species' past.
We have changed things... made modifications.
```

**Shipped**:
```
你渴望坦誠。 給你。
我方造訪過你們的世界，追溯至你們一族數千年前的過往。
我方改變過事情…… 做了修改。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你渴望坦誠。 便給你。
我們造訪過你們的世界，追溯至你們一族數千年前的過往。
我們改變過事物…… 做了一些修改。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「便給你」/「給你」皆對應 "It is given" · 「事物」（複數）較 shipped「事情」貼 "things"。

**你的選擇**: A / B / C(自訂)

---

### #59 · `why_did_this` · 🟠 Q12=A 妳→你

**EN**:
```
What did you change and modify on Earth, AND WHY?!
```

**Shipped**:
```
妳們在地球改變、修改了什麼？ 為什麼？！
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們在地球上改變、修改了什麼？ 為什麼？！
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性。

**你的選擇**: A / B / C(自訂)

---

### #60 · `IDF_PARASITES` · 🟠 Q1=A + 招牌詞 icon 保留

**EN**:
```
Our motives are multiple, our desires complex.
Part of what we do on Earth is for your own protection.
There are parasites. Creatures who dwell Beyond.
They have names, but you do not know them. They would like to find you
but they are blind to your presence... unless you show yourselves.
The Androsynth showed themselves, and something noticed them.
There are no more Androsynth now. Only Orz.
```

**Shipped**:
```
我方的動機是多重的，我方的渴望複雜。
我方在地球所做部分是為了你們自身的保護。
有寄生者。 居於彼域的生物。
他們有名字，但你們不知道。 他們想找到你們
但他們對你們的存在是盲的…… 除非你們自曝其身。
安卓辛族自曝其身，某物注意到了他們。
如今再無安卓辛族。 只剩歐茲族。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們的動機是多重的，我們的渴望複雜。
我們在地球上所做的一部分，是為了你們自身的保護。
有一些寄生者。 居於彼域之中的生物。
牠們有名字，但你們並不知曉。 牠們想找到你們
可是牠們對你們的存在是盲的…… 除非你們自己顯露形跡。
安卓辛族顯露了自己，某種東西注意到了他們。
如今再無安卓辛族。 只剩歐茲族。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「牠們」（動物代詞）對應「creatures」較 shipped「他們」精準 · 「顯露形跡」/「自曝其身」皆對應 "show yourselves" · v3 較 shipped 委婉。

**你的選擇**: A / B / C(自訂)

---

### #62 · `NOT_NOW` · 🟠 Q1=A + 詞義精準

**EN**:
```
No. In a way, ignorance is your armor, your best protection.
They cannot see you now. They cannot smell you.
Much of our work with your people involved making you invisible... changing your smell.
If I tell you more, you will look where you could never look before
and while you are looking you can and will be seen.
You do not want to be seen.
```

**Shipped**:
```
不。 某種意義上，無知是你們的盔甲、你們最佳的保護。
他們此刻看不見你們。 他們聞不到你們。
我方對你們族人的許多工作就是讓你們隱形…… 改變你們的氣味。
若我告訴你更多，你就會看向你原本從未看過之處
而當你在看時，你能且將被看見。
你不會想被看見。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
不。 從某種意義上，無知是你們的盔甲、你們最好的保護。
牠們此刻看不見你們。 牠們聞不到你們的氣息。
我們與你們族人的許多工作，就是讓你們隱形…… 改變你們的氣味。
若我告訴你更多，你就會望向你原本永遠望不到之處
而當你在望的時候，你能被、也將會被看見。
你不會想被看見。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「牠們」（動物代詞）較 shipped「他們」精準 · 「牠們聞不到你們的氣息」加「氣息」對應 "smell you" 增強觸感 · 「望向」/「看向」皆通。

**你的選擇**: A / B / C(自訂)

---

### #64 · `learned_about_umgah` · 🟠 Q12=A 妳→你

**EN**:
```
Have you learned anything about the Umgah yet?
```

**Shipped**:
```
妳們對陰嘎族查到什麼了嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們對陰嘎族的事有查到什麼了嗎？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳們」→ v3「你們」中性 · 「查到什麼」/「事有查到什麼」皆通。

**你的選擇**: A / B / C(自訂)

---

### #65 · `WELL_GO_CHECK` · 🟠 Q1=A voice reform

**EN**:
```
Hmmm... this is disturbing news. They are normally rambunctious to an extreme.
We will send ships to Umgah space to investigate.
We should have some answers in a few days time.
```

**Shipped**:
```
唔…… 這是令人不安的消息。 他們平時是極度活躍的。
我方會派艦艇去陰嘎星域調查。
幾日內應該會有些答案。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
嗯…… 這消息令人不安。 他們平時是極度活躍的。
我們會派艦艇前往陰嘎星域調查。
幾日之內應該就會有些答案。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「嗯…」/「唔…」皆對應 "Hmmm..." · v3「前往陰嘎星域」/shipped「去陰嘎星域」皆通。

**你的選擇**: A / B / C(自訂)

---

### #66 · `NO_NEWS_YET` · 🟠 Q1=A voice reform

**EN**:
```
Our exploration skiffs have not returned. We are concerned.
Perhaps if you ask later, we will know then.
```

**Shipped**:
```
我方的探勘艇尚未返回。 我方感到憂心。
也許你稍後再問，我方屆時會有消息。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們的探勘小艇尚未歸來。 我們感到憂心。
或許等你稍後再問，我們屆時就能知曉。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「探勘小艇」/「探勘艇」皆通 · 「歸來」/「返回」皆通。

**你的選擇**: A / B / C(自訂)

---

### #73 · `DANGEROUS_BUT_USEFUL` · 🟠 Q1=A voice reform

**EN**:
```
The Dnyarri were the most inimical race this galaxy has known.
In other dimensions, other *times*, there are far, far worse beings
but they do not threaten you at the present time.
During their reign, the Dnyarri possessed absolute power over all intelligent species in this region.
They used their slaves for all menial tasks and many forms of depraved entertainment.
If the Talking Pet we gave to the Umgah has attained the coercive abilities of its ancestors
we must assume that other Talking Pets can do likewise.
Therefore the creature must be considered the most dangerous being in the galaxy.
Its destruction is necessary... unless
you can find some way to gain control over the creature!
If you could do this you would have a powerful weapon against the Ur-Quan.
Of course, if you made one mistake, you would be the Dnyarri's slave forever.
```

**Shipped**:
```
蟾亞族是這銀河所知最為敵對的種族。
在其他次元、其他 *時*，還有遠更可怕的生靈
但目前他們並未威脅你們。
蟾亞族統治時期，他們對此區所有智慧物種擁有絕對權力。
他們用奴隸從事一切雜役以及許多墮落形式的娛樂。
若我方給陰嘎族的那隻會話寵已獲其先祖的脅迫能力
我方必須假定其他會話寵也能如此。
因此該生物必須被視為銀河中最危險的存在。
它必須被消滅…… 除非
你能找到某種方法控制這個生物！
若你能做到，你便擁有對抗烏寬族的強大武器。
當然，若你犯一個錯，你就會永遠是蟾亞族的奴隸。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
蟾亞族是這片銀河所知最為敵對的種族。
在其他次元、其他 *時* 之中，還有更為、更為可怕的存在
但牠們目前並不威脅你們。
在他們統治時期，蟾亞族對這片區域內所有智慧物種擁有絕對權力。
他們用奴隸從事一切雜役，以及許多墮落形式的娛樂。
若我們給陰嘎族的那隻會話寵，已獲得其先祖的脅迫能力
我們就必須假定其他會話寵也能如此。
因此，這個生物必須被視為銀河中最危險的存在。
消滅牠是必要的…… 除非
你能找到某種方法控制這個生物！
若你做得到，你便擁有了對抗烏寬族的強大武器。
當然，若你犯下一個錯，你將永遠是蟾亞族的奴隸。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「牠們」（Dnyarri creatures 代詞）· 「更為、更為可怕」對應 "far, far worse" 疊字節奏 · 「消滅牠是必要的」/「它必須被消滅」（v3 主動 vs shipped 被動）較自然。

**你的選擇**: A / B / C(自訂)

---

### #74 · `what_give_me` · 🟠 Q12=A 妳→你

**EN**:
```
You said you had much to give my people. Can you be more specific?
```

**Shipped**:
```
妳說妳有很多可以給我方族人。 能具體點嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你說你們有許多可以給我方族人。 能說具體一點嗎？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳說妳有」→ v3「你說你們有」中性 · 保留「我方族人」（Alliance 政治）。

**你的選擇**: A / B / C(自訂)

---

### #76 · `what_about_tpet` · 🟠 Q12=A 妳→你

**EN**:
```
You mentioned a Talking Pet. How did you find one?
```

**Shipped**:
```
妳提到會話寵。 妳們怎麼找到一隻的？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你提到了一隻會話寵。 你們是怎麼找到一隻的？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳提到」/「妳們怎麼找到」→ v3「你提到」/「你們是怎麼找到」中性。

**你的選擇**: A / B / C(自訂)

---

### #78 · `about_portal_again` · 🟠 Q12=A 妳→你

**EN**:
```
Can you tell me about that Portal Spawner thing again?
```

**Shipped**:
```
妳能再跟我說一次那個傳送門生成器嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
能再跟我說一次那個傳送門生成器的事嗎？
```

**推薦**: 🟠 **B** — Q12=A shipped「妳能再跟我說」→ v3「能再跟我說」中性（省略主詞）。

**你的選擇**: A / B / C(自訂)

---

### #81 · `CLEVER_HUMAN` · 🟠 Q1=A + 招牌強調 icon

**EN**:
```
What a surprise!
As we have always said, Humans are a MOST resourceful and clever species.
We are so proud of you! But don't worry that you shall have to wait.
```

**Shipped**:
```
多麼令人驚喜！
如我方一直所說，人類是最為機智聰明的物種。
我方為你感到驕傲！ 別擔心你必須等候。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
多麼令人驚喜！
正如我們一向所說的—— 人類是『最』機智聰慧的物種。
我們為你感到驕傲！ 但別擔心你必須等候。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · v3「『最』機智聰慧」加全形引號強調（對應 "MOST" 全大寫 · dossier §六強調 icon）· 「聰慧」/「聰明」皆通。

**你的選擇**: A / B / C(自訂)

---

### #82 · `GIVE_PORTAL` · 🟠 Q1=A voice reform

**EN**:
```
We are prepared. Even now our technical personnel are equipping your ship
with a custom version of our Portal Spawner device.
The device is useable only in HyperSpace. Whenever it is activated
the Spawner will focus several inter-dimensional fatigue beams adjacent to your vessel
opening a temporary hole into QuasiSpace. Move quickly through the Portal!
After your ship has passed into QuasiSpace, you can choose any of the nearby Portals
which lead back to HyperSpace, thus saving you needless transit time.
Be keenly aware of this fact! The Spawner requires a great deal of energy to function.
We estimate that each time you use the device, it will consume ten of your fuel units.
```

**Shipped**:
```
我方已備妥。 此刻我方的技術人員正在為你的艦艇裝配
一套訂製版的傳送門生成器裝置。
該裝置僅能在超空間中使用。 每次啟動
生成器會將數道次元疲勞射線聚焦於你的艦艇附近
打開一個通往準空間的臨時洞口。 迅速穿過傳送門！
你的艦艇進入準空間後，你可以選擇任何附近的傳送門
通往超空間，如此省下無謂的航行時間。
請務必注意此點！ 生成器運作需要大量能源。
我方估計你每次使用該裝置，將消耗十單位的燃料。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們已備妥。 就在此刻，我們的技術人員正在為你的艦艇裝配
一套訂製版的傳送門生成器裝置。
此裝置僅能在超空間中使用。 每次啟動之時
生成器會將數道次元疲勞光束聚焦於你艦艇的鄰近之處
在準空間之上開啟一個臨時的洞口。 迅速穿越那扇傳送門！
當你的艦艇進入準空間之後，你可以選擇任何附近的傳送門
它們會通回超空間，如此便省下你無謂的航行時間。
請務必留意這一點！ 生成器運作需要大量的能量。
我們估算，每次你使用此裝置，都將消耗你十單位的燃料。
```

**推薦**: 🟠 **B** — Q1=A 我方 3 處→我們 · 「就在此刻」對應 "Even now" · 「次元疲勞光束」/「次元疲勞射線」皆對應 "inter-dimensional fatigue beams" · v3 較 shipped 詩意留白（「聚焦於你艦艇的鄰近之處」）。

**你的選擇**: A / B / C(自訂)

---

### #85 · `HOSTILE_GOODBYE_1` · 🟠 Q1=A voice reform

**EN**:
```
We have said all there is to be said.
We would prefer your immediate departure, but are prepared for your attack.
```

**Shipped**:
```
我方能說的都說了。
我方希望你立刻離開，但已準備好迎接你的攻擊。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
該說的我們已經都說完了。
我們希望你立即離開，但也已準備好面對你的攻擊。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「該說的我們已經都說完了」/「我方能說的都說了」皆對應 "We have said all there is to be said" · v3 較自然。

**你的選擇**: A / B / C(自訂)

---

### #86 · `HOSTILE_GOODBYE_2` · 🟠 Q1=A voice reform

**EN**:
```
Your behavior is clearly inimical. We resist discorporation.
Further contact between ourselves is pointless.
```

**Shipped**:
```
你的行為顯然不友善。 我方拒絕離身。
我方之間再繼續接觸已無意義。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你的行為顯然懷有敵意。 我們拒絕離身。
我們彼此之間繼續接觸下去，已無意義。
```

**推薦**: 🟠 **B** — Q1=A 我方 2 處→我們 · 「懷有敵意」/「不友善」對應 "inimical"（敵意較強烈）· 「彼此之間繼續接觸下去」/「之間再繼續接觸」皆通。

**你的選擇**: A / B / C(自訂)

---

### #87 · `HOSTILE_GOODBYE_3` · 🟠 Q1=A voice reform

**EN**:
```
Seek death in other corners. Leave us.
```

**Shipped**:
```
去別處尋死吧。 離開我方。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
去別處尋死吧。 離開我們。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 短句。

**你的選擇**: A / B / C(自訂)

---

### #88 · `HOSTILE_GOODBYE_4` · 🟠 Q1=A voice reform

**EN**:
```
Seek death in other corners. Leave us.
```

**Shipped**:
```
去別處尋死吧。 離開我方。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
去別處尋死吧。 離開我們。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 短句（HOSTILE_GOODBYE_3 重複）。

**你的選擇**: A / B / C(自訂)

---

### #89 · `ANGRY_SPACE_HELLO_1` · 🟠 Q1=A voice reform

**EN**:
```
We cannot fathom your reason, therefore you must be acting upon simple instinct.
Perhaps this is our fault. We have always loved instinct
even though we possess none ourselves.
Do you have too much instinct, human? Does your species? We shall see.
```

**Shipped**:
```
我方無法揣度你的理由，因此你必然是憑本能行事。
或許這是我方之過。 我方一向鍾愛本能
即便我方自身並無本能。
你本能過於旺盛嗎，人類？ 你的族人如此嗎？ 我方會看到的。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們無法揣度你的緣由，因此你必然是憑本能在行事。
或許這是我們的過錯。 我們一直深愛本能
即使我們自身並無本能。
你的本能是不是太多了呢，人類？ 你的族人呢？ 我們會看到的。
```

**推薦**: 🟠 **B** — Q1=A 我方 5 處→我們 · 「緣由」/「理由」皆對應 "reason" · 「深愛」/「鍾愛」皆通 · 「本能是不是太多了呢」/「本能過於旺盛嗎」皆通。

**你的選擇**: A / B / C(自訂)

---

### #92 · `NO_FIGHT` · 🟠 Q1=A + 詞選

**EN**:
```
We will never choose to fight you, child.
```

**Shipped**:
```
我方永遠不會選擇與你交戰，孩子。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我們永遠不會選擇與你戰鬥，孩子。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「戰鬥」/「交戰」對應 "fight" · 皆通。

**你的選擇**: A / B / C(自訂)

---

### #94 · `APOLOGIZE_AT_HOMEWORLD` · 🟠 Q1=A voice reform

**EN**:
```
If you wish to make atonement... seek a strangely shaped rock or plant.
However, should you wish to change the nature of our relationship
seek the Arilou in QuasiSpace. You can make the transit at <% comm.getPoint("43.8 : 637.2", "arilou") %>...
...but only when the door is open.
```

**Shipped**:
```
若你想贖罪…… 尋找一顆形狀奇特的岩石或植物。
然而，若你想改變我方之間關係的性質
就在準空間尋找阿麗露。 你可以在 <% comm.getPoint("43.8 : 637.2", "arilou") %> 位置穿越……
……但只在那扇門開啟時。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
若你想贖罪…… 就去尋找一塊形狀奇特的岩石，或一株植物。
然而，若你想改變我們之間關係的本質
就到準空間中來尋找阿麗露。 你可以在 <% comm.getPoint("43.8 : 637.2", "arilou") %> 這處穿越……
……但只在那扇門開啟之時。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「一塊形狀奇特的岩石，或一株植物」加量詞 · 「就到準空間中來尋找阿麗露」較 shipped「就在準空間尋找阿麗露」詩意 · 「本質」/「性質」對應 "nature" 皆通。

**你的選擇**: A / B / C(自訂)

---

### #96 · `GOODBYE_ANGRY_SPACE` · 🟠 Q1=A voice reform

**EN**:
```
When you have resolved your conflict, we shall speak again.
```

**Shipped**:
```
當你解決你的衝突後，我方會再對話。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
當你化解了自身的衝突之後，我們會再對話。
```

**推薦**: 🟠 **B** — Q1=A 我方→我們 · 「化解了自身的衝突之後」/「解決你的衝突後」皆對應 "have resolved your conflict"。

**你的選擇**: A / B / C(自訂)

---

## 🟡 微調（等價） · 27 tokens

**shipped 與 v3 語意完全相同 · 選字/語序/量詞/語氣詞微差** · 推薦 A（shipped 精簡）除非特別註明

### #1 · `INIT_HELLO` · 🟡 v3 更貼原文成就感

**EN**:
```
Hello my little one. I am so pleased to see you!
You have done well for yourself.
It is gratifying.
```

**Shipped**:
```
哈囉，我親愛的小孩。 見到你我真高興！
你把自己照顧得很好。
這令人欣慰。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
哈囉，我親愛的小孩。 見到你我真是欣喜！
你為自己走出了一條好路。
這令我很欣慰。
```

**推薦**: 🟡 **B** — shipped「照顧得很好」偏 caretaker · v3「走出了一條好路」對應 "done well for yourself" 貼原文成就感 + 「令我很欣慰」加 Arilou 個體 voice。 兩者皆通、v3 較符 dossier §四 A 案。

**你的選擇**: A / B / C(自訂)

---

### #6 · `miffed_by_hello` · 🟡 微調（等價）

**EN**:
```
I'll be. It's the Arilou. Why the hell did you run out on the Alliance of Free Stars? What happened?
```

**Shipped**:
```
真是的。 是阿麗露。 你們為什麼要離開自由星系聯盟？ 出了什麼事？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
天啊。 是阿麗露。 你們到底為什麼要拋下自由星系聯盟？ 是出了什麼事？
```

**推薦**: 🟡 **A** — 「真是的」/「天啊」 皆對應 "Ill be" 感嘆詞 · 「離開」/「拋下」皆對應 "run out on" 皆通 · shipped 更精簡。 建議 A 保留 shipped。

**你的選擇**: A / B / C(自訂)

---

### #10 · `FRIENDLY_SPACE_HELLO_3` · 🟡 微調（等價）

**EN**:
```
Last night as you slept, I touched your face and you smiled!...
but now you frown. A pity. Smiling is healthier.
```

**Shipped**:
```
昨夜你睡著時，我撫觸你的臉，你便微笑！……
但現在你皺眉了。 可惜。 微笑更健康。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
昨夜當你入睡時，我輕觸了你的臉，而你便微笑了！……
但如今你卻皺著眉。 真可惜。 微笑對身體比較好。
```

**推薦**: 🟡 **A** — shipped/v3 皆對應原文 · v3「輕觸了」/「昨夜當你入睡」較 shipped「撫觸」/「昨夜你睡著時」略詩意 · shipped 也完整。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #14 · `FRDLY_HOMEWORLD_HELLO_3` · 🟡 微調（等價）

**EN**:
```
Hello. We are pleased to see you again. Have you any numbness yet?
Good. It should be too soon for that. Too soon by far.
```

**Shipped**:
```
哈囉。 再見到你真好。 你有感到任何麻痺嗎？
很好。 現在還不該有。 差得遠了。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
哈囉。 再次見到你我很欣慰。 你有沒有感到任何麻痺呢？
很好。 現在還太早，不該有。 遠遠太早了。
```

**推薦**: 🟡 **A** — shipped「再見到你真好」/「差得遠了」精簡 · v3「再次見到你我很欣慰」/「遠遠太早了」較貼原文 pleased/too soon by far · 皆通。 建議 A（shipped 精煉留白）。

**你的選擇**: A / B / C(自訂)

---

### #15 · `FRDLY_HOMEWORLD_HELLO_4` · 🟡 微調（等價）

**EN**:
```
Yes, Captain? What can the Arilou Lalee'lay of Falayalaralfali do for you this day?
```

**Shipped**:
```
是的，艦長？ 法拉雅拉拉法利的阿麗露·萊蕾今日能為你做些什麼？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
是的，艦長？ 法拉雅拉拉法利的阿麗露·萊蕾今日能為你效勞什麼呢？
```

**推薦**: 🟡 **A** — 「今日能為你做些什麼」/「今日能為你效勞什麼呢」皆對應 "do for you this day" · shipped 更口語自然。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #16 · `whats_up_1` · 🟡 語序調整

**EN**:
```
What exactly IS your connection with Earth and Humans, anyway?
```

**Shipped**:
```
你們到底跟地球和人類有什麼淵源？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
說到底，你們跟地球、跟人類的淵源到底是什麼？
```

**推薦**: 🟡 **A** — shipped「你們到底跟地球和人類有什麼淵源？」較 v3「說到底，你們跟地球、跟人類的淵源到底是什麼？」精煉 · 兩者皆通 · shipped 較口語。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #17 · `whats_up_2` · 🟡 微調（等價）

**EN**:
```
I'm still confused about our relationship. Please elaborate.
```

**Shipped**:
```
我方兩族的關係我還是不清楚。 請多說明一下。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我方兩族的關係，我還是不清楚。 請你多說明一下。
```

**推薦**: 🟡 **A** — 僅新增逗號 + 「請你」 · 皆通 · shipped 更精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #21 · `GENERAL_INFO_4` · 🟡 微調（等價）

**EN**:
```
You already know more than is appropriate. In fact, you may represent an unfortunate complication.
You have been in the stars for much time. Do you seek the doorway, or are you just passing through?
Remember, you can only go over naturally for the three days it is open.
How to find it? Look on your starmap from 17 through 20. The variable star shall be your guide.
```

**Shipped**:
```
你所知已超過所適當。 事實上，你或許代表一個不幸的複雜情況。
你已在群星間許久。 你在尋找那扇門，還是只是路過？
記住，你只有在它開啟的三日內能自然通過。
如何找到？ 看你的星圖 17 至 20 位置。 那顆變星將是你的嚮導。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你所知已經超過了合適的界線。 事實上，你或許代表了一個不幸的複雜情況。
你已在群星之間度過許久。 你在尋找那扇門，還是只是路過？
記住，你只有在那扇門開啟的三日之內能自然通過。
如何找到它呢？ 看看你的星圖 17 至 20 位置。 那顆變星，將是你的嚮導。
```

**推薦**: 🟡 **A** — 「所知已超過所適當」/「所知已經超過了合適的界線」皆對應 "know more than is appropriate" · 皆通 · shipped 精簡。 建議 A（shipped 較凝練）。

**你的選擇**: A / B / C(自訂)

---

### #26 · `why_do_it` · 🟡 微調（音譯 nungy）

**EN**:
```
Okay, you trap these nungy things. Then what?
```

**Shipped**:
```
好，你們捕捉這些冬咕咕東西。 然後呢？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
好，你們捕捉這些寧根東西。 然後呢？
```

**推薦**: 🟡 **B** — shipped「冬咕咕東西」/v3「寧根東西」皆為 "nungy things" 兒化詞的音譯 gag · v3「寧根」對齊 canonical `*Nnngn*` 詞根 · 建議 B（詞根統一）· A 亦可（shipped「冬咕咕」更童趣）。

**你的選擇**: A / B / C(自訂)

---

### #31 · `ARILOU_HINTS_2` · 🟡 Q1=A 微調（無我方）

**EN**:
```
The Mycon change and reform worlds with their Deep Children.
These changes affect others unfortunately.
The fate of your world and your heart relate to these matters.
```

**Shipped**:
```
麥孔族用他們的深層幼體改造與重塑星球。
這些改變不幸也影響了他人。
你的世界與心之命運，與這些事有關。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
麥孔族用他們的深層幼體改造與重塑世界。
不幸的是，這些改變也波及了其他人。
你的世界與你心中的命運，都與這些事息息相關。
```

**推薦**: 🟡 **B** — 無 Q1 差異（此 token shipped 無我方）· v3 微調「不幸的是，這些改變也波及了其他人」較 shipped「這些改變不幸也影響了他人」順口 · 「你的世界與你心中的命運」較 shipped「你的世界與心之命運」少 1 個「之」（可 · dossier 廢除文言之風格）。

**你的選擇**: A / B / C(自訂)

---

### #35 · `GOODBYE_FRIENDLY_SPACE` · 🟡 微調（等價）

**EN**:
```
Farewell child.
```

**Shipped**:
```
再會，親愛的孩子。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
再會了，親愛的孩子。
```

**推薦**: 🟡 **A** — 「再會」/「再會了」對應 "Farewell" · 皆通 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #39 · `invaders_from_mars` · 🟡 微調（等價）

**EN**:
```
You guys are like... invaders from Mars! Weird evil monsters!
```

**Shipped**:
```
你們就像…… 火星入侵者！ 詭異的邪惡怪物！
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你們就像是…… 來自火星的入侵者！ 詭異的邪惡怪物！
```

**推薦**: 🟡 **A** — 僅加「來自」/「就像是」語氣詞 · shipped 更精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #41 · `bug_eyed_fruitcakes` · 🟡 微調（等價）

**EN**:
```
No-no-no-no-no! I'll stop you! You bug-eyed fruitcakes have mutilated your last cow!
```

**Shipped**:
```
不不不不不！ 我要阻止你們！ 你們這些鼓眼怪咖已經割壞了最後一頭牛！
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
不不不不不！ 我要阻止你們！ 你們這些鼓眼怪咖，最後一頭牛已經被你們糟蹋完了！
```

**推薦**: 🟡 **A** — 「已經割壞了最後一頭牛」/「最後一頭牛已經被你們糟蹋完了」皆對應 "have mutilated your last cow" · shipped 主動句較 v3 被動句自然。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #45 · `why_should_i_trust` · 🟡 微調（等價）

**EN**:
```
Why should I trust you? You did funny things to that horror writer a while ago, right?
```

**Shipped**:
```
我為何該信任你們？ 你們對那位恐怖小說家做過怪事，對吧？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我為什麼該信任你們？ 你們前一陣子對那位恐怖小說家做過些怪事，對吧？
```

**推薦**: 🟡 **A** — 「我為何該」/「我為什麼該」皆通 · 加「前一陣子」對應 "a while ago" · 加「些」語氣詞 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #48 · `INTERFERENCE_NECESSARY` · 🟡 微調（等價）

**EN**:
```
What gives you the right to move, the right to fall?
Some acts are motivated, others are automatic.
Do not presume that you can decide which is which for anyone but yourself
or you will be... disappointed.
```

**Shipped**:
```
你憑什麼移動，憑什麼跌倒？
有些行為有動機，有些是自動的。
別以為除了你自己之外，你能替別人決定哪個是哪個
否則你會…… 失望。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
你又憑什麼移動，憑什麼跌倒？
有些行為出於動機，有些則是自動的。
別以為除了你自己之外，你能替任何人決定哪個是哪個
否則你會…… 失望的。
```

**推薦**: 🟡 **A** — 皆對應原文 · v3 加「又」/「任何人」/「失望的」語氣詞 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #49 · `i_just_like_to_leave` · 🟡 微調（等價）

**EN**:
```
Ok, fine, whatever. Just let me leave now, okay?
```

**Shipped**:
```
好啦，隨便啦。 就讓我走吧，好嗎？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
好啦、隨便啦。 就讓我現在離開吧，好嗎？
```

**推薦**: 🟡 **A** — 皆對應原文 · v3 加「現在」/「離開」/「，」 · shipped「就讓我走吧」較 v3「就讓我現在離開吧」自然。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #50 · `SORRY_NO_LEAVE` · 🟡 微調（等價）

**EN**:
```
This matter must be resolved, or many event strands will grow... more complicated.
Your presence is required.
```

**Shipped**:
```
此事必須解決，否則許多事件的線條會變得…… 更複雜。
你的存在是必需的。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
此事必須得到解決，否則許多事件的線索將會變得…… 更加複雜。
需要你的存在。
```

**推薦**: 🟡 **A** — 皆對應原文 · v3「事件的線索」/「更加複雜」較貼原文 event strands/more complicated · shipped「事件的線條」意通但選字略異。 A 較精簡。

**你的選擇**: A / B / C(自訂)

---

### #53 · `what_about_urquan` · 🟡 微調（等價）

**EN**:
```
Well what about the Ur-Quan? What are they up to?
```

**Shipped**:
```
那烏寬族呢？ 他們在幹嘛？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
那烏寬族呢？ 他們在做些什麼？
```

**推薦**: 🟡 **A** — 「他們在幹嘛？」/「他們在做些什麼？」皆對應 "What are they up to?" · shipped 較口語 · 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #61 · `tell_more` · 🟡 微調（等價）

**EN**:
```
This sounds creepy. Please go on.
```

**Shipped**:
```
這聽起來令人毛骨悚然。 請繼續。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
這聽起來令人毛骨悚然。 請繼續說。
```

**推薦**: 🟡 **A** — 僅加「說」語氣詞 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #63 · `umgah_acting_weird` · 🟡 微調（等價）

**EN**:
```
We have met the Umgah, and they are acting extremely weird, like zombie-blobbies!
```

**Shipped**:
```
我方見過陰嘎族，他們表現極其怪異，像是殭屍軟糊糊！
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我方遇到了陰嘎族，他們的行為極其怪異，就像殭屍軟糊糊一樣！
```

**推薦**: 🟡 **A** — 「見過」/「遇到了」皆對應 "met" · 「表現極其怪異」/「行為極其怪異」皆通 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #68 · `what_do_now` · 🟡 微調（等價）

**EN**:
```
So what can we do about the psychically zombified blobbies?
```

**Shipped**:
```
那我方能怎麼對付被精神控制的軟糊糊呢？
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
那我方能拿這些被精神殭屍化的軟糊糊怎麼辦？
```

**推薦**: 🟡 **A** — 「怎麼對付」/「拿⋯⋯怎麼辦」皆對應 "what can we do about" · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #70 · `tell_arilou_about_tpet` · 🟡 微調（等價）

**EN**:
```
The source of the Umgah's compulsion is the Talking Pet you gave the Umgah,
but now it is intelligent and exhibits strange powers.
```

**Shipped**:
```
陰嘎族被精神控制的源頭是你們給他們的那隻會話寵，
但如今牠有智慧且展現詭異能力。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
陰嘎族被脅迫的源頭，就是你們給他們的那隻會話寵，
但如今牠有了智慧，並展現出詭異的能力。
```

**推薦**: 🟡 **A** — 「精神控制」/「脅迫」對應 "compulsion" 皆通 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #71 · `BAD_NEWS_ABOUT_TPET` · 🟡 微調（等價）

**EN**:
```
That is very bad news. This creature, a super-intelligent, psychically coercive creature
is very similar to a race of beings which was thought to have vanished over 20,000 years ago.
They were called the Dnyarri, and history tells that they ruled a wide region of this galaxy
for many thousands of years. The Dnyarri were cruel and devious
and when they were finally overthrown by one of their slave-races
they were supposedly exterminated.
Perhaps this Talking Pet is the degenerate product of the Dnyarri.
```

**Shipped**:
```
那是非常糟糕的消息。 這個生物，一個超智能、能施心靈脅迫的生物
和一個據信已在兩萬多年前消失的種族極為相似。
他們稱為蟾亞族，歷史記載他們曾統治銀河廣大區域
達數千年之久。 蟾亞族殘忍狡詐
最終被其奴族之一推翻時
他們據說被滅絕了。
或許這隻會話寵是蟾亞族的退化產物。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
這是極糟的消息。 這個生物—— 一種超智能、能施心靈脅迫的生物
與一支據信在兩萬多年前就已消失的種族極為相似。
他們被稱為蟾亞族，歷史記載他們曾統治過銀河的廣大區域
長達數千年之久。 蟾亞族殘忍狡詐
當他們最終被自己的奴族之一推翻時
據說他們就此被滅絕。
或許，這隻會話寵，就是蟾亞族的退化產物。
```

**推薦**: 🟡 **A** — 「那是非常糟糕的消息」/「這是極糟的消息」皆對應 "very bad news" · 皆通 · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #80 · `got_it` · 🟡 微調（等價）

**EN**:
```
I have obtained the Warp Pod unit from the Ur-Quan wreck.
```

**Shipped**:
```
我已從烏寬殘骸中取得曲速艙。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
我已從烏寬殘骸中取得曲速艙裝置。
```

**推薦**: 🟡 **A** — 「曲速艙」/「曲速艙裝置」皆對應 "Warp Pod unit" · shipped 精簡（unit 可省）· 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #84 · `GOODBYE_FRDLY_HOMEWORLD` · 🟡 微調（等價）

**EN**:
```
Goodbye clever child.
```

**Shipped**:
```
再見，聰明的孩子。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
再會了，聰明的孩子。
```

**推薦**: 🟡 **A** — 「再見」/「再會了」皆對應 "Goodbye" · shipped 精簡。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #90 · `ANGRY_SPACE_HELLO_2` · 🟡 微調（等價）

**EN**:
```
Human. You flail at the wind. Cease your violence.
Would you hurt your pet? Your child? Your beast?
Please... rethink your posture.
```

**Shipped**:
```
人類。 你正在對空氣揮拳。 停止你的暴力。
你會傷害你的寵物嗎？ 你的孩子？ 你的獸？
請…… 重新思考你的姿態。
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
人類。 你正在對空氣揮拳。 停止你的暴力吧。
你會傷害你的寵物嗎？ 你的孩子？ 你的獸？
請…… 重新思考你的姿態。
```

**推薦**: 🟡 **A** — 僅加「吧」語氣詞 · 其餘完全相同。 建議 A。

**你的選擇**: A / B / C(自訂)

---

### #93 · `im_sorry` · 🟡 微調（等價）

**EN**:
```
Aughhh! I am sorry! WHAT WAS I THINKING?!!
```

**Shipped**:
```
啊！ 我很抱歉！ 我剛才在想什麼？！！
```

**Rebuild v3** (已通過階段 2.5 Read-Aloud 自審):
```
啊！ 我很抱歉！ 我剛才到底在想什麼？！！
```

**推薦**: 🟡 **A** — 僅加「到底」語氣詞。 建議 A。

**你的選擇**: A / B / C(自訂)

---
