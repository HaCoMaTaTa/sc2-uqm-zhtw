# Syreen Rebuild-Compare Diff Report (2026-08-17)

**Rebuild-Compare workflow**: `StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md`  
**v3 clean-room 翻譯**: `translations/syreen.zh-TW.v3.json` (127 tokens · 依 v0.7 dossier §四 + 使用者 Q1-Q12 決策)  
**shipped**: `translations/syreen.zh-TW.json` (127 tokens · v0.5.2 · 2026-08-13)  
**Read-Aloud self-fix (階段 2.5)**: 1/127 (0.8%) · log: `_selfaudit_syreen_v3_readaloud.md` (HORRIBLE_TRUTH 完全一模一樣 → 一模一樣)  
**3-gate verify PASS**: purity 0 / Lua 0 / line-count 127/127  

## Q&A 決策快照

| Q# | 主題 | 選項 | 備註 |
|---|---|---|---|
| Q1 | 您/你 policy | **B** | Mode-based · Mode 1 官方=您 · Mode 2/3/4=你 |
| Q2 | Syra/Gaia 譯法 | **C** | 首介英文 gloss + 中譯 |
| Q3 | Sweet Cakes | **A** | 小甜心（Sweet Cakes） 首介 |
| Q4 | COWABUNGA | **C** | 卡哇邦嘎（COWABUNGA!）· 保留台灣忍者龜 gag |
| Q5 | Habitat | **B** | 棲居艦（shipped canonical） |
| Q6 | Space Patrol | **C** | 星際巡邏隊（Space Patrol）· 首介 gloss |
| Q7 | Starbase Commander | **B** | 星際基地指揮官（shipped canonical · Master_Glossary L280） |
| Q8 | Master Nine | **A** | 烏寬主宰九號（對齊 v3 Ur-Quan 主宰） |
| Q9 | palette | **C** | 混合 · 保留我族/我方/咱倆 · 廢除我等姐妹→我們姐妹 |
| Q10 | Mode 4 CAPS | **A** | 全中譯拖音（**用戶 override 我推薦 C**）· 為什——麼 + 呃嗚嗷嗷嗷 |
| Q11 | Touch-o-Vision | **C** | 觸感視（Touch-o-Vision）· 首介 gloss |
| Q12 | 分批 | **A** | 3 partials × ~42 |

## 統計

| 類別 | 數量 | 佔比 | 預設推薦 |
|---|---|---|---|
| 🟢 完全相同 | 12 | 9% | — |
| ✨ v0.7 canonical 升級 | 13 | 10% | **B (v3)** |
| 🔴 語意/voice icon 大 | 5 | 4% | **B (v3)** |
| 🟠 Mode-shift 您→你 + 文言清除 | 27 | 21% | **B (v3)** |
| 🟡 措辭/palette 微調 | 70 | 55% | **B (v3)** |
| **合計** | **127** | 100% | |

**清除 shipped 文言污染統計**：爾 1 → 0 · 之 25 (grammatical 之前/之後/之一/深淵之子 canonical 保留 · 廢除 shipped 之於/之友屬格) · 此等 3 → 0（此等能力→這種能力 / 此等力量→這種力量 / 此等威脅→這種威脅）

**新增招牌詞（canonical debut）**：**小甜心（Sweet Cakes）** · **卡哇邦嘎（COWABUNGA!）**  · **烏寬主宰九號（Ur-Quan Master Nine）** · **星際巡邏隊（Space Patrol）** · **穿透艦（Penetrator）** · **棲居艦三十一號（Habitat Thirty-One）** · **黛安妮（Diani）** · **雷奈特（Raynet）** · **道德警察（Ethics Police）** · **依瑪（Yma）** · **觸感視（Touch-o-Vision）** · **深淵之子（Deep Children）** 首介 gloss · **超波（HyperWave）** · **光之矛（Spears of Light）** · **歐加農（Organon）** · **時鐘座（Horologii）**  

**Mode 4 招牌 icon 全採用 (Q10=A)**：`為什——麼——艦——長！` · `你怎——麼——會——這麼——說呢——！！！` · `呃嗚嗷嗷嗷！！！！` · `必將為他們的罪行付出慘痛代價！！！` · `正義屬於我們！` · `心中燃起熊熊的怒火！`

**快答格式建議**：使用者若全依推薦 → `全 B` 適用所有 115 個 diff 項（27🟠 + 70🟡 + 13✨ + 5🔴）。若有異議 → 逐項標 `#N=A/C`。

---

## A · 🟢 完全相同 (12 tokens · 無需決策)

這些 tokens shipped 與 v3 一字不差，通常是簡短 player line 或格式固定的 Mode 1 客套語：

- `HELLO_BEFORE_AMBUSH_4`
- `we_are_vindicator`
- `SEE_PROOF`
- `what_happened`
- `GOODBYE`
- `bye_after_vault`
- `bye_after_ambush`
- `GOODBYE_AFTER_AMBUSH`
- `FOUND_VAULT_YET_1`
- `GOODBYE_BEFORE_VAULT`
- `bye_before_ambush`
- `JUST_RELAX`

---

## B · ✨ v0.7 Canonical 升級 (13 tokens · 首介英文 gloss / canonical rename)

**規則**：Q2=C（Syra/Gaia）+ Q3=A（Sweet Cakes）+ Q4=C（COWABUNGA 保留台灣 gag + gloss）+ Q6=C（Space Patrol gloss）+ Q8=A（Master Nine 主宰化）+ Q11=C（Touch-o-Vision gloss）+ 其他 canonical 補完首介英文 gloss。**預設 B (v3)**。

### B#1 · `HELLO_BEFORE_AMBUSH_1` · ✨ 首介 gloss「蓋亞（Gaia）」+ 廢除 shipped「爾艦」+「歸類為獨立艦艇」貼原文

**英文原文**:
> Attention unidentified space vessel!
> Be warned! This slave world and its inhabitants belong to the Ur-Quan.
> I am Starbase Commander Talana of the slave planet Gaia.
> Your ship is not responding to standard Hierarchy identification sequences.
> You are therefore classed as Independent and... WHAT?!
> Is my monitor display correct?!
> Is that a human commanding that vessel?
> Who are you?

**Shipped v0.5.2 (A)**:
> 注意，身分不明星艦！
> 警告！ 這顆奴役星球和其居民屬於烏寬族。
> 我是奴役星球蓋亞的星際基地指揮官泰蘭娜。
> 爾艦沒有回應標準階層識別序列。
> 因此判定為獨立艦艇… 什麼？！
> 我的螢幕顯示無誤嗎？！
> 那艘艦艇的指揮官是人類嗎？
> 您是誰？

**Rebuild v3 (B)**:
> 注意，身分不明的太空艦艇！
> 警告！ 這顆奴役星球和其居民屬於烏寬族。
> 我是奴役星球蓋亞（Gaia）的星際基地指揮官泰蘭娜。
> 您的艦艇沒有回應標準階層識別序列。
> 因此您被歸類為獨立艦艇，而且…… 什麼？！
> 我的螢幕顯示無誤嗎？！
> 那艘艦艇的指揮官是人類嗎？
> 您是哪位？

**推薦**: 🎯 **B (v3)** — 首介 gloss「蓋亞（Gaia）」+ 廢除 shipped「爾艦」+「歸類為獨立艦艇」貼原文

### B#2 · `we_are_vice_squad` · ✨ 首介 gloss「道德警察（Ethics Police）」

**英文原文**:
> We're the Ethics Police. Justify that costume... Immediately!

**Shipped v0.5.2 (A)**:
> 我方是道德警察。 立刻解釋那身制服的正當性！

**Rebuild v3 (B)**:
> 我方是道德警察（Ethics Police）。 請立刻解釋這身裝扮的合理性…… 馬上！

**推薦**: 🎯 **B (v3)** — 首介 gloss「道德警察（Ethics Police）」

### B#3 · `NO_NEED_HELP` · ✨ 首介 gloss「賽拉（Syra）」+ palette 純化

**英文原文**:
> Look friend, I appreciate your offer, but we don't want your help.
> Why? I'll tell you why
> because we're not going to do anything to antagonize the Ur-Quan. That's why.
> We may not like slavery, but it's a damn sight better than our alternatives.
> Below us we have a beautiful world... maybe it's not Syra, but at least it's a home.
> That's a lot more than we ever had before the War... before the Ur-Quan became our masters.

**Shipped v0.5.2 (A)**:
> 聽著朋友，您的好意我心領了，但我族不需要您的幫忙。
> 為什麼？ 我告訴您為什麼
> 因為我族不會做任何激怒烏寬的事。 這就是原因。
> 奴役也許不好受，但比起我族的其他選擇好上千萬倍。
> 下方是一顆美麗的世界… 也許不是賽拉，但至少是個家。
> 那比我族在戰前… 在烏寬成為我族主人之前，擁有的任何東西都多。

**Rebuild v3 (B)**:
> 聽著，朋友，我感謝您的好意，但我族不想要您的幫助。
> 為什麼？ 我告訴您為什麼——
> 因為我族不會做任何激怒烏寬族的事。 就是這樣。
> 我族或許不喜歡奴役，但比起別的選擇，這已經好太多了。
> 我族下方有一顆美麗的世界…… 或許它不是賽拉（Syra），但至少是個家。
> 這已經比戰爭之前…… 比烏寬族成為我族主人之前所擁有的還多了。

**推薦**: 🎯 **B (v3)** — 首介 gloss「賽拉（Syra）」+ palette 純化

### B#4 · `i_need_touch_o_vision` · ✨ 首介 gloss「觸感視（Touch-o-Vision）」(Q11=C)

**英文原文**:
> What I need right now, is a Touch-o-Vision.

**Shipped v0.5.2 (A)**:
> 我現在真正需要的，是一台觸感視。

**Rebuild v3 (B)**:
> 我現在需要的，是一台觸感視（Touch-o-Vision）。

**推薦**: 🎯 **B (v3)** — 首介 gloss「觸感視（Touch-o-Vision）」(Q11=C)

### B#5 · `know_about_deep_children` · ✨ 首介 gloss「深淵之子（Deep Children）」

**英文原文**:
> Talana, have you ever heard of the `Deep Children?'

**Shipped v0.5.2 (A)**:
> 泰蘭娜，您聽過『深淵之子』這個詞嗎？

**Rebuild v3 (B)**:
> 泰蘭娜，妳聽說過「深淵之子」（Deep Children）嗎？

**推薦**: 🎯 **B (v3)** — 首介 gloss「深淵之子（Deep Children）」

### B#6 · `WHAT_ABOUT_DEEP_CHILDREN` · ✨ 首介 gloss「超波（HyperWave）」+「光之矛（Spears of Light）」

**英文原文**:
> Yes, I think so. Aren't they part of the Mycon religion somehow?
> We have recordings of Mycon HyperWave transmissions from the War... pretty weird stuff.
> The Mycons just kind of.. rambled, never making much sense.
> They talked a lot about `Deep Children', and `Spears of Light',
> but we couldn't ever understand what they were talking about.

**Shipped v0.5.2 (A)**:
> 有的，我想是的。 它們不是麥孔族宗教的一部分嗎？
> 我族有戰時麥孔族超波通訊的錄音… 內容非常詭異。
> 麥孔族就那樣… 喃喃自語，多半聽不出所以然。
> 他們談了很多『深淵之子』和『光之矛』
> 但我族從來搞不清楚他們在講什麼。

**Rebuild v3 (B)**:
> 是的，我想我聽過。 那不是麥孔族宗教的一部分嗎？
> 我族有戰爭時期的麥孔族超波（HyperWave）通訊錄音…… 相當詭異的東西。
> 麥孔族就只是…… 喃喃自語，聽起來幾乎沒什麼道理。
> 他們常提到「深淵之子」還有「光之矛」（Spears of Light），
> 但我族從來沒聽懂他們在說什麼。

**推薦**: 🎯 **B (v3)** — 首介 gloss「超波（HyperWave）」+「光之矛（Spears of Light）」

### B#7 · `OUR_NEW_WORLD` · ✨ 首介 gloss「棲居艦三十一號（Habitat Thirty-One）」+「星際巡邏隊（Space Patrol）」+「黛安妮（Diani）」+「雷奈特（Raynet）」+「烏寬主宰九號（Ur-Quan Master Nine）」(Q8=A · 廢除 shipped「主人九號」)

**英文原文**:
> When the Ur-Quan conquered us, over twenty years ago
> I was only a young girl living in Habitat Thirty-One.
> My older sister, Diani, was a starship officer in the Space Patrol
> she was part of the final defense at Raynet... she didn't make it back.
> When the Ur-Quan caught us in open space, we all thought we were going to die
> but then, instead of killing us, the Ur-Quan offered us a choice:
> we could join the ranks of their combat thralls, or we could be slave-shielded in our homeworld.
> Like the people of Earth, we chose peace. We became fallow slaves.
> When the Ur-Quan told us to return to our homeworld, we explained that we had none.
> Ur-Quan Master Nine explained that they had encountered this situation before
> and if we would provide them with a list of our requirements
> they would use their extensive astronomical datastores to find a planet for us!
> So we told them about Syra... about the color of its sky... about the abundant lifeforms,
> about the fertility of the soil and seas.
> Less than an hour later, we received a terse message from Master Nine
> we were to proceed to these coordinates and disembark. This was to be our new home.
> But our new world, Gaia, was everything we described.
> We'd been searching for a home planet for seventy-five years
> and in the end, it was our enemies who gave one to us.
> I grew up on a small island off the main continent, and like all of my people
> we lived each day under the sick, red glow of the slave shield.
> When the Ur-Quan arrived seven years ago to refurbish and recrew this starbase
> I was selected as the new commander.

**Shipped v0.5.2 (A)**:
> 當烏寬征服我族時，二十多年前
> 我只是個住在棲居艦三十一號的小女孩。
> 我的姊姊黛安妮是星際巡邏隊的星艦軍官
> 她參與了在雷奈特的最後防禦戰… 沒能回來。
> 當烏寬在開闊太空追上我族時，我族都以為要死了
> 但他們沒殺我族，而是給了我族一個選擇:
> 加入他們的戰奴，或者被奴役護盾罩在母星上。
> 就像地球人一樣，我族選擇了和平。 我族成了休耕奴。
> 當烏寬要我族回母星時，我族解釋我族沒有母星。
> 烏寬主人九號解釋他們遇過這種狀況
> 只要我族提供一份需求清單
> 他們會動用龐大的天文資料庫替我族找一顆行星！
> 所以我族告訴他們賽拉的事… 天空的顏色、豐富的生命
> 土壤和海洋的肥沃。
> 不到一小時，我族收到主人九號簡短的訊息
> 要我族前往指定座標登陸。 那將是我族的新家。
> 而我族的新世界，蓋亞，確實如我族所描述的一切。
> 我族尋找家園七十五年之久
> 最後竟是敵人給了我族一個。
> 我在主大陸外的小島上長大，跟我族其他人一樣
> 我族每天都活在那病態紅光的奴役護盾下。
> 七年前烏寬來這裡整修並補充星際基地人員時
> 我被選為新任指揮官。

**Rebuild v3 (B)**:
> 烏寬族征服我族的時候，二十多年前——
> 我當時只是個住在棲居艦三十一號（Habitat Thirty-One）的小女孩。
> 我姊姊黛安妮（Diani），是星際巡邏隊（Space Patrol）的一名星艦軍官
> 她參加了雷奈特（Raynet）的最後防禦戰…… 她沒能回來。
> 當烏寬族在外太空攔截到我族時，我們姐妹都以為我們要死了
> 但接著，烏寬族沒有殺我族，反而給了我族一個選擇：
> 我族可以加入他們戰奴的行列，或者在母星上被奴役護盾封印。
> 就像地球人一樣，我族選了和平。 我族成了禁足奴族。
> 當烏寬族要我族返回母星時，我族向他們解釋，我族已經沒有家了。
> 烏寬主宰九號（Ur-Quan Master Nine）表示，他們過去遇過這種情況
> 只要我族提供一份需求清單
> 他們就會用龐大的天文資料庫替我族找一顆行星！
> 於是我族告訴他們賽拉的事…… 天空的顏色…… 豐饒的生命
> 還有土壤與海洋的肥沃。
> 不到一小時後，我族收到主宰九號簡短的訊息
> 要我族前往這些座標登陸。 那將是我族的新家園。
> 而我族的新世界蓋亞，正如我族描述的那樣。
> 我族尋找家園已經找了七十五年
> 到頭來，卻是我族的敵人把家園給了我族。
> 我在主大陸外的一座小島上長大，跟我族所有人一樣
> 我們姐妹每一天都活在奴役護盾那種病態的紅色光芒底下。
> 七年前烏寬族回到這裡，翻修並重新配置這座星際基地
> 我被選為新任指揮官。

**推薦**: 🎯 **B (v3)** — 首介 gloss「棲居艦三十一號（Habitat Thirty-One）」+「星際巡邏隊（Space Patrol）」+「黛安妮（Diani）」+「雷奈特（Raynet）」+「烏寬主宰九號（Ur-Quan Master Nine）」(Q8=A · 廢除 shipped「主人九號」)

### B#8 · `BEFORE_WAR` · ✨ 首介 gloss「依瑪（Yma）」

**英文原文**:
> Our species are almost identical, almost too close a match to be just a coincidence.
> Our bodies are very similar, Captain.
> Ha! ha! Except for... certain parts...
> Our cultural development is also mostly parallel.
> Like you Earthlings, we evolved a society from primitive tribes
> whose main function were to protect themselves from the large reptiles native to our old world.
> The main difference between our two sets of cultures... the split in the paths of our development
> occurred in what would have been your prehistory, say 5000 BCE.
> In your world, the agricultural communities were conquered by the more primitive but also more aggressive, migratory herding peoples.
> This led to a particular kind of sexual and political dominance structure
> which pervaded almost all of your Earth Cultures until the early Twenty First century.
> On Syra, our only primitive migratory tribes were confined to our mountainous regions.
> Their herd beasts, the Yma, did not do well in the agricultural basins and plains.
> The two cultures were isolated until much later
> when the technological superiority of the farmers curtailed any major conflict.

**Shipped v0.5.2 (A)**:
> 我方兩族幾乎一模一樣，如此相近絕非巧合可解。
> 我方身體構造非常接近，艦長。
> 哈！ 哈！ 除了… 某些部位……
> 我方文化發展也大致平行。
> 就像您們地球人，我族從原始部落發展出社會
> 最初的功能是抵禦舊母星原生的大型爬蟲類。
> 我方兩套文化最主要的分歧… 發展路徑的分岔
> 發生在您們的史前時代，大約公元前 5000 年。
> 您們的世界中，農業社群被更原始但更侵略性的遷徙牧民部落征服了。
> 這導致了某種性別與政治支配結構
> 貫穿幾乎所有地球文化直到 21 世紀初。
> 在賽拉，我族唯一的原始遷徙部落被限制在山地。
> 他們的畜群獸『依瑪』在農業盆地和平原適應不良。
> 兩種文化長期隔離
> 直到後來農民的科技優勢，讓重大衝突未曾發生。

**Rebuild v3 (B)**:
> 我族的物種幾乎一模一樣，相似到不像是巧合。
> 我族的身體構造非常相近，艦長。
> 哈！ 哈！ 除了…… 某些部位以外……
> 我族的文化發展也大致並行。
> 像你們地球人一樣，我族的社會也是從原始部落演化而來
> 主要功能是保護自己不被我族舊世界原生的大型爬蟲類獵殺。
> 我族兩套文化最主要的差異…… 我族發展路徑的分歧點
> 發生在相當於你們史前時代的時候，大約公元前 5000 年。
> 在你們的世界，農業社群被更原始但也更好戰的遊牧民族征服。
> 這造就了一種特定的性別與政治支配結構
> 幾乎席捲了你們整個地球文化，直到二十一世紀初期。
> 在賽拉上，我族僅有的原始遊牧部落被侷限在山區。
> 他們的畜牧獸依瑪（Yma）在農業盆地和平原上活不好。
> 兩種文化長時間保持隔離
> 直到後來，農民的科技優勢阻止了任何重大衝突。

**推薦**: 🎯 **B (v3)** — 首介 gloss「依瑪（Yma）」

### B#9 · `OPEN_VAULT` · ✨ 首介 gloss「穿透艦（Penetrator）」

**英文原文**:
> Our first step is to get some mobility.
> We have some fine starship officers on board, and they are all eager to go after the Mycons,
> but without our Penetrator starships, we're totally ineffectual.
> So our first step HAS to be recovering our Space Patrol combat fleet.
> We know that the Ur-Quan didn't destroy them... they never waste anything
> but we believe they have sealed them in some kind of deep vault in the surface of an alien planet.

**Shipped v0.5.2 (A)**:
> 我方第一步是取得機動能力。
> 我方船上有一批優秀的星艦軍官，都渴望對付麥孔族
> 但沒有我方的穿透艦，我方毫無戰力。
> 所以第一步必須是取回我方星際巡邏隊的戰鬥艦隊。
> 我方知道烏寬沒有摧毀它們… 他們從不浪費任何東西
> 但我方相信他們把艦隊封在某顆外星行星地表下的深層地窖裡。

**Rebuild v3 (B)**:
> 我族的第一步是取得機動能力。
> 我族艦上有一批優秀的星艦軍官，全都渴望對付麥孔族，
> 但沒有我族的穿透艦（Penetrator），我族毫無戰力。
> 所以第一步必須是取回我族星際巡邏隊的戰鬥艦隊。
> 我族知道烏寬族沒有摧毀它們…… 他們從不浪費任何東西
> 但我族相信他們把艦隊封在某顆外星行星地表下的深層地窖裡。

**推薦**: 🎯 **B (v3)** — 首介 gloss「穿透艦（Penetrator）」

### B#10 · `doing_this_for_you` · ✨ 首介 gloss「小甜心（Sweet Cakes）」(Q3=A) · 廢除 shipped「甜心」單獨用法

**英文原文**:
> Just remember, I'm doing this for you Sweet Cakes!

**Shipped v0.5.2 (A)**:
> 記得喔，我這都是為了妳做的，甜心！

**Rebuild v3 (B)**:
> 記得喔，我這都是為了妳做的，小甜心（Sweet Cakes）！

**推薦**: 🎯 **B (v3)** — 首介 gloss「小甜心（Sweet Cakes）」(Q3=A) · 廢除 shipped「甜心」單獨用法

### B#11 · `GENERAL_INFO_AFTER_AMBUSH_2` · ✨ 首介 gloss「（Horologii）」

**英文原文**:
> We have been intercepting a concentration of Hierarchy broadcasts
> but we cannot translate their content.
> They all appear to be originating from the direction of the <% comm.getConstellation("Horologii", "samatra") %> constellation.

**Shipped v0.5.2 (A)**:
> 我方一直攔截到大量階層通訊
> 但無法翻譯內容。
> 所有訊號似乎都從 <% comm.getConstellation("時鐘座", "samatra") %> （Horologii）方向發出。

**Rebuild v3 (B)**:
> 我族一直攔截到大量的階層通訊
> 但無法翻譯內容。
> 所有訊號似乎都從 <% comm.getConstellation("時鐘座", "samatra") %>（Horologii） 方向發出。

**推薦**: 🎯 **B (v3)** — 首介 gloss「（Horologii）」

### B#12 · `OK_REPEAT_PLAN` · ✨ 首介 gloss「歐加農（Organon）」

**英文原文**:
> Ok, here's the plan, again.
> You must go to the Mycons and tell them about a world at the <% comm.getStarName("Organon", "mycon trap") %> star system.
> Tell them that you have found the perfect world for their hideous Deep Children.
> We will hide there and wait for them in ambush.
> Then we shall destroy them.

**Shipped v0.5.2 (A)**:
> 好，計畫再說一次。
> 您必須前往麥孔族，告訴他們 <% comm.getStarName("歐加農", "mycon trap") %> （Organon）星系有一顆世界。
> 告訴他們您找到了給他們可怕深淵之子的完美世界。
> 我方會在那裡埋伏等候他們。
> 然後我方將把他們毀滅。

**Rebuild v3 (B)**:
> 好，計畫再說一次。
> 您必須前往麥孔族那裡，告訴他們 <% comm.getStarName("歐加農", "mycon trap") %>（Organon） 星系有一顆世界。
> 告訴他們您找到給他們可怕深淵之子的完美世界。
> 我族會躲在那裡埋伏等候他們。
> 然後我族將消滅他們。

**推薦**: 🎯 **B (v3)** — 首介 gloss「歐加農（Organon）」

### B#13 · `in_the_spirit` · ✨ 首介 gloss「卡哇邦嘎（COWABUNGA!）」(Q4=C · 保留台灣忍者龜 gag + 補英文 gloss)

**英文原文**:
> I see! Well, in the spirit of interspecies communication, let me just say, COWABUNGA!

**Shipped v0.5.2 (A)**:
> 我懂了！ 好吧，本著跨物種交流的精神，讓我說一句「卡哇邦嘎」！

**Rebuild v3 (B)**:
> 我懂了！ 好吧，本著跨物種交流的精神，容我說一句：卡哇邦嘎！（COWABUNGA!）

**推薦**: 🎯 **B (v3)** — 首介 gloss「卡哇邦嘎（COWABUNGA!）」(Q4=C · 保留台灣忍者龜 gag + 補英文 gloss)

---

## C · 🔴 語意/voice icon 大差異 (5 tokens · 逐項決策)

**規則**：這些 tokens 涉及 Mode 4 CAPS icon / Mode 2 flirt interpretive enhance / Mode 3 深沉哀傷 icon — shipped 與 v3 有明確的譯法哲學差異。**預設 B (v3)** 依 dossier v0.7，但 shipped 某些 F系列 audit 選擇（如 F2:J MAYBE_CAPTAIN）也具詩意價值，值得單獨審視。

### C#1 · `MAYBE_CAPTAIN` · 🔴 Mode 2 flirt punchline · shipped 為 F2:J audit 加了「不在口舌之間，而在… 更下面的地方」的 flirt interpretive enhance；v3 直譯貼原文「在別的地方」

**英文原文**:
> Ah, yes... I had almost forgotten the sophistication of human social graces.
> Manners were never the Earthlings' strong point, were they?
> Your species' undeniable appeal can be found... elsewhere.

**Shipped v0.5.2 (A)**:
> 啊，是啊… 我幾乎忘記人類社交禮儀的高雅程度。
> 禮貌從來不是地球人的強項，是吧？
> 您的物種真正無可否認的魅力…… 不在口舌之間，而在… 更下面的地方。

**Rebuild v3 (B)**:
> 啊，是啊…… 我幾乎忘了人類社交禮儀有多「高雅」。
> 禮貌從來不是地球人的強項，是吧？
> 你們物種真正無可否認的魅力…… 在別的地方。

**推薦**: **B (v3)** 依 dossier 直白調情 icon · 但 shipped F2:J 詩意 enhance 也值得考慮 → **可 A** 若你重視原 F 系列 audit 成果

### C#2 · `NEED_PROOF` · 🔴 Mode 3+4 icon · dossier「BURNING RAGE → 心中燃起熊熊的怒火」+ Mode 3 直白你

**英文原文**:
> Captain, if what you say is true, it would turn my world upside down.
> You have no sorrow to match what each of us Syreen feels every day of our lives
> when we remember what we have lost... Syra... our Eden.
> The very idea that the Mycons, or any alien race, may have been responsible for Syra's destruction
> fills me with BURNING RAGE!
> If it were true, none of us here would rest until we had avenged ourselves on the perpetrators.
> We would find some way to leave this starbase, locate our starships, and hunt down the evil monsters!
> Captain, if you ever gather proof of what you say, you MUST inform us immediately.
> But until then... do not mention the subject again. It is too painful.

**Shipped v0.5.2 (A)**:
> 艦長，若您說的是真的，會徹底顛覆我的世界觀。
> 您的悲傷無一能與我等姐妹每人日日承受的相比
> 當我等姐妹回想失去的一切… 賽拉… 我族的伊甸園。
> 光是想到麥孔族，或任何異族，可能對賽拉的毀滅負責
> 就讓我怒火中燒！
> 若這是真的，我族沒有一個人會安於現狀，直到向元兇復仇為止。
> 我族會想盡辦法離開這座星際基地，找回我族的星艦，獵殺那些邪惡的怪物！
> 艦長，若您日後蒐集到證據，您必須立刻通知我族。
> 但在那之前… 別再提這件事。 這太痛了。

**Rebuild v3 (B)**:
> 艦長，如果你所說的是真的，那將把我的整個世界翻轉過來。
> 你的悲傷無法比擬我們塞蓮族每一天所感受的痛
> 每當我們憶起失去的一切…… 賽拉…… 我族的伊甸園。
> 光是「麥孔族，或任何外星種族，可能是賽拉毀滅的元兇」這個念頭本身
> 就讓我心中燃起熊熊的怒火！
> 如果那是真的，我族在這裡不會有一個人歇息，直到我族向兇手復仇為止。
> 我族會想辦法離開這座星際基地，找回我族的戰艦，追獵那些邪惡的怪物！
> 艦長，若你日後蒐集到你所說的證據，你必須立刻通知我族。
> 但在那之前…… 不要再提這個話題。 太痛了。

**推薦**: 🎯 **B (v3)** — Mode 3+4 icon · dossier「BURNING RAGE → 心中燃起熊熊的怒火」+ Mode 3 直白你

### C#3 · `HORRIBLE_TRUTH` · 🔴 Mode 4 CAPS icon · dossier canonical「必將付出慘痛代價」+ 清 shipped「此等能力」→「這種能力」+ Read-Aloud「一模一樣」(去「完全」冗餘)

**英文原文**:
> Great gods! These fragments... they are IDENTICAL to the debris we found near the puncture on Syra!
> We never guessed that the fragments might be organic!
> To have survived re-entry!... nothing organic would remain!... unless
> UNLESS, it was genetically constructed for this purpose!
> AND ONLY THE MYCONS POSSESS THIS CAPABILITY!!
> We will make further tests. Genetic comparisons. Compositional analysis.
> If what you have suggested is true... THE MYCONS WILL PAY DEARLY FOR THEIR CRIMES!!!
> Now LEAVE US, Captain!
> We have work to do.

**Shipped v0.5.2 (A)**:
> 諸神在上！ 這些碎片… 它們和我族在賽拉穿孔附近找到的殘骸完全一樣！
> 我族從未想過那些碎片可能是有機體！
> 竟然撐過大氣層再入！… 有機體根本不可能留下！… 除非
> 除非它是為此目的基因製造的！
> 唯有麥孔族擁有此等能力！！
> 我族會做進一步測試。 基因比對。 成分分析。
> 若您說的是真的… 麥孔族將為他們的罪行付出慘痛代價！！
> 現在離開我族，艦長！
> 我族還有工作要做。

**Rebuild v3 (B)**:
> 諸神在上！ 這些碎片…… 它們和我族在賽拉穿孔附近找到的殘骸一模一樣！
> 我族從未想過那些碎片可能是有機體！
> 竟然能挺過大氣層再入！…… 有機體根本不可能倖存下來！…… 除非——
> 除非它是為此目的基因製造出來的！
> 而且只有麥孔族擁有這種能力！！
> 我族會做進一步測試。 基因比對。 成分分析。
> 如果你所暗示的是真的…… 麥孔族必將為他們的罪行付出慘痛代價！！！
> 現在，離開我族，艦長！
> 我族還有工作要做。

**推薦**: 🎯 **B (v3)** — Mode 4 CAPS icon · dossier canonical「必將付出慘痛代價」+ 清 shipped「此等能力」→「這種能力」+ Read-Aloud「一模一樣」(去「完全」冗餘)

### C#4 · `HELLO_AFTER_AMBUSH_1` · 🔴 Mode 4 CAPS icon · dossier canonical「正義屬於我們」+ v3「寸寸切碎」(sliced to ribbons)

**英文原文**:
> SUCCESS, Captain! The Mycons' fleet is in shambles!
> JUSTICE IS OURS!
> We have revenged ourselves against the heinous Mycons!
> They fell for our trap so completely!
> When they approached <% comm.getStarName("Organon", "mycon trap") %> I, we were hiding behind its moon.
> As they approached, their ships broke combat formation
> in preparation for their hideous implanting ceremony.
> We waited until they were fully dispersed around the planet, then we attacked!
> The standard Mycon tactic would have been to speed out of orbit using a gravity whip maneuver
> but the Podships refused to abandon their slow-moving Deep Children spore pods.
> They remained in the gravity well, and WE SLICED THEM TO RIBBONS!
> They must have lost a dozen ships to their own stupidity... running into their own Plasmoids!
> The rest?... well we took care of most of them... in our own special way.
> and Captain, now that we have taken our revenge on the Mycon
> we give you our starship officers and Penetrator designs so that you can add our ships
> to your fleet.

**Shipped v0.5.2 (A)**:
> 成功了，艦長！ 麥孔族艦隊潰不成軍！
> 正義屬於我等姐妹！
> 我族已對可憎的麥孔族復仇！
> 他們完完全全落入我方的陷阱！
> 當他們接近 <% comm.getStarName("歐加農", "mycon trap") %> （Organon）I 時，我方藏在它的月球背面。
> 他們接近時，艦艇打散戰鬥隊形
> 準備進行他們可怕的植入儀式。
> 我方等到他們完全分散環繞行星，就發動攻擊！
> 標準麥孔族戰術會是用重力甩尾機動加速脫離軌道
> 但莢艦拒絕拋下他們緩慢移動的深淵之子孢子莢。
> 他們留在重力井中，於是我方將他們碎屍萬段！
> 光是自己的愚蠢就讓他們損失了十幾艘… 撞上自己的電漿體！
> 其餘的？… 我方也用… 我方自己的特殊方式，把他們大部分收拾了。
> 艦長，既然我族已向麥孔族復仇
> 我方把星艦軍官和穿透艦設計給您，讓您能把我方的艦艇
> 加入您的艦隊。

**Rebuild v3 (B)**:
> 成功了，艦長！ 麥孔族的艦隊已經潰不成軍！
> 正義屬於我們！
> 我族終於對那些可恨的麥孔族復了仇！
> 他們徹徹底底上了我族的當！
> 當他們接近 <% comm.getStarName("歐加農", "mycon trap") %> I 的時候，我族正藏在它的衛星背後。
> 隨著他們接近，他們的艦艇解開作戰隊形
> 準備進行他們可怕的植入儀式。
> 我族等到他們在行星周圍完全散開，然後就攻擊了！
> 麥孔族標準的戰術是利用引力抽鞭甩出軌道
> 但那些莢艦不肯捨棄慢速的深淵之子孢子艙。
> 他們留在引力井裡，而我族把他們寸寸切碎！
> 他們光憑自己的愚蠢就損失了十幾艘艦…… 撞上自己的電漿團！
> 其餘的呢？…… 呃，我族用自己特別的方式處理了大部分。
> 艦長，既然我族已對麥孔族報了仇
> 我族把星艦軍官和穿透艦的設計圖交給你，好讓你能把我族的艦艇編入
> 你的艦隊。

**推薦**: 🎯 **B (v3)** — Mode 4 CAPS icon · dossier canonical「正義屬於我們」+ v3「寸寸切碎」(sliced to ribbons)

### C#5 · `NOT_EVIL_MONSTER` · 🔴 Mode 4 拖音 icon (Q10=A · 使用者 override 我推薦 C 選 A)：`WHY CAAPTAIN → 為什——麼——艦——長` / `WHYEVER DOO YOOU SAAY THAAAT → 你怎——麼——會——這麼——說呢——` / `REEAARRGGGG → 呃嗚嗷嗷嗷` · **廢除 shipped 保留英文 CAPS**

**英文原文**:
> Ha!-ha!-ha! An alien monster? Me?
> ME?! WHY CAAPTAIN! WHYEVER DOO YOOU SAAY THAAAT!!!
> REEAARRGGGG!!!!
> ...just kidding!

**Shipped v0.5.2 (A)**:
> 哈！-哈！-哈！ 異族怪物？ 我？
> 我？！ WHYEVER 艦~長！ WHYEVER DOO YOOU SAAY THAAAT！！！
> REEAARRGGGG！！！！
> … 開玩笑的啦！

**Rebuild v3 (B)**:
> 哈！-哈！-哈！ 外星怪物？ 我？
> 我？！ 為什——麼——艦——長！ 你怎——麼——會——這麼——說呢——！！！
> 呃嗚嗷嗷嗷！！！！
> …… 開玩笑的啦！

**推薦**: 🎯 **B (v3)** — Mode 4 拖音 icon (Q10=A · 使用者 override 我推薦 C 選 A)：`WHY CAAPTAIN → 為什——麼——艦——長` / `WHYEVER DOO YOOU SAAY THAAAT → 你怎——麼——會——這麼——說呢——` / `REEAARRGGGG → 呃嗚嗷嗷嗷` · **廢除 shipped 保留英文 CAPS**

---

## D · 🟠 Mode-shift 您→你 + 文言清除 (27 tokens · Q1=B 系統套用)

**規則**：Q1=B Mode-based · shipped 幾乎全篇 100% 用 `您`（極 Taiwanese-formal），v3 依 Mode 切換：Mode 1 官方=您（保留）· Mode 2 調情 / Mode 3 深沉 / Mode 4 CAPS = 你（直白）。文言清除：`爾艦` `此等` `哉` 全清為現代白話。**預設 B (v3)**。

**代表樣本 D#1 · `CANT_GIVE_HELP` · Mode 2 flirt icon（招牌「我喜歡你」）**

**英文原文**:
> Look Captain... I like you... even though you're an obnoxious human... I like you.
> In another time, we might have become good friends... perhaps more
> but that's a fantasy, and my job is dealing with reality.
> We're not going to do anything to jeopardize what we've got here.
> We've come too far... lost too much, to ever risk losing Gaia, our new home.
> Don't get all judgmental on me, Captain... you don't know what we've been through.

**Shipped v0.5.2 (A)**:
> 聽著艦長… 我喜歡您… 就算您是個惹人厭的人類… 我還是喜歡您。
> 換個時空，我倆或許能成為好朋友… 甚至更多
> 但那是幻想，而我的職務是面對現實。
> 我族不會做任何危及此地一切的事。
> 我族付出太多… 失去太多，絕不能再冒失去蓋亞這個新家的險。
> 別對我過度批判，艦長… 您不知道我族經歷過什麼。

**Rebuild v3 (B)**:
> 聽著，艦長…… 我喜歡你…… 儘管你是個討人厭的地球人…… 我還是喜歡你。
> 在另一段時空裡，我們或許能成為好朋友…… 甚至更進一步——
> 但那不過是幻想，我的工作是面對現實。
> 我族不會做任何事去破壞現在擁有的一切。
> 我族走得太遠了…… 失去得太多了，絕不願再冒險失去蓋亞，我族的新家園。
> 別對我下這種評斷，艦長…… 你不知道我們姐妹經歷過什麼。

**推薦**: **B (v3)** — Mode 2 直白 你 · dossier 招牌 icon 貼原文

**代表樣本 D#2 · `READY_FOR_AMBUSH` · 文言清除**

**英文原文**:
> We will wait here for the Mycons.

**Shipped v0.5.2 (A)**:
> 我方會在此等候麥孔族。

**Rebuild v3 (B)**:
> 我族會在此等候麥孔族。

**推薦**: **B (v3)** — 清「在此等候（含此等 substring 誤觸不算 · 語意為 wait here）」→ 已為現代白話

**完整 D 系列 token 表**：

| # | Token | 類別 |
|---|---|---|
| D#1 | `HOW_CAN_YOU_BE_HERE` | Q1=B Mode-shift 您(4)→你 (Mode 2/3/4) |
| D#2 | `we_here_to_help` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#3 | `we_need_help` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#4 | `CANT_GIVE_HELP` | Q1=B Mode-shift 您(4)→你 (Mode 2/3/4) |
| D#5 | `OK_NEED` | Q1=B Mode-shift 您(5)→你 (Mode 2/3/4) |
| D#6 | `TOUCH_O_VISION` | Q1=B Mode-shift 您(5)→你 (Mode 2/3/4) |
| D#7 | `mycons_involved` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#8 | `WHAT_PROOF` | Q1=B Mode-shift 您(4)→你 (Mode 2/3/4) |
| D#9 | `have_no_proof` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#10 | `ABOUT_WAR` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#11 | `ABOUT_HOMEWORLD` | Q1=B Mode-shift 您(4)→你 (Mode 2/3/4) |
| D#12 | `DONT_KNOW_HOW` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#13 | `HOPE_YOU_LIKE_IT` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#14 | `HELLO_AFTER_AMBUSH_2` | Q1=B Mode-shift 您(7)→你 (Mode 2/3/4) |
| D#15 | `HELLO_AFTER_AMBUSH_3` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#16 | `HELLO_AFTER_AMBUSH_4` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#17 | `GRATITUDE` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#18 | `READY_FOR_AMBUSH` | v0.7 文言清除：此等 |
| D#19 | `GOODBYE_BEFORE_AMBUSH` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#20 | `MORE_COMFORTABLE` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#21 | `OK_SPIRIT` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#22 | `SOMETHING_LIKE_THIS` | Q1=B Mode-shift 您(3)→你 (Mode 2/3/4) |
| D#23 | `OK_WONT_USE_HANDS` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#24 | `THEN_LET_ME_TEACH` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |
| D#25 | `THEN_STOP_TALKING` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#26 | `SEX_GOODBYE` | Q1=B Mode-shift 您(2)→你 (Mode 2/3/4) |
| D#27 | `OUT_TAKES` | Q1=B Mode-shift 您(1)→你 (Mode 2/3/4) |

---

## E · 🟡 措辭/palette 微調 (70 tokens · 全 B v3)

**規則**：這些是等價微調 —— 標點半→全形（`...` → `……`）· palette 微調（Q9=C · 廢除單獨用「我等」/精化「我方」vs「我族」分情境）· 個別詞語順化（如「幾乎忘記」→「幾乎忘了」）· 半形空格前後標點修正 · 招牌詞小校準。**預設全 B (v3)**。以下為代表樣本：

**代表樣本 E#1 · `HELLO_BEFORE_AMBUSH_2` · 微措辭**

**Shipped (A)**: 又見面了，可愛的人類。 \n 再次見到您，令我心頭一暖。

**Rebuild v3 (B)**: 又見面了，親切的人類。 \n 再次向您致意，令我心頭一暖。

**代表樣本 E#2 · `MATES_KILLED` · Mode 3 grief palette + 「我等姐妹→我們姐妹」廢除**

**Shipped (A) 節錄**：
> 我等姐妹明白，賽拉，我族的天堂、伊甸園，已經消失了。

**Rebuild v3 (B) 節錄**：
> 我們姐妹清楚看見，賽拉，我族的樂園、伊甸園，已經消失了。

（`我等姐妹` → `我們姐妹` · Q9=C 廢除文言化）

**代表樣本 E#3 · `HERES_REWARD` · Mode 2 微調**

**Shipped (A)**:
> 恐怕咱倆的職責都很危險，艦長。
> 我倆或許再也見不到彼此。
> 但至少現在，還有這個…

**Rebuild v3 (B)**:
> 恐怕我們兩人的任務都很危險，艦長。
> 我們或許再也見不到彼此。
> 但至少現在，還有這個……

**完整 E 系列 token 表**：

| # | Token | 類別 |
|---|---|---|
| E#1 | `HELLO_BEFORE_AMBUSH_2` | 措辭/palette 微調 |
| E#2 | `HELLO_BEFORE_AMBUSH_3` | 措辭/palette 微調 |
| E#3 | `OK_VICE` | 措辭/palette 微調 |
| E#4 | `we_are_the_one_for_you_baby` | 措辭/palette 微調 |
| E#5 | `WELCOME_VINDICATOR` | 措辭/palette 微調 |
| E#6 | `we_are_impressed` | 措辭/palette 微調 |
| E#7 | `SO_AM_I_CAPTAIN` | 措辭/palette 微調 |
| E#8 | `i_need_you` | 措辭/palette 微調 |
| E#9 | `have_proof` | 措辭/palette 微調 |
| E#10 | `look_at_egg_sacks` | 措辭/palette 微調 |
| E#11 | `what_doing_here` | 措辭/palette 微調 |
| E#12 | `what_about_war` | 措辭/palette 微調 |
| E#13 | `help_us` | 措辭/palette 微調 |
| E#14 | `WONT_HELP` | 措辭/palette 微調 |
| E#15 | `what_about_history` | 措辭/palette 微調 |
| E#16 | `what_about_homeworld` | 措辭/palette 微調 |
| E#17 | `what_about_outfit` | 措辭/palette 微調 |
| E#18 | `where_mates` | 措辭/palette 微調 |
| E#19 | `MATES_KILLED` | 措辭/palette 微調 |
| E#20 | `get_lonely` | 措辭/palette 微調 |
| E#21 | `MAKE_OUT_ALL_RIGHT` | 措辭/palette 微調 |
| E#22 | `bye` | 措辭/palette 微調 |
| E#23 | `MUST_ACT` | 措辭/palette 微調 |
| E#24 | `whats_next_step` | 措辭/palette 微調 |
| E#25 | `where_is_it` | 措辭/palette 微調 |
| E#26 | `DONT_KNOW_WHERE` | 措辭/palette 微調 |
| E#27 | `been_there` | 措辭/palette 微調 |
| E#28 | `GREAT` | 措辭/palette 微調 |
| E#29 | `GIVE_SHUTTLE` | 措辭/palette 微調 |
| E#30 | `im_on_my_way` | 措辭/palette 微調 |
| E#31 | `if_i_die` | 措辭/palette 微調 |
| E#32 | `GOOD_LUCK` | 措辭/palette 微調 |
| E#33 | `OK_FOUND_VAULT` | 措辭/palette 微調 |
| E#34 | `what_now` | 措辭/palette 微調 |
| E#35 | `HERES_THE_PLAN` | 措辭/palette 微調 |
| E#36 | `whats_my_reward` | 措辭/palette 微調 |
| E#37 | `HERES_REWARD` | 措辭/palette 微調 |
| E#38 | `GOODBYE_AFTER_VAULT` | 措辭/palette 微調 |
| E#39 | `what_now_after_ambush` | 措辭/palette 微調 |
| E#40 | `DO_THIS_AFTER_AMBUSH` | 措辭/palette 微調 |
| E#41 | `what_about_you` | 措辭/palette 微調 |
| E#42 | `ABOUT_ME` | 措辭/palette 微調 |
| E#43 | `whats_up_after_ambush` | 措辭/palette 微調 |
| E#44 | `GENERAL_INFO_AFTER_AMBUSH_1` | 措辭/palette 微調 |
| E#45 | `GENERAL_INFO_AFTER_AMBUSH_3` | 措辭/palette 微調 |
| E#46 | `GENERAL_INFO_AFTER_AMBUSH_4` | 措辭/palette 微調 |
| E#47 | `FOUND_VAULT_YET_2` | 措辭/palette 微調 |
| E#48 | `vault_hint` | 措辭/palette 微調 |
| E#49 | `OK_HINT` | 措辭/palette 微調 |
| E#50 | `found_vault` | 措辭/palette 微調 |
| E#51 | `bye_before_vault` | 措辭/palette 微調 |
| E#52 | `what_do_i_get_for_this` | 措辭/palette 微調 |
| E#53 | `not_sure` | 措辭/palette 微調 |
| E#54 | `PLEASE` | 措辭/palette 微調 |
| E#55 | `repeat_plan` | 措辭/palette 微調 |
| E#56 | `what_about_us` | 措辭/palette 微調 |
| E#57 | `ABOUT_US` | 措辭/palette 微調 |
| E#58 | `what_in_mind` | 措辭/palette 微調 |
| E#59 | `hands_off` | 措辭/palette 微調 |
| E#60 | `why_lights_off` | 措辭/palette 微調 |
| E#61 | `LIGHTS_OFF_BECAUSE` | 措辭/palette 微調 |
| E#62 | `evil_monster` | 措辭/palette 微調 |
| E#63 | `disease` | 措辭/palette 微調 |
| E#64 | `what_happens_if_i_touch_this` | 措辭/palette 微調 |
| E#65 | `THIS_HAPPENS` | 措辭/palette 微調 |
| E#66 | `are_you_sure_this_is_ok` | 措辭/palette 微調 |
| E#67 | `YES_SURE` | 措辭/palette 微調 |
| E#68 | `boy_they_never_taught` | 措辭/palette 微調 |
| E#69 | `not_much_more_to_say` | 措辭/palette 微調 |
| E#70 | `LATER` | 措辭/palette 微調 |

---

## F · 使用者決策格式

```
# 全依推薦（最快）
全 B

# 或分批決策
🟠 全 B · 🟡 全 B · ✨ 全 B · 🔴 全 B

# 或逐項 override
#C1=A  (MAYBE_CAPTAIN 保留 shipped F2:J 詩意 enhance)
#其他=B
```

**應用步驟**（收到決策後）：
1. Merge shipped + v3 依決策
2. Backup: `Copy-Item translations/syreen.zh-TW.json translations/syreen.zh-TW.pre-rebuild.bak`
3. Overwrite: 寫入 merged
4. 3-gate re-verify (purity / line-count / Lua template)
5. Build + package: `.\package_zh-TW.ps1`
6. Deploy to install/content/addons + verify addon markers
7. Update `Dossier_Revision_Progress.md`
8. Git commit