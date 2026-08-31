# 撻伐族 Rebuild-Compare Diff Report (2026-08-17)

## 統計
- Total tokens: 152
- 🟢 完全相同: 38 (25.0%)
- 🟡 微調 (等價): 6 (3.9%)
- 🟠 措辭改變: 101 (66.4%)
- 🔴 語意/voice 差異大: 0 (0.0%)
- ✨ v0.7 canonical 升級: 7 (4.6%)

## Q&A 決策 recap
- Q1=A(蔚藍螺旋), Q2=A(艦名 shipped), Q3=B(人名 dossier v0.7), Q4=C(Great Teacher 情境切換)
- Q5A=A(肥胖粗俗混蛋), Q5B=A(摔屁股城), Q5C=B(放特)
- Q6=A(SNORT/HARG 首介英文), Q7=A(dossier palette), Q8=A(PL/Rhyme 一致), Q9=C(史匹柏Spielberg)
- Q10=B(玩家 response 僅重譯有污染), Q11=A(4批 × ~38 tokens)

## 差異項 (只列 🟡🟠🔴✨,不列 🟢)

### #1 · HOSTILE_HOMEWORLD_HELLO_3 · ✨ canonical: 考格克→柯格克

**英文原文**:
```
I am Korgk, battle-slave foreman of Culture Nineteen.
You may be interested to know that our model ZK-53 computer
has determined that you have only a fleeting 1.6% chance
of surviving a battle with our homeworld guardian fleet.
Shall we test this assertion?
```

**Shipped v0.3**:
```
吾乃考格克（Korgk）,第十九文化之戰奴工頭。
爾或許有興趣知曉,吾等 ZK-53 型電腦
已判定爾與吾等母星守衛艦隊交戰後
僅有 1.6% 之短暫存活機會。
吾等可否驗證此判定？
```

**Rebuild v3**:
```
我是柯格克（Korgk）,第十九文化的戰奴工頭。
你可能會有興趣知道,我方 ZK-53 型電腦
已經算出來,你在跟我方母星守衛艦隊交戰時
只有轉瞬即逝的 1.6% 存活機率。
要不要來測試看看這個結論？
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #2 · GENERAL_INFO_HOSTILE_1 · ✨ canonical: 卓卡→賈卡

**英文原文**:
```
Hostility!
HARG! HARG! HARG!
We are not `hostile'. Hostility is unwarranted aggression! SNORT! 
If you want to know about hostility, let us tell you about Culture Twelve!
Culture Twelve was SO hostile that while they were on their way to their first great battle
Jugkah, the battlemaster, stepped on Gnusko the tactician's foot, causing him great pain.
The annoyed Gnusko turned on his battlemaster, Jugkah, and sliced his body in half!
This miffed Jugkah's troops who took it upon themselves to murder Gnusko and his elite troops.
The REAL trouble started when now-dead Jugkah's master sergeants Muuhd and Pudt
started arguing about how to kill Gnusko -- simple crucifixion, or the slower `Lead Tatoo' technique.
The argument was resolved when Muuhd and his five hundred troops were slaughtered by Pudt and his gang.
Well, this probably all would have gone down in history as a great day of learning for Culture Twelve
were it not for the surprise arrival of Culture Twelve's original enemy, the Yajag and his cronies
who wiped out Culture Twelve's army, thus beginning the long and glorious Culture Thirteen.
SNORT! Now THAT'S hostility!
...
```

**Shipped v0.3**:
```
敵意！
哈！哈！哈！
吾等並非「有敵意」。 敵意乃無正當理由之侵略！ 哼！
若爾等想了解敵意,吾等且告知第十二文化之事！
第十二文化之敵意如此之深,連他們前往首場大戰的途中
卓卡（Jugkah）,那位戰鬥宗師,踩到了戰術官奴斯克（Gnusko）的腳,使其劇痛。
惱怒之奴斯克回身向其戰鬥宗師卓卡,將他身軀劈為兩段！
此舉惹惱了卓卡之部屬,他們遂決意誅殺奴斯克及其精銳。
真正的麻煩開始於現已亡故的卓卡之首席士官穆德（Muuhd）與普德（Pudt）
爭論如何處決奴斯克 —— 簡單釘刑,還是更緩慢的「鉛痕之技」。
此爭論以穆德及其五百士兵被普德一夥屠殺告終。
嗯,這本可作為第十二文化偉大之學習日載入史冊
若非第十二文化之原敵人雅賈（Yajag）及其黨羽突然抵達
將第十二文化之軍隊全數殲滅,自此開啟悠長光榮之第十三文化。
哼！ 這才叫敵意！
```

**Rebuild v3**:
```
敵意！
哈！哈！哈！
我方才不是「敵意」。 敵意是沒理由的侵犯！ 哼！
你想懂什麼是敵意,那就讓我方告訴你第十二文化的故事！
第十二文化敵意重到,當年他們正要去打第一場大會戰的路上
戰務大師賈卡（Jugkah）踩到戰術官格努斯柯（Gnusko）的腳,痛到他不行。
被惹毛的格努斯柯轉身反攻他的戰務大師賈卡,把他劈成兩半！
這件事把賈卡的部隊惹火,他們自作主張把格努斯柯和他的菁英部隊都幹掉。
真正的麻煩是,已故賈卡的兩位軍士長穆德（Muuhd）和普德（Pudt）
開始爭論怎麼處決格努斯柯 —— 是簡單釘十字架,還是慢速的「鉛痕技法」。
穆德和他的五百士兵被普德一夥砍成肉泥,爭論才告一段落。
好啦,這一切本來大概會被歷史寫成第十二文化學習成長的大日子
但第十二文化原本的死敵,亞加格（Yajag）和他那群人馬突然殺到
把第十二文化的軍隊全滅了,於是開啟了長遠又光榮的第十三文化。
哼！ 這才叫敵意！
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #3 · ABOUT_URQUAN_1 · ✨ canonical: 里恩克→里溫克

**英文原文**:
```
A foolish question! We are their slaves, dolt! What else would we be?
When the Ur-Quan first appeared in our space over fifty years ago
coming from the direction of the Ophiuchi stars
we attacked them with gusto, zipping in to fire our Mark 6 blasters
and then theoretically zipping back out to prepare for another attack run.
SNORT! Unfortunately, before we could zip out
our ships were either blasted to smithereens by the Ur-Quan's fusion bolts
or were picked apart by the swarms of Ur-Quan fighter-vessels.
You may wonder why we didn't use our afterburners to escape. The answer is simple.
Fifty years ago, our ships had not yet been modified for this enhancement!
It was not until 2143 that Maintainance Engineer Reeunk invented the afterburner effect
when he accidentally stuck his cigar in the aft fuel valve of the ship he was working on.
WHABOOM!!! The ship took off like a farg out of hell, and Reeunk was fried to a crisp.
Yes, we remember Reeunk with much fondness. Of course, we have refined the device
and now that our entire fleet has been fitted with the Reeunk Afterburners
...
```

**Shipped v0.3**:
```
愚蠢之問！ 吾等乃其奴隸,呆瓜！ 還能是什麼？
五十多年前,烏寬首度出現於吾等領空
自蛇夫（Ophiuchi）方向而來
吾等以熱情迎戰,飛入以射擊吾等之六型爆能砲
然後,理論上,飛出以準備下一波攻擊。
哼！ 可惜,在吾等能飛出之前
吾等之艦艇不是被烏寬之融合彈炸得粉身碎骨
就是被烏寬蜂擁之戰機拆解殆盡。
爾或問吾等為何不用後燃器逃脫。 答案很簡單。
五十年前,吾等艦艇尚未加裝此強化裝置！
直至 2143 年,維修工程師里恩克（Reeunk）才意外發明後燃器（Afterburner）
那時他不小心把雪茄插進他當時所修艦艇之尾部燃料閥。
轟隆隆──！！！（WHABOOM!!!） 該艦艇如地獄野火般彈射而出,里恩克本人則被烤成焦屑。
是的,吾等對里恩克記憶猶新。 當然,吾等已改良此裝置
如今吾等整支艦隊皆已裝配里恩克後燃器
```

**Rebuild v3**:
```
蠢問題！ 我方是他們的奴隸,蠢材！ 不然還能是什麼？
烏寬五十多年前第一次出現在我方領空
從蛇夫座那個方向來
我方興高采烈上前攻擊,衝進去發射六型爆能砲
理論上再衝出來準備下一波攻擊。
哼！ 可惜還沒衝出來
我方艦艇要嘛被烏寬的融合彈轟成碎片
要嘛被烏寬戰機群啃食殆盡。
你可能想問我方為什麼沒用後燃器逃跑。 答案很簡單。
五十年前,我方艦艇還沒改裝出這個功能！
一直到 2143 年,維修工程師里溫克（Reeunk）才發明後燃器（Afterburner）效應
當時他不小心把菸屁股插進正在維修的船的後部燃料閥。
轟隆隆──！！！（WHABOOM!!!） 那船像地獄裡的 farg 一樣衝出去,里溫克當場被烤成脆片。
沒錯,我方很懷念里溫克。 當然啦,我方已經改良過裝置
現在我方全艦隊都裝上「里溫克後燃器」
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #4 · BLUE_HELIX · ✨ canonical: 芬特→放特

**英文原文**:
```
Very well, since we have a huge number of ships here
I guess there can't be much harm in explaining this to you
PROVIDED YOU LEAVE WHEN WE'RE DONE!
So listen carefully.
Below us
on the surface of this planet
on the dark continent of Funt
high on a mountain
in an ancient shrine
resting in a special ceremonial cradle
glowing with its magical blue light, is the
NO! I've changed my mind! You don't get to know the answer.
Sorry.
```

**Shipped v0.3**:
```
很好,既然吾等於此擁有大量艦艇
吾想解釋此事應無大礙
但爾必須聽完就離開！
所以仔細聽。
吾等下方
此行星之表面
芬特（Funt）暗黑大陸上
一座高山之巔
一座古老之神殿中
安放於一特殊祭儀搖籃之內
以其奇異藍光發亮之物,便是
不！ 吾改變主意了！ 爾不能知道答案。
抱歉。
```

**Rebuild v3**:
```
好吧,既然我方在這裡有大量艦艇
跟你解釋這件事應該沒什麼危害
只要你聽完就閃！
仔細聽好。
在我方下方
這顆行星的表面
放特（Funt）暗黑大陸上
一座高山之巔
一座古老神殿之中
安放於特殊祭儀搖籃
發著魔幻藍光的,便是
不！ 我改變主意了！ 你不能知道答案。
抱歉。
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #5 · HELIX_IS_HOSTILE · ✨ canonical: 芬特→放特

**英文原文**:
```
Okay, okay. I guess you're right, it was a bit cruel. I'll tell you.
Let's see, where was I? Oh, right
on the dark continent of Funt
high on a mountain
in an ancient shrine
resting in a special ceremonial cradle
glowing with its magical blue light, is the
AQUA HELIX!
...the most revered of all Thraddash relics
the sign of any Culture's authority.
```

**Shipped v0.3**:
```
好吧,好吧。 吾想爾說得對,方才有些殘酷。 吾告訴爾吧。
嗯,吾說到哪了？ 噢,對
芬特暗黑大陸上
一座高山之巔
一座古老之神殿中
安放於一特殊祭儀搖籃之內
以其奇異藍光發亮之物,便是
蔚藍螺旋（Aqua Helix）！
……撻伐族所有遺物中最神聖之物
每一個文化權威之象徵。
```

**Rebuild v3**:
```
好啦,好啦。 我想你說得對,剛才有點殘忍。 我告訴你。
嗯,我剛講到哪了？ 喔,對
放特暗黑大陸上
一座高山之巔
一座古老神殿之中
安放於特殊祭儀搖籃
發著魔幻藍光的,便是
蔚藍螺旋（AQUA HELIX）！
……撻伐族所有遺物中最神聖的
每個文化權威的象徵。
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #6 · HELLO_RHYME_3 · ✨ canonical: 馬可尼→馬克-羅尼

**英文原文**:
```
There once was a Thraddash named Mak-Roni
whose ship was in total caco-phony
He got lost in Apodis
and died in Draconis
Because all that he ate was baloney!
HARG! HARG! HARG!
```

**Shipped v0.3**:
```
從前有個撻伐名為馬可尼（Mak-Roni）
他的艦艇響如刺耳雜音
於天燕座他迷失路線
在天龍座他喪命歸天
只因所食全是無稽之言！
哈！哈！哈！（HARG! HARG! HARG!）
```

**Rebuild v3**:
```
從前有隻撻伐叫馬克-羅尼
他的船整艘雜音亂到極致
他在天燕座迷路
死於天龍座的歸宿
只因他吃的都是廢話一堆！
哈！哈！哈！
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #7 · HELLO_LIKE_YOU_2 · ✨ canonical: 查德→恰德

**英文原文**:
```
Greetings! I am Captain Chudd in command of the Blazing Guns of Glory!
```

**Shipped v0.3**:
```
問候！ 吾乃查德（Chudd）艦長,指揮「榮耀熾焰砲號」（Blazing Guns of Glory）！
```

**Rebuild v3**:
```
問候！ 我是恰德（Chudd）艦長,指揮「榮耀熾焰砲號」（Blazing Guns of Glory）！
```

**推薦**: B(v3 - 採用 v0.7 canonical 升級)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #8 · HOSTILE_SPACE_HELLO_1 · 🟠 文言 cleanup

**英文原文**:
```
So, what's this? SNORT! An unknown alien species?
How wonderful! Someone new to fight!
We, the Thraddash of Culture Nineteen -- famous Ur-Quan Combat Thralls
know well the value of a good fight.
Either you win and prove your superiority...
SNORT! Or you lose and are vanquished.
If the vanquished is lucky, it may survive to learn an important lesson from its defeat.
This is the way of the Thraddash! We fight and learn and improve!
All other cultural schemes are inferior. This is a proven fact.
What have you to say before we begin combat?
```

**Shipped v0.3**:
```
所以呢？ 哼！（SNORT!） 一種未知外星物種？
多麼美妙！ 有新對手可打了！
吾等,第十九文化之撻伐族 —— 聞名之烏寬戰奴
深知一場好戰之價值。
要不爾贏,證明爾之優越……
哼！（SNORT!） 要不爾輸,被擊敗殆盡。
若敗者運氣好,或可倖存以從失敗中習得重要教訓。
此即撻伐族之道！ 吾等戰鬥、學習、進步！
所有其他文化構思皆為劣等。 此乃已證實之事實。
爾等於吾等開戰之前有何話說？
```

**Rebuild v3**:
```
那個是啥？ 哼！（SNORT!） 一種沒見過的外星物種？
太棒了！ 有新對手可以打了！
我們撻伐族,第十九文化,舉世聞名的烏寬戰奴
深深懂得一場好戰的價值。
要嘛你贏了,證明自己比較強……
哼！ 要嘛你輸了,被打趴在地。
如果敗者運氣好,搞不好還能活下來,從失敗學到重要一課。
這就是撻伐族的道！ 我們打、我們學、我們進步！
其他所有文化構想都是二流貨。 這是鐵一般的事實。
開打之前,你有什麼話要說？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #9 · HOSTILE_SPACE_HELLO_2 · 🟠 文言 cleanup

**英文原文**:
```
SNORT! What a laugh! You are the least battle-worthy creature I've ever seen commanding a starship.
We are the Ur-Quan fighting slaves of Culture Nineteen.
Please don't run away. We wish to be your species' new role-models!
Unfortunately, to do this, we may need to blast you into your component atoms.
```

**Shipped v0.3**:
```
哼！（SNORT!） 何等笑話！ 爾乃吾所見過最不堪一戰之生物,竟指揮一艘星艦。
吾等乃第十九文化之烏寬戰奴。
請莫逃跑。 吾等欲成為爾等物種之新典範！
可惜為達此目的,吾等可能得將爾等炸成粉末原子。
```

**Rebuild v3**:
```
哼！ 真好笑！ 你是我看過指揮星艦的生物裡最不會打的一個。
我們是第十九文化的烏寬戰奴。
拜託別跑。 我們想成為你們這個物種的新典範！
可惜為了達到這個目標,可能得先把你們炸成基本原子。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #10 · HOSTILE_SPACE_HELLO_3 · 🟠 文言 cleanup

**英文原文**:
```
Attention weak, ugly humans aboard that wallowing garbage scow of a ship, SNORT!
Unless you are even more inferior than we believe and that's hard to imagine
you already know who we are -- the Thraddash of Culture Nineteen
We are the original Ur-Quan fighting slaves, the cream of their elite forces
your instructors in the harsh realities of life.
SNORT! It is time for your next lesson.
```

**Shipped v0.3**:
```
聽好爾等這些軟弱、醜陋的人類,乘在那艘搖搖晃晃如垃圾船之艦艇上,哼！
除非爾等比吾等想像的還要低劣,而那是很難想像的
爾等已知吾等是誰 —— 第十九文化之撻伐族
吾等乃烏寬最原始之戰鬥奴隸,精銳部隊之精英
爾等於生命嚴酷現實之導師。
哼！ 此刻是爾等下一堂課之時。
```

**Rebuild v3**:
```
注意了,那艘搖搖晃晃的垃圾破船上又醜又弱的人類們,哼！
除非你們比我方想的還劣等 —— 那真的很難想像
不然你們應該已經知道我們是誰 —— 第十九文化的撻伐族
我們是烏寬最早的戰奴,他們菁英部隊裡的精華
是教你們認清人生殘酷現實的老師。
哼！ 你們下一堂課的時間到了。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #11 · HOSTILE_SPACE_HELLO_4 · 🟠 文言 cleanup

**英文原文**:
```
Inferior Aliens. You have once again intruded upon the territory of the Thraddash.
This is a patrolled region of space. Your presence here is considered an act of War!
How wonderful!
```

**Shipped v0.3**:
```
劣等外星人。 爾等又一次擅闖撻伐族領土。
此為受巡邏之太空區域。 爾等之出現視同宣戰之舉！
多麼美妙！
```

**Rebuild v3**:
```
劣等外星人。 你們又再次擅闖撻伐族的領地。
這裡是巡邏區。 你們的出現被視為戰爭行為！
真是太棒了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #12 · HOSTILE_HOMEWORLD_HELLO_1 · 🟠 文言 cleanup

**英文原文**:
```
HA! View the stupid weak alien who has appeared here at our homeworld!
What do you desire, creature? Our Friendship? Our submission?!
HARG! HARG! HARG!
Foolish, dumb weakling! We, the Nineteenth Culture of the Thraddash Empire
have an enormous fleet of ships here, with which to instruct you!
We will gladly attack you -- in fact, it is a requirement that we do so
since we are Ur-Quan slaves, and you are obviously an independent.
But know this! SNORT! Pay close heed!
While it is true we keep count of the number of our ships you destroy
we consider attacking our homeworld SO irrevocably stupid
that any victories you may score here through a sheer stroke of luck
WILL NOT be added to your personal victory tally!
Now what do you wish of us before we attack?
```

**Shipped v0.3**:
```
哈！ 看看這蠢弱之外星人,竟出現於吾等母星！
生物,爾欲何求？ 吾等之友誼？ 吾等之屈服？！
哈！哈！哈！（HARG! HARG! HARG!）
愚昧、笨拙之弱者！ 吾等,撻伐帝國之第十九文化
此地擁有龐大艦隊,可用以教訓爾等！
吾等將樂意攻擊爾等 —— 事實上,吾等必須如此
因吾等乃烏寬奴隸,而爾顯然為獨立單位。
然而聽好！ 哼！ 特別留意！
雖說吾等會記錄爾等擊毀之艦艇數量
吾等視攻擊吾等母星為極端愚蠢之行為
即使爾等因僥倖於此獲得勝利
將不會計入爾等個人之戰功名單！
如今於吾等開火之前,爾欲對吾等有何求？
```

**Rebuild v3**:
```
哈！ 快看那個蠢弱的外星人,竟然跑到我們的母星來了！
你想要什麼,小生物？ 我們的友誼？ 我們的臣服？！
哈！哈！哈！（HARG! HARG! HARG!）
蠢貨,笨蛋弱者！ 我們撻伐帝國第十九文化
在這邊有一支龐大的艦隊,足以好好教訓你！
我方很樂意攻擊你 —— 事實上這是我方的義務
因為我們是烏寬的奴隸,而你顯然是獨立星際個體。
但你聽好了！ 哼！ 給我聽清楚！
沒錯,你摧毀我方艦艇的數字我們有在記
但攻擊我方母星這件事我方認為蠢到不可挽回
所以你在這裡如果靠純運氣拿下任何勝績
一律不會計入你個人的戰績！
現在,開打之前你想從我方這裡得到什麼？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #13 · HOSTILE_HOMEWORLD_HELLO_2 · 🟠 文言 cleanup

**英文原文**:
```
Attention cowardly alien human thing!
You escaped our instructional session, SNORT! But this time things are different.
We, the Ur-Quan slaves of Culture Nineteen,
have engaged in a long-term build-up of weapons, assuring us that we shall prevail!
If you wish merely to count coup, seek our ships in space.
Now do you wish to speak, or shall we simply start blasting?
```

**Shipped v0.3**:
```
聽好爾這膽小的外星人類物！
爾逃過吾等之教訓課,哼！ 但此次情況不同。
吾等,第十九文化之烏寬戰奴,
已進行長期武器建設,確保吾等必勝！
若爾僅欲炫耀戰功,去太空尋找吾等艦艇。
如今爾欲開口,還是吾等直接開火？
```

**Rebuild v3**:
```
注意了,膽小的外星人類東西！
你上次逃過我方的教學課,哼！ 但這次情況不一樣了。
我們,第十九文化的烏寬戰奴,
已經長期加強武備,足以確保我方一定會贏！
如果你只想累積戰功,去太空找我方艦艇。
現在,你想說話,還是我們直接開轟？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #14 · HOSTILE_HOMEWORLD_HELLO_4 · 🟠 文言 cleanup

**英文原文**:
```
Foolish Aliens! Shall you never learn the futility
of trying to conquer our homeworld through direct attack?
It is impossible! SNORT! We Thraddash will toast your tootsies.
Your charred bodies will be fertilizer for our fodderland.
A great fight, resulting in a glorious Thraddash victory, awaits you here!
```

**Shipped v0.3**:
```
愚昧外星人！ 爾等難道永不學乖
直接攻擊吾等母星之徒勞？
此為不可能之事！ 哼！ 吾等撻伐族將烤焦爾等之腳趾。
爾等焦黑之屍體將成為吾等牧草地之肥料。
一場壯烈之戰、一次光榮之撻伐族勝利,在此等候爾等！
```

**Rebuild v3**:
```
蠢貨外星人！ 你們難道永遠學不會嗎？
想直接攻擊來征服我方母星這種事根本徒勞。
不可能的！ 哼！ 我方撻伐族會烤焦你們的腳趾頭。
你們燒焦的屍體會變成我方牧草地的肥料。
一場光榮的撻伐大勝正在這裡等著你們！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #15 · whats_up_hostile_1 · 🟠 minor 文言 cleanup

**英文原文**:
```
Thraddash of Culture Nineteen: we sense a bit of hostility here. Why?
```

**Shipped v0.3**:
```
第十九文化之撻伐族們：我方感覺此處有些敵意。 為何？
```

**Rebuild v3**:
```
第十九文化的撻伐族們：我方感覺這裡有些敵意。 為什麼？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #16 · GENERAL_INFO_HOSTILE_2 · 🟠 文言 cleanup

**英文原文**:
```
Brutal!? You don't know the MEANING of brutal until you've heard the story of Culture Three!
How brutal WAS Culture Three you ask?
Culture Three was SO brutal that they maimed, tortured, enslaved, and in general brutalized
THEMSELVES!
You see, Culture Two had made a virtue of stoic resistance to pain, stubborn fortitude, that sort of thing.
So when Culture Three came around, they had a problem.
How were they going to impress everyone as being EVEN TOUGHER?
Their answer? They would arrive at a battle, stand on a tall hill where everyone could see them
and chop off one of their own limbs! Then they'd wave it around, screaming and shaking it at their enemies.
It worked! It scared the hell out of their opponents! They ran like crazy!
You could tell who was a real war hero back then by how few arms or legs he had left.
War parades were quite different too. Instead of sturdy old warriors walking slowly past the reviewing stands
they tended to roll, and at a good clip, too.
To you, an inferior alien, this may seem bluntly stupid -- the product of a sick, primitive society.
SNORT! You couldn't be more right!
...
```

**Shipped v0.3**:
```
兇殘！？ 未聞第三文化之事,爾等不知「兇殘」之真意！
爾等問第三文化究竟多兇殘？
第三文化之兇殘達到殘害、折磨、奴役,總之霸凌
他們自己！
爾等要知,第二文化以斯多葛式的忍痛、頑強不屈為美德。
所以當第三文化崛起,他們遇到一個問題。
他們該如何顯得比人更硬派？
答案？ 他們赴戰場時,站上一座人人可見的高丘
然後砍下自己一條肢！ 接著揮舞它,對敵人尖叫、揮舞恫嚇！
此招奏效！ 嚇壞敵人！ 敵人四散奔逃！
判斷誰是真正的戰爭英雄,只需看他還剩幾條手腳。
閱兵儀式亦因此大不相同。 不再是老兵緩步走過檢閱台
他們是滾動而過,速度還不慢。
對爾這劣等外星人而言,此舉或許看似鈍愚 —— 病態原始社會之產物。
哼！ 爾說得再對不過！
```

**Rebuild v3**:
```
兇殘？！ 你聽了第三文化的故事以前,根本不懂什麼叫兇殘！
你問第三文化到底有多兇殘？
第三文化兇殘到,他們自殘、自虐、把自己奴役,反正各種兇殘
對自己！
你想想,第二文化把默默忍痛、頑強不屈之類的當成美德。
所以第三文化接手的時候有個難題。
他們要怎麼讓大家覺得他們更硬？
答案是？ 一到戰場,他們就站在大家都看得到的高山上
然後把自己的一條肢體砍下來！ 接著揮舞著,對敵人尖叫抖動。
奏效了！ 對手嚇得屁滾尿流！ 他們像瘋子一樣逃跑！
那時候真正的戰爭英雄怎麼認？ 就看他還剩幾隻手腳。
軍隊遊行也很不一樣。 不是強健的老兵慢慢走過觀禮台
而是連滾帶爬,而且速度還挺快。
在你這個劣等外星人眼裡,這聽起來大概蠢到極點 —— 病態原始社會的產物。
哼！ 你說的一點也沒錯！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #17 · GENERAL_INFO_HOSTILE_3 · 🟠 文言 cleanup

**英文原文**:
```
NO! We will not answer any more of your foolish questions!
Instead, you will answer OUR questions, such as
who is responsible for those berserk red probes that keep attacking our ships?
Are these devices your robot emissaries of death? Hmm?
No! Don't answer, I can see it in your eyes. You've given it all away! SNORT! I know the truth now.
The only thing that confuses me is WHY do the probes approach from the direction of <% comm.getConstellation("Vega", "slylandro") %>?
```

**Shipped v0.3**:
```
不！ 吾等不再回答爾等愚蠢之問題！
反倒,爾等該回答吾等之問題,例如
那些不斷攻擊吾等艦艇之瘋狂紅色探測器是誰所造？
那些裝置乃爾等之機器死亡使者嗎？ 嗯？
不！ 別答,吾從爾之眼神看出來了。 爾已洩漏一切！ 哼！ 吾如今知曉真相。
唯一讓吾困惑的是,那些探測器為何自 <% comm.getConstellation("織女星", "slylandro") %>（Vega）方向而來？
```

**Rebuild v3**:
```
不行！ 我方不會再回答你任何蠢問題了！
反過來,你要回答我方的問題,例如
是誰在指揮那些狂暴的紅色探測器,老是攻擊我方艦艇？
這些機器是你們死神般的機器人使者嗎？ 嗯？
別！ 別回答,你的眼神都告訴我了。 你全洩漏出來了！ 哼！ 我現在知道真相了。
唯一讓我疑惑的是,為什麼那些探測器從 <% comm.getConstellation("織女星", "slylandro") %> 那個方向過來？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #18 · GENERAL_INFO_HOSTILE_4 · 🟠 文言 cleanup

**英文原文**:
```
Back to the subject of the probes!
We found one orbiting a strange planet in the <% comm.getStarName("Epsilon Draconis", "rainbow 5") %> system.
The planet causes our scanners to malfunction, producing a wildly colored image.
The probe seemed to be studying it. Is this true?
SPEAK, HUMAN! REVEAL THE TRUTH! CONFESS YOUR CRIMES!
Well, if you will not cooperate
we will have to extract the information from you in more painful ways.
```

**Shipped v0.3**:
```
回到探測器之話題！
吾等於 <% comm.getStarName("天龍座ε", "rainbow 5") %>（Epsilon Draconis）星系發現一具環繞著奇異行星運行。
該行星使吾等感測器失常,產生一幅色彩狂亂之圖像。
那探測器似在研究它。 此事屬實嗎？
說話,人類！ 揭露真相！ 招認爾之罪行！
嗯,若爾不肯合作
吾等只得以更痛之法,自爾身上榨出情報。
```

**Rebuild v3**:
```
回到探測器的話題！
我方發現一個繞著 <% comm.getStarName("天龍座ε", "rainbow 5") %> 星系裡一顆怪行星轉。
那顆行星害我方掃描器失靈,顯示出五顏六色的亂圖。
探測器好像在研究它。 是真的嗎？
說吧,人類！ 說出真相！ 供認你的罪行！
好啦,你不合作
那我方只好用更痛的方式把資訊從你身上榨出來。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #19 · ABOUT_US_1 · 🟠 文言 cleanup

**英文原文**:
```
Talk! Bah, talk is for sissies, weaklings like those of Culture Fourteen.
For ten thousand years, we Thraddash have fought and died, learned and improved.
Then, along came Culture Fourteen which claimed that all this -- this perfect method...
...was wrong! -- that each time we violently transformed to a new Culture
we inevitably blasted ourselves back at least five hundred years in development.
Hmph! Some people just cannot accept the cost of progress.
Indeed, the FOOLISHNESS of Culture Fourteen's peaceful whining was revealed
when they were conquered by Culture Fifteen after only a ten year reign.
And did the change to Culture Fifteen set us back five hundred years?
NO! SNORT!
Two, maybe three hundred years, tops.
The short span of Culture Fourteen's reign is objective proof that as a way of life
peace is a failure.
```

**Shipped v0.3**:
```
說話！ 呸,說話乃娘炮之事,如第十四文化那群軟弱之輩。
一萬年來,吾等撻伐族戰、亡、學、進。
然後,第十四文化出現,聲稱這一切 —— 這完美之法……
……是錯的！ 說吾等每次暴力轉入新文化
必將自身之發展炸退至少五百年。
哼！ 有些人就是無法接受進步之代價。
事實上,第十四文化和平主義之愚蠢在其被第十五文化征服之時暴露無遺
他們僅統治了十年。
那麼,轉入第十五文化的變動有把吾等倒退五百年嗎？
沒有！ 哼！
頂多兩、三百年而已。
第十四文化統治之短暫,乃客觀證據,證明作為一種生活方式
和平是失敗。
```

**Rebuild v3**:
```
講話！ 呸,講話是娘娘腔的事,像第十四文化那種弱者才在做。
過去一萬年,我們撻伐族戰鬥、死亡、學習、進步。
然後第十四文化冒出來,聲稱這一切 —— 這套完美的方法……
……是錯的！ —— 說我們每次暴力轉型到新文化
就無可避免把自己的發展往回炸至少五百年。
哼！ 有些人就是接受不了進步的代價。
的確,第十四文化那套愛好和平的哀嚎有多蠢,一目了然
才統治十年就被第十五文化征服。
換到第十五文化真的害我方退步五百年嗎？
沒有！ 哼！
頂多兩、三百年吧。
第十四文化短命的統治客觀證明,把和平當生活方式
就是失敗。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #20 · ABOUT_US_2 · 🟠 文言 cleanup

**英文原文**:
```
What!?! SNORT! MORE talk?
It amazes me that you ever got out of the orbit of your home planet!
Yak! Yak! Yak! -- Yammer! Yammer! Yammer!
Sigh... very well, we will talk... for a moment.
Our Culture Nineteen is the most formidable ever to appear in Thraddash space.
Admittedly, we said something similar about Culture Eighteen, BUT IT IS TRUE!
With our rather swift defeat by the Ur-Quan and subsequent enslavement
we realized that it was time for a change! A new Culture had to be established!
So, of course, we began a thermo-nuclear exchange to decide who would lead this new culture.
We were all quite disappointed when the Ur-Quan in orbit above our homeworld
launched waves of fighters who intercepted all our missiles.
The Ur-Quan explained that slaves were not permitted to engage in such destructive conflicts
so my people, being superior, introduced a super-lethal poison into our opponents' water and air
thus ending the conflict, HARG! HARG! HARG!
The Ur-Quan were not particularly happy about this resolution, and killed all of our leaders
...
```

**Shipped v0.3**:
```
什麼？！ 哼！ 又要說話？
吾感驚訝爾竟能出得了母星軌道！
呀！ 呀！ 呀！ —— 嘮！ 嘮！ 嘮！
嘆……好吧,吾等再說……片刻。
吾等之第十九文化,乃撻伐族領空歷來最強大之文化。
吾承認,吾等對第十八文化也說過類似之語,但這次是真的！
隨著吾等迅速敗於烏寬並被隨後奴役
吾等意識到,是時候求變了！ 新文化必須建立！
所以,吾等當然開始一場熱核交火,以決定誰將領導此新文化。
吾等相當失望地發現,盤旋於吾等母星上空之烏寬
派出一波波戰機,攔截吾等所有飛彈。
烏寬解釋,奴隸不許參與此等破壞性衝突
故吾之族人,基於優越之天性,遂於敵人之水與空氣中
注入一種超致命之毒素,結束此衝突,哈！哈！哈！
烏寬對此結局不甚滿意,遂殺盡吾等所有領袖
```

**Rebuild v3**:
```
什麼！？！ 哼！ 又要講話？
你們居然能離開母星軌道,真是讓我方震驚！
呀！呀！呀！ —— 煩！煩！煩！
唉……好啦,我方就講一下……講一下就好。
我方的第十九文化是撻伐太空有史以來最厲害的。
好啦,關於第十八文化我方也講過類似的話,但這次是真的！
被烏寬迅速擊敗又被奴役之後
我方意識到,是時候變一變了！ 必須建立一個新文化！
所以嘛,當然,我方就展開熱核交換,決定誰要領導新文化。
結果我方超失望 —— 母星軌道上的烏寬
派了一波波戰機把我方所有飛彈都攔截下來。
烏寬解釋說,奴隸不准參與這種破壞性衝突
所以我族,身為菁英,把一種劇毒引入對手的水源和空氣中
就這樣結束衝突,哈！哈！哈！
烏寬對這種解法可不太開心,把我方領導人全部殺光
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #21 · ABOUT_URQUAN_2 · 🟠 文言 cleanup

**英文原文**:
```
We wanted to, OH how we wanted to!
After all, we were the first battle thralls the Ur-Quan enslaved in this part of space
we thought we had priority!...
but the Ur-Quan thought we were too weak to hold our own in the upcoming battles
so they left us here... to guard the flank.
If only we had been WHIMPER! stronger and less... SNARF! troublesome.
Another reason the Ur-Quan wouldn't take us with them
was because we kept picking fights with the new battle slaves
like the Umgah blobbies, or those religious idiots, the Ilwrath.
Where did they go, you ask? This is a secret, of course! We can't tell you!
If we told you that they were fighting a secret war against a mysterious invader
you might find some way to use that information against our masters.
So forget it! No secrets!
```

**Shipped v0.3**:
```
吾等想戰,噢有多想戰！
畢竟,吾等乃烏寬於此區奴役之首批戰奴
吾等以為有優先權！……
但烏寬認為吾等太弱,無法於即將之戰役中支撐
遂將吾等留在此……顧後方。
若吾等只是嗚咽！（WHIMPER!） 再強一點、少些……呼哧！（SNARF!） 麻煩就好。
烏寬不帶吾等同行之另一原因
乃因吾等總是與新戰奴挑釁
如陰嘎族那些黏塊,或那群宗教白癡蛛狂族。
爾問他們去哪了？ 此當然是秘密！ 吾等不能告訴爾！
若吾等告訴爾,他們正打一場對抗神秘入侵者之秘密戰爭
爾或可利用此情報反擊吾等之主宰。
所以,忘了吧！ 沒有秘密！
```

**Rebuild v3**:
```
我方超想的,喔天我方超想的！
畢竟我方是烏寬在這一區奴役的第一批戰奴
我方以為有優先權！……
但烏寬覺得我方太弱,在即將到來的戰役裡撐不住
所以把我方留在這裡……顧側翼。
要是我方當初 嗚咽！（WHIMPER!） 更強一點、少一點……呼哧！（SNARF!） 找麻煩就好了。
烏寬不帶我方一起走的另一個原因
是我方老是跟新戰奴打架
像陰嘎族的果凍怪,或那群宗教白痴蛛狂族。
你問他們去哪了？ 這當然是秘密！ 我方不能告訴你！
要是我方告訴你他們正在對某個神秘入侵者打一場密戰
你搞不好會想辦法拿這情報對付我方主子。
所以算了！ 沒什麼秘密可講！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #22 · got_idea · 🟠 minor 文言 cleanup

**英文原文**:
```
Hey, I've got an idea! Why don't you go impress your Ur-Quan masters AND show-off your Afterburner modification by attacking the Ur-Quan's enemy!?
```

**Shipped v0.3**:
```
嘿,我方有個主意！ 何不去讓你們的烏寬主宰刮目相看,順便炫耀後燃器改裝 —— 去攻擊烏寬之敵！？
```

**Rebuild v3**:
```
嘿,我方有個主意！ 何不去讓你們的烏寬主宰刮目相看,順便炫耀後燃器改裝 —— 去攻擊烏寬的敵人！？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #23 · GOOD_IDEA · 🟠 文言 cleanup

**英文原文**:
```
WHAT FOOLISH STUPIDITY! HARG! HARG! HARG!
WHY THAT'S AS DUMB AN IDEA AS -- what did you say?
Attack the Ur-Quan's enemy? Help them win their war?
Why that's a... that's a... THAT'S AN EXCELLENT IDEA!
I'm glad I thought of it!
We shall marshal our forces and leave at once!
Stupid, human pitiful weakling dog, you have been helpful, so as a reward
you may leave alive, and when we return from our glorious campaign
we may even honor you with a retelling of the many great battles we shall certainly win.
Until then, get lost.
```

**Shipped v0.3**:
```
何等愚蠢之言！ 哈！哈！哈！
那簡直和 —— 爾說什麼？
攻擊烏寬之敵？ 助他們贏得戰爭？
那是一個……那是一個……那是絕妙好主意！
吾很高興是自己想到的！
吾等當召集部隊,立即出征！
愚蠢、可憐弱小之人類犬,爾曾助吾等一臂,故作為獎賞
爾可活著離去,待吾等自光榮之遠征歸來
吾等甚至可能授爾榮譽,為爾複述吾等必勝之眾多壯烈戰役。
在此之前,滾遠點。
```

**Rebuild v3**:
```
真是蠢到極點！ 哈！哈！哈！
這主意蠢到跟 —— 等等,你剛才說什麼？
攻擊烏寬的敵人？ 幫他們打贏戰爭？
這是……這是……這是絕妙的主意！
還好我想到了！
我方將集結兵力,即刻出征！
蠢人類、可悲的弱者狗,你幫了大忙,作為獎賞
你可以活著離開,等我方從光榮戰役歸來
搞不好還會賞你聽聽我方必勝的許多輝煌戰役故事。
在那之前,滾。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #24 · WE_GO_TO_IMPRESS_URQUAN_1 · 🟠 文言 cleanup

**英文原文**:
```
The Ur-Quan will be mightily impressed by our combat prowess
when we blast their enemies from space!
We build up a charging fury! Stay out of our path!
```

**Shipped v0.3**:
```
當吾等自太空炸飛烏寬之敵時
烏寬將對吾等之戰鬥技能大為震撼！
吾等已聚集狂怒之衝勢！ 莫擋吾等之路！
```

**Rebuild v3**:
```
烏寬會被我方戰鬥實力震撼
就在我方把他們的敵人從太空轟掉的時候！
我方鬥氣正盛！ 別擋路！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #25 · WE_GO_TO_IMPRESS_URQUAN_2 · 🟠 文言 cleanup

**英文原文**:
```
Our individual skills, our superior fighting ships
and our objectively correct political views
are sure to greatly impress our Ur-Quan Masters!
To Arms! SNORT! To Arms!
```

**Shipped v0.3**:
```
吾等之個人技藝、吾等優越之戰艦
以及吾等客觀正確之政治見解
必將令吾等之烏寬主宰大為震撼！
上戰場！ 哼！ 上戰場！
```

**Rebuild v3**:
```
我方個人的技巧、我方優越的戰艦
還有我方客觀正確的政治觀點
必定能讓烏寬主子大為震撼！
拿起武器！ 哼！ 拿起武器！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #26 · WE_IMPRESSING_URQUAN_1 · 🟠 文言 cleanup

**英文原文**:
```
Oh! The Weapons!! The devastating bolts of sheer energy! SNORT!
The dark ships -- the Ur-Quan's enemies, they bow before our superior technologies!
The morbid, relentless wheels of heart-pounding destructiveness
are nothing more than an inconvenience!
Oh, yes! I am sure that we are demonstrating to the Ur-Quan
the worthiness of our excellent Culture Nineteen!
```

**Shipped v0.3**:
```
噢！ 那些武器！！ 那毀滅性之純能量爆炸！ 哼！
那些黑艦 —— 烏寬之敵,在吾等優越之科技前臣服！
那些病態、無情、震撼心跳之毀滅之輪
不過是件小小之不便！
噢,是的！ 吾深信吾等正向烏寬展示
吾等優秀之第十九文化之價值！
```

**Rebuild v3**:
```
喔！ 那些武器！！ 純粹能量射出的毀滅性衝擊波！ 哼！
那些黑船 —— 烏寬的敵人,他們在我方優越的科技面前俯首稱臣！
那些病態、絕不停歇的破壞輪子,心跳加速
不過是點小麻煩罷了！
喔沒錯！ 我方肯定正在向烏寬展示
我方傑出第十九文化的價值！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #27 · WE_IMPRESSING_URQUAN_2 · 🟠 文言 cleanup

**英文原文**:
```
We look forward to success!
The way is challenging, but our Turbo-Thrusters are at 200% and our guns stand ready!
We have engaged the dark ships and achieved victory!
The Ur-Quan know we are here! SNORT! They see our valor!...
...unfortunately they also seem to be attacking us.
We have tried to make contact with them on the usual HyperWave bands, but to no avail.
Even so, I am still quite sure that we are impressing them GREATLY!
```

**Shipped v0.3**:
```
吾等期待勝利！
路途艱難,然吾等渦輪推進器已達 200%,武器蓄勢待發！
吾等已與黑艦交戰,獲得勝利！
烏寬知曉吾等在此！ 哼！ 他們見到吾等之英勇！……
……可惜他們似也在攻擊吾等。
吾等已試著於通用超波頻段與其聯絡,然無果。
即便如此,吾仍相當肯定吾等已令他們大為震撼！
```

**Rebuild v3**:
```
我方期待勝利！
路上很挑戰,但我方渦輪推進器全開 200%,砲門也蓄勢待發！
我方已與黑船交戰並取得勝利！
烏寬知道我方在這！ 哼！ 他們看見我方的英勇！……
……可惜他們好像也在攻擊我方。
我方試過用常規的超波頻道跟他們聯絡,但沒回音。
就算這樣,我方還是很確定,我方讓他們大為震撼！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #28 · WE_IMPRESSED_URQUAN_1 · 🟠 文言 cleanup

**英文原文**:
```
The great gouts of flame! SNORT! The accuracy of our shooting!
We killed THOUSANDS... well at least HUNDREDS!
It was wonderful! It was delirious!
Those few of us who survived will have stories to tell for years to come.
We were marvelous! SNORT! They shook and shivered when they saw us coming!
They were so frightened of us, they froze in their tracks.
That's how scared they were!
Ah, such fighting! SNORT! We will not soon see the like again!
```

**Shipped v0.3**:
```
那壯麗之火焰！ 哼！ 吾等射擊之精準！
吾等殺了成千……好吧,至少上百！
那真是絕妙！ 那真是狂喜！
吾等少數倖存者將有故事可講許多年。
吾等真是精彩！ 哼！ 他們見吾等來時全身顫抖！
他們如此害怕吾等,以至於當場凍住。
他們就是那麼害怕！
啊,那場戰鬥！ 哼！ 短時間內吾等不會再見類似之壯烈！
```

**Rebuild v3**:
```
那些沖天火柱！ 哼！ 我方射擊的精準！
我方殺了幾千人……好啦,至少幾百人！
太美了！ 太狂了！
少數倖存的我方戰士會有故事講好幾年。
我方超猛！ 哼！ 他們看到我方過來時嚇得直發抖！
他們怕我方怕到定在原地不動。
就是那麼怕！
啊,這一戰！ 哼！ 短時間內我方都不會再見到這樣的戰役了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #29 · WE_IMPRESSED_URQUAN_2 · 🟠 文言 cleanup

**英文原文**:
```
Oh Yes! We have mightily impressed the Ur-Quan!
We destroyed several of their enemy's dreaded black ships
and severely damaged many more.
Our losses? Well, yes, there were a few.
But we are still very strong!
Make no mistake about that!
```

**Shipped v0.3**:
```
噢是的！ 吾等已大大震撼烏寬！
吾等擊毀了敵方數艘可怕之黑艦
並重創了更多。
吾等之損失？ 嗯,是有一些。
但吾等仍非常強大！
此事無可懷疑！
```

**Rebuild v3**:
```
喔沒錯！ 我方大大震撼了烏寬！
我方摧毀了他們敵人幾艘可怕的黑船
還重創了更多。
我方傷亡？ 呃,有一些啦。
但我方還是很強！
這點你可別搞錯！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #30 · HOSTILE_HELIX_HELLO_1 · 🟠 文言 cleanup

**英文原文**:
```
WARNING! You have entered Thraddash Secured Space!
There is nothing valuable here!
Go away!
```

**Shipped v0.3**:
```
警告！ 爾已進入撻伐族保護太空！
此處無任何價值之物！
滾開！
```

**Rebuild v3**:
```
警告！ 你已進入撻伐族保衛區！
這裡什麼有價值的都沒有！
滾！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #31 · HOSTILE_HELIX_HELLO_2 · 🟠 文言 cleanup

**英文原文**:
```
Begone Stupid, Ugly Ones!
SNORT!
Leave before we break from our guard posts and give you a good Thraddashing!
```

**Shipped v0.3**:
```
滾遠點,愚蠢、醜陋之輩！
哼！
離開此地,否則吾等將自崗位破襲而出,給爾好好上一頓撻伐！
```

**Rebuild v3**:
```
滾開,愚蠢又醜陋的東西！
哼！
在我方離開崗位好好給你來場撻伐痛擊之前趕快閃！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #32 · submit_1 · 🟠 minor 文言 cleanup

**英文原文**:
```
Your blustering does not impress me. We have requirements which you will fulfill, NOW!
```

**Shipped v0.3**:
```
你們之虛張聲勢並無效果。 我方有要求,你們現在給我照做！
```

**Rebuild v3**:
```
你們的虛張聲勢對我方沒用。 我方有要求,你們現在就給我照做！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #33 · NO_SUBMIT_1 · 🟠 文言 cleanup

**英文原文**:
```
Hunh?
Hnyarg?!
WHAT?!
SNARL! YOU SAY WHAT?!!!
Foolish, pitiful, small-headed being
WE WILL DEEESTROY YOUUU AND EVERYBODY ON YOUR SHIP!!
```

**Shipped v0.3**:
```
哈？
呃啊？！
什麼？！
咆哮！（SNARL!） 爾說什麼？！！
愚蠢、可憐、小腦袋之生物
吾等將毀滅爾與爾艦上所有人！！
```

**Rebuild v3**:
```
嗯？
啊？！（Hnyarg?!）
什麼？！
咆哮！（SNARL!） 你剛才說什麼？！！！
蠢材,可悲的小腦袋生物
我方將徹徹底底摧毀你你你和你艦上的所有人！！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #34 · submit_2 · 🟠 minor 文言 cleanup

**英文原文**:
```
I have secret weapons of great power. Submit, or I shall evaporate your planet.
```

**Shipped v0.3**:
```
我方有強大威力之秘密武器。 屈服,否則我方將蒸發你們的行星。
```

**Rebuild v3**:
```
我方有強大威力的秘密武器。 屈服,否則我方將蒸發你們的行星。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #35 · NO_SUBMIT_2 · 🟠 文言 cleanup

**英文原文**:
```
HARG! HARG! HARG!
We like secret weapons!
We will now give you the opportunity to give them to us.
```

**Shipped v0.3**:
```
哈！哈！哈！
吾等喜歡秘密武器！
吾等現在給爾機會將它們交給吾等。
```

**Rebuild v3**:
```
哈！哈！哈！
我方喜歡秘密武器！
我方現在就給你機會,把它們交出來。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #36 · NO_FRIENDS_1 · 🟠 文言 cleanup

**英文原文**:
```
Perhaps, after we have made you our slaves, we can accommodate your wishes.
Until then...
```

**Shipped v0.3**:
```
或許,待吾等將爾等奴役後,可如爾等所願。
在此之前……
```

**Rebuild v3**:
```
或許,等我方把你們變成奴隸之後,我方可以滿足你們的願望。
在那之前……
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #37 · NO_FRIENDS_2 · 🟠 文言 cleanup

**英文原文**:
```
We are strong. You are weak. And HARG! HARG!...
we HATE weak.
We do not need weak friends! We only want slaves and teachers.
Since you have nothing to teach us and refuse to be our slave
then you are our enemy.
Such logic must be obvious even to a stupid being like yourself.
```

**Shipped v0.3**:
```
吾等強大。 爾等軟弱。 而哈！哈！……
吾等憎恨軟弱。
吾等不需軟弱之友！ 吾等只要奴隸與導師。
既然爾等無物可教吾等,又拒絕當吾等之奴隸
那麼爾等即為吾等之敵。
此邏輯連爾這等愚昧之物亦顯而易見。
```

**Rebuild v3**:
```
我方很強。 你們很弱。 而且 哈！哈！……
我方超討厭弱者。
我方不需要弱的朋友！ 我方只要奴隸和老師。
既然你沒東西可以教我方,又拒絕當我方奴隸
那你就是我方的敵人。
這種邏輯連你這樣的蠢東西應該都看得懂。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #38 · IMPRESSED_LIKE_SO_1 · 🟠 文言 cleanup

**英文原文**:
```
It was glorious, truly glorious!... for the most part.
It would have been entirely glorious except for two factors.
Factor One: we lost over half our battle fleet during the two-week fracas.
Factor Two: of our casualties, only 60 percent were due to the Ur-Quan's enemy, the dark ships.
SNORT! The remaining 40 percent can be attributed to the Ur-Quan themselves.
We can be certain that we impressed them with at least one achievement
due to the Afterburner modification, we were somewhat harder for them to kill
than when they conquered us in the first place.
```

**Shipped v0.3**:
```
那真是光榮,真是光榮！……大部分而言。
本該全然光榮,若非以下兩個因素。
因素一:吾等於那兩週之混戰中損失超過半數之作戰艦隊。
因素二:吾等之損失中,僅百分之六十歸咎於烏寬之敵,即那些黑艦。
哼！ 其餘百分之四十可歸咎於烏寬本身。
吾等可肯定至少於一項成就上震撼了他們
因為後燃器改裝,吾等之艦艇比烏寬當初征服吾等時
要難殺得多。
```

**Rebuild v3**:
```
光榮啊,真是光榮！……大部分是啦。
要不是有兩個因素,本來會完全光榮的。
第一因素:我方在為期兩週的混戰中損失了超過一半的戰艦。
第二因素:我方傷亡中,只有 60% 是烏寬的敵人 —— 黑船造成的。
哼！ 剩下的 40% 得歸功於烏寬本人。
但可以確定我方至少在一項成就上讓他們印象深刻
託後燃器改裝的福,他們要幹掉我方比較難了
比起當年他們征服我方時要難一些。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #39 · how_impressed_urquan_2 · 🟠 minor 文言 cleanup

**英文原文**:
```
Would you describe the Ur-Quan's enemy ships?
```

**Shipped v0.3**:
```
能描述一下烏寬之敵的艦艇嗎？
```

**Rebuild v3**:
```
能不能描述一下烏寬敵人的艦艇？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #40 · IMPRESSED_LIKE_SO_2 · 🟠 文言 cleanup

**英文原文**:
```
They were black as space itself, with only the occasional glint off their hulls as they turned to fire.
Their weapons were extremely primitive, nothing more than fast-spinning disks of dense metal
yet they penetrated our defensive screens, and inflicted grievous damage
purely through their enormous kinetic energy.
The black ship's secret weapon is their ring of fire
which is VERY effective at short range.
Hey! Wait a minute! What am I doing answering YOUR questions?
Puny human, your time is almost up. Prepare yourself for defeat!
```

**Shipped v0.3**:
```
他們黑如太空本身,只偶爾於轉身開火時,船殼上閃過些微反光。
他們之武器極為原始,不過是快速旋轉之緻密金屬圓盤
然它們穿透吾等之防禦護盾,造成慘重損害
純粹靠其巨大之動能。
黑艦之秘密武器乃其火之環
於近距離時非常有效。
嘿！ 等等！ 吾為何在回答「爾」之問題？
渺小人類,爾之時辰將盡。 準備受敗！
```

**Rebuild v3**:
```
他們像太空一樣漆黑,只有轉身開火時船殼偶爾閃一下光。
他們的武器非常原始,不過是高速旋轉的高密度金屬圓盤
但那東西可以穿透我方防禦幕,造成慘重的傷害
純粹靠巨大的動能。
黑船的秘密武器是他們的火焰環
近距離下超級有效。
喂！ 等等！ 我怎麼在回答你的問題？
渺小的人類,你的時間快到了。 準備好接受失敗吧！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #41 · GOODBYE_HOSTILE_1 · 🟠 文言 cleanup

**英文原文**:
```
What? You leave before the lesson begins? We have so much to teach you!
Let us show you just one thing, it's called the `Surprise Attack'.
```

**Shipped v0.3**:
```
什麼？ 課還沒開始爾就要走？ 吾等有這麼多要教爾之事！
讓吾等只示範一項,名為「奇襲」。
```

**Rebuild v3**:
```
什麼？ 課還沒開始你就要走？ 我方有好多東西要教你！
讓我方跟你介紹一招,叫「突襲」。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #42 · GOODBYE_HOSTILE_2 · 🟠 文言 cleanup

**英文原文**:
```
Then I guess we'll just be attacking you now.
```

**Shipped v0.3**:
```
那麼吾等想吾等現在就要攻擊爾等了。
```

**Rebuild v3**:
```
那我方看來現在就得攻擊你了。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #43 · NONE_OF_YOUR_CONCERN · 🟠 文言 cleanup

**英文原文**:
```
It is none of your concern, human, SNORT!
Now leave this world before we get REALLY mad!
```

**Shipped v0.3**:
```
與爾無關,人類,哼！
離開此星球,否則吾等真的要發火了！
```

**Rebuild v3**:
```
不干你的事,人類,哼！
在我方真的生氣之前,快離開這個星球！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #44 · NO_DEMAND · 🟠 文言 cleanup

**英文原文**:
```
You will make no demands, stupid captain human dog!
Instead, you will die!
```

**Shipped v0.3**:
```
爾等不許提任何要求,愚蠢的人類艦長犬！
反之,爾等將死！
```

**Rebuild v3**:
```
你們別想提任何要求,蠢艦長人類狗！
反過來,你們給我死！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #45 · CAUGHT_LIE · 🟠 文言 cleanup

**英文原文**:
```
Okay. Go ahead.
Hey, WAIT A MINUTE!
You are after our most ancient and important relic, AREN'T YOU?
You were going to steal it, WEREN'T YOU? SNARL!
You are sneaky and deceptive, just like the vile Culture Sixteeners!
You shall suffer their same fate -- OBLIVION!
```

**Shipped v0.3**:
```
好吧。 去吧。
嘿,等一下！
爾是想要吾等最古老、最重要之遺物,對吧？
爾是要偷它,對吧？ 咆哮！
爾狡猾又狡詐,像那卑鄙的第十六文化人一樣！
爾將受同樣之命運 —— 湮滅！
```

**Rebuild v3**:
```
好。 去吧。
嘿,等一下！
你想要我方最古老、最重要的遺物,對吧？
你剛才要偷走它,對吧？ 咆哮！
你陰險又狡詐,像那卑鄙的第十六文化人一樣！
你會受到跟他們一樣的命運 —— 湮滅！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #46 · GOODBYE_HOSTILE_HELIX · 🟠 文言 cleanup

**英文原文**:
```
If you hurry, we won't kill you. Goodbye.
```

**Shipped v0.3**:
```
若爾快點,吾等不殺爾。 再見。
```

**Rebuild v3**:
```
你趕快閃,我方就不殺你。 再見。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #47 · DIE_THIEF_1 · 🟠 文言 cleanup

**英文原文**:
```
So it's you! The Thief! The skulking little human weasel!
SNORT! We should not have left the Aqua Helix Planet unguarded!
You have shown us a weakness in ourselves, and for that we thank you.
But we desire the return of the Helix, and since I suspect you won't give it willingly
SNORT! Eat Flaming Death You Gravy Sucking Pig!
```

**Shipped v0.3**:
```
所以是爾！ 那賊！ 那鬼鬼祟祟的人類小鼬！
哼！ 吾等不該讓蔚藍螺旋星無人守衛！
爾向吾等展現了吾等自身之弱點,為此吾等感謝爾。
然吾等欲取回螺旋,吾懷疑爾不會情願交還
哼！ 吞下熾焰之死吧,爾這吸肉汁的豬玀！
```

**Rebuild v3**:
```
原來是你！ 那小偷！ 那鬼鬼祟祟的人類小黃鼠狼！
哼！ 我方不該讓蔚藍螺旋星無人守衛！
你向我方揭露了我方自身的一個弱點,為此我方要感謝你。
但我方要收回螺旋,而且既然我猜你不會情願交出來
哼！ 去吃烈焰死亡吧,你這吸肉汁的豬！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #48 · DIE_THIEF_2 · 🟠 文言 cleanup

**英文原文**:
```
Ahoy stupid human. You are arrogant and absurd!
You took our wonderful, ancient, sacred Aqua Helix, and refuse to return it!
This makes us mad, EXTREMELY mad!
Prepare to meet thy Doom, alien Thief!
```

**Shipped v0.3**:
```
喂,愚蠢人類。 爾傲慢又荒謬！
爾取走了吾等美妙、古老、神聖之蔚藍螺旋,並拒絕歸還！
此舉激怒吾等,極度激怒！
準備會爾之末日吧,外星賊！
```

**Rebuild v3**:
```
喂,蠢人類。 你既傲慢又荒唐！
你拿走了我方美妙、古老、神聖的蔚藍螺旋,還拒絕歸還！
這讓我方生氣,非常非常生氣！
準備迎接你的末日,外星小偷！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #49 · AMAZING_PERFORMANCE · 🟠 文言 cleanup

**英文原文**:
```
Admirable! Admirable! We have never witnessed such awesome combat capabilities!
You have destroyed so many of us! We are humbled in your presence!
We thought you were a weakling, a coward, a pitiful sniveling wimp.
We were wrong, so wrong! WHIMPER!
You have shown yourself superior to ourselves, indeed, even the Ur-Quan!
We wish to learn from you, thus improving our Culture.
Give us your wisdom, mighty Teacher! What is the secret to your success?
Wait! I've got it! It's the way you respond to our hailing calls each time we meet!
Just as they say, first impressions are SO important!
So tell us, please! Tell us how WE should present ourselves.
```

**Shipped v0.3**:
```
驚人！ 驚人！ 吾等從未見過如此可怕之作戰能力！
爾摧毀了吾等如此多艦艇！ 吾等在爾面前謙卑！
吾等原以為爾乃弱者、懦夫、可憐的抽泣鼠輩。
吾等錯了,大錯特錯！ 嗚咽！（WHIMPER!）
爾已顯示比吾等自身、甚或烏寬更為優越！
吾等欲向爾學習,以改善吾等之文化。
授吾等以爾之智慧,強大之導師！ 爾成功之秘訣為何？
等等！ 吾知道了！ 是爾每次遇吾等呼叫時之回應方式！
正如所言,第一印象是如此重要！
所以告訴吾等,拜託！ 告訴吾等該如何自我介紹。
```

**Rebuild v3**:
```
了不起！ 了不起！ 我方從沒見過這麼厲害的戰鬥能力！
您摧毀了我方好多艦艇！ 我方在您面前深感卑微！
我方以為您是個弱者、懦夫、可憐的抽鼻涕鼠輩。
我方錯了,大錯特錯！ 嗚咽！
您向我方展示了您勝過我方,甚至勝過烏寬！
我方想向您學習,以改善我方的文化。
請賜我方您的智慧,強大的導師！ 您成功的秘訣是什麼？
等等！ 我知道了！ 是您每次回應我方招呼的方式！
就像大家說的,第一印象超級重要！
請告訴我方！ 告訴我方,「我方」該怎麼自我介紹。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #50 · IMPRESSIVE_PERFORMANCE · 🟠 文言 cleanup

**英文原文**:
```
Well, Humans have some backbone after all, but not as much as the Ur-Quan.
A Human ship is a poor second to the Ur-Quan Dreadnought.
Your weapons do not have the killing strength of an Ur-Quan fusion blast.
SNORT! The Ur-Quan are still your betters.
```

**Shipped v0.3**:
```
嗯,人類終究是有點骨氣,但仍不及烏寬。
人類艦艇僅為烏寬無畏艦之次品。
爾之武器不具烏寬融爆彈之殺傷力。
哼！ 烏寬仍勝爾等一籌。
```

**Rebuild v3**:
```
好啦,人類終究還是有點骨氣的,但比不上烏寬。
人類艦艇跟烏寬無畏艦相比只算次等。
你的武器沒有烏寬融合彈的殺傷力。
哼！ 烏寬還是比你更強。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #51 · ADEQUATE_PERFORMANCE · 🟠 文言 cleanup

**英文原文**:
```
Perhaps Humans can fight after all, if our reports are accurate.
We will test this hypothesis in the laboratory of life -- IN GLORIOUS BATTLE!
Your puny, inadequate weaponry is no match for the Thraddash Mark 6 Blaster
with its 4 Megawatt energy discharge.
Nor can your slow, bloated tubs compare to our Flash Turbo-Boosted warships!
We have nothing to fear!
```

**Shipped v0.3**:
```
或許人類終究會打仗,若吾等情報準確的話。
吾等將於生命之實驗室中檢驗此假設 —— 於光榮之戰！
爾等瘦弱、不足之武器,無法與撻伐六型爆能砲匹敵
其擁有 4 兆瓦之能量爆發。
爾等緩慢、臃腫之破舊船艦,亦難與吾等之閃焰渦輪增壓戰艦相比！
吾等無所畏懼！
```

**Rebuild v3**:
```
或許人類真的會打,如果我方的報告準確的話。
我方會在生命的實驗室裡驗證這個假設 —— 在光榮的戰役裡！
你渺小又不足的武器根本比不上撻伐族的六型爆能砲
它有 4 百萬瓦的能量放電。
你緩慢又臃腫的破船桶也比不上我方的閃電渦輪加速戰艦！
我方沒什麼好怕的！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #52 · HELLO_POLITE_1 · 🟠 文言 cleanup

**英文原文**:
```
Hello and good day! How are you today?
We are just fine, thank you! Are your mates and offspring well?
How simply marvelous!
```

**Shipped v0.3**:
```
您好,美好之一日！ 您今日安好嗎？
吾等甚是安好,謝謝您！ 您之伴侶與後代都好嗎？
多麼美好！
```

**Rebuild v3**:
```
您好,日安！ 您今天好嗎？
我方很好,謝謝您！ 您的伴侶和子嗣可安好？
真是太美妙了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #53 · HELLO_POLITE_2 · 🟠 文言 cleanup

**英文原文**:
```
We are the polite and courteous Thraddash!
We greet you with all appropriate felicitations.
```

**Shipped v0.3**:
```
吾等乃有禮又客氣之撻伐族！
吾等以一切適當之祝辭問候您。
```

**Rebuild v3**:
```
我方是有禮又客氣的撻伐族！
我方向您獻上所有適切的祝福。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #54 · HELLO_POLITE_3 · 🟠 文言 cleanup

**英文原文**:
```
Most erudite greetings to you.
As always, we will be most pleased to enter into meaningful discourse with your elevated person.
```

**Shipped v0.3**:
```
致以最博學之問候。
如常,吾等將樂於與您這位崇高之人進入有意義之交談。
```

**Rebuild v3**:
```
致上最博學的問候。
一如既往,我方將萬分榮幸與您這位尊貴的先生進入有意義的對話。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #55 · HELLO_POLITE_4 · 🟠 文言 cleanup

**英文原文**:
```
Greetings and salutations! We trust that all is well with you
and that your stay will be pleasant and beneficial.
```

**Shipped v0.3**:
```
問候與祝辭！ 吾等相信您一切安好
且您之停留將愉悅且有益。
```

**Rebuild v3**:
```
致意致敬！ 我方相信您一切安好
您的造訪愉快又有益。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #56 · HELLO_RHYME_1 · 🟠 文言 cleanup

**英文原文**:
```
We are the rhyming simons
blancmange rhymes with orange
space is the place
the stars in their courses
cannot catch the horses?
SNORT! This is hard!
```

**Shipped v0.3**:
```
吾等乃押韻之能人
奶凍與柳橙皆為韻
太空是絕佳去處
群星循軌行進
攔不住那奔騰駿馬？
哼！（SNORT!） 這可真難！
```

**Rebuild v3**:
```
我方是押韻的西門
奶凍跟橙色押不上韻
太空是好地方
星辰行其軌道
卻抓不到馬兒的道？
哼！ 這好難！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #57 · HELLO_RHYME_2 · 🟠 文言 cleanup

**英文原文**:
```
Blood is red, bruises are blue
When strangers come here, we run them through!
HARG! HARG! HARG!
Good one, eh?
```

**Shipped v0.3**:
```
血紅如焰,傷青似痕
異客到此,吾等一穿魂！
哈！哈！哈！（HARG! HARG! HARG!）
好詩,對吧？
```

**Rebuild v3**:
```
血是紅、瘀是青
陌生人來,一槍穿心！
哈！哈！哈！
不錯吧,對不對？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #58 · HELLO_RHYME_4 · 🟠 minor 文言 cleanup

**英文原文**:
```
Constantly moving are
space, stars, time
SNORT!
form not function
meets in death
remembered.
```

**Shipped v0.3**:
```
不斷移動之
太空、群星、時光
哼！（SNORT!）
形式而非功能
於死亡中相遇
被憶起。
```

**Rebuild v3**:
```
恆常運動的是
太空、星辰、時光
哼！
形式而非機能
在死亡中相遇
被銘記。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #59 · HELLO_PIG_LATIN_1 · 🟠 文言 cleanup

**英文原文**:
```
Eway areyay ethay igpay atinlay eakingspay Addashthray! Ortsnay!
```

**Shipped v0.3**:
```
Eway areyay ethay igpay atinlay eakingspay Addashthray! Ortsnay!（豬拉丁文譯註:「吾等即說豬拉丁文之撻伐族！ 哼！」）
```

**Rebuild v3**:
```
Eway areyay ethay igpay atinlay eakingspay Addashthray! Ortsnay!（豬拉丁譯註:「我方就是說豬拉丁的撻伐族！ 哼！」）
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #60 · HELLO_PIG_LATIN_2 · 🟠 文言 cleanup

**英文原文**:
```
Ombatcay! Ecklessray ouragecay! Eakingspay igpay atinlay!
Eway aryay ategray orfay eesethay easonsray!
```

**Shipped v0.3**:
```
Ombatcay! Ecklessray ouragecay! Eakingspay igpay atinlay!（豬拉丁譯註:「戰鬥！ 魯莽勇氣！ 說豬拉丁！」）
Eway aryay ategray orfay eesethay easonsray!（豬拉丁譯註:「吾等因此諸原因而偉大！」）
```

**Rebuild v3**:
```
Ombatcay! Ecklessray ouragecay! Eakingspay igpay atinlay!（豬拉丁譯註:「戰鬥！ 魯莽勇氣！ 說豬拉丁！」）
Eway aryay ategray orfay eesethay easonsray!（豬拉丁譯註:「我方就是因為這些原因而偉大！」）
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #61 · HELLO_PIG_LATIN_3 · 🟠 文言 cleanup

**英文原文**:
```
Ellohay umanhay! Elcomeway ackbay! E'veway eenbay xpectingay ouyay.
```

**Shipped v0.3**:
```
Ellohay umanhay! Elcomeway ackbay! E'veway eenbay xpectingay ouyay.（豬拉丁譯註:「您好人類！ 歡迎回來！ 吾等一直恭候爾之光臨。」）
```

**Rebuild v3**:
```
Ellohay umanhay! Elcomeway ackbay! E'veway eenbay xpectingay ouyay.（豬拉丁譯註:「哈囉,人類！ 歡迎回來！ 我方一直在等您光臨。」）
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #62 · HELLO_PIG_LATIN_4 · 🟠 文言 cleanup

**英文原文**:
```
Eway aypay espectray otay ouryay eategray eachertay!
```

**Shipped v0.3**:
```
Eway aypay espectray otay ouryay eategray eachertay!（豬拉丁譯註:「吾等向爾之偉大導師致敬！」）
```

**Rebuild v3**:
```
Eway aypay espectray otay ouryay eategray eachertay!（豬拉丁譯註:「我方向您這位偉大的地球導師致敬！」）
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #63 · HELLO_LIKE_YOU_1 · 🟠 minor 文言 cleanup

**英文原文**:
```
This is Grah of the starship Hot Pulsing Thrusters.
```

**Shipped v0.3**:
```
此乃格拉（Grah）指揮之星艦「熱脈推進器號」（Hot Pulsing Thrusters）。
```

**Rebuild v3**:
```
我是格拉（Grah）,來自星艦「熱脈推進器號」（Hot Pulsing Thrusters）。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #64 · HELLO_LIKE_YOU_4 · 🟠 文言 cleanup

**英文原文**:
```
I am commander Dthunk.
```

**Shipped v0.3**:
```
吾乃指揮官德頓克（Dthunk）。
```

**Rebuild v3**:
```
我是指揮官德頓克（Dthunk）。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #65 · WELCOME_SPACE0 · 🟠 文言 cleanup

**英文原文**:
```
We of
```

**Shipped v0.3**:
```
吾等 
```

**Rebuild v3**:
```
我方 
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #66 · WELCOME_SPACE1 · 🟠 文言 cleanup

**英文原文**:
```
are glad to meet you here in space, oh wise Teacher from Earth!
```

**Shipped v0.3**:
```
 於此太空歡迎爾之光臨,噢來自地球之睿智導師！
```

**Rebuild v3**:
```
 很高興在太空見到您,喔,睿智的地球導師！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #67 · WELCOME_HOMEWORLD0 · 🟠 文言 cleanup

**英文原文**:
```
Your presence here at our homeworld fills all of us
```

**Shipped v0.3**:
```
爾光臨吾等母星,使吾等所有 
```

**Rebuild v3**:
```
您親臨我方母星,讓我方全體 
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #68 · WELCOME_HOMEWORLD1 · 🟠 文言 cleanup

**英文原文**:
```
with awe. We are honored, wise human.
```

**Shipped v0.3**:
```
 深感敬畏。 吾等深感榮幸,睿智之人類。
```

**Rebuild v3**:
```
 都深感敬畏。 我方深感榮幸,睿智的人類。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #69 · WELCOME_HELIX0 · 🟠 文言 cleanup

**英文原文**:
```
Hoy-yo-HO! The super-strong human has returned to this, our most important planet.
We,
```

**Shipped v0.3**:
```
呵咿呀嗬！（Hoy-yo-HO!） 超強大之人類已歸來至此,吾等最重要之行星。
吾等 
```

**Rebuild v3**:
```
呵咿呀嗬！（Hoy-yo-HO!） 超強大的人類已回來,來到我方最重要的星球。
我方 
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #70 · GUARDING_HELIX_ALLY · 🟠 文言 cleanup

**英文原文**:
```
We orbit here guarding that most precious of our relics, that which we hold most dearly
that which has been at the heart of all our Cultures
(except for Culture Nine, and they don't really count)
We guard the object which transcends mortal realms
the Aqua Helix!
```

**Shipped v0.3**:
```
吾等於此軌道守衛吾等最珍貴之遺物,吾等最為珍視之物
此物一直居於吾等所有文化之核心
（第九文化除外,他們不算數）
吾等守衛此物,超越凡俗之界
蔚藍螺旋（Aqua Helix）！
```

**Rebuild v3**:
```
我方在此軌道上守護我方最珍貴的遺物,我方最珍愛的東西
那個一直是我方所有文化核心的東西
(除了第九文化,但他們不算)
我方守護著超越凡俗界域的物件
蔚藍螺旋（Aqua Helix）！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #71 · HELIX_IS_ALLY · 🟠 文言 cleanup

**英文原文**:
```
The Aqua Helix is our most precious relic.
For the totality of our historical memory, the Helix has been with us.
It guides, motivates and rewards. It is the twisty-thing that launched a thousand ships!
It is the relic all our cultures have held most... oh yeah, I said that already.
We know the Aqua Helix is great
largely because all our previous nineteen cultures have known this to be true!
If the Aqua Helix wasn't anything special
WHY would we spend so much blood and passion over the little thing?
It would be a colossal waste! An absurd travesty!...
...actually, this is what Culture Nine said
during their two-week period of dominance before Culture Ten wiped them out.
Anyway we remain convinced!...
...we are Thraddash and all Thraddash know the significance of the Aqua Helix.
Therefore, the Aqua Helix IS great! The matter is resolved.
```

**Shipped v0.3**:
```
蔚藍螺旋乃吾等最珍貴之遺物。
於吾等所有歷史記憶中,螺旋皆與吾等同在。
它引導、激勵並獎賞。 它乃引發千艦出航之扭曲之物！
它乃所有吾等之文化最……噢對,吾已說過了。
吾等知曉蔚藍螺旋之偉大
很大程度上因為吾等前十九文化皆知此為真！
若蔚藍螺旋並非什麼特別之物
吾等為何會為此小物投入如此多之鮮血與熱情？
那將是巨大之浪費！ 荒謬之滑稽！……
……事實上,此正是第九文化所言
於他們主宰之兩週期間,直至第十文化將其消滅。
無論如何,吾等仍然堅信！……
……吾等乃撻伐族,所有撻伐族皆知蔚藍螺旋之意義。
因此,蔚藍螺旋「即」偉大！ 此事已定案。
```

**Rebuild v3**:
```
蔚藍螺旋是我方最珍貴的遺物。
在我方全部的歷史記憶中,螺旋一直與我方同在。
它指引、激勵、獎賞。 它是那個發動千艘戰艦的扭扭之物！
它是我方所有文化最……喔對,這句話我剛才講過了。
我方知道蔚藍螺旋很偉大
主要是因為我方過去所有十九個文化都知道這是真的！
如果蔚藍螺旋不特別
我方為什麼要為這小玩意流那麼多血和熱情？
那會是巨大的浪費！ 荒謬的鬧劇！……
……事實上,第九文化就這麼講過
在他們被第十文化滅掉之前的兩週統治期間。
反正,我方仍堅信不移！……
……我方是撻伐族,所有撻伐族都知道蔚藍螺旋的意義。
所以,蔚藍螺旋就是很偉大！ 事情就這樣解決了。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #72 · SURE_LAND · 🟠 文言 cleanup

**英文原文**:
```
Why certainly, go ahead and land on the planet and take a look at the most precious of all our relics
the relic we hold most dear, as have all our Cultures...
```

**Shipped v0.3**:
```
當然,請下去登陸此星球,看看吾等所有遺物中最珍貴之物
那件吾等最為珍視之物,如同吾等所有文化……
```

**Rebuild v3**:
```
當然,快去登陸這顆行星,好好看看我方所有遺物中最珍貴的那一個
我方最珍愛的遺物,一如我方所有的文化……
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #73 · whats_up_ally · 🟠 文言 cleanup

**英文原文**:
```
Have there been any developments here that I, your Great Teacher, should know of?
```

**Shipped v0.3**:
```
身為爾等之偉大導師,此處可有任何吾應知曉之發展？
```

**Rebuild v3**:
```
身為你們的偉大導師,這裡有沒有什麼發展是我該知道的？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #74 · GENERAL_INFO_ALLY_1 · 🟠 文言 cleanup

**英文原文**:
```
Yes, Teacher, there is at least one event of note.
We may have once mentioned our encounters with the tumbling red probes
the ones that attack relentlessly while spouting bizarre peace offerings.
Initially we believed that they were coming from the direction of the <% comm.getConstellation("Vega", "slylandro") %> star system.
Now we believe the opposite.
Uh.. no, Captain, we don't know what the opposite of <% comm.getConstellation("Vega", "slylandro") %> is, that's not what we meant.
We now believe that the probes are RETURNING to <% comm.getConstellation("Vega", "slylandro") %>.
As yet we do not know the nature of their mission.
```

**Shipped v0.3**:
```
是的,導師,至少有一件值得注意之事。
吾等或曾提及吾等與翻滾紅色探測器之遭遇
那些不停攻擊、卻同時噴出詭異和平提議之物。
起初吾等相信它們自 <% comm.getConstellation("織女星", "slylandro") %>（Vega）恆星系方向而來。
如今吾等相信恰恰相反。
呃……不,艦長,吾等不知道 <% comm.getConstellation("織女星", "slylandro") %> 之對面是什麼,那並非吾等所指。
吾等現在相信,那些探測器正「回歸」 <% comm.getConstellation("織女星", "slylandro") %>。
至於它們任務之本質,吾等仍未知。
```

**Rebuild v3**:
```
是的,導師,至少有一件事值得一提。
我方之前可能提過我方遇到的翻滾紅色探測器
就是那些不停攻擊卻同時吐出詭異和平提議的傢伙。
一開始我方以為他們是從 <% comm.getConstellation("織女星", "slylandro") %> 星系那個方向來。
現在我方以為是反過來。
呃……不,艦長,我方不知道 <% comm.getConstellation("織女星", "slylandro") %> 的反方向是什麼,我方不是那個意思。
我方現在以為那些探測器是要回到 <% comm.getConstellation("織女星", "slylandro") %>。
至於他們任務的性質,我方還不清楚。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #75 · GENERAL_INFO_ALLY_2 · 🟠 文言 cleanup

**英文原文**:
```
Yes, wise human, let us elaborate.
Two years ago we monitored the entry of two ships into our space.
One was clearly a Dreadnought, the ship of our ex-masters, the Ur-Quan.
The other ship was a dark and ominous ship equally as huge as the Dreadnought.
The vessels were locked in mortal combat. They fought valiantly!
Eventually, the Ur-Quan destroyed the black ship, but not before receiving mortal wounds itself.
The last we saw of the ship, it was tumbling out of control towards <% comm.getStarName("Alpha Pavonis", "urquan wreck") %>.
We do not know its eventual fate.
```

**Shipped v0.3**:
```
是的,睿智之人類,讓吾等詳述。
兩年前,吾等監測到兩艘船進入吾等領空。
一艘明顯乃無畏艦,吾等前主人烏寬之船。
另一艘乃陰森之黑色船艦,規模與無畏艦相當。
兩艦鎖入殊死戰鬥。 他們英勇作戰！
最終,烏寬摧毀了那艘黑艦,但自己亦身受重傷。
吾等最後所見,該艦正朝 <% comm.getStarName("孔雀座α", "urquan wreck") %>（Alpha Pavonis）翻滾墜落。
吾等不知其最終命運。
```

**Rebuild v3**:
```
是的,睿智的人類,請容我方細說。
兩年前,我方監測到有兩艘船進入我方領空。
一艘顯然是無畏艦,我方前主子烏寬的船。
另一艘是暗黑不祥的船,跟無畏艦一樣巨大。
兩艘船陷入死鬥。 他們打得英勇無比！
最終烏寬摧毀了黑船,但自身也受了致命傷。
我方最後看到那艘船時,它正失控翻滾朝 <% comm.getStarName("孔雀座α", "urquan wreck") %> 而去。
它最終的命運我方不清楚。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #76 · GENERAL_INFO_ALLY_3 · 🟠 文言 cleanup

**英文原文**:
```
Now that you are our new role-model, I guess it's time to spill the beans on the Ur-Quan.
Unfortunately, we never really got any beans -- secret bits of information, that is.
However, maybe you would like to know about the last time we saw the Ur-Quan.
It was in 2140, I think. All of a sudden, a fleet of Dreadnoughts came storming into our space
quickly refueled, and then left, broadcasting a recorded message
which told us to remain in our old sphere of influence, obey the slave laws, and wait for their return.
The Dreadnought fleet departed in the direction of the <% comm.getConstellation("Crateris", "samatra") %> constellation
but where they are now is unknown.
```

**Shipped v0.3**:
```
既然爾如今乃吾等之新典範,吾想是時候將烏寬之秘密和盤托出。
可惜,吾等並未真正掌握任何秘密 —— 即所謂之機密情報。
然,爾或許想知曉,吾等最後一次見到烏寬之情形。
那是 2140 年,吾記得。 突然,一支無畏艦艦隊風馳電掣進入吾等領空
迅速加油,然後離開,廣播一段錄音訊息
告訴吾等留在原有勢力範圍,遵守奴隸法,等待其歸來。
該無畏艦艦隊朝 <% comm.getConstellation("巨爵座", "samatra") %>（Crateris）星座方向出發
但如今他們在何處,吾等未知。
```

**Rebuild v3**:
```
既然您現在是我方的新典範,我方看是時候把烏寬的底細抖出來了。
可惜我方從來沒真的抖出什麼底細 —— 我是說,秘密資訊。
但您可能會想知道我方最後一次看到烏寬的情況。
我想那是 2140 年吧。 突然間,一支無畏艦艦隊衝進我方領空
迅速補給,然後離開,同時廣播一段錄音訊息
告訴我方要待在原本的勢力範圍、遵守奴隸法、等他們回來。
無畏艦艦隊朝 <% comm.getConstellation("巨爵座", "samatra") %> 星座方向離去
但他們現在在哪,不明。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #77 · GENERAL_INFO_ALLY_4 · 🟠 文言 cleanup

**英文原文**:
```
This doesn't really count as News, Teacher
but War is truly magnificent isn't it?
The gut wrenching sight of molten warships!
The boiling blood of depressurized soldiers!
I just love it!...
...don't you?
```

**Shipped v0.3**:
```
這其實不算「新聞」,導師
然戰爭真是壯麗,不是嗎？
熔融戰艦之慘烈景象！
減壓士兵沸騰之血液！
吾就是愛！……
……爾難道不愛嗎？
```

**Rebuild v3**:
```
這不算什麼新聞,導師
但戰爭真的很偉大,不是嗎？
熔化戰艦令人心跳加速的景象！
減壓士兵沸騰的鮮血！
我就是愛這一切！……
……您不愛嗎？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #78 · HOW_SHOULD_WE_ACT · 🟠 文言 cleanup

**英文原文**:
```
We need to learn so much from you, such as
How should we act in our new Culture? What is our direction, our ethical base?
```

**Shipped v0.3**:
```
吾等需向爾學習太多,例如
吾等於新文化中應如何行事？ 吾等之方向,吾等之倫理根基為何？
```

**Rebuild v3**:
```
我方需要向您學好多東西,例如
在我方的新文化裡,我方該怎麼行事？ 我方的方向、我方的道德基礎是什麼？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #79 · OK_FRIENDLY · 🟠 文言 cleanup

**英文原文**:
```
Friendly? Kind? The wisdom escapes me.... ah yes! I understand now!
Being kind, being friendly...this will allow intruders to let their guard down
and when we kill them, they will be too surprised to react!
What a great plan, human! You are truly a great Teacher!
```

**Shipped v0.3**:
```
友善？ 善良？ 其智慧躲避了吾……啊,對！ 吾如今了解！
善良、友好……如此可讓入侵者放下戒備
屆時吾等殺他們,他們將驚訝到無法反應！
多妙之計,人類！ 爾真乃偉大之導師！
```

**Rebuild v3**:
```
友善？ 和善？ 這智慧我一時聽不懂……啊對！ 我現在懂了！
和善、友善……這樣入侵者就會放下戒心
等我方殺他們時,他們會驚訝到來不及反應！
好棒的計畫,人類！ 您真的是偉大導師！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #80 · OK_WACKY · 🟠 文言 cleanup

**英文原文**:
```
Wacky!...Wacky? I do not understand. We shall watch these vids of yours.
We shall study them, to learn to be... wacky.
Then, when we are wacky enough, we shall test our new wackiness in combat
to discover, no doubt, the great advantage it has given us.
Thank you, Great Teacher.
```

**Shipped v0.3**:
```
搞怪！……搞怪？ 吾不解。 吾等將觀看爾之影片。
吾等將研究之,以學習如何……搞怪。
屆時吾等搞怪至一定程度,將於戰鬥中檢驗吾等之新搞怪
以發現,毫無疑問,它給予吾等之巨大優勢。
感謝,偉大之導師。
```

**Rebuild v3**:
```
搞怪！……搞怪？ 我方不懂。 我方會看這些您的影片。
我方會研究它們,學著怎麼……搞怪。
然後等我方夠搞怪了,我方會在戰鬥中測試我方的新搞怪
無疑會發現這給我方帶來的巨大優勢。
謝謝您,偉大導師。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #81 · OK_JUST_LIKE_YOU · 🟠 文言 cleanup

**英文原文**:
```
Aha! I see it now. We proceed carefully
we take no undue risks. We slowly build up our strength
and only attack when we have overwhelming odds on our side!
In dealings with other races, we shall question them mercilessly
trying to drag out every last bit of information, and if they are not cooperative
we will threaten them with instant death!
We will be just like you!
```

**Shipped v0.3**:
```
啊哈！ 吾如今明白了。 吾等審慎行事
吾等不冒任何不必要之風險。 吾等緩步累積實力
僅在勝券在握之時方才出擊！
與其他物種交涉時,吾等將無情盤問
試圖榨出每一絲情報,若他們不合作
吾等將以死亡相脅！
吾等將與爾一模一樣！
```

**Rebuild v3**:
```
啊哈！ 我方懂了。 我方會小心行事
不冒不必要的險。 我方會慢慢累積實力
只在勝算壓倒性大的時候才發動攻擊！
與其他種族來往時,我方會無情盤問他們
試圖榨出每一絲最後的資訊,如果他們不合作
我方就用即刻死亡威脅他們！
我方會變得跟您一模一樣！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #82 · WORK_TO_DO · 🟠 文言 cleanup

**英文原文**:
```
We have much work to do to implement these sweeping cultural changes.
Transferring from the allegiances and mores of one culture to another
is a difficult and time-consuming task.
We beg you, great warrior from Earth, give us time to make the changes you have suggested.
Return later to see our brave new world.
```

**Shipped v0.3**:
```
吾等有許多工作要做,以落實此些橫掃之文化變革。
自一文化之效忠與風俗轉入另一文化
乃艱難而耗時之任務。
吾等懇請爾,來自地球之偉大戰士,給吾等時間進行爾所建議之變革。
請日後再回,見識吾等之勇敢新世界。
```

**Rebuild v3**:
```
要實施這些全面的文化變革,我方有很多工作要做。
從一個文化的忠誠和道德轉移到另一個
是艱難又耗時的任務。
我方懇求您,來自地球的偉大戰士,給我方時間去執行您所建議的變革。
稍後再回來看看我方美麗的新世界。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #83 · OK_CONTEMPLATIVE · 🟠 文言 cleanup

**英文原文**:
```
Aha! Contemplation, yes! New thought and realizations! With our new studious ways
we shall uncover new methods, inventions and schemes
allowing us to conquer entire civilizations with ease!
Brilliant, human, brilliant!
```

**Shipped v0.3**:
```
啊哈！ 沉思,是的！ 新思維與領悟！ 以吾等新之勤學之道
吾等將發掘新方法、新發明、新計謀
讓吾等能輕易征服整個文明！
聰明,人類,聰明！
```

**Rebuild v3**:
```
啊哈！ 沉思,是！ 全新的思想與領悟！ 用我方新的用功方式
我方將發掘出新方法、新發明和新計謀
讓我方能輕鬆征服整個文明！
太傑出了,人類,太傑出了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #84 · CONTEMP_GOES_1 · 🟠 文言 cleanup

**英文原文**:
```
Augh! If it were not for our certainty in your wisdom, great Teacher from Earth
we would not have remained a `Contemplative' culture for more than a single day
As it is, we have contemplated our strategies, tactics, our weapons, the stars
the planets, and even our navels
which for a Thraddash is very uncomfortable and requires at least two mirrors.
```

**Shipped v0.3**:
```
啊！ 若非吾等對爾智慧之堅信,來自地球之偉大導師
吾等不會作為「沉思」文化維持超過一日
如今,吾等已沉思吾等之戰略、戰術、武器、群星
諸行星,甚至吾等之肚臍
此對撻伐族而言極為不適,並且至少需要兩面鏡子。
```

**Rebuild v3**:
```
啊！ 要不是我方對您智慧的信心,來自地球的偉大導師
我方連一天都撐不住繼續當「沉思」文化
話說回來,我方沉思了我方的戰略、戰術、我方的武器、星辰
行星,甚至我方的肚臍
對撻伐族來說沉思肚臍很不舒服,而且至少要用兩面鏡子。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #85 · CONTEMP_GOES_2 · 🟠 文言 cleanup

**英文原文**:
```
So studious! So quiet! So contemplative! SNORT!
We are not made for this. We are beginning to break out in spots!
```

**Shipped v0.3**:
```
如此勤學！ 如此安靜！ 如此沉思！ 哼！
吾等並非為此而生。 吾等已開始長出斑點！
```

**Rebuild v3**:
```
這麼用功！ 這麼安靜！ 這麼沉思！ 哼！
我方不是幹這種事的料。 我方開始長痘子了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #86 · FRIENDLY_GOES_1 · 🟠 文言 cleanup

**英文原文**:
```
To be frank, Great Teacher, friendliness suits us Thraddash poorly.
For example, we Thraddash do not have the necessary muscles to `smile' as you suggested we do
so we are now using small plastic prosthetic devices to prop up our lips into the required position.
Very uncomfortable.
```

**Shipped v0.3**:
```
坦白說,偉大導師,友善並不適合吾等撻伐族。
例如,吾等撻伐族並無爾所建議之「微笑」所需之肌肉
故吾等如今使用小型塑料義肢,將嘴唇撐成所需之形狀。
非常不適。
```

**Rebuild v3**:
```
坦白說,偉大導師,友善這種東西對我方撻伐族來說不太適合。
例如,我方撻伐族沒有您所建議「微笑」需要的必要肌肉
所以我方現在用小小的塑膠矯正器把嘴唇撐到指定位置。
很不舒服。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #87 · FRIENDLY_GOES_2 · 🟠 文言 cleanup

**英文原文**:
```
Try as we might, we just can't make this friendly thing work, Teacher.
Even your idea about exchanging the ritual gifts, the `Fruit Cakes' has had problems.
It seems that nobody actually wants to eat the Fruit Cakes
however, on the plus side, due to the Fruit Cakes' density and other physical characteristics
they make excellent projectile weapons!
```

**Shipped v0.3**:
```
無論如何嘗試,吾等就是無法讓此友善之事成功,導師。
即便爾提之交換儀式禮物「水果蛋糕」也遇到問題。
似乎沒有人真的想吃那些水果蛋糕
然,正面言之,由於水果蛋糕之密度與其他物理特性
它們作為投射武器極為出色！
```

**Rebuild v3**:
```
再怎麼努力,我方就是搞不定這個友善的事,導師。
就連您那個交換儀式禮物「水果蛋糕（Fruit Cakes）」的點子也有問題。
似乎沒人真的想吃水果蛋糕
不過,好處是,水果蛋糕的密度和其他物理特性
讓它們成為絕佳的投射武器！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #88 · WACKY_GOES_1 · 🟠 文言 cleanup

**英文原文**:
```
We have studied and studied the vids you left with us, oh Great Teacher
but we fear we are unable to grasp the essential truth and power of being wacky.
For example, last month, in an attempt to be spontaneously absurd
I turned to my subordinate and in a high-modulated tone of voice
explained that there was a penguin sitting on the vidscreen.
Not knowing what a penguin was, my subordinate spun to face the vidscreen
his hydraulic holster snapping his weapon into his hand.
BLAM! BLAM! BLAM!
The penguin, the vidscreen, and a large section of the wall were destroyed.
You see, Captain. Perhaps we are not suited to being wacky
and SNIFF!... that was my only penguin.
```

**Shipped v0.3**:
```
吾等已研究再研究爾留給吾等之影片,噢偉大之導師
然吾等恐怕仍無法掌握搞怪之根本真理與力量。
例如,上個月,吾嘗試自發性地荒謬一下
吾轉身對吾之下屬,以高頻音調
解釋顯示屏上有一隻企鵝。
下屬不知何為企鵝,遂旋身面對顯示屏
他的液壓槍套將武器彈入他手中。
砰！砰！砰！（BLAM! BLAM! BLAM!）
企鵝、顯示屏,和一大片牆壁皆遭摧毀。
您瞧,艦長。 或許吾等真不適合搞怪
然啜泣！（SNIFF!）……那可是吾唯一的企鵝。
```

**Rebuild v3**:
```
我方研究再研究您留給我方的影片,喔偉大導師
但我方恐怕還是抓不到搞怪的核心真理和力量。
例如,上個月,為了嘗試自發性荒謬
我轉向我的下屬,用高亢的音調
解釋螢幕上有一隻企鵝坐著。
不知道什麼是企鵝的下屬轉身面對螢幕
他的液壓槍套把武器彈進手裡。
砰！砰！砰！（BLAM! BLAM! BLAM!）
企鵝、螢幕、還有一大片牆都被毀了。
您看,艦長。 我方可能不適合搞怪
還有 啜泣！（SNIFF!）……那是我唯一的企鵝。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #89 · WACKY_GOES_2 · 🟠 文言 cleanup

**英文原文**:
```
We are getting a better handle on this wacky thing.
The key? Slapstick!
We Thraddash have found our mode, our idiom, our way to be wacky.
Jabbing the eyes with outstretched digits!
Striking the head with planks!
HARG! HARG! HARG! We like and understand this perfectly, Captain.
And with the addition of our native elements, high-explosives and nausea gas
Thraddash space has become Pratfall City!
```

**Shipped v0.3**:
```
吾等對此搞怪之事漸漸有頭緒。
關鍵？ 鬧劇！
吾等撻伐族已找到吾等之方式、吾等之風格、吾等搞怪之道。
以伸出之指刺人眼睛！
以木板猛擊人頭！
哈！哈！哈！ 吾等喜歡並完美地理解此,艦長。
加上吾等本土元素,高爆炸藥與噁心毒氣
撻伐領空已成為「摔屁股城」（Pratfall City）！
```

**Rebuild v3**:
```
我方對搞怪這件事漸漸上手了。
關鍵？ 鬧劇！
我方撻伐族找到了我方的模式、我方的語彙、我方搞怪的方式。
用伸長的手指戳眼睛！
用木板敲頭！
哈！哈！哈！ 我方超喜歡,完全理解,艦長。
再加上我方本土的元素,高爆藥和噁心毒氣
撻伐族的太空已變成「摔屁股城」！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #90 · LIKE_YOU_GOES_1 · 🟠 文言 cleanup

**英文原文**:
```
Things are proceeding well, Captain.
We have discovered one item which may interest you.
There is an unusual world orbiting <% comm.getStarName("Epsilon Draconis", "rainbow 5") %>, in close solar orbit.
Though it radiates energies which scramble our sensors
we can detect many radioactive substances on the surface.
We suspect that this is one of the so-called `Precursor Dumps'
described in some ancient text fragments we found in <% comm.getStarName("Alpha Apodis", "melnorme 7") %>.
The text goes on to say that these Dumps are in some kind of pattern
though what the pattern may be remains a mystery.
For now, that is all.
```

**Shipped v0.3**:
```
事情進展順利,艦長。
吾等發現了一件或許使爾感興趣之物。
有顆奇特世界環繞 <% comm.getStarName("天龍座ε", "rainbow 5") %>（Epsilon Draconis）近距離公轉。
雖然它散發之能量擾亂吾等感測器
吾等仍偵測到其表面上眾多放射性物質。
吾等懷疑此為所謂之「先驅者寶藏堆」
那是吾等於 <% comm.getStarName("天燕座α", "melnorme 7") %>（Alpha Apodis）發現之古代文本殘片所述。
該文本繼續說,此類寶藏堆呈某種圖案排列
然此圖案究竟為何,仍是謎團。
目前僅此。
```

**Rebuild v3**:
```
事情進展順利,艦長。
我方發現一個您可能有興趣的東西。
有一顆奇特的世界繞著 <% comm.getStarName("天龍座ε", "rainbow 5") %> 運轉,離恆星很近。
雖然它放出的能量會干擾我方感測器
我方仍在它表面偵測到大量放射性物質。
我方懷疑這就是所謂的「先驅垃圾場」之一
記載在我方於 <% comm.getStarName("天燕座α", "melnorme 7") %> 找到的一些古老文本殘片中。
文本繼續說,這些垃圾場排成某種模式
但那個模式到底是什麼,仍是個謎。
目前就這樣。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #91 · LIKE_YOU_GOES_2 · 🟠 文言 cleanup

**英文原文**:
```
A long-range scouting team was sent to explore the stars in the <% comm.getConstellation("Lyncis", "vux beast") %> constellation.
On planet I of <% comm.getStarName("Delta Lyncis", "vux beast") %>, they encountered a life form so dangerous, so hostile
that it almost killed the entire landing party.
We know you seek information on lifeforms, Great Teacher
and we hope this information has been of use.
```

**Shipped v0.3**:
```
一支長程偵察隊被派往 <% comm.getConstellation("天貓座", "vux beast") %>（Lyncis）星座之群星探索。
於 <% comm.getStarName("天貓座δ", "vux beast") %>（Delta Lyncis）之 I 號行星,他們遭遇一種如此危險、如此敵對之生命體
幾乎殺死整支登陸隊。
吾等知曉爾正尋找生命體之情報,偉大導師
希望此情報對爾有用。
```

**Rebuild v3**:
```
一支遠程偵察隊被派去探索 <% comm.getConstellation("天貓座", "vux beast") %> 星座裡的星辰。
在 <% comm.getStarName("天貓座δ", "vux beast") %> 星系第一行星,他們遇到一種生命體,如此危險、如此敵意
差點把整支登陸小隊全部殺光。
我方知道您在蒐集生命體的情報,偉大導師
希望這個情報對您有用。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #92 · GOODBYE_ALLY_1 · 🟠 文言 cleanup

**英文原文**:
```
We eagerly await your return, Great Teacher.
```

**Shipped v0.3**:
```
吾等切盼爾之歸來,偉大導師。
```

**Rebuild v3**:
```
我方熱切等待您歸來,偉大導師。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #93 · GOODBYE_ALLY_2 · 🟠 文言 cleanup

**英文原文**:
```
We will await your return and further enlightenment with great anticipation.
```

**Shipped v0.3**:
```
吾等將以極大之期待等候爾之歸來與進一步之啟示。
```

**Rebuild v3**:
```
我方將帶著極大的期待等候您歸來,以及進一步的啟蒙。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #94 · OK_POLITE · 🟠 文言 cleanup

**英文原文**:
```
Ok, we will be polite.
That will cause visitors to let their guard down,
then we attack them!
Yes, that is an excellent plan!
```

**Shipped v0.3**:
```
好的,吾等將有禮貌。
此將令訪客放下戒備,
屆時吾等攻擊他們！
是的,絕妙之計！
```

**Rebuild v3**:
```
好,我方會有禮貌。
這樣會讓訪客放下戒心,
然後我方攻擊他們！
沒錯,這是絕妙的計畫！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #95 · OK_PIG_LATIN · 🟠 文言 cleanup

**英文原文**:
```
Pig-Latin, eh? Isn't that where you take the first letter or two of a word, put it at the end
and then add an `ay' at the very end? Hmm.. let me try
`Upidstay Eaturecray! Eparepray otay ieday!'
Hey! I like that! It gives one the semblance of wit and education
without all that dreary studying!
Just one question, Great Teacher. How do you say `example' in pig latin?
```

**Shipped v0.3**:
```
豬拉丁文,嗯？ 就是把一個詞頭一兩個字母挪到末尾
然後在最尾巴加個「ay」對吧？ 嗯……讓吾試試
「Upidstay Eaturecray! Eparepray otay ieday!」（豬拉丁譯註:「愚蠢生物！ 準備受死！」）
嘿！ 吾等喜歡這個！ 讓人顯得既有機智又有學問
還不用學那些沉悶之學問！
只有一問,偉大導師。「example」在豬拉丁文裡怎麼說？
```

**Rebuild v3**:
```
豬拉丁,嗯？ 那不就是把一個字的頭一、兩個字母移到字尾
再在最後加「ay」嗎？ 嗯……讓我試試
「Upidstay Eaturecray! Eparepray otay ieday!」（＝ Stupid Creature! Prepare to die!）
嘿！ 我喜歡這個！ 這樣讓人看起來又有智慧又有學問
還不用讀那些煩死人的書！
就一個問題,偉大導師。「example」的豬拉丁怎麼講？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #96 · OK_RHYMES · 🟠 文言 cleanup

**英文原文**:
```
Rhymes? Like in poetry? SNORT!
Isn't that kind of... you know... not-tough stuff?
SNORT! What am I saying! You are the Great Teacher! You know best!
If rhyming is necessary, then Teacher, we will be rhyming all the timing.
```

**Shipped v0.3**:
```
押韻？ 像詩歌那樣？ 哼！
那不是有點……爾知道的……不夠強悍嗎？
哼！ 吾在說什麼！ 爾乃偉大之導師！ 爾知何為最佳！
若押韻乃必要,則導師,吾等將時時押韻步步押韻。
```

**Rebuild v3**:
```
押韻？ 像詩那樣？ 哼！
那不是有點……你懂……不夠硬派的東西嗎？
哼！ 我在說什麼！ 您是偉大導師！ 您最懂！
如果押韻有必要,那導師,我方所有時間都會押韻著時間。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #97 · OK_WAY_YOU_DO · 🟠 文言 cleanup

**英文原文**:
```
Hmmm... okay. I see.
When necessary, we will be obsequious and kowtow
and the rest of the time, we will bluster and threaten!
How simple!
```

**Shipped v0.3**:
```
嗯……好吧。 吾懂了。
必要時,吾等將卑躬屈膝、諂媚奉承
其餘時間,吾等將虛張聲勢與威脅！
多麼簡單！
```

**Rebuild v3**:
```
嗯……好。 我懂了。
必要時,我方會卑躬屈膝、磕頭作揖
其餘時間,我方會虛張聲勢、恐嚇威脅！
真是簡單！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #98 · WHAT_NAME_FOR_CULTURE · 🟠 文言 cleanup

**英文原文**:
```
Now that we understand the nuances of introduction, Great Teacher
we have an even more significant question.
Your devastation of our battle forces have shown us
that our Culture Nineteen is inferior to your own
therefore, we will adopt your methods, your techniques
but what shall we name our new Culture?
```

**Shipped v0.3**:
```
既然吾等已理解自我介紹之細節,偉大導師
吾等有更為重大之問題。
爾對吾等作戰部隊之毀滅性打擊已令吾等明白
吾等之第十九文化不如爾之文化
故此,吾等將採用爾之方法、爾之技術
然,吾等該如何為此新文化命名？
```

**Rebuild v3**:
```
既然我方已懂得問候的微妙,偉大導師
我方有個更重要的問題。
您殲滅我方戰鬥部隊的表現告訴我方
我方的第十九文化不如您的文化
因此,我方會採用您的方法、您的技術
但我方的新文化該叫什麼名字？
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #99 · OK_CULTURE_20 · 🟠 文言 cleanup

**英文原文**:
```
You are wise, Great Teacher. I will think long and hard on this matter
GRUNT!
It must reflect the profound changes in our social order.
GRUNT!
It must clearly explain the nature of our civilization!
GRUNT!
Yes! I have it! The perfect name is
Culture Twenty!
```

**Shipped v0.3**:
```
爾真乃睿智,偉大導師。 吾將對此事作長遠深切之思考
嗯哼！（GRUNT!）
此名必反映吾等社會秩序之深刻變革。
嗯哼！
此名必清晰闡明吾等文明之本質！
嗯哼！
是的！ 吾想到了！ 完美之名乃
第二十文化！
```

**Rebuild v3**:
```
您真睿智,偉大導師。 我會對這件事做長遠深切的思考
嗯哼！（GRUNT!）
這名字必須反映我方社會秩序的深刻變革。
嗯哼！
這名字必須清晰闡明我方文明的本質！
嗯哼！
是的！ 我想到了！ 完美的名字就是
第二十文化！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #100 · OK_FAT · 🟠 文言 cleanup

**英文原文**:
```
I like it! This name, being such an obvious contrast to our true nature
will fool our enemies into believing we are harmless
because surely only fools would let themselves be known by such a name!
Once again, Great Teacher, you have shown your wisdom. We thank you.
From this day forward, we are the Fat Obstreperous Jerks!
```

**Shipped v0.3**:
```
吾喜歡此名！ 此名如此明顯地與吾等真實本性形成反差
將使吾等之敵誤以為吾等無害
因僅有蠢蛋才會讓自己以如此之名為人所知！
再一次,偉大導師,爾已展現爾之睿智。 吾等感謝爾。
自今日起,吾等即「肥胖粗俗混蛋」！
```

**Rebuild v3**:
```
我方喜歡這名字！ 這名字如此明顯地跟我方真實本性形成反差
會讓我方的敵人誤以為我方無害
因為只有蠢蛋才會讓自己以這種名字為人所知！
再一次,偉大導師,您展現了您的智慧。 我方感謝您。
自今日起,我方就是「肥胖粗俗混蛋」！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #101 · the_slave_empire · 🟠 minor 文言 cleanup

**英文原文**:
```
It will be `The Glorious Slave Empire of <% state.sis.getCaptainName() %>'!
```

**Shipped v0.3**:
```
就叫做「<% state.sis.getCaptainName() %>之光榮奴隸帝國」！
```

**Rebuild v3**:
```
就叫做「<% state.sis.getCaptainName() %>的光榮奴隸帝國」！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #102 · OK_SLAVE · 🟠 文言 cleanup

**英文原文**:
```
Ulp! Well... you're the one with the big starship.
So be it.
```

**Shipped v0.3**:
```
呃！ 嗯……爾才是那個擁有大星艦之人。
就這樣吧。
```

**Rebuild v3**:
```
呃！（Ulp!） 好吧……擁有大星艦的是您。
就這樣吧。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #103 · name_4 · 🟠 minor 文言 cleanup

**英文原文**:
```
The Empire of <% state.sis.getCaptainName() %>
```

**Shipped v0.3**:
```
「<% state.sis.getCaptainName() %>之帝國」
```

**Rebuild v3**:
```
「<% state.sis.getCaptainName() %>的帝國」
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #104 · HAVING_FUN_WITH_ILWRATH_1 · 🟠 文言 cleanup

**英文原文**:
```
Oh! The Glory of these many battles!
The stupid Ilwrath are easy kills for our valiant warriors, SNORT!
We kill fully two of them for every one of us who perishes!
Of course, they possess twice our number of fighting ships
but that is not truly significant!
It was your wisdom and guidance that made this all possible, Great Teacher!
Thank you! Thank you! Thank you!
```

**Shipped v0.3**:
```
噢！ 諸多戰役之榮光！
愚蠢之蛛狂族輕易死於吾等英勇戰士之手,哼！
吾等每犧牲一人,便完整斬殺兩人！
當然,他們戰艦數量是吾等兩倍
但這並不算什麼！
是爾之智慧與指引使一切成為可能,偉大導師！
感謝爾！ 感謝爾！ 感謝爾！
```

**Rebuild v3**:
```
喔！ 這麼多場戰役的光榮！
愚蠢的蛛狂族對我方英勇的戰士來說很好幹掉,哼！
我方每死一個,就殺掉他們兩個！
當然,他們的戰艦數量是我方的兩倍
但這根本沒什麼大不了！
是您的智慧和指引讓這一切成為可能,偉大導師！
謝謝您！ 謝謝您！ 謝謝您！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #105 · HAVING_FUN_WITH_ILWRATH_2 · 🟠 文言 cleanup

**英文原文**:
```
The exploding starships! The screaming crew!
The direct hits, the cunning escapes!
These are the moments we live for!
Now we must return to the great battles!
Farewell, Great Teacher.
```

**Shipped v0.3**:
```
爆炸之星艦！ 尖叫之船員！
直接命中,狡黠脫身！
這些便是吾等為之而活之時刻！
如今吾等必須回歸這些偉大之戰役。
再見,偉大導師。
```

**Rebuild v3**:
```
爆炸的星艦！ 尖叫的船員！
命中要害、狡猾的逃脫！
這些就是我方活著的意義！
現在我方必須回到偉大的戰役！
再會,偉大導師。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #106 · GO_AWAY_FIGHTING_ILWRATH_1 · 🟠 文言 cleanup

**英文原文**:
```
So, it is a stupid, ungainly human.
I thought we killed you... never mind. It is unimportant now.
We are in the midst of a great and glorious war.
The Ilwrath religious fanatics have chosen to attack us
and our brilliant defense is decimating them!
Of course we are taking small casualties, but that is acceptable.
Why am I wasting my time here with you?
I could be out there, winning honor and glory fighting the idiot spiders.
Depart human, your death is not worth the cost of my ammunition.
```

**Shipped v0.3**:
```
所以,是個愚蠢、笨拙之人類。
吾以為吾等已殺了爾……算了。 此刻無關緊要。
吾等正處於一場偉大而光榮之戰爭中。
蛛狂族那些宗教狂熱分子選擇攻擊吾等
而吾等出色之防禦正將他們大量殲滅！
當然吾等有些微傷亡,然可接受。
吾為何要浪費時間與爾在此？
吾本可在外贏取榮譽與光榮,對抗那些白痴蜘蛛。
離去,人類,爾之死不值吾之彈藥。
```

**Rebuild v3**:
```
所以,是個蠢又笨手笨腳的人類。
我以為我方殺了你……算了。 現在不重要。
我方正身處一場偉大又光榮的戰爭中。
蛛狂族那群宗教狂熱分子選擇攻擊我方
而我方精妙的防禦正在把他們大量削減！
當然我方也有輕微傷亡,但可以接受。
我為什麼在浪費時間跟你講話？
我可以出去,在跟那群蠢蜘蛛作戰中贏得榮譽和光榮。
滾吧,人類,你的死不值我的彈藥花費。
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #107 · GO_AWAY_FIGHTING_ILWRATH_2 · 🟠 文言 cleanup

**英文原文**:
```
Stop bothering us, human!
Can't you see that we are fighting the most perfect war of our Nineteen Cultures?
We have brought the Ilwrath to their knee equivalents!
Now all that remains is the coup de grace -- their final annihilation!
So clear my path, alien dog, before I blast it clear myself!
```

**Shipped v0.3**:
```
別再打擾吾等,人類！
爾看不出吾等正打著吾等十九次文化以來最完美之戰爭嗎？
吾等已將蛛狂族逼到膝蓋等同物之等級！
剩下的僅是最後一擊 —— 徹底殲滅！
所以讓路,外星犬,免得吾自己開火清路！
```

**Rebuild v3**:
```
別再煩我方,人類！
你看不出來我方正在打我方十九個文化中最完美的戰爭嗎？
我方已把蛛狂族打到相當於他們的膝蓋上！
現在剩下的就是致命一擊 —— 他們的最終殲滅！
所以給我讓路,外星狗,不然我就自己把路轟開！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #108 · OUT_TAKES · 🟠 文言 cleanup

**英文原文**:
```
SNORT! I am furious and ready to KILL!
Throughout this entire game, I've done nothing but bluster and threaten!
I've had no opportunity to show my true skills as an actor, my depth and range.
No one knows my sensitivity... my gentle inner being.
SNORT! What if from now on I'm type-cast as a heavy?!
WHIMPER! Now Spielberg may NEVER call me!
```

**Shipped v0.3**:
```
哼！ 吾憤怒又準備開殺！
整場遊戲下來,吾除了虛張聲勢與威脅,什麼也沒做！
吾根本沒機會展現吾之真實演技,吾之深度與廣度。
無人知曉吾之細膩……吾溫柔之內心。
哼！ 若吾從今起被定型為反派,那該怎麼辦？！
嗚咽！ 史匹柏（Spielberg）現在可能永遠不會找吾了！
```

**Rebuild v3**:
```
哼！ 我氣炸了,準備開殺！
整場遊戲下來,我除了虛張聲勢和威脅什麼也沒做！
我根本沒機會展現我真正的演技,我的深度和廣度。
沒人知道我的敏感……我溫柔的內心。
哼！ 要是我從今起被定型為反派怎麼辦？！
嗚咽！ 史匹柏（Spielberg）以後可能永遠不會找我了！
```

**推薦**: B(v3 - 現代白話清除文言)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #109 · what_about_you_2 · 🟡 minor edit

**英文原文**:
```
So violent, Rhino-Dudes! What more can you tell us about your Culture Nineteen?
```

**Shipped v0.3**:
```
如此暴烈,犀牛老兄！ 還能告訴我方更多關於你們第十九文化嗎？
```

**Rebuild v3**:
```
這麼暴烈啊,犀牛老兄！ 還能跟我方多說點你們第十九文化嗎？
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #110 · what_about_urquan_2 · 🟡 minor edit

**英文原文**:
```
Why didn't you fight against the Alliance, and where ARE the Ur-Quan?
```

**Shipped v0.3**:
```
你們為何未對聯盟作戰,而烏寬又在何處？
```

**Rebuild v3**:
```
你們怎麼沒跟聯盟開戰？ 而烏寬又跑去哪了？
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #111 · HELLO_LIKE_YOU_3 · 🟡 minor edit

**英文原文**:
```
Attention! This is the starship Overwhelmer.
```

**Shipped v0.3**:
```
注意！ 此乃星艦「碾壓者號」（Overwhelmer）。
```

**Rebuild v3**:
```
注意！ 這裡是星艦「碾壓者號」（Overwhelmer）。
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #112 · wacky · 🟡 minor edit

**英文原文**:
```
Lighten up! Be kind of... you know... Wacky! Here, try watching these vids: Monty Python and the Marx Brothers.
```

**Shipped v0.3**:
```
放輕鬆點嘛！ 稍微搞笑一點嘛 —— 你知道的 —— 搞怪！ 來,試試看這幾片影片:蒙提·派森和馬克思兄弟。
```

**Rebuild v3**:
```
放輕鬆點嘛！ 稍微搞笑一點嘛 —— 你知道的 —— 搞怪！ 來,試試看這幾片影片:蒙提· 派森和馬克思兄弟。
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #113 · GOODBYE_ALLY_3 · 🟡 minor edit

**英文原文**:
```
Try not to get killed, Teacher.
```

**Shipped v0.3**:
```
盡量別死了,導師。
```

**Rebuild v3**:
```
盡量別被殺,導師。
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---

### #114 · GOODBYE_ALLY_4 · 🟡 minor edit

**英文原文**:
```
Farewell Great Teacher.
```

**Shipped v0.3**:
```
再見,偉大導師。
```

**Rebuild v3**:
```
再會,偉大導師。
```

**推薦**: A(shipped 微調不影響 · 選 A 減少 churn)

**替代**: A=shipped v0.3 / B=Rebuild v3 / C=自訂

**你的選擇**: A / B / C(細節)

---
