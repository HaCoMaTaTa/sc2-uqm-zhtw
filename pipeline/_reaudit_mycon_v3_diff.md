# Mycon Rebuild-Compare Diff Report (2026-08-17)

**Rebuild-Compare workflow**: `StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md`  
**v3 clean-room 翻譯**: `translations/mycon.zh-TW.v3.json` (109 tokens · 依 v0.7 dossier §四 + 使用者 Q1-Q20 決策)  
**shipped**: `translations/mycon.zh-TW.json` (109 tokens · v0.5.2 · 2026-08-10)  
**Read-Aloud self-fix (階段 2.5)**: 3/109 (2.8%) · log: `_selfaudit_mycon_v3_readaloud.md`  
**3-gate verify PASS**: purity 0 / Lua 0 / line-count 109/109  

## 統計

| 類別 | 數量 | 佔比 | 預設推薦 |
|---|---|---|---|
| 🟢 完全相同 | 39 | 36% | — (無需決策) |
| ✨ v0.7 canonical 升級 | 9 | 8% | **B (v3)** — 使用者 Q3/Q6/Q7/Q9 已定 |
| 🟠 主要重譯 (v0.5 文言 → v3 白話) | 6 | 6% | **B (v3)** — Utwig 級文言全清 |
| 🟠 markdown `**` icon 清除 | 1 | 1% | **B (v3)** — Q15=A 短句斷句 |
| 🟡 微調 (措辭等價) | 54 | 50% | **B (v3)** — Q10/Q11=A 全清文言 |

**清除 shipped 文言污染統計**：吾 34 → 0 · 吾等 61 → 0 · 之 117 → ~12 (canonical icon 保留：光之矛/祖輩之祖輩/聖源之X) · 乃 37 → 0 · 汝 36 → 0 · 此等 2 → 0 · 彼等 5 → 0 · markdown `**` 6 → 0

**快答格式建議**：使用者若全依推薦 → `全 B`（適用所有 70 個 diff 項）。若有異議 → 逐項標 `#N=A/C`。

---

## A · ✨ v0.7 canonical 升級 (9 tokens)

**規則**：Q3=A / Q6=A / Q7=A / Q9=A 使用者已定，v3 全面升級 shipped canonical。**預設 B (v3)**。

### A#1 · `RAMBLE_4` · ✨ 升級：`深淵之子`→`深層幼體`

**英文原文**:
> The Deep Children are part of Juffo-Wup -- home builders.
> The dwellers in the Mohorovichic.

**Shipped v0.5.2**:
> 深淵之子乃 聖源 之一部 —— 家園之篩造者。
> 深居地殼者。

**Rebuild v3**:
> 深層幼體是聖源的一部分——家園的建造者。
> 深居地殼者。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#2 · `RAMBLE_10` · ✨ 升級：`深淵之子`→`深層幼體`

**英文原文**:
> The Deep Children!
> Spears of light in the darkness! 
> Their discarded husks speak of joy to come.

**Shipped v0.5.2**:
> 深淵之子！
> 黑暗中之光矛！
> 彼等所棄之殼衣，訴說著即將之喜樂。

**Rebuild v3**:
> 深層幼體！
> 黑暗中的光之矛！
> 他們捨棄的殼衣，訴說著將至的喜樂。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#3 · `RAMBLE_25` · ✨ 升級：`深淵之子`→`深層幼體`

**英文原文**:
> The Deep Children fall from the Void, gathering speed for the penetration
> The tough casing warms as it passes through the atmosphere, glowing white as it hits the surface
> solid rock flows like liquid, and the child slips into the warm, safe depths beneath the crust.

**Shipped v0.5.2**:
> 深淵之子自虛空中墜落，為穿透累積速度
> 堅硬之殼衣於穿越大氣時變暖，撞擊地表時熾放白光
> 堅實之岩石如液體般流動，子代滑入地殼之下溫暖安全之深處。

**Rebuild v3**:
> 深層幼體自虛空中墜落，為穿透而累積速度
> 堅硬的殼衣穿越大氣時漸熱，撞擊地表時熾放白光
> 堅實的岩石如液體般流動，幼體便滑入地殼下方溫暖安全的深處。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#4 · `RAMBLE_28` · ✨ 升級：`孕育結點`→`孵化結點`

**英文原文**:
> I am Gussh
> I attend the birthing nodes
> I died 343 Earth years ago
> I do not know how.

**Shipped v0.5.2**:
> 吾乃古許（Gussh）
> 吾侍奉孕育結點
> 吾於三百四十三地球年前死去
> 吾不知因何。

**Rebuild v3**:
> 我是古許（Gussh）
> 我侍奉孵化結點
> 我於 343 地球年前死去
> 我不知因何。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#5 · `RAMBLE_29` · ✨ 升級：`創世者`→`造物主`

**英文原文**:
> When Juffo-Wup is complete
> when at last there is no Void, no Non
> when the Creators return
> then we can finally rest.

**Shipped v0.5.2**:
> 當 聖源 已然完整
> 當終無虛空、無異類
> 當創世者歸來
> 吾等便可終得安息。

**Rebuild v3**:
> 當聖源圓滿之時
> 當終於再無虛空，再無異類
> 當造物主（Creators）歸來
> 我們便終能安息。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#6 · `ABOUT_SHATTERED` · ✨ 升級：`深淵之子`→`深層幼體`

**英文原文**:
> These are the homes of the Deep Children.

**Shipped v0.5.2**:
> 此等乃深淵之子之家園。

**Rebuild v3**:
> 這些是深層幼體的家園。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#7 · `i_have_a_cunning_plan` · ✨ 升級：`深淵之子`→`深層幼體`

**英文原文**:
> There is a world at the star <% comm.getStarName("Organon", "mycon trap") %>. I believe it is perfect for your Deep Children.

**Shipped v0.5.2**:
> 在 <% comm.getStarName("歐加農", "mycon trap") %> （Organon） 星有一顆星球。 我方相信對你們的深淵之子而言那是完美之處。

**Rebuild v3**:
> 在 <% comm.getStarName("歐加農", "mycon trap") %> （Organon） 星有一顆星球。 我方相信對你們的深層幼體而言那是完美之處。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#8 · `UNFORSEEN_DELAYS` · ✨ 升級：`深淵之子`→`深層幼體` · 同時 markdown `**` 清除

**英文原文**:
> We have experienced unforeseen delays implanting Deep Children beneath the crust of <% comm.getStarName("Organon", "mycon trap") %> 1.
> However, Juffo-Wup is inevitable.  The Deep Children WILL be born.

**Shipped v0.5.2**:
> 吾等於 <% comm.getStarName("歐加農", "mycon trap") %> 1 之地殼下植入深淵之子時，遭遇了未預見之延誤。
> 然而，聖源 乃無可避免。 深淵之子**將**誕生。

**Rebuild v3**:
> 我們在 <% comm.getStarName("歐加農", "mycon trap") %> 1 的地殼下方植入深層幼體時，遭遇了未預見的延誤。
> 然而，聖源無可避免。 深層幼體必將誕生。 這是必然。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

### A#9 · `WE_GO_TO_IMPLANT` · ✨ 升級：`孕育艦隊`→`孵化艦隊` · 同時 markdown `**` 清除

**英文原文**:
> If your words are true, we will gladly spread Juffo-Wup to a new world!
> We will assemble the Birthing Fleet and send them to this planet.
> We will send many ships to protect the Children as they grow.
> You have been of service to us.
> Your insight into the ineffable Juffo-Wup is encouraging.
> Perhaps, if we were to plant spore sacs in your brain organ
> and let its tendrils spread through your flesh
> then you would truly understand Juffo-Wup... become part of Juffo-Wup.
> You WOULD be happier and more fulfilled.  Consider our offer.

**Shipped v0.5.2**:
> 若汝之言屬實，吾等將樂於將 聖源 散布至一新世界！
> 吾等將集結孕育艦隊，遣其至此星球。
> 吾等將遣多艦以保護子代之成長。
> 汝已為吾等效勞。
> 汝對難以言喻之 聖源 之洞察令人振奮。
> 或許，若吾等在汝之腦器官中植入孢囊
> 並讓其觸鬚遍布汝之肉身
> 則汝將真正理解 聖源……成為 聖源 之一部。
> 汝**將**更加幸福並更加滿足。 考慮吾等之提議。

**Rebuild v3**:
> 若你的言語屬實，我們將樂於將聖源散布至一新世界！
> 我們將集結孵化艦隊，遣其至此星球。
> 我們將派出多艘艦艇，護衛幼體的成長。
> 你為我們效勞了。
> 你洞察聖源那難以言喻的深意，令人振奮。
> 或許，若我們在你的腦器官中植入孢囊
> 並讓其觸鬚遍布你的肉身
> 那麼你便能真正理解聖源……成為聖源的一部分。
> 你會更加幸福。 更加滿足。 考慮我們的提議。

**推薦**: 🎯 **B (v3)** — 依 v0.7 dossier canonical

---

## B · 🟠 主要重譯 (Utwig 級文言全清 · 6 tokens)

**規則**：Shipped v0.5 使用「吾/爾/汝/乃/之」重度文言體，v3 依 v0.7 dossier §四 改「我/我們/你」現代科幻宗教獨白。**預設 B (v3)**。

### B#1 · `TELL_US_ABOUT_WORLD` · 🟠 shipped 文言 8 處 → v3 全清

**英文原文**:
> Your suggestion is appropriate.
> Acceptable new worlds are a priority for the rapid and complete spread of Juffo-Wup.
> We wish to know more for our suitability assessment.
> Tell us of this world.

**Shipped v0.5.2**:
> 汝之建議適宜。
> 可接受之新世界，乃 聖源 迅速且完整散布之要務。
> 吾等欲得知更多，以進行適宜性評估。
> 告知吾等此世界之事。

**Rebuild v3**:
> 你的提議合宜。
> 合適的新世界，是聖源迅速且完整散布的要務。
> 我們希望知道更多，以評估其適宜性。
> 告訴我們這個世界的事。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

### B#2 · `RAMBLE_7` · 🟠 shipped 文言 10 處 → v3 全清

**英文原文**:
> Pulsing hot liquid flows through my outstretched tendrils, sending thrills into my interior.
> The moment has come. I swell and burst.
> Above me a cloud of whispering life whirls through the air.
> I am content.

**Shipped v0.5.2**:
> 脈動之熱液流經吾伸展之觸鬚，將戰慄送入吾之內裡。
> 時刻已至。 吾腫脹並炸裂。
> 吾之上方，一團耳語之新生於空中盤旋。
> 吾滿足。

**Rebuild v3**:
> 脈動的熱液流經我伸展的觸鬚，將戰慄送入我的內裡。
> 時刻已至。 我腫脹，然後迸裂。
> 在我上方，一團耳語的新生於空中盤旋。
> 我感到滿足。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

### B#3 · `RAMBLE_9` · 🟠 shipped 文言 11 處 → v3 全清

**英文原文**:
> Your simple sexual process produces random mosaics of genetic instructions
> yet with the simplicity of breath, I modify my own patterns.
> You humans improve a tool and double your capabilities.
> We Mycon improve ourselves and increase a thousand-fold.

**Shipped v0.5.2**:
> 汝簡陋之性交過程僅生出遺傳指令之隨機拼貼
> 然而，如呼吸般簡便，吾修改吾自身之樣式。
> 汝人類改良一件工具而使汝之能力加倍。
> 吾等麥孔改良吾等自身，而增益千倍。

**Rebuild v3**:
> 你們簡陋的有性生殖，只產出遺傳指令的隨機拼貼
> 而我，如呼吸般輕易，便能修改自身的樣式。
> 你們人類改良一件工具，能力便加倍。
> 我們麥孔改良自身，增益千倍。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

### B#4 · `RAMBLE_11` · 🟠 shipped 文言 10 處 → v3 全清

**英文原文**:
> I have chosen my offsprings' memories carefully from my set of remembrances
> the sweet and warm times of my existence and those of my parents' parents' parents
> the bits of a million lifetimes coalesced into a birth gift of complete awareness.

**Shipped v0.5.2**:
> 吾已由吾眾多回憶中細心擇取吾子代之記憶
> 吾存在之甜美溫暖時光，以及吾親之親之親之時光
> 百萬生涯之片段，融合為一份完全覺知之出生贈禮。

**Rebuild v3**:
> 我已從我眾多的回憶中，細心挑選了給子代的記憶
> 我存在的甜美溫暖時光，以及我祖輩之祖輩之祖輩的時光
> 百萬生涯的片段，融合為一份完整覺知的出生贈禮。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

### B#5 · `HELLO_SPACE_1` · 🟠 shipped 文言 9 處 → v3 全清

**英文原文**:
> We are part of Juffo-Wup.
> Juffo-Wup is the hot light in the darkness.
> All else is unfulfilled Void.
> The source of Juffo-Wup is at <% comm.getPoint("629.1, 220.8", "mycon") %>.
> We are the Mycon.

**Shipped v0.5.2**:
> 吾等乃 聖源（Juffo-Wup） 之一部。
> 聖源 乃黑暗中之熱光。
> 餘皆未竟之虛空。
> 聖源 之源頭於 <% comm.getPoint("629.1, 220.8", "mycon") %>。
> 吾等乃麥孔。

**Rebuild v3**:
> 我們是聖源（Juffo-Wup）的一部分。
> 聖源，即黑暗中的熾光。
> 此外皆是未竟的虛空。
> 聖源的源頭，在 <% comm.getPoint("629.1, 220.8", "mycon") %>。
> 我們是麥孔族。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

### B#6 · `GENERAL_INFO_SUN_DEVICE` · 🟠 shipped 文言 15 處 → v3 全清

**英文原文**:
> Juffo-Wup is the power of life... hot warmth in the cold Void. 
> It flows through all things, binding them together, making them one.
> You are Non-Juffo-Wup, you cannot understand.
> Below is the pod of Juffo-Wup -- there for a thousand centuries.
> When we are cold, the pod opens and warms us.
> When it is dark, the pod clenches and lo, there is light.
> You are the Non. The pod is not for you. You must leave.

**Shipped v0.5.2**:
> 聖源 乃生命之力……冷虛空中之熱暖。
> 其流經萬物，將其等結合，使之為一。
> 汝乃非 聖源，汝不能理解。
> 下方乃 聖源 之莢 —— 於彼處已千個世紀。
> 當吾等寒冷時，莢張啟，暖吾等。
> 當黑暗時，莢緊縮，觀之，光明現。
> 汝即異類。 莢非為汝設。 汝必須離去。

**Rebuild v3**:
> 聖源即生命的力量……冰冷虛空中的熾熱。
> 它流經萬物，將它們繫結，融為一體。
> 你是非聖源者（Non-Juffo-Wup），你無法理解。
> 下方是聖源的莢——已在此地千個世紀。
> 當我們寒冷時，莢張開，溫暖我們。
> 當黑暗降臨時，莢緊縮，看啊，光便現身。
> 你即異類。 這莢不是為你設的。 你必須離去。

**推薦**: 🎯 **B (v3)** — v0.7 文言廢除政策

---

## C · 🟠 markdown `**` icon 清除 (1 tokens)

**規則**：UQM 引擎不渲染 markdown，會字面顯示星號。v3 改短句斷句 icon 對應原文 CAPS 強調。**預設 B (v3)**。

### C#1 · `NEVER_LET_LAND` · 🟠 `**` markdown → 短句斷句

**英文原文**:
> Juffo-Wup flows through Time and Space. It cannot be stopped by mere energy blasts.
> However, you are Non -- not part of Juffo-Wup.
> You CAN be destroyed by energy blasts.
> Let us demonstrate.

**Shipped v0.5.2**:
> 聖源 流經時間與空間。 其不能為單純之能量爆擊所阻。
> 然而，汝乃異類 —— 非 聖源 之一部。
> 汝**可**被能量爆擊所毀滅。
> 讓吾等示範。

**Rebuild v3**:
> 聖源流經時間與空間。 它不能被單純的能量爆擊所阻擋。
> 然而，你是異類——不是聖源的一部分。
> 但你不同。 你能被能量爆擊摧毀。
> 讓我們示範。

**推薦**: 🎯 **B (v3)** — Q15=A 短句斷句取代 markdown 粗體 (Alien_Speech §1.6)

---

## D · 🟡 微調 (措辭等價 · shipped 輕度文言 → v3 白話 · 54 tokens)

**規則**：這些 tokens shipped 文言程度輕，主要是 v0.7 用「你/我們」取代「汝/吾等」+ 微調用字。**預設 B (v3)**。

| # | Token | Shipped 摘要 | v3 摘要 | 差異類型 |
|---|---|---|---|---|
| D#1 | `BYE_AND_DIE_HOMEWORLD` | 汝阻礙 聖源 於宇宙之流動。 吾等現將清除此淤塞。 吾等現將藉除去汝以助 聖源！ | 你阻礙了聖源在宇宙間的流動。 我們現在就要清除這個阻塞。 我們現在就要協助聖源，消滅你！ | 文言 5 處清除 |
| D#2 | `RAMBLE_1` | 一顆孢子降落，於朽爛中尋得養分，並很快臻於成熟…… 其復吐出新生之雲，一千顆孢子，各自降落，於朽爛中尋得養分 … | 一枚孢子降落，在腐朽中尋得養分，很快便長至成熟…… 接著，它吐出一朵新生命的雲霧，一千枚孢子，各自降落，在腐朽… | 文言 1 處清除 |
| D#3 | `RAMBLE_2` | 吾等之軀體因基因之熱情而沸騰。 汝一族千人所擁之豐美，不及吾一顆細胞。 | 我們的軀體，因基因的熱情而沸騰。 你們一族一千個個體，也不及我一顆細胞裡的豐盈。 | 文言 6 處清除 |
| D#4 | `RAMBLE_3` | 吾充盈於吾親之親之親之親之親。 吾即彼等 —— 而彼等即吾等。 昔時，與此刻。 | 我盈滿於我的祖輩之祖輩之祖輩之祖輩之祖輩。 我即他們——他們即我們。 彼時，此時。 | 文言 4 處清除 |
| D#5 | `RAMBLE_5` | 吾乃杜奇（Dugee） 吾乃純度監督者 吾抉擇何芽准予成熟 何者則必當根除。 吾於五萬七千二百八十三年前因一般… | 我是杜奇（Dugee） 我是純度監控者 我選擇哪些芽苞得以成熟 哪些必須根除。 我於 57,283 年前因總體… | 文言 6 處清除 |
| D#6 | `RAMBLE_6` | 一顆冷石，於虛空中無聲旋轉，一具子代之胎宮。 | 一顆冷石，在虛空中無聲旋轉，一具幼體的胎宮。 | 文言 1 處清除 |
| D#7 | `RAMBLE_8` | 聖源 於此地強盛。 | 聖源，在此地強盛。 | 措辭微調 |
| D#8 | `RAMBLE_12` | 於黑暗中彼等生長，深處之火滋養子代。 彼等之出生，將溫暖吹散於一冷世界之上。 | 他們在黑暗中生長，深處的火焰滋養著幼體。 他們的誕生，為冷寂的世界吹入溫暖。 | 文言 3 處清除 |
| D#9 | `RAMBLE_13` | 『……系統需要更多能量。 一便利之源頭位於地殼之下……』 | 『……系統需要更多能量。 一處便利的來源，就在地殼下方……』 | 文言 2 處清除 |
| D#10 | `RAMBLE_14` | 吾等仰仗 聖源 以求方向，而其提供了樣式 無盡之擴張，伴以純淨之成就，並對錯誤絕不容忍。 | 我們仰望聖源以求方向，它便提供了樣式 無盡的擴張，伴隨純粹的成就，對錯誤絕不容忍。 | 文言 3 處清除 |
| D#11 | `RAMBLE_15` | 吾乃舒洛許（Shloosh） 吾於一萬四千地球年前遭焚毀 吾如今存活，僅一瞬之久 然後，吾便消逝。 | 我是舒洛許（Shloosh） 我於一萬四千地球年前被焚化 我此刻活著，僅為一瞬 而後，我便消逝。 | 文言 6 處清除 |
| D#12 | `RAMBLE_16` | 『……納入緻密之角閃石纖維，確保於環境極端下之生存……』 | 『……納入緻密的角閃石纖維，確保於極端環境中存續……』 | 文言 2 處清除 |
| D#13 | `RAMBLE_17` | 吾渴慕岩漿 流動之溫暖玄武岩 熔岩池之赤紅光焰。 | 我渴望岩漿 流動溫熱的玄武岩 熔岩池赤紅的光焰。 | 文言 3 處清除 |
| D#14 | `RAMBLE_18` | 當吾等遇到異類時，吾等必須吸納此異類，或拒斥此異類，使其不再為異類。 | 當我們遭遇異類時，我們必須吸納此異類，或拒斥此異類，使其不再是異類。 | 文言 2 處清除 |
| D#15 | `RAMBLE_19` | 『……噪訊進入訊號無可避免。 吾等必須包含一過濾機制……』 | 『……噪訊進入訊號無可避免。 我們必須納入一過濾機制……』 | 文言 1 處清除 |
| D#16 | `RAMBLE_20` | 個體之停止無可避免 乃存在之後果 然隨新生命之誕生，個體性得部分傳承 偶有機會於一段間隔中取得主導 達成某種共… | 個體的終止無可避免 這是存在的必然結果 然而，隨著新生命的誕生，個體性得以部分傳承 偶爾能於一段間隔中取得主導… | 文言 4 處清除 |
| D#17 | `RAMBLE_21` | 『……生存乃要務。 擴張乃要務。 處理乃要務……』 | 『……生存是要務。 擴張是要務。 處理是要務……』 | 文言 3 處清除 |
| D#18 | `RAMBLE_22` | 聖源 承認無法虛化之異類之存在 當吾等面對此等時，吾等結合、吸納，並等待吾等之機會 以習得其弱點，藉此化異類為… | 聖源亦承認，有些異類是無法虛化的。 當我們面對此類時，我們結合、吸納，並等待機會 以習得其弱點，藉此將異類化為… | 文言 6 處清除 |
| D#19 | `RAMBLE_23` | 有時，吾遇一他者，其於心中與吾共享某親之生命 若吾等言談，此片段便於吾等雙方皆佔主導 而自我與自我相會，偶而生… | 有時，我遇到另一者，他在心中與我共享某位親輩的生命 若我們交談，這個片段便在雙方心中佔據主導 自我與自我相會，… | 文言 5 處清除 |
| D#20 | `RAMBLE_24` | 莢艦以電漿封存場而嗡鳴 其子嗣尋求化異類為虛空 場域漸緊，愈緊 產生器之低頻轟隆漸升為高頻燃燒之尖嘯 忽然之靜… | 莢艦因電漿封存場而嗡鳴 它們的子嗣，尋求將異類轉為虛空 場域漸漸繃緊，越來越緊 產生器的低頻轟鳴，逐漸升為燃燒… | 文言 4 處清除 |
| D#21 | `RAMBLE_26` | 『……觀察……思考……行動……觀察……學習……記憶……傳授……重複……』 | 『……觀察……思考……行動……觀察……學習……記憶……教授……重複……』 | 措辭微調 |
| D#22 | `RAMBLE_27` | 植入艦隊已於綠色世界之上軌道集結 脆弱之樣式揭示引入之點。 子代已為其出生之旅備妥。 釋放！ | 植入艦隊已於綠色世界上方的軌道集結 脆弱處的樣式，揭示了引入的地點。 幼體已為它的孵化之旅做好準備。 釋放！ | 文言 3 處清除 |
| D#23 | `RAMBLE_30` | 黑暗即虛空 聖源 即光。 | 黑暗即虛空 聖源即光。 | 措辭微調 |
| D#24 | `RAMBLE_31` | 『……行星改造生物體 94-18：至傳送台就汝之位……』 | 『……行星改造生物體 94-18：至傳送台，就位……』 | 文言 2 處清除 |
| D#25 | `RAMBLE_32` | 汝即異類。 汝必須走，且永不歸來。 | 你即異類。 你必須離去，永不返回。 | 文言 2 處清除 |
| D#26 | `BYE_AND_DIE_SPACE` | 聖源 充盈吾之纖維，吾脹滿。 暴力之舉隨之而至。 | 聖源充盈於我的纖維，我腫脹起來。 暴力隨之而至。 | 文言 4 處清除 |
| D#27 | `HELLO_HOMEWORLD_1` | 聖源（Juffo-Wup） 即一切…… 全然存在，散布並將異類轉化為 聖源。 汝即異類，必須成為 聖源，或化為… | 聖源（Juffo-Wup）即一切……無所不在，散布著，將異類轉化為聖源。 你即異類，必須成為聖源，或化為虛空。… | 文言 6 處清除 |
| D#28 | `HELLO_HOMEWORLD_2` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#29 | `HELLO_HOMEWORLD_3` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#30 | `HELLO_HOMEWORLD_4` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#31 | `HELLO_HOMEWORLD_5` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#32 | `HELLO_HOMEWORLD_6` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#33 | `HELLO_HOMEWORLD_7` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#34 | `HELLO_HOMEWORLD_8` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#35 | `HELLO_SPACE_2` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#36 | `HELLO_SPACE_3` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#37 | `HELLO_SPACE_4` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#38 | `HELLO_SPACE_5` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#39 | `HELLO_SPACE_6` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#40 | `HELLO_SPACE_7` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#41 | `HELLO_SPACE_8` | 吾等乃麥孔。 | 我們是麥孔族。 | 文言 2 處清除 |
| D#42 | `GOODBYE_SUN_DEVICE` | 離開吾等之聖地。 | 離開我們的聖地。 | 文言 2 處清除 |
| D#43 | `RESPONSE_1` | 此為善。 | 甚好。 | 措辭微調 |
| D#44 | `RESPONSE_2` | 此為善。 | 甚好。 | 措辭微調 |
| D#45 | `RESPONSE_3` | 此為善。 | 甚好。 | 措辭微調 |
| D#46 | `clue_2` | 豐盛之生命覆蓋其表面。 | 豐盛的生命覆蓋其表面。 | 文言 1 處清除 |
| D#47 | `what_about_shattered` | 為何「碎裂世界群」只出現在你們的星域？ | 為何「碎裂世界」只出現在你們的星域？ | 措辭微調 |
| D#48 | `HELLO_SUN_DEVICE_WORLD_1` | 此乃聖地 充盈於 聖源。 然此非源頭。 聖源 湧自 <% comm.getPoint("629.1, 220.… | 這是聖地 充盈著聖源。 但這裡不是源頭。 聖源湧自 <% comm.getPoint("629.1, 220.… | 文言 3 處清除 |
| D#49 | `HELLO_SUN_DEVICE_WORLD_2` | 汝已返回吾等之聖地。 此不可容。 離去。 | 你返回了我們的聖地。 這不被允許。 離去。 | 文言 3 處清除 |
| D#50 | `DIE_LIAR` | 汝乃 聖源 之障礙。 汝必須被除去。 | 你是聖源的障礙。 你必須被清除。 | 文言 4 處清除 |
| D#51 | `DIE_THIEF` | 汝已自吾等取走某物，其為吾等所重視 某物對 聖源 為要緊。 吾等要求恆星操控器。 吾等現將自汝手中奪回！ | 你自我們手中取走了我們所重視的東西 某樣對聖源至關重要的東西。 我們需要恆星操控器。 我們現在就要從你手中奪回… | 文言 6 處清除 |
| D#52 | `DIE_THIEF_AGAIN` | 汝已自吾等取走某物，其為吾等所重視……其對 聖源 為要緊。 立即歸還恆星操控器。 | 你自我們手中取走了我們所重視的東西……那對聖源至關重要。 立即歸還恆星操控器。 | 文言 3 處清除 |
| D#53 | `GOODBYE_AND_DIE` | 聖源 即一切 然汝非 聖源 之一部 是故汝必須止其存在。 吾等將使汝停止存在，為 聖源。 | 聖源即一切 但你不是聖源的一部分 因此你必須停止存在。 我們將使你停止存在，為了聖源。 | 文言 5 處清除 |
| D#54 | `WONT_FALL_FOR_TRICK` | 吾等不解讀 聖源 之意志。 唯源頭具此權能。 除非另有指示，聖源 要求吾等留於此處。 | 我們不解讀聖源的意志。 唯有源頭具有此權能。 除非另有指示，聖源要求我們留在此地。 | 文言 3 處清除 |

**推薦**: 🎯 **B (v3) 全部** — Q10=A/Q11=A 廢除文言助詞政策

---

## E · 🟢 完全相同 (39 tokens · 保留 shipped · 無需決策)

多為玩家 response (Q12=A 保留 shipped 微調) + `We are the Mycon` 重複 + RESPONSE_1-3 + AMBUSH_TAIL/RAMBLE_TAIL 靜默 token。

- **AMBUSH_TAIL**: `AMBUSH_TAIL`
- **RAMBLE_TAIL**: `RAMBLE_TAIL`
- **bye_homeworld**: `bye_homeworld`
- **bye_space**: `bye_space`
- **bye_sun_device**: `bye_sun_device`
- **came_to_homeworld**: `came_to_homeworld`
- **clue**: `clue_1`, `clue_3`
- **come_in_peace**: `come_in_peace`
- **gonna_die**: `gonna_die`
- **how_goes_implanting**: `how_goes_implanting`
- **insult**: `insult_1`, `insult_2`, `insult_3`, `insult_4`, `insult_5`, `insult_6`, `insult_7`, `insult_8`
- **lets_be_friends**: `lets_be_friends`
- **like_to_land**: `like_to_land`
- **question**: `question_1`, `question_2`, `question_3`, `question_4`, `question_5`, `question_6`, `question_7`, `question_8`, `question_9`, `question_10`, `question_11`, `question_12`, `question_13`, `question_14`, `question_15`, `question_16`
- **submit_to_us**: `submit_to_us`
- **whats_up_sun_device**: `whats_up_sun_device`

---

## 決策快答

**若全依推薦（推薦）**：
```
全 B
```

**若逐項調整**：
```
A#3=A  B#5=A  C#2=A  D#7=A ...
```

**替代選項**：
- **A** = shipped v0.5.2 保留
- **B** = Rebuild v3 (推薦)
- **C** = 自訂（請提具體 token 措辭）