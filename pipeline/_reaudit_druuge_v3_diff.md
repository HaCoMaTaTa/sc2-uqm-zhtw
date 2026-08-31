# Druuge Rebuild-Compare Diff Report (2026-08-17)

## 統計

- Total tokens: 105
- 🟢 完全相同: 5 (4.8%)
- 🟡 微調 (等價): 71 (67.6%)
- 🟠 措辭改變: 6 (5.7%)
- 🔴 語意/voice 差異大: 2 (1.9%)
- ✨ v0.7 canonical 升級: 21 (20.0%)
- ⚙ 階段 2.5 Read-Aloud self-fix: 5 (4.8%) · **已直接應用於 v3** · 詳見 `_selfaudit_druuge_v3_readaloud.md`

## Q&A 決策摘要

- **Q1=B** 血紅集團（保留 shipped v0.3 · Master_Glossary L316 已同步）
- **Q2=A** 毒賈條例 3429 號－A86 分項〈星艦廢船之定義〉
- **Q3=A** 仇怨名冊
- **Q4=C** 送去餵熔爐（保留 shipped「熔爐」+ dossier「送去餵」合成 · 客製）
- **Q5=A** 超波播送器（Master_Glossary L371）
- **Q6=A** 玫瑰球體（Master_Glossary L223）
- **Q7=A** 發光魔杖
- **Q8 客製** 漩渦生成器 / 傳送門生成器（保留 shipped 漩渦 · Portal Spawner 補全生成器）
- **Q9=A** 深層幼體（Master_Glossary L119 v0.7 · 跨族 Mycon+Syreen+Arilou 統一）
- **Q10=A** 二度靈視（保留 shipped）
- **Q11=B** Depart 情境化（拒絕/hostile 用「離開。」冷酷 · 一般場合可 shipped「離去/走吧」）
- **Q12=A** （嘿嘿嘿）
- **Q13=A** 感嘆詞：Aieee!/Ho-ho-ho!/Ha-ha!/(hee-hee-hee) 全中譯 · 僅 Kyeee! Lykeee-lieee! 保留原文
- **Q14=B** 血紅集團之高級專員（保留 shipped 職稱）
- **Q15=A** 契約套語採 dossier §六 例 4（崇拜方/鑑於/以下簡稱/茲此/包括但不限於）
- **Q16=A** 保留 shipped voice palette（在下/敝方/我方/本商號）
- **Q17=A** OUT_TAKES 用「我」（打破第四牆）
- **Q18=B** 玩家對 Druuge 稱謂：熱情話術/交易用「您」· 拒絕/敵對用「你」
- **Q19=A** 保留大多「之」（現代連詞 + 契約法律語域）
- **Q20=A** 3 partials × ~35 tokens

---

## 差異項（依類別分組 · 只列 🟡🟠🔴✨）

## ✨ v0.7 canonical 升級（21 項）

### #1 · `NOT_GET_BOMB` · ✨ v0.7 canonical 升級

**英文原文**:
```
LIAR!
It is WE who are the genuine owners! Not you, Captain.
Those many years ago, when we offered the Ultron to the Utwig
how they capered and laughed at their good fortune... Fools!
Then they begged to hold the device, just for a moment.
To close the deal, I permitted this... a grievous mistake!
The moment the High Proctor touched the Ultron, her body arched
and her eyes rolled back in her head.
She began to babble meaningless phrases and howl like a beast.
We had expected the Utwig to fall for our Sell, to buy the useless device. But never with such gusto!
Their self-doubt and lack of clear reason left them vulnerable to our every manipulation.
But then, the Proctor's body relaxed, and her eyes slowly closed.
When they re-opened, her visual orbs shone with a wild and frightening light.
`This is all we could have dreamed of... and more!', she intoned. `And now, Druuge, as to your price...'
I opened my mouth to speak, but before I could utter a word, the Proctor interrupted
`Wait! The Ultron feeds your thoughts directly to me. Do not speak! I know what you desire.'
What could I say? That the Ultron was a farce and could do no such thing? I was stunned and silent.
The Proctor continued. `You Druuge of the Crimson Corporation desire an object of great antiquity!'
`Something of secret function and value. Very well! It shall be done.'
And with that we were led to a small vault.
The Proctor ceremoniously opened the door of the vault
and explained that because we had been of such great service, ALL of the treasures within were now ours!
Inside we found a hodge-podge of ancient and useless artifacts
a glowing rod, an absurd trident and more such junk.
I could see no way to salvage the disastrous situation at that time.
But when I heard of you, your travels, and your foolish quest for freedom
I realized that you could be the agent of our justice... and lo!... it is so.
You have heard our justification. It is valid and unassailable.
Now GO! And do not return.
```

**Shipped v0.3**:
```
騙子！
那可是敝方才是真正的擁有者！ 不是您，艦長。
多年前，當我方將厄創獻給憂特族時
他們是如何為自身幸運蹦跳歡笑… 傻瓜！
然後他們懇求將該裝置拿在手上把玩，僅短短片刻。
為了成交，在下允准了此舉… 一個嚴重的錯誤！
當高階護法一觸摸厄創，她的身軀便向後拱起
雙眼向上翻。
她開始喃喃無意義的短句並如野獸般嚎叫。
我方原期待憂特族會被銷售話術打動，買下這無用裝置。 但從未預期他們會如此熱切！
他們的自我懷疑與缺乏理性思考，使他們容易被我方任意操縱。
然而，護法的身軀鬆弛下來，雙眼緩緩闔上。
再度睜開時，她的視覺球體閃著狂野而駭人的光芒。
『這是我等夢寐以求的一切… 甚至更多！』她低吟道。『如今，毒賈族，關於您之酬勞…』
在下正欲開口，護法卻搶先打斷
『稍待！ 厄創正將您的念頭直接餵送給我。 莫言！ 我知您所欲。』
在下能說什麼？ 說厄創是騙局，不可能做這樣的事嗎？ 在下震驚而沉默。
護法繼續道。『您血紅集團之毒賈族想要一件古老之物！』
『某種功能與價值皆秘不可宣之物。 好極！ 就這麼辦。』
說著我方便被引至一小型地窖。
護法儀式性地開啟地窖之門
並解釋道由於我方立下大功，其內『所有』寶藏如今皆屬我方！
裡頭我方發現一堆古老又無用的雜什
一根發光棒、一根荒謬的三叉戟以及諸如此類的垃圾。
在下當時看不出如何挽回這場災難。
但當在下聽聞您、您的旅程、您追求自由的愚昧探索
在下便意識到您可為敝方伸張正義之代理人… 果然！… 如此。
您已聽聞我方之辯解。 此辯有效且不可攻擊。
如今走吧！ 莫再返回。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
騙子！
真正的擁有者是我方！ 不是您，艦長。
多年之前，當敝方將厄創獻給憂特族時
他們是如何為自己的好運雀躍歡笑…… 傻瓜！
然後他們懇求把裝置拿在手上把玩，只要一瞬間就好。
為了成交，在下允許了此事…… 一個嚴重的錯誤！
就在高階監督者觸碰厄創的那一刻，她的身軀向後拱起
雙眼向上翻。
她開始喃喃無意義的字句，並如野獸般嚎叫。
我方原本預期憂特族會被推銷話術打動，買下這件無用的裝置。 但從未預料他們會如此熱切！
他們的自我懷疑與缺乏理性，使他們對敝方的每一次操弄毫無抵抗。
然而，監督者的身軀鬆弛下來，雙眼緩緩闔上。
再度睜開時，她的視覺球體閃著狂野而駭人的光芒。
「這是我們夢寐以求的一切…… 甚至更多！」她低吟道。「如今，毒賈族，關於您那份報酬……」
在下正欲開口，監督者卻搶先打斷
「稍待！ 厄創正將您的念頭直接傳送給我。 莫言！ 我知道您所欲求為何。」
在下能說什麼？ 說厄創其實是一場騙局，根本做不到那樣的事嗎？ 在下震驚而沉默。
監督者繼續說。「您們血紅集團之毒賈族想要一件極其古老之物！」
「某種功能與價值皆秘不可宣之物。 好極了！ 就這麼辦。」
說著，我方便被引至一座小型地窖。
監督者儀式性地打開地窖之門
並解釋道：由於敝方立下大功，其內「所有」寶藏如今皆屬敝方！
裡頭我方發現一堆古老又無用的雜什
一根發光魔杖、一根荒謬的三叉戟以及諸如此類的垃圾。
在下當時看不出如何挽回這場災難。
但當在下聽聞您、您的旅程、以及您那愚昧的追求自由之舉
在下便意識到您可以成為敝方伸張正義的代理人…… 果不其然！…… 確實如此。
您已聽聞我方的辯解。 此辯有效且不可反駁。
如今走吧！ 莫再回來。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #2 · `FIGHT_FOR_BOMB` · ✨ v0.7 canonical 升級

**英文原文**:
```
No! You will not!
We know your soul, young Captain. It is no brighter than ours!
We acknowledge our greed. We revel in it.
You are the dishonest one! Hiding your shame in shadows, you fabricate justifications, rationales!
In the end, we are just the same.
But now you stand in our way. You will not be moved.
Therefore, we will add your true name to our Ledger of Hatred, but first
Die, child, DIE!
```

**Shipped v0.3**:
```
不！ 您不能！
我方知您之魂，年輕艦長。 它並不比敝方之魂更明亮！
我方承認自身之貪。 我方樂在其中。
您才是不誠實的那一位！ 將羞恥藏於陰影，捏造理由、藉口！
最終，我方與您是一模一樣的。
然如今您擋在我方之前。 您將無法動搖。
因此，我方將把您真正的名字加入我方之憎恨帳簿，但首先
死吧，孩子，死吧！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
不！ 你不能！
我方知曉你的靈魂，年輕的艦長。 它並不比敝方之靈魂更為明亮！
我方承認自身的貧婪。 我方樂在其中。
你才是不誠實的那一位！ 你把羞恥藏於陰影之中，捧造理由、藉口！
最終，我方與你其實一模一樣。
然而如今你擋在我方之前。 你無法動搖我方。
因此，我方將把你的真名列入仇怨名冊，但首先
死吧，孩子，死吧！
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #3 · `TRADE_FOR_SPHERE` · ✨ v0.7 canonical 升級

**英文原文**:
```
Captain! A special deal, a bargain unequalled!
Instead of the usual payment we would give for this item
what would you say to a different exchange?
We would like to trade your commodity for a highly valuable Precursor artifact
The Rosy Sphere!
Its origins are filled with wonder, and its powers are uncontestable, though subtle.
What is your response?
```

**Shipped v0.3**:
```
艦長！ 一筆特別的交易，無可比擬之議價！
除了敝方通常為此物提供之付款
對於另一種交換方式，您意下如何？
敝方欲用您的商品交換一件價值極高之先驅者文物
玫瑰球！
其起源充滿奇妙，其能力雖細微卻無可爭議。
您之回應為何？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
艦長！ 一筆特別的交易，一項無可比擬的優惠！
除了敝方通常會為此物支付的一般報酬
您意下如何考慮一種不同的交換方式？
敝方願用您手上的商品，交換一件價值極高的先驅者文物
玫瑰球體！
它的起源充滿驚奇，其力量雖然幽微，卻無可置疑。
您的回覆為何？
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #4 · `OK_HERES_SPHERE` · ✨ v0.7 canonical 升級

**英文原文**:
```
Ha-ha! You are indeed a wise young human!
The Rosy Sphere is yours.
```

**Shipped v0.3**:
```
哈哈！ 您確為明智之年輕人類！
玫瑰球歸您所有。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
哈哈！ 您真是位睿智的年輕人類！
玫瑰球體歸您所有了。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #5 · `whats_the_sphere_again` · ✨ v0.7 canonical 升級

**英文原文**:
```
Tell me more about this Artifact, this Rosy Sphere.
```

**Shipped v0.3**:
```
跟我方多說說這件文物，這顆玫瑰球。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
跟我說說這件文物，這顆玫瑰球體。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #6 · `HAVE_SPHERE` · ✨ v0.7 canonical 升級

**英文原文**:
```
The Rosy Sphere! An ancient Precursor artifact of unrivaled beauty and mystery.
Yours for the amazing bargain of only 100 crew.
```

**Shipped v0.3**:
```
玫瑰球！ 一件古老先驅者文物，其美與神秘無可比擬。
您可以極驚人議價僅 100 名船員取得。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
玫瑰球體！ 一件無與倫比之美麗與神秘的古老先驅者文物。
僅需 100 名船員這般驚人的低價，即可歸您所有。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #7 · `HAVE_ART_2` · ✨ v0.7 canonical 升級

**英文原文**:
```
The Glowing Rod! What unearthly powers will you gain
when you hold this coruscating staff high above your head and scream, `Kyeee! Lykeee-lieee!'
And it can be yours for only 100 crew.
```

**Shipped v0.3**:
```
發光棒！ 當您高舉此閃爍杖於頭頂並高喊『Kyeee！ Lykeee-lieee！』時
您將獲得何等超自然之力！
您可僅以 100 名船員擁有。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
發光魔杖！ 當您將這根閃爍的魔杖高舉過頭並大喊「Kyeee! Lykeee-lieee!」時
您將獲得何等超凡之力！
僅以 100 名船員之代價，它便可歸您所有。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #8 · `INIT_SPACE_HELLO` · ✨ v0.7 canonical 升級

**英文原文**:
```
Greetings friend and fellow explorer.
I am an Officer of the Crimson Corporation.
We are the Druuge.
We are delighted to make your acquaintance, and hope that we can do business together.
Should your desires be similar, please hurry to our main trading world at <% comm.getStarName("Zeta Persei", "druuge") %> I.
```

**Shipped v0.3**:
```
問候，朋友，同為探索者。
在下為血紅集團之高級專員。
我方是毒賈族。
很榮幸與您相識，並希望我方能共同做生意。
若您所欲相符，請速前往我方位於 <% comm.getStarName("英仙座ζ", "druuge") %> （Zeta Persei） I 之主要貿易世界。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您好，朋友，同為探索者。
在下是血紅集團之高級專員。
我方是毒賈族。
很高興與您相識，並希望我方能一同做生意。
若您所求相合，請速前往我方位於 <% comm.getStarName("英仙座ζ", "druuge") %>（Zeta Persei） I 的主要貿易世界。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #9 · `GEN_INFO_AT_TRADE_WORLD_2` · ✨ v0.7 canonical 升級

**英文原文**:
```
While I am sure, Captain, that you would never make this foolish mistake
I still feel I should warn you about one of our laws, specifically
Druuge Statute 3429 - subsection A86, Definition of Starship Derelicts.
Simply put, Captain, this statute recognizes that the universe is an inherently hostile place
and any ship which is unable to defend itself incites violence
usually because someone will try to take the unarmed ship by force.
Therefore any unarmed vessel in our space is defined as a derelict
and is available for salvage by anyone who finds it.
```

**Shipped v0.3**:
```
在下確信，艦長，您絕不會犯此愚昧之錯
然在下仍覺得應提醒您敝方之一條律法，即
毒賈法規第 3429 條 - A86 分節，廢艦之定義。
簡言之，艦長，此法規承認宇宙本質為敵對之所在
任何無力自衛之艦艇皆挑起暴力
通常因為總有人試圖以武力奪取此無武裝之艦艇。
因此我方星域內任何無武裝載具皆被定義為廢艦
並可由任何發現者打撈之。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
在下確信，艦長，您絕不會犯下如此愚昧的錯誤
然而在下仍覺得應該提醒您一條敝方之法規，特別是
毒賈條例 3429 號－A86 分項〈星艦廢船之定義〉。
簡而言之，艦長，此條例承認宇宙本質上為一敵對之場所
任何無自衛能力之船艦，將招致暴力
通常是因為總有人會試圖以武力奪取無武裝之船艦。
故凡於我方星域內之無武裝載具，均定義為廢船
並可由任何發現者依法回收處置。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #10 · `GEN_INFO_AT_TRADE_WORLD_3` · ✨ v0.7 canonical 升級

**英文原文**:
```
In case it has not been made clear to you, Captain
aside from your crew, there are certain items which we are willing to trade for.
Specifically, these include: Vortex Spawners, HyperWave 'Casters
and the tough, fungal mats discarded by the Mycon Deep Children
as they penetrate a planet's crust.
```

**Shipped v0.3**:
```
以防您尚未清楚，艦長
除您之船員外，敝方尚有特定願交易之物品。
具體而言，包括:漩渦生成器、超波廣播器
以及麥孔深淵之子穿透行星地殼時
所拋棄之堅韌真菌墊。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
以防您尚未清楚，艦長
除了您的船員之外，敝方尚有若干特定願意交易的物品。
具體而言，包括：漩渦生成器、超波播送器
以及麥孔深層幼體穿透行星地殼時
所拋棄之堅韌真菌墊。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #11 · `GEN_INFO_AT_TRADE_WORLD_4` · ✨ v0.7 canonical 升級

**英文原文**:
```
You may be surprised to learn that we are deeply spiritual beings, Captain.
We worship our god with great enthusiasm.
You want details? Why certainly.
We Druuge are especially fortunate souls.
Most aliens we have encountered have, at best, a tenuous relationship with their gods
but we Druuge have an iron-clad contract!
Our document reads as follows:
Whereas the Druuge (hereinafter known as `the Worshippers')
wish to establish a long-term relationship with an omnipotent and all-knowing deific entity
(hereinafter known as `God' or `god')
which shall mutually benefit both parties, the parties agree to abide by the following terms and commitments
for the rest of eternity.
The Worshippers hereby promise to perform faithfully and to the best of their ability
the following:
1. Worshippers shall make regular and sincere obeisance to God, including but not limited to
prayer, sacrifice, and the building of large structures.
2. Worshippers shall make every attempt to convert non-believers (hereinafter known as `Them')
making sure to obtain signed documents from same attesting to said conversion.
3. Worshippers shall not enter into an agreement with another deity, without written permission from God.
In consideration of the above correctly performed obeisance, God shall provide:
1. Continued existance with little or no modification to the perceived reality of the Worshippers.
2. No fewer than 3 miracles (Force Majeure), whose exact nature and timing
shall be left to God's sole discretion.
3. Worshippers shall enjoy some form of life after death
which shall remain a complete and total mystery to the Worshippers until such time as they die.
We, the undersigned, hereby swear to fulfill our obligations as defined above.
Signed, The Druuge.
(God, being omni-present and all-knowing is considered to have signed this document, by default.)
```

**Shipped v0.3**:
```
您可能會驚訝地發現，我方是深具靈性之生靈，艦長。
我方以極大熱忱崇拜我方之神。
您想知道細節？ 當然可以。
我方毒賈族尤為幸運之靈。
我方所遇之大多外族，充其量與其神明有著薄弱之關係
但我方毒賈族擁有一鐵板釘釘之契約！
我方之文件內容如下:
鑒於毒賈族(下稱『立約人』)
希望與一全能且全知之神性存有
(下稱『神』或『神明』)
建立長期關係，以互利雙方，雙方同意遵行下列條款與承諾
直至永恆。
立約人謹此承諾將忠實地並盡其所能履行
下列事項:
一、立約人應向神做定期且誠摯之敬拜，包括但不限於
祈禱、獻祭與大型建物之興建。
二、立約人應盡力使非信徒(下稱『他者』)改宗
並確保取得後者所簽署之改宗證明文件。
三、立約人未經神書面許可，不得與其他神靈締結協議。
作為上述正確履行敬拜之對價，神應提供:
一、對立約人所知覺之現實維持存續，僅作極少或無修改。
二、不少於三次奇蹟(不可抗力)，其確切性質與時機
悉由神獨自裁量。
三、立約人應享有某形式之來世
其性質對立約人保持完全神秘，直至他們死亡時方揭示。
吾等，具名於下者，謹此立誓履行上述所定之義務。
簽名，毒賈族。
(神因無所不在且全知，據此視為預設簽署本文件。)
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您或許會驚訝地發現，我方是極具靈性的生靈，艦長。
我方以極大熱心崇拜我方之神。
您想知道細節？ 當然可以。
我方毒賈族尤為幸運之靈。
我方所遇之大多外族，充其量與其神明有著薄弱之關係
但我方毒賈族擁有一鐵板釘釘之合約！
本合約之內容如下：
鑑於毒賈族（以下簡稱「崇拜方」）
希望與一位全能且全知之神性實體
（以下簡稱「神」或「神明」）
建立長期關係，以互蒙其利，雙方同意茲此遵行下列條款與義務
直至永恆。
崇拜方茲此承諾將忠實地並盡其所能履行
下列事項：
一、崇拜方應向神明行定期且誠摯之敬拜，包括但不限於
祈禱、獻祭、與大型建物之興建。
二、崇拜方應盡力使非信徒（以下簡稱「他者」）改宗
並確保取得後者所簽署之改宗證明文件。
三、崇拜方未經神明書面許可，不得與其他神靈締結協議。
作為上述正確履行敬拜之對價，神明應提供：
一、對崇拜方所感知現實之持續存續，僅作極少或無修改。
二、不少於三次奇蹟（不可抗力），其確切性質與時機
悉由神明獨自裁量。
三、崇拜方應享有某種形式之來世
其性質對崇拜方保持完全神秘，直至他們死亡之時方得揭曉。
我方，具名於下者，茲此立誓履行上述所定之義務。
簽署：毒賈族。
（神明因無所不在且全知，據此視為預設簽署本文件。）
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #12 · `SCAN_FRAGMENTS` · ✨ v0.7 canonical 升級

**英文原文**:
```
We know that you have Mycon Deep Child egg case fragments aboard your vessel.
Would you consider trading them to us for a shiny new Mauler starship?
```

**Shipped v0.3**:
```
敝方知您艦上帶有麥孔深淵之子卵殼碎片。
您是否考慮以其與敝方交換一艘閃亮的新蹂躪者艦？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我方得知您艦上帶有麥孔深層幼體之卵殼碎片。
您是否考慮以此與敝方交換一艘閃亮的全新毒賈重擊者艦？
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #13 · `SCAN_DRUUGE_CASTER` · ✨ v0.7 canonical 升級

**英文原文**:
```
Our sensors reveal that you have one of our more powerful HyperWave 'Casters on board your ship.
Have no fear, Captain. It was abandoned on the Burvixese moon
and by our law it belongs to you; however
we are fond of the device and wish to regain it through trade.
Give us the 'Caster, and we will give you all the fuel your ship can hold.
```

**Shipped v0.3**:
```
敝方感應器顯示您艦上有一具敝方較強之超波廣播器。
無須擔憂，艦長。 它是於布維族之衛星被棄置
依敝方之法它屬於您;然
敝方仍鍾愛此裝置並希望透過交易取回。
將廣播器交予敝方，敝方將給您艦艇所能容納之全部燃料。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
敝方感應器顯示您艦上有一具我方較為強力的超波播送器。
無須擔憂，艦長。 它是於布維族的衛星上遭棄置
依敝方之法，它屬於您；然而
我方仍鍾愛此裝置並希望透過交易將其取回。
將此播送器交予敝方，我方將給您艦艇所能容納之全部燃料。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #14 · `buy_art_2` · ✨ v0.7 canonical 升級

**英文原文**:
```
I require the Glowing Rod.
```

**Shipped v0.3**:
```
我要那根發光棒。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要那根發光魔杖。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #15 · `buy_rosy_sphere` · ✨ v0.7 canonical 升級

**英文原文**:
```
I wish to acquire the Rosy Sphere.
```

**Shipped v0.3**:
```
我想取得玫瑰球。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我想取得玫瑰球體。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #16 · `sell_caster` · ✨ v0.7 canonical 升級

**英文原文**:
```
I will sell the HyperWave 'Caster to you.
```

**Shipped v0.3**:
```
我把超波廣播器賣給你們。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要把超波播送器賣給你們。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #17 · `sell_spawner` · ✨ v0.7 canonical 升級

**英文原文**:
```
I will sell the Portal Spawner to you.
```

**Shipped v0.3**:
```
我把傳送門生成器賣給你們。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要把傳送門生成器賣給你們。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #18 · `BOUGHT_FRAGMENTS` · ✨ v0.7 canonical 升級

**英文原文**:
```
I accept the deal for the Mycon Deep Child eggcase.
```

**Shipped v0.3**:
```
在下接受麥孔深淵之子卵殼之交易。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我接受這項麥孔深層幼體卵殼之交易。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #19 · `BOUGHT_CASTER` · ✨ v0.7 canonical 升級

**英文原文**:
```
I will buy the HyperWave 'Caster.
```

**Shipped v0.3**:
```
在下將購入超波廣播器。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要買下這具超波播送器。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #20 · `BOUGHT_SPAWNER` · ✨ v0.7 canonical 升級

**英文原文**:
```
I will take the QuasiSpace Portal Spawner.
```

**Shipped v0.3**:
```
在下將取走準空間傳送門生成器。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要收下這具準空間傳送門生成器。
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

### #21 · `SALVAGE_YOUR_SHIP_2` · ✨ v0.7 canonical 升級

**英文原文**:
```
Under the authority of Druuge Statute 3429, subsection A86
`Definition of Starship Derelicts'
I hereby declare your undefended vessel as my salvaged property.
You have five seconds to vacate the premises before I am forced to remove you by force
Time's up!
```

**Shipped v0.3**:
```
依毒賈法規第 3429 條 A86 分節之權限
『廢艦之定義』
在下謹此宣告您之無防禦艦艇為在下之打撈財產。
您有五秒時間離開此地，否則在下將被迫以武力驅離
時間到！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
依毒賈條例 3429 號－A86 分項
〈星艦廢船之定義〉之授權
在下茲此宣告您那艘無防禦之艦艇為在下之打撈財產。
您有五秒鐘的時間離開此地，否則在下將被迫以武力將您驅離
時間到！
```

**推薦**: B (v3) — v0.7 canonical 升級（Master_Glossary / dossier §四 align）

**你的選擇**: A / B / C(自訂)

---

## 🔴 語意/voice 差異大（2 項）

### #22 · `GOODBYE_FROM_BOMB_PLANET` · 🔴 語意/voice 差異大

**英文原文**:
```
Your appreciation of this difficult situation does you credit.
```

**Shipped v0.3**:
```
您對此困境之理解令您增光。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您對這艱難情勢的體諒，令人讚賞。
```

**推薦**: B (v3) — 語意/voice 差異需重定，v3 已對齊 dossier §四 v0.7

**你的選擇**: A / B / C(自訂)

---

### #23 · `bye` · 🔴 語意/voice 差異大

**英文原文**:
```
I will leave now.
```

**Shipped v0.3**:
```
我現在要走了。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我這就告辭。
```

**推薦**: B (v3) — 語意/voice 差異需重定，v3 已對齊 dossier §四 v0.7

**你的選擇**: A / B / C(自訂)

---

## 🟠 措辭改變（6 項）

### #24 · `isnt_this_slave_trading` · 🟠 措辭改變

**英文原文**:
```
Gee, isn't this kind of like... slave trading?
```

**Shipped v0.3**:
```
喂，這不是有點像… 販奴嗎？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
咦，這聽起來不就是……販奴交易嗎？
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

### #25 · `whats_up_at_trade_world` · 🟠 措辭改變

**英文原文**:
```
What can you tell us about this trade world?
```

**Shipped v0.3**:
```
跟我方說說這個貿易世界吧。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
關於這座貿易世界，你能告訴我什麼？
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

### #26 · `READY_TO_BUY` · 🟠 措辭改變

**英文原文**:
```
We are prepared to make a deal.
```

**Shipped v0.3**:
```
敝方已備好議價。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我方已準備好進行交易。
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

### #27 · `EXCHANGE_MADE` · 🟠 措辭改變

**英文原文**:
```
The agreed-upon exchange is hereby enacted.
```

**Shipped v0.3**:
```
所議之交換於此實施。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
茲此執行協議之交易。
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

### #28 · `want_to_sell` · 🟠 措辭改變

**英文原文**:
```
I would like to sell items.
```

**Shipped v0.3**:
```
我想出售物品。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我想要賣些東西。
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

### #29 · `BOUGHT_MAIDENS` · 🟠 措辭改變

**英文原文**:
```
I will purchase the fertile Shofixti adolescents.
```

**Shipped v0.3**:
```
在下將購入這些能生育之修烈士族少年。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我將採購那些具生殖力的年輕修烈士少女。
```

**推薦**: 依推薦（多為 B）— 措辭改進但語意等價 · shipped 有 canonical 尾巴則保留 A

**你的選擇**: A / B / C(自訂)

---

## 🟡 微調（等價）（71 項）

### #30 · `AMBUSH_IS_FIRST_HELLO` · 🟡 微調（等價）

**英文原文**:
```
We are the Druuge of the Crimson Corporation. The planet you approach belongs to us.
All other claims are hereby rendered invalid and uncontestable.
Depart.
```

**Shipped v0.3**:
```
我方是血紅集團（Crimson Corporation）之毒賈族。 爾所接近的行星為敝方所有。
所有其他主張至此宣告無效且不可爭議。
離去。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我方是血紅集團之毒賈族。 您所接近的行星屬於敝方所有。
所有其他主張均茲此宣告無效且不可爭議。
離開。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #31 · `INIT_BOMB_WORLD_HELLO` · 🟡 微調（等價）

**英文原文**:
```
Fancy meeting you here, Captain!
```

**Shipped v0.3**:
```
真巧在這裡遇到您，艦長！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
真湊巧在此見到您，艦長！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #32 · `SUBSEQ_BOMB_WORLD_HELLO` · 🟡 微調（等價）

**英文原文**:
```
The treasure on this world is our property! It belongs to the Crimson Corporation.
Your presence here can only be interpreted
as an attempt to deprive us of what is rightfully ours!
Leave!.. And do not bother us again!...
Or prepare to suffer the severe consequences.
```

**Shipped v0.3**:
```
此世界之寶藏為敝方之財產！ 屬於血紅集團。
您出現在此，只能被解讀為
意圖剝奪敝方合法所有之物！
離開！… 且莫再打擾我方！…
否則請準備承受嚴重後果。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
此世界的寶藏是敝方的財產！ 它屬於血紅集團。
您出現於此，只能被解讀為
意圖剝奪我方合法應得之物！
離開！…… 且莫再打擾敝方！……
否則請準備承擔嚴重的後果。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #33 · `whats_up_at_bomb_planet` · 🟡 微調（等價）

**英文原文**:
```
Druuge starship captain. Justify your presence here.
```

**Shipped v0.3**:
```
毒賈族星艦艦長。 說明你為何在此。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
毒賈艦長。 說明你出現於此的理由。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #34 · `GEN_INFO_AT_BOMB_PLANET` · 🟡 微調（等價）

**英文原文**:
```
We, the appointed representatives of the Crimson Corporation 
merely come to obtain the fair and reasonable payment for our goods!
We travelled to this region of space years ago to sell the useless Ultron device to the Utwig.
We knew even then of the weapon on the surface below us -- this was to be our price!
But the Utwig used a clever ploy to cheat us!
I had convinced the morose Utwig fools that the Ultron was the answer to all of their pitiful dreams.
`Powers?', the Proctors whined. `Will it give us the powers we crave?' 
I assured them that, yes, the Ultron would give them the Second Sight
the Ultron would allow them to see into the past and the future
the Ultron would slowly imbue each of them with unique secret powers of great significance
the Ultron would ensure that their race's huge potential for greatness would be fulfilled.
Then... then a mistake was made.
Enough foolishness! We will take the Precursor device from the surface and then leave.
Thereafter, I may see fit to bequeath the entire planet to you, Captain
for your invaluable services in the past
provided you leave now!
```

**Shipped v0.3**:
```
我方，血紅集團之委任代表
僅是前來收取敝方商品公平合理之付款！
數年前我方前往此星域，將無用之厄創賣給憂特族。
那時我方便已知曉下方地表之武器 —— 那應是我方之應得！
然憂特族用巧計欺騙了我方！
在下曾說服那些陰鬱的憂特族傻瓜，讓其相信厄創是他們所有可悲夢想之答案。
『能力？』護法們哀求道。『它能否賜予我等所渴求之能力？』
在下向他們保證，是的，厄創將賜予他們二度靈視
厄創將讓他們得以看見過去與未來
厄創將漸次為每一位灌輸具有重大意義的獨特秘能
厄創將確保他們一族偉大之潛能得以實現。
然後… 然後犯了一個錯誤。
夠了愚行！ 我方將從地表拿走先驅者裝置，然後離開。
此後，或許在下會樂意將整顆行星贈予您，艦長
以答謝您過往無價之貢獻
前提是您現在離開！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
敝方，血紅集團之委任代表
僅是前來收取本商號商品那份公平合理之報酬！
數年之前，敝方前往此星域，將無用的厄創裝置賣給憂特族。
那時我方便已知曉下方地表的武器 —— 那本應是敝方應得之報酬！
然而憂特族用了巧妙的詭計欺騙了我方！
在下曾說服那些陰鬱的憂特族傻瓜，讓他們相信厄創是他們一切可悲夢想的答案。
「能力？」監督者哀求道。「它能否賜予我們所渴望的能力？」
在下向他們保證，是的，厄創將賜予他們二度靈視
厄創將讓他們得以窺見過去與未來
厄創將漸次為每一位灌注具有重大意義的獨特秘能
厄創將確保他們一族偉大的潛能得以實現。
然後……然後犯了一個錯誤。
夠了，愚行到此為止！ 敝方將從地表取走那件先驅者裝置，然後離去。
此後，或許在下會樂於將整顆行星贈予您，艦長
以答謝您過往那份無價的貢獻
前提是您現在就離開！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #35 · `we_get_bomb` · 🟡 微調（等價）

**英文原文**:
```
This Precursor artifact does not belong to you. It is rightfully ours. Stand aside.
```

**Shipped v0.3**:
```
這件先驅者文物不屬於你們。 依法屬於我方。 讓開。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
這件先驅者文物不屬於你們。 它是我方合法所有。 讓開。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #36 · `then_we_take_bomb` · 🟡 微調（等價）

**英文原文**:
```
Regardless of your feelings in this matter,  we will now take the device.
```

**Shipped v0.3**:
```
無論你們對此事有何感受，我方現在就要取走該裝置。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
不管你們對此事作何感想， 我們現在就要拿走那件裝置。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #37 · `NOT_ENOUGH_ROOM` · 🟡 微調（等價）

**英文原文**:
```
You don't have enough room in your fleet for the ships we want to give you.
```

**Shipped v0.3**:
```
您艦隊中沒有足夠空間容納敝方欲給予的艦艇。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您的艦隊沒有足夠的空間容納敝方所要贈予您的艦艇。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #38 · `no_way` · 🟡 微調（等價）

**英文原文**:
```
Thanks, but no thanks.
```

**Shipped v0.3**:
```
謝了，但不用。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
多謝，但敬謝不敏。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #39 · `OK_REGULAR_DEAL` · 🟡 微調（等價）

**英文原文**:
```
Very well, we can understand your trepidation.
We have been unfair in springing this offer on you so suddenly.
Perhaps we can offer the deal again, in the future
when you have had time to think about it.
```

**Shipped v0.3**:
```
很好，敝方理解您之遲疑。
如此突然拋出此提議實屬敝方不公。
或許將來，當您有時間思考後
敝方可再次提出此交易。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
很好，敝方能理解您的猶豫。
如此突然地向您提出此議，是我方不夠周到。
或許敝方可以在未來再度提出此交易
待您有時間好好考慮之後。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #40 · `way` · 🟡 微調（等價）

**英文原文**:
```
I accept this unusual offer.
```

**Shipped v0.3**:
```
我接受此不尋常之提議。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我接受這項不尋常的提議。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #41 · `SPHERE_IS` · 🟡 微調（等價）

**英文原文**:
```
Its genesis is lost in antiquity, along with the race who created it
the marvelous Precursors!
Note how the device glows, how it throbs... pulsing slowly... bright... then dark...
like the heart of a slumbering god.
Captain, this artifact has been in our possession for eons.
Vast brutal wars have been fought over its possession.
The offer we make to you here today is quite unique!
Do not make a hasty choice.
```

**Shipped v0.3**:
```
其誕生已失於遠古，連同創造它的種族
那奇妙的先驅者！
注意該裝置如何發光、如何搏動… 緩慢地脈動… 明… 暗…
如沉睡之神的心臟。
艦長，此文物於敝方所有已歷萬年。
巨大殘酷之戰爭曾為爭奪其擁有權而發動。
敝方今日對您之提議相當獨特！
莫倉促決定。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
它的誕生已湮沒於遠古，連同創造它的那個種族
那奇妙的先驅族！
請注意此裝置如何發光、如何搏動…… 緩緩地脈動…… 明亮…… 幽暗……
猶如一位沉睡神明的心臟。
艦長，此文物落於敝方所有已逾萬年。
無數殘酷的巨大戰爭曾為爭奪其歸屬而爆發。
敝方今日對您所提出的條件，可謂絕無僅有！
請勿倉促決定。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #42 · `WE_SELL_FOR_CREW` · 🟡 微調（等價）

**英文原文**:
```
Since this is your first time trading with us, Captain
allow me to explain our standard operating procedures.
We will sell you fuel, ancient artifacts, even our own Mauler starships!
All that we ask in return is that you assign some of your crew to serving here at our trade world
on a permanent basis.
```

**Shipped v0.3**:
```
既然這是您首次與敝方交易，艦長
請容在下說明敝方之標準作業程序。
敝方將售予您燃料、古老文物、甚至敝方自身之蹂躪者艦艇！
敝方只要求您將部分船員永久指派
至此為敝方之貿易世界服務。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
既然這是您首次與敝方交易，艦長
請容在下說明我方的標準作業流程。
敝方將售予您燃料、古老文物、乃至敝方自身的毒賈重擊者艦！
我方所要求的回報僅僅是：您指派部分船員來此
於敝方的貿易世界永久服役。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #43 · `i_will_never_trade_crew` · 🟡 微調（等價）

**英文原文**:
```
I will never sell my crew to be your slaves.
```

**Shipped v0.3**:
```
我絕不會把我的船員賣去給你們當奴隸。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我絕不會出賣我的船員給你們當奴隸。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #44 · `YOUR_LOSS` · 🟡 微調（等價）

**英文原文**:
```
This a great loss for us both, but we will not make an exception in your case.
However, please try to be receptive to what I am about to say.
We have taken the liberty of entering your ships's computer system
to investigate the agreement signed by the Earthling volunteers who serve aboard your vessel.
As we expected, we found that they have promised to obey you, Captain, under every circumstance
no exceptions.
You are fully within your rights to deal with us in our required manner.
Should you change your mind, we will always be ready to work with you, Captain.
```

**Shipped v0.3**:
```
這對雙方皆為重大損失，但敝方不會為您破例。
然，請試著接受在下即將所述之言。
敝方擅自進入您艦艇的電腦系統
查閱了您艦上地球人志願者所簽之協議。
如敝方所預期，我方發現他們已允諾在任何情況下遵從您，艦長
毫無例外。
您完全有權以敝方要求之方式與敝方交易。
若您改變主意，敝方將永遠準備好與您合作，艦長。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
這對雙方都是重大損失，但敝方不會為您破例。
然而，請試著接納在下接下來所要說的話。
我方擅自進入了您艦上的電腦系統
查閱了那些於您艦上服役的地球人志願船員所簽下的協議。
一如所料，我方發現他們已承諾聽從您的命令，艦長，於任何情境下皆然
毫無例外。
您完全有權以敝方所要求之方式與我方交易。
倘若您改變心意，我方隨時樂意與您合作，艦長。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #45 · `NO_SLAVE_TRADE` · 🟡 微調（等價）

**英文原文**:
```
No, no, no, Captain! Slaves have no choice in their destiny, no freedom.
We would never accept the permanent assignment of one of your people
unless we knew that they had granted you the rights to make such a deal.
```

**Shipped v0.3**:
```
不、不、不，艦長！ 奴隸對自身命運無選擇、無自由。
敝方絕不會接受永久指派您的族人
除非我方知曉他們已授予您做出此類交易之權利。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
不、不、不，艦長！ 奴隸對自身的命運毫無選擇、毫無自由。
敝方絕不會接受永久指派您的族人前來
除非我方確知：他們已授予您進行此類交易之權利。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #46 · `what_do_with_crew` · 🟡 微調（等價）

**英文原文**:
```
Well, what would my crew members do here?
```

**Shipped v0.3**:
```
那我的船員在這裡要做什麼？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
呃，我的船員來到這裡會做些什麼？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #47 · `HAVE_FUN` · 🟡 微調（等價）

**英文原文**:
```
People as skilled as your flagship's crew will receive immediate posts in our starfleet.
They will serve alongside our own Druuge starship personnel
sharing every duty.
```

**Shipped v0.3**:
```
如您旗艦船員之技藝人才，將於敝方之星際艦隊立即獲得職位。
他們將與敝方自身之毒賈族星艦人員並肩服務
共同分擔每一項職責。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
像您艦上這般熟練的船員，將立即獲派職位於敝方的星艦隊。
他們會與我方毒賈艦艇上的原有人員並肩服役
共同分擔一切勤務。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #48 · `im_ready_to_buy` · 🟡 微調（等價）

**英文原文**:
```
...I am ready to make purchases.
```

**Shipped v0.3**:
```
……我準備採購了。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
……我準備好進行採購了。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #49 · `THIS_FOR_SALE` · 🟡 微調（等價）

**英文原文**:
```
Excellent! Let us begin.
Our inventory presently includes...
```

**Shipped v0.3**:
```
極佳！ 讓我方開始吧。
敝方目前存貨包括…
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
太好了！ 讓我方開始吧。
敝方目前的存貨包括……
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #50 · `HAVE_ART_1` · 🟡 微調（等價）

**英文原文**:
```
The Trident of Wimbli! Not just one, but fully THREE mystic prongs give this artifact
its awesome capabilities. Are you strong enough to master its power? Or will it master you?
Cost? 100 crew.
```

**Shipped v0.3**:
```
溫布利三叉戟！ 不只一支，而是完整三支神秘尖叉，賦予此文物
可畏之能力。 您是否強大到可駕馭其力？ 抑或它將反過來駕馭您？
代價？ 100 名船員。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
溫布利三叉戟！ 不只一支，而是完整三支神秘的尖叉，賦予此文物
令人生畏的能力。 您是否強大到能駕馭其力？ 抑或它將反過來駕馭您？
代價？ 100 名船員。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #51 · `SHIPS_AND_FUEL` · 🟡 微調（等價）

**英文原文**:
```
As always, we also have an unlimited supply of exceptionally high-performance starship fuel
at a cost of ten crew for ten units of fuel
as well as a freshly assembled Mauler starship
which we will trade for 100 of your crew.
```

**Shipped v0.3**:
```
如同往常，我方亦有無限之高性能星艦燃料
售價為十名船員換十單位燃料
以及一艘剛組裝完成之蹂躪者艦
我方將以您 100 名船員與您交換。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
如往常一般，我方也備有無限量的高效能星艦燃料
代價為 10 名船員換取 10 單位燃料
此外還有一艘剛出廠的毒賈重擊者艦
敝方願以 100 名您的船員換取此艦。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #52 · `BOUGHT_SHIP` · 🟡 微調（等價）

**英文原文**:
```
Good choice. Your fleet swells with power!
With the purchase of additional Mauler vessels, you would be nigh-invincible!
```

**Shipped v0.3**:
```
好選擇。 您的艦隊威力大增！
再購入額外之蹂躪者艦，您將接近無敵！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
明智的抉擇。 您的艦隊實力大幅增長！
若您再購入額外的重擊者艦，將幾近所向無敵！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #53 · `BOUGHT_FUEL` · 🟡 微調（等價）

**英文原文**:
```
The fuel has been transferred to your vehicle.
I expect you will notice the immediate benefits of our secret fuel additives.
```

**Shipped v0.3**:
```
燃料已轉入您的載具。
在下預期您將立即察覺敝方秘密燃料添加物之效益。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
燃料已注入您的艦艇。
在下相信您很快就會察覺敝方那份秘密燃料添加劑之立即效益。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #54 · `BOUGHT_ART_2` · 🟡 微調（等價）

**英文原文**:
```
So fortunate for you! So sad for me. I fear this relic of the glorious past
was all that kept me from ending my life to leave this vale of tears.
Now what shall I do?
```

**Shipped v0.3**:
```
您真是走運！ 對在下卻多可悲！ 恐這光輝過往之遺物
是唯一阻擋在下了結此生離開此涕谷之物。
如今在下該當如何？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您真是好運！ 我卻悲哀。 在下擔心這件昔日榮光的遺物
本是唯一讓在下不至於了結性命、逃離此淚谷之依託。
如今在下該當如何？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #55 · `BOUGHT_ART_1` · 🟡 微調（等價）

**英文原文**:
```
Ho-ho, Captain! Do not point the prongs at me in such a carefree manner!
I might have been accidentally incinerated, or transported to a hostile dimension.
You wield the Trident with authority, Captain.
I can tell that already you are realizing the true scope of this artifact's powers.
```

**Shipped v0.3**:
```
呵呵，艦長！ 莫將尖叉如此漫不經心地對準在下！
在下可能會被意外燒盡，或被送至敵對次元。
您揮舞此三叉戟頗具威嚴，艦長。
在下已看出您正在領悟此文物之力真正的規模。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
呵呵，艦長！ 請勿如此隨意地將尖叉朝向在下！
在下可能會被意外焚化，或被傳送至一個充滿敵意的維度。
您駕馭三叉戟的手法堪稱權威，艦長。
在下看得出來，您已經開始理解此文物真正的力量規模了。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #56 · `BOUGHT_SPHERE` · 🟡 微調（等價）

**英文原文**:
```
I stride to the Sphere's containment vessel and pull it slowly from its ancient cradle.
The dust of centuries has made a gentle weld... there! It has come free.
Now, into your hands I place the ancient sphere. Do you feel that, Captain?
Has the warmth already penetrated the skin of your hands into your soul?
Well it soon shall, Captain. Just keep trying.
```

**Shipped v0.3**:
```
在下步向玫瑰球的封存容器並將其緩緩自古老的搖籃中拉出。
數世紀之塵已將其輕輕黏結… 到了！ 它脫離了。
如今，在下將這顆古老之球放入您手中。 您可感受到嗎，艦長？
那溫暖是否已透過您手掌之皮膚滲入您的靈魂？
嗯很快就會了，艦長。 請繼續嘗試。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
在下步向球體的容器，將它緩緩自那古老的托座中取出。
數個世紀的塵封已將它輕柔地黏合……好了！ 它脫離了。
如今，在下將這顆古老球體置於您的手中。 您感覺到了嗎，艦長？
那股暖意是否已透過您的掌膚，滲入您的靈魂之中？
很快就會的，艦長。 請繼續嘗試。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #57 · `repeat_what_to_sell` · 🟡 微調（等價）

**英文原文**:
```
Uh, could you repeat what you have to sell?
```

**Shipped v0.3**:
```
呃，您能重複一下您有什麼要賣的嗎？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
呃，能不能重複一次你們有什麼要賣的？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #58 · `SUBSEQUENT_SPACE_HELLO` · 🟡 微調（等價）

**英文原文**:
```
Ah, the young starship captain from Earth!
We hope your adventures have brought you wealth.
How can we be of service?
```

**Shipped v0.3**:
```
啊，來自地球之年輕星艦艦長！
我方希望您之冒險已為您帶來財富。
我方能為您效勞嗎？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
啊，來自地球的年輕星艦艦長！
希望您的冒險為您帶來了財富。
有什麼我方能效勞的？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #59 · `whats_up_in_space` · 🟡 微調（等價）

**英文原文**:
```
What can you tell us of your culture, your species?
```

**Shipped v0.3**:
```
說說你們的文化、你們的物種吧。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
你們的文化、你們的物種，能跟我說些什麼？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #60 · `GENERAL_INFO_IN_SPACE_1` · 🟡 微調（等價）

**英文原文**:
```
More than a culture, Captain, we are an organization -- the Crimson Corporation!
Our corporation seeks only to improve our quality of life
and does so via the `Dribble-Down' effect.
```

**Shipped v0.3**:
```
不僅是文化，艦長，我方是一個組織 —— 血紅集團！
本集團僅追求改善我等之生活品質
並透過『涓滴下滲』效應達成之。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
遠不止是文化，艦長，我方是一個組織 —— 血紅集團！
本集團所追求的僅是提升我方之生活品質
並透過「涓滴」效應加以達成。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #61 · `GENERAL_INFO_IN_SPACE_2` · 🟡 微調（等價）

**英文原文**:
```
You wish to know more about us? Excellent! 
After all, knowledge should be free, eh Captain?!
Let's see... about us
well, we ARE the Crimson Corporation, and the Crimson Corporation is us.
When the Corporation's earnings are up, our quality of life soars, and our benefit packages improve.
The further up the ladder you are, the more you profit individually.
When times are hard, the Corporation must cut costs, usually by laying off employees.
Since everything on our world is Corporation property
this means any ex-employee is instantly trespassing and is guilty of stealing Corporation property
such as air and sunlight. The only appropriate penalty for theft
is to feed the furnace.
```

**Shipped v0.3**:
```
您想多了解敝方？ 極佳！
畢竟，知識本應免費，是吧艦長？！
看看… 關於敝方
嗯，敝方『就是』血紅集團，血紅集團『就是』敝方。
本集團盈利上升時，我等生活品質飆升，福利方案改善。
您於階梯上愈往上爬，個人利潤愈豐厚。
困難時期，本集團必須削減成本，通常靠裁員。
由於我方世界之一切皆為集團財產
這意味任何前員工立即為侵入者，並犯有偷竊集團財產罪
諸如空氣與陽光。 對偷竊之唯一適切懲罰
即送熔爐。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您想知道更多關於我方之事？ 好極了！
畢竟，知識本應是免費的，是吧艦長？！
讓在下想想…… 關於我方
嗯，我方「就是」血紅集團，血紅集團就是我方。
當集團營收上升，我方生活品質便隨之飛升，福利方案也隨之改善。
您於階級上爬得越高，您個人所獲之利潤便越豐厚。
景氣不佳時，集團必須削減成本，通常做法是資遣員工。
由於我方世界之上一切皆為集團財產
這意味著任何前員工瞬間即成非法侵入者，並犯下竊取集團財產之罪
諸如空氣與陽光。 對於竊盜之罪，唯一合宜的懲處
即是送去餵熔爐。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #62 · `GENERAL_INFO_IN_SPACE_3` · 🟡 微調（等價）

**英文原文**:
```
You know, Captain, we have heard that there is a race called the Melnorme
which has recently entered this part of the galaxy.
We understand that they sell fuel for gross profit
charge fees for common knowledge
and provide a `rescue service' which amounts to little more than piracy.
How criminal.
Just an aside, Captain. We thought you might like to know
that the resources which can be salvaged from a Melnorme wreck are phenomenal.
```

**Shipped v0.3**:
```
您知道嗎，艦長，我方聽聞有一族名為梅諾商
最近進入銀河此區。
我方了解他們售燃料謀取暴利
對常識收費
並提供『救援服務』，實則近乎海盜行為。
何其罪惡。
順帶一提，艦長。 我方想您或許有意知道
可自梅諾商殘骸打撈出之資源相當驚人。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您知道嗎，艦長，我方聽說有一個名為梅諾商之種族
近來進入了銀河系的這一部分。
據我方所知，他們販售燃料以牟取暴利
對常識性知識收取費用
並提供一種所謂「救援服務」，其本質不過是海盜行為。
何其罪惡。
順帶一提，艦長。 我方猜您可能會想知道
從一艘梅諾商船骸上可回收的資源相當驚人。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #63 · `GENERAL_INFO_IN_SPACE_4` · 🟡 微調（等價）

**英文原文**:
```
More information, Captain? You have learned so much about us already!
Very well.
You may be interested to know that we recently diverted the onslaught of a hostile alien race.
We learned of its approach from our ex-clients, the Burvixese.
The kind and philanthropic Burvixese informed us that a dark and sinister armada
had detected our HyperWave emissions, and though still distant
was inexorably homing in on our central trade world at <% comm.getStarName("Zeta Persei", "druuge") %>.
We devised a brilliant plan, implemented it perfectly
and were thus spared gruesome death at the hands of the aliens
who we later learned call themselves the `Kohr-Ah'.
```

**Shipped v0.3**:
```
更多資訊，艦長？ 您已對敝方了解如此之多！
很好。
您或許有興趣知道，我方近來成功轉移了一敵對外星種族的攻擊。
我方是從前客戶布維族處得知其接近。
和藹博愛之布維族告知我方有一支黑暗邪惡之艦隊
偵測到我方之超波發射，儘管仍在遠方
卻不可阻擋地朝我方位於英仙座ζ之中央貿易星而來。
我方設計了一個絕妙計畫，完美地執行了它
因而免遭那外族之殘酷屠戮
那族後來我方得知自稱『柯亞族』。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
更多資訊，艦長？ 您已對我方瞭解如此之多！
很好。
您或許有興趣知道，我方近日成功轉移了一波外族的猛烈進攻。
這消息是我方從前客戶 —— 布維族那裡得知的。
那和藹博愛的布維族告知我方：一支黑暗而陰險的艦隊
已偵測到我方之超波發射，儘管仍在遠方
卻正無可阻擋地朝我方位於 <% comm.getStarName("英仙座ζ", "druuge") %> 之中央貿易世界逼近。
我方構思出一項絕妙的計畫，完美地執行了它
因而幸免於遭受那些外族之手的殘忍屠戮
那個種族我方後來得知，自稱為「柯亞族」。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #64 · `HSTL_TRADE_WORLD_HELLO_1` · 🟡 微調（等價）

**英文原文**:
```
What, you wish to rob our Trade World, eh? Not today, boyo!
```

**Shipped v0.3**:
```
怎麼，您想搶劫敝方貿易世界，嗯？ 今天可不行，小子！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
什麼，你想搶劫敝方的貿易世界，嗯？ 今天可不成，小子！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #65 · `HSTL_TRADE_WORLD_HELLO_2` · 🟡 微調（等價）

**英文原文**:
```
You made a mistake returning here, Captain.
We know your true colors. You are a blackheart.
```

**Shipped v0.3**:
```
您犯了個錯誤，回來這裡，艦長。
敝方已知您真面目。 您是黑心者。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
你回來這裡是犯了個錯誤，艦長。
我方已知你的真面目。 你是個黑心賊。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #66 · `HOSTILE_SPACE_HELLO_1` · 🟡 微調（等價）

**英文原文**:
```
Villains! Pilferers! Crooks!
Look to your souls. Make your peace.
You are about to die.
```

**Shipped v0.3**:
```
惡棍！ 竊賊！ 罪犯！
看看您之靈魂。 做好和解。
您即將死。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
惡徒！ 小偷！ 騙子！
看看你們的靈魂吧。 做好和解。
你們即將赴死。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #67 · `HOSTILE_SPACE_HELLO_2` · 🟡 微調（等價）

**英文原文**:
```
Foul pirate! We know of your violence and thievery.
You are undone, and must pay the price for your wretched deeds!
```

**Shipped v0.3**:
```
卑鄙海盜！ 敝方知曉您之暴行與盜竊。
您已完了，必須為您可悲之惡行付出代價！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
污穢的海盜！ 我方知曉你的暴行與竊行。
你已完蛋，必須為你那些可鄙的行徑付出代價！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #68 · `INITIAL_TRADE_WORLD_HELLO` · 🟡 微調（等價）

**英文原文**:
```
Attention alien starship.
You have arrived at the Central Trade World of the Crimson Corporation
Home of the Druuge.
Be welcome and take advantage of our excellent deals.
```

**Shipped v0.3**:
```
注意，外星星艦。
您已抵達血紅集團之中央貿易星
毒賈族之家。
歡迎並利用敝方之絕佳交易。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
注意，外星艦艇。
您已抵達血紅集團之中央貿易世界
毒賈族之家園。
歡迎光臨，並請善加利用敝方之絕妙交易。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #69 · `SSQ_TRADE_WORLD_HELLO_1` · 🟡 微調（等價）

**英文原文**:
```
It's always pleasant to see you again, Captain.
Are you here today to buy or sell?
```

**Shipped v0.3**:
```
再次見到您總是愉悅，艦長。
您今日來此是要買還是要賣？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
再次見到您總是令人愉快，艦長。
您今日光臨是為了買，還是賣？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #70 · `SSQ_TRADE_WORLD_HELLO_2` · 🟡 微調（等價）

**英文原文**:
```
Ah! It is the young human in the giant alien spacecraft.
```

**Shipped v0.3**:
```
啊！ 是那位駕著巨型異星艦艇之年輕人類。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
啊！ 是那位駕著巨型外星飛船的年輕人類。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #71 · `SSQ_TRADE_WORLD_HELLO_3` · 🟡 微調（等價）

**英文原文**:
```
We welcome you to our Trade World once again, Captain.
We are at your service.
```

**Shipped v0.3**:
```
我方再度歡迎您來到敝方貿易世界，艦長。
我方樂於為您效勞。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
再度歡迎您蒞臨我方貿易世界，艦長。
我方為您效勞。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #72 · `SSQ_TRADE_WORLD_HELLO_4` · 🟡 微調（等價）

**英文原文**:
```
Hello Captain. Back so soon?
```

**Shipped v0.3**:
```
哈囉艦長。 這麼快就回來了？
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您好，艦長。 這麼快就回來了？
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #73 · `GEN_INFO_AT_TRADE_WORLD_1` · 🟡 微調（等價）

**英文原文**:
```
This is the heart of our operation, the vital core of the Crimson Corporation.
A million deals are made here each day, perhaps more.
You would be wise to take advantage of all our services, Captain.
You will not find better deals anywhere.
```

**Shipped v0.3**:
```
此為敝方營運之核心，血紅集團之要害。
每日於此進行百萬筆交易，或許更多。
您明智地利用敝方所有服務，艦長。
您無處能找到比這更好之交易。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
此處乃敝方營運之心臟，血紅集團之命脈核心。
每日於此完成的交易數以百萬計，或許更多。
您明智地善加利用敝方之全部服務，艦長。
您到任何地方都找不到比這更好的交易。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #74 · `SCAN_MAIDENS` · 🟡 微調（等價）

**英文原文**:
```
It has come to our attention that you have female Shofixti creatures on board your ship.
We have the means to fertilize these creatures artificially
allowing us to produce a hybrid beast to attend our furnaces.
We must have those females, Captain!
We are prepared to offer you fully six of our devastating Mauler starships in exchange.
```

**Shipped v0.3**:
```
敝方注意到您艦上有雌性修烈士族生物。
敝方有法為此等生物人工授精
可產生一混種獸來看管敝方之熔爐。
我方必得那些雌性，艦長！
敝方準備好以整整六艘敝方毀滅性蹂躪者艦艇與您交換。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
敝方注意到您艦上有雌性修烈士族生物。
我方有辦法為此等生物進行人工授精
藉此培育一種混種獸來看管敝方之熔爐。
我方必須得到那些雌性，艦長！
敝方準備以整整六艘毀滅性的毒賈重擊者艦與您交換。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #75 · `SCAN_ARILOU_SPAWNER` · 🟡 微調（等價）

**英文原文**:
```
We note you possess a Vortex Spawner.
In exchange for the simple device we will give you three Mauler starships
and fill your fuel tanks, at no extra charge.
```

**Shipped v0.3**:
```
敝方注意您擁有一具漩渦生成器。
以此簡單裝置交換，敝方將給您三艘蹂躪者艦
並將您之燃料箱注滿，不另收費。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我方注意到您擁有一具漩渦生成器。
若以此簡單裝置交換，敝方將給您三艘毒賈重擊者艦
並將您的燃料箱注滿，不另收費。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #76 · `ENOUGH_FRAGMENTS` · 🟡 微調（等價）

**英文原文**:
```
We have scanned additional Mycon Egg cases on your ship
however, we have a sufficient supply, and do not intend to make further purchases of this commodity.
```

**Shipped v0.3**:
```
敝方已掃描到您艦上另有麥孔卵殼
然，敝方存量已足，不打算再購此商品。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我方掃描到您艦上尚有其他麥孔卵殼
然而，敝方庫存已足，無意再進一步採購此項商品。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #77 · `READY_TO_SELL` · 🟡 微調（等價）

**英文原文**:
```
Excellent! Let us begin.
Our inventory presently includes:
```

**Shipped v0.3**:
```
極佳！ 讓我方開始吧。
敝方目前之存貨包括:
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
好極了！ 讓我方開始吧。
敝方目前的存貨包括：
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #78 · `BYE_FROM_TRADE_WORLD_1` · 🟡 微調（等價）

**英文原文**:
```
Return soon, Captain. Your patronage is appreciated.
```

**Shipped v0.3**:
```
早日回來，艦長。 感謝您之惠顧。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
請速返，艦長。 敝方感謝您的惠顧。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #79 · `BYE_FROM_TRADE_WORLD_2` · 🟡 微調（等價）

**英文原文**:
```
Until next time, captain.
```

**Shipped v0.3**:
```
下次見，艦長。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
下回再見，艦長。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #80 · `NOT_ENOUGH_CREW` · 🟡 微調（等價）

**英文原文**:
```
Unfortunately, Captain, you do not have enough crew to make this purchase.
```

**Shipped v0.3**:
```
很不幸，艦長，您沒有足夠船員做此採購。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
很遺憾，艦長，您的船員數量不足以完成此次採購。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #81 · `OK_DONE_BUYING` · 🟡 微調（等價）

**英文原文**:
```
Are you sure?... as you wish.
```

**Shipped v0.3**:
```
您確定嗎？… 悉聽尊便。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您確定嗎？…… 悉聽尊便。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #82 · `want_to_buy` · 🟡 微調（等價）

**英文原文**:
```
I would like to make a purchase.
```

**Shipped v0.3**:
```
我想採購。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我想要進行採購。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #83 · `buy_druuge_ship` · 🟡 微調（等價）

**英文原文**:
```
I wish to purchase a Druuge Mauler.
```

**Shipped v0.3**:
```
我想購買一艘毒賈族蹂躪者艦。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我想購買一艘毒賈重擊者艦。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #84 · `buy_art_1` · 🟡 微調（等價）

**英文原文**:
```
I must have Wimbli's Trident.
```

**Shipped v0.3**:
```
我一定要溫布利三叉戟。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我一定要拿到溫布利三叉戟。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #85 · `done_selling` · 🟡 微調（等價）

**英文原文**:
```
I do not wish to sell anything more.
```

**Shipped v0.3**:
```
我不打算再賣任何東西。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我不想再賣任何東西了。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #86 · `sell_maidens` · 🟡 微調（等價）

**英文原文**:
```
I will sell the Shofixti Maidens to you.
```

**Shipped v0.3**:
```
我把修烈士族少女賣給你們。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要把修菲少女賣給你們。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #87 · `sell_fragments` · 🟡 微調（等價）

**英文原文**:
```
I will sell the Egg Case fragments to you.
```

**Shipped v0.3**:
```
我把卵殼碎片賣給你們。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我要把卵殼碎片賣給你們。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #88 · `YOU_GET` · 🟡 微調（等價）

**英文原文**:
```
In exchange, you shall receive 
```

**Shipped v0.3**:
```
作為交換，您將收到 
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
作為交換，您將得到 
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #89 · `YOU_ALSO_GET` · 🟡 微調（等價）

**英文原文**:
```
In addition, as agreed, we will also give you 
```

**Shipped v0.3**:
```
此外，如所議，敝方將另贈予您 
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
此外，依照協議，我方還將給您 
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #90 · `SALVAGE_YOUR_SHIP_1` · 🟡 微調（等價）

**英文原文**:
```
I note that your ship is unarmed and unescorted.
Therefore, by Druuge law, your ship is deemed derelict, and is subject to the laws of salvage.
While I would prefer to take your ship intact, alas, I suspect you will force me to sell it as scrap.
```

**Shipped v0.3**:
```
在下注意到您之艦艇無武裝且無護航。
因此，依毒賈法，您艦被視為廢艦，適用打撈法律。
在下寧願完整取走您之艦艇，然，恐您將迫使在下將其作為廢料出售。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
在下注意到您的艦艇既無武裝亦無護航。
因此，依毒賈之法，您的艦艇被判定為廢船，適用廢船回收之相關法律。
在下原本更希望完整取走您的艦艇，然而，恐怕您將迫使在下把它當作廢料出售。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #91 · `DEAL_FOR_STATED_SHIPS` · 🟡 微調（等價）

**英文原文**:
```
the agreed-upon number of ships.
```

**Shipped v0.3**:
```
所議定之艦艇數量。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
協議所定數量之艦艇。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #92 · `DEAL_FOR_LESS_SHIPS` · 🟡 微調（等價）

**英文原文**:
```
less than the number of ships I originally offered
because you have no room for the the full amount in your fleet!
Unfortunate for you, I'm afraid, but legal I assure you.
```

**Shipped v0.3**:
```
少於在下原提議之艦艇數量
因您艦隊中無容納全數之空間！
恐對您不幸，但在下向您保證合法。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
少於在下原本承諾的艦艇數量
因為您的艦隊沒有足夠空間容納全數！
對您而言確實不巧，敝方深感遺憾，但依法無誤，在下向您保證。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #93 · `DEAL_FOR_NO_SHIPS` · 🟡 微調（等價）

**英文原文**:
```
the number of ships which can be added to your fleet
and according to my scan of your task force, that is none.
A serious mistake on your part captain, I'm afraid, but a great boon for the Firm.
With such a fine deal under my belt, perhaps I should take the rest of the day off.
```

**Shipped v0.3**:
```
可加入您艦隊之艦艇數量
而依在下對您戰鬥組之掃描，該數為零。
您犯了嚴重錯誤，艦長，恐是如此，但對本公司乃一大恩澤。
有此絕妙成交在手，或許在下應該提前下班。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
以您艦隊尚能容納之艦艇數量計
而依在下對您部隊之掃描，該數為零。
這對您而言是個嚴重的失策，艦長，恐怕如此，但對本商號而言則是天大的意外之財。
有了這樣一筆漂亮交易，或許在下今天下午該放個假了。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #94 · `FUEL0` · 🟡 微調（等價）

**英文原文**:
```
All the fuel your ship can hold.
We are now hooking up the fuel lines to fill your tanks.
Hmm..
```

**Shipped v0.3**:
```
您艦艇所能容納之全部燃料。
我方現在正接上燃料管以注滿您之箱體。
嗯…
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您艦艇所能容納的全部燃料。
我方現正接上燃料管，注滿您的箱體。
嗯……
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #95 · `HIDEOUS_DEAL` · 🟡 微調（等價）

**英文原文**:
```
Aieee! I am ruined! You have sucked my full tanks until they are dry!
Cruel Monster! Bloated Villain! Slicer of innocent throats!
What shall I tell the Manager?! My spouse?!
I shall certainly be assigned to tend the furnaces.
I shall burn in the atomic fires!
Aieee!
```

**Shipped v0.3**:
```
Aieee！ 在下毀了！ 您將在下滿箱吸乾至滴水不剩！
殘忍怪物！ 膨脹惡棍！ 割喉無辜者！
在下該對經理人如何交代？！ 對在下之配偶？！
在下必被指派去看管熔爐。
在下將於原子之火中燃燒！
Aieee！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
哎唷唷！ 在下毀了！ 您將在下的滿箱吸到一滴不剩！
殘忍的怪物！ 臃腫的惡棍！ 割無辜者喉嚨之徒！
在下該如何對經理交代？！ 對在下的配偶交代？！
在下必定會被指派去顧那些熔爐。
在下將在原子火焰中焚燒！
哎唷唷！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #96 · `BAD_DEAL` · 🟡 微調（等價）

**英文原文**:
```
This will look very bad on my record, Captain. You have hurt me deeply.
I had expected an understanding between trading partners, between equals
but NO! The moment my back is turned, you fill your bloated tanks far beyond a reasonable limit.
I have learned an important lesson from you today
One I shall never forget.
```

**Shipped v0.3**:
```
此事於在下履歷上將極為難看，艦長。 您深深傷了在下。
在下原期待交易夥伴之間、平等者之間應有的理解
然沒有！ 在下一轉背，您便將您膨脹之箱體注滿遠超合理之限。
在下今日從您處學到重要一課
終生難忘。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
此事在下履歷上將極為難看，艦長。 您深深傷了在下的心。
在下原期待貿易夥伴之間、對等者之間該有的體諒
然而不然！ 在下才一轉身，您便將您那膨脹的箱體注滿，遠超合理限度。
在下今日從您身上學到一堂重要的課
終生難忘。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #97 · `FAIR_DEAL` · 🟡 微調（等價）

**英文原文**:
```
You have received a fair exchange for your device, Captain.
Perhaps more than fair for you.
I will not be able to brag about this exchange, but then again
I need not worry about feeding the furnace.
```

**Shipped v0.3**:
```
您為您之裝置獲得公平之交換，艦長。
或許對您甚至比公平更好。
在下無法拿此交易誇口，但至少
在下無須擔心送熔爐。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
您為您的裝置獲得了公平的交換，艦長。
對您而言或許甚至超越公平。
在下無法拿這筆交易誇口，但至少
在下無須擔憂被送去餵熔爐。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #98 · `GOOD_DEAL` · 🟡 微調（等價）

**英文原文**:
```
Well done, Captain. Quite a fair exchange. Good job.
(hee-hee-hee).
```

**Shipped v0.3**:
```
幹得好，艦長。 相當公平之交換。 好差事。
（hee-hee-hee）。
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
幹得漂亮，艦長。 相當公平的交換。 幹得好。
（嘿嘿嘿）。
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #99 · `FINE_DEAL` · 🟡 微調（等價）

**英文原文**:
```
Ha-ha, yes! Yes! Yes! Yes! Yes! Yes!
A fine deal, Captain. An excellent bargain... for me!
Ho-ho-ho! When I offered you all the fuel you could hold, you could have drained every drop I had.
Cold sweat dripped from my palms as I watched my workers begin the transfer.
And then it was over... so soon! So gloriously soon!
I shall be promoted at least three full steps! A new office! A benefits package!
Fortune has smiled on me today!
I feel so lucky, Captain, that you did not have the forethought to arrive here with a dozen empty tanks.
Thank you! Thank you! Thank you!
```

**Shipped v0.3**:
```
哈哈，是的！ 是的！ 是的！ 是的！ 是的！ 是的！
絕妙之交易，艦長。 極佳之議價… 對在下而言！
Ho-ho-ho！ 當在下提議您可取走全部之燃料時，您本可將在下所有一滴不剩地耗盡。
看著在下之工人開始轉運時，冷汗自在下之掌心滴落。
然後就結束了… 如此之快！ 如此光榮之快！
在下至少會被提升整整三級！ 新辦公室！ 福利方案！
幸運今日對在下微笑！
在下感到如此幸運，艦長，您並未預先思慮，帶著一打空箱體來到此處。
謝謝您！ 謝謝您！ 謝謝您！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
哈哈，是的！ 是的！ 是的！ 是的！ 是的！ 是的！
絕妙的交易，艦長。 極佳的議價…… 對在下而言！
呵呵呵！ 當在下提議給您所能承載的全部燃料時，您本可將在下所有的一滴不剩耗盡。
當在下看著手下工人開始轉運時，冷汗自掌心滴落。
然後就結束了…… 如此之快！ 光榮地如此之快！
在下至少會被升整整三級！ 全新辦公室！ 福利方案！
幸運今日對在下微笑！
在下感到如此僥倖，艦長，您並未預先思考，帶著十來個空箱體來到此處。
感謝您！ 感謝您！ 感謝您！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---

### #100 · `OUT_TAKES` · 🟡 微調（等價）

**英文原文**:
```
I hope you know that contract negotiations are going to be very rough
for my role in the sequel... yes, rough indeed. To begin with
I want ten percent of the royalties, creative control over my dialog
and a fat cut of the toy licenses.
What!? What did you say?! The sequel is going to be all about ME?
How wonderful! What an honor! What a great chance to move up the ladder towards
PRODUCER!
Forget everything I said about license fees!
It's an honor just to work with you!
```

**Shipped v0.3**:
```
我希望您明白，為我在續集中的角色
合約談判將會非常艱難… 是的，確實艱難。 開始就是
我要百分之十版稅、對我對白的創意控制
以及玩具授權的豐厚分成。
什麼？！ 您說什麼？！ 續集要以我為主角？
多麼美妙！ 何等榮譽！ 多好的機會可以往上爬到
製作人！
剛才我說的授權費全都算了！
光是能與您共事就是榮譽！
```

**Rebuild v3**（已通過階段 2.5 自審）:
```
我希望您明白，續集裡我角色的合約談判
將會非常艱難…… 是的，確實艱難。 首先
我要百分之十的版稅、對我台詞的創意主控權
以及玩具授權費的豐厚分紅。
什麼？！ 您說什麼？！ 續集要以我為主角？
多麼美妙！ 何等榮耀！ 多好的機會可以往上爬到
製片！
方才我說的授權費就全部作罷！
光是能與您共事，就是我的榮幸！
```

**推薦**: A (shipped) — 微調等價，shipped 已可接受

**你的選擇**: A / B / C(自訂)

---
