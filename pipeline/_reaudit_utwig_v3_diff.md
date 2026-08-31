# Utwig Rebuild-Compare v3 Diff Report (2026-08-15)

**Trigger**: `StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md` v3 pass
**Reason**: `02_Races/Utwig.md` §四 v0.7 (2026-08-15) 重大修訂 — 舊「莎士比亞式悲劇詠嘆調」廢止,改為「現代學者式憂鬱華麗長句 + 官僚報告體 + 冷式反諷」。
**Compare target**: `utwig.zh-TW.v0.6-mixed.bak` (shipped 混合版)
**Rebuild artifact**: `utwig.zh-TW.v3.json`

## 統計

- Total tokens: 114
- 🟢 完全相同: 4 (3.5%)
- 🟡 微調 (等價): 0 (0.0%)
- 🟠 措辭改變: 56 (49.1%)
- 🔴 語意/voice 差異大: 52 (45.6%)
- ✨ v0.7 canonical 升級: 2 (1.8%)

**變更幅度**: 96.5% (預期 82%+ 因語體整體翻轉)

## v0.7 語體翻轉核心變化

| 面向 | v0.6 shipped (混合莎士比亞/mixed) | v3 clean-room (現代學者式) |
|---|---|---|
| 自稱 | 吾 / 吾等 / 本族 (文言) | 我方 / 我們憂特 / 憂特 (現代) |
| 對玩家 | 爾 / 爾等 (文言) | 你 / 你們 / 艦長 (現代) |
| 句法 | 之 / 乃 / 者 / 哉 密集 | 現代長句 + 委員會官樣 |
| 感嘆詞 | Oh, woe! = 悲夫! (文言) | Oh, woe! = 痛哉! (與 Alas! 併合 v0.7) |
| 兩長面具 | 勞苦但必需之活動之面具 / 狂野歡欣與狂喜跳躍之面具 | 必需辛勞事務面具 / 狂喜歡騰彈跳面具 (>10 字重譯) |
| **保留** | Q1-Q7 canonical + 13 短面具 + 7 self-address + 4 訪客稱呼 | 完全承襲 shipped |

## 批次接受選項

使用者可回覆:

- **🟢 全採 v3** — 一次接受所有 v3 clean-room 重譯 (推薦, 因語體整體翻轉)
- **🔴 逐項挑** — 對 🔴 級別差異逐項回覆 A/B/C
- **🟠 全 shipped** — 拒絕 v3, 保留 v0.6-mixed (等於放棄 v0.7 dossier 更新)
- **✨ 只採 canonical 升級** — 只採 ✨ 標記的 canonical 升級,其他保留 shipped (保守選項)
- **混合**: e.g. `🟢 除 #23=A / #45=C(...)`

---

## 差異項 (只列 🟡🟠🔴✨,不列 🟢) — 共 110 tokens

### #1 · `NEUTRAL_SPACE_HELLO_1` · 🔴

**英文原文**:
```
Ugh. I suppose, as a courtesy, I should extend an appropriate greeting.
On behalf of the Utwig Proctors I truly hope, for your sake
that your day has been better than ours
although this really isn't saying that much.
```

**Shipped v0.6-mixed**:
```
唉。 想來，出於禮儀，本族應當向仁慈的星際旅人致以合宜之問候。
代表憂特監督者，吾衷心期盼，為爾之故
爾今日之光陰能勝過吾等
儘管此願實在說不上什麼。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
唉。 想來,出於禮貌,本監督團應向仁慈的星際旅人給予一個適當的問候。
代表憂特監督者,本代表衷心希望,看在你的份上,
你今天過得比我們好一些──
儘管這個祈願實在說不上什麼分量。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #2 · `NEUTRAL_SPACE_HELLO_2` · 🔴

**英文原文**:
```
Just go away. Leave us to ponder our grief.
```

**Shipped v0.6-mixed**:
```
走吧。 讓吾等自沉哀思。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
走吧。 讓我獨自沉思這份哀傷。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #3 · `HOSTILE_SPACE_HELLO_1` · 🔴

**英文原文**:
```
Yagh! Your attitude toward us is not acceptable!
We apologize for having to deal with you this way,
but since the loss of the Ultron, we have no choice.
As we prepare to die, so should you.
```

**Shipped v0.6-mixed**:
```
呀哈！（Yagh!） 爾對吾等之態度不可容忍！
吾等對必須以此方式對待爾深感抱歉，
然自厄創失落以來，吾等別無選擇。
吾等既將赴死，爾亦當如是。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
呀哈！（Yagh!） 你對本族的態度令人無法接受！
我們對於必須以這種方式應對你深表歉意，
然而自從失去厄創以來，本族別無選擇。
我們既已準備就義，你也理當如此。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #4 · `HOSTILE_SPACE_HELLO_2` · 🔴

**英文原文**:
```
You have caught us in a private, dark moment.
We must guarantee your silence with your complete and total destruction.
```

**Shipped v0.6-mixed**:
```
爾於吾等私密之黑暗時刻闖入。
吾等必須以爾之完全徹底之毀滅來確保爾之緘默。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你在本族私密的黑暗時刻撞見了我們憂特。
我方必須以你徹底而全面的毀滅，來確保你的緘默。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #5 · `BOMB_WORLD_HELLO_1` · 🟠

**英文原文**:
```
Attention alien vessel: this world is under the full jurisdiction of the Utwig Proctorate.
We extend a subdued but civil greeting.
```

**Shipped v0.6-mixed**:
```
注意，外星艦艇：此世界完全處於憂特監督團之管轄下。
吾等向仁慈的星際旅人致以壓抑卻有禮之問候。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
注意，外星艦艇:此世界完全處於憂特監督團的管轄之下。
本監督團向仁慈的星際旅人獻上一個克制但仍不失禮貌的問候。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #6 · `BOMB_WORLD_HELLO_2` · 🔴

**英文原文**:
```
You have arrived at a most inopportune time.
Collectively, our species is dealing with a great remorse.
Nevertheless in order to foster a spirit of interspecies good will
we pull ourselves from our intense cycle of self-analysis
and offer this greeting which, we hope, will suffice.
```

**Shipped v0.6-mixed**:
```
爾於最不宜之時刻蒞臨。
吾族集體正處於巨大悔恨之中。
然為增進種族間之善意
吾等自濃烈之自省循環中抽身
並致以此問候，期能勉強應酬。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你在最不宜的時刻蒞臨。
我們憂特整體正處於一場巨大的悔恨之中。
然而，為了培養跨種族善意的氛圍，
本族從強烈的自我反省循環中暫時抽身，
獻上這個問候，希望這樣就足夠了。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #7 · `HOSTILE_BOMB_HELLO_1` · 🔴

**英文原文**:
```
Oh, woe! We find your presence here disconcerting.
In order to deal with the situation in such a way that we maintain some semblance of authority
we are forced to deploy our forces against your armada.
Prepare yourselves for battle.
```

**Shipped v0.6-mixed**:
```
喔，痛哉！（Oh, woe!） 吾等發覺爾之存在令人不安。
為維持一絲權威之表象處理此情況
吾等不得不部署武力對付爾之艦隊。
爾等，準備戰鬥。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
痛哉！（Oh, woe!） 本族覺得你在此的出現令人不安。
為了在應對此局面的同時仍能維持一絲權威的表象，
我們不得不動員武力對抗你的艦隊。
你們，請為戰鬥做好準備。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #8 · `HOSTILE_BOMB_HELLO_2` · 🔴

**英文原文**:
```
In a fit of depression I find it necessary to vent my irreconcilable frustration on you.
I normally do not engage in such fervent activities
but I now find myself inspired to do my best to annihilate you with expediency.
```

**Shipped v0.6-mixed**:
```
於憂鬱之發作中，本族發覺必須將無法排解之挫敗發洩於爾。
本族一般不從事此等激烈活動
然本族此刻竟感靈感湧現，盡力迅速將爾殲滅。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
在一次憂鬱的發作中，我認為有必要將這股無可調解的挫折感發洩到你身上。
我平日並不從事這類激烈的活動，
然而此刻卻感到靈感湧現，將竭盡全力盡速將你殲滅。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #9 · `NEUTRAL_HOMEWORLD_HELLO_1` · 🟠

**英文原文**:
```
Normally we would not bother to acknowledge your presence
but you find us in a state of moderate depression
instead of our normal cycle of self-destructive tendencies.
```

**Shipped v0.6-mixed**:
```
平日吾等不會費心承認爾之存在
然爾此時遇上悲慘的憂特正處中度憂鬱之狀
而非吾等常態之自毀循環。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
平日本族不會費心承認你的存在，
然而你此時碰上悲慘的憂特族正處於中度憂鬱的狀態，
而非我們一貫的自毀傾向循環之中。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #10 · `NEUTRAL_HOMEWORLD_HELLO_2` · 🟠

**英文原文**:
```
Alien vessel, grieve for the loss of both the Utwig and the Universe at large.
```

**Shipped v0.6-mixed**:
```
外星艦艇，為失落的憂特與寰宇整體之失落，一同哀悼吧。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
外星艦艇，請為失落的憂特與整個寰宇的失落一同哀悼吧。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #11 · `NEUTRAL_HOMEWORLD_HELLO_3` · 🔴

**英文原文**:
```
You disturb our routine of eternal grieving
yet we extend to you the courtesy of acknowledgment.
```

**Shipped v0.6-mixed**:
```
爾擾亂了吾等永恆哀悼之常軌
然吾等仍以承認爾之禮儀致意。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你擾亂了本族永恆哀悼的例行程序，
然而我們仍以承認你存在這樣的禮貌相待。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #12 · `NEUTRAL_HOMEWORLD_HELLO_4` · 🔴

**英文原文**:
```
I am so depressed. You can try to cheer me up if you want to.
```

**Shipped v0.6-mixed**:
```
本族好憂鬱。 若爾願，可試著讓本族振作。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我非常憂鬱。 你若願意，可以試著讓我振作起來。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #13 · `HOSTILE_HOMEWORLD_HELLO_1` · 🟠

**英文原文**:
```
You have angered the spirit of the Utwig.
Although depressed almost to the point of an inability to perform any actions whatsoever
we find within ourselves the verve required to engage you in a duel to the death.
Indeed, we will find satisfaction in your demise or in our release from our mortal burden.
```

**Shipped v0.6-mixed**:
```
爾已激怒罪惡的戴面具者之靈魂。
儘管吾等憂鬱幾近無法採取任何行動之地步
仍於自身尋得與爾一決生死所需之熱忱。
誠然，吾等將於爾之殞歿中尋得滿足，或於自身凡塵重擔之解脫中尋得滿足。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你已激怒罪惡的戴面具者之魂靈。
儘管本族憂鬱到幾乎無法採取任何行動的地步，
仍在自身之中找到了與你進行生死決鬥所需的熱忱。
誠然，我們將在你的殞歿之中尋得滿足，或在自身凡塵重擔的解脫之中尋得滿足。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #14 · `HOSTILE_HOMEWORLD_HELLO_2` · 🔴

**英文原文**:
```
Attention offending vessel! Your presence here is deeply appreciated!
You have stirred us from our depression-induced apathy
to the point where our desire actually registers as a sensation!
We look forward to either finding personal release in the netherworld
or obliterating you successfully.
We thank you for this opportunity!
```

**Shipped v0.6-mixed**:
```
注意，冒犯之艦艇！ 爾於此之存在深受吾等感激！
爾將吾等自憂鬱誘發之冷漠中喚醒
以致吾等之慾望竟真正登記為感覺！
吾等期待或於冥界之個人解脫
或成功將爾殲滅。
吾等感謝爾此一機會！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
注意，冒犯之艦艇！ 你在此的出現令本族深深感激！
你已將我們從憂鬱誘發的淡漠中喚醒，
以致我們的意欲竟然真的化為一種知覺！
本族期盼在冥府之中尋得個人的解脫，
或成功將你盡數殲滅。
我們感謝你賜予此一機遇！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #15 · `why_you_here` · 🔴

**英文原文**:
```
For what purpose do you linger at this location?
```

**Shipped v0.6-mixed**:
```
爾等因何目的滯留於此地？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你們為何滯留在此處？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #16 · `WE_GUARD_BOMB` · 🟠

**英文原文**:
```
We are the stewards of the Bomb.
We keep it from those who would use it unwisely.
In addition, we are prepared to act under the direction of the Proctorate
should we decide to make a final atonement for our most grievous blunder.
```

**Shipped v0.6-mixed**:
```
吾等哀嘆之族，為此炸彈之守護者。
吾等保其遠離不智使用之徒。
此外，吾等預備隨時聽從監督團之指示行動
倘若吾等決意為此極其嚴重之過錯作最終之贖罪。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我們憂特是這顆炸彈的守護者。
本族保護它，遠離那些會不明智使用它的人。
除此之外，我們已預備隨時聽從監督團的指示行動,
倘若本族決意為自身最嚴重的過失作最終的贖罪。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #17 · `what_about_bomb` · 🔴

**英文原文**:
```
Hmm, this must be a pretty special Bomb to have all of you keeping an eye on it.
```

**Shipped v0.6-mixed**:
```
唔，這一定是顆挺特別的「炸彈」，才會需要你們全部盯著。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嗯,這炸彈想必挺特別,能讓你們一群人都盯著它。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #18 · `ABOUT_BOMB` · 🔴

**英文原文**:
```
You are correct. It is a relic of Precursor origin.
It has the power to destroy entire planetary objects, perhaps even galaxies.
The Utwig have been entrusted by fate to watch over this device
so that it will be used in the way that it was intended by destiny.
```

**Shipped v0.6-mixed**:
```
爾所言不虛。 其乃先驅者起源之遺物。
其擁有摧毀整個行星，甚至或許整個星系之力量。
憂特由命運所託，守護此裝置
以確保其將依命運所安排之方式使用。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你所言正確。 它是先驅者血脈的遺物。
它的力量足以摧毀完整的行星體,甚至可能摧毀整個星系。
命運將此裝置託付給我們憂特看管,
以確保它能按天命所安排的方式被使用。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #19 · `give_us_bomb_or_die` · 🟠

**英文原文**:
```
We have an urgent need for this device. Give us the Bomb.
```

**Shipped v0.6-mixed**:
```
我方對此裝置有緊急需求。 把「炸彈」交出來。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方急需此裝置。 把炸彈交出來。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #20 · `GUARDS_WARN` · 🔴

**英文原文**:
```
We cannot relinquish control of this instrument of power!
You cannot have the Bomb.
Any attempt on your part to change this current arrangement
will be met with fearsome Utwig resistance!
```

**Shipped v0.6-mixed**:
```
吾等不可放棄對此力量工具之控制！
爾不可持有「炸彈」。
爾之任何試圖改變此現狀之嘗試
將遭遇令人畏懼之憂特抵抗！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族無法放棄對此力量之器的掌控！
你不能擁有這顆炸彈。
你若有任何企圖想改變當前的安排,
將遭遇憂特可怖的抵抗！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #21 · `demand_bomb` · 🟠

**英文原文**:
```
We will now take the Bomb. Give it to us.
```

**Shipped v0.6-mixed**:
```
我方現在就要拿走「炸彈」。 交出來。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方這就要取走炸彈。 交出來。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #22 · `GUARDS_FIGHT` · 🔴

**英文原文**:
```
Our anguish serves only to fuel our resolve concerning the jurisdiction of this device.
We stand ready!
```

**Shipped v0.6-mixed**:
```
吾等之痛楚僅為吾等對此裝置管轄權之決心添薪。
吾等已備戰！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族的苦痛只會強化我們對此裝置管轄權的決心。
我方已然備妥！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #23 · `may_we_have_bomb` · 🔴

**英文原文**:
```
Wow, that is pretty neat! May we have the Bomb?
```

**Shipped v0.6-mixed**:
```
哇，這可挺酷的！ 我方能拿「炸彈」嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
哇,那還挺酷的！ 我方可以擁有那顆炸彈嗎？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #24 · `NO_BOMB` · 🔴

**英文原文**:
```
Yes, it IS a remarkable device.
It is understandable that you would like to possess it yourselves.
Our mandate, however, requires that we maintain full control of the Bomb.
```

**Shipped v0.6-mixed**:
```
是的，此裝置著實非凡。
爾等欲親自擁有之，此亦可理解。
然吾等之使命，要求吾等維持對炸彈之完全掌控。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
是的,它確實是一件非凡的裝置。
你們想要親自擁有它,這也是可以理解的。
然而,本族的職責要求我們必須維持對這顆炸彈的完全掌控。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #25 · `please` · 🔴

**英文原文**:
```
Oh, please can't we have it? It would make us really happy!
```

**Shipped v0.6-mixed**:
```
喔，拜託咱們能不能拿？ 那可讓我方超開心！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
噢,拜託嘛,讓我方擁有它不行嗎？ 我方會超開心的！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #26 · `SORRY_NO_BOMB` · 🔴

**英文原文**:
```
No, we are sorry. You cannot have the Bomb.
Besides being against our orders, imagine what would happen if for some reason
our Proctors decide to use it to destroy our civilization.
How would we explain its absence?
```

**Shipped v0.6-mixed**:
```
不行，吾等抱歉。 爾不可持有「炸彈」。
且此不僅違反吾等之令，試想若因某故
吾等監督者決意用之毀滅吾等自身之文明。
吾等該如何解釋其缺席？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
不,本族深感抱歉。 你不能擁有這顆炸彈。
除了違反命令之外,試想若我們的監督者出於某種原因
決意以它摧毀我們憂特的文明,
本族又該如何解釋炸彈的下落？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #27 · `whats_up_bomb` · 🔴

**英文原文**:
```
Tell us about the Bomb. What's the scoop?
```

**Shipped v0.6-mixed**:
```
跟我方講講「炸彈」吧。 內幕如何？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
說說這炸彈吧。 有什麼內情？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #28 · `GENERAL_INFO_BOMB_1` · 🟠

**英文原文**:
```
During standard exploration procedures we came across what appeared to be
an ancient Precursor supply base.
It had been dismantled and appeared to be empty.
In the staging area there was a collection of what appeared to be refuse.
During the cataloging of these various items, this device was discovered in a damaged container.
From what our scientists can tell, it appears to be a planeteering tool
capable of reducing moon-sized objects to particulate dust clouds.
We believe that it was either accidentally forgotten
or simply left because of a lack of room on the departing vessel.
```

**Shipped v0.6-mixed**:
```
於例行探勘程序中，吾等遇見一處疑似
古先驅者補給基地之地。
其已被拆解，看似空無一物。
於整備區有一批看似廢棄物之聚集。
於編目各項時，此裝置於一破損容器中被發現。
據吾等科學家所能判斷，其似為一星體工程器（planeteering tool）
足以將月球尺寸之物體化為顆粒塵埃雲。
吾等相信其或係意外遺忘
或僅因離場艦艇艙位不足而遭遺留。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
在一次例行的探勘程序中,本族遇見一處疑似
古先驅者補給基地的地方。
它已被拆解,看起來空無一物。
在整備區有一堆看似廢棄物的聚集品。
當我們在對各項物品進行編目時,此裝置在一破損的容器中被發現。
根據我方科學家所能判斷,它看似為一件星體工程器(planeteering tool),
足以將月球尺寸的物體化為顆粒狀的塵埃雲。
本族相信它或許是意外被遺忘,
又或者僅是因離場艦艇艙位不足而被留下。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #29 · `GENERAL_INFO_BOMB_2` · 🔴

**英文原文**:
```
The Bomb may have been left here by mistake.
We suspect that if activated, it will turn this entire planet
into nothing more than an expanding mass of tiny dirt clods.
The Utwig have considered carefully that perhaps it would be best to use this device
to put us out of our collective misery.
Although this may sound extreme, I will point out that our mishandling of the Ultron
is a disaster of epic proportions.
```

**Shipped v0.6-mixed**:
```
此「炸彈」或為錯留於此。
吾等猜測若啟動之，其將把此整個行星
化為不過是一團擴散之塵屑。
憂特已仔細考慮，或許以此裝置
終結吾等之集體苦難乃最佳之選。
儘管此聞來或極端，本族要指出
吾等對厄創之失手乃史詩級之災難。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
這顆炸彈可能是被誤留於此。
本族猜想,若將它啟動,它會將這整顆行星
化為一團不斷擴散的微小土塊。
我們憂特已仔細考慮過,或許最好的做法是以此裝置
將我們從集體的悲苦中解脫。
儘管這聽起來很極端,我仍要指出:本族對厄創的疏失處理
是一場史詩級規模的災難。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #30 · `bye_bomb` · 🔴

**英文原文**:
```
This Bomb is pretty dangerous and you guys are crazy. I'm getting out of here!
```

**Shipped v0.6-mixed**:
```
這「炸彈」蠻危險的，你們也怪怪的。 我方要離開了！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
這炸彈挺危險的,而且你們一夥都瘋了。 我方閃了！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #31 · `GOODBYE_BOMB` · 🔴

**英文原文**:
```
Ha ha, don't worry. Hey! I laughed! How could I do that?
Now I sink into a depression that leaves me speechless.
```

**Shipped v0.6-mixed**:
```
哈哈，別擔心。 喂！ 本族笑了！ 本族怎能如此？
如今本族沉入令我無語之憂鬱。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
哈哈,別擔心。 咦！ 我笑了！ 我怎麼可能笑得出來？
現在我陷入一種令我無語的憂鬱狀態。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #32 · `hey_wait_got_ultron` · 🔴

**英文原文**:
```
Whoa there, hold your horses! Look at this! We've got your Ultron!
```

**Shipped v0.6-mixed**:
```
喔喂，等一下！ 看這個！ 我方帶著爾等的厄創來了！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
喔喔,先別急！ 看這個！ 我方手上有你們的厄創！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #33 · `TAUNT_US_BUT_WE_LOOK` · 🔴

**英文原文**:
```
Taunting us buys you nothing except to steel our resolve to end your existence.
In fact, we will humor you in your little game.
You have seconds to show us whatever bric-a-brac you possess.
We will then commence with the cessation of your existence.
```

**Shipped v0.6-mixed**:
```
嘲笑吾等除了堅定吾等終結爾存在之決心外，別無所獲。
事實上，吾等將姑息爾之小遊戲。
爾有數秒展示爾所擁有之任何無足輕重之物。
然後吾等將開始爾之終結。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嘲弄本族對你毫無益處,只會強化我們終結你存在的決心。
事實上,我方會奉陪一下你這個小把戲。
你有幾秒鐘的時間出示你手上任何雜貨。
之後本族便會開始終結你的存在。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #34 · `TRICKED_US_1` · 🔴

**英文原文**:
```
I expected no less.
You hold before us nothing more than a reminder of a past mistake that offends us to no end.
We now commence your termination.
```

**Shipped v0.6-mixed**:
```
本族並不意外。
爾於吾等面前所持之物，不過是一段過去錯誤之無盡冒犯之提醒。
吾等現在開始爾之終結。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我也料想不到別的了。
你在本族面前所持之物,不過是一項令我無比反感的過往錯誤的提醒物。
本族現在開始終結你的存在。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #35 · `TRICKED_US_2` · 🔴

**英文原文**:
```
I am speechless with rage... and yet, I must speak!
How dare you flaunt the collective embarrassment of the Utwig?!
You will now pay for your severe breach of etiquette!
```

**Shipped v0.6-mixed**:
```
本族氣得語塞…… 然本族必須說話！
爾竟敢炫耀憂特之集體恥辱？！
爾將為爾嚴重違反禮儀付出代價！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我憤怒到說不出話……然而,我必須開口！
你竟敢炫耀我們憂特的集體難堪？！
你現在就得為這嚴重的禮儀違犯付出代價！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #36 · `we_are_vindicator` · 🟠

**英文原文**:
```
This is Captain <% state.sis.getCaptainName() %>, representing <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>. Please respond.
```

**Shipped v0.6-mixed**:
```
我是 <% state.sis.getCaptainName() %> 艦長，代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>。 請回應。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方為 <% state.sis.getCaptainName() %> 艦長,代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>。 請回應。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #37 · `WOULD_BE_HAPPY_BUT` · 🔴

**英文原文**:
```
What good would that do -- I mean, why should we?
We agonized for hours wondering if it was a cruel twist of fate
or simply a serious case of butterfingery.
Ah, the lifetimes that have been spent in the pursuit of the elusive answer
to this deceptively simple question has driven many of us down the dark road of self-destruction.
Indeed, even as these words strike the ears of any who care to listen
the real question is, Does It Matter? I cannot say, I wallow in a quandary
unable to determine what better atones for my part of the Great Sin.
Should I engage in slow and painful self-termination?
Should I commit myself to a long life of painful self-flagellation?
Should I throw myself with enthusiastic verve at the problem of collective annihilation?
I do not know. Even now my mind writhes in anguish of indecision, lest the outcome be inadequate.
```

**Shipped v0.6-mixed**:
```
此有何用 —— 本族之意，吾等何必？
吾等已煎熬數小時，苦思是命運之殘酷捉弄
抑或僅是一場嚴重之笨手指事件。
啊，追尋此看似簡單之提問之難捉之解答
已耗盡多少一生 —— 引無數同族步入自毀之黑暗大道。
確實，即使此語擊中任何願聽者之耳
真正之問題是：這重要嗎？ 本族無法斷言，本族深陷於困境之中
無法決定何者更能贖回本族於「大罪」之份。
本族該從事緩慢而痛苦之自我終結？
本族該獻身於漫長之自我鞭笞人生？
本族該以熱切之勁力投身於集體毀滅之議題？
本族不知。 即使此刻，本族之心於猶豫之痛楚中扭動，唯恐結果不夠適切。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
那樣做又有何益──我是說,本族為何應該？
我煎熬了數小時,反覆思考那究竟是命運的殘酷扭轉,
還是單純一場嚴重的失手案例。
唉,多少生命耗在追尋這個看似簡單、實則難解的問題之上,
而追尋這個難以捉摸的答案,已將我們憂特之中許多人推上自毀的黑暗道路。
誠然,即便此刻這些話語傳入任何願意傾聽者的耳中,
真正的問題卻是:這重要嗎？ 我無法作答,我沉溺於一個困境,
無法判斷什麼才能更妥善地為我在那場大罪中所扮的角色贖罪。
我是否應從事緩慢而痛苦的自我終結？
我是否應將自己託付予一場漫長而苦痛的自我鞭笞？
我是否應以熱切的衝勁投身於集體毀滅的課題？
我不知。 即便此刻,我的心智仍在猶豫不決的煎熬中扭動,唯恐結果不敷所需。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #38 · `why_sad` · 🔴

**英文原文**:
```
Hmm, I detect that recent events have not gone your way. Why don't you start at the beginning?
```

**Shipped v0.6-mixed**:
```
唔，我方察覺最近發生的事對你們不太順利。 何不從頭說起？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嗯,我方察覺到近來的事件並不如你們所願。 為何不從頭說起？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #39 · `ULTRON_BROKE` · 🔴

**英文原文**:
```
*Sigh* All right, I'll try, but you know, it really doesn't matter.
After all, we have a famous Utwig saying: when one loses the reason for existence
one tends to get less motivated.
This goes hand-in-hand with the painfully appropriate credo
`We broke it so we are paying for it'.
Of course, this isn't really accurate; the situation is so much more hideous!
Imagine, if you can, holding within your hands The Answer!...
...only to have it taunt you with its former potential!
Ah, cruel irony! The loss of the Ultron grieves us all!
```

**Shipped v0.6-mixed**:
```
（嘆氣）好吧，本族試試看，但爾知道，這根本無關緊要。
畢竟，吾等有一句著名之憂特諺語：當一族失去存在之理由
其往往變得較無動力。
此與那句令人痛心之貼切信條並肩：
『吾等打壞了，所以吾等付出代價』。
當然，此並不真正準確；情況更為可怕！
試想，若爾能，於爾手中握有「答案」！……
……卻只能被其昔日之潛力嘲笑！
啊，殘酷之諷刺！ 厄創之失落令吾等所有人悲痛！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
*嘆息*(*Sigh*) 好吧,我會試著說,然而你知道,這其實根本不重要。
畢竟,我們憂特有一句著名的諺語:當一個人失去存在的理由時,
他往往會變得較無動力。
這與那句令人痛苦地貼切的信條並行呼應──
「我們打破了它,所以我們正為它付出代價」。
當然,這其實並不精確;實情要遠比這醜惡得多！
試想,若你能想像,將「答案」握於雙手之中！……
……卻只能任它以其昔日的潛能嘲弄你！
唉,殘酷的反諷！ 厄創的失落令我們所有人為之悲慟！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #40 · `what_ultron` · 🟠

**英文原文**:
```
Um, yes, of course, the Ultron. We grieve. How sad. Now, what was it again?
```

**Shipped v0.6-mixed**:
```
呃，是的，當然，厄創。 我方為你們哀悼。 多悲傷。 那，它到底是什麼來著？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
呃,是啊,當然是厄創啦。 我方哀悼,好悲傷。 那麼,它到底是什麼來著？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #41 · `GLORIOUS_ULTRON` · 🔴

**英文原文**:
```
Bah! It doesn't matter! Besides being of no concern to you
I find discussion of this matter, well, distasteful.
*Sigh.* The Ultron was not only the thing which assures total and complete meaning of life for you and I
it is Universal; I'm sure that you too are aware of this thing if only in legend!
It granted us all limitless power and knowledge.
It has been since, well, rendered inoperative.
```

**Shipped v0.6-mixed**:
```
呸！（Bah!） 這無關緊要！ 除了與爾無關之外
本族發現討論此事，嗯，令人不快。
（嘆氣。）厄創不僅是為爾我確保生命完全徹底之意義之物
其更是「宇宙的」；本族確信爾對此物即使只從傳說中亦有所聞！
其賜予吾等所有無限之力量與知識。
它自從……嗯，已然失效。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
呸！（Bah!） 這無關緊要！ 除了與你無關之外,
我覺得討論這個議題,嗯,令人不悅。
*嘆息*。 厄創不僅是那項確保你我生命全然而完整意義之物──
它是宇宙性的;我確信你也知曉此物,即便只是聽聞傳說！
它賜予我們所有人無邊的力量與知識。
從那時起,嗯,它便失去了功能。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #42 · `dont_be_babies` · 🔴

**英文原文**:
```
Just because you busted your Ultra-thingy, don't be a bunch of cry-babies!
```

**Shipped v0.6-mixed**:
```
只不過弄壞了你們的厄玩意兒，別當一群哭啼的娃兒！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
只不過弄壞了你們的厄創之物,別搞得像一群愛哭鬼似的！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #43 · `MOCK_OUR_PAIN` · 🔴

**英文原文**:
```
Gah! Now you've really done it!
Your blatant transgressions have me hopping mad!
Hop hop hop! Okay, that's it! Put up your dukes! Nobody makes fun of the Ultron!
```

**Shipped v0.6-mixed**:
```
哈！（Gah!） 爾這下可真惹到本族了！
爾之公然冒犯讓本族火冒三丈！
跳跳跳！ 好，就這樣！ 拿起拳頭來！ 沒人可以嘲笑厄創！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嘎！（Gah!） 這下你可真的做到了！
你這公然的冒犯讓我氣得跳腳！
跳、跳、跳！ 好,就這樣！ 舉起你的拳頭！ 沒人可以取笑厄創！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #44 · `real_sorry_about_ultron` · 🟠

**英文原文**:
```
Sniff. That reminds me when my pet dog Splib ran in front of a... rock chipper!
```

**Shipped v0.6-mixed**:
```
哭。 那讓我方想起我方的寵物狗小普利（Splib）跑到一台…… 石頭切碎機前面！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
抽泣。（Sniff.） 這讓我方想起我方的寵物狗小普利(Splib)衝到一台……碎石機前的往事！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #45 · `APPRECIATE_SYMPATHY` · 🔴

**英文原文**:
```
You are kind. If we could wield the Ultron to resurrect your Splib, we would.
But I suddenly am overcome with waves of depression.
I must retire now to perform rituals of anguish.
Waves of trauma wash across my being even now. I must go.
```

**Shipped v0.6-mixed**:
```
爾真仁慈。 若吾等能揮動厄創使爾之小普利復活，吾等定會如是。
然本族忽然被憂鬱之浪淹沒。
本族此刻須告退，執行痛楚之儀式。
創傷之浪甚至此刻仍衝擊本族之存在。 本族必須走了。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你真是善良。 我若能運用厄創使你的小普利復活,本族一定會做的。
然而我忽然被一波波憂鬱所淹沒。
我現在必須退下,去舉行哀慟的儀式。
即便此刻,創傷的浪潮仍在洗刷我的存在。 我必須離去。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #46 · `what_about_you_1` · 🟠

**英文原文**:
```
A truly unique set of events put you in your current state. Am I right?
```

**Shipped v0.6-mixed**:
```
一連串真正獨特的事件讓你們陷入現在的狀態。 我方沒說錯吧？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
一連串真正獨特的事件將你們帶入現在的狀態。 我方沒說錯吧？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #47 · `ABOUT_US_1` · ✨

**英文原文**:
```
Hah, to say the least!
Our past is one of a glorious and proud people coupled with a cataclysm that rocks the Universe
to its very core!
It all began when the Chimt rose from the Murky Bog and the Utwig emerged as well.
In these primitive times we cavorted about our world oblivious to any sort of higher purpose
we took everything at face value.
Meanwhile, the tendrils of the Chimt infiltrated the vast sky canopies of Fahz and then the veils fell!
Suddenly, the Utwig were stunned by a collective realization!
All immediately and urgently donned veils of every description! Hides, leaves, shells, rocks
even living drells were donned in the early days.
You see, the face is the mechanism that expresses many of the primitive qualities that hinder sentience.
Now rid of constant reminders of greed, rage, hatred, and lust
the wisdom of the Utwig was no longer hampered by constant reminders of the primitive urge.
Over many generations mask etiquette was refined to a rock-solid foundation of our society.
Sure, the Morality Riots were expensive, both in lives and infrastructure
but the result was better mask regulation; specification from your basic Mask of Gruelling but Neccessary Activity
to the most highly decorated Countenance of Stellar Representation. These were clearly defined.
Recognizing the importance of flexibility, clear-cut and efficient procedures for revision and redesign
dealt with the few anomalies.  From that moment when we covered the source of our intellectual oppression
we knew that it was a grand purpose that defined our destiny.
Are you still listening?!
Our entire development as a sentient species was coordinated to coincide with the appearance of a remarkable device
the Ultron!
We were oblivious to its tragic implication.
```

**Shipped v0.6-mixed**:
```
哈，說得含蓄了！
吾等之過往乃一族光榮驕傲之人民，配合一場撼動宇宙
至其核心之大劫難！
一切始於欽特（Chimt）自幽暗沼澤崛起，憂特亦隨之出現。
於此原始時代，吾等於世界上嬉遊，對任何較高之目的懵然無知
吾等對一切僅取表面之義。
與此同時，欽特之觸鬚滲入法茲（Fahz）廣袤之天穹，而後帷幕降下！
剎那間，憂特震撼於一集體之領悟！
眾人立即急迫地披上各式各樣之遮罩！ 皮革、樹葉、貝殼、岩石
早期甚至有活生生之卓爾（Drell）被戴上。
爾當知，臉面乃展現阻礙感知之諸多原始特質之機關。
如今擺脫貪、怒、恨、慾之持續提醒
憂特之智慧不再被原始衝動之持續提醒所阻礙。
歷經多世代之演進，面具禮儀被精煉為吾等社會之磐石根基。
誠然，禮法暴動之代價高昂，於生命與基建皆然
然結果乃更佳之面具規範；由爾基本之「勞苦但必需之活動之面具」（Mask of Gruelling but Necessary Activity）
至裝飾最為華麗之「星辰代表之容貌」（Countenance of Stellar Representation），皆有明確之定義。
承認靈活性之重要，明確而有效率之修訂與重設計程序
處理了少數異常情況。 自吾等遮蔽智識壓迫之源之時刻起
吾等便知，此乃一項界定吾等命運之偉大目的。
爾仍在聽嗎？!
吾等作為有感之族群之整體發展，被安排為與一件非凡裝置之現身同步
此即厄創！
吾等對其悲劇之含意懵然無知。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
哈,這麼說已算輕描淡寫了！
本族的過往是一段輝煌而驕傲的族群故事,與一場撼動宇宙核心的
劫難相伴而生！
一切始於欽特(Chimt)自幽暗沼澤(Murky Bog)中興起,我們憂特也同時浮現。
在那些原始的年代,我們在星球上嬉戲翻騰,對任何更高的目的毫無察覺,
本族對一切都只看表面。
與此同時,欽特的觸鬚滲入了法茲(Fahz)廣袤的天穹,接著,遮蔽物落下了！
突然之間,我們憂特被一項集體性的覺悟所震懾！
所有人立即而迫切地戴上了各式各樣的遮蔽物！ 獸皮、樹葉、貝殼、石頭,
早期甚至還有活生生的卓爾(Drell)被戴上。
你要知道,臉面正是那個表現出諸多阻礙感知的原始特質之機關。
如今擺脫了貪、怒、恨、慾的持續提醒,
我們憂特的智慧不再被原始衝動的持續提醒所阻礙。
歷經多世代的演進,面具禮儀被精煉成本族社會的磐石根基。
誠然,禮法暴動的代價高昂,無論在生命或基建方面皆然,
然而其結果是更佳的面具規範;規格從你基本的「例行辛勞事務面具」(Mask of Gruelling but Necessary Activity)
一直到最華麗裝飾的「星辰代表容貌」(Countenance of Stellar Representation)。 這些都有明確的定義。
承認彈性的重要性,清晰而有效率的修訂與重設計程序,
處理了少數的異常情況。 自本族遮蔽智識壓迫來源的那一刻起,
我便明白:這是一項界定我們命運的宏大目的。
你還在聽嗎？！
憂特一族作為感知物種的整體發展,正好與一件非凡裝置的出現同步協調──
那就是厄創！
我當時對它悲劇性的含意毫無察覺。
```

**Canonical 升級理由**: v0.7 dossier §四 Q_C 決策 — 面具名 >10 字者 clean-room 重譯以貼合現代學者風格。

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #48 · `what_about_you_2` · 🔴

**英文原文**:
```
Yow! Absolutely fascinating. But what exactly do you mean by tragic?
```

**Shipped v0.6-mixed**:
```
呀！ 絕對迷人。 但你方才說的「悲劇性」是什麼意思？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
哇！ 太精彩了。 不過你所說的「悲劇性」究竟是什麼意思？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #49 · `ABOUT_US_2` · 🔴

**英文原文**:
```
In order for you to truly understand the situation, you need to know more about the Ultron
and its unique capabilities.
You see, when the Druuge discovered the Ultron they knew that it was ours.
The Druuge were compelled by intrinsic universal direction to take it to where it has always belonged.
They brought it to us.
Oh, the Ultron!
It assured total and complete meaning of life for All -- the Universal!
With the Ultron in hand I could sense not only your motivations and desires, but your purpose.
I could act upon these things in ways that would most likely seem mysterious if not, well, daft.
Years later, you would herald our participation in your development as the turning point for your species.
The Druuge were only one of the few to benefit in this way.
Even now, they are puzzled by the way we rewarded them for the delivery of the Ultron to its correct place.
In twenty-four years, two months and three days they will all dance the dance of Jubilation.
Indeed, the Ultron has allowed us to fundamentally change the Druuge forever!
The Supox too received many benefits from our use of the Ultron.
They can testify to its power!
```

**Shipped v0.6-mixed**:
```
為使爾真正了解此情境，爾需知曉更多關於厄創
及其獨特能力之事。
爾看，當毒賈族發現厄創時，他們知曉其為吾等所有之物。
毒賈族被內在之宇宙指引所驅使，將其帶往其一向所歸屬之處。
他們將其帶至吾等處。
喔，厄創！
它為所有人 —— 即「宇宙的」—— 確保生命完全徹底之意義！
手持厄創，本族不僅能感應爾之動機與欲望，亦能感應爾之目的。
本族能以那些看似神秘、若非，嗯，愚蠢之方式對此等事物採取行動。
數年後，爾將稱頌吾等於爾發展中之參與，視其為爾一族之轉捩點。
毒賈族僅為以此方式受益之少數之一。
即使此刻，他們對吾等為感謝其將厄創交至正確之處所給予之回報之方式仍感困惑。
於二十四年、兩個月又三日內，他們將全體共舞「歡欣之舞」。
確實，厄創已讓吾等從根本上永久改變了毒賈族！
蘇菩族亦從吾等使用厄創中獲益甚多。
他們可為其力量作證！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
為了讓你能真正理解此一情境,你需要對厄創與其獨特能力
有更多的認識。
你要知道,當毒賈族發現厄創時,他們便知曉它本屬我們憂特。
毒賈族被一種內在的宇宙性指引所驅使,將它帶到它一直以來所歸屬之處。
他們將它帶到了本族面前。
噢,厄創！
它確保了所有存有的生命享有全然而完整的意義──那是宇宙性的！
厄創在手,我不僅能感知你的動機與慾望,還能感知你的目的。
我能對這些事物採取行動,其方式即使不算蠢,也極可能顯得神祕。
數年之後,你將會把我們對你們發展的參與,宣稱為你們物種的轉折點。
毒賈族只是以此方式受益的少數之一。
即便此刻,他們仍對本族為表彰他們將厄創遞送至正確之處所給予的回報方式感到困惑。
在二十四年二個月又三天之後,他們全體將會跳起歡欣之舞。
誠然,厄創使憂特一族得以永久地徹底改變毒賈族！
蘇菩族也從我們對厄創的運用中獲得了諸多益處。
他們能為它的力量作證！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #50 · `what_about_you_3` · 🔴

**英文原文**:
```
Hmm, sounds like things were going pretty well. So what happened?
```

**Shipped v0.6-mixed**:
```
嗯，聽起來事情進展相當順利。 那後來怎麼了？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嗯,聽起來一切都相當順利。 那後來發生了什麼事？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #51 · `ABOUT_US_3` · 🟠

**英文原文**:
```
Yes, things were perfect. What happened is, well, I... it is difficult to talk about.
But I saw it happen. I witnessed the Chinz-Rahl celebration.
I felt the Ultron fill the empty place that I did not know was there.
I saw the Grand Proctor pass it to
well, they say that the Chief Groo did not know that it was so heavy and slippery.
Perhaps it was a combination of factors.
Some who have reviewed the records claim it was actually a conspiracy!
The commission investigation officially stated that the Ultron was rendered inoperative by the fall to the ground,
yet many feel that the whole story has not yet been told!
As it struck the ground, I saw its glow fade, and then the painful void incapacitated all.
All Utwig immediately donned the mask of Ultimate Embarrassment and Shame with a vow to wear it forever!
Bonfires all over Fahz consumed all but this mask; no other mask was spared!
The Visage of Ceremonial Orations in all of its contexts and revisions,
as I'm sure you understand,
all of the courting masks from the clever and intriguing Veil of Flirtatious Prancing
to the infamous Lewd Monacle... all consumed by the hungry flames.
Even the most fundamental fixtures were committed to this irreversible fate.
The Mask of Natural Bodily Excretions once hung in every lavatory!
Most of the public facilities have removed the disposable mask dispensers
but every once in a while I still see such a repository... always empty.
In despair, we gave the broken device to our allies, the Supox, who live at <% comm.getStarName("Beta Librae", "supox") %>.
We just couldn't stand to look at it any longer.
At that time, many suggested that we use the Precursor relic as a form of self punishment.
The proposal was that we collectively go to the second moon of the sixth planet of <% comm.getStarName("Zeta Hyades", "bomb") %>...
...and use the ancient planeteering device to end our existence.
After much discussion, we decided that we deserved to suffer.
We can use the Bomb if we ever decide the time is right
in the meantime, we atone for our grievous mistake with our collective misery.
I suddenly sink into a chasm of depression. I must go.
```

**Shipped v0.6-mixed**:
```
是的，事事完美。 然後發生之事，唉，吾……實在難以啟齒。
但吾親眼目睹。 吾見證了欽茲拉爾（Chinz-Rahl）慶典。
吾感到厄創填滿了吾原本不知存在之空缺。
吾看到大監督者將其傳予
唉，眾人說首領古魯（Groo）並不知曉其竟如此沉重又滑手。
或許是多重因素之集合。
有些查閱記錄之人聲稱，那實則是一場陰謀！
委員會之調查正式宣稱厄創係因摔落地面而失效
然多有人覺得整段真相尚未道盡！
其撞地之時，吾見其光芒漸弱，隨後痛楚之虛空使眾人陷於無能。
所有憂特立即戴上「至極羞愧與恥辱之面具」（Mask of Ultimate Embarrassment and Shame），並發誓終生佩戴！
遍及法茲之篝火吞盡了除此面具外之一切；無有其他面具倖免！
「儀典演說之相貌」（Visage of Ceremonial Orations）於其所有情境與修訂版本中
爾應能理解
所有求偶用之面具，自巧妙迷人之「調情蹦跳之薄紗」（Veil of Flirtatious Prancing）
至臭名昭著之「下流之單片眼鏡」（Lewd Monacle）……皆為飢餓之烈焰吞噬。
即便最基本之裝置亦被推向此不可逆之命運。
「自然體液排泄之面具」(Mask of Natural Bodily Excretions）曾懸掛於每間廁所！
大多數公共設施已移除拋棄式面具分配器
然吾偶爾仍見這樣的儲存匣……永遠空無一物。
於絕望之中，吾等將此破損之裝置給予吾等之盟友蘇菩族，其居於 <% comm.getStarName("天秤座β", "supox") %>。
吾等實在再也無法忍受注視其面。
彼時，許多人建議吾等以此先驅者遺物作為自我懲罰之形式。
提議乃吾等集體前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> 第六顆行星之第二顆衛星……
……並以此古代星體工程裝置終結吾等之存在。
歷經眾多討論後，吾等決意吾等應當受苦。
若吾等有朝一日決意時機成熟，可運用此炸彈
在此期間，吾等以集體之悲愴為此嚴重之過錯贖罪。
吾忽而墜入憂鬱之深淵。 吾必須離去。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
是的,那時一切都很完美。 至於後來發生什麼──嗯,我……這很難說出口。
但我目擊了那件事。 我見證了欽茲拉爾(Chinz-Rahl)慶典。
我感受到厄創填滿了那個我原不知道存在的空缺之處。
我看見大監督者將它傳予──
唉,眾人都說首領古魯(Groo)並不知道它竟如此沉重又滑手。
或許是多重因素的組合。
一些查閱過記錄的人聲稱,那實際上是一場陰謀！
委員會調查已正式聲明,厄創是由於摔落地面而失去功能──
然而許多人覺得完整的真相尚未被公諸於世！
當它撞擊地面時,我看見它的光芒逐漸消退,隨後那痛苦的虛空令所有人陷入無能。
所有憂特立即戴上了「至極羞恥面具」(Mask of Ultimate Embarrassment and Shame),並立誓終生佩戴！
遍佈法茲的篝火吞噬了除此面具之外的一切;沒有任何其他面具倖免！
「儀典演說相貌」(Visage of Ceremonial Orations)在其所有情境與修訂版本之中,
我相信你能理解,
所有的求偶面具,從精巧而引人入勝的「調情蹦跳薄紗」(Veil of Flirtatious Prancing)
到臭名昭著的「下流單片眼鏡」(Lewd Monacle)……皆被飢餓的烈焰吞噬。
即便最基本的裝置也都被推向此不可逆的命運。
「自然體液排泄面具」(Mask of Natural Bodily Excretions)曾懸掛於每一間廁所！
大多數公共設施已移除拋棄式面具分配器,
然而我偶爾仍會看到這樣的儲存匣……永遠空無一物。
在絕望之中,本族將此破損的裝置給予我們的盟友蘇菩族,他們居於 <% comm.getStarName("天秤座β", "supox") %>。
我們就是無法再繼續看著它。
當時,許多人建議本族將這件先驅者遺物作為一種自我懲罰的形式。
提案是,憂特一族集體前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> 第六顆行星的第二顆衛星……
……並使用這件古老的星體工程裝置(planeteering device)終結我們的存在。
經過大量討論,本族決定我們應該受苦。
本族可以在認定時機成熟時使用這顆炸彈,
在此期間,我們以集體的悲苦為自身嚴重的過失贖罪。
我忽然沉入一道憂鬱的深淵。 我必須離去。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #52 · `what_about_urquan_1` · 🔴

**英文原文**:
```
Do you know anything about the enslaving Ur-Quan?
```

**Shipped v0.6-mixed**:
```
你們對奴役銀河的烏寬族有任何了解嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你們對那奴役他人的烏寬族有什麼認識嗎？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #53 · `ABOUT_URQUAN_1` · 🟠

**英文原文**:
```
We know nothing of this species that you mention.
However, while we are on the subject of evil and powerful species
we have encountered a particularly gruesome race that seemed to come from the direction of <% comm.getConstellation("Arcturus", "burvixese") %>.
When we hailed them, they responded with mighty weapons that sent our delegation to their deaths
lucky fools.
The alien's dark crusty battleships are capable of guiding spinning mines into almost any location
and should an enemy get too close, a fiery corona emerges to inflict fearsome damage.
In our skirmishes with the race, who called themselves the Kohr-Ah
we found that by using our own shielding capability we could sweep through the mines, absorb the corona
and then get close enough to the dark ships to give a lick of our own.
In truth, however, they are very powerful and ruthless.
When the Kohr-Ah started to press toward our homeworld
we thought that our deserved punishment was being administered.
But then, a mystery? They suddenly became disinterested and veered away. Bah! Confounding frustration!
With the Ultron I could speak knowledgeably on this subject!
To have this quality torn from our grasp emphasizes how meaningless our existence really is.
This lack of meaning is what drives my species to the serious contemplation of a quick end!
```

**Shipped v0.6-mixed**:
```
吾等對爾所提之此物種一無所知。
然而，既然吾等談到邪惡而強大之物種
吾等曾遭遇一特別可怖之族，似來自 <% comm.getConstellation("大角星", "burvixese") %> （Arcturus） 方向。
吾等呼叫他們時，他們以強大之武器回應，將吾等之代表團送至他們死亡
幸運之愚者。
此外星族黑而堅硬之戰艦能將旋轉之地雷導向幾乎任何位置
若敵人靠得太近，則會湧出火焰光冕造成可怖之損傷。
於吾等與此族之衝突中，他們自稱為柯亞
吾等發現，藉由使用吾等自身之護盾能力，吾等能穿越地雷、吸收光冕
然後靠近黑艦給予吾等自身之一擊。
然真相是，他們極為強大且無情。
當柯亞開始向吾等母星壓迫時
吾等以為吾等應得之懲罰正被執行。
然後，一謎團？ 他們忽然失去興趣並轉向。 呸！ 令人困惑之挫敗！
若吾等擁有厄創，本族便能對此主題博識談論！
此質被自吾等掌中撕去，強調了吾等之存在多麼毫無意義。
此意義之缺失，驅使吾族嚴肅思考迅速之終結！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你所提及的這個物種,本族一無所知。
然而,既然話題是邪惡而強大的物種,
我們憂特曾遭遇過一支特別可怖的族群,看似從 <% comm.getConstellation("大角星", "burvixese") %> 方向而來。
當本族向他們發出招呼,他們以強大的武器回應,將我方的代表團送上死路──
一群幸運的傻瓜。
那些外星族群的黑色硬殼戰艦有能力將旋轉飛雷引導至幾乎任何位置,
而一旦敵艦靠得太近,便會有一道炙焰光冕湧現,造成可怖的傷害。
在本族與此族群──他們自稱為柯亞──的數次交鋒中,
我們發現運用自身的護盾能力便能穿越那些飛雷、吸收那道光冕,
繼而靠近黑艦,回敬一擊。
然而,說實在的,他們既強大又冷酷無情。
當柯亞開始朝我們的母星壓進之時,
本族以為我們應得的懲罰正被施行。
然而接著竟是個謎團？ 他們忽然失去興趣,轉向他方。 呸！（Bah!） 令人困惑的挫折！
若厄創在手,我便能對此議題博學地發言！
這項素質被自我們手中撕走一事,正好凸顯了我們的存在究竟有多麼無意義。
正是這種意義的缺失,驅使我們憂特認真思考一個迅速的終結！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #54 · `what_about_urquan_2` · 🟠

**英文原文**:
```
Yes, that is really a pity. So what more do you know about the Kohr-Ah?
```

**Shipped v0.6-mixed**:
```
是啊，那真令人惋惜。 那你們對柯亞還知道些什麼？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
是啊,那真是可惜。 那麼你們對柯亞還知道些什麼？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #55 · `ABOUT_URQUAN_2` · 🔴

**英文原文**:
```
Aagghh! Your query once again painfully reminds me of the Ultron and what it was for the Universe!
I could tell you all and correct ALL that is wrong in the Universe!
All I can tell you is that the Kohr-Ah live to kill.
Their stated purpose is to seek out new life and new civilizations
and then annihilate them.
We seemed to qualify as such and that is why it is puzzling that after pursuing us with some tenacity
they suddenly turned away and headed toward <% comm.getConstellation("Crateris", "samatra") %>.
Aangh! All this speculation would be unnecessary if only we had saved the Ultron!
It would not have taken much; a diving catch, a thrown pillow
even a fuzzy wumpus would have broken the fall satisfactorily!
Indeed, a panel convened to analyze the possibilities
concluded there were at least 623 ways that the Ultron could have been saved
if we had been prepared! Aagghh!
Let us cease our discussion concerning these matters.
```

**Shipped v0.6-mixed**:
```
啊嗚嗚──！（Aagghh!） 爾之查問再度令吾痛切地憶及厄創與其對宇宙之意義！
若厄創尚在，吾便能盡告爾一切、並匡正宇宙中一切之錯！
吾所能告知爾者，僅為柯亞為殺戮而生。
其等聲明之目的乃探尋新之生命與新之文明
然後將其等湮滅。
吾等似乎符合此條件，故其等以相當之毅力追擊吾等後
忽而放棄、轉向 <% comm.getConstellation("巨爵座", "samatra") %> 而去，此事令人困惑。
嗄──！（Aangh!） 若吾等當時能救下厄創，此等揣測便全然不必！
所需之力並不多；一次撲救、一顆拋出之枕頭
甚或一隻毛絨溫獸都能令其墜落被妥適承接！
誠然，一調查小組召開以分析各種可能性
結論為當時若吾等有備，至少有六百二十三種方法可救下厄創！
啊嗚嗚──！
讓吾等停止關於此事之討論吧。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊嗚嗚──！（Aagghh!） 你的問題再次痛苦地讓我想起厄創,以及它對宇宙的意義！
我本可以告訴你一切,並修正宇宙間所有錯誤之事！
我現在能告訴你的僅有:柯亞為殺戮而生。
他們宣稱的目的是尋找新的生命與新的文明,
然後將它們殲滅。
本族似乎正符合此一條件,因此令人困惑的是,在他們以某種頑強的姿態追擊我們之後,
他們卻忽然轉頭朝 <% comm.getConstellation("巨爵座", "samatra") %> 而去。
嗄──！（Aangh!） 若當初我們救下了厄創,這一切臆測本無必要！
其實不需要多少──一個俯身飛撲、一個投擲的枕頭,
即便是一隻毛絨溫獸(fuzzy wumpus),也足以令這場摔落得到令人滿意的緩衝！
誠然,一個為分析可能性而召開的專家小組
得出結論:至少有六百二十三種方法可以救下厄創──
如果當初我們有所準備的話！ 啊嗚嗚──！
本族就此中止對這些事務的討論吧。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #56 · `got_ultron` · 🔴

**英文原文**:
```
Hey guys, guess what we've got! We've got THE ULTRON! Wanna see it?
```

**Shipped v0.6-mixed**:
```
喂各位，猜猜我方拿到什麼？ 我方拿到厄創了！ 想看嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嘿,你們,猜猜我方手上有什麼！ 我方拿到「厄創」了！ 想看看嗎？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #57 · `DONT_WANT_TO_LOOK` · 🔴

**英文原文**:
```
Gaaah! Should I set my gaze upon such a sight I might suffer sleepless nights for years on end!
It is a symbol of the collective Utwig failure.
It is our ultimate tragedy!
```

**Shipped v0.6-mixed**:
```
嘎啊！（Gaaah!） 若本族將目光落於此景，本族恐將連年不眠！
其乃憂特集體失敗之象徵。
其乃吾等之終極悲劇！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
呃啊啊啊──！（Gaaah!） 我若將目光投向這樣的景象,或許將連年遭受失眠之夜的折磨！
它是我們憂特集體失敗的象徵。
它是本族的終極悲劇！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #58 · `SICK_TRICK_1` · 🔴

**英文原文**:
```
Why do you flaunt the husk which once was the Ultron?
Can't you see how much we suffer? Is this not enough?
This thing you possess... this husk of lost destiny, it is the symbol of the Ultimate Utwig Anguish!
Do - Not - Tor - ment - Me - So!
```

**Shipped v0.6-mixed**:
```
爾為何炫耀那曾為厄創之空殼？
爾看不見吾等所受之痛？ 此還不夠嗎？
爾所擁之此物…… 此失落命運之空殼，乃「至極憂特之痛」之象徵！
莫—折—磨—本—族—如—此！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你為何要炫耀那個曾是厄創的軀殼？
你看不見我們受了多深的苦嗎？ 這還不夠嗎？
你所擁有之物……那個失落命運的軀殼,正是「終極憂特苦痛」的象徵！
別──這──樣──折──磨──我！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #59 · `SICK_TRICK_2` · 🔴

**英文原文**:
```
AAAHHH!! Stop! I know that I deserve it but I cannot bear it.
Stop, please! To view this thing... I would rather bare my face
and work all of its parts in a grotesque display of self-degradation! Leave now!
```

**Shipped v0.6-mixed**:
```
啊啊啊！！（AAAHHH!!） 停！ 本族知本族該受，然本族無法忍受。
拜託停止！ 見此物…… 本族寧可裸露本族之臉
以自貶之怪誕展示活動其所有部件！ 現在離去！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊啊啊──！！（AAAHHH!!） 住手！ 我知道我應得此報,然而我無法承受。
請住手！ 觀看此物……我寧可袒露我的臉面,
以一場怪誕的自貶展演操作它所有的部件！ 立刻離去！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #60 · `bye_neutral` · 🔴

**英文原文**:
```
We now terminate communication in a civil, yet efficient manner.
```

**Shipped v0.6-mixed**:
```
我方就此以文明卻高效之方式結束通訊。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方現在以文明而有效率的方式終止通訊。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #61 · `GOODBYE_NEUTRAL` · 🔴

**英文原文**:
```
As do we. Go now with neither malice nor joy.
```

**Shipped v0.6-mixed**:
```
吾等亦然。 走吧，不帶惡意亦不帶喜悅。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族亦然。 走吧,不帶惡意也不帶欣喜。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #62 · `TOO_LATE` · 🟠

**英文原文**:
```
BUT WAIT!!
The Ultron moans and hums! Matters of significance are being relayed to our brains.
It has been so long since we communicated with the Ultimate in such a manner
but slowly, the truth is revealed!!...
Something dire is afoot in the galaxy
The Kohr-Ah, the dark cousins of the Ur-Quan, have won their Doctrinal Conflict
and are even now moving through the stars on a mission of universal genocide.
The Ultron reveals that our participation is required to stop the Kohr-Ah
before they destroy all life in this part of the galaxy.
We will grant you the boon of our nigh invincible Jugger starship designs
as well as a supply of trained starship commanders.
If our allies, the Supox, are still alive, I am certain they will give you the same assistance.
```

**Shipped v0.6-mixed**:
```
但等等！！
厄創在低吟與鳴響！ 重要之事正被傳達至吾等腦中。
吾等已許久未以此方式與「至極」溝通
然緩緩地，真相被揭示！！……
銀河中有可怕之事正在進行
柯亞，烏寬之陰黑表親，已贏得他們之教義戰爭
此刻正穿越群星，執行一場宇宙級之種族滅絕使命。
厄創揭示，吾等之參與是必要，以阻止柯亞
在他們摧毀此區銀河所有生命之前。
吾等將賜予爾吾等近乎無敵之重砲艦設計之恩惠
以及一批訓練有素之星艦艦長。
若吾等之盟友蘇菩族仍存活，本族確信他們將給予爾同樣之協助。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
且慢！！
厄創呻吟又低鳴！ 重大事務正被傳達至我的心智。
本族已許久未曾以此方式與「至極」溝通,
然而真相正緩緩被揭示！！……
銀河系裡有大事發生──
柯亞,那烏寬族的黑色堂親,已贏得了他們的教義戰爭,
而此刻正穿越群星,執行一場宇宙性的種族滅絕任務。
厄創揭示:需要我們憂特的參與,以在柯亞摧毀本星域所有生命之前
阻止他們。
我方將授予你本族近乎無敵的重砲艦(Jugger)設計,
以及一批訓練有素的星艦指揮官作為賜予。
若我方的盟友蘇菩族仍然存活,我確信他們也會給予你相同的協助。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #63 · `HAPPY_DAYS` · 🟠

**英文原文**:
```
AAAHHH!! Every divot, every crack on Its surface is etched forever in my soul!
Remove It from my sight lest I purge my... hey!
that is not the devastated Ultron
it is the image of the Ultron BEFORE!... a trick? A TRICK?!
Oooh! I had no idea that any species could sink so low!
How dare you try to manipulate me with that cheap stage prop?!... why it's not even
Hey, wait a second, it looks like... CAN IT BE?... YES, IT IS!...A MIRACLE!!
OH HAPPY DAY!!  JOYOUS OCCASION!!
You have our eternal thanks, good Captain!
You will be immortalized as the blessed figure that delivered unto us our future!
We will revere your very likeness!
Let me take the Ultron...yes, I feel the link...the knowledge, and... the Power.
Hmm, it seems that there is much to do.
Indeed, it seems that you should proceed to the second moon of the sixth planet of <% comm.getStarName("Zeta Hyades", "bomb") %>...
...and take what you find there; we no longer have need for it
but the Ultron reveals that YOU will!
I thank you for your part in the grand scheme. We now recover that which is ours via destiny
and proceed to perform our essential service for the universe.
```

**Shipped v0.6-mixed**:
```
啊啊啊──！！ 其表面之每一凹痕、每一裂縫，皆永銘於吾之靈魂之中！
將其從吾之視線移開，免得吾清空吾之……咦！
那並非那損毀之厄創
那是先前厄創之影像！……一個把戲？ 一個把戲？！
噢噢噢！（Oooh!） 吾竟不知有任何族群能墮落至此地步！
爾竟敢以此廉價舞台道具擺弄吾？！……何況那甚至不是──
喂，等等，看起來像是……果真是嗎？……是的，就是它！……一個奇蹟！！
噢，歡欣之日！！ 歡樂之時！！
蒙福的憂特對爾致以永恆之感激，善良之艦長！
爾將以將吾等之未來送予吾等之蒙福身影名垂不朽！
吾等將崇敬爾之樣貌！
容吾接過厄創……是的，吾感到那連結……那知識，以及……那力量。
嗯，看來吾等尚有諸多事宜要做。
誠然，看來爾應前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> 第六顆行星之第二顆衛星……
……並取回爾於彼處尋得之物；吾等不再需要它
但厄創揭示爾將需要！
吾感謝爾於此宏大格局中之付出。 吾等現循天命收回本屬吾等之物
繼而執行吾等對宇宙之核心使命。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊啊啊──！！(AAAHHH!!) 它表面的每一個凹痕、每一道裂縫,都永恆銘刻在我的靈魂之中！
將它從我的視線移開,免得我清空我的……咦！
那並非那損毀的厄創──
那是先前厄創的影像！……一個把戲？ 一個把戲？！
噢噢噢！（Oooh!） 我竟不知有任何族群能墮落至此地步！
你竟敢以這廉價的舞台道具來操弄我？！……何況它甚至不是──
喂,等等,看起來像是……果真是嗎？……是的,就是它！……一個奇蹟！！
噢,歡欣之日！！ 歡樂的時刻！！
蒙福的憂特對你致以永恆的感激,善良的艦長！
你將以將我們憂特的未來送予本族的蒙福身影,而名垂不朽！
本族將崇敬你的樣貌！
讓我接過厄創……是的,我感受到那連結……那知識,以及……那力量。
嗯,看來我們尚有諸多事宜要做。
誠然,看來你應前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> 第六顆行星的第二顆衛星……
……並取回你於彼處尋得之物;我們憂特不再需要它,
但厄創揭示:你將會需要它！
我感謝你於此宏大格局中的付出。 本族現在遵循天命收回本屬憂特一族之物,
繼而執行我們對宇宙的核心使命。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #64 · `OK_ATTACK_KOHRAH` · 🟠

**英文原文**:
```
BUT WAIT!!
The Ultron throbs and whistles! Matters of significance are being relayed to our brains.
It has been so long since we communicated with the ultimate in such a manner
but slowly, the truth is revealed... our destiny!!
We have been directed to join with our Supox allies and attack...
YOU!...
...no wait, that's wrong. Sorry.
We attack... YOUR ENEMIES... the Ur-Quan and the Kohr-Ah!...
...no, that's not quite right either... what? Oh, okay.
We must strike ONLY the black ships... only the Kohr-Ah!
IN ADDITION! We will grant you the boon of our Jugger starship designs
as well as a supply of trained starship commanders.
Our Juggers are nigh invincible!
I can also say with certainty that our allies, the Supox, will give you the same assistance.
Together, we shall defeat the Kohr-Ah!... or at least provide you with a few more months
to find a more permanent solution.
Now, Captain, we must leave to prepare our battle fleets. Wish us luck!
```

**Shipped v0.6-mixed**:
```
然且慢！！
厄創震動而鳴嘯！ 事關重大之訊息正被傳達至吾等之腦海。
吾等已許久未曾以此方式與至物溝通
然真相緩緩揭露……吾等之天命！！
吾等榮光族被指示加入吾等之盟友蘇菩族，並攻擊……
爾！……
……不，等等，錯了。 抱歉。
吾等攻擊……爾之敵人……烏寬與柯亞！……
……不，這也不太對……什麼？ 噢，好吧。
吾等必須僅打擊那些黑艦……僅打擊柯亞！
此外！ 吾等將賜予爾吾等重砲艦設計之恩澤
以及一批訓練有素之艦艇指揮官。
吾等之重砲艦幾近無敵！
吾亦可斷言，吾等之盟友蘇菩族，將給予爾同樣之援助。
攜手同心，吾等必擊敗柯亞！……或至少為爾多爭得數月
以尋得更持久之解答。
如今，艦長，吾等必須離去，準備吾等之戰鬥艦隊。 祝吾等好運！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
且慢！！
厄創震動又鳴嘯！ 事關重大的訊息正被傳達至我的心智。
本族已許久未曾以此方式與「至極」溝通,
然而真相緩緩揭露……我們憂特的天命！！
蒙福的憂特被指示加入我方的盟友蘇菩族,並攻擊……
你！……
……不,等等,錯了。 抱歉。
我們攻擊……你的敵人……烏寬族與柯亞！……
……不,這也不太對……什麼？ 噢,好吧。
本族必須僅打擊那些黑艦……僅打擊柯亞！
此外！ 我方將賜予你我們憂特重砲艦設計的恩澤,
以及一批訓練有素的星艦指揮官。
本族的重砲艦近乎無敵！
我亦可斷言,我方的盟友蘇菩族將給予你相同的援助。
攜手同心,我們必擊敗柯亞！……或至少為你多爭得數月,
以尋得更持久的解答。
如今,艦長,本族必須離去,準備我方的戰鬥艦隊。 祝我們好運！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #65 · `whats_up_after_space` · 🟠

**英文原文**:
```
Tell us what events have transpired since we last met.
```

**Shipped v0.6-mixed**:
```
跟我方講講自上次見面以來發生的事吧。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
說說自我方上次見面以來發生了什麼事。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #66 · `GENERAL_INFO_AFTER_SPACE_1` · 🟠

**英文原文**:
```
We have met the Kohr-Ah in battle, and... well, let me explain.
Initially, when our forces swept to the <% comm.getConstellation("Horologii", "samatra") %> stars
they proved effective against the armaments of the Kohr-Ah.
With our shield-absorption technology we were able to sweep clear the Kohr-Ah's spinning blades
and absorb the brunt of their fiery corona, allowing our Supox allies to concentrate on the vessels themselves.
However, the costs were high... very high.
I should don the facial effigy of Remorse For Lost Comrades.
```

**Shipped v0.6-mixed**:
```
吾等已於戰場遇柯亞，然……容吾解釋。
最初，當吾等之部隊掃入 <% comm.getConstellation("時鐘座", "samatra") %> 之群星
其等對柯亞之軍備甚為有效。
運用吾等之護盾吸收技術，吾等能掃清柯亞之旋轉飛刃
並吸收其熾烈光冕之衝擊，令吾等之蘇菩盟友得以專注於敵艦本體。
然代價高昂……甚為高昂。
吾應戴上「哀悼陣亡同袍」（Remorse For Lost Comrades）之容。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族已於戰場遇上柯亞,而……讓我解釋。
最初,當我們的部隊掃入 <% comm.getConstellation("時鐘座", "samatra") %> 的群星時,
他們對柯亞的軍備甚為有效。
運用本族的護盾吸收技術,我們能掃清柯亞的旋轉飛刃,
並吸收其熾烈光冕的衝擊,令我方的蘇菩盟友得以專注於敵艦本體。
然而代價高昂……甚為高昂。
我應戴上「哀悼陣亡袍澤」(Remorse For Lost Comrades)之容。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #67 · `GENERAL_INFO_AFTER_SPACE_2` · 🟠

**英文原文**:
```
As you know, we were forced to withdraw from the Kohr-Ah offensive.
Although we were able to make good account of ourselves, our casualties were high.
In our attempt to balance the Doctrinal Conflict between the Kohr-Ah and the Ur-Quan
we avoided the Ur-Quan; however, they continued to engage us whenever possible.
We had no choice but to take whatever losses were handed to us.
I can think of no mask that properly expresses how I feel concerning this situation.
```

**Shipped v0.6-mixed**:
```
如爾所知，吾等被迫自柯亞攻勢中撤退。
儘管吾等已盡力表現，吾等之傷亡仍高。
於吾等試圖平衡柯亞與烏寬族之教義戰爭時
吾等避開烏寬族；然而，他們持續於可能時交戰吾等。
吾等別無選擇，只能承受任何被交予之損失。
本族想不到任何面具能正確表達本族對此情況之感受。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
如你所知,本族被迫自柯亞攻勢中撤退。
儘管我們已盡力表現,本族的傷亡仍高。
在憂特一族試圖平衡柯亞與烏寬族的教義戰爭時,
本族刻意避開烏寬族;然而,只要有機會他們仍持續攻擊我們。
本族別無選擇,只能承受任何被交予的損失。
我想不到任何面具能正確表達我對此情況的感受。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #68 · `what_now_after_space` · 🔴

**英文原文**:
```
Given what you have learned, what do you think we should do now?
```

**Shipped v0.6-mixed**:
```
根據你們所學到的，你們認為我方現在該怎麼做？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
就你所知,你認為我方現在該怎麼做？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #69 · `DO_THIS_AFTER_SPACE` · 🟠

**英文原文**:
```
We have done all that we can. There are no others capable of significant intervention.
Certain doom grows imminent for all of us. We lament.
But wait!...listen closely! The Ultron intervenes! There is a solution!
YOU are the solution!
Only YOU may halt the Kohr-Ah's seemingly inevitable advance upon life.
They CAN be defeated and you MUST do it!
Oh, my spirit is lifted! If only my mask of Confident and Lofty Posture had not been burned
I would don it with rash impudence ignoring all etiquette and procedures!
```

**Shipped v0.6-mixed**:
```
吾等已竭盡所能。 再無其他能夠有效介入者。
確定之厄運迫近吾等所有人。 吾等哀嘆。
然且慢！……仔細聽！ 厄創介入！ 有解答！
爾乃解答！
唯爾能阻止柯亞看似不可避免之對生命之進犯。
其等能被擊敗，而爾必須為之！
噢，吾之心神振奮！ 若吾之「自信高貴姿態之面具」（Mask of Confident and Lofty Posture）不曾被焚
吾將以鹵莽之魯直將其戴上，不顧一切禮儀與程序！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族已竭盡所能。 再無其他能夠有效介入者。
確定的厄運迫近我們所有人。 我方哀嘆。
然且慢！……仔細聽！ 厄創介入！ 有解答！
你就是解答！
唯有你能阻止柯亞看似不可避免的、對生命的進犯。
他們能被擊敗,而你必須為之！
噢,我的心神振奮！ 若我的「自信高貴姿態面具」(Mask of Confident and Lofty Posture)不曾被焚,
我將以鹵莽的魯直將它戴上,不顧一切禮儀與程序！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #70 · `bye_after_space` · 🟠

**英文原文**:
```
We thank you for your aid. We go now to address the matters at hand.
```

**Shipped v0.6-mixed**:
```
感謝你們的協助。 我方現在得處理眼前的事務了。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方感謝你的援助。 我方現在要去處理眼前的事務了。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #71 · `GOODBYE_AFTER_SPACE` · 🟠

**英文原文**:
```
Excellent! The Ultron's coruscations indicate that your future actions are laced with great potential!
Proceed with our heartiest endorsement!
```

**Shipped v0.6-mixed**:
```
極佳！ 厄創之閃耀顯示爾未來之行動蘊含巨大潛能！
以吾等最誠摯之支持繼續前進！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
極佳！ 厄創的閃耀顯示你未來的行動蘊含巨大潛能！
帶著我們最誠摯的支持繼續前進！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #72 · `whats_up_before_space` · 🟠

**英文原文**:
```
We are pleased that we were of assistance in the recovery of your Ultron.
```

**Shipped v0.6-mixed**:
```
我方很高興能協助你們找回厄創。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方很高興能協助你們取回厄創。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #73 · `GENERAL_INFO_BEFORE_SPACE_1` · 🟠

**英文原文**:
```
Indeed! We are in the process of reacclimating our brains to its metawave gyrations.
Even now we are compelled to implement a plan of interference, thwarting the goals of the Kohr-Ah.
We sense through the influence of the Ultron that these creatures of evil
have goals which are mutually exclusive with our existence, and your own.
Even now, aided by the intangible guidance of the Ultron, we formulate a plan
that will serve to preserve the diversity in the galaxy.
We prepare an armada composed of the collective might of both the Utwig and Supox forces
that will pursue the invaders with the intent of foiling their plan of doom.
```

**Shipped v0.6-mixed**:
```
確實！ 吾等正處於使吾等腦部重新適應其超波動盪之過程中。
即使此刻，吾等被迫執行一項干擾之計畫，挫敗柯亞之目標。
吾等透過厄創之影響感應到，此等邪惡之生物
擁有與吾等與爾之存在互斥之目標。
即使此刻，於厄創之無形指引輔助下，吾等制定一項計畫
將能保存銀河中之多樣性。
吾等準備一支由憂特與蘇菩兵力集體之力量組成之艦隊
將以挫敗其厄運之計畫為意圖追擊入侵者。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
確實！ 本族正處於使我們腦部重新適應厄創超波動盪的過程中。
即便此刻,我方也被驅使去實施一項干擾計畫,以挫敗柯亞的目標。
透過厄創的影響,我們感應到:這些邪惡的生物
所懷的目標,與本族及你的存在互斥。
即便此刻,在厄創無形指引的輔助下,我們正制定一項計畫,
以保存銀河系中的多樣性。
本族正籌組一支由憂特與蘇菩兵力集體之力量組成的艦隊,
將以挫敗其厄運計畫為意圖,追擊入侵者。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #74 · `GENERAL_INFO_BEFORE_SPACE_2` · 🟠

**英文原文**:
```
We have determined that the Kohr-Ah are engaging in battle with the species you call Ur-Quan.
We are unable to determine the cause of this conflict.
Even meticulous employment of the Ultron in this matter has yielded only minimal insight.
In any case, after interpreting the direction provided by the Ultron
we must let the two species cancel each other out via attrition through combat.
```

**Shipped v0.6-mixed**:
```
吾等已確定柯亞正與爾稱為烏寬族之物種交戰。
吾等無法確定此衝突之原因。
即使謹慎地將厄創用於此事，也僅產生極少之洞察。
無論如何，於解讀厄創所提供之指引後
吾等必須讓兩物種透過戰鬥中之消耗互相抵消。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族已確定柯亞正與你所稱為烏寬族的物種交戰。
我們無法確定此衝突的原因。
即便謹慎地將厄創用於此事,也僅產生極少的洞察。
無論如何,在解讀厄創所提供的指引之後,
本族必須讓這兩個物種透過戰鬥中的消耗互相抵消。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #75 · `what_now_before_space` · 🔴

**英文原文**:
```
Does the remarkable device suggest to us a potential course of action?
```

**Shipped v0.6-mixed**:
```
這件卓越之裝置有向我方建議潛在的行動方針嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
那件非凡的裝置對我方是否有任何潛在行動的建議？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #76 · `DO_THIS_BEFORE_SPACE` · 🟠

**英文原文**:
```
Your request is within our capabilities. One moment
Mmmm, emanations from the Ultron... orange furry air breathes tender yawns
Yes, it all becomes clear now... you must do something with the great Bomb
the Precursor relic we kept at <% comm.getStarName("Zeta Hyades", "bomb") %> VI-B.
It seems that this Bomb must be, ah...
eaten?... no. Hugged?... no
Ah! IMPROVED! That's it!  The Bomb must be improved to fulfill its final destiny!
```

**Shipped v0.6-mixed**:
```
爾之請求在吾等之能力範圍內。 稍待
唔嗯，來自厄創之流溢……橘色毛絨的空氣呼出溫柔的哈欠
是的，一切現在都清楚了……爾必須對那大炸彈做些什麼
即吾等保管於 <% comm.getStarName("畢宿星團ζ", "bomb") %> VI-B 之先驅者遺物。
看來此炸彈必須，啊……
吃掉？……不。 擁抱？……不
啊！ 改良！ 就是了！ 此炸彈必須被改良以完成其最終之天命！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你的請求在本族的能力範圍之內。 稍待──
唔嗯,來自厄創的流溢……橘色毛絨的空氣呼出溫柔的哈欠
是的,一切現在都清楚了……你必須對那顆大炸彈做些什麼──
即我們保管於 <% comm.getStarName("畢宿星團ζ", "bomb") %> VI-B 的先驅者遺物。
看來這顆炸彈必須,啊……
吃掉？……不。 擁抱？……不──
啊！ 改良！ 就是了！ 這顆炸彈必須被改良,以完成它最終的天命！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #77 · `bye_before_space` · 🟠

**英文原文**:
```
We anticipate an era of glory for the Utwig! Farewell!
```

**Shipped v0.6-mixed**:
```
我方預期憂特的榮耀時代將至！ 再會！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方期待憂特的榮耀時代！ 珍重！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #78 · `GOODBYE_BEFORE_SPACE` · 🟠

**英文原文**:
```
There is much for us to do. May the Ultron be with you!
```

**Shipped v0.6-mixed**:
```
吾等尚有諸多事要做。 願厄創與爾同在！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族尚有諸多事要做。 願厄創與你同在！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #79 · `how_went_war` · 🟠

**英文原文**:
```
What were the results of your actions against the Ur-Quan and Kohr-Ah?
```

**Shipped v0.6-mixed**:
```
你們對抗烏寬族與柯亞的行動結果如何？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你們對烏寬族與柯亞的行動結果如何？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #80 · `ABOUT_BATTLE` · 🟠

**英文原文**:
```
Ah Captain! The battle against the Kohr-Ah was fearsome.
As we and our allied Supox approached the main force
we found that the Kohr-Ah and the species you call the Ur-Quan
were engaged in a conflict of fundamental doctrine in which the Kohr-Ah thesis seemed superior.
Acting under the guidance of the Ultron, we engaged the Kohr-Ah in an effort to balance the battle.
We met with some success. We would sweep the mines clear and deplete the energy reserves of the Kohr-Ah vessels.
Then, the brave Supox would dart in and direct their weapons against the black ships.
Timing was critical. Our losses were high.
Battered in the extreme, we were forced to withdraw.
```

**Shipped v0.6-mixed**:
```
啊，艦長！ 對抗柯亞之戰役可畏。
當吾等與吾等結盟之蘇菩族接近主力時
吾等發現柯亞與爾稱為烏寬族之物種
正陷入教義根本之衝突中，而柯亞之論題似乎較優。
於厄創之指引下行動，吾等交戰柯亞以圖平衡戰役。
吾等取得部分成功。 吾等會掃除地雷，耗盡柯亞艦艇之能量儲備。
然後，勇敢之蘇菩會俯衝而入，將其武器對準黑艦。
時機至關重要。 吾等之損失高昂。
極端受創之下，吾等被迫撤退。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊,艦長！ 對抗柯亞的戰役可畏。
當本族與結盟的蘇菩族接近主力時,
我們發現柯亞與你稱為烏寬族的物種
正陷入一場教義根本的衝突,而柯亞的論題似乎較優。
在厄創的指引下行動,我方交戰柯亞以圖平衡戰役。
本族取得了部分成功。 我們會掃除地雷,並耗盡柯亞艦艇的能量儲備。
然後,勇敢的蘇菩會俯衝而入,將他們的武器對準黑艦。
時機至關重要。 我方的損失高昂。
在極端受創之下,本族被迫撤退。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #81 · `how_goes_war` · 🟠

**英文原文**:
```
How is your engagement with the Kohr-Ah and Ur-Quan going?
```

**Shipped v0.6-mixed**:
```
你們與柯亞和烏寬族的交戰進行得如何？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你們與柯亞及烏寬族的交戰進行得如何？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #82 · `BATTLE_HAPPENS_1` · 🟠

**英文原文**:
```
Even as I speak, brave Utwig and noble Supox launch themselves against the merciless arsenal of the Kohr-Ah.
We continue to refine our tactics.
Alas, the Kohr-Ah are winning their war with the Ur-Quan.
We grow uncomfortable with the success that the Kohr-Ah are currently enjoying,
so we fight only the Kohr-Ah in hopes of weakening their stand against the Ur-Quan.
The Ur-Quan complicate matters by blasting our vessels with fusion bolts
thus we have made it a policy to avoid Ur-Quan ships whenever possible.
```

**Shipped v0.6-mixed**:
```
即使本族此刻言之，勇敢之憂特與高貴之蘇菩，正投身於柯亞無情之武備之前。
吾等持續精進吾等之戰術。
痛哉！（Alas!） 柯亞正贏得其與烏寬族之戰爭。
吾等對柯亞當前所享之成功感到不安，
故吾等只交戰柯亞，以期削弱其對烏寬族之立場。
烏寬族以聚變彈爆擊吾等艦艇讓事情更複雜
故吾等已將盡可能避開烏寬艦艇定為政策。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
即便此刻本族言之,勇敢的憂特與高貴的蘇菩,正投身於柯亞無情的武備之前。
我們持續精進戰術。
痛哉！（Alas!） 柯亞正贏得他們與烏寬族的戰爭。
本族對柯亞當前所享的成功感到不安,
因此我方只交戰柯亞,以期削弱他們對烏寬族的立場。
烏寬族以聚變彈爆擊我們艦艇,讓事情更加複雜,
因此本族已將盡可能避開烏寬艦艇定為政策。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #83 · `BATTLE_HAPPENS_2` · 🟠

**英文原文**:
```
We have discovered that the Kohr-Ah, in addition to their formidable battle vessels
will soon possess an immense ship capable of inflicting destruction on a vast scale.
I do not need to examine the pulsations of the Ultron to know that they will use this instrument
to implement their stated objective: the elimination of all intelligent life besides their own.
```

**Shipped v0.6-mixed**:
```
吾等已發現柯亞除了其令人畏懼之戰鬥艦艇
將很快擁有一巨型艦艇，能造成大規模之毀滅。
本族無需檢視厄創之脈動便知他們將用此工具
執行其宣稱之目標：消滅除其自身外所有智慧生命。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族已發現柯亞除了其令人畏懼的戰鬥艦艇之外,
很快將擁有一艘巨型艦艇,能造成大規模的毀滅。
我無需檢視厄創的脈動便能知曉:他們將運用此工具
執行他們宣稱的目標:消滅除他們自身之外所有的智慧生命。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #84 · `FLEET_ON_WAY` · 🟠

**英文原文**:
```
Even as I utter these words, the combined military resource of both the Utwig and Supox
proceed toward <% comm.getConstellation("Horologii", "samatra") %> to intercept the Kohr-Ah.
Besides the importance of our efforts, the Ultron indicates
all futures which include our survival are contingent on the actions that you now take.
```

**Shipped v0.6-mixed**:
```
即使本族此刻說出這些話，憂特與蘇菩之聯合軍事資源
正朝 <% comm.getConstellation("時鐘座", "samatra") %> 前進以攔截柯亞。
除了吾等之努力之重要性外，厄創顯示
所有包含吾等生存之未來皆取決於爾此刻所採取之行動。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
即便此刻本族說出這些話,憂特與蘇菩的聯合軍事資源
正朝 <% comm.getConstellation("時鐘座", "samatra") %> 前進,以攔截柯亞。
除了我們努力的重要性之外,厄創亦顯示:
所有包含我方生存在內的未來,皆取決於你此刻所採取的行動。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #85 · `learn_new_info` · 🔴

**英文原文**:
```
I'm glad things are looking up. Anything in the way of new developments?
```

**Shipped v0.6-mixed**:
```
很高興情況有起色。 有什麼新發展嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方很高興情況正在好轉。 有沒有任何新進展？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #86 · `NO_NEW_INFO` · 🟠

**英文原文**:
```
Even now we acclimate to the great power of the Ultron
but are overwhelmed with the resources that the Ultron offers
in effect, we have grown rusty in its use.
As soon as we regain our proficiency, we will be able to accommodate all your requests.
```

**Shipped v0.6-mixed**:
```
即使此刻吾等仍在適應厄創之偉大力量
卻被厄創所提供之資源壓倒
實際上，吾等於其使用上已生疏了。
一旦吾等恢復熟練度，吾等將能滿足爾所有請求。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
即便此刻,本族仍在適應厄創的偉大力量,
卻被厄創所提供的資源壓倒,
實際上,我們對它的使用已經生疏了。
一旦本族恢復熟練度,我方將能滿足你所有的請求。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #87 · `SAMATRA` · 🟠

**英文原文**:
```
The Kohr-Ah will soon possess a seemingly invincible vessel called the Sa-Matra.
I cannot give you specifics regarding this matter other than its general location
somewhere in the <% comm.getConstellation("Crateris", "samatra") %> constellation.
The Sa-Matra is seemingly invincible, able to lay waste to an entire planet in less than an eyeblink.
The Ultron indicates that you must somehow destroy this thing or the Kohr-Ah will destroy all known life.
```

**Shipped v0.6-mixed**:
```
柯亞將很快擁有一看似無敵之艦艇，稱為薩瑪特拉。
本族除其大略位置外，無法給予爾關於此事之具體資訊
位於 <% comm.getConstellation("巨爵座", "samatra") %> （Crateris） 星座某處。
薩瑪特拉看似無敵，能於眨眼之間讓整個行星化為廢墟。
厄創顯示爾必須以某種方式摧毀此物，否則柯亞將摧毀所有已知生命。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
柯亞很快將擁有一艘看似無敵的艦艇,稱為薩瑪特拉。
除了它的大略位置之外,本族無法給予你關於此事的具體資訊──
位於 <% comm.getConstellation("巨爵座", "samatra") %>(Crateris) 星座某處。
薩瑪特拉看似無敵,能在眨眼之間讓整顆行星化為廢墟。
厄創顯示:你必須以某種方式摧毀此物,否則柯亞將摧毀所有已知的生命。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #88 · `what_now_homeworld` · 🔴

**英文原文**:
```
What course of action does the Ultron, your powerful attribute amplifier, recommend for us now?
```

**Shipped v0.6-mixed**:
```
爾等之偉大屬性放大器 —— 厄創 —— 對我方推薦何行動方針？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
厄創──你們那強大的屬性放大器(attribute amplifier)──對我方現在的行動有何建議？
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #89 · `HOPE_KILL_EACH_OTHER` · 🟠

**英文原文**:
```
We can only hope that our efforts to balance the forces of the Ur-Quan and the Kohr-Ah
will permit them to mutually annihilate each other.
```

**Shipped v0.6-mixed**:
```
吾等只能期望吾等平衡烏寬族與柯亞之力量之努力
將使他們得以互相殲滅。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族只能期望我們平衡烏寬族與柯亞力量的努力,
將使他們得以互相殲滅。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #90 · `how_is_ultron` · 🟠

**英文原文**:
```
It seems that you are making good use of the Ultron. Is this so?
```

**Shipped v0.6-mixed**:
```
看來你們善用了厄創。 是這樣嗎？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
看來你們把厄創運用得挺好。 情況是這樣嗎？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #91 · `ULTRON_IS_GREAT` · ✨

**英文原文**:
```
You ask a question that I hesitate to answer. You see, normally at this point
I would don the mask of Rampant Jubilation and Jumping With Ecstatic Glee.
This mask is seldom worn, for few events merit its complexity.
Since I do not currently possess this mask
let me just say that the Ultron is everything it could ever possibly be and MORE!
Even now I sense that your curiosity is piqued to an extreme.
You wish to ask more questions.
However, these questions are probably best left unasked.
It is through the potent yet harmonious force of the Ultron
that I will now cause you to drop the subject altogether.
```

**Shipped v0.6-mixed**:
```
爾問了一個吾遲疑回答之問題。 爾當知，於此常態場合
吾會戴上「狂野歡欣與狂喜跳躍之面具」（Mask of Rampant Jubilation and Jumping With Ecstatic Glee）。
此面具鮮少佩戴，因少有事件配得其複雜性。
既然吾此刻並不擁有此面具
容吾直言：厄創乃其所可能之一切──甚至更多！
即便此刻，吾感到爾之好奇心已被激至極致。
爾欲問更多問題。
然而，此等問題或許最好不問。
乃透過厄創之強大而和諧之力
吾此刻將令爾徹底放棄此話題。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你問了一個我遲疑作答的問題。 你要知道,在此類常態場合,
我會戴上「狂喜歡騰彈跳面具」(Mask of Rampant Jubilation and Jumping With Ecstatic Glee)。
此面具鮮少被佩戴,因為少有事件配得上它的複雜性。
既然我此刻並不擁有這件面具,
容我直言:厄創就是它所可能是的一切──甚至更多！
即便此刻,我也感到你的好奇心已被激至極致。
你想問更多的問題。
然而,這些問題,或許最好不要問。
透過厄創那強大而和諧的力量,
本族此刻將令你徹底放棄這個話題。
```

**Canonical 升級理由**: v0.7 dossier §四 Q_C 決策 — 面具名 >10 字者 clean-room 重譯以貼合現代學者風格。

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #92 · `bye_allied_homeworld` · 🔴

**英文原文**:
```
We acknowledge the celestial Ultron and your assistance. We will now be on our way.
```

**Shipped v0.6-mixed**:
```
我方感謝天國的厄創與你們的協助。 我方就此告辭。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我方向天國的厄創與你們的援助致意。 本族現在要動身了。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #93 · `GOODBYE_ALLIED_HOMEWORLD` · 🔴

**英文原文**:
```
It is as the Ultron wills. So be it. We bid you the very best luck.
Although it is true that all possibilities can be realized through proper utilization of the Ultron
we are, as yet, deficient operators of this grand device.
We will, however, make a best attempt to help you from afar.
```

**Shipped v0.6-mixed**:
```
如厄創之意志。 就此決定。 吾等祝爾最好之運。
儘管所有可能性皆可透過厄創之適當使用實現
吾等，至今為止，尚為此宏大裝置不成熟之操作者。
然而，吾等將自遠方盡最大努力協助爾。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
這即是厄創的意志。 就這樣吧。 本族祝你獲得最好的運氣。
誠然,所有可能性都能透過厄創的適當運用而實現,
然而,我們到目前為止,仍是這件宏大裝置尚不成熟的操作者。
話雖如此,本族仍將自遠方盡最大的努力協助你。
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #94 · `ALLIED_HOMEWORLD_HELLO_1` · 🟠

**英文原文**:
```
Ah! It is the legendary Earth Captain! A grand celebration is in order!
We prepare now for the festivities!
Many will bow before you and offer their profuse thanks!
Proceed now to our main spaceport and then on to the parade!
The two week celebration of great thanks will begin! Joy!
What? You are too busy? Alas... perhaps another time.
```

**Shipped v0.6-mixed**:
```
啊！ 那乃傳奇之地球艦長！ 應舉大慶！
蒙福的憂特現正為慶典籌備！
眾人將於爾前俯首，獻上滿溢之謝意！
現前往吾等之主太空港，繼而參加遊行！
兩週之盛大感恩慶典即將開始！ 歡欣！
什麼？ 爾太忙？ 痛哉…… 或許改日再說。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊！ 那是傳奇的地球艦長！ 應舉行盛大慶典！
蒙福的憂特現正為慶典籌備！
眾人將於你面前俯首,獻上滿溢的謝意！
現在請前往本族的主太空港,繼而參加遊行！
為期兩週的盛大感恩慶典即將開始！ 歡欣！
什麼？ 你太忙？ 痛哉…… 或許改日再說。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #95 · `ALLIED_HOMEWORLD_HELLO_2` · 🟠

**英文原文**:
```
Our spirits are lifted by your visit!
I sense through the Ultron's powers that you are curious
about the status of your well-deserved facial appliance. Fear not!
Even though we currently have no masks worthy of your stature
with the re-establishment of the Ultron within the structure of the Utwig wholeness
we proceed with the design and implementation of what will truly be the pinnacle of Utwig ingenuity.
At long last, you will be able to cover your unsightly mug with distinction!
```

**Shipped v0.6-mixed**:
```
神聖之艦長之蒞臨令吾等之心神振奮！
吾透過厄創之力感應到爾對爾應得
之面部器具狀態感到好奇。 勿懼！
儘管吾等此刻並無配得爾身份之面具
然隨厄創於憂特整體結構中之重新確立
吾等正推進設計與實作，此物將真正成為憂特智慧之巔峰。
終有一日，爾將能以卓然之姿遮蔽爾醜陋之臉！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
神聖之艦長的蒞臨令本族的心神振奮！
我透過厄創之力感應到:你對自己應得的
面部器具狀態感到好奇。 勿懼！
儘管本族此刻並無配得你身份的面具,
然而隨著厄創於憂特整體結構中的重新確立,
我們正推進設計與實作,此物將真正成為憂特智慧的巔峰。
終有一日,你將能以卓然的姿態遮蔽你那醜陋的臉！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #96 · `ALLIED_HOMEWORLD_HELLO_3` · 🟠

**英文原文**:
```
Ah, I see that it is the great Earth Captain honoring my lowly self with undeserved attention.
Even now my skin prickles with embarrassment since I am unable to don a mask
that accurately indicates my awed and respectful attitude toward you.
I am glad to say, however, that we are in a process
of redefining and restructuring our entire countenance catalog.
The results will be dramatic since the Ultron is now integrated in this process.
In the meantime, I beg that you bear with us while we complete this task.
```

**Shipped v0.6-mixed**:
```
啊，本族看見是偉大之地球艦長，正以不當之關注屈就本族之卑下。
即使此刻，本族之皮膚亦因無法戴上準確表達本族對爾崇敬與尊敬態度之面具
而尷尬得起雞皮疙瘩。
然本族欣然報告，吾等正處於
重新定義並重構吾等整個容貌目錄之過程中。
結果將戲劇性，因厄創如今已納入此過程。
在此期間，本族懇求爾容忍吾等完成此任務。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊,我看見,是偉大的地球艦長,正以不當的關注屈就本族的卑下。
即便此刻,我的皮膚也因無法戴上準確表達我對你崇敬與尊敬態度的面具
而尷尬得起雞皮疙瘩。
然而,本族欣然報告:我們正處於
重新定義並重構我們整個容貌目錄的過程之中。
結果將極具戲劇性,因為厄創如今已納入這個過程。
在此期間,我懇求你容忍本族完成這項任務。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #97 · `ALLIED_HOMEWORLD_HELLO_4` · 🟠

**英文原文**:
```
I am honored to encounter your greatness!
Currently, our collective creative force is engaged in a project to honor you.
We are in the process of transforming a planetary body
in a location that will remain secret
into a Great Mask. This mask will be worn by one individual and ONLY one individual!
It is the mask of the great Captain! It is YOU that wears this mask.
When you don this mask, we will see the eyes come alive.
When you speak, all will hear. When you smile, we will rejoice!
I sense your excitement concerning this project!
```

**Shipped v0.6-mixed**:
```
吾深感榮幸能遇爾之偉大！
目前，吾等集體之創造力正投入一項榮耀爾之計劃。
吾等正將一顆行星星體
於一處將保守秘密之地
轉變為一副至偉面具。 此面具將由一位、且僅一位個體佩戴！
此乃偉大艦長之面具！ 佩戴此面具者乃爾也。
當爾戴上此面具，吾等將見其眼眸活過來。
當爾發言，眾人將聞。 當爾微笑，吾等榮光族將歡欣！
吾感到爾對此計劃之興奮！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我深感榮幸能遇上你的偉大！
目前,本族集體的創造力正投入一項榮耀你的計畫。
我們正將一顆行星星體──
位於一處將保守秘密的地方──
轉變為一副至偉的面具。 此面具將由一位、且僅一位個體佩戴！
這是偉大艦長的面具！ 佩戴此面具者就是你。
當你戴上此面具,我們將看見那雙眼眸活了過來。
當你發言,眾人將傾聽。 當你微笑,蒙福的憂特將歡欣鼓舞！
我感受到你對此計畫的興奮！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #98 · `HELLO_BEFORE_KOHRAH_SPACE_1` · 🟠

**英文原文**:
```
Suddenly I am overcome with embarrassment!
I possess the distinguished honor of addressing the legendary Earth Captain!
Please excuse my lack of proper facial appliance.
This occasion ideally calls for me to don the Expression of Ultimate Gratitude.
Eegh! I am compelled by the forceful Emanations of the Ultron to describe the appearance of the mask.
Its foundation is composed entirely of a matrix of beetle secretions and Trooba Fern
in an intricate and complex texture.
The process is extremely time-consuming since even the best-trained beetle colonies
will build a thousand rejects for every successful foundation.
Alas, it will be many years before any of the Utwig will be able to wear such a mask.
```

**Shipped v0.6-mixed**:
```
吾忽然被尷尬所襲！
吾擁有向這位傳奇之地球艦長致辭之殊榮！
請恕吾未著合宜之面部器具。
此場合理應要求吾戴上「至極感激之表情」（Expression of Ultimate Gratitude）。
咦咦！（Eegh!） 吾被厄創之強力流溢所驅，須描述此面具之外觀。
其根基完全由甲蟲分泌物與楚巴蕨（Trooba Fern）之基質組成
織就精巧複雜之紋理。
其過程極為耗時，因即使訓練最精良之甲蟲群
每建成一個成功之根基便會產出千個廢品。
痛哉！（Alas!） 尚需許多年，任何憂特方能戴上此等面具。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我忽然被尷尬所襲擊！
我擁有向這位傳奇的地球艦長致辭的殊榮！
請恕我未著合宜的面部器具。
此場合理應要求我戴上「至極感激表情」(Expression of Ultimate Gratitude)。
咦咦！（Eegh!） 我被厄創強力的流溢所驅使,必須描述此面具的外觀。
它的根基完全由甲蟲分泌物與楚巴蕨(Trooba Fern)的基質組成,
織就出精巧複雜的紋理。
此過程極為耗時,因為即便訓練最精良的甲蟲群,
每建成一個成功的根基,便會產出一千個廢品。
痛哉！（Alas!） 尚需許多年,任何憂特方能戴上這樣的面具。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #99 · `HELLO_BEFORE_KOHRAH_SPACE_2` · 🟠

**英文原文**:
```
Do my eyes deceive me? Am I a victim of a glorious vision?
I believe that I see before me the legendary Earth Captain!
We have conducted a complete survey of the Utwig
and we have convened the committee that will guide the formation of your Saintly Facade.
We eagerly anticipate the delivery of an appliance!
Imagine, when development is completed in perhaps less than ten years
you may esthetically conceal the constant reminder of your bestial aspects
and walk with pride amongst those of sophisticated intellect!
```

**Shipped v0.6-mixed**:
```
吾之眼欺吾乎？ 吾乃一光榮異象之受害者乎？
吾相信吾眼前所見乃傳奇之地球艦長！
吾等已對憂特族進行完整之調查
並召集了一委員會，將引領爾之「聖徒面容」（Saintly Facade）之成形。
吾等熱切期盼一件器具之交付！
試想，當開發完成之時──或許不到十年
爾或能以美學方式遮蔽爾獸性面相之持續提醒
並於雅緻智者之中昂首闊步！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
我的雙眼欺瞞我嗎？ 我是一個光榮異象的受害者嗎？
我相信自己眼前所見的正是那位傳奇的地球艦長！
本族已對憂特族進行了完整的調查,
並召集了一個委員會,將引領你的「聖徒面容」(Saintly Facade)之成形。
我們熱切期盼一件器具的交付！
試想,當開發完成之時──或許不到十年──
你或能以美學方式遮蔽你獸性面相的持續提醒,
並於雅緻智者之中昂首闊步！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #100 · `HELLO_DURING_KOHRAH_SPACE_1` · 🟠

**英文原文**:
```
The Ultron indicates that you must leave the area immediately! You are in extreme danger!
This area is currently controlled by either the Ur-Quan or the Kohr-Ah, we are not sure.
We are currently engaging the Kohr-Ah in an attempt to balance the conflict. Stay clear!
```

**Shipped v0.6-mixed**:
```
厄創顯示爾必須立即離開此區域！ 爾處於極端危險！
此區目前由烏寬族或柯亞控制，吾等不確定。
吾等目前正交戰柯亞以圖平衡衝突。 遠離！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
厄創顯示:你必須立即離開此區域！ 你正處於極端危險之中！
此區目前由烏寬族或柯亞控制,本族不確定。
我方目前正交戰柯亞,以圖平衡衝突。 請遠離！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #101 · `HELLO_DURING_KOHRAH_SPACE_2` · 🟠

**英文原文**:
```
Battle rages in the immediate area. Beware!
The Ur-Quan and the Kohr-Ah are engaged in a conflict of doctrinal extremes.
The Ur-Quan argument seems inferior.
You must clear the area before you become a victim of either the Ur-Quan or Kohr-Ah.
Leave now! We shall remain in an attempt to balance the conflict
so that the two forces of evil might more effectively negate each other.
```

**Shipped v0.6-mixed**:
```
戰役於周邊區域激烈進行。 當心！
烏寬族與柯亞正陷入教義極端之衝突。
烏寬族之論點似乎較低劣。
爾必須清空區域，以免爾成為烏寬族或柯亞之受害者。
現在離去！ 吾等將留下以圖平衡衝突
使兩股邪惡之力更有效地互相抵消。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
戰役在周邊區域激烈進行。 當心！
烏寬族與柯亞正陷入一場教義極端的衝突。
烏寬族的論點似乎較為低劣。
你必須清空區域,以免你成為烏寬族或柯亞的受害者。
現在請離去！ 本族將留下以圖平衡衝突,
使這兩股邪惡之力能更有效地互相抵消。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #102 · `HELLO_AFTER_KOHRAH_SPACE_1` · 🟠

**英文原文**:
```
We extend our sincere greetings to the remarkable being
that returned to the Utwig the meaning for our continued existence.
We have returned from a conflict of a grand scale with our fleet battered
but our masks of Valor and Derring-Do held high!
```

**Shipped v0.6-mixed**:
```
吾等向這位非凡之存在致以真誠之問候
是他將吾等憂特之存續意義歸還於吾等。
吾等自宏大規模之衝突歸來，艦隊受創
然吾等之「英勇無畏之面具」（Masks of Valor and Derring-Do）高舉！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
本族向這位非凡的存有致以真誠的問候──
是他將我們憂特之存續意義歸還於我方。
我們自宏大規模的衝突歸來,艦隊受創,
然而本族的「英勇無畏面具」(Masks of Valor and Derring-Do)高高舉起！
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #103 · `HELLO_AFTER_KOHRAH_SPACE_2` · 🟠

**英文原文**:
```
Ah, it is the most recently appointed Ultron Saint -- the Captain from Earth!
We flick our facial appliances collectively in a smart salute indicating both respect and gratitude.
How can we assist you?
```

**Shipped v0.6-mixed**:
```
啊，那乃最新受封之厄創聖徒──那位來自地球的艦長！
吾等集體翻動吾等之面部器具，作一俐落之敬禮，以示尊敬與感謝。
吾等如何援助爾？
```

**Rebuild v3 (v0.7 modern scholar)**:
```
啊,那正是最新受封的厄創聖徒──那位來自地球的艦長！
本族集體翻動我方的面部器具,作一俐落的敬禮,以示尊敬與感謝。
我能如何援助你？
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #104 · `UP_TO_YOU` · 🟠

**英文原文**:
```
The prognosticating harmonics of the Ultron reveal a truth.
We Utwig have done all that CAN be done to aid you.
Our tasks must now be confined to directing the many channels of causation.
Feel confident that we are using the Ultron to this end.
```

**Shipped v0.6-mixed**:
```
厄創之預示諧振揭示一項真相。
吾等憂特已做了所有能為援助爾而做之事。
吾等之任務此後必局限於指引因果之諸多渠道。
請信任吾等正為此運用厄創。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
厄創的預示諧振揭示了一項真相。
我們憂特已做了所有能為援助你而做的事。
本族的任務此後必侷限於指引因果的諸多渠道。
請相信:我們正為此目的運用厄創。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #105 · `can_you_help` · 🟠

**英文原文**:
```
Material aid from you would tilt the balance in the favor of Good.
```

**Shipped v0.6-mixed**:
```
你們的物資援助能將天平傾向「善」之一方。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
你們的物資援助將使天平朝向「善」的一方傾斜。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #106 · `HOW_HELP` · 🟠

**英文原文**:
```
Hmm... a reasonable request. Give us a second while we consult the Ultimate.
```

**Shipped v0.6-mixed**:
```
嗯…… 一合理之請求。 稍待片刻，讓吾等諮詢「至極」。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
嗯…… 一個合理的請求。 稍待片刻,讓本族諮詢「至極」。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #107 · `DONT_NEED` · 🟠

**英文原文**:
```
The Ultron confirms the evidence of our ocularities
you are strong, smart and capable.
Your fleet is at maximum strength and your ethics are sound.
Further assistance would be redundant.
```

**Shipped v0.6-mixed**:
```
厄創證實吾等眼力所見之證
爾強壯、聰明、有能力。
爾之艦隊處於最大實力，爾之倫理亦健全。
更多之協助將屬多餘。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
厄創證實了本族肉眼所見的證據──
你強壯、聰明,且有能力。
你的艦隊處於最大實力,你的倫理亦為健全。
更多的協助將屬多餘。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #108 · `HAVE_4_SHIPS` · 🔴

**英文原文**:
```
Just so. The Ultron has hummed its assent.
Take possession of four of our Jugger craft this instant!
```

**Shipped v0.6-mixed**:
```
正是。 厄創已鳴響其贊同。
此刻取走吾等之四艘重砲艦！
```

**Rebuild v3 (v0.7 modern scholar)**:
```
正是。 厄創已鳴響它的贊同。
此刻,請取走本族的四艘重砲艦(Jugger)！
```

**推薦**: 🟢 v3 (整體語體翻轉;shipped 使用文言不符 v0.7 dossier)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #109 · `NO_ULTRON_AT_BOMB` · 🟠

**英文原文**:
```
Foolish tricksters! Don't you know the Druuge tried that ploy on us just a few days ago?
You say you have the Ultron, that you wish to return it to us... LIES!
The moment our back is turned, you will sneak down to the surface of this world
and deprive us of our destructive device of dignity.
If you truly had our Ultron, repaired to its state of perfection
you would surely take it to the Proctors at our homeworld at <% comm.getStarName("Beta Aquarii", "utwig") %>.
Speak no more of this subject.
```

**Shipped v0.6-mixed**:
```
愚蠢之騙徒！ 爾豈不知毒賈族數日前才對吾等玩過此招？
爾言擁有厄創，欲將其歸還吾等……謊言！
爾等一轉頭，便將偷偷潛至此世界之表面
奪走吾等尊嚴之毀滅性裝置。
若爾當真擁有吾等之厄創，且已修復至圓滿狀態
爾必當將其送至吾等母星之監督團所在，即 <% comm.getStarName("寶瓶座β", "utwig") %>。
勿再言及此事。
```

**Rebuild v3 (v0.7 modern scholar)**:
```
愚蠢的騙徒！ 你難道不知道毒賈族數日前才對本族玩過此招？
你聲稱擁有厄創,想將它歸還我方……謊言！
你們一轉頭,便會偷偷潛至此世界的表面,
奪走我們尊嚴之毀滅性裝置。
你若當真擁有本族的厄創,且已將它修復至圓滿的狀態,
你必定會將它送至我們母星的監督團所在,即 <% comm.getStarName("寶瓶座β", "utwig") %>。
勿再言及此事。
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---

### #110 · `OUT_TAKES` · 🟠

**英文原文**:
```
Hello again, heroic humanoid!
Ever since you returned the Ultron to us
everything has been WONDERFUL... just perfect!
Within just two days our factories will begin churning out
appropriate facial appliances, and I have already picked out my first mask
the Domino of Unrivaled Merriment!
Yes, we are all ecstatic... even the High Proctor gambols
as she performs the Exultant Caper of Revelation!
Look how she leaps with the Ultron held high!
How she twists, how she twirls, how she slips and tosses the Ultron into the air... OH NOOooooo!!!
(CRASH!!)
```

**Shipped v0.6-mixed**:
```
再次相見，英勇之人形生物！
自爾將厄創歸還吾等以來
一切皆美妙……完美無瑕！
僅兩日之內，吾等之工坊便將開始大量產出
合宜之面部器具，而吾已為吾自己挑好第一副面具
即「無比歡樂之多米諾面具」（Domino of Unrivaled Merriment）！
是的，吾等皆狂喜……即便是高階監督者
於她表演「啟示狂歡跳躍」（Exultant Caper of Revelation）之時亦嬉戲跳躍！
看她高舉厄創躍動！
看她如何扭轉、如何旋轉、如何失手將厄創拋向空中……噢，不噢噢噢噢──！！！
（砰！！）
```

**Rebuild v3 (v0.7 modern scholar)**:
```
再次相見,英勇的人形生物！
自從你將厄創歸還我們以來,
一切皆美妙……完美無瑕！
僅在兩日之內,我們的工坊便將開始大量產出
合宜的面部器具,而我已為自己挑好第一副面具──
即「無比歡樂多米諾面具」(Domino of Unrivaled Merriment)！
是的,蒙福的憂特皆狂喜……即便是高階監督者,
在她表演「啟示歡騰躍舞」(Exultant Caper of Revelation)之時亦嬉戲跳躍！
看她高舉厄創躍動！
看她如何扭轉、如何旋轉、如何失手將厄創拋向空中……噢,不噢噢噢噢──！！！
(砰！！)
```

**推薦**: 🟢 v3 (v0.7 現代學者風格)

**你的選擇**: A (v3) / B (shipped) / C (自訂)

---
