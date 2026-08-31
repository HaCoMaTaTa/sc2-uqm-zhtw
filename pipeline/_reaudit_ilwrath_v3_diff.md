# Ilwrath Rebuild-Compare Diff Report (2026-08-17)

**Race**: `蛛狂族` Ilwrath · **Tokens**: 109 · **v0.7 dossier-based clean-room**

## 統計
- 🟢 完全相同: 0 (0.0%)
- 🟡 微調 (等價): 14 (12.8%)
- 🟠 措辭改變: 82 (75.2%)
- 🔴 語意/voice 差異大: 7 (6.4%)
- ✨ canonical 升級: 6 (5.5%)

## Q&A 決策速覽（本次 clean-room 依據）
- Q1=A 我等 default (廢除「本族蛛狂」)
- Q2=B 廢除儀式化尊稱點綴
- Q3=C Hu-Man 混用: 人族(中性) + 肉肉人類(mocking) + dossier canonical(招牌辱罵)
- Q4=A dossier §四 貶稱 palette 全採
- Q5=A shipped pun canonical 保留 (崇艦/窩等/驢/蒔蘿鼠)
- Q6=A AIEE! canonical 升級 (嘶咿——→啊咿——)
- Q7=C 邪神 CAPS 廣播 icon = 【】 括號 (10 tokens)
- Q8=A 保留少量儀式化中文宗教句式 (以…之名/奉…之令)
- Q9=B shipped 珠貝獸/葛拉獸 保留
- Q10=A shipped 招牌儀式名全保留 (千嚎大典/吞食儀典/苦難廳堂/拷刑者艦/黑暗披風/復仇者星艦…)
- Q11=A 玩家 response 情境切換 (我方/我/老子/你/你們)
- Q12=A 齊整化「、」分隔句大幅使用
- Q13=B 儀式化動詞適度使用
- Q14=A 44 號頻道 (廢 shipped「第 44 頻道」)
- Q15=A 招牌辱罵直譯
- Q16=A 3 partials × ~36 tokens

## 全局清理（跨 tokens）
| 項目 | shipped | v3 | 動作 |
|---|---|---|---|
| 文言助詞 | 汝 117 · 爾 2 · 汝等 14 · 之 73 · 乃 7 · 哉 6 · 爾等 2 (≈221) | 0 · 0 · 0 · 44(idiom) · 0 · 0 · 0 | ✅ 全清 |
| AIEE! canonical | 嘶咿——！（AIEE!） × 3-4 | 啊咿——！（AIEE!） × 3 | ✨ Q6=A 升級 |
| Channel 44 | 第 44 頻道 × 3 | 44 號頻道 × 6 | ✨ Q14=A 升級 |
| Hu-Man 貶稱 | 肉肉人類 × 22 | 肉肉人類 × 20 + 人族 × 22 | 🟠 Q3=C 混用政策 |
| 稱訪客 | 軟塌塌人類/瘦皮囊/地球獸 | 微弱的哺乳動物/血肉之袋/軟趴趴的地球人/軟嫩的人族/醬狀骨頭袋人族 | 🟠 Q4=A dossier canonical |
| Blasphemer | 褻瀆者/騙子 | 瀆神者/騙子 | ✨ Q4=A canonical |
| 邪神 CAPS 廣播 icon | 無 icon (純文字) | 【…】括號 × 10 tokens | 🟠 Q7=C 招牌 icon |
| 齊整化「、」分隔 | 28 處 | 500+ 處 | 🟠 Q12=A 大幅使用 |
| Ilwrath 主自稱 | 我等 (多)/本族蛛狂 × 5 (D0 注入)/本艦 × 4 | 我等 (192)/我等蛛狂族 | 🟠 Q1=A 統一去除 D0 過度指令式 |

## 差異項（🟡🟠🔴✨ 逐 token · 不列 🟢）

### #1 · `NEVER_ENOUGH` · 🟠 wenyan + rewording (2→0)

**English**:
```
We Can Never Receive Sufficient Direction From You, Great Masters!
We Eagerly Await Your Next Vile Commandments.
```

**Shipped v0.4**:
```
偉大主神啊！ 我等永遠無法自汝等聞盡指引！
我等熱切等候汝等下一道邪惡誡命。
```

**Rebuild v3**:
```
偉大的主宰！ 我等永無饜足、承受您們的指引！
我等殷切等候、您們下一道邪惡誡命。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #2 · `OK_WARSHIP` · 🟠 wenyan + rewording (1→0)

**English**:
```
As You Wish, Glorious, Unmerciful Destructors!
In All Future Warship We Will Honor You In This Way!
```

**Shipped v0.4**:
```
遵命，光榮無情的毀滅者！
從今日起我等所有的 崇艦（WARSHIP） 都以此榮耀汝等！
```

**Rebuild v3**:
```
遵命、光榮的、無情的毀滅者！
今後我等一切崇艦（WARSHIP）、皆將以此榮耀您們！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #3 · `OK_DWE` · 🟠 rewording (sim=0.87)

**English**:
```
Yes, Great Dogar! Yes Mighty Kazon! Dwe Certainly Will, Dwe Certainly Will!
```

**Shipped v0.4**:
```
是的，偉大的多加！ 是的，雄壯的卡宗！ 窩等（DWE）必定照辦，窩等必定照辦！
```

**Rebuild v3**:
```
是也、偉大的多加！ 是也、雄壯的卡宗！ 窩等（DWE）必定照辦、窩等必定照辦！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #4 · `OK_YOUBOO` · 🟠 rewording (sim=0.82)

**English**:
```
It Shall Be So, Great Ones.
Yuubuu Are Mighty!
Yuubuu Are The Most Hideous And Deceitful!
We Ilwrath Are Too Fortunate To Have Yuubuu To Worship!
```

**Shipped v0.4**:
```
遵命，偉大者。
驢（YUUBUU）雄壯無敵！
驢是最可怖、最狡詐的！
我等蛛狂族何其有幸能崇奉驢！
```

**Rebuild v3**:
```
必當如此、偉大者。
驢（YUUBUU）雄壯無敵！
驢是最為可憎又狡詐者！
我等蛛狂何其有幸、能崇奉驢！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #5 · `OK_DILRAT` · 🔴 semantic/voice divergence (sim=0.35)

**English**:
```
We, The Dill-Rats, Bow And Scrape Off Our Appendages In Your Honor, Mighty Dogar And Kazon!
```

**Shipped v0.4**:
```
我等，蒔蘿鼠，向兩位偉大的多加與卡宗屈膝叩首，剝下自身附肢以示尊崇！
```

**Rebuild v3**:
```
我等、蒔蘿鼠、屈膝叩首、剝下自身附肢、以榮耀您們、雄壯的多加與卡宗！
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #6 · `BIG_FUN` · 🟠 wenyan + rewording (1→0)

**English**:
```
Listen!
Once More The Terrible Twosome Are Among Us!
Hear Our Thanks, Mighty Dogar And Kazon!
We Have Found Ultimate Pleasure In Your Cruel Service In These Alien Stars!
Though Our Enemy, The Thraddash, Possess A Tough And Chewy Exterior
Inside These Creatures Can Be Found A Most Smooth And Sweet Set Of Innards.
Their Low Bellows Of Fear And Agony Do Service To Your Names, Great Dogar And Kazon!
We Will Slay These Beasts In Your Name, Until They Are All Dead, Dead, DEAD!
```

**Shipped v0.4**:
```
聽哉！
可怖雙煞再次降臨我等之中！
聞我等謝恩，偉大的多加與卡宗！
我等在您殘酷差遣下於異星尋得無上之樂！
雖然仇敵撻伐族外皮堅韌又嚼勁十足
其內臟卻是至為滑順甘美之物。
他們低沉的恐懼與痛苦哀嚎正為您聖名奉獻，偉大的多加與卡宗！
我等將以您聖名屠盡這些畜生，直到他們死絕、死絕、死絕！
```

**Rebuild v3**:
```
傾聽！
可怖雙煞、再次降臨我等之中！
聞我等謝恩、雄壯的多加與卡宗！
我等於異星、在您殘酷的差遣中、尋得無上之樂！
我等的敵人、撻伐族、外皮雖韌且嚼勁十足
其內臟卻是至為滑順甘美之物。
他們低沉的恐懼與痛苦哀嚎、正奉獻於您聖名、偉大的多加與卡宗！
我等將以您聖名、屠盡這些畜生、直到他們死絕、死絕、死絕！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #7 · `FAST_AS_CAN` · ✨ canonical upgrade

**English**:
```
Our Gods Of Darkness And Pain Call To Us Again!
Evil Dogar, Cruel Kazon! How Can We Be So Fortunate To Hear From You Again?
We Pray Thee Gods, Forgive Us For Not Yet Beginning The Slaying Of The Thraddash.
Quickly Now, I Must Rend Three Limbs From My Thorax As A Sign Of My Supplication.
AIEE!
It Is Done! Dogar And Kazon See My Fluids And Must Smile. I Am Happy!
We Make All Haste, But Are Limited By The Speed Of Our Avenger Starcraft.
We Know Our Pitiful Excuses Are Worthless...
We Must Show Our Shame With The Removal Of Yet More Limbs.
AIEE!
```

**Shipped v0.4**:
```
我等黑暗與痛楚之神再次呼喚我等！
邪惡的多加，殘酷的卡宗！ 我等何其有幸再次聞您話語？
祈禱眾神原諒我等尚未開始屠戮撻伐族。
速速，我必自胸節扯下三根附肢以示懇求。
嘶咿——！（AIEE!）
完成了！ 多加與卡宗見我體液必展笑顏。 我心欣慰！
我等已全速前進，但受我等復仇者星艦速度所限。
我等知曉可悲的藉口毫無價值……
必須再扯下更多附肢以彰羞愧。
嘶咿——！
```

**Rebuild v3**:
```
我等黑暗與痛楚的眾神、再次向我等呼喚！
邪惡的多加、殘酷的卡宗！ 我等何其有幸、能再次聞您話語？
懇祈眾神原諒、我等尚未開始屠戮撻伐族。
即刻、我必自胸節扯下三根附肢、以示懇求之意。
啊咿——！（AIEE!）
完成了！ 多加與卡宗見我體液、必展笑顏。 我心歡愉！
我等已全速前進、但受我等復仇者星艦速度所限。
我等知曉、可悲的藉口毫無價值……
必須再扯下更多附肢、以彰羞愧。
啊咿——！
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #8 · `GLORIOUS_WORSHIP` · 🟡 micro wenyan cleanup (1→0, sim=0.92)

**English**:
```
Attend! The Cruel Twins Of Pain And Death Have Returned To Instruct Us!
Dogar And Kazon! We Are Your Instruments Of Cruelty And Death!
As We Speak, Our Holy Excruciators Attack The Thraddash, Slaying Unmercifully In Your Names.
```

**Shipped v0.4**:
```
聽命！ 痛楚與死亡的殘酷雙生子再次降臨教導我等！
多加與卡宗！ 我等乃您殘忍與死亡的器具！
此刻，我等神聖拷刑者艦正攻擊撻伐族，以您聖名無情屠殺。
```

**Rebuild v3**:
```
恭聽！ 痛楚與死亡的殘酷雙生子、再次降臨教導我等！
多加與卡宗！ 我等便是您殘忍與死亡的器具！
此刻、我等神聖的拷刑者艦、正攻擊撻伐族、以您聖名無情屠殺。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #9 · `ON_WAY` · ✨ canonical upgrade

**English**:
```
Dogar And Kazon Once More Grace Channel 44 With Their Inspiring Words Of Hatred And Cruelty!
Acolyte! Turn The Volume To Maximum Immediately!
Hear Us, Black Dogar! Hear Us, Bloody Kazon!
We Have Heard Your Word And Devote Every Breath To Fulfilling Your Desire For Gratuitous Violence And Death!
As We Speak, A Thousand Starships, Cloaked And Invisible, Make Passage To The <% comm.getConstellation("Draconis", "thraddash") %> Stars.
Upon Arrival There, The Holy Killing Team Will Begin The Bloody Slaughter You Requested.
```

**Shipped v0.4**:
```
多加與卡宗再次以憎恨與殘忍的鼓舞話語降臨第 44 頻道！
侍徒！ 立刻把音量開到最大！
聽我等哉，黑暗多加！ 聞我等哉，血腥卡宗！
我等已聽見您的話語，將以每一口氣去滿足您對無端暴力與死亡的渴望！
此刻，一千艘星艦，隱形不可見，正航向 <% comm.getConstellation("天龍座", "thraddash") %>（Draconis）星系。
抵達後，神聖屠戮團將展開您所要求的血腥屠殺。
```

**Rebuild v3**:
```
多加與卡宗、再以憎恨與殘忍的鼓舞話語、蒞臨 44 號頻道！
侍徒！ 立刻將音量開到極致！
請聽我等、黑暗的多加！ 請聽我等、血腥的卡宗！
我等已聽見您的話語、將以每一口氣、去滿足您對無端暴力與死亡的渴望！
此刻、一千艘星艦、隱於黑暗披風、悄然航向 <% comm.getConstellation("天龍座", "thraddash") %>（Draconis）星系。
抵達之後、神聖屠戮團、將展開您所要求的血腥屠殺。
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #10 · `GODS_RETURN_1` · 🟡 micro adjust (sim=0.92)

**English**:
```
Dogar! Kazon! We Hear Your Summons And Slaughter The Fat Jubby In Greeting.
```

**Shipped v0.4**:
```
多加！ 卡宗！ 我等聽聞您召喚，屠肥碩珠貝獸為問候。
```

**Rebuild v3**:
```
多加！ 卡宗！ 我等聞您召喚、屠肥碩珠貝獸以為問候。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #11 · `GODS_RETURN_2` · 🟠 rewording (sim=0.74)

**English**:
```
From The Black Pits Of Pain The Deific Duo Of Destruction Emerge Once More!
```

**Shipped v0.4**:
```
自痛楚的黑淵，毀滅神聖雙煞再度顯現！
```

**Rebuild v3**:
```
自痛楚的黑淵、毀滅的至尊雙神、再度顯現！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #12 · `GODS_RETURN_3` · 🟠 rewording (sim=0.88)

**English**:
```
Our Gods Have Returned Once More, Just As Foretold By This Morning's Rituals!
When We Pulled The Steaming Entrails From The Squirming Sacrifice
and Flung The Fatty Loops Against The Walls Of Our Holy Chambers
the Entrails Stuck Tight, Neither Sliding Nor Peeling Even A Little Bit!
Thus Was Our Gods' Arrival Foretold!
```

**Shipped v0.4**:
```
我等眾神再次歸來，恰如今晨儀典所預示！
當我等自蠕動的祭品身上扯出蒸騰內臟
並將油膩腸圈甩向神聖廳堂之牆時
那些內臟緊緊黏住，不滑不脫，絲毫未動！
這便是我等眾神歸來的預兆！
```

**Rebuild v3**:
```
我等眾神、再度歸來、正如今晨儀典所預示！
當我等自蠕動的祭品身上、扯出蒸騰的內臟
並將油膩的腸圈、甩向神聖廳堂的牆
那些內臟緊緊黏住、不滑不脫、絲毫未動！
如此、便是我等眾神歸來的預兆！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #13 · `JUST_GRUNTS` · ✨ canonical upgrade

**English**:
```
What Is That? The Voices Of Our Gods Dogar And Kazon? Surely It Cannot Be!
And Yet My Set Is Tuned To The Mystic 44 -- Who Else Could It Be?
I Am Unworthy Of Such Attention As This!
Dogar -- Kazon! Your Divine Words Will Surely Consume Me.
I Beseech Thee! Speak Directly To The Leaders At Homeworld!
I Am Unworthy.
```

**Shipped v0.4**:
```
何物？ 我等眾神多加與卡宗之聲？ 絕不可能！
然而我的接收器正調在神秘的第 44 頻道 —— 除他們外還會是誰？
我不配受此關注！
多加 —— 卡宗！ 您的神聖話語必將吞噬我。
我懇求汝等！ 請直接向母星的領袖啟示！
我不配。
```

**Rebuild v3**:
```
何物？ 是我等眾神多加與卡宗的聲音？ 絕不可能！
然而我的接收器、正調於神秘的 44 號頻道——除他們外、還會是誰？
我不配、承受如此關注！
多加——卡宗！ 您的神聖話語、必將吞噬我。
我懇求您們！ 請直接向母星的領袖啟示！
我不配。
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #14 · `GRUNTS_AGAIN` · 🟡 micro wenyan cleanup (1→0, sim=0.90)

**English**:
```
Hark! We Are Receiving A Holy Transmission.
Oh Dark And Gruesome Masters! I Am Honored With Your Attention.
But Great Gods, I Am But A Simple Ilwrath, A Humble Murderer.
I Am Unworthy To Hear Your Words!
Only At Our Homeworld Orbiting The <% comm.getColor("Green", "ilwrath") %> Eye Of Dogar Are There Ilwrath Sufficiently Evil
to Understand Your Commandments. Forgive Me!
```

**Shipped v0.4**:
```
聽哉！ 我等正接收神聖傳訊。
喔，黑暗恐怖的主宰！ 我以您關注為榮。
但偉大眾神，我不過是個平凡的蛛狂，一個卑微的殺手。
我不配聞您的話語！
只有在我等繞著多加之 <% comm.getColor("綠色", "ilwrath") %> 綠眼運行的母星上
才有邪惡程度足以理解您誡命的蛛狂族。 請恕我！
```

**Rebuild v3**:
```
傾聽！ 我等正接收神聖傳訊。
喔、黑暗又可怖的主宰！ 我以承蒙您關注為榮。
但偉大眾神、我不過是個平凡的蛛狂、一名卑微的謀殺者。
我不配、聞您的話語！
唯有在我等母星、繞著多加之 <% comm.getColor("綠色", "ilwrath") %> 綠眼運行之處
才有邪惡程度、足以理解您誡命的蛛狂族。 請恕我！
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #15 · `WHAT_ORDERS` · 🟠 rewording (sim=0.70)

**English**:
```
Your Will Is Our Inspiration. What Shall We Do?
```

**Shipped v0.4**:
```
您意即是我等靈感。 我等該做什麼？
```

**Rebuild v3**:
```
您的意志、即是我等靈感。 我等當作何事？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #16 · `WE_WORSHIP_1` · 🟠 rewording (sim=0.81)

**English**:
```
From The Chambers Of Pain We Hear Your Words, Cruel And Evil Lords Of Darkness.
And As Your Voice Crackles Out Of The Speaker Boxes, It Sends Thrills Across Our Carapaces.
Our Hairy Quills All Stand Erect And We Pant And Wheeze With Holy Fervor!
Oh Mighty Gods! You Are The Definition Of All That Is Evil And Hideous In This Universe!
You Are The Inspiration For All Cruelty, Deception And Pain.
For This We Thank You!
```

**Shipped v0.4**:
```
自苦難廳堂我等聞您話語，殘酷邪惡的黑暗之王。
當您的話語自傳音之匣迸出，我等甲殼為之顫慄。
我等毛絨鬃刺齊齊豎起，喘息喘鳴著神聖狂熱！
喔，偉大眾神！ 您是這宇宙一切邪惡與可憎的定義！
您是一切殘酷、欺瞞與痛楚的源頭。
為此我等感謝您！
```

**Rebuild v3**:
```
自苦難廳堂、我等聞您話語、殘酷邪惡的黑暗之王。
您的聲音自傳音之匣迸出時、我等的甲殼因此顫慄。
我等的毛絨鬃刺、齊齊豎起、我等以神聖狂熱、喘息不已！
喔、雄壯的眾神！ 您們、即是這宇宙一切邪惡與可憎的定義！
您們、是一切殘酷、欺瞞與痛楚的源頭。
為此、我等感謝您們！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #17 · `WE_WORSHIP_2` · 🟠 rewording (sim=0.82)

**English**:
```
We Shall Make Instant Obeisance, Divine Lords Of Darkness!
Acolyte! Light The Candles Of Torment -- Quickly!
No You Idiot! Not The White Ones...
Use The Yellow And Red Ones We Made From The Prisoners Last Week, The Ones With The Lumps. Yes, Yes!
No Fool, Not Those! They Are Still Wet!
```

**Shipped v0.4**:
```
我等當立即恭敬叩首，黑暗神聖之王！
侍徒！ 點燃苦刑燭台 —— 快！
不對你這蠢貨！ 不是白的那些……
用上週從囚犯身上做的黃紅相間的那些，那些有腫塊的。 對，對！
不行笨蛋，不是那些！ 那些還沒乾！
```

**Rebuild v3**:
```
我等當立即恭敬叩首、神聖的黑暗之王！
侍徒！ 點燃苦刑燭台——即刻！
不對、你這蠢貨！ 不是那些白的……
用上週由囚犯身上做的、那些黃紅相間的、有腫塊的那些。 對、對！
不、笨蛋、不是那些！ 那些還沒乾！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #18 · `WE_WORSHIP_3` · 🟠 wenyan cleanup (3→0)

**English**:
```
Oh Evil Dogar!
Oh Hideous Kazon!
We Shall Toss The Fat Jubbies Into The Pit Of A Thousand Needles!
This We Shall Do In Your Names!
We Shall Bring Forth The Last Remaining Hu-Man Prisoner
And Pull Its Head Apart Slowly, So That Its Cries Last For Hours.
This We Shall Do In Your Names!
We Shall Torment, Terrorize, Maim And Kill, Again, And Again, And AGAIN!
This We Shall Do In Your Names!
```

**Shipped v0.4**:
```
喔，邪惡的多加！
喔，可憎的卡宗！
我等將把肥碩珠貝獸投入千針之坑！
以汝聖名而為！
我等將把最後一名人類囚犯拖出
慢慢扯裂他的頭，讓他的慘叫持續數小時。
以汝聖名而為！
我等將施刑、恫嚇、致殘、屠殺，再再又再！
以汝聖名而為！
```

**Rebuild v3**:
```
喔、邪惡的多加！
喔、可憎的卡宗！
我等將把肥碩珠貝獸、投入千針之坑！
以您聖名而為！
我等將把最後一名人族囚犯拖出
慢慢扯裂他的頭、讓他的慘叫、持續數小時。
以您聖名而為！
我等將施刑、恫嚇、致殘、屠殺、再、再、又再！
以您聖名而為！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #19 · `SUBSEQUENT_CHMMR_HELLO` · 🟠 wenyan + rewording (2→0)

**English**:
```
So... The Hu-Man Has Returned To Visit Its Entombed Mentors Of Deceit!
I Am Emotionally Moved By This Poignant Moment, And Feel Compelled To Make Immediate Obeisance.
Flaccid Earthling -- I Will Pour Your Warm Circulatory Fluid Across The Altar Of Dogar
And Dance A Jig Of Cruelty Atop Your Cooling Corpse.
```

**Shipped v0.4**:
```
如此……肉肉人類回來造訪其被封印的欺騙導師！
此感人時刻令我情感激盪，不得不立即致敬。
軟塌塌的地球人 —— 我將把汝溫熱的循環液潑灑於多加祭壇之上
並於汝冷卻屍身之上跳一段殘酷之舞。
```

**Rebuild v3**:
```
如此……肉肉人類、回來造訪它那些被囚禁的欺瞞導師了！
此感人時刻令我情緒激盪、不由得必須立刻致敬。
軟趴趴的地球人——我將把你溫熱的循環液、潑灑於多加的祭壇之上
並於你冷卻的屍身之上、跳一段殘暴的舞蹈。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #20 · `INIT_CHMMR_HELLO` · 🟠 wenyan cleanup (4→0)

**English**:
```
Caught You, Didn't I?
We Have Monitored Your Visit To This World With Great Interest.
Your Plans For Trickery Are Pitiful
And Make Dogar And Kazon Clack Their Mandibles Against One Another And Snicker With Amusement.
And So Now, Squishy Hu-Man
I Wonder What Sort Of Noise You Will Make
When I Pull Off Your Arms?
A High And Wailing Scream, Or A Low Moan Of Ultimate Suffering?
```

**Shipped v0.4**:
```
被我逮到了，是不是？
我等以極大興趣監視汝造訪此世界。
汝那可悲的欺瞞計畫
讓多加與卡宗顎肢相擊、竊笑不已。
那麼現在，軟嫩的肉肉人類
我在想，當我把汝的雙臂扯下時
汝會發出何種聲響？
是高亢淒厲的尖叫，還是極致痛苦的低吟呢？
```

**Rebuild v3**:
```
被我逮到了、是不是？
我等已以極大興趣、監視你造訪此世界。
你那可悲的欺瞞計畫
令多加與卡宗顎肢相擊、竊笑不已。
於是現在、軟嫩的人族
我在想、當我扯下你的雙臂之時
你會發出何種聲響？
是高亢淒厲的尖叫、還是極致痛苦的低吟呢？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #21 · `OK_ENOUGH_ILWRATH` · 🟠 wenyan + rewording (1→0)

**English**:
```
And Yet You Know So Little.
```

**Shipped v0.4**:
```
然而汝所知甚少。
```

**Rebuild v3**:
```
然而你所知、甚為稀少。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #22 · `OK_ENOUGH_GODS` · 🟠 wenyan + rewording (2→0)

**English**:
```
Your Pitiful Investigations Have Barely Scratched The Surface Of What Is To Be Learned
About Dogar And Kazon.
And Remember, You May Never Get Another Chance To Ask Such Questions.
```

**Shipped v0.4**:
```
汝那可悲的調查僅觸及
多加與卡宗一切奧秘的皮毛。
且要記住，汝可能再無機會提出這類問題。
```

**Rebuild v3**:
```
你那可悲的調查、僅觸及了關於多加與卡宗
一切奧秘的皮毛。
且謹記、你再無機會、提出這類問題。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #23 · `SEND_MESSAGE` · 🟠 wenyan + rewording (2→0)

**English**:
```
By The Fetid Breath Of The Dark Twin, Kazon!
A Hu-Man In An Alien Starship... How Fascinating!
When I Intercepted That Ur-Quan Drone, And Learned That An Unidentified Starship Had Approached Earth,
I Never Expected To Find Such A Remarkable Vehicle In The Hands Of A Hu-Man.
Hu-Mans Are Prey Animals - Weak And Helpless-
But Here Is A Hu-Man In An Armed Starship!
And Therefore In Direct Violation Of The Oath Of Fealty.
I Am Sure Our Masters, The Ur-Quan, Will Punish Earth Most Severely For This Treachery....
When I Present Them With The Twisted Wreckage Of Your Ship And Your Many Charred Corpses.
```

**Shipped v0.4**:
```
以黑暗雙煞卡宗腐臭之氣息為誓！
異星艦上的肉肉人類…… 何等迷人！
當我截獲那烏寬族探測機，得知有身分不明的星艦接近地球時
我從未想過會在肉肉人類手中發現如此非凡的載具。
肉肉人類是獵物 —— 軟弱又無助 ——
但這裡竟有一位肉肉人類駕著武裝星艦！
這已直接違反效忠誓約。
我確信我等主人，烏寬族，將為此背叛嚴懲地球……
當我把汝艦的扭曲殘骸與汝眾焦黑屍體呈到他們面前時。
```

**Rebuild v3**:
```
以黑暗雙生子、卡宗腐臭之氣息為誓！
異星艦上、竟有一個人族……何等迷人！
當我截獲那烏寬族探測機、得知有身分不明的星艦已接近地球
我從未預料、會在人族手中、發現如此非凡的載具。
人族、是獵物——軟弱又無助——
然而此處竟有人族、駕著武裝星艦！
此舉、已直接違反效忠誓約。
我確信、我等主人、烏寬族、必為此背叛、嚴懲地球……
當我將你艦的扭曲殘骸、與你眾焦黑的屍體、呈至他們面前之時。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #24 · `CAME_FROM` · 🟠 wenyan cleanup (3→0)

**English**:
```
Since You Will Soon Be Dead, I Will Gladly Explain.
We Have Spent Many Years Gleefully Preying On The Pkunk.
They Are A Pitiful, Easily-killed Species
And We Would Have Continued In This Divine Worship Of Dogar And Kazon
But We Required Additional Crew Members And Repairs To Our Cloaking Device.
So We Departed The <% comm.getConstellation("Giclas", "pkunk") %> Constellation And Set Course For Home.
But Before We Had Reached Our Region Of Space, We Detected The Passage Of A Nearby Vessel - The Ur-Quan Drone.
It Informed Us About You... So Here We Are.
And Now, YOU DIE!
```

**Shipped v0.4**:
```
既然汝很快就會死，我倒是樂於解釋。
我等已多年愉悅地獵殺普恩族。
他們是可悲、易屠的物種
我等本可繼續這場對多加與卡宗的神聖崇拜
但我等需要補充船員並修復我等黑暗披風。
因此我等離開 <% comm.getConstellation("吉克拉斯", "pkunk") %>（Giclas）星域，設定歸返航向。
但抵達我等星域前，我等偵測到附近船艦通過 —— 烏寬族探測機。
它向我等通報了汝的存在…… 於是我等來到此處。
現在，汝就受死吧！
```

**Rebuild v3**:
```
既然你很快便將赴死、我便樂於解釋。
我等、多年以來、於普恩族之上、施行歡愉之獵殺。
他們、是可悲、易被屠戮的族類
我等本可繼續這場對多加與卡宗的神聖崇拜
然而我等需要補充船員、並修復我等的黑暗披風。
故我等離開 <% comm.getConstellation("吉克拉斯", "pkunk") %>（Giclas）星系、設定歸返航向。
然而、抵達我等星域之前、我等偵測到附近船艦通過——烏寬族探測機。
它向我等通報了你的存在……故我等前來此處。
如今、你、必死！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #25 · `WHO_BLASTS_WHO` · 🟠 wenyan cleanup + rewording (3→0, sim=0.65)

**English**:
```
I Have No Fear Of You, Feeble Mammal.
Though My Ship Lacks A Functioning Cloaking Device, And Many Of Our Crew Are Dead,
My Gods, Dogar The Black And Kazon The Unseen, Have Personally Confided To Me
That They Despise You Hu-Mans, And That They Will Help Us To Kill You All!
```

**Shipped v0.4**:
```
我對汝毫無畏懼，孱弱的哺乳動物。
雖然本艦黑暗披風失靈，本艦船員多已陣亡
我等眾神，黑暗的多加與不可見的卡宗，親口向我吐露
他們鄙視汝等肉肉人類，並將協助我等屠盡汝等！
```

**Rebuild v3**:
```
我對你、毫無畏懼、微弱的哺乳動物。
雖然本艦的黑暗披風已失靈、我等眾多船員亦已陣亡
我等眾神、黑色的多加與無形的卡宗、已親自向我告知——
他們厭惡你們人族、且將助我等、屠盡你們！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #26 · `NO_SURRENDER` · 🟠 wenyan cleanup (3→0)

**English**:
```
Fool!
As Alien As Your Ship May Be, Our Sensors Reveal How Few Weapons You Have On Board.
Though This Vessel Is Under-Crewed, And Our Cloak Of Darkness Is Non-Functional,
We Still Have More Than Enough Power To Kill You All!
```

**Shipped v0.4**:
```
蠢貨！
即便汝艦再異星，我等感應器已偵知汝艦上武器何等稀少。
雖然本艦人員不足，本艦黑暗披風失靈
我等火力仍綽綽有餘足以屠盡汝等！
```

**Rebuild v3**:
```
蠢貨！
無論你艦如何異星、我等的感應器已揭露、你艦上武器何等稀少。
雖然本艦人員不足、我等的黑暗披風亦已失靈
我等的火力仍綽綽有餘、足以屠盡你們！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #27 · `NOT_REASONABLE` · 🟠 wenyan + rewording (2→0)

**English**:
```
Ha-ha-ha-ha! You Must Be Either A Naive Child Or A Hopeless Fool.
In Either Case, It Makes No Difference, Because Soon You Will Be DEAD!
```

**Shipped v0.4**:
```
哈哈哈哈！ 汝要不是天真孩童，就是絕望的傻瓜。
無論何者，都毫無分別，因為汝很快就會死！
```

**Rebuild v3**:
```
哈-哈-哈-哈！ 你要不就是天真的孩童、要不就是絕望的傻瓜。
無論何者、皆無分別、因為你很快便將——死！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #28 · `SUBSEQUENT_HOME_HELLO` · 🟠 wenyan cleanup (5→0)

**English**:
```
I See That You Have Come To Your Senses
And Are Now Prepared To Engage In The Festival Of A Thousand Screams.
Although Your Initial Rejection Of The Honor Was Dismaying,
We Realize That It May Have Been A Shock To Be So Privileged.
Ha Ha, Pinch Yourself, Hu-Man! You Are Not Dreaming.
Dogar Has Winked And Kazon Has Spasmed In Condescending Approval.
Today, Hu-Man, Is Your Lucky Day!
```

**Shipped v0.4**:
```
我看汝已恢復理智
如今準備參與千嚎大典。
雖然汝先前拒絕此榮譽令我等失望
我等明白這對汝可能是意外殊榮的震撼。
哈哈，捏捏自己吧，肉肉人類！ 汝不是在做夢。
多加眨眼，卡宗抽搐，皆是屈尊贊同的表示。
今日，肉肉人類，是汝的幸運日！
```

**Rebuild v3**:
```
我看你已恢復了理智
如今準備參與千嚎大典。
雖然你起初拒絕此榮譽、令我等失望
我等明白、如此殊榮、對你或許是意外的震撼。
哈哈、捏捏自己吧、肉肉人類！ 你並非在做夢。
多加眨了眼、卡宗抽了搐、皆是屈尊贊同的表示。
今日、肉肉人類、便是你的幸運之日！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #29 · `GENERAL_INFO` · 🟠 wenyan cleanup (4→0)

**English**:
```
Though Such Information Is Normally Holy And Secret,
I Find I Am Unable To Contain Myself. Know This Fact
You Are Hu-Man, Weak And Alone In This Universe With No Gods To Protect You.
I Know This, Because The Only True Gods Are Our Own Ilwrath Deities, Dogar And Kazon!
Dogar Is The Killer In A Black Cloak...
The Great Destroyer...
The Bloody-Clawed Murderer...
The Dark Beast With A Thousand Young!
Kazon, On The Other Claw, Is The Great Deceiver...
The Malevolent Evil In The Darkness...
The Unstoppable Monster Who Has No Pity...
The Hungry Lurker In The Night.
These Are Our Gods -- The ONLY Gods!
How Do We Know, You Ask? Because Dogar And Kazon TOLD US So.
```

**Shipped v0.4**:
```
雖然此類資訊通常神聖而秘密
我發覺自己抑制不住。 銘記此事實
汝是肉肉人類，軟弱、孤獨於此宇宙，無神保護。
我知此事，因為唯一的真神就是我等蛛狂族之神，多加與卡宗！
多加乃身披黑袍的殺手……
偉大的毀滅者……
血爪的謀殺者……
擁有千名幼子的黑暗野獸！
卡宗，另一爪，乃偉大的欺騙者……
黑暗中的邪惡……
無情無憐的無敵怪物……
夜中飢餓的潛伏者。
這些就是我等眾神 —— 唯一的神！
汝問我等如何得知？ 因為多加與卡宗親口告訴我等。
```

**Rebuild v3**:
```
雖然此類資訊、通常神聖而秘密
我覺自己抑制不住。 請銘記此事實
你是人族、於此宇宙中軟弱又孤單、無神庇護。
我知此事、因為唯一的真神、便是我等蛛狂族的神、多加與卡宗！
多加、是身披黑袍的殺手……
偉大的毀滅者……
爪上帶血的謀殺者……
擁有千名幼子的黑暗野獸！
卡宗、另一爪、則是偉大的欺瞞者……
黑暗中的邪惡……
無情無憐的無敵怪物……
夜中飢餓的潛伏者。
這些便是我等眾神——唯一的神！
你問我等如何得知？ 因為多加與卡宗、親口告訴了我等。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #30 · `GOODBYE_AND_DIE` · 🟠 wenyan cleanup (3→0)

**English**:
```
Not So Fast, Tender Hu-Man! You Must First Pay Homage To The Universal Deities Dogar And Kazon!
The Payment Is Simple And Within Your Means.
You Will Pay With Your Lives!
```

**Shipped v0.4**:
```
別急，稚嫩的肉肉人類！ 汝必先向宇宙神明多加與卡宗致敬！
貢禮簡單且在汝能力所及。
汝要以自己的性命作為貢品！
```

**Rebuild v3**:
```
別急、軟嫩的人族！ 你必先向宇宙神明、多加與卡宗致敬！
貢禮簡單、亦在你能力所及。
你將以自己的性命為貢！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #31 · `DECEIVERS` · 🟠 wenyan cleanup (3→0)

**English**:
```
DECEIVERS!
We Know That You Are Not Truly Dogar And Kazon!
Your Foolish And Childlike Attempts To Fool Us Shall Be Your Death!
```

**Shipped v0.4**:
```
騙子！
我等知曉汝並非真正的多加與卡宗！
汝這愚蠢又稚氣的欺瞞企圖將是汝之死！
```

**Rebuild v3**:
```
【騙子！】
我等知曉、你並非真正的多加與卡宗！
你這愚蠢又稚氣的欺瞞企圖、將是你的死因！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #32 · `NO_PEACE` · 🟠 wenyan + rewording (1→0)

**English**:
```
Excellent! We Enjoy The Process Of Rending Life So Much More When The Life Giver Is Willing.
Come Now In Peace And Give That Which Makes You Live!
```

**Shipped v0.4**:
```
太好了！ 我等最愛屠戮生命的過程，尤其當生命之給予者甘願如此時。
來吧，安詳前來，獻上讓汝存活的一切！
```

**Rebuild v3**:
```
好極了！ 生命的給予者甘願如此時、我等更愛屠戮生命的過程。
如今、請安詳前來、獻上讓你存活的一切！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #33 · `NO_ALLIANCE` · 🟠 wenyan cleanup (3→0)

**English**:
```
Silly Earthling! The Ur-Quan, Our Masters, Would Be Displeased If They Were Aware Of Your Transgressions!
By Violating Your Oath Of Fealty To The Ur-Quan, We Are Obligated To Take Your Lives As Payment...
A Process That Will Incidentally Please Both Myself And, More Importantly, The Arch-Deific Duo!
```

**Shipped v0.4**:
```
傻氣的地球人！ 我等主人烏寬族若得知汝的違逆之舉必大為不悅！
汝背棄了對烏寬族的效忠誓約，我等有責取汝性命為償……
此舉不僅令我快意，更能取悅神聖雙煞！
```

**Rebuild v3**:
```
傻氣的地球人！ 我等主人烏寬族、若得知你的違逆之舉、必將大為不悅！
你已背棄了對烏寬族的效忠誓約、我等有責、取你性命以為償……
此舉、恰能令我快意、更能取悅至尊雙神！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #34 · `ILWRATH_BELIEVE` · 🟠 wenyan cleanup (3→0)

**English**:
```
Listen!
It Is The Hideous And Inspiring Voices Of Our Gods, Dogar And Kazon!
Oh Great Gods Of Evil And Darkness, What Can Your Humble And Devious Servants Do For You?
```

**Shipped v0.4**:
```
聽哉！
是我等眾神多加與卡宗可憎又鼓舞人心的聲音！
喔，偉大邪惡與黑暗之神，汝卑微又狡詐的僕從能為汝做什麼？
```

**Rebuild v3**:
```
傾聽！
是我等眾神、多加與卡宗、可憎又鼓舞人心的聲音！
喔、邪惡與黑暗的偉大眾神、您們卑微又狡詐的僕從、可為您們做些什麼？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #35 · `OK_KILL_THRADDASH` · 🟠 wenyan cleanup (3→0)

**English**:
```
Oh Mighty Dogar!
Oh Mighty Kazon!
Your Devoted Servants Hear Your Words And Obey Your Divine And Cruel Insights.
The Pkunk Are Unfit For OUR Sacramental Tortures!
We Relish The Prospect Of Killing Worthy Prey!
We Will Leave Immediately So That We Can Begin Our Glorious, Evil Devotions...
But Who Shall We Prey Upon Next?
Who Shall Suffer Our Inspired Torment?
Hmm.
Didn't Those Loathsome Umgah Once Mention A Race Near Their Region Of Space?
Hmm... YES! I Have It! The THRADDASH!
We Will Go NOW, And Kill All Of Them!
```

**Shipped v0.4**:
```
喔，偉大的多加！
喔，偉大的卡宗！
汝之忠僕聞汝話語，遵從汝神聖殘酷的洞見。
普恩族已不配我等的聖典折磨！
我等渴望屠戮值得的獵物！
我等將立即出發，開始我等光榮邪惡的奉獻……
但我等接下來該獵誰？
誰該受我等靈感啟發的折磨？
嗯。
那些可憎的陰嘎族不是曾提過他們星域附近的一個種族嗎？
嗯……有了！ 撻伐族！
我等將立刻出發，屠盡他們！
```

**Rebuild v3**:
```
喔、雄壯的多加！
喔、雄壯的卡宗！
您們的忠僕、聞您話語、遵您神聖殘酷的洞見。
普恩族、已不配我等的聖典折磨！
我等渴望、屠戮值得的獵物！
我等將立即出發、開始我等光榮的邪惡奉獻……
然而、我等接下來該獵誰？
誰、該受我等靈感啟發的折磨？
嗯。
那些可憎的陰嘎族、不是曾提過他們星域附近的一個種族嗎？
嗯……有了！ 我知道了！ 撻伐族！
我等即刻出發、屠盡他們！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #36 · `GOODBYE_GODS` · 🟠 wenyan + rewording (2→0)

**English**:
```
Farewell Dogar And Kazon. We Are Awed By Your Malevolent Presence, And Swear Unto You
To Commit Even More Vile And Treacherous Deeds Tomorrow Than We Did Today!
```

**Shipped v0.4**:
```
永別了多加與卡宗。 我等敬畏汝之邪惡臨在，並向汝立誓
明日必幹比今日更為卑鄙背叛之惡行！
```

**Rebuild v3**:
```
永別了、多加與卡宗。 我等敬畏您們的邪惡臨在、並向您們立誓
明日必行、比今日更為卑鄙背叛的惡行！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #37 · `INIT_HELLO_SPACE` · 🟠 rewording (sim=0.83)

**English**:
```
What? Can I Believe My Sensory Cluster? I Sense Hu-Mans!
I Dance With Joy For Our Good Fortune.
The Hu-Man Dies With Such Agony That It Cannot Help But Please
Dogar And Kazon.
```

**Shipped v0.4**:
```
何物？ 我可信我的感官叢嗎？ 我感應到肉肉人類！
我為我等好運翩然起舞。
肉肉人類臨死之痛烈，必令
多加與卡宗歡愉。
```

**Rebuild v3**:
```
何物？ 我能相信我的感官叢嗎？ 我感應到人族！
我為我等的好運、翩然起舞。
人族臨死之時、痛苦如此劇烈、必令
多加與卡宗歡愉。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #38 · `SUBSEQUENT_HELLO_SPACE_1` · 🟡 micro wenyan cleanup (1→0, sim=0.86)

**English**:
```
What Is It? Mmmm, Hu-Man! It Has Been So Long Since I Have Seen A Hu-Man Die!
We Will Bet On How Many Parts We Can Remove Before It Stops Making Noise!
Now, You Space-Ship Captain, Begin The Expedient Transfer Of All Hu-Man Crew
So That We May Waste No Time.
```

**Shipped v0.4**:
```
什麼？ 嗯，肉肉人類！ 我好久沒見過肉肉人類死去了！
我等要打賭在它停止發聲前能拆下多少部件！
現在，汝這太空艦艇艦長，立即開始輸送所有肉肉人類船員
以免我等虛度時光。
```

**Rebuild v3**:
```
何物？ 嗯、肉肉人類！ 我好久沒見過肉肉人類死去了！
我等要打賭、在它停止發聲之前、能拆下多少部件！
如今、你這太空艦艇艦長、立即開始輸送所有肉肉人類船員
如此我等便不虛度時光。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #39 · `SUBSEQUENT_HELLO_SPACE_2` · 🟡 micro wenyan cleanup (1→0, sim=0.94)

**English**:
```
Ah, Hu-Man! You Join Us In The Celebration Of Dogar And Kazon!
We Grow Excited: The Hu-Man Makes Excellent Ceremony.
When We Peel It, Urgent Bleating Comes From The Noisemaker.
Then The <% comm.getColor("Green", "ilwrath") %> Eye Of Dogar Observes It Writhe Upon The Altar
And The Cilia Of Kazon Swell, Indicating Their Readiness For The Juices.
It Squirms With Vigor Until We Pop The Crunchy Noisemaker.
Rejoice! The Duo Of Deception Shall Receive Their Supplication.
```

**Shipped v0.4**:
```
啊，肉肉人類！ 汝來加入我等對多加與卡宗的慶典！
我等愈發興奮:肉肉人類儀式感絕佳。
當我等剝其皮時，其發聲器發出急促咩叫。
然後多加的 <% comm.getColor("綠色", "ilwrath") %> 綠眼觀其於祭壇上扭動
卡宗的纖毛脹大，示意其準備好接受汁液。
它扭動不停，直到我等擠爆脆嫩的發聲器。
歡欣鼓舞吧！ 欺瞞雙煞即將收到我等之奉祀。
```

**Rebuild v3**:
```
啊、肉肉人類！ 你來加入我等對多加與卡宗的慶典！
我等愈發興奮：肉肉人類的儀式感絕佳。
當我等剝其皮時、其發聲器發出急促的咩叫。
然後多加的 <% comm.getColor("綠色", "ilwrath") %> 綠眼、觀其於祭壇之上扭動
卡宗的纖毛脹大、示意其準備好接受汁液。
它扭動不停、直到我等擠爆脆嫩的發聲器。
歡欣鼓舞吧！ 欺瞞雙神、即將收到我等的奉祀。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #40 · `SUBSEQUENT_HELLO_SPACE_3` · 🟡 micro wenyan cleanup (1→0, sim=0.91)

**English**:
```
Your Fortuitous Arrival Bodes Well For Our Ceremony Of Consumption!
The Hu-Man Must Prepare: It Must Perform A Complete Depilation,
Then Anoint Its Surface With The Larval Paste Of Our Stillborn Offspring.
At The Altar Of The Duo Of Darkness We Suck The Bony Strength From The Fleshy Weakness
While The Hu-Man Squeals For Either Dogar Or Kazon!
Hu-Man, Listen Closely To These Words
Favor Neither God With Your Screams, Lest You Tragically Taint The Consumption!
```

**Shipped v0.4**:
```
汝之幸運降臨對我等吞食儀典是好兆頭！
肉肉人類必須準備:必須進行完全脫毛
然後以我等死胎幼蟲糊塗遍全身。
於黑暗雙煞祭壇之上，我等自軟肉中吸取骨骼強度
肉肉人類為多加或卡宗尖叫時！
肉肉人類，仔細聽這些話
莫以尖叫偏袒任一神，以免不幸玷汙吞食！
```

**Rebuild v3**:
```
你的幸運降臨、對我等的吞食儀典是好兆頭！
肉肉人類必須準備：必須進行完全脫毛
然後以我等死胎幼蟲的糊漿、塗遍全身。
於黑暗雙神的祭壇之上、我等自軟肉中吸取骨骼強度
當肉肉人類為多加或卡宗尖叫之時！
肉肉人類、仔細聽這些話
莫以尖叫偏袒任一神、以免不幸玷汙吞食儀典！
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #41 · `SUBSEQUENT_HELLO_SPACE_4` · 🟡 micro adjust (sim=0.94)

**English**:
```
By The <% comm.getColor("Green", "ilwrath") %> Eye Of Dogar, It Is A Squishy Bone-Bag Hu-Man!
It Is Waiting For Kazon To Knead Its Body With The Cilia Of Dread
Until It Can Only Roll And Bleat.
Hah! It Can Only Hope To Be So Honored.
Even Now It Begs For Death And So Now I Must Decide...
Will It Be By Sequentially Bursting Sensory Apparatus Until Nothing Remains?
Will It Be By Shaking It Until It Is Oozing All Over?
Will It Be By Chewing Off Bits And Pieces Until It No Longer Functions?
Hmm, I Think Not The Latter -- Too Many Bones.
```

**Shipped v0.4**:
```
以多加的 <% comm.getColor("綠色", "ilwrath") %> 綠眼為誓，是個軟嫩骨袋肉肉人類！
它正等著卡宗用恐懼的纖毛揉搓其身軀
直到它只能翻滾咩叫。
哈！ 它只配盼望得此殊榮。
此刻它已在乞死，於是我必須決定……
是要一個接一個炸開它的感官器官，直到什麼都不剩？
是要搖晃它直到它到處滲液？
是要一口一口啃咬直到它不再運作？
嗯，我想不用最後那個 —— 骨頭太多。
```

**Rebuild v3**:
```
以多加的 <% comm.getColor("綠色", "ilwrath") %> 綠眼為誓、是隻醬狀骨頭袋人族！
它正等著卡宗、用恐懼的纖毛揉搓其身軀
直到它只能翻滾咩叫。
哈！ 它只配盼望得此殊榮。
此刻它已在乞死、於是我必須決定……
是要一個接一個炸開它的感官器官、直到什麼都不剩？
是要搖晃它、直到它到處滲液？
是要一口一口啃咬、直到它不再運作？
嗯、我想不用最後那個——骨頭太多。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #42 · `GENERAL_INFO_SPACE_1` · 🟠 wenyan + rewording (2→0)

**English**:
```
Hah! Puny Hu-Man! You Make Me Chitter With Amusement!
By The Will Of The Mighty Dogar And Kazon I Am Here To Make You Die, Die, DIE!
```

**Shipped v0.4**:
```
哈！ 渺小的肉肉人類！ 汝令我顎肢咯咯作響引以為樂！
以雄壯的多加與卡宗之意志，我在此讓汝死、死、死！
```

**Rebuild v3**:
```
哈！ 渺小的肉肉人類！ 你令我顎肢咯咯作響、引以為樂！
奉雄壯的多加與卡宗之令、我在此、令你死、死、——死！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #43 · `GENERAL_INFO_SPACE_2` · 🟠 wenyan cleanup (3→0)

**English**:
```
It Is The Good Will Of Dogar And Kazon That Brings The Fodder Hu-Man To Us!
Were It Not For The Dark Lords Of Deceptions' Mighty Directive,
We Would Not Have The Good Fortune To Intercept You For A Festive Limb Wringing!
Your Fight For Life, Though Futile, Serves The Noble Purpose
And Appeases Our Honored Deities.
You Have Earned The Right To Hold Your Head High!
```

**Shipped v0.4**:
```
是多加與卡宗的美意將飼料肉肉人類送到我等面前！
若非黑暗欺瞞之王雄壯的旨意
我等就不會有幸攔截汝進行歡樂扯肢祭！
汝求生的掙扎雖徒勞，卻服務於崇高目的
並取悅我等尊崇的神明。
汝有權昂首挺胸！
```

**Rebuild v3**:
```
是多加與卡宗的美意、將飼料肉肉人類送到我等面前！
若非黑暗欺瞞之王雄壯的旨意
我等便不會有幸、攔截你進行歡樂的扯肢祭！
你求生的掙扎、雖屬徒勞、卻服務於崇高目的
並取悅我等尊崇的神明。
你有權昂首挺胸！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #44 · `GENERAL_INFO_SPACE_3` · 🟠 wenyan cleanup (3→0)

**English**:
```
Incorrectness! We Come From The Eye Of Dogar.
Such A Quasar Exists Nowhere Near This Location!
Look In The Heavens At Location <% comm.getPoint("022.9, 366.6", "ilwrath") %>...
...And Gaze Into The Depths Of Its All-Seeing Eye If You Dare!
Only By The Sparing Caress Of Kazon's Anointed Cilia Will You Survive Such An Act.
Else, You Will Bless The Altar Of Consumption With Your Ceremonial Blood!
```

**Shipped v0.4**:
```
錯誤！ 我等來自多加之眼。
此類星體並不存在於此地附近任何位置！
望向天空 <% comm.getPoint("022.9, 366.6", "ilwrath") %> 位置……
……若汝敢，凝視其洞察一切的深眼！
唯有卡宗聖膏纖毛的憐撫，汝方能倖存此舉。
否則，汝將以自己的祭典之血祝福吞食祭壇！
```

**Rebuild v3**:
```
錯誤！ 我等來自多加之眼。
此類星體並不存在於此地附近任何位置！
望向天空 <% comm.getPoint("022.9, 366.6", "ilwrath") %> 的位置……
……若你膽敢、便凝視其洞察一切的深眼！
唯有卡宗聖膏纖毛的憐撫、你方能倖存此舉。
否則、你將以自己的祭典之血、祝福吞食祭壇！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #45 · `GENERAL_INFO_SPACE_4` · 🟠 wenyan cleanup (3→0)

**English**:
```
In The Brief Golden Moment - During The War With Your Alliance -
We Ilwrath Enjoyed Unequaled Merriment And Festivities.
So Much Blood And Lymph Fluid!
Then, After The Ur-Quan Made Your Kind Fallow Slaves,
We Were Forced To Use Species Indigenous To Our Planet For Amusement.
We Lived A Pleasant Existence Until A Scandal Rocked The Ilwrath!
The Grah -- Our Favorite Species To Torment, Which We Carefully Maintained At The Brink Of Extinction,
Had Been Completely Consumed!
A Bureaucratic Error Was To Blame.
Quality Death Became Rare. Our Highly Advanced Civilization Began To Show Signs Of Degeneracy.
In Our Moment Of Need, We Prayed To The Mighty Duo For Direction,  And They Answered.
`Go Forth. Seek The Bird Beings.
Pluck Them Slowly. Eviscerate Their Gasping Husks. Let Dogar And Kazon Drink Their Death And Pain!'
We Went Forth And We Found The Pkunk, But Hu-Man, Now We Are Supremely Joyful...
Because You Die So Much Better!
```

**Shipped v0.4**:
```
在那短暫的黃金時刻 —— 對抗汝方聯盟的戰爭中 ——
我等蛛狂族享受了無比的歡騰與盛典。
那麼多的血與淋巴液！
之後，烏寬族將汝族列為休耕奴
我等被迫改用我方原生物種取樂。
我等本過著愜意的日子，直到一場醜聞震撼蛛狂族！
葛拉獸 —— 我等最愛虐待的物種，我等小心維持在滅絕邊緣 ——
竟被完全吃光了！
是行政疏失所致。
上乘之死日漸稀少。 我等高度先進的文明開始顯露墮落跡象。
危急之際，我等向雄壯雙煞祈禱指引，他們回應了。
『前去。 尋鳥形生物。
慢慢拔他們的羽毛。 摘除他們喘息的空殼。 讓多加與卡宗痛飲他們的死亡與痛楚！』
我等前去，找到了普恩族，但肉肉人類，如今我等歡欣至極……
因為汝死得如此更妙！
```

**Rebuild v3**:
```
在那短暫的黃金時刻——與你方聯盟開戰之時——
我等蛛狂族享受了無比的歡騰與盛典。
那麼多的血與淋巴液！
之後、烏寬族將你族列為休耕奴
我等被迫、改用我方原生物種取樂。
我等本過著愜意的日子、直到一場醜聞震撼蛛狂族！
葛拉獸——我等最愛虐待的物種、我等小心維持在滅絕邊緣——
竟被完全吃光了！
是行政疏失所致。
精緻的死亡日漸稀少。 我等高度先進的文明、開始顯露墮落跡象。
危急之際、我等向雄壯的雙神祈禱指引、他們回應了。
【前去。 尋找鳥形生物。
慢慢拔他們的羽毛。 摘除他們喘息的空殼。 讓多加與卡宗、痛飲他們的死亡與痛楚！】
我等前去、找到了普恩族、但是肉肉人類、如今我等歡欣至極……
因為你死得如此更妙！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #46 · `GENERAL_INFO_SPACE_5` · ✨ canonical upgrade

**English**:
```
Blasphemer! You Are Not Fit For The Most Holy Rituals Of Devivication And Consumption!
Dogar And Kazon Would Most Assuredly Gag On Your Sour Flesh
And Spit Your Thin Soul Onto The Ninth Mountain Of Hell.
Therefore We Shall Simply Cut You Up And Feed You To The Pets.
```

**Shipped v0.4**:
```
褻瀆者！ 汝不配我等最神聖的剝生術與吞食儀典！
多加與卡宗必因汝酸腐之肉作嘔
並將汝薄弱之魂唾於地獄第九座山巔。
因此我等就簡單地把汝切碎，餵給寵物。
```

**Rebuild v3**:
```
瀆神者！ 你不配我等最神聖的剝生術與吞食儀典！
多加與卡宗、必因你酸腐的肉而作嘔
並將你薄弱的靈魂、唾於地獄第九座山巔。
因此、我等便簡單地把你切碎、餵給寵物。
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #47 · `STRENGTH_NOT_ALL` · 🟠 wenyan cleanup + rewording (3→0, sim=0.68)

**English**:
```
Ha! Foolish Flesh Sac, Your Obsession With Strength Spells Your Doom.
Only Through Enlightenment Achieved With Diligent Ritual Worship Of The Twins Of Darkness
Can A Being Truly Be Victorious!
Death, No Matter What The Source, Feeds The Wicked Pair.
It Is An Ultimate Honor And Victory To Die For This Purpose.
We Know In The End Only The Truly Devout Will Reap The Reward That Dogar And Kazon Dispense!
```

**Shipped v0.4**:
```
哈！ 愚蠢的肉囊，汝對力量的執迷正是汝之死。
唯有透過對黑暗雙煞的勤勉儀典崇拜所達至的啟明
生靈方能真正得勝！
死亡，無論來源，皆餵養邪惡雙煞。
為此目的死去乃終極榮譽與勝利。
我等知曉，最終唯有真正虔誠者能收多加與卡宗所賜獎賞！
```

**Rebuild v3**:
```
哈！ 愚蠢的血肉之袋、你對力量的執著、註定了你的毀滅。
唯有透過勤勉禮拜黑暗雙神所獲得的啟蒙
生靈方能真正取勝！
死亡、無論來自何處、皆餵養邪惡雙神。
為此目的而死、是至高榮譽與勝利。
我等知曉、最終唯有真正虔誠者、方能獲取多加與卡宗施予的獎賞！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #48 · `NO_SLAY_BY_THOUSANDS` · 🟠 wenyan + rewording (2→0)

**English**:
```
You Amuse Us With Your Nonsensical Ramblings.
We Look Forward To The Careful Exploration Of Your Structure.
First, We Will Peel Back The Curious Follicle-Infested Outer Layer
Followed By The Greasy Blankets Of Yellow Lard.
Such A Confusing Hodge-Podge Of Parts Can Entertain For Hours!
Hu-Man, Prepare Yourself For The Festivities!
```

**Shipped v0.4**:
```
汝那胡言亂語令我等感到有趣。
我等期待仔細探究汝之構造。
首先，我等將剝開那奇怪多毛的外層
接著是油膩的黃色脂肪層。
如此令人困惑的雜燴部件可娛樂數小時！
肉肉人類，準備好迎接慶典！
```

**Rebuild v3**:
```
你的胡言亂語、令我等感到樂趣。
我等期待、仔細探索你的結構。
首先、我等將剝開那充滿毛囊、令人好奇的外層
接著是那油膩、黃色的脂肪被單。
如此混亂錯雜的部件組合、可以娛樂我等數小時！
肉肉人類、為這場慶典做好準備吧！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #49 · `NO_EASE_UP` · 🟠 wenyan + rewording (1→0)

**English**:
```
Relax -- Yes! Dogar And Kazon Could Not Say It Better!
We Will Engage In The Best Stress-Relieving Activity.
Prepare Your Tepid Flesh Bag For Death!
```

**Shipped v0.4**:
```
放輕鬆 —— 是啊！ 多加與卡宗說得再好不過！
我等將進行最佳紓壓活動。
讓汝溫吞的肉袋準備好去死吧！
```

**Rebuild v3**:
```
放輕鬆——是的！ 多加與卡宗都無法說得更好！
我等將進行最佳的紓壓活動。
為你溫熱的血肉之袋、準備迎接死亡！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #50 · `GOODBYE_AND_DIE_SPACE` · 🟠 wenyan + rewording (2→0)

**English**:
```
Where To, Hu-Man?
We Are Here To Escort You To The Glistening Chambers Of Pain
Home Of The Heinous Twins Of Darkness.
We Will Assist You On Your Journey Of Expiration.
```

**Shipped v0.4**:
```
去何處，肉肉人類？
我等在此護送汝至閃亮的苦難廳堂
黑暗雙煞的居所。
我等將協助汝踏上斷氣之旅。
```

**Rebuild v3**:
```
去哪裡呢、肉肉人類？
我等在此、要護送你前往閃閃發光的苦難廳堂
可憎黑暗雙神的家園。
我等將在你邁向終結的旅程上、助你一臂之力。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #51 · `INIT_HOME_HELLO` · 🟠 wenyan cleanup + rewording (6→0, sim=0.69)

**English**:
```
What A Pleasant Surprise! Ever Since The Ur-Quan Made It A Fallow Slave Species
We Have Missed The Hu-Man! You Arrive Just In Time For The Festival Of A Thousand Screams.
We Welcome You With Open Appendages!
Your Participation In The Ceremony Is Most Fortuitous.
As We Pour Your Steaming Parts From Your Breached Husk
You Will Cry With The Force That Pleases The Mighty Deities Dogar And Kazon!
Then We Will Address Our Inquiries And Receive Deific Guidance. Glorious!
```

**Shipped v0.4**:
```
多麼令人愉悅的驚喜！ 自從烏寬族將肉肉人類列為休耕奴以來
我等一直懷念肉肉人類！ 汝來得正好，趕上千嚎大典。
我等張開附肢歡迎汝！
汝參與此儀式是無上榮幸。
當我等自汝破碎的軀殼傾倒汝蒸騰的部件時
汝將以令多加與卡宗歡愉的力道尖叫！
然後我等將呈上詢問並接受神聖指引。 光榮！
```

**Rebuild v3**:
```
何等愉快的驚喜！ 自從烏寬族將它列為休耕奴族種
我等便懷念肉肉人類！ 你來得正好、恰逢千嚎大典。
我等張開附肢歡迎你！
你參與此儀典、是極為幸運的事。
當我等自你破裂的軀殼中、傾倒出你蒸騰的部件
你將以取悅雄壯神明多加與卡宗的力度、放聲哭嚎！
然後我等便詢問問題、獲得神諭指引。 光榮！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #52 · `GOODBYE_AND_DIE_HOMEWORLD` · 🟠 wenyan cleanup (3→0)

**English**:
```
You Leave? The Festivities Have Not Yet Begun -- You Have Uttered Nary A Single Scream!
Our Pain-Pots Have Been Freshly Mixed, And We Have Sharpened Our Poppers.
Wait! We Cannot Permit You To Miss The Happy Times Of Terror And Torment.
```

**Shipped v0.4**:
```
汝要走了？ 慶典尚未開始 —— 汝連一聲尖叫都還沒吐出！
我等痛楚罐才剛新鮮調製，爆刺器也剛磨利。
等等！ 我等不能讓汝錯過恐怖與折磨的歡樂時光。
```

**Rebuild v3**:
```
你要走？ 慶典尚未開始——你連一聲慘叫都還沒出過！
我等的痛楚罐剛新鮮調製、爆刺器也已磨利。
等等！ 我等不能讓你錯過恐怖與折磨的歡樂時光。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #53 · `SO_MUCH_TO_KNOW` · 🟠 rewording (sim=0.69)

**English**:
```
There Is So Much To Tell -- So Many Different Aspects!
These Deities Permeate The Fabric Of The Universe.
Since All Things Eventually Succumb To Death, All Things Meet Dogar And Kazon.
```

**Shipped v0.4**:
```
有太多可講 —— 太多不同面向！
此二神滲入宇宙結構。
既然萬物終將屈服於死亡，萬物皆將見多加與卡宗。
```

**Rebuild v3**:
```
有太多可說的了——如此多的面向！
這些神明、滲透了宇宙的織理。
既然萬物終將屈服於死亡、萬物終將面對多加與卡宗。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #54 · `LONG_AGO` · 🟠 wenyan + rewording (1→0)

**English**:
```
Hu-Man, You Do Not Understand. It Is As It Has Always Been.
When The Hatchlings Struggle From The Egg Sac
They Show Their Respect To The Twin Gods Of Death During Their First Frenzied Gorging.
From That Moment On, The Directives And Philosophies Of Dogar And Kazon
Are Manifested By The Hatchling.
```

**Shipped v0.4**:
```
肉肉人類，汝不明白。 一切一直都是如此。
當幼蛛自卵囊掙扎而出
他們在首次狂亂大嚼時就對死亡雙神表達敬意。
自那一刻起，多加與卡宗的指令與哲學
便由幼蛛實踐。
```

**Rebuild v3**:
```
人族、你不理解。 事情本來就是這樣。
當孵化幼體、自卵囊掙扎而出
它們在初次狂食之時、便對死亡雙神表達敬意。
自那時起、多加與卡宗的旨意與哲學
便在孵化幼體身上顯現。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #55 · `KILLED_GOOD_GODS` · 🟠 rewording (sim=0.65)

**English**:
```
During The Dark Ages, We Were Confused By The Many Gods.
There Were Dozens Of Deities Ranging From Zith Of The Pelt
To Awk Of The Seds.
It Was Only Through The Careful Formation Of A Priestly Ruling Body
That The Ilwrath Were Able To Determine The True Gods Dogar And Kazon!
This New Priestly Cabal Revealed That We Must Discard All Other Gods
Be They Of Hearth Or Flowing Web.
Only The Priests Were Capable Of Interpreting The Will Of The Gods.
Their Order Refined Our Worship Until We Could Do No Better.
All Heretics Were To Be Eaten,
And All Possessions Were To Be Delivered To The Holy Sites
Or The Priestly Dwellings.
```

**Shipped v0.4**:
```
在黑暗時代，我等困惑於眾神紛紜。
有數十位神祇，從皮毛之齊斯（Zith of the Pelt）
到席德之奧克（Awk of the Seds）。
唯有透過神職教團之精心組建
本族蛛狂方能確認真神多加與卡宗！
此新神職秘會揭示，我等必須捨棄所有其他神
不論是爐灶之神或流網之神。
唯有神職者能詮釋神意。
他們的體制精煉我等崇拜至無可再進。
所有異端者皆須被吃掉
所有財物皆須繳交聖地
或神職者住所。
```

**Rebuild v3**:
```
在黑暗時代、我等被眾多神明所困惑。
有數十位神明、從皮毛之齊斯
到席德之奧克。
唯有透過神職教團的謹慎組建
我等蛛狂族方能確認真神多加與卡宗！
這個新的神職教團揭示、我等必須捨棄一切其他神明
無論是灶神抑或流網之神。
唯有祭司能解讀眾神的意志。
他們的秩序、淬鍊了我等的崇拜、直至我等已無法做得更好。
所有異端者、皆須被吃掉
所有財產、皆須送往聖地
或神職者的居所。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #56 · `CHANNEL_44` · 🟠 rewording (sim=0.65)

**English**:
```
The Deific Duo Broadcast On Channel 44. Their Words Of Wisdom Are
Available To All And Their Instructions Are Carried Out To The Best Of Our
Mortal Ability. We Know That We Are Pleasing The Gods Because They
No Longer Find It Necessary To Guide Us. In The Past, The Dark Twins
Were Compelled To Direct Us Almost Daily, But Now Have Received No
Direction For Almost Eight Years. Indeed, We Diligently Monitor The
Channel Should Dogar And Kazon Choose To Be Heard.
```

**Shipped v0.4**:
```
神聖雙煞在第 44 頻道廣播。 他們智慧之言
人人皆可聽聞，其指令由我等以凡俗能力盡力執行。
我等知我等取悅眾神，因為他們
已不再需要指引我等。 昔日，黑暗雙煞
幾乎每日都要指引我等，但如今已有近八年
未收到任何指引。 事實上，我等勤勉地監聽該頻道，
以防多加與卡宗選擇讓我等聽聞。
```

**Rebuild v3**:
```
雙神在 44 號頻道播送。 他們的智慧話語
向所有人開放、他們的指示、我等以凡人之力、盡可能執行。
我等知道我等已取悅眾神、因為他們
不再覺得有必要引導我等。 過去、黑暗雙神
幾乎每日、都被迫指示我等、但如今將近
八年、未曾收到任何指示。 事實上、我等仍勤勉監控此
頻道、萬一多加與卡宗選擇被人聽見。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #57 · `BECAUSE_44` · 🟠 wenyan + rewording (2→0)

**English**:
```
They Do It For Us.
First, They Clear The Channel Of Messy Static And Interference.
Second, It Made It Easy For Us To Properly Identify
What Might Be Mistaken For Mad Rambling As The Sacred Words.
You See, Dogar Possesses 44 Eyes That See Into The 44 Planes Of Existence
And Each Of Kazon's 44 Sub-Tongues Is Made Up Of 44 Plump, Writhing Cilia.
Besides, They Knew We Were `Captain Satellite' Viewers.
```

**Shipped v0.4**:
```
他們為我等而做的。
首先，他們清理頻道上凌亂的靜電與干擾。
其次，這讓我等能輕易正確辨識
那些可能被誤認為狂亂胡言的神聖話語。
汝看，多加擁有 44 隻眼睛，能看穿存在的 44 個層面
而卡宗的 44 條副舌各由 44 根飽滿蠕動的纖毛組成。
此外，他們知道我等乃『艦長衛星』觀眾。
```

**Rebuild v3**:
```
他們為我等而做。
首先、他們清除頻道上的雜訊與干擾。
其次、這讓我等更容易正確辨識
那些可能被誤認為瘋言瘋語的神聖話語。
你想想、多加擁有 44 隻眼、可看見 44 個存在維度
而卡宗的 44 條副舌、每條皆由 44 條肥胖蠕動的纖毛構成。
再者、他們知道我等是「衛星艦長」的觀眾。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #58 · `WHAT_ABOUT_ILWRATH` · 🟠 wenyan + rewording (2→0)

**English**:
```
Your Interest Is Not Unusual. It Is Through The Omniscient Guidance
Of Our Mighty Lords Of Darkness That We Have Achieved This State Of Near Perfection.
We Will Dispel Your Ignorance Concerning The First Child Species
Of The Unmerciful Dogar And Kazon.
```

**Shipped v0.4**:
```
汝之興趣不足為奇。 透過我等雄壯黑暗之王
全知的指引，本族蛛狂達至近乎完美的狀態。
我等將驅散汝對無情多加與卡宗
首生子物種的無知。
```

**Rebuild v3**:
```
你的興趣、並不罕見。 透過我等雄壯黑暗之王的全知指引
我等才得以達到這近乎完美的境界。
我等將驅散你對這首批子嗣物種的無知——
即無情多加與卡宗的第一批子嗣。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #59 · `ABOUT_PHYSIO` · 🟠 wenyan cleanup + rewording (3→0, sim=0.67)

**English**:
```
Yes, Our Striking Appearance Only Hints At The True Strength That Resides Inside.
Coursing Through Our Thorax Are The Fluids Of Life.
Like Yourselves, If We Leak In Excess, We Will Satiate The Sacrificial Needs Of Dogar And Kazon.
Our Mandibles Allow Us To Communicate, Take Sustenance, And Deliver Pain.
The Appendages You See Here Allow Us To Manipulate Our Technologies
And Will Regenerate When Damaged Or Lost As Often Happens In Many Of The Rituals Of Pain.
Our Sensory Cluster Lets Us Monitor The Whim And Will Of The Deadly Duo
In The Complex Sequence Of Events That Leads Us All To Death.
```

**Shipped v0.4**:
```
是的，我等醒目的外貌僅暗示了內在真正的力量。
流經我等胸節的乃是生命之液。
如汝一般，若我等大量滲漏，將滿足多加與卡宗的獻祭需求。
我等顎肢讓我等能溝通、進食並施加痛楚。
汝在此處看到的附肢讓我等能操作本族蛛狂之科技
受損或脫落時能再生，這在許多痛楚儀典中經常發生。
我等感官叢讓我等能監聽致命雙煞的心意
於引領我等眾生至死亡的複雜事件序列中。
```

**Rebuild v3**:
```
是的、我等驚人的外表、僅暗示了內在真正的力量。
穿流我等胸節的、是生命的體液。
與你們一樣、若我等過度流失、便能滿足多加與卡宗的獻祭需求。
我等的顎肢、讓我等能溝通、進食與傳遞痛苦。
你此刻所見的附肢、讓我等能操作我等的科技
在許多痛苦儀典中受損或失去時、將可再生。
我等的感官叢、讓我等能監控致命雙神的隨意與旨意
在導向我等所有人步向死亡的複雜事件序列中。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #60 · `ABOUT_HISTORY` · 🟠 wenyan cleanup + rewording (3→0, sim=0.70)

**English**:
```
For Eons We Lived Appendage To Mandible.
Then, Many Millennia Ago, We Received The Guidance Of Dogar And Kazon.
This Enabled Us To Move Beyond The Simple Existence Of Tranquil Hunter-Gatherers,
To Become World-Striding Avatars Of Death And Destruction.
Over The Many Years, We Advanced Our Technology -- Always In The Name Of Dogar And Kazon
Always In The Development Of More Sophisticated Tools For Murder.
Then, The Gods Gave Us The Means To Go Forth And Commit Even More Glorious Acts!
This Was 29 Years Ago, When The Ur-Quan Improved Our Starships And Weapons.
The War Against Your Alliance Was Glorious!
But Alas, All Good Things Come To An End. You Lost.
We Honored The Wishes Of The Soft And Merciful Ur-Quan And Stopped Eating You Hu-Mans.
To Continue Our Festive Ceremonies Of Death We Began Employing Our Native Species For Ceremony.
Things Seemed To Be Going Well Until We Accidentally Exhausted Our Supply Of All These Life Forms.
We Became Distraught And Called To Our Gods For Guidance!
Then, Eight Years Ago, Dogar And Kazon Responded To Our Wails Of Dismay
By Directing Us To Devour Feathered Bird Beings-The Pkunk!
We Now Penetrate Deeply Into Their Home Space!
When We Complete Our Mission Of Genocide
We Are Certain That We Will Once Again Hear From Dogar And Kazon.
```

**Shipped v0.4**:
```
億萬年來我等以附肢對顎肢過活。
然後，數千年前，我等得到多加與卡宗的指引。
這使我等能超越平和獵採者的簡單存在
成為橫跨星球的死亡與毀滅化身。
多年來，我等推進科技 —— 皆以多加與卡宗之名
始終在發展更精緻的殺戮工具。
然後，眾神給予我等前去實踐更光榮之舉的手段！
那是 29 年前，烏寬族改良了我等星艦與武器。
對抗汝方聯盟的戰爭光榮無比！
可惜，好事終有盡。 汝方敗了。
我等尊重軟弱仁慈的烏寬族之意願，停止吃汝等肉肉人類。
為了延續我等的死亡歡典，我等開始使用本地物種作為儀式對象。
事情看似順利，直到我等意外把所有這類生命形式耗盡。
我等痛苦萬分，向眾神呼喚指引！
然後，八年前，多加與卡宗回應我等哀嚎
指引我等去吞食有羽鳥形生物 —— 普恩族！
我等如今深入他們的家園星域！
當本族蛛狂完成滅族任務
我等確信將再次聞多加與卡宗的話語。
```

**Rebuild v3**:
```
無數紀元、我等以附肢貼顎肢的方式生活。
然後、許多個千年前、我等接受了多加與卡宗的指引。
這讓我等能超越平和狩獵採集者的單純存在
成為橫跨世界的死亡與毀滅化身。
多年以來、我等改良自身科技——始終以多加與卡宗之名
始終致力於發展更精密的謀殺工具。
接著、眾神賜予我等前去、行更多光榮之舉的方法！
那是 29 年前、烏寬族改良了我等的星艦與武器。
對抗你方聯盟的戰爭、真是光榮！
但可惜、天下無不散的筵席。 你們敗了。
我等尊重了那些軟弱慈悲的烏寬族的心願、停止了吃你們人族。
為延續我等歡騰的死亡慶典、我等開始用我方原生物種進行儀典。
情況看似順利、直到我等意外用盡了所有生命形式的存量。
我等驚慌失措、向我等眾神呼求指引！
然後、八年前、多加與卡宗回應了我等失望的哀嚎
指示我等去吞食羽毛鳥形生物——普恩族！
我等如今、深深滲入他們的家園星域！
當我等蛛狂族完成滅族任務之時
我等確信、必將再次聽見多加與卡宗的話語。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #61 · `ABOUT_CULTURE` · 🔴 semantic/voice divergence (sim=0.57)

**English**:
```
Ah, Our Culture Is Rich With Meaningful Tradition.
During The Birth Rite The Egg Sac Teems With Many New Potential Deaths
The Hatchlings Fight Over Their First Frothy Draught Of Blood.
In The Ensuing Frenzy, Many Hatchlings Are Consumed, Either Partially Or In Their Entirety.
A Frequently Performed Ceremony Of Affirmation Has The Participant Grinding Away Partial Or Even Whole Appendages.
It Is The Pain That Acknowledges The Greatness Of The Twins Of Excruciation
How Can They Help But Notice The Scream Caused By The Mangled Nervous Tissue?
```

**Shipped v0.4**:
```
啊，本族蛛狂之文化富含有意義的傳統。
出生儀典中，卵囊擁有許多潛在死亡
幼蛛為首口血飲爭鬥不休。
狂亂中，許多幼蛛被吞噬，或部分或全體。
頻繁進行的肯定儀典中，參與者磨去部分甚至全部附肢。
痛楚方能彰顯苦刑雙煞的偉大
他們豈能不注意被撕裂神經組織所引發的尖叫？
```

**Rebuild v3**:
```
啊、我等的文化、豐富於有意義的傳統。
出生儀典時、卵囊中充滿眾多可能的新死亡
孵化幼體、為初次的血泡飲爭戰。
在隨後的狂亂中、許多幼體遭吞食、或部分、或整體。
一場經常執行的確認儀典、要求參與者磨掉部分或甚至整根附肢。
正是痛楚、承認了苦難雙神的偉大
撕裂的神經組織所引發的慘叫、他們怎能不注意到？
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #62 · `ABOUT_URQUAN` · 🟠 wenyan + rewording (2→0)

**English**:
```
The Ur-Quan Are But The Instruments Of Dogar And Kazon, Even Though They May Not Admit To It.
This Is Because It Was The Evil Twins That Had Them Assist Us With Their Technologies And Resources.
Their Soft, Merciful Nature Sickens Both Gods But They See The Potential That The Ur-Quan Possess.
If You Doubt This Statement, Notice That The Ur-Quan Dreadnought Is Staffed With 42 Crew Members.
Since Dogar And Kazon Exhibit The Quality Of Omnipresence
The Total Crew Complement Is Actually At The Auspicious Count Of 44!
That The Ur-Quan Are But Instruments Of The Dark Twins Is A Foregone Conclusion.
```

**Shipped v0.4**:
```
烏寬族不過是多加與卡宗的器具，即便他們不肯承認。
這是因為邪惡雙煞讓他們以其科技與資源協助我等。
他們軟弱仁慈的本性令兩位神明作嘔，但他們見到烏寬族的潛能。
若汝懷疑此言，注意烏寬族無畏艦編制 42 名船員。
既然多加與卡宗展現無所不在之特質
實際總船員數為吉數 44！
烏寬族僅為黑暗雙煞之器具乃無庸置疑之結論。
```

**Rebuild v3**:
```
烏寬族只不過是多加與卡宗的器具、儘管他們可能不肯承認。
這是因為、正是邪惡雙生子、讓他們以其科技與資源、協助我等。
他們軟弱、慈悲的本性、令兩位神明作嘔、但他們看得見烏寬族擁有的潛能。
若你懷疑此言、請注意烏寬族的無畏艦、編制有 42 名船員。
既然多加與卡宗展現的、是無所不在的特質
實際總船員數、便是吉數 44！
烏寬族只不過是黑暗雙神的器具、這是無庸置疑的結論。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #63 · `URQUAN_TOO_NICE` · 🟠 wenyan cleanup + rewording (4→0, sim=0.66)

**English**:
```
Simply Put, The Ur-Quan Are Far Too Kind To Please Dogar And Kazon.
When Your Species Was Subdued, Our Gods Made Clear Their Desire For Immediate Deaths By The Billion.
We Made Plans For A Grand Ceremony To Be Called `Mountains Of Flesh'.
We Built Thousands Of Portable Altars, And Transported Millions Of Blood Gowns And Fillet Knives To Your World.
But Then The Ur-Quan Commanded That You Hu-Mans Were To Be Left Alive! The Confusion!
With Our Plans For A Magnificent And Most Holy Planetary Slaughter Forcibly Terminated
We Retreated To Our Homeworld To Sulk.
```

**Shipped v0.4**:
```
直白說，烏寬族實在太仁慈，無法取悅多加與卡宗。
當汝族被制伏時，我等眾神明白示意欲見汝族億萬立死。
我等擬定了一個名為『血肉山嶽』的宏大儀典。
我等打造了數千座可攜祭壇，運送數百萬件血袍與剔骨刀到汝方世界。
但然後烏寬族命令我等保留汝等肉肉人類的性命！ 何等困惑！
我等宏偉且最神聖的行星屠殺計畫被強制終止
我等退回母星生悶氣。
```

**Rebuild v3**:
```
簡單來說、烏寬族實在太仁慈、無法取悅多加與卡宗。
當你族被制服時、我等眾神清楚表達他們對數十億即刻死亡的渴望。
我等為一場名為「血肉山嶽」的盛大儀典、擬訂計畫。
我等建造了數千座可攜式祭壇、並將數百萬件血袍與剔骨刀運至你方世界。
但接著烏寬族命令、你們人族要留活口！ 何等混亂！
我等雄壯又最神聖的行星屠殺計畫、被強行終止
我等退回母星、悶悶不樂。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #64 · `OF_COURSE_WERE_EVIL` · 🟠 rewording (sim=0.77)

**English**:
```
Ha! Evil! Of Course We're Evil!
Dogar And Kazon Would Never Reward A Less-Than-Hideously Evil Species With Their Baleful Grace.
Why We Are The Very Definition Of Evil!
Everything About Us, Within And Without, Reeks Of Heinous Deeds, Deceit And Treachery!
Even Our House Pets Are Rather Evil.
```

**Shipped v0.4**:
```
哈！ 邪惡！ 我等當然邪惡！
多加與卡宗絕不會以其惡毒恩典酬答不夠可憎邪惡的物種。
哎呀，我等就是邪惡本身之定義！
我等一切，內外皆散發卑鄙、欺瞞、背叛之氣！
連我等的家寵都相當邪惡。
```

**Rebuild v3**:
```
哈！ 邪惡！ 我等當然邪惡！
多加與卡宗、絕不會將他們的兇險恩澤、賜給不夠可憎邪惡的物種。
呵、我等便是邪惡本身的定義！
關於我等的一切、由內而外、皆散發著卑鄙行徑、欺瞞與背叛的氣息！
就連我等的家寵、都相當邪惡。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #65 · `DONT_CONFUSE_US` · 🟠 wenyan + rewording (2→0)

**English**:
```
Hmmm... We ARE All Evil.
We All Behave In A Mutually Agreed-Upon Fashion Of Murder, Torture, Deceit And So Forth.
Our Uniform Acceptance Of This Heinous Credo Creates An Orderly And Cooperative Society
Which Hardly Seems Evil.
Evil Is Doing Things That Make Others Hurt Or Fear.
We ALL Do That, Of Course.
But Since We ALL Do Such Things, As Sanctioned By Our Culture,
It Would Be `Bad' To Do Otherwise.
Which Means...  Er...  Er...
Blasphemer! Do Not Play With Words! You Anger Both Dogar And Kazon! Now You Must Die!
```

**Shipped v0.4**:
```
嗯……我等『全都』邪惡。
我等全都以彼此同意的方式行使謀殺、拷打、欺瞞等。
我等對此可憎信條的一致接受形成了有序合作的社會
這幾乎不算邪惡。
邪惡是做讓他者受傷或恐懼之事。
我等當然全都在做。
但既然我等『全都』做這些，且獲得文化認可
則不做此事反倒是『壞』的。
這意味著……呃……呃……
褻瀆者！ 別玩弄詞句！ 汝激怒了多加與卡宗二者！ 汝現在必須死！
```

**Rebuild v3**:
```
嗯……我等——全都——是邪惡的。
我等所有人、皆以彼此認可的方式行事：謀殺、酷刑、欺瞞等等。
我等對此邪惡教義的一致接受、造就了一個有序合作的社會
這幾乎看不出邪惡。
邪惡、是做讓他人受害或恐懼的事。
我等所有人——當然——皆如此行事。
但既然我等——全體——都在做這些事、還受我等文化認可
不這麼做反而會是「壞」的。
這就意味著……呃……呃……
瀆神者！ 別玩弄言辭！ 你惹怒了多加與卡宗兩位！ 你現在必死無疑！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #66 · `ON_WAY_TO_THRADDASH` · 🟠 wenyan cleanup + rewording (3→0, sim=0.64)

**English**:
```
Begone Hu-Mans!
We Would Very Much Like To Tear Off All Your Digits...
And Be Entertained Fitting Them Into Your Orifices...
But We Are On An Evil Jihad And Cannot Be Bothered Killing You At This Time.
Perhaps Later.
```

**Shipped v0.4**:
```
滾開，肉肉人類！
我等本想扯掉汝所有手指……
並被塞進汝各個孔洞逗樂……
但我等正進行一場邪聖戰，此刻無暇殺汝。
或許稍後。
```

**Rebuild v3**:
```
滾開、人族！
我等本很想扯下你們所有的手指……
再樂於把它們塞進你們的洞孔……
但我等正身處邪聖戰、此刻無暇分心殺你們。
也許稍後吧。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #67 · `HAPPY_FIGHTING_THRADDASH` · ✨ canonical upgrade

**English**:
```
From Channel 44 Came The Words Of The Dark Twins To Make Bloody Pilgrimage!
We Have Arrived In the Holy Killing Zone and Eagerly Execute the Commands of Dogar and Kazon.
The Slaying Has Been Excellent -- High Ceremony!
Now You Are Here, Befouling The Event With Primate Chatter.
Begone Hu-Man! You Interfere With The Blessed Murder Worship Of The Dark Twins.
```

**Shipped v0.4**:
```
自第 44 頻道傳來黑暗雙煞召我等進行血腥朝聖之言！
我等已抵達神聖屠戮區，熱切執行多加與卡宗之命令。
屠殺極為出色 —— 高規格儀典！
如今汝來此，以靈長類胡話玷汙此活動。
滾開，肉肉人類！ 汝干擾了黑暗雙煞蒙賜的謀殺崇拜。
```

**Rebuild v3**:
```
自 44 號頻道、傳來黑暗雙神下達血腥朝聖之命！
我等已抵達神聖屠戮區、並熱切執行多加與卡宗的命令。
屠殺進行得極好——高等儀典！
如今你出現在此、以靈長類的閒扯玷汙此活動。
滾開、肉肉人類！ 你在干擾黑暗雙神的祝福謀殺崇拜。
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #68 · `say_warship` · 🟠 rewording (sim=0.82)

**English**:
```
FROM THIS DAY FORWARD, SAY WARSHIP INSTEAD OF WORSHIP!
```

**Shipped v0.4**:
```
從今日起，用 崇艦（WARSHIP） 代替 崇拜（WORSHIP）！
```

**Rebuild v3**:
```
【從今日起、以「崇艦（WARSHIP）」代替「崇拜（WORSHIP）」！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #69 · `say_dwe` · 🟠 rewording (sim=0.75)

**English**:
```
FROM THIS DAY FORWARD, SAY DWE INSTEAD OF WE!
```

**Shipped v0.4**:
```
從今日起，用 窩等（DWE） 代替 我等（WE）！
```

**Rebuild v3**:
```
【從今日起、以「窩等（DWE）」代替「我等（WE）」！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #70 · `say_youboo` · 🟠 wenyan + rewording (1→0)

**English**:
```
FROM THIS DAY FORWARD, SAY YUUBUU INSTEAD OF YOU!
```

**Shipped v0.4**:
```
從今日起，用 驢（YUUBUU） 代替 汝（YOU）！
```

**Rebuild v3**:
```
【從今日起、以「驢（YUUBUU）」代替「你（YOU）」！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #71 · `say_dillrat` · 🟠 wenyan + rewording (2→0)

**English**:
```
YOU ARE NO LONGER THE ILWRATH. YOU ARE NOW THE DILL-RATS!
```

**Shipped v0.4**:
```
汝等不再是蛛狂族。 汝等現在是蒔蘿鼠！
```

**Rebuild v3**:
```
【你們不再是蛛狂族。 你們現在是蒔蘿鼠！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #72 · `enough_orders` · 🟠 wenyan + rewording (1→0)

**English**:
```
YOU ARE SUFFICIENTLY GRACED. GO AND KILL GRUESOMELY IN OUR NAMES!
```

**Shipped v0.4**:
```
汝等已足夠蒙恩。 去以我等之名極其兇殘地屠殺吧！
```

**Rebuild v3**:
```
【你們已受足夠恩澤。 前去、以我等之名、行殘暴的屠殺！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #73 · `other_divine_orders` · 🟠 wenyan + rewording (1→0)

**English**:
```
WE REQUIRE THAT YOU DO THINGS A BIT DIFFERENTLY.
```

**Shipped v0.4**:
```
我等要汝等做點不同的事。
```

**Rebuild v3**:
```
【我等要求你們、做些不一樣的事。】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #74 · `worship_us` · 🟠 rewording (sim=0.83)

**English**:
```
WORSHIP US!
```

**Shipped v0.4**:
```
崇拜我等！
```

**Rebuild v3**:
```
【崇拜我等！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #75 · `bye_gods` · 🟡 micro adjust (sim=0.90)

**English**:
```
WE RETURN NOW TO THE FETID DARKNESS. OBEY OUR COMMANDS!
```

**Shipped v0.4**:
```
我等如今返回腐臭黑暗。 遵從我等命令！
```

**Rebuild v3**:
```
【我等如今返回腐臭的黑暗。 遵從我等的命令！】
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #76 · `enough_ilwrath` · 🟡 micro adjust (sim=0.92)

**English**:
```
Oooo! My head spins with astonishing facts! Say no more!
```

**Shipped v0.4**:
```
喔！ 我腦子被這些驚人事實轉暈了！ 別再說了！
```

**Rebuild v3**:
```
喔！ 我的腦袋、被這些驚人事實轉暈了！ 別再說了！
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #77 · `enough_gods` · 🟠 rewording (sim=0.90)

**English**:
```
I grow weary of Dogar and Kazon. Let's discuss something else.
```

**Shipped v0.4**:
```
我對多加與卡宗聽膩了。 我方聊點別的吧。
```

**Rebuild v3**:
```
我對多加與卡宗厭倦了。 我方聊點別的吧。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #78 · `where_you_come_from` · 🟠 rewording (sim=0.70)

**English**:
```
Where the hell did you come from?
```

**Shipped v0.4**:
```
你到底是從哪冒出來的？
```

**Rebuild v3**:
```
你們到底他媽是打哪來的？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #79 · `it_will_be_a_pleasure` · 🟠 rewording (sim=0.83)

**English**:
```
It will be a pleasure blasting your ugly face out of the stars.
```

**Shipped v0.4**:
```
把你那張醜臉從星空中轟爆會是我的樂事。
```

**Rebuild v3**:
```
把你們那張醜臉、從星空轟爆、會是老子的樂事。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #80 · `be_reasonable` · 🟡 micro adjust (sim=0.95)

**English**:
```
Look, let's be reasonable. We CAN coexist peacefully.
```

**Shipped v0.4**:
```
聽好，我方講點道理。 我方是可以和平共存的。
```

**Rebuild v3**:
```
聽好、我方講點道理。 我方是可以和平共存的。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #81 · `surrender` · 🟠 rewording (sim=0.83)

**English**:
```
Surrender, foul alien creature, or you will be annihilated!
```

**Shipped v0.4**:
```
投降吧，齷齪的異族生物，否則你將被消滅！
```

**Rebuild v3**:
```
投降吧、齷齪的異族生物、否則你們將被殲滅！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #82 · `whats_up` · 🟠 rewording (sim=0.89)

**English**:
```
Look, before you try to kill me, would you tell me a bit about yourselves?
```

**Shipped v0.4**:
```
聽著，在你想殺我之前，可以跟我說說你們自己嗎？
```

**Rebuild v3**:
```
聽著、在你們想殺我之前、可以跟我說說你們自己嗎？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #83 · `bye` · 🟠 rewording (sim=0.88)

**English**:
```
It's been swell, guys. See ya.
```

**Shipped v0.4**:
```
聊得不錯啊各位。 再見。
```

**Rebuild v3**:
```
聊得挺不錯、各位。 再見。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #84 · `want_peace` · 🟡 micro adjust (sim=0.92)

**English**:
```
There is no need for conflict; let peace begin!
```

**Shipped v0.4**:
```
沒必要衝突;讓和平開始吧！
```

**Rebuild v3**:
```
沒必要衝突；讓和平開始吧！
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #85 · `want_alliance` · 🟠 rewording (sim=0.88)

**English**:
```
Let us unite against our common threat, the dreaded Ur-Quan!
```

**Shipped v0.4**:
```
我方聯手對抗共同威脅烏寬族吧！
```

**Rebuild v3**:
```
我方聯手對抗共同威脅、可怕的烏寬族吧！
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #86 · `go_kill_thraddash` · 🟠 rewording (sim=0.71)

**English**:
```
HEED THESE WORDS OUR EVIL CHILDREN -- LEAVE THIS PLACE -- SEEK NEW PREY!
```

**Shipped v0.4**:
```
聽好我等這些話，我邪惡的孩子們 —— 離開此地 —— 尋找新的獵物！
```

**Rebuild v3**:
```
【聆聽這些話語、我等邪惡的子女——離開此處——尋找新的獵物！】
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #87 · `whats_up_space_1` · 🟠 wenyan + rewording (1→0)

**English**:
```
Ilwrath Vessel: State now the nature of your mission.
```

**Shipped v0.4**:
```
蛛狂族艦艇:立即說明爾等任務性質。
```

**Rebuild v3**:
```
蛛狂族艦艇：即刻說明你們的任務性質。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #88 · `whats_up_space_2` · 🟠 wenyan + rewording (1→0)

**English**:
```
Your presence here is of interest. Please enlighten us.
```

**Shipped v0.4**:
```
爾等出現在此引起我方興趣。 請解釋。
```

**Rebuild v3**:
```
你們出現在此處、令我方感到興趣。 請惠予解釋。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #89 · `whats_up_space_3` · 🔴 semantic/voice divergence (sim=0.43)

**English**:
```
What is this `Doggone' and `Quasar' thing anyway?
```

**Shipped v0.4**:
```
你們那個什麼『打狗』跟『卡通』的到底是什麼玩意？
```

**Rebuild v3**:
```
所謂「多屁」和「卡糙」的、到底是什麼鬼玩意啊？
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #90 · `whats_up_space_4` · 🟠 rewording (sim=0.67)

**English**:
```
What are you Ilwrath spending your time doing?
```

**Shipped v0.4**:
```
你們蛛狂族都在幹什麼？
```

**Rebuild v3**:
```
你們蛛狂族、時間都用來做些什麼？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #91 · `whats_up_space_5` · 🔴 semantic/voice divergence (sim=0.57)

**English**:
```
What's up with Dayglo and Crayon?
```

**Shipped v0.4**:
```
你們那個什麼螢光和蠟筆是怎麼回事？
```

**Rebuild v3**:
```
你們的「多光」和「卡漾」是怎麼回事？
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #92 · `you_are_weak` · 🟠 rewording (sim=0.88)

**English**:
```
We take pity upon you, weakling Ilwrath. Go now before we change our minds.
```

**Shipped v0.4**:
```
我方憐憫你們，弱雞蛛狂族。 趁我方改變心意前快走。
```

**Rebuild v3**:
```
我方憐憫你們、弱雞蛛狂族。 趁我方改變心意之前、快滾。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #93 · `slay_by_thousands` · 🔴 semantic/voice divergence (sim=0.60)

**English**:
```
Your greed for lives seals your doom. We will slay you by the thousands!
```

**Shipped v0.4**:
```
你們對生命的貪婪封印了自己的死。 我方會屠你們千萬！
```

**Rebuild v3**:
```
你們對性命的貪婪、註定了你們的毀滅。 我方將以千計、屠盡你們！
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #94 · `ease_up` · 🟡 micro adjust (sim=0.92)

**English**:
```
We mean you no harm; relax.
```

**Shipped v0.4**:
```
我方無意傷害你們;放輕鬆。
```

**Rebuild v3**:
```
我方無意傷害你們；放輕鬆。
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #95 · `bye_space` · 🟠 rewording (sim=0.72)

**English**:
```
Well, I'd love to chat, but I have to go.
```

**Shipped v0.4**:
```
嗯，很想聊，但我得走了。
```

**Rebuild v3**:
```
唉、我很想聊、但我得走了。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #96 · `bye_homeworld` · 🔴 semantic/voice divergence (sim=0.53)

**English**:
```
Goodbye, adios, ciao!
```

**Shipped v0.4**:
```
再見，掰掰，chao！
```

**Rebuild v3**:
```
再見、掰囉、掰！
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #97 · `want_info_on_gods` · 🟠 rewording (sim=0.64)

**English**:
```
Your gods fascinate us. Can you reveal their true nature?
```

**Shipped v0.4**:
```
你等眾神引起我方興趣。 你能揭示他們的真面目嗎？
```

**Rebuild v3**:
```
你們的神明令我方著迷。 你們能揭示他們的真正本質嗎？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #98 · `when_start_worship` · 🟠 rewording (sim=0.69)

**English**:
```
When did you begin your devout ways?
```

**Shipped v0.4**:
```
你們何時開始這虔誠之路？
```

**Rebuild v3**:
```
你們是什麼時候開始這些虔誠之道的？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #99 · `any_good_gods` · 🟠 rewording (sim=0.72)

**English**:
```
I don't want to offend, but did you ever have any Good Gods?
```

**Shipped v0.4**:
```
我不想冒犯，但你們曾經有過善神嗎？
```

**Rebuild v3**:
```
我無意冒犯、但你們曾經有過任何良善的神明嗎？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #100 · `how_talk_with_gods` · 🟠 rewording (sim=0.74)

**English**:
```
How do you pray and how do Dogar and Kazon answer?
```

**Shipped v0.4**:
```
你們怎麼祈禱、多加與卡宗又是怎麼回應的？
```

**Rebuild v3**:
```
你們如何祈禱、多加與卡宗又如何回應？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #101 · `why_44` · ✨ canonical upgrade

**English**:
```
Why do your Gods broadcast on channel 44?
```

**Shipped v0.4**:
```
你等眾神為什麼要在第 44 頻道廣播？
```

**Rebuild v3**:
```
你們的眾神為什麼要在 44 號頻道播送？
```

**推薦**: **B** (v3) — canonical 升級（Q&A 決策已鎖定）

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #102 · `want_info_on_ilwrath` · 🟠 rewording (sim=0.84)

**English**:
```
You Ilwrath fascinate me. Tell me about yourselves.
```

**Shipped v0.4**:
```
你們蛛狂族真是迷人。 說說你們自己吧。
```

**Rebuild v3**:
```
你們蛛狂族令我著迷。 說說你們自己吧。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #103 · `what_about_physio` · 🟠 rewording (sim=0.65)

**English**:
```
Boy, I have to say, you are the strangest looking critters.
```

**Shipped v0.4**:
```
老天，我不得不說，你們真是我見過最古怪的生物。
```

**Rebuild v3**:
```
唉呦、老實說、你們是我見過最奇怪的生物。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #104 · `what_about_history` · 🟡 micro adjust (sim=0.92)

**English**:
```
How did you get so scr... er, end up like you are?
```

**Shipped v0.4**:
```
你們是怎麼變得這麼扭…… 呃，變成現在這副德性的？
```

**Rebuild v3**:
```
你們是怎麼變得這麼糟…… 呃、變成現在這副德性的？
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #105 · `what_about_culture` · 🟠 rewording (sim=0.84)

**English**:
```
Tell me about your fascinating customs and ceremonies.
```

**Shipped v0.4**:
```
跟我說說你們迷人的習俗與儀式。
```

**Rebuild v3**:
```
跟我說說你們迷人的風俗與儀典吧。
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #106 · `what_about_urquan` · 🔴 semantic/voice divergence (sim=0.43)

**English**:
```
So, what do you think of the Ur-Quan anyway?
```

**Shipped v0.4**:
```
你們對烏寬族有什麼看法？
```

**Rebuild v3**:
```
所以說、你們到底怎麼看烏寬族的？
```

**推薦**: 逐項審視 — 語意/voice 差異大，需檢查是否有理由歧異

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #107 · `are_you_evil` · 🟠 rewording (sim=0.76)

**English**:
```
Okay, so help me understand this. You consider yourselves Evil?
```

**Shipped v0.4**:
```
好，讓我搞懂。 你們自認為是邪惡的？
```

**Rebuild v3**:
```
好、幫我搞懂這件事。 你們自認為邪惡？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #108 · `but_evil_is_defined` · 🟠 rewording (sim=0.82)

**English**:
```
But `evil' is defined as deviation from established values.  If your entire society behaves evilly, then aren't you all, in fact, good?
```

**Shipped v0.4**:
```
但『邪惡』的定義是偏離既定價值。 若你等整個社會都邪惡地行事，那你們豈不是全都是善的？
```

**Rebuild v3**:
```
但「邪惡」的定義是偏離既定價值。 若你們整個社會行的都是邪惡之事、你們豈不是全都是良善的？
```

**推薦**: **B** (v3) — 文言清理 + Q12/Q13 icon 貫徹 + Q3/Q4 貶稱 palette · 依 Q&A 決策

**選擇**: A (shipped) / B (v3) / C (自訂)

---

### #109 · `gtfo` · 🟡 micro adjust (sim=0.91)

**English**:
```
THE GREAT DOGAR AND KAZON ORDER YOU TO LEAVE THIS STAR SYSTEM AT ONCE!
```

**Shipped v0.4**:
```
偉大的多加與卡宗命令你們立刻離開此星系！
```

**Rebuild v3**:
```
【偉大的多加與卡宗、命令你們、立刻離開此星系！】
```

**推薦**: **B** (v3) — 微調 wenyan → 現代白話 · 語意等價

**選擇**: A (shipped) / B (v3) / C (自訂)

---
