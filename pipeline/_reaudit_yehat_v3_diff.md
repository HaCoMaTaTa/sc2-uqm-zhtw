# Yehat (+ Rebels) Rebuild-Compare Diff Report v3

**日期**: 2026-08-16  
**方法**: v0.7 dossier-based clean-room rebuild 完成後,程式化 diff shipped v0.6  
**Workflow**: [Rebuild_And_Compare.md](../StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md)  
**v3 files**: `translations/yehat.zh-TW.v3.json` (68 tokens) + `translations/yehatrebels.zh-TW.v3.json` (34 tokens) = **102 tokens**

## 統計

| 類別 | Emoji | 意義 | Count | % |
|---|---|---|---:|---:|
| 完全相同,可全繼承 shipped | 🟢 | v3 vs shipped | 3 | 2.9% |
| 微調 · 等價,v3 版更符 dossier 一致性 | 🟡 | v3 vs shipped | 7 | 6.9% |
| 措辭改變 · v0.6 文言 → v0.7 白話 + 鳥鳴 icon | 🟠 | v3 vs shipped | 86 | 84.3% |
| 語意 / voice 差異大 · 需 case-by-case 判斷 | 🔴 | v3 vs shipped | 6 | 5.9% |
| canonical 升級 · v0.5.2+ 新版鎖定 | ✨ | v3 vs shipped | 0 | 0.0% |
| **總計** | | | **102** | 100.0% |

## Q&A 決策鎖定 (v3 依此執行)

- Q1=A 自稱分散 palette (本騎士/本氏族/我族/我們/我方/我/我等)
- Q2=A 鳥鳴 icon 完整補回 (BRAAK/AWK/HISS/HOOT/CLACK/YEEP/HEEP/sob!/whimper!/gulp!)
- Q3=A 保皇派 vs 叛軍派 情境判斷語氣
- Q4=A 蘇格蘭進行式選擇性模擬 (only when be+ing/are being)
- Q5=A 玩家 response 稱呼: 兄弟/翼哈特朋友/翼哈特騎士 情境切換
- Q6=A 玩家自稱情境: 我方/我/老子
- Q7=A 陛下情境: 女皇陛下(保皇派) / 偽女皇(叛軍派)
- Q8=B 平實: 母星/我族世界/我族巢
- Q9=繼承 翼哈特叛軍
- Q10=**翼-翼氏族** (Zeep-Zeep 意譯,呼應鳥人 icon)
- Q11=葉哈→翼哈特 全數統一
- Q12=分批 partial-1..6 (實際執行:yehat 4 批 + yehatrebels 2 批 = 6 批)

## 3-gate verify 結果

- ✅ **Gate 1 純度**: race=0, simp=0, variant=0 (清除 shipped 之 92+95=187 個之 + 爾 50+30=80 個等文言污染)
- ✅ **Gate 2 行數**: 0 mismatch (102/102 tokens 對齊原文)
- ✅ **Gate 3 Lua template**: 0 English leak (3 個 getStarName first-args 已改中譯 + 首介英文)

## 主要 canonical 修正

| 舊 (shipped v0.6) | 新 (v3 per Master_Glossary v0.5.2+) | 出現 tokens |
|---|---|---|
| 蘇菲斯特族 | **修烈士族** (Master_Glossary L50 v0.4 rename) | shofixti_alive_1/2, whats_up_space_3, SEND_HIM_OVER_1/2, WE_REVOLT, GENERAL_INFO_SPACE_3, HERES_A_HINT, ABOUT_WAR, ABOUT_URQUAN, what_about_urquan |
| 葉哈 | **翼哈特** (Master_Glossary L51 v0.4 rename) | HOMEWORLD_HELLO_1 (殘留 1x) 全掃 |
| 榮耀裝置 | **榮耀彈** (v0.5.2 D1 統一) | WE_REVOLT |
| 女王 | **女皇** (dossier §四 canonical) | 多處 |
| 等級體 | **階層** (Ur-Quan Hierarchy v0.2 canonical) | GENERAL_INFO_SPACE_1, ABOUT_URQUAN, ABOUT_CLUE |

## 新增 canonical (待 Master_Glossary 補登)

| 英文 | v3 中譯 | 說明 | 待決 Q |
|---|---|---|---|
| Zeep-Zeep Clan | **翼-翼氏族** | Q10 使用者鎖定 (2026-08-16) 意譯呼應 wing icon | ✅ locked |
| Feep-Eeep Starship Clan | **費普-伊普 星艦氏族** (Feep-Eeep) | v3 音譯 + 英文首介; 保皇派敵對氏族 | 使用者可選 A=音譯 / B=意譯「啾-啾」 / C=保留英文 |
| Wars of Ascension | **升位戰爭** | v3 意譯; 翼哈特古代群雄爭王 | 使用者可核 |
| Battle Thrall(s) | **戰奴** | GENERAL_INFO_SPACE_4 使用; 對齊 Master_Glossary L299 |  |
| harridan (a true harridan) | **十足的潑婦** | Master_Glossary L387 canonical |  |
| harpy Queen | **鷹身女妖女皇** | Master_Glossary L388 canonical |  |

## ✨ Canonical 升級 (Star) · 0 tokens

_無自動偵測到 star 條目_ (原因: shipped 已部分使用 v0.4+ canonical;實際 canonical 修正見上表)


## 🔴 語意 / voice 差異大 · 6 tokens

### #1 · `WE_CANNOT_1` · 🔴 RED · _sim=0.172; 文言助詞清除=3_

**英文原文**:
```
As much as my heart cries to aid ye, valiant human, I cannot!
Each of us is sworn first to our Queen who
has commanded us to treat ye as an enemy of the Crown!
```

**Shipped v0.6**:
```
縱使我心哭泣欲助爾，勇武的人類，我亦無法！
我等每一員皆先向女皇立誓
她命我族視爾為王室之敵！
```

**Rebuild v3 (clean-room)**:
```
勇敢的人類啊——本騎士的心雖竭力泣求要援助你,卻做不到!
本氏族的每一位戰士,皆已誓忠於女皇陛下——
而她——已下令要我等視你為皇室大敵!
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `WE_CANNOT_1=A` (繼承 shipped) / `WE_CANNOT_1=B` (採用 v3) / `WE_CANNOT_1=C自訂:...`

---

### #2 · `GO_IN_PEACE` · 🔴 RED · _sim=0.295; 文言助詞清除=2_

**英文原文**:
```
Though honoring our past commitment we are not,
we will be letting you go in peace.
```

**Shipped v0.6**:
```
雖然我等未能榮耀我族過去之承諾，
我等仍會讓爾平安離開。
```

**Rebuild v3 (clean-room)**:
```
雖然我族——未能守住昔日的承諾——
我族仍將——放你——安然離去。
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `GO_IN_PEACE=A` (繼承 shipped) / `GO_IN_PEACE=B` (採用 v3) / `GO_IN_PEACE=C自訂:...`

---

### #3 · `SEND_HIM_OVER_2` · 🔴 RED · _sim=0.13; 文言助詞清除=2_

**英文原文**:
```
Ye are lying to us once, Captain. Now we need the hard evidence.
Order yer supposed Shofixti to come to us, Captain.
```

**Shipped v0.6**:
```
爾騙過我等一次，艦長。 如今我等需要硬證據。
命爾所謂的修烈士族至我等這裡來，艦長。
```

**Rebuild v3 (clean-room)**:
```
艦長,你曾對我族撒過一次謊。此番,我族需要確鑿的實證。
命令你所謂的那位修烈士,前來我族這裡,艦長。
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `SEND_HIM_OVER_2=A` (繼承 shipped) / `SEND_HIM_OVER_2=B` (採用 v3) / `SEND_HIM_OVER_2=C自訂:...`

---

### #4 · `not_here` · 🔴 RED · _sim=0.276_

**英文原文**:
```
Well I don't have one right HERE.
```

**Shipped v0.6**:
```
呃，我這裡剛好沒有。
```

**Rebuild v3 (clean-room)**:
```
這個嘛……我方**現在**手邊沒有耶。
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `not_here=A` (繼承 shipped) / `not_here=B` (採用 v3) / `not_here=C自訂:...`

---

### #5 · `ROYALIST_SPACE_HELLO_2` · 🔴 RED · _sim=0.232; 文言助詞清除=4_

**英文原文**:
```
It is the human Agitator who would see Her Radiant Majesty pulled from the High Perch!
Ye will rue the day ye devised this wicked scheme!
```

**Shipped v0.6**:
```
此人乃將陛下自女王高棲拉下之人類煽動者！
爾終將悔恨設下此邪惡陰謀之日！
```

**Rebuild v3 (clean-room)**:
```
就是這個人類——這**煽動者**——想要看到光輝女皇陛下,從高懸王座上被扯下!
你將悔恨——你策劃這卑劣陰謀的那一天!
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `ROYALIST_SPACE_HELLO_2=A` (繼承 shipped) / `ROYALIST_SPACE_HELLO_2=B` (採用 v3) / `ROYALIST_SPACE_HELLO_2=C自訂:...`

---

### #6 · `WHAT_INFO` · 🔴 RED · _sim=0.286; 文言助詞清除=1_

**英文原文**:
```
Of course! What knowledge do ye seek?
```

**Shipped v0.6**:
```
當然！ 爾欲求何等知識？
```

**Rebuild v3 (clean-room)**:
```
當然!你——想探詢什麼樣的知識?
```

**推薦**: B · v3 依 v0.7 dossier 重建 voice,shipped 語氣顯不合;建議 B 但需 case-by-case 判斷

**你的選擇**: `WHAT_INFO=A` (繼承 shipped) / `WHAT_INFO=B` (採用 v3) / `WHAT_INFO=C自訂:...`

---


## 🟠 措辭改變 · 86 tokens

> 這是最大分類。v3 對整段做 v0.7 dossier voice 改寫: 文言助詞清除 + 「本騎士/本氏族」正式集體感 + 鳥鳴 icon 補回 + 蘇格蘭進行式模擬。
> 建議策略: **🟠 全 B (採用 v3)** — 統一維持 v0.7 dossier 語體。若使用者發現個別語感不合,再逐項改 A。

### #1 · `HOMEWORLD_HELLO_1` · 🟠 ORANGE · _sim=0.365; 文言助詞清除=3_

**英文原文**:
```
It is sure and a true thing that the alien interloper has now been warned
not to approach Caer Zeep-Reep, the Queen's High Perch
lest it be blasted without further warning!
```

**Shipped v0.6**:
```
此乃確鑿無疑之事:外星闖入者已被警告
莫要接近齊普瑞普堡（Caer Zeep-Reep），女皇高棲之殿
否則將不再警告，直接轟殺！
```

**Rebuild v3 (clean-room)**:
```
本氏族鄭重相告，外星闖入者：
切莫接近凱爾茲皮里普——女皇的高懸王座，
否則將遭轟成粉塵，再無警告！
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HOMEWORLD_HELLO_1=A` (繼承 shipped) / `HOMEWORLD_HELLO_1=B` (採用 v3) / `HOMEWORLD_HELLO_1=C自訂:...`

---

### #2 · `HOMEWORLD_HELLO_2` · 🟠 ORANGE · _sim=0.421_

**英文原文**:
```
It is a shocking thing to see the return of the human renegade!
One knows this will not be boding well with her Majesty today.
```

**Shipped v0.6**:
```
見到人類叛徒歸來，實在令人震驚！
可知這在今日女皇陛下面前，兆頭斷然不佳。
```

**Rebuild v3 (clean-room)**:
```
甚為驚駭！竟又見人類叛徒歸返！
本騎士深知——今日此事，將不合女皇陛下的心意。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HOMEWORLD_HELLO_2=A` (繼承 shipped) / `HOMEWORLD_HELLO_2=B` (採用 v3) / `HOMEWORLD_HELLO_2=C自訂:...`

---

### #3 · `whats_up_homeworld` · 🟠 ORANGE · _sim=0.691_

**英文原文**:
```
What has happened in the twenty years since our species last met?
```

**Shipped v0.6**:
```
自我方兩族上次相遇以來的二十年間，發生了什麼？
```

**Rebuild v3 (clean-room)**:
```
自從我方兩族上次相會，已過二十年了。這段期間，究竟發生了什麼事？
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `whats_up_homeworld=A` (繼承 shipped) / `whats_up_homeworld=B` (採用 v3) / `whats_up_homeworld=C自訂:...`

---

### #4 · `GENERAL_INFO_HOMEWORLD_1` · 🟠 ORANGE · _sim=0.513; 文言助詞清除=7_

**英文原文**:
```
It is a wondering thought that crosses my mind human starship Captain.
Are ye not knowing that the cause of our Queen and empire
is now allied with the fortunes of the mighty Ur-Quan?...
...and that yer presence here is being only the end of yer life?
Haven't ye got the sense, human, to know this simple thing?
```

**Shipped v0.6**:
```
有一疑念掠過我心，人類星艦艦長。
汝豈不知，我等翼哈特族之女皇與帝國之志業
如今已與雄壯的烏寬族禍福與共？…
…而汝現身此地，僅是為汝性命劃下句點？
人類，汝豈連如此簡單之事都無知覺？
```

**Rebuild v3 (clean-room)**:
```
本騎士心中，掠過一個令人納悶的念頭——人類星艦艦長啊！
你難道不知，我族女皇與帝國的偉業
如今正與強大的烏寬命運相繫？……
……而你出現在此，只是正走向你性命的終點？
人類，你的智慧，難道連這樣簡單的事都無法明白？
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_HOMEWORLD_1=A` (繼承 shipped) / `GENERAL_INFO_HOMEWORLD_1=B` (採用 v3) / `GENERAL_INFO_HOMEWORLD_1=C自訂:...`

---

### #5 · `GENERAL_INFO_HOMEWORLD_2` · 🟠 ORANGE · _sim=0.516; 文言助詞清除=10_

**英文原文**:
```
Ye are asking the words of a mindless child, human!
Here, in the Hall of the Queen's High Perch
ye shall not be finding the sympathies ye so vainly seek.
There are none here but the nobles and battlemasters of the Yehat Clans.
It is a sure thing that we will not be casting flower petals in yer path of rebellion.
```

**Shipped v0.6**:
```
汝所問，乃無知孺子之言，人類！
此地乃女皇高棲之殿
汝在此決不可能找到汝所徒勞尋求的同情。
此處除翼哈特氏族之貴族與戰陣統領外別無他人。
可以確定，本氏族絕不會為汝叛逆之路撒花鋪徑。
```

**Rebuild v3 (clean-room)**:
```
人類，你所問的，儘是無腦孩童的字句！
此處——女皇高懸王座的殿堂內——
你將尋不到你所徒勞渴求的同情。
此地唯有翼哈特各氏族的貴族與戰陣首領。
可以確切地說：我族絕不會在你叛逆的路上，為你灑下花瓣。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_HOMEWORLD_2=A` (繼承 shipped) / `GENERAL_INFO_HOMEWORLD_2=B` (採用 v3) / `GENERAL_INFO_HOMEWORLD_2=C自訂:...`

---

### #6 · `ENEMY_MUST_DIE` · 🟠 ORANGE · _sim=0.399; 文言助詞清除=14_

**英文原文**:
```
Are ye DAFT human!? Have ye not heard our words?
You and yer kind are slaves, just as we
but you humans have been confined within a shield of slaves!
To be found outside this selfsame shield is surely yer own doom!
It is NOT a permitted thing fer ye to be a-travelling through space
and now, we must be conforming to our Queen's oath to the Ur-Quan.
We must be getting about the business of killing you!
```

**Shipped v0.6**:
```
汝腦子壞了嗎，人類？！ 我等之言汝沒聽進去？
汝與汝族人皆是奴隸，正如我等翼哈特
可汝等人類被囚於奴隸護盾之內！
被發現於此護盾之外，肯定是汝自尋滅亡！
汝於太空中遊歷已是不許之事
如今我等須遵行我等翼哈特族之女皇對烏寬族之誓約。
我等只得動手殺汝了！
```

**Rebuild v3 (clean-room)**:
```
人類,你可**神智混亂**了!?我族說的話,你難道沒聽進去嗎?
你和你們同族,皆是奴隸,如同我族亦然——
只是你們人類,被囚禁在一道奴隸護盾裡頭!
一旦被人發現離開這道護盾,那便是你自尋末路!
你竟在星際間 **正遨遊而行**——此事斷斷不可容許!
如今,我族必須履行我族女皇對烏寬立下的誓約。
我族必須動手——**將你了結**!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ENEMY_MUST_DIE=A` (繼承 shipped) / `ENEMY_MUST_DIE=B` (採用 v3) / `ENEMY_MUST_DIE=C自訂:...`

---

### #7 · `at_least_help_us_homeworld` · 🟠 ORANGE · _sim=0.634_

**英文原文**:
```
You must help us. Surely you owe us this much, at least!
```

**Shipped v0.6**:
```
你必須幫我方。 這點忙至少你欠我方！
```

**Rebuild v3 (clean-room)**:
```
你們必須幫我方。至少這一點——你們是欠我方的!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `at_least_help_us_homeworld=A` (繼承 shipped) / `at_least_help_us_homeworld=B` (採用 v3) / `at_least_help_us_homeworld=C自訂:...`

---

### #8 · `NO_HELP_ENEMY` · 🟠 ORANGE · _sim=0.476; 文言助詞清除=7_

**英文原文**:
```
It is an unbelievable thing!
Ye speak the words that ruffle our feathers and cause our blood to boil!
We, the loyal servants of our Queen, bless her Beak, will not be helping the likes of you
or any of the traitor Yehat bastards ye may have found among the ranks of the starship Clans!
```

**Shipped v0.6**:
```
此言令人難以置信！
汝所言之語，令我等羽翎倒立、血氣翻騰！
本騎士乃女皇陛下之忠僕，願賜福她的鳥喙，絕不會助汝之流
或汝在星艦氏族中或許找到的那些翼哈特叛徒混蛋！
```

**Rebuild v3 (clean-room)**:
```
此事簡直難以置信!
你這番話,令我族羽毛倒豎、血脈沸騰!
我族——女皇忠誠的僕從,願聖喙永耀——絕不會出手助你這等東西,
更遑論那些你或許在星艦氏族當中找到的翼哈特叛徒賤種!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `NO_HELP_ENEMY=A` (繼承 shipped) / `NO_HELP_ENEMY=B` (採用 v3) / `NO_HELP_ENEMY=C自訂:...`

---

### #9 · `give_info` · 🟠 ORANGE · _sim=0.514_

**英文原文**:
```
Surely giving us some scraps of information would be okay, wouldn't it?
```

**Shipped v0.6**:
```
至少給我方一些情報碎片總可以吧？
```

**Rebuild v3 (clean-room)**:
```
就算給我方一點點情報碎屑,總該無妨吧?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `give_info=A` (繼承 shipped) / `give_info=B` (採用 v3) / `give_info=C自訂:...`

---

### #10 · `NO_INFO_FOR_ENEMY` · 🟠 ORANGE · _sim=0.474; 文言助詞清除=8_

**英文原文**:
```
Our Queen has spoken the commands to us, and we are obeying her words!
No assistance, of any kind at all, shall be given to you, human
so do not be making the assumptions, that ye know a right thing from a wrong!
Are ye smarter than the Queen, is that what yer saying, human?
We shall not be giving ye a SCRAP OF MEAT!... much less our secrets.
```

**Shipped v0.6**:
```
我等翼哈特族之女皇已下命令，本氏族遵行她的話語！
任何形式的協助皆不會給汝，人類
莫要以為汝分得清是非對錯！
汝比女皇聰明嗎，是汝所言之意嗎，人類？
我等連一片肉屑都不會給汝！… 更別提我等之秘密。
```

**Rebuild v3 (clean-room)**:
```
我族女皇早已下達旨令,而我族——正謹遵著她的言辭!
人類,任何形式的援助,皆不會給予你,
所以,別再擅自揣測——好像你能分辨是非曲直似的!
你是說你比我族女皇更聰明嗎,人類?
我族連**一塊肉屑**都不會給你!……更遑論我族的機密。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `NO_INFO_FOR_ENEMY=A` (繼承 shipped) / `NO_INFO_FOR_ENEMY=B` (採用 v3) / `NO_INFO_FOR_ENEMY=C自訂:...`

---

### #11 · `what_about_pkunk_royalist` · 🟠 ORANGE · _sim=0.642_

**英文原文**:
```
We have encountered an offshoot of your species, the Pkunk. Tell us about them.
```

**Shipped v0.6**:
```
我方遇到你們的一個分支族群，普恩族。 說說他們吧。
```

**Rebuild v3 (clean-room)**:
```
我方遇到了你們翼哈特的分支——普恩族。跟我方談談他們吧。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_pkunk_royalist=A` (繼承 shipped) / `what_about_pkunk_royalist=B` (採用 v3) / `what_about_pkunk_royalist=C自訂:...`

---

### #12 · `PKUNK_ABSORBED_ROYALIST` · 🟠 ORANGE · _sim=0.636_

**英文原文**:
```
The Pkunk have been absorbed.
They are no more. This is how it should be.
Now the matter is settled, human. Do not be bringing it up again...
```

**Shipped v0.6**:
```
普恩族已被吸收。
他們不復存在。 理當如此。
此事已了，人類。 莫要再提起…
```

**Rebuild v3 (clean-room)**:
```
普恩族早已被吸收殆盡。
他們早已不復存在。這正是本該有的結局。
此事已定,人類。**別再提起**……
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `PKUNK_ABSORBED_ROYALIST=A` (繼承 shipped) / `PKUNK_ABSORBED_ROYALIST=B` (採用 v3) / `PKUNK_ABSORBED_ROYALIST=C自訂:...`

---

### #13 · `HATE_PKUNK_ROYALIST` · 🟠 ORANGE · _sim=0.447; 文言助詞清除=6_

**英文原文**:
```
The cowards live?!! This is unbelievable!!
It is a SAD, SAD day to be hearing this thing from ye, human.
The P... the Pku... I canna even say their vile name!
The Pku... PKU-NK! are the greatest embarrassment our species has ever suffered!
Do not be calling these wretched creatures an offshoot of our species!
Better it is that ye be calling them GARBAGE or DROPPINGS!
Or better yet do not be talking about them at all!
```

**Shipped v0.6**:
```
那些懦夫還活著？！！ 難以置信！！
此乃悲哀，悲哀之日，竟從汝口中聽到此事，人類。
那普… 那普恩… 我連他們卑劣之名都難以啟齒！
那普… 普——恩——族！ 是我族有史以來最大之恥辱！
莫要把那些卑鄙生物稱為我族之分支！
寧可稱他們為垃圾或糞便！
或者最好完全別提他們！
```

**Rebuild v3 (clean-room)**:
```
那些懦夫還活著?!!簡直難以置信!!
人類,從你口中聽到此事——今日真是**沉痛萬分**的一天!
那……那個普……普恩——本騎士連他們污穢的名字都說不出口!
那個普……**普恩!**是我族物種有史以來蒙受過**最深**的羞辱!
別把那些卑劣生物,稱作我族的分支!
你若非要稱呼他們,該叫他們**垃圾**或**糞便**才對!
甚至——**你根本就別再提起他們**才好!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HATE_PKUNK_ROYALIST=A` (繼承 shipped) / `HATE_PKUNK_ROYALIST=B` (採用 v3) / `HATE_PKUNK_ROYALIST=C自訂:...`

---

### #14 · `GOODBYE_AND_DIE_HOMEWORLD` · 🟠 ORANGE · _sim=0.466; 文言助詞清除=4_

**英文原文**:
```
So human, now ye be thinking that ye shall slink away
to commit some vile treason and dirty our Queen's good name. Isn't this true?
Do not be answering! We know the truth.
We will not let ye pass!
```

**Shipped v0.6**:
```
所以人類，如今汝以為汝可以偷偷溜走
去犯下某種卑鄙的叛逆，玷汙我等翼哈特族之女皇令名。 不是嗎？
莫要回答！ 本氏族已知真相。
本氏族不會讓汝走！
```

**Rebuild v3 (clean-room)**:
```
所以啊,人類,你如今正想著要偷偷溜走,
去幹些卑鄙的叛逆勾當、玷污我族女皇的清譽——是不是這樣?
別回答!我族早就知道實情。
我族絕不會放你過去!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GOODBYE_AND_DIE_HOMEWORLD=A` (繼承 shipped) / `GOODBYE_AND_DIE_HOMEWORLD=B` (採用 v3) / `GOODBYE_AND_DIE_HOMEWORLD=C自訂:...`

---

### #15 · `SPACE_HELLO_1` · 🟠 ORANGE · _sim=0.5; 文言助詞清除=9_

**英文原文**:
```
What am I seeing on my view screen!?
It is none other than the flattened old face of our friends the human!
But old ally, are ye not knowing that we, the Yehat are allied with the Ur-Quan now?...
and yer presence outside the slave shield, and in an armed starship
are clear violations of yer Oath of Fealty?!
Whatever shall we do? It just isn't a right thing to kill you, human,
...but as a loyal member of my Clan, I must obey the wishes of our Queen!
```

**Shipped v0.6**:
```
我眼前螢幕上所見為何？！
除了我族老友人類那張扁平的老臉還會是誰！
可老盟友，汝豈不知我等翼哈特族現已與烏寬族結盟？…
汝身在奴役護盾之外、駕武裝星艦
乃明顯違反汝之效忠誓約？！
該當如何是好？ 殺汝實在不是正當之事，人類，
… 可作為本氏族的忠實一員，我須遵從女皇之願！
```

**Rebuild v3 (clean-room)**:
```
我族觀察屏上,看到了什麼!?
這不是別的,正是我族好友——人類——那張扁平的老臉!
但老盟友啊,你難道不知,如今我族翼哈特已與烏寬結盟?……
你出現在奴隸護盾外頭,又駕著武裝星艦
分明違背了你當初的效忠誓約!?
我族該如何是好?要殺你,實在不是件對的事,人類,
……但身為我氏族的忠誠一員,本騎士必須遵行女皇陛下的旨意!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SPACE_HELLO_1=A` (繼承 shipped) / `SPACE_HELLO_1=B` (採用 v3) / `SPACE_HELLO_1=C自訂:...`

---

### #16 · `SPACE_HELLO_2` · 🟠 ORANGE · _sim=0.352; 文言助詞清除=6_

**英文原文**:
```
Human, what are you doing back here!? Are you totally off yer perch!?
We have sympathies fer yer cause, tis true
but we must obey the orders of our Queen, however much we may disagree with them!
```

**Shipped v0.6**:
```
人類，汝回來這裡做什麼？！ 汝之棲杆坍了不成，怎會如此瘋癲？！
我族心繫汝之志業，此為真
可我等須遵行女皇之命，不論我等多麼不同意！
```

**Rebuild v3 (clean-room)**:
```
人類,你回這裡來做什麼!?你是徹底跌下高懸王座了嗎!?
我族對你的信念,確乎懷有同情——這是真的
但我族必須遵從女皇陛下的旨令,不論我族心中有多不贊同!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SPACE_HELLO_2=A` (繼承 shipped) / `SPACE_HELLO_2=B` (採用 v3) / `SPACE_HELLO_2=C自訂:...`

---

### #17 · `SPACE_HELLO_3` · 🟠 ORANGE · _sim=0.341; 文言助詞清除=5_

**英文原文**:
```
Human! I am beginning to think that ye are touched, fer sure!
Ye tempt fate and our sympathy too much, I think.
This time, perhaps we cannot be as much yer friends as ye would like.
```

**Shipped v0.6**:
```
人類！ 我漸信汝之神智已亂，斷斷無疑！
汝挑戰命運與我族同情心過度，我以為。
這一次，我等或許無法如汝所望般與汝為友。
```

**Rebuild v3 (clean-room)**:
```
人類!本騎士開始覺得——你的腦筋確乎已不對勁了!
你試探命運,也試探我族的同情——實在太過分了。
這一回,或許我族已無法像你所期望的那樣,做你的朋友了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SPACE_HELLO_3=A` (繼承 shipped) / `SPACE_HELLO_3=B` (採用 v3) / `SPACE_HELLO_3=C自訂:...`

---

### #18 · `SPACE_HELLO_4` · 🟠 ORANGE · _sim=0.455; 文言助詞清除=4_

**英文原文**:
```
Human! Human. You try our souls with yer return!
What is it ye be wanting now?
```

**Shipped v0.6**:
```
人類！ 人類。 汝之歸來煎熬著我族之靈魂！
汝現在想要什麼？
```

**Rebuild v3 (clean-room)**:
```
人類!人類啊……你的歸來,實在磨煉了我族的靈魂!
你這一回,又想要什麼?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SPACE_HELLO_4=A` (繼承 shipped) / `SPACE_HELLO_4=B` (採用 v3) / `SPACE_HELLO_4=C自訂:...`

---

### #19 · `whats_up_space_1` · 🟠 ORANGE · _sim=0.653_

**英文原文**:
```
We should be allies... friends! Explain why this cannot be.
```

**Shipped v0.6**:
```
我方應是盟友… 朋友！ 解釋為何不能如此。
```

**Rebuild v3 (clean-room)**:
```
我方兩族本應是盟友……是朋友!請說明,為何如今不能如此。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `whats_up_space_1=A` (繼承 shipped) / `whats_up_space_1=B` (採用 v3) / `whats_up_space_1=C自訂:...`

---

### #20 · `GENERAL_INFO_SPACE_1` · 🟠 ORANGE · _sim=0.54; 文言助詞清除=5_

**英文原文**:
```
Your words are flying in the face of the facts, human.
We are no longer being your allies.
But unlike the nobles of our homeworld, we, of the Starship Clans
are bereaved at this course of events.
The Queen's decision to be joining the Hierarchy, pains us!
```

**Shipped v0.6**:
```
汝之言飛在事實面前，人類。
我族已非汝之盟。
可與母星那些貴族不同，我等星艦氏族
對此事態的發展深感悲慟。
女皇加入階層之決定，令我族心痛！
```

**Rebuild v3 (clean-room)**:
```
人類,你所言——正逆風飛在事實的臉上。
我族已不再是你的盟友。
但與母星巢中的貴族不同,我族——星艦氏族的一員——
對這番事態演變,深感喪痛。
女皇陛下決意加入烏寬階層一事,令我族心痛!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_SPACE_1=A` (繼承 shipped) / `GENERAL_INFO_SPACE_1=B` (採用 v3) / `GENERAL_INFO_SPACE_1=C自訂:...`

---

### #21 · `whats_up_space_2` · 🟠 ORANGE · _sim=0.6_

**英文原文**:
```
How did the Ur-Quan defeat you? What happened?
```

**Shipped v0.6**:
```
烏寬族是怎麼打敗你們的？ 到底怎麼回事？
```

**Rebuild v3 (clean-room)**:
```
烏寬是怎麼打敗你們的?究竟發生了什麼事?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `whats_up_space_2=A` (繼承 shipped) / `whats_up_space_2=B` (採用 v3) / `whats_up_space_2=C自訂:...`

---

### #22 · `GENERAL_INFO_SPACE_2` · 🟠 ORANGE · _sim=0.609; 文言助詞清除=3; 鳥鳴補回=1_

**英文原文**:
```
WE - WERE - NOT - DEFEATED, HUMAN!!!!
Never! Never in the two-thousand years of the Veep-Neep Queens
have the Yehat ever, EVER suffered a defeat!
It is this fact ALONE that is making our loyalty to the Queen so strong!
This is the unbreakable bond that keeps the Clans together!
When the Ur-Quan were entering our home star system at <% comm.getStarName("Gamma Serpentis", "yehat") %>...
...we had a thousand starships prepared to defend our home
and then... the Queen... She... she
allied with the Ur-Quan
and the fight is over before it is even begun. AWK!
```

**Shipped v0.6**:
```
我等翼哈特族─從未─被打敗，人類！！！！
從未！ 維普涅普女皇兩千年的統治中
翼哈特族從未、從未嘗過敗績！
光憑此事實，我族對女皇之忠誠才如此堅定！
這是把眾氏族凝在一起的、不可斷絕之連結！
當烏寬族進入我族母星系 <% comm.getStarName("巨蛇座γ", "yehat") %> （Gamma Serpentis） 時…
…我等已有千艘星艦準備護衛家園
然後… 女皇… 她… 她
與烏寬族結盟
戰事未啓，便已終焉。 呱！（AWK!）
```

**Rebuild v3 (clean-room)**:
```
**我族——並未——戰敗,人類!!!!**
絕無!在維普涅普王朝的兩千年裡
翼哈特從未,從未——嚐過戰敗的滋味!
正是這件事實——這唯一的事實——使我族對女皇陛下的忠誠如此堅固!
這正是把眾氏族凝聚在一起、無法割斷的血誓!
當烏寬正入侵我族母星星系——<% comm.getStarName("巨蛇座γ", "yehat") %>（Gamma Serpentis）——那一刻……
……我族已備好千艘星艦,守衛家園
然後……女皇陛下……她……她
與烏寬結了盟
戰鬥還未開始,便已結束。呱!(AWK!)
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_SPACE_2=A` (繼承 shipped) / `GENERAL_INFO_SPACE_2=B` (採用 v3) / `GENERAL_INFO_SPACE_2=C自訂:...`

---

### #23 · `whats_up_space_3` · 🟠 ORANGE · _sim=0.737_

**英文原文**:
```
What about your legendary honor? Your courage? What would the Shofixti think?!
```

**Shipped v0.6**:
```
那你們的傳奇榮譽呢？ 你們的勇氣呢？ 修烈士族會怎麼想？！
```

**Rebuild v3 (clean-room)**:
```
那你們傳奇般的榮耀呢?你們的勇氣呢?修烈士族會怎麼想?!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `whats_up_space_3=A` (繼承 shipped) / `whats_up_space_3=B` (採用 v3) / `whats_up_space_3=C自訂:...`

---

### #24 · `GENERAL_INFO_SPACE_3` · 🟠 ORANGE · _sim=0.522; 文言助詞清除=1; 鳥鳴補回=3_

**英文原文**:
```
(sob!)... (whimper) We have fallen so far. (sob!)
We are not being the same (whimper!) great birds of prey your people were once knowing and trusting.
We have each betrayed the honor of our Clan, (whimper!)... just as our Queen
is betraying each of us with her association with the Ur-Quan...
If the valiant child species, the (sob-gulp!)... Shofixti were being here today
the shame!... Oh the shame!... it would be unbearable!
(whimper!)... awk!
```

**Shipped v0.6**:
```
(嗚咽！)…(啜泣) 我族已墮落至此。 (嗚咽！)
我族已非(啜泣！)貴族曾知曉並信任的偉大猛禽。
我等各自背叛了氏族的榮譽，(啜泣！)…正如我族之女皇
以她與烏寬族的勾結背叛了我等每一人…
若那勇武的子輩物種，那(嗚咽-哽咽！)…修烈士族今日還在
那羞恥！… 喔那羞恥！… 會令人難以承受！
(啜泣！)…呱！（AWK!）
```

**Rebuild v3 (clean-room)**:
```
(嗚咽!)……(低鳴!)我族……墮落得如此深遠。(嗚咽!)
我族已不再是——(低鳴!)——你們曾經認識、曾經信賴的那些猛禽了。
我族每一員都背棄了我氏族的榮耀,(低鳴!)……正如女皇陛下
以與烏寬的結盟,正背棄我族每一員……
若那勇敢的子輩物種——(嗚咽——吞嚥聲!)……修烈士族——今日仍在這裡
那份羞愧!……啊那份羞愧!……將無可承受!
(低鳴!)……呱!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_SPACE_3=A` (繼承 shipped) / `GENERAL_INFO_SPACE_3=B` (採用 v3) / `GENERAL_INFO_SPACE_3=C自訂:...`

---

### #25 · `GENERAL_INFO_SPACE_4` · 🟠 ORANGE · _sim=0.444; 文言助詞清除=3_

**英文原文**:
```
NO!  WE ARE NOT SLAVES!! WE ARE!... We are!... we are...
Battle Thralls.
```

**Shipped v0.6**:
```
不！ 我等非奴！！ 我等乃！… 我等乃！… 我等乃…
戰奴。
```

**Rebuild v3 (clean-room)**:
```
不!我族並非奴隸!!我族——是!……我族是!……我族是……
戰奴。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GENERAL_INFO_SPACE_4=A` (繼承 shipped) / `GENERAL_INFO_SPACE_4=B` (採用 v3) / `GENERAL_INFO_SPACE_4=C自訂:...`

---

### #26 · `i_demand_you_ally_space` · 🟠 ORANGE · _sim=0.882; 文言助詞清除=5_

**英文原文**:
```
By your honor, Yehat captain, I, <% state.sis.getCaptainName() %>, master of the <% state.sis.getShipName() %>, in the name of <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> call upon the Starship Clans to honor their word and fight for our cause!
```

**Shipped v0.6**:
```
以爾之榮譽為誓，翼哈特族艦長，我 <% state.sis.getCaptainName() %>，<% state.sis.getShipName() %> 號之主，以 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> 之名，呼籲星艦氏族信守諾言，為我方之志業而戰！
```

**Rebuild v3 (clean-room)**:
```
以你們的榮耀為誓,翼哈特艦長——我,<% state.sis.getCaptainName() %>,<% state.sis.getShipName() %>的主宰,以 <% comm.getPhrase("name_" .. (state.prop.get("NEW_ALLIANCE_NAME") + 1)) %> 為名,呼籲星艦氏族——恪守你們的誓言,為我方大業而戰!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `i_demand_you_ally_space=A` (繼承 shipped) / `i_demand_you_ally_space=B` (採用 v3) / `i_demand_you_ally_space=C自訂:...`

---

### #27 · `WE_CANNOT_2` · 🟠 ORANGE · _sim=0.475; 文言助詞清除=6_

**英文原文**:
```
Can't ye see that ye are killing me human?
The shame!... the awful shame of it!
What ye say is true, we SHOULD be under the same wing
but DAMN YER EYES!... our Queen has given the Ur-Quan our allegiance
and there is nothing I can be doing about it now!
```

**Shipped v0.6**:
```
汝豈看不出汝正在殺我，人類？
那羞恥！… 那可怕的羞恥！
汝所言為真，我等本應在同一羽翼之下
可該死！… 我族之女皇已將我等之效忠奉予烏寬族
如今我對此無能為力！
```

**Rebuild v3 (clean-room)**:
```
你難道看不見自己**正在殺著**我嗎,人類?
羞愧啊!……這無可言喻的羞愧!
你所言不假,我族**本應**與你們同翼並肩——
但可恨啊!……我族的女皇陛下,已將效忠獻給了烏寬
如今我族——正無能為力!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `WE_CANNOT_2=A` (繼承 shipped) / `WE_CANNOT_2=B` (採用 v3) / `WE_CANNOT_2=C自訂:...`

---

### #28 · `at_least_help_us_space` · 🟠 ORANGE · _sim=0.722_

**英文原文**:
```
At least help us with materials for our struggle!
```

**Shipped v0.6**:
```
那至少幫我方一些物資協助我方奮戰！
```

**Rebuild v3 (clean-room)**:
```
至少,給我方一些物資,幫助我方奮戰吧!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `at_least_help_us_space=A` (繼承 shipped) / `at_least_help_us_space=B` (採用 v3) / `at_least_help_us_space=C自訂:...`

---

### #29 · `SORRY_CANNOT` · 🟠 ORANGE · _sim=0.351; 文言助詞清除=3_

**英文原文**:
```
We cannot!
To be doing so would be a direct violation of our royal Queen's commands!
```

**Shipped v0.6**:
```
我等不能！
若如此為之，實乃公然違逆我族尊貴女皇之命！
```

**Rebuild v3 (clean-room)**:
```
我族做不到!
若這樣做,便是直接違逆我族女皇陛下所頒的旨令!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SORRY_CANNOT=A` (繼承 shipped) / `SORRY_CANNOT=B` (採用 v3) / `SORRY_CANNOT=C自訂:...`

---

### #30 · `dishonor` · 🟠 ORANGE · _sim=0.489_

**英文原文**:
```
Think Yehat. The sheer dishonor of it all.
```

**Shipped v0.6**:
```
想想吧，翼哈特族。 這一切的極端不榮譽。
```

**Rebuild v3 (clean-room)**:
```
想一想,翼哈特——這一切,是何等徹底的失卻榮耀啊。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `dishonor=A` (繼承 shipped) / `dishonor=B` (採用 v3) / `dishonor=C自訂:...`

---

### #31 · `HERES_A_HINT` · 🟠 ORANGE · _sim=0.523; 文言助詞清除=8_

**英文原文**:
```
We cannot be giving ye material aid, Captain.
But perhaps ye can make use of this information, Captain.
When we were fighting the Great War against the Mycons
we encountered a number of odd worlds which seemed to be having their crust shattered.
Molten lava ran across the surface in huge rivers, and dense metallic elements were abundant.
But the strangest world we found was the first planet at the star at coordinates <% comm.getPoint("639.5 : 231.2", "sun device") %>.
The Mycons were guarding this planet with an almost limitless number of their Podships
as though there were something of great value there.
We could never break through their forces, though we destroyed scores of their ships.
Perhaps, if ye fare better than us, or can somehow trick the Mycons to let ye land
you may discover this secret, and it may help ye in yer quest.
```

**Shipped v0.6**:
```
物資援助我等無法給爾，艦長。
可或許爾能用這條情報，艦長。
當我等翼哈特族與麥孔族大戰時
我等曾遇不少怪異的世界，其地殼似乎被擊碎過。
熔漿在地表上如巨河奔流，濃密金屬元素豐富。
但我族發現最奇特的世界，是位於座標 <% comm.getPoint("639.5 : 231.2", "sun device") %> 恆星旁的第一顆行星。
麥孔族用近乎無窮的莢艦守著這顆行星
彷彿那裡有極高價值之物。
我等從未能突破他們的兵力，儘管我等摧毀了他們數十艘船。
或許，若爾比我等更有本事，或能設法騙麥孔族讓爾登陸
爾可能會發現這個秘密，或許對爾之征程有所助益。
```

**Rebuild v3 (clean-room)**:
```
艦長,我族無法給你物資上的援助。
但或許——你能用得上這一則情報,艦長。
昔日我族與麥孔族鏖戰時期
曾發現數座奇異的世界,那些世界的地殼彷彿正被撕裂
熔岩如巨河般在地表流淌,重金屬元素遍地皆是。
但我族所遇到最古怪的一顆星球,是座標 <% comm.getPoint("639.5 : 231.2", "sun device") %> 所指星系的第一顆行星。
麥孔族守衛那顆星球時,派出了近乎無盡的莢艦
彷彿那裡確乎藏著什麼絕大的珍寶。
我族從未能突破他們的軍勢,雖然我族擊沉了他們數十艘星艦。
或許,倘若你的運氣比我族更佳,或能設法誘騙麥孔族允你降落
你將會揭開這樁秘密——而此秘密,或許能助你這番追尋。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HERES_A_HINT=A` (繼承 shipped) / `HERES_A_HINT=B` (採用 v3) / `HERES_A_HINT=C自訂:...`

---

### #32 · `what_about_pkunk_space` · 🟠 ORANGE · _sim=0.444_

**英文原文**:
```
Tell us about the Pkunk.
```

**Shipped v0.6**:
```
說說普恩族吧。
```

**Rebuild v3 (clean-room)**:
```
跟我方講講普恩族的事。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_pkunk_space=A` (繼承 shipped) / `what_about_pkunk_space=B` (採用 v3) / `what_about_pkunk_space=C自訂:...`

---

### #33 · `PKUNK_ABSORBED_SPACE` · 🟠 ORANGE · _sim=0.471; 文言助詞清除=2_

**英文原文**:
```
This is a matter for the Yehat, human, and ONLY for the Yehat.
The Pkunk have been absorbed... and that is being the end of it.
Do not ask further about this matter.
```

**Shipped v0.6**:
```
此事只關翼哈特族之事，人類，僅是翼哈特族之事。
普恩族已被吸收… 到此為止。
莫再問及此事。
```

**Rebuild v3 (clean-room)**:
```
人類,這是翼哈特的家務事,**唯有**翼哈特才能過問。
普恩族早已被吸收殆盡……此事就此了結。
別再追問這事了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `PKUNK_ABSORBED_SPACE=A` (繼承 shipped) / `PKUNK_ABSORBED_SPACE=B` (採用 v3) / `PKUNK_ABSORBED_SPACE=C自訂:...`

---

### #34 · `HATE_PKUNK_SPACE` · 🟠 ORANGE · _sim=0.542; 文言助詞清除=4_

**英文原文**:
```
You have met them!?? The wretched creatures are alive?!!
You should be telling us where they are, Captain!
Tell us so that we can be correcting the mistake made a thousand years ago
when we permitted the Pkunk to leave our Nest alive.
By all rights, we should have eliminated the craven cowards down to the last bird!
```

**Shipped v0.6**:
```
汝遇到他們了？！！ 那些可鄙的生物還活著？！！
爾該告訴我等他們在哪，艦長！
告訴我等，好讓我族彌補一千年前所犯之錯
當我等允許普恩族活著離開我族之巢穴。
按理，本氏族本該將那些懦弱者一鳥不剩全部消滅！
```

**Rebuild v3 (clean-room)**:
```
你居然遇到了他們?!!那些卑劣生物還活著?!!
艦長,你該告訴我族——他們在哪裡!
告訴我族,讓我族——正好——把千年前所犯的過錯給糾正過來
就是那次:我族竟允許普恩族活著離開我族的巢!
按理說,我族本該把那些懦弱的膽小鬼——一鳥不留——盡數剿滅!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HATE_PKUNK_SPACE=A` (繼承 shipped) / `HATE_PKUNK_SPACE=B` (採用 v3) / `HATE_PKUNK_SPACE=C自訂:...`

---

### #35 · `GOODBYE_AND_DIE_SPACE` · 🟠 ORANGE · _sim=0.494; 文言助詞清除=3_

**英文原文**:
```
You are causing us sorrow, human, sorrow indeed,
because now we must obey the commands of our Queen and destroy you.
```

**Shipped v0.6**:
```
爾令我族心生悲傷，人類，深深的悲傷，
因為現在我等須遵行女皇之命，將爾摧毀。
```

**Rebuild v3 (clean-room)**:
```
你正給我族帶來悲傷,人類——確確實實的悲傷——
只因如今我族必須遵行女皇陛下的旨令,將你摧毀。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GOODBYE_AND_DIE_SPACE=A` (繼承 shipped) / `GOODBYE_AND_DIE_SPACE=B` (採用 v3) / `GOODBYE_AND_DIE_SPACE=C自訂:...`

---

### #36 · `shofixti_alive_1` · 🟠 ORANGE · _sim=0.744_

**英文原文**:
```
This may come as a shock, but the Shofixti are reborn.
```

**Shipped v0.6**:
```
這消息可能令你們震撼，但修烈士族重生了。
```

**Rebuild v3 (clean-room)**:
```
這消息或許令你們震驚——但修烈士族已經重生了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `shofixti_alive_1=A` (繼承 shipped) / `shofixti_alive_1=B` (採用 v3) / `shofixti_alive_1=C自訂:...`

---

### #37 · `shofixti_alive_2` · 🟠 ORANGE · _sim=0.708_

**英文原文**:
```
We have a Shofixti Captain here with us. Now do you believe?
```

**Shipped v0.6**:
```
我方現在船上有一位修烈士族艦長。 現在你信了嗎？
```

**Rebuild v3 (clean-room)**:
```
我方這裡有一位修烈士艦長同行。現在你們相信了嗎?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `shofixti_alive_2=A` (繼承 shipped) / `shofixti_alive_2=B` (採用 v3) / `shofixti_alive_2=C自訂:...`

---

### #38 · `SEND_HIM_OVER_1` · 🟠 ORANGE · _sim=0.453; 文言助詞清除=5_

**英文原文**:
```
If this is being a true thing, there will be many changes.
But we are a species long wise in the ways of deceit.
Ye must be proving these words ye say, Captain.
Send the Shofixti to us as a way of proof.
```

**Shipped v0.6**:
```
若此言為真，將有諸多變革。
可我族乃善辨詭計之眾。
爾必須證明爾所言之語，艦長。
把修烈士族送至我等這裡以為證。
```

**Rebuild v3 (clean-room)**:
```
倘若此事屬實——那將會有許多變化。
但我族——是一支對詭詐伎倆久經世故的物種。
艦長,你必須證明你所說的每一句話。
把那位修烈士族——派到我族這裡來——作為證明。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `SEND_HIM_OVER_1=A` (繼承 shipped) / `SEND_HIM_OVER_1=B` (採用 v3) / `SEND_HIM_OVER_1=C自訂:...`

---

### #39 · `JUST_A_TRICK_1` · 🟠 ORANGE · _sim=0.34; 文言助詞清除=6_

**英文原文**:
```
It is a trick then, isn't it! And nothing more.
Human, we have been patient with ye up to this point, but now ye have gone too far.
Ye have most skillfully rubbed the salt into our wounds, and ye shall pay fer it in blood!
```

**Shipped v0.6**:
```
此乃詭計，不是嗎！ 別無他物。
人類，我族對爾一直耐心至此，但如今爾太過分了。
爾巧妙地把鹽揉進我族之傷口，爾當以鮮血作為代價！
```

**Rebuild v3 (clean-room)**:
```
那麼——這就是個詭計,是不是!不過如此。
人類,我族至此對你已是萬般忍耐——但你此番已越過分寸太遠。
你以無比純熟的手法,將鹽撒進我族的傷口——這筆帳,你將以血償還!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `JUST_A_TRICK_1=A` (繼承 shipped) / `JUST_A_TRICK_1=B` (採用 v3) / `JUST_A_TRICK_1=C自訂:...`

---

### #40 · `JUST_A_TRICK_2` · 🟠 ORANGE · _sim=0.426; 文言助詞清除=2_

**英文原文**:
```
Another TRICK!
Yer lying tongue has doomed ye!
```

**Shipped v0.6**:
```
又是詭計！
爾說謊的舌頭已判了爾死刑！
```

**Rebuild v3 (clean-room)**:
```
又一個**詭計**!
你那撒謊的舌頭,已注定了你的滅亡!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `JUST_A_TRICK_2=A` (繼承 shipped) / `JUST_A_TRICK_2=B` (採用 v3) / `JUST_A_TRICK_2=C自訂:...`

---

### #41 · `ok_send` · 🟠 ORANGE · _sim=0.4_

**英文原文**:
```
All right, I'll send over the Shofixti... but don't mess with him, okay?
```

**Shipped v0.6**:
```
好啦，我會派修烈士族過去… 但不要傷害他，好嗎？
```

**Rebuild v3 (clean-room)**:
```
好吧,我方會把那位修烈士送過去……但你們可別對他亂來,聽到沒?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ok_send=A` (繼承 shipped) / `ok_send=B` (採用 v3) / `ok_send=C自訂:...`

---

### #42 · `WE_REVOLT` · 🟠 ORANGE · _sim=0.461; 文言助詞清除=11_

**英文原文**:
```
We are scanning the separation of a vessel from yer fleet, Captain
and indeed, its configuration matches that of a Shofixti Scout vessel.
This had better not be a trick, Captain!
We are knowing the power of a Glory Device, and if you detonate the weapon near us
the price for you shall be dear, very dear.
The Scout has docked, and we await the pilot's appearance at the airlock.
The atmosphere cycle is complete... the door slides open... and
IT IS TRUE!!! THE SHOFIXTI ARE ALIVE!!!
Look at that furred muzzle, those shining black eyes, the sweet claws!
Our children have returned from oblivion!!
But now we are faced with the cruellest truth!...
...We who have sacrificed our honor! We who have lain with the enemy!
WE ARE NOT WORTHY! WE ARE NOTHING!...We are less than nothing.
But wait! We are not Spathi. We are Yehat... OF THE STARSHIP CLANS!
We will NOT live this lie any longer!
Listen as I speak these words! If our Queen makes the dishonorable command
then it is THE QUEEN WHO HAS NO HONOR!
And a dishonorable Queen is NO QUEEN AT ALL!
We, the Zeep-Zeep, are the only Clan who remember the TRUE MEANING of honor
we shall TEAR THE QUEEN FROM HER THRONE!
The two-thousand year reign of the Veep-Neep Queens IS OVER!
THE REVOLUTION HAS BEGUN!
```

**Shipped v0.6**:
```
我方掃描到有一艘船艦自爾艦隊分離，艦長
且其構型確與修烈士族偵察艦相符。
這最好別是詭計，艦長！
我等深知榮耀彈的威力，若爾在我等附近引爆該武器
爾將付出的代價將極為慘重，極為慘重。
偵察艦已對接，我方在氣閘等候飛行員現身。
大氣循環完成… 艙門滑開… 然後
是真的！！！ 修烈士族還活著！！！
看那毛絨口鼻、那閃亮黑眼、那可愛的爪子！
我族之子輩自幽冥歸來了！！
可如今我族面對最殘酷之真相！…
…我族犧牲了榮譽！ 我族與敵共眠！
我等不配！ 我等一無是處！… 我等連虛無都不如。
但等等！ 我等非史怕族。 我等乃翼哈特族… 星艦氏族之屬！
我等不會再活在這謊言中！
聽我說出此言！ 若我族之女皇下達不榮譽之命
那便是女皇本身無榮譽！
而無榮譽之女皇根本不算女皇！
我等齊普齊普氏族，是唯一還記得榮譽真義的氏族
我等必自寶座上扯下女皇！
維普涅普女皇兩千年之統治結束了！
革命已經展開！
```

**Rebuild v3 (clean-room)**:
```
艦長——我族正掃描到一艘船艦,正從你艦隊分離而出
確實,其構型與修烈士偵察艦相符。
這最好不是個詭計,艦長!
我族深知**榮耀彈**的威力——若你在我族附近引爆這件武器
那代價,你將付得——極其慘重、極其慘重。
偵察艦已對接,我族——正在氣密艙門邊——等候那位駕駛員現身。
大氣循環完成……艙門滑開……然後——
**是真的!!!修烈士族還活著!!!**
看那毛茸茸的口鼻!那閃亮的黑眼!那可愛的爪子!
我族的後嗣——已從湮沒深淵歸來!!
然而,此刻——我族正面對**最為殘酷**的真相!……
……我族——是那些犧牲了自身榮耀的族人!是那些與敵人同床共枕的族人!
**我族不配!我族甚為虛無!**……我族甚至不如虛無。
但——且慢!我族並非史怕族!我族是翼哈特——**星艦氏族的一員!**
我族——**絕不**再苟活於這番謊言裡!
聽本騎士這番話語!若我族的女皇下達失卻榮耀的旨令——
那便是**失卻榮耀的,是女皇本人**!
**一位失卻榮耀的女皇——根本不配為皇!**
我族——翼-翼氏族——是唯一還記得榮耀**真正意義**的氏族!
我族——**將把女皇從她的王座上——扯下!**
維普涅普王朝——兩千年的統治——**已然告終!**
**革命——已然掀起!**
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `WE_REVOLT=A` (繼承 shipped) / `WE_REVOLT=B` (採用 v3) / `WE_REVOLT=C自訂:...`

---

### #43 · `ROYALIST_SPACE_HELLO_1` · 🟠 ORANGE · _sim=0.482; 文言助詞清除=15_

**英文原文**:
```
Human... ye shall never be fully comprehending the damage you are doing now to our Yehat culture.
For fully TWO THOUSAND YEARS there has been peace between the Clans!...
...and now you have cast the ancient seed of dissension between our beaks!
The bloody Wars of Ascension are renewed, and YOU are the cause, Captain!
While the Zeep-Zeep traitors may be your allies, Captain
I can be assuring you that we, of the Feep-Eeep Starship Clan
are wanting nothing more dearly than your death!
```

**Shipped v0.6**:
```
人類… 爾永遠無法完全理解爾如今對我等翼哈特族之文化所造之傷害。
整整兩千年，眾氏族之間一直和平！…
…如今爾在我族鳥喙之間播下不和之古種！
血腥的升位之戰再起，而爾正是禍源，艦長！
齊普齊普叛徒或許是爾之盟友，艦長
可本費普伊普星艦氏族向爾保證
最渴望的莫過於爾之死！
```

**Rebuild v3 (clean-room)**:
```
人類啊……你將永遠無法完全領會——此番你正在對我族翼哈特文化所造成的損害。
整整**兩千年**——眾氏族間一直是和平的!……
……而如今,你卻在我族喙間——播下了古老的紛爭種子!
血腥的「升位戰爭」再度掀起——艦長,肇因**正是你**!
翼-翼氏族那些叛徒或許已成為你的盟友,艦長
但本騎士可以向你確保——我族——費普-伊普(Feep-Eeep) 星艦氏族——
正沒有比看你死更令我族珍愛的事!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ROYALIST_SPACE_HELLO_1=A` (繼承 shipped) / `ROYALIST_SPACE_HELLO_1=B` (採用 v3) / `ROYALIST_SPACE_HELLO_1=C自訂:...`

---

### #44 · `ROYALIST_HOMEWORLD_HELLO_1` · 🟠 ORANGE · _sim=0.375; 文言助詞清除=4_

**英文原文**:
```
Human! Like all heroes, ye be as brainless as ye are brave.
Do ye not know, that here there be none of the traitorous Zeep-Zeep Starship Clans!
Ye are as good as dead, human.
```

**Shipped v0.6**:
```
人類！ 一如眾英雄，爾勇敢卻無腦。
爾豈不知，此處無叛逆的齊普齊普星艦氏族一員！
爾等同已死之人，人類。
```

**Rebuild v3 (clean-room)**:
```
人類!像所有英雄一樣,你既無腦——也勇敢。
你難道不知——此地並無任何叛徒翼-翼星艦氏族的人!
人類——你可算是死定了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ROYALIST_HOMEWORLD_HELLO_1=A` (繼承 shipped) / `ROYALIST_HOMEWORLD_HELLO_1=B` (採用 v3) / `ROYALIST_HOMEWORLD_HELLO_1=C自訂:...`

---

### #45 · `ROYALIST_HOMEWORLD_HELLO_2` · 🟠 ORANGE · _sim=0.359; 文言助詞清除=4_

**英文原文**:
```
Cease yer bloody taunting, human!
Ye dance like a sick breeg, never engaging us in battle-to-the-death
as honor and true courage are demanding!
```

**Shipped v0.6**:
```
停止爾之血腥挑釁，人類！
爾似病布利格般蹦跳戲耍，未曾與我等生死相搏
如同榮譽與真勇所要求之事！
```

**Rebuild v3 (clean-room)**:
```
別再嘰嘰喳喳地挑釁了,人類!
你像一頭生病的布利格獸(breeg)一樣亂舞——從不肯與我族一戰決死
——就如榮耀與真正的勇氣所要求的那樣!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ROYALIST_HOMEWORLD_HELLO_2=A` (繼承 shipped) / `ROYALIST_HOMEWORLD_HELLO_2=B` (採用 v3) / `ROYALIST_HOMEWORLD_HELLO_2=C自訂:...`

---

### #46 · `how_is_rebellion` · 🟠 ORANGE · _sim=0.5_

**英文原文**:
```
So, how's the revolution going for you guys?
```

**Shipped v0.6**:
```
所以，你們的革命進行得如何？
```

**Rebuild v3 (clean-room)**:
```
那個——你們的革命,進行得怎麼樣了?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `how_is_rebellion=A` (繼承 shipped) / `how_is_rebellion=B` (採用 v3) / `how_is_rebellion=C自訂:...`

---

### #47 · `ROYALIST_REBELLION_1` · 🟠 ORANGE · _sim=0.461; 文言助詞清除=3_

**英文原文**:
```
Revolution!? Ye compliment yerself unnecessarily, Captain.
This is nothing more than a... band of thugs trying to undo the peace of a hundred generations!
We will roast the traitors in their ships, and crack the eggs in their Clanhome
so that never again will the Zeep-Zeep criminals be flying though our stars.
```

**Shipped v0.6**:
```
革命？！ 爾不必抬舉自己，艦長。
這不過是… 一群暴徒想要毀掉百代的和平！
本氏族將把叛徒燒烤在他們的船艦上，敲碎叛徒族巢之卵
讓齊普齊普罪人永遠不再飛過我等翼哈特族之星域。
```

**Rebuild v3 (clean-room)**:
```
革命!?艦長,你自我抬舉,實無必要。
這不過是……一群暴徒,妄圖顛覆百代累積下來的和平!
我族將把那些叛徒——在他們的星艦裡烤熟——並敲碎他們氏族巢裡的每一顆蛋
好讓翼-翼氏族的罪犯,再也無法飛掠我族的星辰。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ROYALIST_REBELLION_1=A` (繼承 shipped) / `ROYALIST_REBELLION_1=B` (採用 v3) / `ROYALIST_REBELLION_1=C自訂:...`

---

### #48 · `ROYALIST_REBELLION_2` · 🟠 ORANGE · _sim=0.478; 文言助詞清除=1_

**英文原文**:
```
Do not be worrying yerself, Captain! Victory is almost within our grasp.
```

**Shipped v0.6**:
```
莫替自己擔憂，艦長！ 勝利幾乎近在本氏族之手。
```

**Rebuild v3 (clean-room)**:
```
別為此擔憂,艦長!勝利——已幾乎握在我族掌中。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ROYALIST_REBELLION_2=A` (繼承 shipped) / `ROYALIST_REBELLION_2=B` (採用 v3) / `ROYALIST_REBELLION_2=C自訂:...`

---

### #49 · `sorry_about_revolution` · 🟠 ORANGE · _sim=0.51_

**英文原文**:
```
Gosh, I'm sorry about this revolution thing. I didn't mean any harm.
```

**Shipped v0.6**:
```
哎唷，這次革命事件我很抱歉。 我沒有惡意。
```

**Rebuild v3 (clean-room)**:
```
唉,這場革命的事……我方真的很抱歉。我方並沒有想要造成傷害。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `sorry_about_revolution=A` (繼承 shipped) / `sorry_about_revolution=B` (採用 v3) / `sorry_about_revolution=C自訂:...`

---

### #50 · `ALL_YOUR_FAULT` · 🟠 ORANGE · _sim=0.596; 文言助詞清除=3_

**英文原文**:
```
The pain and suffering of this useless conflict are being nothing but a tragic waste of life.
Congratulate yourself, Captain. The source of all this death and misery is yerself.
```

**Shipped v0.6**:
```
此無用衝突之痛苦與磨難，只是生命的悲慘浪費。
恭喜自己吧，艦長。 這一切死亡與苦難之根源，就是爾自己。
```

**Rebuild v3 (clean-room)**:
```
這場無謂衝突所帶來的痛苦與折磨——不過是生命的一場悲慘揮霍罷了。
恭喜你,艦長。這一切死亡與苦難的根源——正是**你自己**。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ALL_YOUR_FAULT=A` (繼承 shipped) / `ALL_YOUR_FAULT=B` (採用 v3) / `ALL_YOUR_FAULT=C自訂:...`

---

### #51 · `bye_royalist` · 🟠 ORANGE · _sim=0.667_

**英文原文**:
```
Goodbye Royalist fool!
```

**Shipped v0.6**:
```
再見了，保皇派蠢貨！
```

**Rebuild v3 (clean-room)**:
```
再會了,保皇派的蠢貨!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `bye_royalist=A` (繼承 shipped) / `bye_royalist=B` (採用 v3) / `bye_royalist=C自訂:...`

---

### #52 · `GOODBYE_AND_DIE_ROYALIST` · 🟠 ORANGE · _sim=0.649; 文言助詞清除=3_

**英文原文**:
```
Now ye must pay fer yer crimes, human!
```

**Shipped v0.6**:
```
如今爾必須為爾之罪付出代價，人類！
```

**Rebuild v3 (clean-room)**:
```
如今——你必須為你的罪行付出代價,人類!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GOODBYE_AND_DIE_ROYALIST=A` (繼承 shipped) / `GOODBYE_AND_DIE_ROYALIST=B` (採用 v3) / `GOODBYE_AND_DIE_ROYALIST=C自訂:...`

---

### #53 · `name_3` · 🟠 ORANGE · _sim=0.727_

**英文原文**:
```
The United Federation of Worlds
```

**Shipped v0.6**:
```
聯合世界聯邦
```

**Rebuild v3 (clean-room)**:
```
諸世界聯邦
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `name_3=A` (繼承 shipped) / `name_3=B` (採用 v3) / `name_3=C自訂:...`

---

### #54 · `OUT_TAKES` · 🟠 ORANGE · _sim=0.463; 文言助詞清除=3_

**英文原文**:
```
So, I suppose you are wondering what I'm doing at this control console
well, I guess I can tell you now.
I'm writing a screenplay!
It's an existential thriller!
Kind of a cross between a Woody Allen angst-fest mixed with some of Tobe Hooper's best work.
But actually, this is just my way of getting my wing in the door, you see
what I really want to do is DIRECT!
```

**Shipped v0.6**:
```
所以，我猜爾正納悶我在這控制台前做什麼
嗯，我想我現在可以告訴爾了。
我在寫劇本！
是個存在主義驚悚劇！
有點像伍迪·艾倫的焦慮盛宴，融合陶比·胡柏最好的作品。
可其實，這只是我把翅膀伸進門內的方式，爾看
我真正想做的是導演！
```

**Rebuild v3 (clean-room)**:
```
所以嘛,本騎士猜——你正在納悶,本騎士在這操控台前到底在幹什麼
好吧,大概可以告訴你了。
本騎士——正在寫一部劇本!
是齣**存在主義驚悚劇**!
大概是伍迪·艾倫(Woody Allen)那種焦慮劇——混上一點托比·胡珀(Tobe Hooper)的經典恐怖手法。
不過說真的,這只是本騎士——想把翅膀伸進門的方式,你懂吧
本騎士**真正**想做的——是**當導演**!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `OUT_TAKES=A` (繼承 shipped) / `OUT_TAKES=B` (採用 v3) / `OUT_TAKES=C自訂:...`

---

### #55 · `REBEL_HELLO_1` · 🟠 ORANGE · _sim=0.479; 文言助詞清除=1_

**英文原文**:
```
Welcome to ye, human friend and ally!
The revolution has begun and clans flock to our cause!
```

**Shipped v0.6**:
```
歡迎爾至此,人類友人與盟友！
革命已然開始,氏族紛紛歸附我等大業！
```

**Rebuild v3 (clean-room)**:
```
歡迎你——人類朋友,人類盟友!
革命已然掀起——眾氏族正紛紛湧向我族的義舉!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_HELLO_1=A` (繼承 shipped) / `REBEL_HELLO_1=B` (採用 v3) / `REBEL_HELLO_1=C自訂:...`

---

### #56 · `REBEL_HELLO_2` · 🟠 ORANGE · _sim=0.577; 文言助詞清除=2_

**英文原文**:
```
Greetings friend from Earth!
The head of our revolution, Cheep-Guava, has led us to many great victories.
We have cleaned the Royalist traitors from five star systems!
```

**Shipped v0.6**:
```
來自地球之友人,問候！
我等革命之首腦,奇普-瓜瓦（Cheep-Guava）,已領我等取得諸多輝煌大捷。
我等已從五個星系肅清保皇派叛徒！
```

**Rebuild v3 (clean-room)**:
```
問候你,來自地球的朋友!
我族革命的首腦——奇普-瓜瓦(Cheep-Guava)——已率領我族贏得無數大捷。
我族已把保皇派叛徒——從五個星系當中——清剿一空!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_HELLO_2=A` (繼承 shipped) / `REBEL_HELLO_2=B` (採用 v3) / `REBEL_HELLO_2=C自訂:...`

---

### #57 · `REBEL_HELLO_3` · 🟠 ORANGE · _sim=0.452; 文言助詞清除=7_

**英文原文**:
```
A greeting to ye, Captain!
We hope yer battles have been fierce and yer enemies are left in ruin.
Now what can we be doing fer ye?
```

**Shipped v0.6**:
```
向爾致意,艦長！
願爾之戰役激烈非凡,爾之敵人皆已成為廢墟。
如今我等能為爾效何等之勞？
```

**Rebuild v3 (clean-room)**:
```
向你問候,艦長!
我族期盼——你的戰役激烈,你的敵人只剩廢墟一片。
如今——我族能為你做些什麼呢?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_HELLO_3=A` (繼承 shipped) / `REBEL_HELLO_3=B` (採用 v3) / `REBEL_HELLO_3=C自訂:...`

---

### #58 · `REBEL_HELLO_4` · 🟠 ORANGE · _sim=0.389; 文言助詞清除=1_

**英文原文**:
```
Hello Captain. What are you needing from us this day?
```

**Shipped v0.6**:
```
艦長好。 今日爾有何所需於我等？
```

**Rebuild v3 (clean-room)**:
```
你好啊,艦長。今日你——需要我族做什麼?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_HELLO_4=A` (繼承 shipped) / `REBEL_HELLO_4=B` (採用 v3) / `REBEL_HELLO_4=C自訂:...`

---

### #59 · `how_goes_revolution` · 🟠 ORANGE · _sim=0.667_

**英文原文**:
```
How is the revolution going?
```

**Shipped v0.6**:
```
革命進展如何？
```

**Rebuild v3 (clean-room)**:
```
革命進行得如何?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `how_goes_revolution=A` (繼承 shipped) / `how_goes_revolution=B` (採用 v3) / `how_goes_revolution=C自訂:...`

---

### #60 · `REBEL_REVOLUTION_1` · 🟠 ORANGE · _sim=0.738_

**英文原文**:
```
We have cleaned the Royalist traitors from five systems
and even the Veep-Kreep Clan is joining with us against the false Queen!
```

**Shipped v0.6**:
```
我等已從五個星系肅清保皇派叛徒
連維普克利普氏族（Veep-Kreep Clan）都加入我等,共同對抗偽女皇！
```

**Rebuild v3 (clean-room)**:
```
我族已從五個星系——把保皇派叛徒清剿一空
甚至連維普克利普氏族(Veep-Kreep Clan)——也已加入我族,共抗**偽女皇**!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_REVOLUTION_1=A` (繼承 shipped) / `REBEL_REVOLUTION_1=B` (採用 v3) / `REBEL_REVOLUTION_1=C自訂:...`

---

### #61 · `REBEL_REVOLUTION_2` · 🟠 ORANGE · _sim=0.497; 文言助詞清除=2_

**英文原文**:
```
It is a sad thing, this battle that has pitched Clan against Clan, ship against ship
I myself have sent three Royalist Terminators and their brave crew to the Great Beyond!
What a waste.
We pray that the struggle ends quickly.
```

**Shipped v0.6**:
```
此乃悲哀之事,此戰役令氏族相殘、艦艇相搏
本騎士親手將三艘保皇派終結者與其英勇艦員送入蒼宇彼方！
何等浪費。
我等祈禱此掙扎速速終結。
```

**Rebuild v3 (clean-room)**:
```
可歎啊——這場戰事——氏族對氏族、星艦對星艦——已然打成這樣
本騎士親手,把三艘保皇派終結者及其英勇的船員——送往**蒼宇彼方**!
何等浪費啊。
我族祈願——這場鬥爭能早日結束。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_REVOLUTION_2=A` (繼承 shipped) / `REBEL_REVOLUTION_2=B` (採用 v3) / `REBEL_REVOLUTION_2=C自訂:...`

---

### #62 · `REBEL_REVOLUTION_3` · 🟠 ORANGE · _sim=0.495; 文言助詞清除=2_

**英文原文**:
```
Though we have taken grave losses -- lost brave and true shipmates
the enemy -- the fake Queen and her cronies,  have suffered far worse.
```

**Shipped v0.6**:
```
雖我等已蒙重大損失 —— 失去英勇忠貞之袍澤
而敵方 —— 那偽女皇與其黨羽,所受之苦遠甚於此。
```

**Rebuild v3 (clean-room)**:
```
雖然我族——蒙受了慘重損失——失去了無數英勇忠信的同袍——
但敵人——那**偽女皇**與她的黨羽——所受的重創,遠更慘烈。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_REVOLUTION_3=A` (繼承 shipped) / `REBEL_REVOLUTION_3=B` (採用 v3) / `REBEL_REVOLUTION_3=C自訂:...`

---

### #63 · `REBEL_REVOLUTION_4` · 🟠 ORANGE · _sim=0.667; 文言助詞清除=2_

**英文原文**:
```
Our victory is in sight, just beyond the next battle
or perhaps the next.
```

**Shipped v0.6**:
```
我等之勝利已在眼前,就在下一場戰役之後
又或許,下下一場。
```

**Rebuild v3 (clean-room)**:
```
我族的勝利——已在望——就在下一場戰役過後
或者——下下一場。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `REBEL_REVOLUTION_4=A` (繼承 shipped) / `REBEL_REVOLUTION_4=B` (採用 v3) / `REBEL_REVOLUTION_4=C自訂:...`

---

### #64 · `any_ships` · 🟠 ORANGE · _sim=0.571; 文言助詞清除=1_

**英文原文**:
```
Do you have any ships available to join our fleet?
```

**Shipped v0.6**:
```
你們有可加入我方艦隊之艦艇嗎？
```

**Rebuild v3 (clean-room)**:
```
你們有沒有多的戰艦——可以加入我方艦隊?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `any_ships=A` (繼承 shipped) / `any_ships=B` (採用 v3) / `any_ships=C自訂:...`

---

### #65 · `NO_ROOM` · 🟠 ORANGE · _sim=0.557; 文言助詞清除=1_

**英文原文**:
```
The question is moot, is it not, since ye have no room fer such ships in yer fleet?
```

**Shipped v0.6**:
```
此問無意義,不是嗎,既然爾艦隊已無空位容納此等艦艇？
```

**Rebuild v3 (clean-room)**:
```
這問題已無意義——不是嗎——既然你艦隊裡——已無空間再容納這樣的戰艦?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `NO_ROOM=A` (繼承 shipped) / `NO_ROOM=B` (採用 v3) / `NO_ROOM=C自訂:...`

---

### #66 · `HAVE_ALL_SHIPS` · 🟠 ORANGE · _sim=0.361; 文言助詞清除=3_

**英文原文**:
```
We are honored to help ye, Captain!
We shall attach four Terminators to yer fleet immediately.
```

**Shipped v0.6**:
```
我等能助爾實乃榮幸,艦長！
我等即刻將四艘終結者附於爾艦隊。
```

**Rebuild v3 (clean-room)**:
```
艦長——能相助你一臂,實為我族的榮耀!
我族將立刻——把四艘終結者——編入你的艦隊。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HAVE_ALL_SHIPS=A` (繼承 shipped) / `HAVE_ALL_SHIPS=B` (採用 v3) / `HAVE_ALL_SHIPS=C自訂:...`

---

### #67 · `HAVE_FEW_SHIPS` · 🟠 ORANGE · _sim=0.397; 文言助詞清除=7_

**英文原文**:
```
We are happy assisting ye, Captain.
We shall provide ye with enough of our Terminator vessels to complete yer fleet.
Fight well with them, Captain. They are our best and brightest.
```

**Shipped v0.6**:
```
能助爾我等甚感欣喜,艦長。
我等將提供爾足夠之終結者艦艇,使爾艦隊圓滿。
善用之而戰,艦長。 它們乃我等之精銳。
```

**Rebuild v3 (clean-room)**:
```
艦長——援助你,我族甚為歡喜。
我族將提供你——足量的終結者戰艦,把你的艦隊補齊。
艦長,好好善用他們作戰。他們是我族最優秀、最卓越的戰士。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HAVE_FEW_SHIPS=A` (繼承 shipped) / `HAVE_FEW_SHIPS=B` (採用 v3) / `HAVE_FEW_SHIPS=C自訂:...`

---

### #68 · `NO_SHIPS_YET` · 🟠 ORANGE · _sim=0.367; 文言助詞清除=4_

**英文原文**:
```
Alas, as yet we have no ships which we can be making available to ye at this time.
However, if ye return at a later date, perhaps then we shall have something fer ye.
```

**Shipped v0.6**:
```
唉,目前我等尚無可撥予爾之艦艇。
然而,爾若日後再返,或許屆時我等便有物可贈爾。
```

**Rebuild v3 (clean-room)**:
```
唉——很遺憾,眼下我族——尚無戰艦——可以提供給你。
不過,倘若你日後再度歸來——屆時我族或許——就有些東西給你了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `NO_SHIPS_YET=A` (繼承 shipped) / `NO_SHIPS_YET=B` (採用 v3) / `NO_SHIPS_YET=C自訂:...`

---

### #69 · `what_about_royalty` · 🟠 ORANGE · _sim=0.345; 文言助詞清除=1_

**英文原文**:
```
Can you tell me about your Royal Family?
```

**Shipped v0.6**:
```
能否告訴我方你們的王室之事？
```

**Rebuild v3 (clean-room)**:
```
你們能否——說一說你們的皇族?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_royalty=A` (繼承 shipped) / `what_about_royalty=B` (採用 v3) / `what_about_royalty=C自訂:...`

---

### #70 · `ABOUT_ROYALTY` · 🟠 ORANGE · _sim=0.322; 文言助詞清除=21_

**英文原文**:
```
The FALSE Royals, ye should say, Captain!
To understand our relationship with the Veep-Neep Queens, ye must first learn a bit of our history.
In the ancient past, we Yehat were little more than a collection of warring Clans.
That history is bloody, Captain... hideous. We were barbarous then, aye... murderers all.
Many great warlords rose from the hills and forests of our verdant homeworld to unite the clans
to become King of all Yehat Clans. Each one failed.
It was no male who finally won the great prize, the High Perch of Caer Zeep-Reep!
No, Captain, it was a female!... a wise and powerful Queen... the first of the Veep-Neep Dynasty.
In exchange fer the Clans' fealty, she gave a simple, compelling promise.
She guaranteed that united under her wing, the Clans would NEVER suffer defeat!
And she kept her promise. At long last, there was peace on our world.
Her line kept true to this promise fer over twenty centuries
soothing ruffled feathers, dispensing justice, stamping out foment
but then came the present Queen... a true harridan!
Under her rule, the power of the Starship Clans was transferred
to the sycophantic Homeworld dandies... to `warlords' who had nae seen true combat.
We, the beak and claw of the Yehat Empire were powerless to influence her decisions.
When the Queen showed the true colors of her plumage and allied with the evil Ur-Quan worms
we realized that she would do anything, ANYTHING!...
...to maintain the illusion of upholding her ancestor's promise
even if it meant destroying our honor, everything that we stand fer, in the exchange.
Now we, the true Yehat Clans, seek to pull the false Queen from the High Perch.
Perhaps we will find a new Queen someday who will bring together the Clans once more.
Or sadly, I fear we may never replace the Veep-Neeps Queens
and we shall fight Clan against Clan until only the bloody feathers remain.
```

**Shipped v0.6**:
```
應說「偽」王室,艦長！
欲了解我等與維普涅普女皇之關係,爾須先知一點我族歷史。
遠古之時,我等翼哈特族不過是一群相爭之氏族。
那段歷史血腥,艦長…可怖。 我等當時野蠻,是啊…盡是殺戮者。
多少偉大戰陣統領自我族蒼綠母星之丘陵與森林崛起,欲統一諸氏族
成為所有翼哈特氏族之王。 各個皆敗。
最終贏得那大彩、那齊普瑞普堡（Caer Zeep-Reep）之女王高棲者,並非雄性！
不,艦長,乃一位雌性！…一位睿智強大之女皇…維普涅普王朝之首任。
以換取諸氏族之效忠,她給了一個簡單而動人之承諾。
她保證,團結於她羽翼之下,諸氏族將絕不會遭受敗績！
她亦履行承諾。 終於,我族之世界迎來了和平。
她的血脈忠實守此承諾兩千餘年
撫平氣憤羽翎、施行公義、平息騷動
然而如今這一任女皇…真是一個十足的潑婦！
在她統治下,星艦氏族之權柄被移轉
給那些諂媚的母星紈褲子弟…給那些未見過真正戰陣之「戰陣統領」。
我等,身為翼哈特帝國之喙與爪,竟無力左右她之決策。
當那女皇露出真正之羽色,與那邪惡烏寬蟲蟻結盟時
我等方明白她會為此不擇手段,無所不為！…
…只為維持履行祖先承諾之假象
哪怕以毀我等之榮譽、我等所堅守之一切為代價交換。
如今我等,真正的翼哈特氏族,誓將偽女皇自女王高棲拉下。
或許有朝一日,我等能覓得新女皇,再一次將諸氏族凝聚為一。
或悲哀地,本騎士恐我等永難有物替代維普涅普女皇
而我等將氏族相殘,直至只餘血染羽翎。
```

**Rebuild v3 (clean-room)**:
```
艦長,你應該說是**偽王室**才對!
要理解我族與維普涅普王朝的糾葛,你必先了解——我族的一段歷史。
遠古年代,我族翼哈特——不過是一群相互攻伐的氏族聚合罷了。
那段歷史——血腥不堪,艦長……醜陋不已。當時我族還是野蠻的——沒錯,人人皆是屠夫。
數以百計的偉大戰主——從我族翠綠母星的丘陵與森林中——崛起而出,妄圖統一眾氏族——
——登上翼哈特眾氏族的王位。每一位——都失敗了。
最終,贏得那份大獎——凱爾茲皮里普高懸王座——的,並非一位雄鳥!
不,艦長——竟是一位雌鳥!……一位智慧超群、力量非凡的女皇……維普涅普王朝的第一任。
作為眾氏族效忠的交換,她給出了一個簡潔而有力的承諾。
她保證——只要聚合於她的雙翼下——眾氏族將**永不**嚐到戰敗的滋味!
而她也守住了這個諾言。終於——我族的世界迎來了和平。
她的血脈——秉持這份承諾——已逾二十世紀
撫平羽毛間的爭端、施行正義、根除禍端
但——如今這位女皇——是個**十足的潑婦**!
在她統治下,星艦氏族的力量——被轉移到
那些諂媚的母星紈絝子弟身上——那些從未見識過真正戰陣的所謂「戰主」。
我族——翼哈特帝國的喙與爪——竟無力左右她的決定。
當女皇露出羽毛下的真面目、與那邪惡的烏寬蠕蟲結盟時
我族才驚覺——她會做**任何事**,**任何事**!……
……只為維持一個假象——好像她仍在守著她祖先的承諾
即使代價是——毀滅我族的榮耀、毀滅我族所堅持的一切——她也在所不惜。
如今——我族——真正的翼哈特氏族——要把偽女皇從高懸王座上——扯下!
或許——他日我族將尋得一位新女皇——再度把眾氏族凝聚在一起。
又或者——可歎地——我族或許永遠找不到人來取代維普涅普王朝
——而我族只能——氏族對氏族——鬥到只剩血染的羽毛為止。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ABOUT_ROYALTY=A` (繼承 shipped) / `ABOUT_ROYALTY=B` (採用 v3) / `ABOUT_ROYALTY=C自訂:...`

---

### #71 · `what_about_war` · 🟠 ORANGE · _sim=0.476; 文言助詞清除=1_

**英文原文**:
```
Tell me about the end of the War.
```

**Shipped v0.6**:
```
說說戰爭之末的事。
```

**Rebuild v3 (clean-room)**:
```
說說——那場大戰的結局。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_war=A` (繼承 shipped) / `what_about_war=B` (採用 v3) / `what_about_war=C自訂:...`

---

### #72 · `ABOUT_WAR` · 🟠 ORANGE · _sim=0.51; 文言助詞清除=21_

**英文原文**:
```
I will describe these events, Captain.
They make fer a tale, Captain, wrought with sadness... and heroism!... and betrayal.
After the Chenjesu, Mmrnmhrm and yer species were defeated
We prepared a defense in the Shofixti homestar, <% comm.getStarName("Delta Gorno", "shofixti") %>.
Aside our Shofixti, our adopted children, we awaited the onslaught of the Ur-Quan armada.
We waited with eagerness, with the hot anticipation of battle!
But then we received an unbelievable message from our Queen... `Retreat'.
We could not believe it! Tactical withdrawals, yes... but to pull back the entire fleet?
There was no mistake... no garbled orders.
We obeyed.
Oh, Captain! The eyes of the Shofixti! Their bright and valiant eyes!... as we moved away.
Without us... they had no hope of forming a tactical wedge.
They would barely slow the Hierarchy fleet.
When the Ur-Quan came, the Shofixti fought as immortal heroes!...
darting in and out of the Dreadnought formations
and then suddenly BLAZING!... like dying stars.
But... in only a few hours... the Shofixti fleet was gone
and the Dreadnoughts moved towards the homeworld.
```

**Shipped v0.6**:
```
本騎士將為爾道盡此等事件,艦長。
此故事,艦長,交織著哀傷…與英雄氣概！…與背叛。
晶智族、姆姆族與爾族被擊敗之後
我等於修烈士族之母星 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno）備戰防禦。
在我等之側乃我等收養之子,修烈士族,共同等候烏寬艦隊之猛攻。
我等熱切等候,懷著戰意之熾熱期盼！
卻於此時我等收到來自女皇之難以置信之訊…「撤退」。
我等無法相信！ 戰術性後撤,可以…但令整支艦隊撤回？
並無錯誤…並非誤傳之命。
我等遵命了。
啊,艦長！ 修烈士族之眼！ 那明亮而勇敢之眼！…當我等撤離之際。
無我等之助…他們已無形成戰術楔形之望。
他們幾乎無力阻延階層艦隊。
烏寬到來之時,修烈士族如不朽英雄般奮戰！…
穿梭於無畏艦編隊之間
然後突然烈焰爆燃！…如垂死之星。
然而…僅數小時之內…修烈士族艦隊便已無存
而無畏艦紛紛朝其母星進發。
```

**Rebuild v3 (clean-room)**:
```
艦長,本騎士將為你描述這一切經過。
艦長——這是一則故事——編織著哀傷……英勇!……與背叛。
在晶智族、姆姆族與你們一族相繼戰敗後
我族——在修烈士族的母星 <% comm.getStarName("戈爾諾δ", "shofixti") %>（Delta Gorno） 佈下了防禦陣勢。
與我族的修烈士族——我族收養的子輩——並肩,等候烏寬艦隊的襲擊。
我族滿懷熱切等候——期盼著戰鬥的熾熱期待!
但那時——我族收到了女皇陛下——一道令我族無法置信的旨令……「撤退」。
我族無法相信!戰術性撤離——當然可以……但——把整支艦隊——都撤走?
並非誤傳……並非亂碼的旨令。
我族——遵命了。
啊,艦長!修烈士族那些眼睛!那些明亮而英勇的眼睛!……當我族——正撤離而去時。
沒有我族撐腰……他們就無法形成戰術楔形陣。
他們——連拖慢階層艦隊的速度都做不到。
當烏寬到來,修烈士族——奮戰如不朽的英雄!……
——在無畏艦編隊間穿梭進出——
——然後突然**熊熊烈焰**綻放!……像瀕死的恆星。
但……僅僅幾小時後……修烈士族艦隊——已然全滅
而無畏艦隊——朝著修烈士母星——推進而去。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ABOUT_WAR=A` (繼承 shipped) / `ABOUT_WAR=B` (採用 v3) / `ABOUT_WAR=C自訂:...`

---

### #73 · `what_about_urquan` · 🟠 ORANGE · _sim=0.56_

**英文原文**:
```
How were the Shofixti defeated?
```

**Shipped v0.6**:
```
修烈士族是如何被擊敗的？
```

**Rebuild v3 (clean-room)**:
```
修烈士族——是怎麼戰敗的?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_urquan=A` (繼承 shipped) / `what_about_urquan=B` (採用 v3) / `what_about_urquan=C自訂:...`

---

### #74 · `ABOUT_URQUAN` · 🟠 ORANGE · _sim=0.558; 文言助詞清除=11_

**英文原文**:
```
As we abandoned the Shofixti to the oncoming Ur-Quan armada
we watched the situation on the sterile displays of our long-range sensors.
Suddenly the screens flared and went black... burnt out! We ran to the windows
just in time to see the Shofixti's sun burning with incredible light
many orders of magnitude greater than its normal brilliance!
A million tongues of fusion fire spread through the star system
devastating the inner system's planets, but incinerating ALL the Ur-Quan vessels!
In that moment, the Hierarchy's war fleet was reduced by almost thirty percent.
We later remembered that not too many years before the appearance of the Ur-Quan
the Shofixti had told us that they had found `something'.
With the pride of a hatchling's first flight, they unveiled their find
it was about the size of a surface transport, but cylindrical and entirely black.
Across its surface were a million characters scrawled in an alien script.
The message was clear... DANGER! DO NOT TOUCH!
We trusted the Shofixti to respect the warning, and left the device in their possession.
At the end, when the Ur-Quan were approaching their planet
the Shofixti must have realized that they could not win
but at least they could insure that both sides would lose.
They must have detonated the device in the outer layer of their sun.
The sudden removal of a section of the sun's surface layers
allowed the pressurized plasma from the interior to burst out
like a miniature super nova.
```

**Shipped v0.6**:
```
當我等將修烈士族棄置於逼近之烏寬艦隊面前時
我等於長程感應器之冷冷螢幕上觀察局勢。
忽然螢幕炫光一閃便一片漆黑…燒毀了！ 我等奔向舷窗
恰好見修烈士族之太陽以難以置信之光焰燃燒
其亮度較平時高出數個數量級！
數以百萬計之融合火舌蔓延過整個星系
毀滅內側行星,卻焚盡了「所有」烏寬艦艇！
那一瞬,階層之戰爭艦隊減少了近三成。
我等後來憶起,烏寬出現前不算太久
修烈士族曾告我等,他們找到「某物」。
以雛鳥處女航之驕傲,他們揭曉其發現
那物大小約如地面運輸艇,卻是圓柱形且通體漆黑。
其表面以外星文字刻著數百萬個字符。
訊息一目瞭然…「危險！ 勿觸！」
我等相信修烈士族會敬重此警告,便將該裝置留予他們持有。
最終,烏寬逼近其行星之時
修烈士族必已察覺他們無法取勝
但至少他們能確保雙方皆敗。
他們必是將該裝置引爆於其太陽之外層。
太陽表面層一段之瞬間剝離
使內部加壓之電漿爆湧而出
如一顆微型超新星。
```

**Rebuild v3 (clean-room)**:
```
當我族——把修烈士族拋給那正襲來的烏寬艦隊——
我族在遠程感測器那冰冷的顯示屏上——看著整個局勢。
突然——屏幕閃了一下,便黑了……燒毀了!我族衝向舷窗——
恰好看見——修烈士族的太陽——正以難以置信的光焰燃燒
——比其平時的光輝——強上不知多少個數量級!
上百萬條核融烈焰——在整個星系間蔓延
——蕩平了內圈行星,卻也把**所有**烏寬戰艦——全數焚為灰燼!
就在那一刻,階層的戰爭艦隊——被削減了將近三成。
我族後來回憶起——就在烏寬出現前——為時不算太久
修烈士族曾告訴我族——他們發現了「某個東西」。
帶著初雛第一次飛行的驕傲——他們揭開了那項發現
——那東西大約有地表運輸艇那般大——卻是圓柱形、通體漆黑。
其表面上,刻著上百萬個異形文字。
訊息明白無誤……**危險!請勿觸碰!**
我族信任修烈士族會尊重這一警告,便把那件裝置——留在他們手上。
到了最後——當烏寬軍勢逼近修烈士族母星
修烈士族——必定已明白——他們無法取勝
——但至少,他們能保證——雙方——同歸於盡。
他們必定——把那件裝置——引爆於自己太陽的外層。
太陽表面某一區塊——突遭抽離
——讓內部那高壓的電漿——爆湧而出
——像一顆微型的超新星。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ABOUT_URQUAN=A` (繼承 shipped) / `ABOUT_URQUAN=B` (採用 v3) / `ABOUT_URQUAN=C自訂:...`

---

### #75 · `what_about_vux` · 🟠 ORANGE · _sim=0.645_

**英文原文**:
```
Do you know anything about the VUX?
```

**Shipped v0.6**:
```
關於 VUX 你知道些什麼？
```

**Rebuild v3 (clean-room)**:
```
你們——對 VUX 知道些什麼嗎?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_vux=A` (繼承 shipped) / `what_about_vux=B` (採用 v3) / `what_about_vux=C自訂:...`

---

### #76 · `ABOUT_VUX` · 🟠 ORANGE · _sim=0.615; 文言助詞清除=8_

**英文原文**:
```
The grotesque monsters? They are an effete and bigoted race, unworthy prey
with one exception... General ZEX.
He commanded the entire VUX fleet during the Great War
and even by our high standards of battle skill, he is a genius.
The brilliant tactics of Fortress Square and the Dynamic Triangle are his creations.
Without ZEX, the VUX would have fallen to our Alliance fleets in weeks
but ZEX always found a way to turn his own weakness into an advantage.
After the War, we learned that the Primat and the VUX High Council
decided to move ZEX out of the picture, and sent him off to `luxurious retirement' at <% comm.getStarName("Alpha Cerenkov", "maidens") %> I.
We have heard that he spends his time pursuing his hobby, though we do not know what more than that.
```

**Shipped v0.6**:
```
那群怪誕之魔物？ 他們乃一個柔弱而偏執之種族,不配為獵物
然,有一例外…澤克斯將軍（General ZEX）。
他於大戰期間指揮整支 VUX 艦隊
即使以我等之高戰技標準衡量,他亦是一位天才。
堡壘方陣（Fortress Square）與機動三角陣（Dynamic Triangle）之精妙戰術皆為其所創。
若無澤克斯,VUX 早在數週內便會潰於我等聯盟艦隊之下
然澤克斯總能將自身之弱轉化為優勢。
戰後,我等得知總議長（Primat）與 VUX 最高議會
決意將澤克斯自舞台移除,將他送往 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） I 號行星「豪華退休」。
聽聞他在該處消磨時光追求其嗜好,除此之外我等所知不多。
```

**Rebuild v3 (clean-room)**:
```
那些醜怪嗎?那是一支陰柔而偏執的種族——不值得獵殺——
——只有一個例外……澤克斯上將(General ZEX)。
大戰時期,他指揮整支 VUX 艦隊——
——即使按我族**極高**的戰技標準衡量,他仍是個天才。
**堡壘方陣**與**機動三角陣**——那些精妙戰術——都是他的創作。
若無澤克斯,VUX 早已在數週內——敗給我方聯盟艦隊
——但澤克斯總能找出方法——把自己的弱點——轉化為優勢。
大戰後,我族才得知——**總議長**(Primat)與 VUX 最高議會
——決意把澤克斯挪出局面——把他打發到 <% comm.getStarName("契倫科夫α", "maidens") %>（Alpha Cerenkov） 星系的一號行星——「豪華退休」。
我族聽說,他都在鑽研自己的嗜好——不過我族——並不知道那是什麼。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ABOUT_VUX=A` (繼承 shipped) / `ABOUT_VUX=B` (採用 v3) / `ABOUT_VUX=C自訂:...`

---

### #77 · `what_about_clue` · 🟠 ORANGE · _sim=0.667_

**英文原文**:
```
How can we defeat the Ur-Quan? 
```

**Shipped v0.6**:
```
我方要如何擊敗烏寬？
```

**Rebuild v3 (clean-room)**:
```
我方要如何——才能打敗烏寬?
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_clue=A` (繼承 shipped) / `what_about_clue=B` (採用 v3) / `what_about_clue=C自訂:...`

---

### #78 · `ABOUT_CLUE` · 🟠 ORANGE · _sim=0.442; 文言助詞清除=13_

**英文原文**:
```
If I were ye, brave human, I'd probably be seeking the focus of the Ur-Quan's power
and do whatever is necessary to destroy it.
We may have a hint as to just what that weak spot is.
When we were being Hierarchy battle slaves
we learned that the Ur-Quan were possessing some kind of super-weapon
a huge battleship they called `Sa-Matra' with the firepower to destroy an entire star fleet.
For some reason, the Ur-Quan were reluctant to use the vessel.
It wasn't until their armada was finally held back at the coreward front
that they brought the Sa-Matra's power to bear on the Alliance.
Captain, here's my advice... ye can be destroying Dreadnoughts until the breegs come home
but ye are never going to defeat the Ur-Quan Hierarchy until ye eliminate their Sa-Matra.
```

**Shipped v0.6**:
```
若本騎士為爾,勇敢之人類,本騎士大概會去尋找烏寬力量之核心焦點
並不擇手段將其毀滅。
我等或許對那弱點為何有所提示。
當我等身為階層之戰奴時
我等得知烏寬擁有某種超級武器
一艘他們稱之為「薩瑪特拉」（Sa-Matra）之巨大戰艦,其火力足以摧毀整支星艦隊。
因不知何故,烏寬對啟用該艦顯得躊躇。
直到他們之艦隊終於在銀核前線受阻時
他們才將薩瑪特拉之力量傾瀉於聯盟之上。
艦長,聽我一言…爾可以擊落無畏艦擊到布利格歸巢
然爾永難擊敗烏寬階層,除非爾將他們之薩瑪特拉摧毀。
```

**Rebuild v3 (clean-room)**:
```
勇敢的人類,若本騎士是你——大概會去尋找烏寬勢力的核心——
——然後,不計代價把它摧毀。
關於那個弱點——我族——或許——有一絲線索。
當我族——正被迫充當階層的戰奴時
——我族得知,烏寬手上握著某種超級武器——
——一艘巨大的戰艦——他們喚作**「薩瑪特拉」(Sa-Matra)**——擁有足以毀滅整支星際艦隊的火力。
不知為何,烏寬——一直不願動用這艘戰艦。
直到他們的艦隊——終於在星核前線被阻擋下來——
——他們才把薩瑪特拉的威力——傾瀉在聯盟身上。
艦長,本騎士的建議是……你可以持續擊沉無畏艦——直到布利格獸都回巢了為止——
——但只要不消滅那艘薩瑪特拉,你——就永遠無法擊敗烏寬階層。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `ABOUT_CLUE=A` (繼承 shipped) / `ABOUT_CLUE=B` (採用 v3) / `ABOUT_CLUE=C自訂:...`

---

### #79 · `enough_info` · 🟠 ORANGE · _sim=0.476_

**英文原文**:
```
That's sufficient information for now.
```

**Shipped v0.6**:
```
情報暫時夠用了。
```

**Rebuild v3 (clean-room)**:
```
目前——這樣的情報就夠了。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `enough_info=A` (繼承 shipped) / `enough_info=B` (採用 v3) / `enough_info=C自訂:...`

---

### #80 · `OK_ENOUGH_INFO` · 🟠 ORANGE · _sim=0.552_

**英文原文**:
```
If you need to know anything more, just ask.
```

**Shipped v0.6**:
```
若還需更多所知,只管開口。
```

**Rebuild v3 (clean-room)**:
```
你若還需要知道什麼——儘管開口。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `OK_ENOUGH_INFO=A` (繼承 shipped) / `OK_ENOUGH_INFO=B` (採用 v3) / `OK_ENOUGH_INFO=C自訂:...`

---

### #81 · `bye_rebel` · 🟠 ORANGE · _sim=0.491_

**英文原文**:
```
Goodbye brave rebels. Viva la Revolution!
```

**Shipped v0.6**:
```
再見了,勇敢的叛軍們。 革命萬歲！
```

**Rebuild v3 (clean-room)**:
```
再會了,勇敢的叛軍。革命萬歲!(Viva la Revolution!)
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `bye_rebel=A` (繼承 shipped) / `bye_rebel=B` (採用 v3) / `bye_rebel=C自訂:...`

---

### #82 · `GOODBYE_REBEL` · 🟠 ORANGE · _sim=0.6_

**英文原文**:
```
Goodbye human comrade. Fight well!
```

**Shipped v0.6**:
```
再見了,人類同志。 善戰而歸！
```

**Rebuild v3 (clean-room)**:
```
再會了,人類的同志。奮戰無悔!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `GOODBYE_REBEL=A` (繼承 shipped) / `GOODBYE_REBEL=B` (採用 v3) / `GOODBYE_REBEL=C自訂:...`

---

### #83 · `YEHAT_CAVALRY` · 🟠 ORANGE · _sim=0.467; 文言助詞清除=8_

**英文原文**:
```
Greetings human friend! We know ye are about to be attacking the Sa-Matra
and probably don't like being interrupted, but we have important news!...
The Rebellion is WON! We are VICTORIOUS!
We have pulled the Veep-Neep harpy Queen and her cronies from the High Perch!
And better yet... we have found a new Queen!...
...A Queen who will unite the Clans in peace and harmony as never before!
You will never guess who it is, Captain!
A PKUNK! Yes! It is TRUE!
They survived their absorption into our culture
and are now providing us with insights into ourselves we never dreamed of!
We only THOUGHT we were being happy birds of prey! We were fooling ourselves!
Our new Queen's name is Braky Girdy the First!... and her first command
was to rush here and bring ye these ships...Yehat Terminators and Pkunk Furies.
Now, Captain, together we can attack the Sa-Matra!
```

**Shipped v0.6**:
```
問候,人類友人！ 我等知爾正欲攻擊薩瑪特拉
此時多半不願被打斷,然我等有重大消息！…
叛變勝利了！ 我等大勝！
我等已將維普涅普鷹身女妖女皇（harpy Queen）與其黨羽自女王高棲拉下！
更妙的是…我等已覓得新女皇！…
…一位將以前所未有之和平與和諧凝聚諸氏族之女皇！
爾絕料想不到她是誰,艦長！
一位普恩族！ 是的！ 此事屬實！
他們挺過了融入我族文化之過程
而今正提供我等連做夢也不曾想過之自省洞見！
我等從前只「以為」自己是快樂之猛禽！ 我等實在是自欺欺人！
我等新女皇名為布拉基·葛迪一世（Braky Girdy the First）！…她的首道諭令
便是急馳至此,為爾帶來這些艦艇…翼哈特終結者與普恩烈憤艦（Pkunk Fury）。
如今,艦長,我等可共同攻擊薩瑪特拉了！
```

**Rebuild v3 (clean-room)**:
```
問候你,人類朋友!我族知道——你正打算攻擊薩瑪特拉——
——大概不喜歡被打斷,但我族有**重要消息**!……
**革命——勝利了!**我族——**取得勝利!**
我族已把維普涅普那**鷹身女妖女皇(harpy Queen)**——與她的黨羽——從高懸王座上——扯下!
還有更妙的……**我族——找到了一位新女皇!**……
……一位將把眾氏族——凝聚在和平與和諧當中——**前所未有**的女皇!
艦長,你**絕對**猜不到她是誰!
是**一位普恩族!**沒錯!這是**真的!**
他們——當年被吸收進我族文化裡——竟然存活下來
——而如今,正把——我族——從未夢想過的自我洞察——傳遞給我族!
我族——本來**以為**——自己是快樂的猛禽!其實我族——是在自欺欺人!
我族新任女皇的名字是——**布拉基·葛迪一世**(Braky Girdy the First)!……而她的第一道旨令
——就是趕來這裡——把這些戰艦——送到你手上……翼哈特終結者,以及普恩烈憤艦(Pkunk Fury)。
如今,艦長——**你我攜手——一同攻擊薩瑪特拉!**
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `YEHAT_CAVALRY=A` (繼承 shipped) / `YEHAT_CAVALRY=B` (採用 v3) / `YEHAT_CAVALRY=C自訂:...`

---

### #84 · `what_about_pkunk_rebel` · 🟠 ORANGE · _sim=0.642_

**英文原文**:
```
We have encountered an offshoot of your species, the Pkunk. Tell us about them.
```

**Shipped v0.6**:
```
我方遇到你們的一個分支族群,普恩族。 說說他們吧。
```

**Rebuild v3 (clean-room)**:
```
我方遇到了你們翼哈特的分支——普恩族。跟我方談談他們吧。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `what_about_pkunk_rebel=A` (繼承 shipped) / `what_about_pkunk_rebel=B` (採用 v3) / `what_about_pkunk_rebel=C自訂:...`

---

### #85 · `PKUNK_ABSORBED_REBEL` · 🟠 ORANGE · _sim=0.667_

**英文原文**:
```
The Pkunk have been absorbed.
They are no more. This is how it should be.
Now the matter is settled, human. Do not be bringing it up again.
```

**Shipped v0.6**:
```
普恩族已被吸收。
他們不復存在。 理當如此。
此事已了,人類。 莫要再提起。
```

**Rebuild v3 (clean-room)**:
```
普恩族早已被吸收殆盡。
他們早已不復存在。這正是本該有的結局。
此事已定,人類。**別再提起**。
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `PKUNK_ABSORBED_REBEL=A` (繼承 shipped) / `PKUNK_ABSORBED_REBEL=B` (採用 v3) / `PKUNK_ABSORBED_REBEL=C自訂:...`

---

### #86 · `HATE_PKUNK_REBEL` · 🟠 ORANGE · _sim=0.472; 文言助詞清除=6_

**英文原文**:
```
The cowards live?!! This is unbelievable!!
It is a SAD, SAD day to be hearing this thing from ye, human.
The P... the Pku... I canna even say their vile name!
The Pku... PKU-NK! are the greatest embarrassment our species has ever suffered!
Do not be calling these wretched creatures an offshoot of our species!
Better it is that ye be calling them GARBAGE! or DROPPINGS!
Or better yet do not be talking about them at all!
```

**Shipped v0.6**:
```
那些懦夫還活著？！！ 難以置信！！
此乃悲哀,悲哀之日,竟從爾口中聽到此事,人類。
那普…那普恩…本騎士連他們卑劣之名都難以啟齒！
那普…普——恩——族！ 是我族有史以來最大之恥辱！
莫要把那些卑鄙生物稱為我族之分支！
寧可稱他們為垃圾！或糞便！
或者最好完全別提他們！
```

**Rebuild v3 (clean-room)**:
```
那些懦夫還活著?!!簡直難以置信!!
人類,從你口中聽到此事——今日真是**沉痛萬分**的一天!
那……那個普……普恩——本騎士連他們污穢的名字都說不出口!
那個普……**普恩!**是我族物種有史以來蒙受過**最深**的羞辱!
別把那些卑劣生物,稱作我族的分支!
你若非要稱呼他們,該叫他們**垃圾**或**糞便**才對!
甚至——**你根本就別再提起他們**才好!
```

**推薦**: B · v3 已對齊 v0.7 dossier(白話 + 鳥鳴 icon + 「本」字集體感);shipped 為 v0.6 文言污染

**你的選擇**: `HATE_PKUNK_REBEL=A` (繼承 shipped) / `HATE_PKUNK_REBEL=B` (採用 v3) / `HATE_PKUNK_REBEL=C自訂:...`

---


## 🟡 微調 (等價) · 7 tokens

> 主要是短玩家 response 或短 NPC 回應。v3 與 shipped 語意等價,選字略異。
> 建議: **🟡 全 B (採用 v3)** 以維持整體 voice 一致性。

| # | Token | Emoji | Sim | Shipped 前 35 字 | v3 前 35 字 | 推薦 |
|---:|---|:---:|---:|---|---|:---:|
| #1 | `i_demand_you_ally_homeworld` | 🟡 | sim=0.919 | `我，<% state.sis.getCaptainName() %>，...` | `我,<% state.sis.getCaptainName() %>,...` | B |
| #2 | `bye_homeworld` | 🟡 | sim=0.776 | `你們讓我方失望。 我方原本對你們期望更高。 再見。...` | `你們令我方失望了。我方原本對你們期待更多。再會。...` | B |
| #3 | `whats_up_space_4` | 🟡 | sim=0.88 | `你們不就是烏寬族的奴隸嗎？...` | `你們不就是烏寬的奴隸嗎?...` | B |
| #4 | `obligation` | 🟡 | sim=0.781 | `你們一族的義務豈能就這樣被遺忘？ 你們的榮譽、你們的驕傲呢？！...` | `你們一族的義務,豈能就這樣被遺忘!?你們的榮耀呢,你們的驕傲呢!?...` | B |
| #5 | `bye_space` | 🟡 | sim=0.778 | `再見，翼哈特族… 我方的盟友與朋友。...` | `再會了,翼哈特……我方的盟友與朋友。...` | B |
| #6 | `not_send` | 🟡 | sim=0.765 | `我不會讓我的軍官陷入這樣的險境。 我怎麼知道你們不會直接殺了他？...` | `我方不會讓自己麾下的軍官陷入這種險境。我方怎麼知道你們不會直接把他殺了...` | B |
| #7 | `give_info_rebels` | 🟡 | sim=0.769 | `願與我方分享一些情報嗎？...` | `你們能與我方分享一些情報嗎?...` | B |


## 🟢 完全相同 · 3 tokens

| Token | 說明 |
|---|---|
| `name_1` | v3 與 shipped 逐字相同 (通常為短玩家 response 或 name_* alliance 名 canonical) |
| `name_2` | v3 與 shipped 逐字相同 (通常為短玩家 response 或 name_* alliance 名 canonical) |
| `name_4` | v3 與 shipped 逐字相同 (通常為短玩家 response 或 name_* alliance 名 canonical) |


## 使用者決策接口

回覆格式:
```
🟢 全 A · 🟡 全 B · 🟠 全 B (推薦) · 🔴 逐項挑 · ✨ N/A
```
或個別:
```
#(token1)=A #(token2)=B #(token3)=C(細節: 前半 shipped + 後半 v3)
```

合併決策後,執行:
```powershell
# 備份 shipped
Copy-Item translations/yehat.zh-TW.json translations/yehat.zh-TW.pre-rebuild.bak
Copy-Item translations/yehatrebels.zh-TW.json translations/yehatrebels.zh-TW.pre-rebuild.bak
# Apply merged decisions (待使用者回覆後產生 _apply_yehat_decisions.py)
# Build + package
./build_zh-TW.ps1  # 觸發 Step 0 purity + Lua gate
./package_zh-TW.ps1
```