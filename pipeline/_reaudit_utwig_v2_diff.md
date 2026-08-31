# Utwig Rebuild-Compare Diff Report (2026-08-15)

## 統計

- Total tokens: 114
- 🟢 完全相同: 5 (4.4%)
- 🟡 微調 (等價): 2 (1.8%)
- 🟠 措辭改變: 13 (11.4%)
- 🔴 語意/voice 差異大: 94 (82.5%)

## Anchoring-Risk 標記

以下 12 tokens 在 Phase 1.5 意外看見 shipped 譯文 (user 選項 B 授權繼續執行)。若 diff 中此 12 tokens 的 rebuild 與 shipped 相似度 >30% 需視為 anchoring 污染 (per §六情境 B):

- ⚠️ **NEUTRAL_SPACE_HELLO_1**: 🔴 semantic
- ⚠️ **NEUTRAL_SPACE_HELLO_2**: 🔴 semantic
- ⚠️ **HOSTILE_SPACE_HELLO_1**: 🟠 phrasing
- ⚠️ **HOSTILE_SPACE_HELLO_2**: 🔴 semantic
- ⚠️ **BOMB_WORLD_HELLO_1**: 🟠 phrasing
- ⚠️ **BOMB_WORLD_HELLO_2**: 🟠 phrasing
- ⚠️ **HOSTILE_BOMB_HELLO_1**: 🟠 phrasing
- ⚠️ **HOSTILE_BOMB_HELLO_2**: 🔴 semantic
- ⚠️ **NEUTRAL_HOMEWORLD_HELLO_1**: 🔴 semantic
- ⚠️ **NEUTRAL_HOMEWORLD_HELLO_2**: 🔴 semantic
- ⚠️ **NEUTRAL_HOMEWORLD_HELLO_3**: 🟡 minor
- ⚠️ **NEUTRAL_HOMEWORLD_HELLO_4**: 🔴 semantic

**Anchoring 檢查**: 12 tokens 中 0 個完全相同 = 0%. 
✅ <30% 相同 = anchoring 影響可控。

---

## 差異項 (只列 🟡🟠🔴,不列 🟢)

### 🟡 微調 (等價) (2 tokens)

#### #1 · NEUTRAL_HOMEWORLD_HELLO_3 · 🟡 ⚠️ ANCHORING-RISK

**英文原文**:
```
You disturb our routine of eternal grieving
yet we extend to you the courtesy of acknowledgment.
```

**Shipped**:
```
爾擾亂了吾等永恆哀悼之常軌
然吾等仍以承認爾之禮儀致意。
```

**Rebuild v2**:
```
爾擾亂了吾等永恆哀悼之常軌
然吾等仍以承認之禮儀致意。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #2 · we_are_vindicator · 🟡

**英文原文**:
```
This is Captain <% state.sis.getCaptainName() %>, representing <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>. Please respond.
```

**Shipped**:
```
我是 <% state.sis.getCaptainName() %> 艦長，代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>。 請回應。
```

**Rebuild v2**:
```
我方為 <% state.sis.getCaptainName() %> 艦長，代表 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %>。 請回應。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

### 🟠 措辭改變 (13 tokens)

#### #3 · HOSTILE_SPACE_HELLO_1 · 🟠 ⚠️ ANCHORING-RISK

**英文原文**:
```
Yagh! Your attitude toward us is not acceptable!
We apologize for having to deal with you this way,
but since the loss of the Ultron, we have no choice.
As we prepare to die, so should you.
```

**Shipped**:
```
呀哈！（Yagh!） 爾對吾等之態度不可容忍！
吾等對必須以此方式對待爾深感抱歉，
然自厄創失落以來，吾等別無選擇。
吾等既將赴死，爾亦當如是。
```

**Rebuild v2**:
```
呀哈！（Yagh!） 爾對吾等之態度令人無法容忍！
吾等為必須以此方式應對爾深表歉意，
然自厄創失落以來，吾等別無選擇。
吾等既預備赴死，爾亦當如是。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #4 · BOMB_WORLD_HELLO_1 · 🟠 ⚠️ ANCHORING-RISK

**英文原文**:
```
Attention alien vessel: this world is under the full jurisdiction of the Utwig Proctorate.
We extend a subdued but civil greeting.
```

**Shipped**:
```
注意，外星艦艇：此世界完全處於憂特監督團之管轄下。
吾等致以低沉但有禮之問候。
```

**Rebuild v2**:
```
注意，外星艦艇：此世界完全處於憂特監督團之管轄下。
吾等向仁慈的星際旅人致以壓抑卻有禮之問候。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #5 · BOMB_WORLD_HELLO_2 · 🟠 ⚠️ ANCHORING-RISK

**英文原文**:
```
You have arrived at a most inopportune time.
Collectively, our species is dealing with a great remorse.
Nevertheless in order to foster a spirit of interspecies good will
we pull ourselves from our intense cycle of self-analysis
and offer this greeting which, we hope, will suffice.
```

**Shipped**:
```
爾於最不宜之時刻蒞臨。
吾族集體正處於巨大悔恨之中。
然為增進種族間之善意
吾等自濃烈之自省循環中抽身
並致以此問候，期能勉強應酬。
```

**Rebuild v2**:
```
爾於最不宜之時刻蒞臨。
吾族集體正處於巨大悔恨之中。
然而為促進種族間之善意
吾等自濃烈之自省循環中抽身
獻上此問候，冀能足矣。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #6 · HOSTILE_BOMB_HELLO_1 · 🟠 ⚠️ ANCHORING-RISK

**英文原文**:
```
Oh, woe! We find your presence here disconcerting.
In order to deal with the situation in such a way that we maintain some semblance of authority
we are forced to deploy our forces against your armada.
Prepare yourselves for battle.
```

**Shipped**:
```
喔，痛哉！（Oh, woe!） 吾等發覺爾之存在令人不安。
為維持一絲權威之表象處理此情況
吾等不得不部署武力對付爾之艦隊。
爾等，準備戰鬥。
```

**Rebuild v2**:
```
喔，悲夫！（Oh, woe!） 吾等覺爾之存在令人不安。
為以維持一絲權威之表象應對此局面
吾等不得不動員武力對抗爾之艦隊。
爾等，備戰。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #7 · TRICKED_US_1 · 🟠

**英文原文**:
```
I expected no less.
You hold before us nothing more than a reminder of a past mistake that offends us to no end.
We now commence your termination.
```

**Shipped**:
```
本族並不意外。
爾於吾等面前所持之物，不過是一段過去錯誤之無盡冒犯之提醒。
吾等現在開始爾之終結。
```

**Rebuild v2**:
```
吾早已料及。
爾於吾等面前所持之物，不過是無盡冒犯吾等之過往錯誤之提醒。
吾等現即開始爾之終結。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #8 · real_sorry_about_ultron · 🟠

**英文原文**:
```
Sniff. That reminds me when my pet dog Splib ran in front of a... rock chipper!
```

**Shipped**:
```
哭。 那讓我方想起我方的寵物狗小普利（Splib）跑到一台…… 石頭切碎機前面！
```

**Rebuild v2**:
```
抽泣。 這讓我方想起我方的寵物狗小普利（Splib）跑到……一台碎石機前面的事！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #9 · what_about_you_3 · 🟠

**英文原文**:
```
Hmm, sounds like things were going pretty well. So what happened?
```

**Shipped**:
```
嗯，聽起來事情進展相當順利。 那後來怎麼了？
```

**Rebuild v2**:
```
嗯，聽起來事情原本挺順利。 那後來怎麼了？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #10 · what_about_urquan_2 · 🟠

**英文原文**:
```
Yes, that is really a pity. So what more do you know about the Kohr-Ah?
```

**Shipped**:
```
是啊，那真令人惋惜。 那你們對柯亞還知道些什麼？
```

**Rebuild v2**:
```
是的，那確實令人惋惜。 那你們對柯亞還知道些什麼？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #11 · got_ultron · 🟠

**英文原文**:
```
Hey guys, guess what we've got! We've got THE ULTRON! Wanna see it?
```

**Shipped**:
```
喂各位，猜猜我方帶了什麼！ 我方拿到**厄創**了！ 想看嗎？
```

**Rebuild v2**:
```
喂各位，猜猜我方拿到什麼？ 我方拿到厄創了！ 想看嗎？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #12 · GOODBYE_NEUTRAL · 🟠

**英文原文**:
```
As do we. Go now with neither malice nor joy.
```

**Shipped**:
```
吾等亦然。 走吧，不帶惡意亦不帶喜悅。
```

**Rebuild v2**:
```
吾等亦然。 且去吧，不帶惡意亦不帶歡愉。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #13 · DO_THIS_BEFORE_SPACE · 🟠

**英文原文**:
```
Your request is within our capabilities. One moment
Mmmm, emanations from the Ultron... orange furry air breathes tender yawns
Yes, it all becomes clear now... you must do something with the great Bomb
the Precursor relic we kept at <% comm.getStarName("Zeta Hyades", "bomb") %> VI-B.
It seems that this Bomb must be, ah...
eaten?... no. Hugged?... no
...
```

**Shipped**:
```
爾之請求在吾等能力之內。 稍待片刻
嗯，來自厄創之流溢…… 橘色毛茸茸的空氣呼出溫柔之呵欠
是的，一切變得清晰了…… 爾必須對那件偉大之「炸彈」做點事
那件吾等留於 <% comm.getStarName("畢宿星團ζ", "bomb") %> （Zeta Hyades） VI-B 之先驅者遺物。
看來此「炸彈」必須被，啊……
吃掉？…… 不。 擁抱？…… 不
啊！ **改良**！ 就是它！ 此「炸彈」必須被改良以實現其最終命運！
```

**Rebuild v2**:
```
爾之請求在吾等之能力範圍內。 稍待
唔嗯，來自厄創之流溢……橘色毛絨的空氣呼出溫柔的哈欠
是的，一切現在都清楚了……爾必須對那大炸彈做些什麼
即吾等保管於 <% comm.getStarName("畢宿星團ζ", "bomb") %> VI-B 之先驅者遺物。
看來此炸彈必須，啊……
吃掉？……不。 擁抱？……不
啊！ 改良！ 就是了！ 此炸彈必須被改良以完成其最終之天命！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #14 · GOODBYE_BEFORE_SPACE · 🟠

**英文原文**:
```
There is much for us to do. May the Ultron be with you!
```

**Shipped**:
```
吾等尚有諸多事要做。 願厄創與爾同在！
```

**Rebuild v2**:
```
吾等尚有諸多事宜要做。 願厄創與爾同在！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #15 · FLEET_ON_WAY · 🟠

**英文原文**:
```
Even as I utter these words, the combined military resource of both the Utwig and Supox
proceed toward <% comm.getConstellation("Horologii", "samatra") %> to intercept the Kohr-Ah.
Besides the importance of our efforts, the Ultron indicates
all futures which include our survival are contingent on the actions that you now take.
```

**Shipped**:
```
即使本族此刻說出這些話，憂特與蘇菩之聯合軍事資源
正朝 <% comm.getConstellation("時鐘座", "samatra") %> 前進以攔截柯亞。
除了吾等之努力之重要性外，厄創顯示
所有包含吾等生存之未來皆取決於爾此刻所採取之行動。
```

**Rebuild v2**:
```
即便吾說此言之際，憂特與蘇菩族之合體軍事資源
正前往 <% comm.getConstellation("時鐘座", "samatra") %> 攔截柯亞。
除吾等努力之重要性外，厄創指出
一切包含吾等存續之未來，皆繫於爾此刻所採取之行動。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

### 🔴 語意/voice 差異大 (94 tokens)

#### #16 · NEUTRAL_SPACE_HELLO_1 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
Ugh. I suppose, as a courtesy, I should extend an appropriate greeting.
On behalf of the Utwig Proctors I truly hope, for your sake
that your day has been better than ours
although this really isn't saying that much.
```

**Shipped**:
```
呃。 想來，出於禮儀，本族應致以適當之問候。
代表憂特監督者，本族真心希望，為爾之故
爾今日之時光比吾等更佳
儘管此等祈願實在說不上什麼。
```

**Rebuild v2**:
```
唉。 想來，出於禮儀，本族應當向仁慈的星際旅人致以合宜之問候。
代表憂特監督者，吾衷心期盼，為爾之故
爾今日之光陰能勝過吾等
儘管此願實在說不上什麼。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #17 · NEUTRAL_SPACE_HELLO_2 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
Just go away. Leave us to ponder our grief.
```

**Shipped**:
```
走吧。 讓吾等自沉哀思。
```

**Rebuild v2**:
```
去吧。 留吾等獨自沉思哀傷。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #18 · HOSTILE_SPACE_HELLO_2 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
You have caught us in a private, dark moment.
We must guarantee your silence with your complete and total destruction.
```

**Shipped**:
```
爾於吾等私密之黑暗時刻闖入。
吾等必須以爾之完全徹底之毀滅來確保爾之緘默。
```

**Rebuild v2**:
```
爾於吾等私密黑暗之時刻擾我。
吾等必須以爾徹底全然之毀滅，來確保爾之緘默。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #19 · HOSTILE_BOMB_HELLO_2 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
In a fit of depression I find it necessary to vent my irreconcilable frustration on you.
I normally do not engage in such fervent activities
but I now find myself inspired to do my best to annihilate you with expediency.
```

**Shipped**:
```
於憂鬱之發作中，本族發覺必須將無法排解之挫敗發洩於爾。
本族一般不從事此等激烈活動
然本族此刻竟感靈感湧現，盡力迅速將爾殲滅。
```

**Rebuild v2**:
```
於憂鬱之發作中，吾覺有必要將無可調解之挫折發洩於爾。
吾平日不從事此等激烈之活動
然此刻竟感靈感湧現，將竭力盡速殲滅爾等。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #20 · NEUTRAL_HOMEWORLD_HELLO_1 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
Normally we would not bother to acknowledge your presence
but you find us in a state of moderate depression
instead of our normal cycle of self-destructive tendencies.
```

**Shipped**:
```
通常吾等不會費心承認爾之存在
然爾發覺吾等正處於中度憂鬱之狀
而非吾等平常之自毀傾向循環。
```

**Rebuild v2**:
```
平日吾等不會費心承認爾之存在
然爾此時遇上悲慘的憂特正處中度憂鬱之狀
而非吾等常態之自毀循環。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #21 · NEUTRAL_HOMEWORLD_HELLO_2 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
Alien vessel, grieve for the loss of both the Utwig and the Universe at large.
```

**Shipped**:
```
外星艦艇，為憂特之失落與整個宇宙之失落哀悼吧。
```

**Rebuild v2**:
```
外星艦艇，為失落的憂特與寰宇整體之失落，一同哀悼吧。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #22 · NEUTRAL_HOMEWORLD_HELLO_4 · 🔴 ⚠️ ANCHORING-RISK

**英文原文**:
```
I am so depressed. You can try to cheer me up if you want to.
```

**Shipped**:
```
本族好憂鬱。 若爾願，可試著讓本族振作。
```

**Rebuild v2**:
```
吾好憂鬱。 爾若願意，可試著讓吾振作。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #23 · HOSTILE_HOMEWORLD_HELLO_1 · 🔴

**英文原文**:
```
You have angered the spirit of the Utwig.
Although depressed almost to the point of an inability to perform any actions whatsoever
we find within ourselves the verve required to engage you in a duel to the death.
Indeed, we will find satisfaction in your demise or in our release from our mortal burden.
```

**Shipped**:
```
爾激怒了憂特之靈。
儘管吾等憂鬱至幾乎無法執行任何動作
吾等仍於自身之內找到與爾展開生死決鬥所需之勁力。
確實，吾等或於爾之殞命中、或於吾等自凡世重擔之解脫中，尋得滿足。
```

**Rebuild v2**:
```
爾已激怒罪惡的戴面具者之靈魂。
儘管吾等憂鬱幾近無法採取任何行動之地步
仍於自身尋得與爾一決生死所需之熱忱。
誠然，吾等將於爾之殞歿中尋得滿足，或於自身凡塵重擔之解脫中尋得滿足。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #24 · HOSTILE_HOMEWORLD_HELLO_2 · 🔴

**英文原文**:
```
Attention offending vessel! Your presence here is deeply appreciated!
You have stirred us from our depression-induced apathy
to the point where our desire actually registers as a sensation!
We look forward to either finding personal release in the netherworld
or obliterating you successfully.
We thank you for this opportunity!
```

**Shipped**:
```
注意，冒犯之艦艇！ 爾於此之存在深受吾等感激！
爾將吾等自憂鬱誘發之冷漠中喚醒
以致吾等之慾望竟真正登記為感覺！
吾等期待或於冥界之個人解脫
或成功將爾殲滅。
吾等感謝爾此一機會！
```

**Rebuild v2**:
```
注意，冒犯之艦艇！ 爾之蒞臨令吾等深深感激！
爾已將吾等自憂鬱誘發之淡漠中喚起
以致吾等之意欲竟得以化為知覺！
吾等期盼於冥府中尋得個人之解脫
或成功將爾盡數殲滅。
感謝爾賜予此機遇！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #25 · why_you_here · 🔴

**英文原文**:
```
For what purpose do you linger at this location?
```

**Shipped**:
```
爾等因何目的滯留於此地？
```

**Rebuild v2**:
```
你們為何滯留於此處？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #26 · WE_GUARD_BOMB · 🔴

**英文原文**:
```
We are the stewards of the Bomb.
We keep it from those who would use it unwisely.
In addition, we are prepared to act under the direction of the Proctorate
should we decide to make a final atonement for our most grievous blunder.
```

**Shipped**:
```
吾等乃「炸彈」之守護者。
吾等使其遠離不智之用途者。
此外，吾等已準備妥當，聽從監督團之指令行事
若吾等決意為自身最嚴重之過失作出最終贖罪。
```

**Rebuild v2**:
```
吾等哀嘆之族，為此炸彈之守護者。
吾等保其遠離不智使用之徒。
此外，吾等預備隨時聽從監督團之指示行動
倘若吾等決意為此極其嚴重之過錯作最終之贖罪。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #27 · what_about_bomb · 🔴

**英文原文**:
```
Hmm, this must be a pretty special Bomb to have all of you keeping an eye on it.
```

**Shipped**:
```
唔，這一定是顆挺特別的「炸彈」，才會需要你們全部盯著。
```

**Rebuild v2**:
```
嗯，這炸彈想必挺特別，能讓你們一群人都盯著它。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #28 · ABOUT_BOMB · 🔴

**英文原文**:
```
You are correct. It is a relic of Precursor origin.
It has the power to destroy entire planetary objects, perhaps even galaxies.
The Utwig have been entrusted by fate to watch over this device
so that it will be used in the way that it was intended by destiny.
```

**Shipped**:
```
爾所言不虛。 其乃先驅者起源之遺物。
其擁有摧毀整個行星，甚至或許整個星系之力量。
憂特由命運所託，守護此裝置
以確保其將依命運所安排之方式使用。
```

**Rebuild v2**:
```
爾言正是。 其乃先驅者遺物。
其力足以摧毀完整之行星，甚或整個星系。
命運將此裝置託付憂特看管
使其得以按天命所定之方式使用。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #29 · give_us_bomb_or_die · 🔴

**英文原文**:
```
We have an urgent need for this device. Give us the Bomb.
```

**Shipped**:
```
我方對此裝置有緊急需求。 把「炸彈」交出來。
```

**Rebuild v2**:
```
我方急需此裝置。 把炸彈交出來。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #30 · GUARDS_WARN · 🔴

**英文原文**:
```
We cannot relinquish control of this instrument of power!
You cannot have the Bomb.
Any attempt on your part to change this current arrangement
will be met with fearsome Utwig resistance!
```

**Shipped**:
```
吾等不可放棄對此力量工具之控制！
爾不可持有「炸彈」。
爾之任何試圖改變此現狀之嘗試
將遭遇令人畏懼之憂特抵抗！
```

**Rebuild v2**:
```
吾等豈能放棄此力量之利器！
爾不得擁有此炸彈。
爾若企圖改變此當前之安排
必遭憂特可怖之抵抗！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #31 · demand_bomb · 🔴

**英文原文**:
```
We will now take the Bomb. Give it to us.
```

**Shipped**:
```
我方現在就要拿走「炸彈」。 交出來。
```

**Rebuild v2**:
```
我方這就要取走炸彈。 交出來。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #32 · GUARDS_FIGHT · 🔴

**英文原文**:
```
Our anguish serves only to fuel our resolve concerning the jurisdiction of this device.
We stand ready!
```

**Shipped**:
```
吾等之痛楚僅為吾等對此裝置管轄權之決心添薪。
吾等已備戰！
```

**Rebuild v2**:
```
吾等之苦痛，只增強吾等對此裝置管轄之決心。
吾等已然備妥！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #33 · may_we_have_bomb · 🔴

**英文原文**:
```
Wow, that is pretty neat! May we have the Bomb?
```

**Shipped**:
```
哇，這可挺酷的！ 我方能拿「炸彈」嗎？
```

**Rebuild v2**:
```
哇，那還挺酷的！ 我方可以擁有那顆炸彈嗎？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #34 · NO_BOMB · 🔴

**英文原文**:
```
Yes, it IS a remarkable device.
It is understandable that you would like to possess it yourselves.
Our mandate, however, requires that we maintain full control of the Bomb.
```

**Shipped**:
```
誠然，其**乃**卓越之裝置。
爾自身欲擁有之，實可理解。
然吾等之使命要求吾等對「炸彈」保持完全控制。
```

**Rebuild v2**:
```
是的，此裝置著實非凡。
爾等欲親自擁有之，此亦可理解。
然吾等之使命，要求吾等維持對炸彈之完全掌控。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #35 · please · 🔴

**英文原文**:
```
Oh, please can't we have it? It would make us really happy!
```

**Shipped**:
```
喔，拜託咱們能不能拿？ 那可讓我方超開心！
```

**Rebuild v2**:
```
噢，拜託嘛，讓我方擁有它不行嗎？ 我方會超開心的！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #36 · SORRY_NO_BOMB · 🔴

**英文原文**:
```
No, we are sorry. You cannot have the Bomb.
Besides being against our orders, imagine what would happen if for some reason
our Proctors decide to use it to destroy our civilization.
How would we explain its absence?
```

**Shipped**:
```
不行，吾等抱歉。 爾不可持有「炸彈」。
且此不僅違反吾等之令，試想若因某故
吾等監督者決意用之毀滅吾等自身之文明。
吾等該如何解釋其缺席？
```

**Rebuild v2**:
```
不，吾等甚感抱歉。 爾不得擁有此炸彈。
除違反吾等之命令外，設想若因故
吾等之監督者決意以其摧毀吾等之文明
吾等又將如何解釋炸彈之下落？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #37 · whats_up_bomb · 🔴

**英文原文**:
```
Tell us about the Bomb. What's the scoop?
```

**Shipped**:
```
跟我方講講「炸彈」吧。 內幕如何？
```

**Rebuild v2**:
```
說說這炸彈吧。 有什麼內情？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #38 · GENERAL_INFO_BOMB_1 · 🔴

**英文原文**:
```
During standard exploration procedures we came across what appeared to be
an ancient Precursor supply base.
It had been dismantled and appeared to be empty.
In the staging area there was a collection of what appeared to be refuse.
During the cataloging of these various items, this device was discovered in a damaged container.
From what our scientists can tell, it appears to be a planeteering tool
...
```

**Shipped**:
```
於標準勘探程序中，吾等發現似為
某古先驅者補給基地。
其已被拆解，看似空無一物。
於整備區有一堆看似廢棄物之物。
於編目此等各項物品時，此裝置於一破損之容器中被發現。
以吾等科學家所能判定，其似為一行星工程工具
可將月亮大小之物體化為顆粒塵雲。
吾等相信其或為意外遺忘
或僅因離去之艦艇缺乏空間而留下。
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #39 · GENERAL_INFO_BOMB_2 · 🔴

**英文原文**:
```
The Bomb may have been left here by mistake.
We suspect that if activated, it will turn this entire planet
into nothing more than an expanding mass of tiny dirt clods.
The Utwig have considered carefully that perhaps it would be best to use this device
to put us out of our collective misery.
Although this may sound extreme, I will point out that our mishandling of the Ultron
...
```

**Shipped**:
```
此「炸彈」或為錯留於此。
吾等猜測若啟動之，其將把此整個行星
化為不過是一團擴散之塵屑。
憂特已仔細考慮，或許以此裝置
終結吾等之集體苦難乃最佳之選。
儘管此聞來或極端，本族要指出
吾等對厄創之失手乃史詩級之災難。
```

**Rebuild v2**:
```
此炸彈或係誤留於此。
吾等疑其若啟動，將把此整顆行星
化為一團向外擴散之微小土塊。
憂特已慎重考慮，或許最佳之途
乃以此裝置終結吾等之集體悲愴。
此聽來或極端，然吾當指出，吾等對厄創之失手
乃一場史詩級之災難。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #40 · bye_bomb · 🔴

**英文原文**:
```
This Bomb is pretty dangerous and you guys are crazy. I'm getting out of here!
```

**Shipped**:
```
這「炸彈」蠻危險的，你們也怪怪的。 我方要離開了！
```

**Rebuild v2**:
```
這炸彈挺危險的，你們也太瘋了。 我先閃了！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #41 · GOODBYE_BOMB · 🔴

**英文原文**:
```
Ha ha, don't worry. Hey! I laughed! How could I do that?
Now I sink into a depression that leaves me speechless.
```

**Shipped**:
```
哈哈，別擔心。 喂！ 本族笑了！ 本族怎能如此？
如今本族沉入令我無語之憂鬱。
```

**Rebuild v2**:
```
哈哈，勿慌。 咦！ 吾竟笑了！ 吾豈能如此？
如今吾沉入令吾語塞之憂鬱之中。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #42 · hey_wait_got_ultron · 🔴

**英文原文**:
```
Whoa there, hold your horses! Look at this! We've got your Ultron!
```

**Shipped**:
```
喔喂，等一下！ 看這個！ 我方帶著爾等的厄創來了！
```

**Rebuild v2**:
```
喔喔慢著，別急啊！ 你看這個！ 我方拿到你們的厄創了！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #43 · TAUNT_US_BUT_WE_LOOK · 🔴

**英文原文**:
```
Taunting us buys you nothing except to steel our resolve to end your existence.
In fact, we will humor you in your little game.
You have seconds to show us whatever bric-a-brac you possess.
We will then commence with the cessation of your existence.
```

**Shipped**:
```
嘲笑吾等除了堅定吾等終結爾存在之決心外，別無所獲。
事實上，吾等將姑息爾之小遊戲。
爾有數秒展示爾所擁有之任何無足輕重之物。
然後吾等將開始爾之終結。
```

**Rebuild v2**:
```
嘲弄吾等於爾一無所獲，只能堅定吾等終結爾存在之決心。
事實上，吾等將姑且陪爾玩此小小遊戲。
爾有數秒可展示爾所擁之任何破爛雜物。
接著吾等便將開始終止爾之存在。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #44 · TRICKED_US_2 · 🔴

**英文原文**:
```
I am speechless with rage... and yet, I must speak!
How dare you flaunt the collective embarrassment of the Utwig?!
You will now pay for your severe breach of etiquette!
```

**Shipped**:
```
本族氣得語塞…… 然本族必須說話！
爾竟敢炫耀憂特之集體恥辱？！
爾將為爾嚴重違反禮儀付出代價！
```

**Rebuild v2**:
```
吾憤怒得語塞……然吾又必須開口！
爾竟敢炫耀憂特集體之難堪？!
爾此刻將為此嚴重之失禮付出代價！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #45 · WOULD_BE_HAPPY_BUT · 🔴

**英文原文**:
```
What good would that do -- I mean, why should we?
We agonized for hours wondering if it was a cruel twist of fate
or simply a serious case of butterfingery.
Ah, the lifetimes that have been spent in the pursuit of the elusive answer
to this deceptively simple question has driven many of us down the dark road of self-destruction.
Indeed, even as these words strike the ears of any who care to listen
...
```

**Shipped**:
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

**Rebuild v2**:
```
如此又能有何益處── 吾意，吾等何必為之？
吾等苦思數小時，思忖此究係命運之殘酷扭曲
抑或僅是嚴重之手滑一場。
啊，多少代之生命耗於追尋此看似簡單問題之難解答案
致使吾等許多人步上自毀之陰暗道途。
誠然，即便此言此刻正撞入任何願聽者之耳
真正之問題是：此事重要嗎？ 吾說不出，吾深陷困境之中
無以決斷何者能更妥地為吾於大罪中所擔之份贖罪。
吾當緩慢而痛苦地自我了結？
吾當投身漫長痛苦之自我鞭笞？
吾當熱忱地投入集體湮滅之議題？
吾不知。 即便此刻，吾之心靈仍於猶疑之痛楚中扭動，唯恐結果不足。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #46 · why_sad · 🔴

**英文原文**:
```
Hmm, I detect that recent events have not gone your way. Why don't you start at the beginning?
```

**Shipped**:
```
唔，我方察覺最近發生的事對你們不太順利。 何不從頭說起？
```

**Rebuild v2**:
```
嗯，我察覺你們最近諸事不順。 何不從頭說起？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #47 · ULTRON_BROKE · 🔴

**英文原文**:
```
*Sigh* All right, I'll try, but you know, it really doesn't matter.
After all, we have a famous Utwig saying: when one loses the reason for existence
one tends to get less motivated.
This goes hand-in-hand with the painfully appropriate credo
`We broke it so we are paying for it'.
Of course, this isn't really accurate; the situation is so much more hideous!
...
```

**Shipped**:
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

**Rebuild v2**:
```
*嘆息*（*Sigh*） 好吧，吾將盡力，然爾知曉，此事實在不重要。
畢竟，吾等有句知名之憂特諺語：當一者失去存在之理由
其動力便趨於低落。
此與此痛切合宜之信條攜手同行:
「吾等損之，故吾等償之」。
當然此並非全然準確；情勢遠比此淒厲得多！
爾若能想像，掌中握著答案本身！……
……卻只見它以昔日之潛能嘲弄爾！
啊，殘酷之諷刺！ 厄創之失落令吾等萬般悲愴！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #48 · what_ultron · 🔴

**英文原文**:
```
Um, yes, of course, the Ultron. We grieve. How sad. Now, what was it again?
```

**Shipped**:
```
呃，是的，當然，厄創。 我方為你們哀悼。 多悲傷。 那，它到底是什麼來著？
```

**Rebuild v2**:
```
呃，對，當然，厄創。 我方哀傷。 好悲傷。 話說回來，那是啥東西來著？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #49 · GLORIOUS_ULTRON · 🔴

**英文原文**:
```
Bah! It doesn't matter! Besides being of no concern to you
I find discussion of this matter, well, distasteful.
*Sigh.* The Ultron was not only the thing which assures total and complete meaning of life for you and I
it is Universal; I'm sure that you too are aware of this thing if only in legend!
It granted us all limitless power and knowledge.
It has been since, well, rendered inoperative.
```

**Shipped**:
```
呸！（Bah!） 這無關緊要！ 除了與爾無關之外
本族發現討論此事，嗯，令人不快。
（嘆氣。）厄創不僅是為爾我確保生命完全徹底之意義之物
其更是「宇宙的」；本族確信爾對此物即使只從傳說中亦有所聞！
其賜予吾等所有無限之力量與知識。
它自從……嗯，已然失效。
```

**Rebuild v2**:
```
呸！（Bah!） 這無關緊要！ 除了與爾無涉之外
吾覺討論此事……嗯，令人厭惡。
*嘆息*（*Sigh.*） 厄創不僅乃確保爾我生命之絕對圓滿意義之物
其乃宇宙至物；吾深信爾亦有耳聞，哪怕僅於傳說之中！
其賜予吾等無盡之力量與知識。
自此，其便，唔，陷於失效。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #50 · dont_be_babies · 🔴

**英文原文**:
```
Just because you busted your Ultra-thingy, don't be a bunch of cry-babies!
```

**Shipped**:
```
只不過弄壞了你們的厄玩意兒，別當一群哭啼的娃兒！
```

**Rebuild v2**:
```
就算你們搞壞了那什麼厄創破爛玩意兒，也別當一群愛哭鬼啊！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #51 · MOCK_OUR_PAIN · 🔴

**英文原文**:
```
Gah! Now you've really done it!
Your blatant transgressions have me hopping mad!
Hop hop hop! Okay, that's it! Put up your dukes! Nobody makes fun of the Ultron!
```

**Shipped**:
```
哈！（Gah!） 爾這下可真惹到本族了！
爾之公然冒犯讓本族火冒三丈！
跳跳跳！ 好，就這樣！ 拿起拳頭來！ 沒人可以嘲笑厄創！
```

**Rebuild v2**:
```
嘎！（Gah!） 爾此下當真惹惱吾了！
爾之公然放肆令吾勃然大怒！
蹦！蹦！蹦！ 好吧，夠了！ 亮傢伙來吧！ 沒人可拿厄創開玩笑！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #52 · APPRECIATE_SYMPATHY · 🔴

**英文原文**:
```
You are kind. If we could wield the Ultron to resurrect your Splib, we would.
But I suddenly am overcome with waves of depression.
I must retire now to perform rituals of anguish.
Waves of trauma wash across my being even now. I must go.
```

**Shipped**:
```
爾真仁慈。 若吾等能揮動厄創使爾之小普利復活，吾等定會如是。
然本族忽然被憂鬱之浪淹沒。
本族此刻須告退，執行痛楚之儀式。
創傷之浪甚至此刻仍衝擊本族之存在。 本族必須走了。
```

**Rebuild v2**:
```
爾甚善良。 若吾等能運用厄創使爾之小普利復活，吾等必為之。
然吾忽被數波憂鬱襲來。
吾必須退去，以行痛苦之儀式。
創傷之波浪此刻仍席捲吾之存在。 吾必須離去。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #53 · what_about_you_1 · 🔴

**英文原文**:
```
A truly unique set of events put you in your current state. Am I right?
```

**Shipped**:
```
一連串真正獨特的事件讓你們陷入現在的狀態。 我方沒說錯吧？
```

**Rebuild v2**:
```
一連串真正獨特的事件將你們置於眼下之境地。 我方說得對嗎？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #54 · ABOUT_US_1 · 🔴

**英文原文**:
```
Hah, to say the least!
Our past is one of a glorious and proud people coupled with a cataclysm that rocks the Universe
to its very core!
It all began when the Chimt rose from the Murky Bog and the Utwig emerged as well.
In these primitive times we cavorted about our world oblivious to any sort of higher purpose
we took everything at face value.
...
```

**Shipped**:
```
哈，那還只是輕描淡寫！
吾等之過去乃輝煌自豪之族群，卻遭遇撼動宇宙
至其核心之災難！
一切始於欽特（Chimt）自「混沌之沼」升起、忧特亦同時湧現之時。
於此原始時代，吾等於吾等世界上嬉戲，全然無知於任何更高之目的
吾等按面貌接受一切。
與此同時，欽特（Chimt）之觸鬚滞入法茲（Fahz）之龽闊天穹，然後帷幕落下！
忽然間，忧特被一集體之領悟震撼！
所有人立即急切地佩戴起各式帷幕！ 獸皮、樹葉、貝殼、岩石
於早期日子中，甚至活生生之卓爾（Drell）也被佩戴。
爾看，臉部乃表達許多阻礙感知能力之原始特質之機制。
如今擺脱了負、怒、恨、欲之持續提醒
忧特之智慧不再受原始衝動之持續提醒所阻。
經歷許多世代，面具禮儀被精煉為吾等社會磐石般之基礎。
是的，「禮法暴動」代價不菲，於生命與基礎設施皆然
然結果乃更佳之面具規範；從基本之「勞苦但必需之活動之面具」
到最華麗之「星辰代表之容貌」。 此等皆有明確定義。
認識到靈活性之重要，明確且高效之修訂與再設計程序
處理了少數異常情況。 從吾等覆蓋吾等智識壓迫之源頭之時刻起
吾等便知曉此乃一定義吾等命運之宏大目的。
爾還在聽嗎？！
吾等作為感知物種之整個發展，皆被協調以配合一非凡裝置之出現
厄創！
吾等對其悲劇性之含意懵然無知。
```

**Rebuild v2**:
```
哈，說得含蓄了！
吾等之過往乃一族光榮驕傲之人民，配合一場撼動宇宙至其核心之大劫難！
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #55 · what_about_you_2 · 🔴

**英文原文**:
```
Yow! Absolutely fascinating. But what exactly do you mean by tragic?
```

**Shipped**:
```
呀！ 絕對迷人。 但你方才說的「悲劇性」是什麼意思？
```

**Rebuild v2**:
```
哇喔！ 精彩極了。 不過你們所謂「悲劇」究竟是何意？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #56 · ABOUT_US_2 · 🔴

**英文原文**:
```
In order for you to truly understand the situation, you need to know more about the Ultron
and its unique capabilities.
You see, when the Druuge discovered the Ultron they knew that it was ours.
The Druuge were compelled by intrinsic universal direction to take it to where it has always belonged.
They brought it to us.
Oh, the Ultron!
...
```

**Shipped**:
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

**Rebuild v2**:
```
為使爾真正明白此局，爾需對厄創及其獨特能力有更多之了解。
爾當知，當毒賈族發現厄創之時，其等便知其乃吾等之物。
毒賈族受內在之宇宙指引所驅，將其帶往其本屬之處。
其等將其送至吾等手中。
噢，厄創！
其確保萬眾之生命有其絕對而圓滿之意義──此即宇宙至物！
厄創在手，吾不僅能感知爾之動機與欲望，更能感知爾之目的。
吾能以最可能顯得神秘、若非如此便顯得瘋癲之方式作用於此等事物。
數年之後，爾將把吾等對爾發展之參與，譽為爾族之轉捩點。
毒賈族僅為以此方式受益之少數之一。
即便此刻，其等對吾等為酬其送厄創至正位而給予之獎賞，仍感困惑。
於二十四年、兩個月又三日之後，其等將盡數舞歡愉之舞。
誠然，厄創使吾等得以自根本徹底改變毒賈族！
蘇菩族亦自吾等對厄創之運用中受益良多。
其等可為其力量作證！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #57 · ABOUT_US_3 · 🔴

**英文原文**:
```
Yes, things were perfect. What happened is, well, I... it is difficult to talk about.
But I saw it happen. I witnessed the Chinz-Rahl celebration.
I felt the Ultron fill the empty place that I did not know was there.
I saw the Grand Proctor pass it to
well, they say that the Chief Groo did not know that it was so heavy and slippery.
Perhaps it was a combination of factors.
...
```

**Shipped**:
```
是的，事情本是完美。 發生之事是，嗯，本族……很難啟齒。
然本族目睹了。 本族目睹了欽茲拉爾（Chinz-Rahl）慶典。
本族感受到厄創填滿了本族不知存在之空虛。
本族看見大監督者將其傳給
嗯，眾人皆稱首領古魯不知其如此沉重且滑手。
或許是諸多因素之組合。
有些檢視記錄者聲稱那實為一場陰謀！
調查委員會正式聲明厄創是因摔至地面而失效
然許多人覺得完整之故事尚未被說出！
當其撞擊地面時，本族看見其光芒褪去，然後痛苦之空虛使所有人失能。
所有憂特立即戴上「至極羞愧與恥辱之面具」，並發誓永遠佩戴！
法茲（Fahz）遍地之篝火吞噬了除此面具之外之一切；沒有其他面具倖免！
「儀典演說之相貌」之所有情境與修訂版
本族確信爾能了解，
所有求偶面具，從巧妙且引人遐思之「調情蹦跳之薄紗」
到惡名昭彰之「下流之單片眼鏡」……全都被飢餓之火焰吞噬。
即使最基本之設施亦被送入此不可逆之命運。
「自然體液排泄之面具」曾懸掛於每一間淨房！
多數公共設施已移除拋棄式面具供應器
但偶爾本族仍見此等貯放處…… 永遠是空的。
於絕望之中，吾等將破損之裝置交給吾等之盟友蘇菩族，他們居於 <% comm.getStarName("天秤座β", "supox") %> （Beta Librae）。
吾等再也無法忍受看著它。
那時，許多人建議吾等用此先驅者遺物作為自我懲罰之形式。
提案是吾等集體前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> （Zeta Hyades） 第六行星之第二衛星……
……並用此古老之行星工程裝置結束吾等之存在。
經過大量討論後，吾等決定吾等應受苦。
吾等可在決定時機成熟時使用「炸彈」
在此期間，吾等以吾等集體之苦難為吾等嚴重之過失贖罪。
本族忽然沉入憂鬱之深淵。 本族必須告退。
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #58 · what_about_urquan_1 · 🔴

**英文原文**:
```
Do you know anything about the enslaving Ur-Quan?
```

**Shipped**:
```
你們對奴役銀河的烏寬族有任何了解嗎？
```

**Rebuild v2**:
```
你們對奴役他族之烏寬族可有任何了解？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #59 · ABOUT_URQUAN_1 · 🔴

**英文原文**:
```
We know nothing of this species that you mention.
However, while we are on the subject of evil and powerful species
we have encountered a particularly gruesome race that seemed to come from the direction of <% comm.getConstellation("Arcturus", "burvixese") %>.
When we hailed them, they responded with mighty weapons that sent our delegation to their deaths
lucky fools.
The alien's dark crusty battleships are capable of guiding spinning mines into almost any location
...
```

**Shipped**:
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

**Rebuild v2**:
```
吾等對爾所提及之族群一無所知。
然當吾等論及邪惡強大之族群時
吾等曾遇一種特別可怖之族群，其似乎來自 <% comm.getConstellation("大角星", "burvixese") %> 之方向。
吾等向其致意之時，其等以強大武器回應，將吾等之使團送入死境
如彼幸運之愚者。
此異族之黝黑硬殼戰艦能將旋轉水雷引導至幾乎任何位置
若敵人靠得太近，便會湧現熾烈之光冕，造成可怖之傷害。
於吾等與該族之交鋒中──其自稱柯亞
吾等發現運用吾等自身之護盾能力，可掃清水雷、吸收光冕
繼而靠近黑艦，予以吾等之痛擊。
然真相而言，其等甚為強大而殘暴。
當柯亞開始向吾等之母星逼近之時
吾等以為此乃吾等應得之懲罰正被施行。
然後，一個謎團？ 其等忽而失去興趣，轉向他方而去。 呸！（Bah!） 令人困惑之挫敗！
若厄創尚在，吾便能於此題目上侃侃而談！
此特質被自吾等掌中撕去，愈顯吾等之存在何等無意義。
此無意義之感，正是驅動吾族嚴肅思考速斷生命之因！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #60 · ABOUT_URQUAN_2 · 🔴

**英文原文**:
```
Aagghh! Your query once again painfully reminds me of the Ultron and what it was for the Universe!
I could tell you all and correct ALL that is wrong in the Universe!
All I can tell you is that the Kohr-Ah live to kill.
Their stated purpose is to seek out new life and new civilizations
and then annihilate them.
We seemed to qualify as such and that is why it is puzzling that after pursuing us with some tenacity
...
```

**Shipped**:
```
啊哈！（Aagghh!） 爾之問訊再度痛楚地提醒本族厄創以及其對宇宙之意義！
本族本能告訴爾一切，並匡正宇宙中**所有**之錯誤！
本族所能告訴爾的僅是柯亞為殺戴而活。
他們宣稱之目的乃尋找新生命與新文明
然後將其消滅。
吾等似乎符合此類，故令人困惑者乃他們以某種堅韌追擊吾等之後
忽然轉向並朝 <% comm.getConstellation("巨爵座", "samatra") %> （Crateris） 而去。
啊！（Aangh!） 若吾等當時救下厄創，此等揣測皆屬多餘！
本可輕易 —— 一次撲抓、一顆丟出之枕頭
甚至一頭毛茅茅之小獸皆能滿意地緩衝其跌落！
確實，一組召開之分析可能性之委員會
斷定當時若吾等已備妥，厄創原本至少有 623 種方式可被救下
若吾等已備妥！ 啊哈！
讓吾等停止關於此等事之討論吧。
```

**Rebuild v2**:
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
結論為當時若吾等有備，至少有六百二十三種方法可救下厄創！ 啊嗚嗚──！
讓吾等停止關於此事之討論吧。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #61 · DONT_WANT_TO_LOOK · 🔴

**英文原文**:
```
Gaaah! Should I set my gaze upon such a sight I might suffer sleepless nights for years on end!
It is a symbol of the collective Utwig failure.
It is our ultimate tragedy!
```

**Shipped**:
```
嘎啊！（Gaaah!） 若本族將目光落於此景，本族恐將連年不眠！
其乃憂特集體失敗之象徵。
其乃吾等之終極悲劇！
```

**Rebuild v2**:
```
呃啊啊啊──！（Gaaah!） 若吾將目光投於此景，吾或將數年不能安眠！
其乃憂特集體失敗之象徵。
其乃吾等終極之悲劇！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #62 · SICK_TRICK_1 · 🔴

**英文原文**:
```
Why do you flaunt the husk which once was the Ultron?
Can't you see how much we suffer? Is this not enough?
This thing you possess... this husk of lost destiny, it is the symbol of the Ultimate Utwig Anguish!
Do - Not - Tor - ment - Me - So!
```

**Shipped**:
```
爾為何炫耀那曾為厄創之空殼？
爾看不見吾等所受之痛？ 此還不夠嗎？
爾所擁之此物…… 此失落命運之空殼，乃「至極憂特之痛」之象徵！
莫—折—磨—本—族—如—此！
```

**Rebuild v2**:
```
爾何以於吾等面前炫耀昔日厄創之空殼？
爾豈看不見吾等承受何等痛苦？ 這還不夠嗎？
爾所持之物……此散失天命之空殼，乃憂特終極痛楚之象徵！
別 - 這 - 般 - 折 - 磨 - 吾！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #63 · SICK_TRICK_2 · 🔴

**英文原文**:
```
AAAHHH!! Stop! I know that I deserve it but I cannot bear it.
Stop, please! To view this thing... I would rather bare my face
and work all of its parts in a grotesque display of self-degradation! Leave now!
```

**Shipped**:
```
啊啊啊！！（AAAHHH!!） 停！ 本族知本族該受，然本族無法忍受。
拜託停止！ 見此物…… 本族寧可裸露本族之臉
以自貶之怪誕展示活動其所有部件！ 現在離去！
```

**Rebuild v2**:
```
啊啊啊──！！（AAAHHH!!） 住手！ 吾知吾應受之，然吾實無力承受。
住手，拜託！ 觀此物……吾寧願裸露吾之臉面
以醜怪之自貶展示扭動所有面部之機件！ 速速離去！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #64 · bye_neutral · 🔴

**英文原文**:
```
We now terminate communication in a civil, yet efficient manner.
```

**Shipped**:
```
我方就此以文明卻高效之方式結束通訊。
```

**Rebuild v2**:
```
我方以有禮而有效之方式結束此次通訊。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #65 · TOO_LATE · 🔴

**英文原文**:
```
BUT WAIT!!
The Ultron moans and hums! Matters of significance are being relayed to our brains.
It has been so long since we communicated with the Ultimate in such a manner
but slowly, the truth is revealed!!...
Something dire is afoot in the galaxy
The Kohr-Ah, the dark cousins of the Ur-Quan, have won their Doctrinal Conflict
...
```

**Shipped**:
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

**Rebuild v2**:
```
然且慢！！
厄創嗚咽而低鳴！ 事關重大之訊息正被傳達至吾等之腦海。
吾等已許久未曾以此方式與至物溝通
然真相緩緩揭露！！……
銀河中有大事正在醞釀
柯亞──烏寬之陰黑表親──已勝出其教義戰爭
甚至此刻正穿越諸星，執行寰宇滅族之使命。
厄創揭示吾等之參與乃阻止柯亞所必需
免其毀滅此片銀河之所有生命。
吾等將賜予爾吾等近乎無敵之重砲艦設計
以及一批訓練有素之艦艇指揮官。
若吾等之盟友蘇菩族仍存於世，吾深信其等亦將給予爾同樣之援助。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #66 · HAPPY_DAYS · 🔴

**英文原文**:
```
AAAHHH!! Every divot, every crack on Its surface is etched forever in my soul!
Remove It from my sight lest I purge my... hey!
that is not the devastated Ultron
it is the image of the Ultron BEFORE!... a trick? A TRICK?!
Oooh! I had no idea that any species could sink so low!
How dare you try to manipulate me with that cheap stage prop?!... why it's not even
...
```

**Shipped**:
```
啊啊啊！！（AAAHHH!!） 其表面之每一凹痕、每一裂隙都永恆蝕刻於本族之靈魂！
將它從本族視線移走，以免本族將本族的…… 喂！
這不是那個殘破的厄創
這是**未破損前**之厄創的影像！…… 一個把戲？ 一個把戲？！
喔哦！ 本族沒料到有物種能墮落至此！
爾竟敢用那廉價舞台道具操縱本族？！…… 這甚至不像
喂，等等，看起來像…… **這可能嗎**？…… **是的，就是它**！…… **一個奇蹟**！！
**喔幸福之日**！！（OH HAPPY DAY!!） **喜樂之時刻**！！（JOYOUS OCCASION!!）
爾獲吾等永恆之感謝，善良之艦長！
爾將被永垂不朽為將吾等之未來遞送予吾等之蒙福身影！
吾等將崇敬爾之形貌！
讓本族接過厄創…… 是的，本族感受到那連結…… 那知識……以及那**力量**。
嗯，看來有許多事要做。
確實，看來爾應前往 <% comm.getStarName("畢宿星團ζ", "bomb") %> （Zeta Hyades） 第六行星之第二衛星……
……並取走爾於彼處所見之物；吾等不再需要它
然厄創揭示**爾**將需要！
本族感謝爾於此宏大計畫中之份。 吾等現在藉命運取回屬於吾等之物
並著手為宇宙執行吾等本質之服務。
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #67 · OK_ATTACK_KOHRAH · 🔴

**英文原文**:
```
BUT WAIT!!
The Ultron throbs and whistles! Matters of significance are being relayed to our brains.
It has been so long since we communicated with the ultimate in such a manner
but slowly, the truth is revealed... our destiny!!
We have been directed to join with our Supox allies and attack...
YOU!...
...
```

**Shipped**:
```
但等等！！
厄創在悸動與呼嘯！ 重要之事正被傳達至吾等腦中。
吾等已許久未以此方式與「至極」溝通
然緩緩地，真相被揭示…… **吾等之命運**！！
吾等被指示與吾等之蘇菩盟友聯合並攻擊……
**爾**！……
……不對，等等，那是錯的。 抱歉。
吾等攻擊…… **爾之敵人**…… 烏寬族與柯亞！……
……不，那也不太對…… 什麼？ 喔，好吧。
吾等必須**只**攻擊黑艦…… **只**攻擊柯亞！
**此外**！ 吾等將賜予爾吾等重砲艦設計之恩惠
以及一批訓練有素之星艦艦長。
吾等之重砲艦近乎無敵！
本族亦可肯定地說，吾等之盟友蘇菩族，將給予爾同樣之協助。
吾等合力，將擊敗柯亞！…… 或至少為爾爭取多幾個月
以尋找更長久之解決之道。
如今，艦長，吾等必須告退，準備吾等之戰鬥艦隊。 祝吾等好運！
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #68 · whats_up_after_space · 🔴

**英文原文**:
```
Tell us what events have transpired since we last met.
```

**Shipped**:
```
跟我方講講自上次見面以來發生的事吧。
```

**Rebuild v2**:
```
說說我方上次一別以來發生了什麼事。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #69 · GENERAL_INFO_AFTER_SPACE_1 · 🔴

**英文原文**:
```
We have met the Kohr-Ah in battle, and... well, let me explain.
Initially, when our forces swept to the <% comm.getConstellation("Horologii", "samatra") %> stars
they proved effective against the armaments of the Kohr-Ah.
With our shield-absorption technology we were able to sweep clear the Kohr-Ah's spinning blades
and absorb the brunt of their fiery corona, allowing our Supox allies to concentrate on the vessels themselves.
However, the costs were high... very high.
...
```

**Shipped**:
```
吾等已於戰鬥中遭遇柯亞，且…… 嗯，讓本族解釋。
最初，當吾等之部隊掃向 <% comm.getConstellation("時鐘座", "samatra") %> （Horologii） 群星時
他們對抗柯亞之武備確實有效。
藉由吾等之護盾吸收技術，吾等能掃除柯亞之旋轉刀刃
並吸收其火焰光冕之衝擊，讓吾等之蘇菩盟友能集中對付艦艇本身。
然而，代價高昂…… 極為高昂。
本族該戴上「哀悼陣亡同袍」之容。
```

**Rebuild v2**:
```
吾等已於戰場遇柯亞，然……容吾解釋。
最初，當吾等之部隊掃入 <% comm.getConstellation("時鐘座", "samatra") %> 之群星
其等對柯亞之軍備甚為有效。
運用吾等之護盾吸收技術，吾等能掃清柯亞之旋轉飛刃
並吸收其熾烈光冕之衝擊，令吾等之蘇菩盟友得以專注於敵艦本體。
然代價高昂……甚為高昂。
吾應戴上「哀悼陣亡同袍」（Remorse For Lost Comrades）之容。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #70 · GENERAL_INFO_AFTER_SPACE_2 · 🔴

**英文原文**:
```
As you know, we were forced to withdraw from the Kohr-Ah offensive.
Although we were able to make good account of ourselves, our casualties were high.
In our attempt to balance the Doctrinal Conflict between the Kohr-Ah and the Ur-Quan
we avoided the Ur-Quan; however, they continued to engage us whenever possible.
We had no choice but to take whatever losses were handed to us.
I can think of no mask that properly expresses how I feel concerning this situation.
```

**Shipped**:
```
如爾所知，吾等被迫自柯亞攻勢中撤退。
儘管吾等已盡力表現，吾等之傷亡仍高。
於吾等試圖平衡柯亞與烏寬族之教義戰爭時
吾等避開烏寬族；然而，他們持續於可能時交戰吾等。
吾等別無選擇，只能承受任何被交予之損失。
本族想不到任何面具能正確表達本族對此情況之感受。
```

**Rebuild v2**:
```
如爾所知，吾等被迫自對柯亞之攻勢中撤退。
儘管吾等能作良好之奮戰，然吾等傷亡慘重。
於吾等平衡柯亞與烏寬教義戰爭之嘗試中
吾等避開烏寬；然而其等只要有機會便持續與吾等交戰。
吾等別無選擇，只得承受一切被加諸於身之損失。
吾想不出有何面具能適切表達吾對此局勢之感受。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #71 · what_now_after_space · 🔴

**英文原文**:
```
Given what you have learned, what do you think we should do now?
```

**Shipped**:
```
根據你們所學到的，你們認為我方現在該怎麼做？
```

**Rebuild v2**:
```
以你們所知，你們認為我方此刻該如何應對？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #72 · DO_THIS_AFTER_SPACE · 🔴

**英文原文**:
```
We have done all that we can. There are no others capable of significant intervention.
Certain doom grows imminent for all of us. We lament.
But wait!...listen closely! The Ultron intervenes! There is a solution!
YOU are the solution!
Only YOU may halt the Kohr-Ah's seemingly inevitable advance upon life.
They CAN be defeated and you MUST do it!
...
```

**Shipped**:
```
吾等已盡吾等所能為之事。 無其他人能作有意義之介入。
吾等所有人皆迫近確定之厄運。 吾等哀嘆。
然而等等！…… 仔細聽！ 厄創介入！ 有一解決之道！
**爾**乃解決之道！
只有**爾**能阻止柯亞看似無可避免之對生命之進逼。
他們**可**被擊敗，而爾**必**做到！
喔，本族之精神被提振！ 若本族之「自信高貴姿態之面具」未被焚毀
本族將以魯莽戴上之，無視所有禮儀與程序！
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #73 · bye_after_space · 🔴

**英文原文**:
```
We thank you for your aid. We go now to address the matters at hand.
```

**Shipped**:
```
感謝你們的協助。 我方現在得處理眼前的事務了。
```

**Rebuild v2**:
```
我方感謝你們的援助。 我方現在便前去處理眼下之事。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #74 · GOODBYE_AFTER_SPACE · 🔴

**英文原文**:
```
Excellent! The Ultron's coruscations indicate that your future actions are laced with great potential!
Proceed with our heartiest endorsement!
```

**Shipped**:
```
極佳！ 厄創之閃耀顯示爾未來之行動蘊含巨大潛能！
以吾等最誠摯之支持繼續前進！
```

**Rebuild v2**:
```
極佳！ 厄創之閃耀顯示爾未來之行動充滿巨大之潛能！
帶著吾等最真摯之背書前行吧！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #75 · GENERAL_INFO_BEFORE_SPACE_1 · 🔴

**英文原文**:
```
Indeed! We are in the process of reacclimating our brains to its metawave gyrations.
Even now we are compelled to implement a plan of interference, thwarting the goals of the Kohr-Ah.
We sense through the influence of the Ultron that these creatures of evil
have goals which are mutually exclusive with our existence, and your own.
Even now, aided by the intangible guidance of the Ultron, we formulate a plan
that will serve to preserve the diversity in the galaxy.
...
```

**Shipped**:
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

**Rebuild v2**:
```
誠然！ 吾等正處於使腦部重新適應其超波迴旋之過程。
即便此刻，吾等已被驅使實施干擾計劃，挫敗柯亞之目的。
吾等透過厄創之影響感知到，此等邪惡之造物
擁有與吾等之存在、以及爾之存在，互不相容之目標。
即便此刻，於厄創之無形指引下，吾等擬定一項計劃
用以保存銀河中之多樣性。
吾等備妥一支艦隊，由憂特與蘇菩族部隊之集體力量所組成
其將追擊侵略者，意在破壞其毀滅計劃。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #76 · GENERAL_INFO_BEFORE_SPACE_2 · 🔴

**英文原文**:
```
We have determined that the Kohr-Ah are engaging in battle with the species you call Ur-Quan.
We are unable to determine the cause of this conflict.
Even meticulous employment of the Ultron in this matter has yielded only minimal insight.
In any case, after interpreting the direction provided by the Ultron
we must let the two species cancel each other out via attrition through combat.
```

**Shipped**:
```
吾等已確定柯亞正與爾稱為烏寬族之物種交戰。
吾等無法確定此衝突之原因。
即使謹慎地將厄創用於此事，也僅產生極少之洞察。
無論如何，於解讀厄創所提供之指引後
吾等必須讓兩物種透過戰鬥中之消耗互相抵消。
```

**Rebuild v2**:
```
吾等已判定柯亞正與爾所稱之烏寬族交戰。
吾等無法判定此衝突之原由。
即便於此事上細心運用厄創，亦僅得極少之洞察。
無論如何，於解讀厄創所提供之指引後
吾等必須任由此二族透過戰鬥消耗互相抵銷。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #77 · what_now_before_space · 🔴

**英文原文**:
```
Does the remarkable device suggest to us a potential course of action?
```

**Shipped**:
```
這件卓越之裝置有向我方建議潛在的行動方針嗎？
```

**Rebuild v2**:
```
那件非凡裝置可有向我方指出可行之方向？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #78 · bye_before_space · 🔴

**英文原文**:
```
We anticipate an era of glory for the Utwig! Farewell!
```

**Shipped**:
```
我方預期憂特的榮耀時代將至！ 再會！
```

**Rebuild v2**:
```
我方期待憂特族一段光榮之時代！ 再會！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #79 · how_went_war · 🔴

**英文原文**:
```
What were the results of your actions against the Ur-Quan and Kohr-Ah?
```

**Shipped**:
```
你們對抗烏寬族與柯亞的行動結果如何？
```

**Rebuild v2**:
```
你們對烏寬與柯亞行動之結果如何？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #80 · ABOUT_BATTLE · 🔴

**英文原文**:
```
Ah Captain! The battle against the Kohr-Ah was fearsome.
As we and our allied Supox approached the main force
we found that the Kohr-Ah and the species you call the Ur-Quan
were engaged in a conflict of fundamental doctrine in which the Kohr-Ah thesis seemed superior.
Acting under the guidance of the Ultron, we engaged the Kohr-Ah in an effort to balance the battle.
We met with some success. We would sweep the mines clear and deplete the energy reserves of the Kohr-Ah vessels.
...
```

**Shipped**:
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

**Rebuild v2**:
```
啊，艦長！ 對柯亞之戰乃令人畏懼。
當吾等與盟友蘇菩族逼近主要戰力時
吾等發現柯亞與爾所稱之烏寬族
正陷於一場根本教義之衝突，其中柯亞之主張似乎居於上風。
於厄創之指引下行動，吾等與柯亞交戰以求平衡此戰局。
吾等有些許勝績。 吾等會掃清水雷、耗盡柯亞艦艇之能量儲備。
繼而，勇敢之蘇菩族將迅捷插入，以其武器對準黑艦。
時機至關重要。 吾等損失慘重。
遭受極端摧殘後，吾等被迫撤退。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #81 · how_goes_war · 🔴

**英文原文**:
```
How is your engagement with the Kohr-Ah and Ur-Quan going?
```

**Shipped**:
```
你們與柯亞和烏寬族的交戰進行得如何？
```

**Rebuild v2**:
```
你們與柯亞、烏寬的交戰進展如何？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #82 · BATTLE_HAPPENS_1 · 🔴

**英文原文**:
```
Even as I speak, brave Utwig and noble Supox launch themselves against the merciless arsenal of the Kohr-Ah.
We continue to refine our tactics.
Alas, the Kohr-Ah are winning their war with the Ur-Quan.
We grow uncomfortable with the success that the Kohr-Ah are currently enjoying,
so we fight only the Kohr-Ah in hopes of weakening their stand against the Ur-Quan.
The Ur-Quan complicate matters by blasting our vessels with fusion bolts
...
```

**Shipped**:
```
即使本族此刻言之，勇敢之憂特與高貴之蘇菩，正投身於柯亞無情之武備之前。
吾等持續精進吾等之戰術。
痛哉！（Alas!） 柯亞正贏得其與烏寬族之戰爭。
吾等對柯亞當前所享之成功感到不安，
故吾等只交戰柯亞，以期削弱其對烏寬族之立場。
烏寬族以聚變彈爆擊吾等艦艇讓事情更複雜
故吾等已將盡可能避開烏寬艦艇定為政策。
```

**Rebuild v2**:
```
即便吾正在言說之時，勇敢之憂特與尊貴之蘇菩族正投身對抗柯亞無情之軍火。
吾等持續精進吾等之戰術。
痛哉！（Alas!）柯亞正贏得對烏寬之戰爭。
吾等對柯亞現下所享之勝績漸感不安，
故吾等僅與柯亞交戰，冀能削弱其對烏寬之立場。
烏寬以融合炮猛擊吾等之艦艇，使局面更趨複雜
故吾等已訂立政策，儘可能避開烏寬之艦艇。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #83 · BATTLE_HAPPENS_2 · 🔴

**英文原文**:
```
We have discovered that the Kohr-Ah, in addition to their formidable battle vessels
will soon possess an immense ship capable of inflicting destruction on a vast scale.
I do not need to examine the pulsations of the Ultron to know that they will use this instrument
to implement their stated objective: the elimination of all intelligent life besides their own.
```

**Shipped**:
```
吾等已發現柯亞除了其令人畏懼之戰鬥艦艇
將很快擁有一巨型艦艇，能造成大規模之毀滅。
本族無需檢視厄創之脈動便知他們將用此工具
執行其宣稱之目標：消滅除其自身外所有智慧生命。
```

**Rebuild v2**:
```
吾等已發現，柯亞除其可畏之戰艦外
不久將擁有一艘巨大之艦艇，能造成大規模之毀滅。
吾無需觀察厄創之脈動，便知其等將以此利器
執行其所宣稱之目標：除自身外，消滅所有具智慧之生命。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #84 · learn_new_info · 🔴

**英文原文**:
```
I'm glad things are looking up. Anything in the way of new developments?
```

**Shipped**:
```
很高興情況有起色。 有什麼新發展嗎？
```

**Rebuild v2**:
```
我方很高興情況正好轉。 有什麼新進展嗎？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #85 · NO_NEW_INFO · 🔴

**英文原文**:
```
Even now we acclimate to the great power of the Ultron
but are overwhelmed with the resources that the Ultron offers
in effect, we have grown rusty in its use.
As soon as we regain our proficiency, we will be able to accommodate all your requests.
```

**Shipped**:
```
即使此刻吾等仍在適應厄創之偉大力量
卻被厄創所提供之資源壓倒
實際上，吾等於其使用上已生疏了。
一旦吾等恢復熟練度，吾等將能滿足爾所有請求。
```

**Rebuild v2**:
```
即便此刻，吾等正在適應厄創之偉大力量
然吾等仍被厄創所提供之資源淹沒
事實上，吾等於其運用上已生疏。
一旦吾等重拾熟練，吾等便能滿足爾之一切請求。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #86 · SAMATRA · 🔴

**英文原文**:
```
The Kohr-Ah will soon possess a seemingly invincible vessel called the Sa-Matra.
I cannot give you specifics regarding this matter other than its general location
somewhere in the <% comm.getConstellation("Crateris", "samatra") %> constellation.
The Sa-Matra is seemingly invincible, able to lay waste to an entire planet in less than an eyeblink.
The Ultron indicates that you must somehow destroy this thing or the Kohr-Ah will destroy all known life.
```

**Shipped**:
```
柯亞將很快擁有一看似無敵之艦艇，稱為薩瑪特拉。
本族除其大略位置外，無法給予爾關於此事之具體資訊
位於 <% comm.getConstellation("巨爵座", "samatra") %> （Crateris） 星座某處。
薩瑪特拉看似無敵，能於眨眼之間讓整個行星化為廢墟。
厄創顯示爾必須以某種方式摧毀此物，否則柯亞將摧毀所有已知生命。
```

**Rebuild v2**:
```
柯亞不久將擁有一艘看似無敵之艦艇，名為薩瑪特拉。
除其大致位置在 <% comm.getConstellation("巨爵座", "samatra") %> 之某處外
吾無法給予爾更多細節。
薩瑪特拉看似無敵，能於眨眼之間夷平整顆行星。
厄創指示，爾必須設法摧毀此物，否則柯亞將毀滅所有已知之生命。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #87 · what_now_homeworld · 🔴

**英文原文**:
```
What course of action does the Ultron, your powerful attribute amplifier, recommend for us now?
```

**Shipped**:
```
爾等之偉大屬性放大器 —— 厄創 —— 對我方推薦何行動方針？
```

**Rebuild v2**:
```
你們那強大之稟賦放大器──厄創──此刻建議我方採取何種行動？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #88 · HOPE_KILL_EACH_OTHER · 🔴

**英文原文**:
```
We can only hope that our efforts to balance the forces of the Ur-Quan and the Kohr-Ah
will permit them to mutually annihilate each other.
```

**Shipped**:
```
吾等只能期望吾等平衡烏寬族與柯亞之力量之努力
將使他們得以互相殲滅。
```

**Rebuild v2**:
```
吾等只能企盼，吾等平衡烏寬與柯亞勢力之努力
將令其等互相殲滅。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #89 · how_is_ultron · 🔴

**英文原文**:
```
It seems that you are making good use of the Ultron. Is this so?
```

**Shipped**:
```
看來你們善用了厄創。 是這樣嗎？
```

**Rebuild v2**:
```
看來你們對厄創運用甚佳。 是否如此？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #90 · ULTRON_IS_GREAT · 🔴

**英文原文**:
```
You ask a question that I hesitate to answer. You see, normally at this point
I would don the mask of Rampant Jubilation and Jumping With Ecstatic Glee.
This mask is seldom worn, for few events merit its complexity.
Since I do not currently possess this mask
let me just say that the Ultron is everything it could ever possibly be and MORE!
Even now I sense that your curiosity is piqued to an extreme.
...
```

**Shipped**:
```
爾提出之問題本族猶豫作答。 爾看，通常於此刻
本族將戴上「狂野歡欣與狂喜跳躍之面具」。
此面具極少佩戴，因少有事件配得上其複雜性。
既然本族目前不擁此面具
請容本族僅言：厄創乃其可能為之一切，而**更多**！
本族此刻感受到爾之好奇心已被激至極致。
爾欲問更多問題。
然而，這些問題最好還是別問。
藉由厄創強大而和諧之力量
本族現在將使爾徹底放下此話題。
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #91 · bye_allied_homeworld · 🔴

**英文原文**:
```
We acknowledge the celestial Ultron and your assistance. We will now be on our way.
```

**Shipped**:
```
我方感謝天國的厄創與你們的協助。 我方就此告辭。
```

**Rebuild v2**:
```
我方向那天國般之厄創與你們的援助致意。 我方這就上路了。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #92 · GOODBYE_ALLIED_HOMEWORLD · 🔴

**英文原文**:
```
It is as the Ultron wills. So be it. We bid you the very best luck.
Although it is true that all possibilities can be realized through proper utilization of the Ultron
we are, as yet, deficient operators of this grand device.
We will, however, make a best attempt to help you from afar.
```

**Shipped**:
```
如厄創之意志。 就此決定。 吾等祝爾最好之運。
儘管所有可能性皆可透過厄創之適當使用實現
吾等，至今為止，尚為此宏大裝置不成熟之操作者。
然而，吾等將自遠方盡最大努力協助爾。
```

**Rebuild v2**:
```
此乃厄創之意。 便如此。 吾等祝爾至高之好運。
雖說於厄創之妥善運用下，一切可能性皆可實現
然吾等目前於此宏偉裝置之操作上仍有不足。
然吾等將盡力自遠方助爾。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #93 · ALLIED_HOMEWORLD_HELLO_1 · 🔴

**英文原文**:
```
Ah! It is the legendary Earth Captain! A grand celebration is in order!
We prepare now for the festivities!
Many will bow before you and offer their profuse thanks!
Proceed now to our main spaceport and then on to the parade!
The two week celebration of great thanks will begin! Joy!
What? You are too busy? Alas... perhaps another time.
```

**Shipped**:
```
啊！ 是那傳奇之地球艦長！ 一場盛大之慶祝理當舉辦！
吾等現在為慶典做準備！
許多人將於爾面前鞠躬並致以濃厚之感謝！
現在前往吾等主要之太空港，然後參加遊行吧！
為期兩週之感恩慶典即將開始！ 歡欣！
什麼？ 爾太忙了？ 痛哉！（Alas!）……或許改日吧。
```

**Rebuild v2**:
```
啊！ 那乃傳奇之地球艦長！ 應舉大慶！
蒙福的憂特現正為慶典籌備！
眾人將於爾前俯首，獻上滿溢之謝意！
現前往吾等之主太空港，繼而參加遊行！
兩週之盛大感恩慶典即將開始！ 歡欣！
什麼？ 爾太忙？ 痛哉…… 或許改日再說。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #94 · ALLIED_HOMEWORLD_HELLO_2 · 🔴

**英文原文**:
```
Our spirits are lifted by your visit!
I sense through the Ultron's powers that you are curious
about the status of your well-deserved facial appliance. Fear not!
Even though we currently have no masks worthy of your stature
with the re-establishment of the Ultron within the structure of the Utwig wholeness
we proceed with the design and implementation of what will truly be the pinnacle of Utwig ingenuity.
...
```

**Shipped**:
```
吾等之精神因爾之到訪而振奮！
本族透過厄創之力感應到爾對爾當之無愧之面具狀態感到好奇。
莫懼！
儘管吾等目前無面具配得上爾之地位
隨著厄創重歸憂特整體之結構
吾等正著手設計與實作，那將真正成為憂特巧思之巔峰之物。
終於，爾將能以尊嚴掩蓋爾那不甚好看之嘴臉！
```

**Rebuild v2**:
```
神聖之艦長之蒞臨令吾等之心神振奮！
吾透過厄創之力感應到爾對爾應得之面部器具狀態感到好奇。 勿懼！
儘管吾等此刻並無配得爾身份之面具
然隨厄創於憂特整體結構中之重新確立
吾等正推進設計與實作，此物將真正成為憂特智慧之巔峰。
終有一日，爾將能以卓然之姿遮蔽爾醜陋之臉！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #95 · ALLIED_HOMEWORLD_HELLO_3 · 🔴

**英文原文**:
```
Ah, I see that it is the great Earth Captain honoring my lowly self with undeserved attention.
Even now my skin prickles with embarrassment since I am unable to don a mask
that accurately indicates my awed and respectful attitude toward you.
I am glad to say, however, that we are in a process
of redefining and restructuring our entire countenance catalog.
The results will be dramatic since the Ultron is now integrated in this process.
...
```

**Shipped**:
```
啊，本族看見是偉大之地球艦長，正以不當之關注屈就本族之卑下。
即使此刻，本族之皮膚亦因無法戴上準確表達本族對爾崇敬與尊敬態度之面具
而尷尬得起雞皮疙瘩。
然本族欣然報告，吾等正處於
重新定義並重構吾等整個容貌目錄之過程中。
結果將戲劇性，因厄創如今已納入此過程。
在此期間，本族懇求爾容忍吾等完成此任務。
```

**Rebuild v2**:
```
啊，吾見那偉大之地球艦長以不配之關注榮寵吾這卑微之身。
即便此刻，吾之肌膚因無法戴上一副能準確表達
吾對爾敬畏尊崇之態度之面具，而因尷尬刺痛。
然吾欣然告知，吾等正處於
重新定義與重塑吾等整套容貌目錄之過程。
成果將戲劇性地卓越，因厄創現已整合於此過程之中。
與此同時，吾懇請爾寬容以待，容吾等完成此任務。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #96 · ALLIED_HOMEWORLD_HELLO_4 · 🔴

**英文原文**:
```
I am honored to encounter your greatness!
Currently, our collective creative force is engaged in a project to honor you.
We are in the process of transforming a planetary body
in a location that will remain secret
into a Great Mask. This mask will be worn by one individual and ONLY one individual!
It is the mask of the great Captain! It is YOU that wears this mask.
...
```

**Shipped**:
```
本族有幸遭遇爾之偉大！
目前，吾等之集體創造力正投身於一項榮耀爾之計畫中。
吾等正處於將一顆行星體
轉化為「偉大之面具」之過程中，地點將保密。
此面具將由一位個體佩戴，且**僅**由一位個體佩戴！
此乃偉大艦長之面具！ 佩戴此面具的乃是**爾**。
當爾戴上此面具時，吾等將見雙眼活過來。
當爾說話時，所有人都會聽見。 當爾微笑時，吾等將歡欣！
本族感應到爾對此計畫之興奮！
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #97 · HELLO_BEFORE_KOHRAH_SPACE_1 · 🔴

**英文原文**:
```
Suddenly I am overcome with embarrassment!
I possess the distinguished honor of addressing the legendary Earth Captain!
Please excuse my lack of proper facial appliance.
This occasion ideally calls for me to don the Expression of Ultimate Gratitude.
Eegh! I am compelled by the forceful Emanations of the Ultron to describe the appearance of the mask.
Its foundation is composed entirely of a matrix of beetle secretions and Trooba Fern
...
```

**Shipped**:
```
本族忽然被尷尬淹沒！
本族擁有向傳奇之地球艦長致意之殊榮！
請原諒本族缺乏適當之面具。
此時機理當召喚本族戴上「至極感激之表情」。
嗯！ 本族被厄創強大之流溢驅使描述那面具之外貌。
其基礎完全由甲蟲分泌物與楚巴蕨（Trooba Fern）之矩陣構成
呈精巧複雜之紋理。
此過程極為耗時，因即使訓練最好之甲蟲群落
也需為每一成功之基礎製造一千個廢品。
痛哉！ 憂特族要能佩戴此等面具還需許多年。
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #98 · HELLO_BEFORE_KOHRAH_SPACE_2 · 🔴

**英文原文**:
```
Do my eyes deceive me? Am I a victim of a glorious vision?
I believe that I see before me the legendary Earth Captain!
We have conducted a complete survey of the Utwig
and we have convened the committee that will guide the formation of your Saintly Facade.
We eagerly anticipate the delivery of an appliance!
Imagine, when development is completed in perhaps less than ten years
...
```

**Shipped**:
```
本族雙眼是否欺騙本族？ 本族是否為榮光之幻象之受害者？
本族相信本族看見面前乃傳奇之地球艦長！
吾等已對憂特族進行完整之調查
並已召開委員會，將引導爾「聖徒面容」之形成。
吾等熱切期待面具之交付！
試想，當開發於或許不到十年內完成時
爾將能以美學掩蓋爾動物本性之持續提醒
並於精深智識之族類間昂然行走！
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #99 · HELLO_DURING_KOHRAH_SPACE_1 · 🔴

**英文原文**:
```
The Ultron indicates that you must leave the area immediately! You are in extreme danger!
This area is currently controlled by either the Ur-Quan or the Kohr-Ah, we are not sure.
We are currently engaging the Kohr-Ah in an attempt to balance the conflict. Stay clear!
```

**Shipped**:
```
厄創顯示爾必須立即離開此區域！ 爾處於極端危險！
此區目前由烏寬族或柯亞控制，吾等不確定。
吾等目前正交戰柯亞以圖平衡衝突。 遠離！
```

**Rebuild v2**:
```
厄創指示爾必須立即離開此區域！ 爾身處極端之危險！
此區域現由烏寬或柯亞控制，吾等不確定為何者。
吾等正與柯亞交戰，以求平衡此衝突。 遠離此地！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #100 · HELLO_DURING_KOHRAH_SPACE_2 · 🔴

**英文原文**:
```
Battle rages in the immediate area. Beware!
The Ur-Quan and the Kohr-Ah are engaged in a conflict of doctrinal extremes.
The Ur-Quan argument seems inferior.
You must clear the area before you become a victim of either the Ur-Quan or Kohr-Ah.
Leave now! We shall remain in an attempt to balance the conflict
so that the two forces of evil might more effectively negate each other.
```

**Shipped**:
```
戰役於周邊區域激烈進行。 當心！
烏寬族與柯亞正陷入教義極端之衝突。
烏寬族之論點似乎較低劣。
爾必須清空區域，以免爾成為烏寬族或柯亞之受害者。
現在離去！ 吾等將留下以圖平衡衝突
使兩股邪惡之力更有效地互相抵消。
```

**Rebuild v2**:
```
戰火於周遭區域肆虐。 提防！
烏寬與柯亞正陷於一場極端教義之衝突。
烏寬之主張似居下風。
爾必須離開此區域，免爾成為烏寬或柯亞之犧牲品。
速速離去！ 吾等將留下，嘗試平衡此衝突
使此二股邪惡勢力得以更有效地互相抵銷。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #101 · HELLO_AFTER_KOHRAH_SPACE_1 · 🔴

**英文原文**:
```
We extend our sincere greetings to the remarkable being
that returned to the Utwig the meaning for our continued existence.
We have returned from a conflict of a grand scale with our fleet battered
but our masks of Valor and Derring-Do held high!
```

**Shipped**:
```
吾等致以誠摯之問候於此非凡之存在者
此人為憂特族尋回吾等繼續存在之意義。
吾等已自宏大規模之衝突返回，吾等艦隊雖有損傷
然吾等之「英勇無畏之面具」高舉！
```

**Rebuild v2**:
```
吾等向這位非凡之存在致以真誠之問候
是他將吾等憂特之存續意義歸還於吾等。
吾等自宏大規模之衝突歸來，艦隊受創
然吾等之「英勇無畏之面具」（Masks of Valor and Derring-Do）高舉！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #102 · HELLO_AFTER_KOHRAH_SPACE_2 · 🔴

**英文原文**:
```
Ah, it is the most recently appointed Ultron Saint -- the Captain from Earth!
We flick our facial appliances collectively in a smart salute indicating both respect and gratitude.
How can we assist you?
```

**Shipped**:
```
啊，此乃最近被任命之厄創聖者 —— 來自地球之艦長！
吾等集體以敏捷之敬禮輕彈吾等之面具，同時表達尊敬與感激。
吾等能如何協助爾？
```

**Rebuild v2**:
```
啊，那乃最新受封之厄創聖徒──那位來自地球的艦長！
吾等集體翻動吾等之面部器具，作一俐落之敬禮，以示尊敬與感謝。
吾等如何援助爾？
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #103 · UP_TO_YOU · 🔴

**英文原文**:
```
The prognosticating harmonics of the Ultron reveal a truth.
We Utwig have done all that CAN be done to aid you.
Our tasks must now be confined to directing the many channels of causation.
Feel confident that we are using the Ultron to this end.
```

**Shipped**:
```
厄創之預示和諧揭示一真相。
吾等憂特族已盡吾等**所能**做之一切以協助爾。
吾等之任務如今必須侷限於引導因果之諸多渠道。
請放心，吾等正將厄創用於此目的。
```

**Rebuild v2**:
```
厄創之預示諧振揭示一項真相。
吾等憂特已做了所有能為援助爾而做之事。
吾等之任務此後必局限於指引因果之諸多渠道。
請信任吾等正為此運用厄創。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #104 · can_you_help · 🔴

**英文原文**:
```
Material aid from you would tilt the balance in the favor of Good.
```

**Shipped**:
```
你們的物資援助能將天平傾向「善」之一方。
```

**Rebuild v2**:
```
你們的物資援助將令天秤傾向善之一方。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #105 · HOW_HELP · 🔴

**英文原文**:
```
Hmm... a reasonable request. Give us a second while we consult the Ultimate.
```

**Shipped**:
```
嗯…… 一合理之請求。 稍待片刻，讓吾等諮詢「至極」。
```

**Rebuild v2**:
```
嗯……合理之請求。 容吾等片刻，讓吾等諮詢那至物。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #106 · DONT_NEED · 🔴

**英文原文**:
```
The Ultron confirms the evidence of our ocularities
you are strong, smart and capable.
Your fleet is at maximum strength and your ethics are sound.
Further assistance would be redundant.
```

**Shipped**:
```
厄創證實吾等眼力所見之證
爾強壯、聰明、有能力。
爾之艦隊處於最大實力，爾之倫理亦健全。
更多之協助將屬多餘。
```

**Rebuild v2**:
```
厄創確認吾等目視之證據
爾乃強壯、聰穎且能幹。
爾之艦隊已達最強狀態，爾之倫理亦穩固。
進一步之援助將顯多餘。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #107 · HAVE_4_SHIPS · 🔴

**英文原文**:
```
Just so. The Ultron has hummed its assent.
Take possession of four of our Jugger craft this instant!
```

**Shipped**:
```
正是。 厄創已鳴響其贊同。
此刻取走吾等之四艘重砲艦！
```

**Rebuild v2**:
```
正是如此。 厄創已低鳴其允諾。
此刻便接收吾等四艘重砲艦！
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #108 · NO_ULTRON_AT_BOMB · 🔴

**英文原文**:
```
Foolish tricksters! Don't you know the Druuge tried that ploy on us just a few days ago?
You say you have the Ultron, that you wish to return it to us... LIES!
The moment our back is turned, you will sneak down to the surface of this world
and deprive us of our destructive device of dignity.
If you truly had our Ultron, repaired to its state of perfection
you would surely take it to the Proctors at our homeworld at <% comm.getStarName("Beta Aquarii", "utwig") %>.
...
```

**Shipped**:
```
愚蠢之騙徒！ 爾不知毒賈族數日前才對吾等玩過此招？
爾說爾有厄創，說爾欲將其歸還吾等…… **謊言**！
吾等一轉身，爾便偷溜至此世界之表面
並奪走吾等尊嚴之破壞裝置。
爾若真有吾等之厄創，已修復至其完美狀態
爾定會將其帶至位於 <% comm.getStarName("寶瓶座β", "utwig") %> （Beta Aquarii） 之吾等母星監督者處。
此議題爾再別多提。
```

**Rebuild v2**:
```
愚蠢之騙徒！ 爾豈不知毒賈族數日前才對吾等玩過此招？
爾言擁有厄創，欲將其歸還吾等……謊言！
爾等一轉頭，便將偷偷潛至此世界之表面
奪走吾等尊嚴之毀滅性裝置。
若爾當真擁有吾等之厄創，且已修復至圓滿狀態
爾必當將其送至吾等母星之監督團所在，即 <% comm.getStarName("寶瓶座β", "utwig") %>。
勿再言及此事。
```

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

#### #109 · OUT_TAKES · 🔴

**英文原文**:
```
Hello again, heroic humanoid!
Ever since you returned the Ultron to us
everything has been WONDERFUL... just perfect!
Within just two days our factories will begin churning out
appropriate facial appliances, and I have already picked out my first mask
the Domino of Unrivaled Merriment!
...
```

**Shipped**:
```
又見面了，英雄類人生物！
自從爾將厄創歸還吾等以來
一切都**棒透了**…… 完美無瑕！
短短兩天之內，吾等之工廠將開始生產
適當之面具，本族已挑好本族的第一個面具
那將會是「無比歡樂之多米諾面具」！
是的，吾等所有人都欣喜若狂…… 甚至連高階監督者也在雀躍
她正表演「啟示狂歡跳躍」！
看她如何雀躍，如何將厄創高舉！
看她如何扭轉，如何旋轉，如何滑手然後將厄創拋入空中…… 喔不哦哦哦！！！
（碰！！）
```

**Rebuild v2**:
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

**你的選擇**: A (shipped) / B (rebuild v2) / C (自訂,說明後半)

---

