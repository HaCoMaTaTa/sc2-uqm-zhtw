# Ur-Quan Kohr-Ah Rebuild-Compare Diff Report (2026-08-16 · v0.7 v3.1 clean-room)

**族**：`kohrah` (Ur-Quan Kohr-Ah)
**檔案**：`uqm-work/translations/kohrah.zh-TW.json` (shipped v0.4.14c++, 76 tokens)
**v3.1**：`uqm-work/translations/kohrah.zh-TW.v3.json` (clean-room · Dossier v0.7 A 案極簡冷酷宣告體 · 使用者審視後直譯修訂)
**規模**：76 tokens · shipped 17,464 bytes · v3.1 ~18 KB
**3-gate**：purity=0 (race/simp/variant) · Lua=0 · line-count=76/76 ✅
**Backup**：`uqm-work/translations/kohrah.zh-TW.pre-rebuild.bak`

**v3.1 revision（2026-08-16 使用者審視後追加）**：
- 使用者指出 #1/#2 直譯痕跡明顯 · 全檔掃描發現 18 處直譯（涵蓋 22 tokens）· 全採 v3.1 修訂
- 主要類型：`What is/It is + 抽象名詞` 直搬 · apposition 直搬 · 名詞化直搬（life forms/efforts to resist）· 「群星之界／在此／奉上／速決而無血」書面過度
- 修訂範圍：why_kill_all_1/2/3 · HELLO_AND_DIE_2/4-8 · HELLO_SAMATRA · WE_KILL_ALL_1 · KILL_BECAUSE_1 · WILL_KILL_2/4 · WE_WERE_SLAVES · WE_ARE_URQUAN_TOO · BONE_GARDENS · YOU_DIE · THEN_DIE · PLEADING_IS_USELESS_1/4 · GAME_OVER_DUDE
- Voice 保持不變（判決書口吻／冷酷／短句／現代白話），僅去除英文語序直搬痕跡

---

## 統計

| 類別 | 數量 | 占比 |
|---|---|---|
| 🟢 完全相同 | 17 | 22% |
| 🟡 微調（等價） | 15 | 20% |
| 🟠 措辭改變（去文言污染 + dossier icon 採用） | 35 | 46% |
| 🔴 語意/voice 差異大 | 0 | 0% |
| ✨ v0.5.2 canonical 升級（+ 措辭改變） | 9 | 12% |

**污染統計對照**：

| 項目 | shipped | v3 | 削減 |
|---|---|---|---|
| 吾 | 9 | 0 | -100% |
| 爾 | 80 | 1 (卓爾族 canonical race name) | -99% |
| 之（文言助詞） | 131 | 0（保留 24 現代固定詞：現在與永恆之道 / 儀式之戰 / 之後 / 之前 / 之時 / 之一 / 心靈之力 等）| -100% |
| 乃 | 17 | 0 | -100% |
| 哉 | 2 | 0 | -100% |
| 爾等 | 5 | 0 | -100% |
| **合計文言助詞** | **244** | **0** | **-100%** |

**Canonical 保留**（未新增，皆繼承 shipped）：柯亞 / 克澤札 / 烏寬 / 塔洛族 / 蟾亞 / 會話寵 / 尤利族 / 卓爾族 / 苦刑器 / 骨骸坑 / 執行者 / 綠烏寬 / 黑烏寬 / 頹靡的科學家 / 官僚 / 教義戰爭 / 永恆教條

**新採用 canonical**（Master_Glossary v0.2/v0.5.2 對齊 · 與 Kzer-Za v3 一致）：
- **感知聯盟**（Sentient Milieu · shipped「意識邦聯」× 3 tokens）
- **梅努族**（Mael-Num · shipped「邁爾努族」× 1 token）
- **現在與永恆之道**（Path of Now and Forever · shipped「今與永恆之道」× 4 tokens）
- **薩瑪特拉**（Sa-Matra · shipped「薩-瑪特拉」× 3 tokens · 與 Kzer-Za v3 一致無破折號）

**廢除**（Q5=A · dossier §四 明令）：
- **「永恆教條之執行者」** headline（KILL_BECAUSE_2 · dossier §四 明列 ❌ 過度冗長）
- **「淨化者」** 精簡至 1 場（HELLO_AND_DIE_1 首場儀式點綴，廢除 shipped 其他 3 tokens 過度插入）

---

## 🟢 完全相同（17 tokens · 不列細節）

`why_kill_all_2` · `why_kill_all_4` · `please_dont_kill_1` · `please_dont_kill_2` · `please_dont_kill_3` · `bye_frenzy_1` · `bye_frenzy_2` · `bye_frenzy_3` · `bye_frenzy_4` · `threat_4` · `relationship_with_urquan` · `what_are_you_hovering_over` · `you_sure_are_creepy` · `stop_that_gross_blinking` · `plead_1` · `plead_2` · `plead_4` · `bye`

（皆為玩家 response 短句、簡潔詞句，與 shipped 完全一致）

---

## 🟡 微調（15 tokens · 等價替換 · 預設 A shipped）

### #1 · `why_kill_all_1` · 🟡
- EN: `What is this madness!? Why are you trying to kill everyone?`
- Shipped：`這是什麼瘋狂？！ 你們為何要屠殺所有人？`
- v3：`這是什麼瘋狂？！ 你們為什麼要殺光所有人？`
- 差異：「為何」→「為什麼」（更口語）· 「屠殺」→「殺光」（更口語）
- 推薦：🟡 **A**（shipped「為何」「屠殺」語氣更急促合玩家反應）
- 選擇：A / B

### #2 · `why_kill_all_3` · 🟡
- EN: `What has made you this way? It is insane!`
- Shipped：`是什麼讓你們變成這樣的？ 這是瘋了！`
- v3：`是什麼讓你們變成這樣？ 這是瘋狂！`
- 差異：「這樣的」→「這樣」· 「瘋了」→「瘋狂」
- 推薦：🟡 **A**（等價 · shipped 「瘋了」更符玩家口語感）
- 選擇：A / B

### #3 · `please_dont_kill_4` · 🟡
- EN: `Is there anything we can do to make you stop the killing?`
- Shipped：`我方有沒有什麼辦法能讓你們停止殺戮？`
- v3：`我方有什麼辦法能讓你們停止殺戮嗎？`
- 差異：「有沒有」→「有...嗎」（等價）
- 推薦：🟡 **A**（等價）
- 選擇：A / B

### #4 · `threat_1` · 🟡
- EN: `If you attack us, we will destroy you. Don't even try it.`
- Shipped：`如果你們攻擊我方，我方將摧毀你們。 想都別想。`
- v3：`如果你們攻擊我方，我方會摧毀你們。 想都別想。`
- 差異：「將」→「會」
- 推薦：🟡 **A**（EN `will` 對「將」更精確）
- 選擇：A / B

### #5 · `threat_3` · 🟡
- EN: `You have attacked us before, and we survived! You cannot defeat us. Submit!`
- Shipped：`你們以前攻擊過我方，我方倖存了！ 你們無法擊敗我方。 投降！`
- v3：`你們以前攻擊過我方，我方倖存了！ 你們無法擊敗我方。 投降吧！`
- 差異：末尾加「吧」
- 推薦：🟡 **A**（EN `Submit!` 命令句無語氣詞 · shipped 更貼原文）
- 選擇：A / B

### #6 · `key_phrase` · 🟡
- EN: `Hold! What you are doing to us is wrong! Why do you do this thing?`
- Shipped：`住手！ 你們對我方所做的是錯的！ 為何為此？`
- v3：`住手！ 你們對我方所做的是錯的！ 為何要這麼做？`
- 差異：「為何為此」→「為何要這麼做」（EN `Why do you do this thing?` 完整句 · shipped 過簡）
- 推薦：🟠 **B**（v3 完整對應 EN · 觸發 key phrase 需明確重複「這件事」呼應 THEN_DIE `Your words, 'Why do you do this thing?'`）
- 選擇：A / B

### #7 · `why_do_you_destroy` · 🟡
- EN: `Kohr-Ah, tell us about yourselves.`
- Shipped：`柯亞族，說說你們自己吧。`
- v3：`柯亞，跟我方說說你們自己。`
- 差異：「柯亞族」→「柯亞」（EN `Kohr-Ah` 直呼族名，v3 更精確）· 加「跟我方」
- 推薦：🟡 **A**（shipped「柯亞族」更完整不易誤讀 · 「說說...吧」更自然口語）
- 選擇：A / B

### #8 · `what_about_culture` · 🟡
- EN: `Who or what are the Dnyarri?`
- Shipped：`蟾亞族是誰？ 或是什麼？`
- v3：`蟾亞是誰？ 或是什麼？`
- 差異：「蟾亞族」→「蟾亞」（EN 只有 `Dnyarri` 無 "race"，v3 精確）
- 推薦：🟡 **A**（shipped 「族」字更清晰指涉種族實體，語順更自然）
- 選擇：A / B

### #9 · `how_leave_me_alone` · 🟡
- EN: `How did you defeat the Dnyarri?`
- Shipped：`你們是如何擊敗蟾亞族的？`
- v3：`你們是如何擊敗蟾亞的？`
- 差異：同上（「蟾亞族」→「蟾亞」）
- 推薦：🟡 **A**（同 #8 理由）
- 選擇：A / B

### #10 · `guess_thats_all` · 🟡
- EN: `I guess that's it. Thanks for the info. We'll just leave now.`
- Shipped：`我猜就這樣了。 感謝你們告訴我方。 我方現在就離開。`
- v3：`我猜就這樣了。 感謝你們的說明。 我方現在就離開。`
- 差異：「告訴我方」→「的說明」
- 推薦：🟡 **A**（shipped 更貼玩家口吻 · 「告訴」動作感更強）
- 選擇：A / B

### #11 · `plead_3` · 🟡
- EN: `What if we promise to be your slaves? Will you let us live then?`
- Shipped：`要不我方保證做你們的奴隸？ 那樣你們會讓我方活嗎？`
- v3：`要不我方答應做你們的奴隸？ 那樣你們會讓我方活嗎？`
- 差異：「保證」→「答應」
- 推薦：🟡 **A**（EN `promise` 對「保證」更精確）
- 選擇：A / B

### #12 · `WE_KILL_ALL_2` · 🟡
- EN: `We are the Ur-Quan Kohr-Ah.\nPrepare for the cleansing.`
- Shipped：`我等乃烏寬柯亞族。\n預備接受淨化。`
- v3：`我族即烏寬柯亞。\n準備接受淨化。`
- 差異：「我等乃」→「我族即」（去文言 · Q2=C）· 「烏寬柯亞族」→「烏寬柯亞」（EN 無 "race"）· 「預備」→「準備」（現代標準）
- 推薦：🟠 **B**（v3 · Q2=C 我族 + Q3=A 去文言 · 「準備」= 現代標準）
- 選擇：A / B

### #13 · `WE_KILL_ALL_3` · 🟡
- 同 #12（三 tokens 完全重複，EN 一致）
- 推薦：🟠 **B**
- 選擇：A / B

### #14 · `WE_KILL_ALL_4` · 🟡
- 同 #12
- 推薦：🟠 **B**
- 選擇：A / B

### #15 · `RESISTANCE_IS_USELESS_2` · 🟡
- EN: `It is not.`
- Shipped：`非也。`
- v3：`並非如此。`
- 差異：「非也」（文言）→「並非如此」（現代）
- 推薦：🟠 **B**（v3 · 「非也」是文言 Q3=A 廢除）
- 選擇：A / B

---

## 🟠 措辭改變（35 tokens · 大多為去文言 + dossier §六 icon 採用）

### #16 · `SENSE_EVIL` · 🟠
- EN: `We sense... something... something ancient... a sickly smell... a chilling wind.\nMy ancestors scream from within their chambers in my mind\nbut I cannot understand their words.\nThis feeling... a memory? It sickens us, and for the first time in our lives\nfor the first time in generations\nWe fear.`
- Shipped：`我等感應到… 某物… 某物古老… 一股病態氣息… 一股寒風。\n吾先祖自吾心之殿堂尖嚎\n然吾不能解其語。\n此感… 是記憶？ 令我等作嘔，而生平第一次\n數代以來第一次\n我等，感到恐懼。`
- v3：`我族感應到…… 某種東西…… 某種古老的東西…… 一股病態的氣息…… 一陣寒風。\n我的先祖，在我心中的殿堂內尖嚎——\n但我無法理解他們的話語。\n這感覺…… 是記憶？ 讓我族作嘔——而此生第一次——\n數代以來第一次——\n我族，感到恐懼。`
- 差異分析：
  - `We sense` → 我族（正確 · 集體感應）
  - `My ancestors ... my mind` → **個體「我的先祖／我心中」**（Q2=C · EN 是 my/I 單數，唯一情緒段個體視角）
  - `us / our lives / We` → 集體（我族／此生）
  - shipped 全用「吾」「吾等」文言 → v3 全清除
- 推薦：🟠 **B**（v3 · Q2=C 個體「我」保 EN 單數 · 全面去文言）
- 選擇：A / B

### #17 · `HELLO_AND_DIE_1` · 🟠
- EN: `We are the Ur-Quan Kohr-Ah.\nWe cleanse our destiny.\nYou will soon die.\nMake whatever rituals are necessary for your species.`
- Shipped：`我等乃烏寬柯亞族（Ur-Quan Kohr-Ah），淨化者。\n淨化，即我等之天命。\n爾之死即臨。\n爾族有何必要儀式，請即舉行。`
- v3：`我族即烏寬柯亞——淨化者。\n我族淨化——即我族的宿命。\n你即將死亡。\n為你的族群舉行任何必要的儀式。`
- 差異分析：
  - **儀式化「淨化者」保留**（Q2=C · dossier §四 允許罕見儀式段 · 僅此一場）
  - `We cleanse our destiny` → 我族淨化——即我族的宿命（保 EN 對句判決節奏）
  - `You will soon die.` → 你即將死亡（現代白話 · 廢除「爾之死即臨」文言）
- 推薦：🟠 **B**
- 選擇：A / B

### #18 · `HELLO_AND_DIE_2` · ✨（薩瑪特拉 canonical）
- EN: `We are the Ur-Quan Kohr-Ah.\nYour presence here is premature.\nWe fight the Kzer-Za for supremacy of Doctrine\nand possession of the Sa-Matra.\nWhen the battle is won, our task is simple.\nWe cleanse. You are the filth.`
- Shipped：`我等乃烏寬柯亞族。\n爾出現於此為時尚早。\n我等正與克澤札族進行教條之爭\n以及薩-瑪特拉之爭奪。\n戰勝之時，我等之任務簡單。\n我等淨化。 爾等即穢物。`
- v3：`我族即烏寬柯亞。\n你出現在此，時機尚早。\n我族正與克澤札交戰——爭奪教義的主宰\n以及薩瑪特拉的掌控權。\n戰勝之後，我族的任務簡單。\n我族淨化。 你就是污穢。`
- 差異分析：
  - ✨ **薩-瑪特拉** → **薩瑪特拉**（v0.5.2 canonical · 與 Kzer-Za v3 一致）
  - `filth` → **污穢**（Kohr-Ah 招牌 · shipped「穢物」保留原意但 dossier canonical 為「污穢」）
  - dossier §六 例 3 對句「我族淨化。 你就是污穢。」= 招牌 icon
- 推薦：✨ **B**（v3 · canonical + dossier §六 對句 icon）
- 選擇：A / B

### #19 · `HELLO_AND_DIE_3` · 🟠
- EN: `We are the Ur-Quan Kohr-Ah.\nYou have evaded our attempts to cleanse.\nYou are no longer filth. You are a threat.\nThreats deserve greater attention than filth.`
- Shipped：`我等乃烏寬柯亞族。\n爾已閃避我等之淨化嘗試。\n爾已不再是穢物。 爾為威脅。\n威脅比穢物更值得關注。`
- v3：`我族即烏寬柯亞。\n你已規避我族的淨化行動。\n你不再是污穢。 你是威脅。\n威脅比污穢更值得關注。`
- 差異分析：
  - shipped 全用「爾」「之」文言 → v3 全清除
  - `filth → 穢物` → **污穢**（canonical 統一）
  - dossier §四 明列「You are no longer filth. You are a threat.」為升級 icon
- 推薦：🟠 **B**
- 選擇：A / B

### #20 · `HELLO_AND_DIE_4` · 🟠
- EN: `We are the Ur-Quan Kohr-Ah.\nOur nature, the fulfillment of our fate\nrequires your destruction.`
- Shipped：`我等乃烏寬柯亞族。\n我等本質，我等命運之實現\n要求爾之毀滅。`
- v3：`我族即烏寬柯亞。\n我族的本質——我族命運的實現——\n需要你的毀滅。`
- 差異分析：
  - 「乃」「之」全清除
  - `requires` → 需要（v3 更精確 · 「要求」有命令感，v3 保留判決宿命感）
- 推薦：🟠 **B**
- 選擇：A / B

### #21-25 · `HELLO_AND_DIE_5` / `_6` / `_7` / `_8` · 🟠
- EN 5 tokens identical to #4 (`HELLO_AND_DIE_4-8` 完全重複)
- shipped/v3 完全同 #20
- 推薦：🟠 **B**（統一同 #20 · dossier B 決策自動延伸）
- 選擇：A / B（一次決策 5 tokens 一致）

（合併為 4 tokens：`HELLO_AND_DIE_5`, `_6`, `_7`, `_8`）

### #22 · `HELLO_SAMATRA` · ✨（薩瑪特拉 canonical + dossier §六 例 5）
- EN: `FILTH! YOU may NOT approach the Sa-Matra.\nYour death was inevitable, but now it is also imminent.`
- Shipped：`穢物！ 爾不可接近薩-瑪特拉。\n爾之死本即無可避免，如今更是迫在眉睫。`
- v3：`污穢！ 你，不得，靠近薩瑪特拉！！\n你的死亡本就無可避免——但現在，也已迫在眉睫！`
- 差異分析：
  - ✨ **薩-瑪特拉** → **薩瑪特拉** canonical
  - **穢物** → **污穢** canonical
  - **CAPS icon**（Q1=D · dossier §六 例 5）：
    - `FILTH!` → 「污穢！」+ 感嘆號適量
    - `YOU may NOT` → 「你，不得，」（三段斷句強調）
    - `Sa-Matra.` → 「薩瑪特拉！！」（雙感嘆號比 EN 更強調 · dossier §六 例 5 canonical）
  - shipped「爾之死本即」文言 → v3「你的死亡本就」現代
- 推薦：✨ **B**（v3 · dossier §六 例 5 canonical 招牌 icon）
- 選擇：A / B

### #23 · `WE_KILL_ALL_1` · ✨（現在與永恆之道 + 薩瑪特拉 canonical + Q5 廢除「淨化者」）
- EN: `We are the Ur-Quan Kohr-Ah.\nWe have won the ritual war against our cousins, the Kzer-Za.\nOur Doctrine, the Path of Now and Forever, shall be dominant\nuntil the Kzer-Za win such a war.\nWe now cleanse the Kzer-Za slave-races.\nThen we shall take possession of the Sa-Matra and move on\nto find new intelligence\nnew filth to cleanse.`
- Shipped：`我等乃烏寬柯亞族。\n我等已於儀式之戰中戰勝我等族兄克澤札。\n我等教條，今與永恆之道，將主宰\n直至克澤札贏得此類戰爭。\n我等淨化者現淨化克澤札之奴族。\n然後我等將接收薩-瑪特拉，繼續前進\n尋覓新的智慧\n新的穢物以淨化之。`
- v3：`我族即烏寬柯亞。\n我族已在儀式之戰中戰勝我族的灰色同胞——克澤札。\n我族的教義——現在與永恆之道——將成為主宰\n直至克澤札贏得下一場此類之戰。\n我族現在淨化克澤札的奴役族群。\n然後，我族將接管薩瑪特拉，繼續前進——\n去尋找新的智慧生命——\n新的、可供淨化的污穢。`
- 差異分析：
  - ✨ **今與永恆之道** → **現在與永恆之道** canonical (Master_Glossary v0.2)
  - ✨ **薩-瑪特拉** → **薩瑪特拉** canonical
  - Q5=A **廢除「淨化者」頭銜**（shipped「我等淨化者現淨化」→ v3「我族現在淨化」）
  - `our cousins, the Kzer-Za` → **灰色同胞——克澤札**（dossier §四 Kohr-Ah 對 Kzer-Za 稱謂 canonical，替換 shipped「族兄」）
- 推薦：✨ **B**
- 選擇：A / B

### #24 · `KILL_BECAUSE_1` · 🟠（dossier §六 例 1 招牌 icon）
- EN: `We do not kill. We cleanse.\nCleansing is necessary to ensure our eternal freedom and security.\nIndeed, you fail to understand: there is no death.\nOnly termination and rebirth.\nEach termination brings around the new chance\nthe possibility to be born an Ur-Quan.\nWe merely present this opportunity, make it available to all.`
- Shipped：`我等非殺戮。 我等淨化。\n淨化，乃保我等永恆自由與安全所必需。\n實情是，爾未能理解:並無死亡之事。\n只有終結與再生。\n每一次終結帶來新機\n重生為烏寬之可能。\n我等僅是提供此機遇，令其為眾人所可得。`
- v3：`我族不殺戮。 我族淨化。\n淨化，是確保我族永恆自由與安全所必需。\n的確，你未能理解：並無死亡這件事。\n只有終結與重生。\n每一次終結都帶來新的機會——\n以烏寬之身誕生的可能。\n我族僅是提供這個機會，讓所有人都能取得。`
- 差異分析：
  - **`We do not kill. We cleanse.`** → 「我族不殺戮。 我族淨化。」= **dossier §六 例 1 canonical 招牌 icon**（廢除 shipped「非殺戮」文言）
  - 全面去除「吾等」「乃」「爾」「之事」「機遇」文言
- 推薦：🟠 **B**（招牌 icon 直接採 dossier）
- 選擇：A / B

### #25 · `KILL_BECAUSE_2` · ✨（現在與永恆之道 canonical + Q5 廢除「執行者」）
- EN: `Our Path of Now and Forever is self-justifying, it needs no confirmation.\nWe cleanse. That is all. There is no more.`
- Shipped：`我等永恆教條之執行者，今與永恆之道自證其身，不需認可。\n我等淨化。 僅此而已。 別無其他。`
- v3：`我族的現在與永恆之道，不證自明——不需認可。\n我族淨化。 僅此而已。 別無其他。`
- 差異分析：
  - ✨ **今與永恆之道** → **現在與永恆之道** canonical
  - Q5=A **廢除「永恆教條之執行者」**（dossier §四 明列 ❌ 過度冗長、非原文語域）
  - 「自證其身」→「不證自明」（dossier §四 canonical 現代白話 · 例 `self-justifying → 不證自明`）
- 推薦：✨ **B**
- 選擇：A / B

### #26 · `KILL_BECAUSE_3` · 🟠
- EN: `You have not asked properly.\nIf you do not ask properly, we will not discuss this matter.\nInstead, we cleanse.`
- Shipped：`爾未以正確方式提問。\n若爾不以正確方式提問，我等不會討論此事。\n取而代之，我等淨化。`
- v3：`你的提問方式不正確。\n若你的提問方式不正確，我族將不討論此事。\n取而代之——我族淨化。`
- 差異：全面去「爾」「我等」文言 · 「不會」→「將不」（更冷酷正式）
- 推薦：🟠 **B**
- 選擇：A / B

### #27 · `KILL_BECAUSE_4` · 🟠
- EN: `Your understanding is not necessary.`
- Shipped：`爾之理解並非必要。`
- v3：`你的理解，並非必要。`
- 差異：「爾之」→「你的」+ 加逗號斷句（判決書節奏）
- 推薦：🟠 **B**
- 選擇：A / B

### #28 · `WILL_KILL_1` · 🟠（dossier §六 例 2 招牌 icon）
- EN: `We have listened. We are unmoved. The cleansing will proceed.`
- Shipped：`我等已聆聽。 我等不為所動。 淨化將繼續。`
- v3：`我族聽過了。 我族不動搖。 淨化將繼續進行。`
- 差異：dossier §六 例 2 canonical「我族聽過了。 我族不動搖。 淨化將繼續進行。」= 招牌 icon（判決書三段節奏）· shipped「已聆聽」較正式雅 · v3「聽過了」較口語判決
- 推薦：🟠 **B**（招牌 icon 直接採 dossier）
- 選擇：A / B

### #29 · `WILL_KILL_2` · 🟠
- EN: `The cleansing ensures our freedom and security.\nThreats to this freedom and security are confined to non-Ur-Quan intelligent life forms.\nTo preserve our freedom and security, we cleanse such threats.`
- Shipped：`淨化確保我等之自由與安全。\n對此自由與安全之威脅，僅限於非烏寬的智慧生命形式。\n為保全我等之自由與安全，我等淨化此類威脅。`
- v3：`淨化，確保我族的自由與安全。\n對此自由與安全的威脅——僅限於非烏寬的智慧生命形式。\n為了維護我族的自由與安全，我族淨化此類威脅。`
- 差異：全面去「我等」「之」文言 · 加逗號斷句 + 破折號
- 推薦：🟠 **B**
- 選擇：A / B

### #30 · `WILL_KILL_3` · 🟠
- EN: `We do not have to stop. No one can make us stop except the Kzer-Za\nand they have lost the war. Our doctrine is now dominant.\nThe cleansing will continue.`
- Shipped：`我等無須停下。 無人能令我等停下，除了克澤札\n然他們已於戰爭中落敗。 我等永恆教條如今主宰。\n淨化將繼續。`
- v3：`我族無需停下。 除了克澤札，無人能令我族停下——\n而他們已在戰爭中落敗。 我族的教義如今主宰一切。\n淨化將繼續。`
- 差異：全面去「我等」文言 · Q5=A 廢除「永恆」headline（EN 只說 `Our doctrine`）· 「已於」→「已在」
- 推薦：🟠 **B**
- 選擇：A / B

### #31 · `WILL_KILL_4` · 🟠
- EN: `If you eliminate all non-Ur-Quan sentient races, including yourselves\nthen we will stop.\nWe have made this offer before. No one accepts.\nSo we cleanse.`
- Shipped：`若爾消滅所有非烏寬的有情種族，包括爾自身\n則我等將停下。\n此提議我等以往提過。 無人接受。\n所以我等淨化。`
- v3：`若你們消滅所有非烏寬的有情種族——包括你們自己——\n那麼我族將停下。\n此項提議，我族以往提過。 無人接受。\n所以，我族淨化。`
- 差異：全面去「爾」「我等」文言 · 「則」→「那麼」· 加破折號斷句
- 推薦：🟠 **B**
- 選擇：A / B

### #32-35 · `GOODBYE_AND_DIE_FRENZY_1..4` · 🟠 x4（dossier §六 例 4 招牌 icon）
- EN: `You may not leave. You are filth.\nYou shall be cleansed.`
- Shipped：`爾不可離開。 爾為穢物。\n爾當被淨化。`
- v3：`你不可離去。 你就是污穢。\n你將被淨化。`
- 差異分析：
  - **dossier §六 例 4 canonical**：`You are filth. You shall be cleansed.` → 「你就是污穢。 你將被淨化。」
  - 「爾」→「你」· 「穢物」→「污穢」（canonical）· 「爾當」→「你將」（現代未來式 Q7=C）
- 推薦：🟠 **B**（4 tokens 一次決策 · 招牌 icon）
- 選擇：A / B

### #36 · `RESISTANCE_IS_USELESS_1` · 🟠
- EN: `Over five thousand races have made such a claim.\nWe survived. They did not.\nNor shall you.`
- Shipped：`已有五千餘族提出此類主張。\n我等倖存。 他們未然。\n爾亦不會。`
- v3：`超過五千個族群提出過此類主張。\n我族倖存了。 他們沒有。\n你也不會。`
- 差異：「已有」→「超過」· 「爾亦」→「你也」· 「未然」→「沒有」
- 推薦：🟠 **B**
- 選擇：A / B

### #37 · `RESISTANCE_IS_USELESS_3` · 🟠（dossier §六 例 3 招牌對稱 icon · Q8=A）
- EN: `We did. You did. Yes we can. No.`
- Shipped：`我等為之。 爾為之。 是，我等能。 否。`
- v3：`我族做過。 你也做過。 是的，可以。 不。`
- 差異：**Q8=A 直採 dossier §六 例 3 canonical**（4 句極簡對稱回應 · 招牌 icon）
- 推薦：🟠 **B**
- 選擇：A / B

### #38 · `RESISTANCE_IS_USELESS_4` · 🟠
- EN: `Our counter to your statement is simpler\njust \`die'.`
- Shipped：`我等對爾之言之回應更為簡潔\n即『死』。`
- v3：`我族對你陳述的回應更簡潔——\n即『死』。`
- 差異：「爾之言之」→「你陳述的」· 加破折號斷句
- 推薦：🟠 **B**
- 選擇：A / B

### #39 · `RESPONSE_TO_KEY_PHRASE` · 🟠（Q1=D 三度遞減 icon + Q3=A 外來者）
- EN: `THE WORDS!... the Words... the words\nAlien, you have spoken the Words. You have spoken them rightly.\nWe will explain to you about the Dnyarri, our slavemasters\nthe Taalo, our only friends... whom we exterminated\nand our reasons why we cleanse the galaxy of all other sentient life.\nWe have explained this before, over twenty thousand years ago.\nYour words, 'Why do you do this thing?' echo that ancient plea.\nYou see, alien, we were a proud and mighty race, who were cruelly enslaved.\nFor thousands of years, we had no free will.\nWe were nothing more than tools.\nNever again will anyone enslave our people.\nWe cleanse the galaxy of such threats.`
- Shipped：`那些話！… 那些話… 那些話\n異族，爾說了那些話。 爾正確地說了。\n我方將向爾說明蟾亞族，我方之奴役者\n塔洛族，我方唯一之友… 我方將他們滅絕之\n以及我方為何淨化銀河中所有其他有情生命之緣由。\n此事我方曾以往解釋過，於兩萬多年前。\n爾之言，『為何為此？』，正是那古老懇求之迴響。\n爾看，異族，我方曾為驕傲而強大之族，卻被殘忍地奴役。\n數千年間，我方無自由意志。\n我方不過是工具。\n無人可再如此奴役我方之族。\n我方淨化銀河中此類威脅。`
- v3：`那些話語！…… 那些話語…… 那些話語……\n外來者，你說出了那些話語。 你說對了。\n我族將向你說明蟾亞——我族的奴役者——\n以及塔洛——我族唯一的朋友…… 遭我族親手滅絕的朋友——\n還有我族淨化銀河所有其他有情生命的理由。\n此事，我族以往解釋過——兩萬多年前。\n你的話，『為何要做這件事？』，正是那古老懇求的迴響。\n你看，外來者，我族曾是驕傲而強大的種族——卻被殘忍地奴役。\n數千年間，我族沒有自由意志。\n我族不過是工具。\n再無任何人能如此奴役我族。\n我族淨化銀河中此類威脅。`
- 差異分析：
  - **`THE WORDS!... the Words... the words` → 「那些話語！…… 那些話語…… 那些話語……」**（Q1=D dossier §六 例 6 canonical **三度遞減音量 icon**）
  - `Alien` → **外來者**（Q3=A canonical · shipped「異族」較舊）
  - shipped 全面「爾」「我方」文言 → v3 全清除
  - `Why do you do this thing?` 回呼 → 對齊 #6 `key_phrase` 的「為何要這麼做」
- 推薦：🟠 **B**（招牌 icon + canonical）
- 選擇：A / B

### #40 · `WE_WERE_SLAVES` · ✨（感知聯盟 canonical）
- EN: `We evolved on a hostile world... [12 lines lore]`
- Shipped：全用「我方」「之」文言 + `意識邦聯（Sentient Milieu）`
- v3：全去文言 + `感知聯盟` canonical + 保留敘事節奏
- 差異分析：
  - ✨ **意識邦聯** → **感知聯盟** canonical (Master_Glossary v0.5.2)
  - 大量「我方」「之」文言全清除
  - 敘事節奏保留（12 行對應 EN 12 行）
- 推薦：✨ **B**
- 選擇：A / B

### #41 · `WE_ARE_URQUAN_TOO` · 🟠
- EN: `Of all the species we have met... [10 lines lore about Taalo/Dnyarri]`
- Shipped：全用「我方」「之」文言 · `意識邦聯之六族`
- v3：全去文言 · `感知聯盟其他六個族群`
- 推薦：🟠 **B**
- 選擇：A / B

### #42 · `BONE_GARDENS` · ✨（感知聯盟 canonical）
- EN: `It was on a routine planetfall... [Dnyarri origin story]`
- Shipped：`意識邦聯` + 大量文言
- v3：`感知聯盟` + 現代白話
- 推薦：✨ **B**
- 選擇：A / B

### #43 · `YOU_DIE` · ✨（感知聯盟 canonical + Q2=C 個體「我」段）
- EN: `For thousands of years, we were unthinking slaves to the Dnyarri...\n[個體段] I grow tired of talking, alien, and your time grows short.\nI will continue for but a moment longer...\nCan you imagine, alien, what it must have been like to wear an Excruciator?`
- Shipped：`吾將僅再繼續片刻` + `爾能想像穿戴苦刑器` + 大量文言
- v3：`我僅再繼續片刻` + `你能想像嗎——穿戴苦刑器` + 現代白話 + Q2=C 個體「我」（EN `I grow tired / I will continue`）
- 差異分析：
  - ✨ **舊感知聯盟**（v0.2 canonical）
  - Q2=C **個體「我」段**（`I grow tired / I will continue` · Kohr-Ah 個別艦長對玩家講話）
  - 「爾」「我等」「吾」全清除
- 推薦：✨ **B**
- 選擇：A / B

### #44 · `THEN_DIE` · ✨（現在與永恆之道 + 梅努族 + 感知聯盟 三 canonical）
- EN: `No, it is not. There is more you must hear.\n...declared the Path of Now and Forever...\nThe one-eyed creatures, the Mael-Num, asked so simply...`
- Shipped：`宣告今與永恆之道` + `邁爾努族` + 大量文言
- v3：`宣告了現在與永恆之道` + `梅努族` + 現代白話
- 差異分析：
  - ✨ **今與永恆之道** → **現在與永恆之道**
  - ✨ **邁爾努族** → **梅努族**（Master_Glossary v0.2）
  - ✨ **意識邦聯** → **感知聯盟**
  - shipped「非也，尚未完」等文言全清除
- 推薦：✨ **B**（三 canonical 齊升級）
- 選擇：A / B

### #45 · `BONE_PILE` · 🟠（Q2=C 個體「我」段）
- EN: `My trophy bone-pit.\nIn here is one skeleton from each of the races which I personally exterminated.\nI fondle these bones and recall the fine cleansing.\nPerhaps your bones will grace this pit momentarily\nunless they are accidentally vaporized.`
- Shipped：`此乃吾之戰利骨骸坑。\n此處存放吾親手滅絕之各族骨骸，皆吾親手滅絕所得。\n我撫弄這些骨頭，回想那些精彩之淨化。\n或許稍後爾之骨骸也能點綴此坑\n除非它們不慎被汽化。`
- v3：`這是我的戰利骨骸坑。\n此處存放我親手滅絕的每一個族群的一副骨骸。\n我撫弄這些骨頭，回想那些精彩的淨化。\n或許你的骨骸稍後也能點綴此坑——\n除非它們不慎被汽化。`
- 差異分析：
  - Q2=C **個體「我」段**（EN `My trophy... I personally... I fondle` · Kohr-Ah 個別艦長獨白）
  - shipped「吾」「爾」「之」全清除
  - shipped 有句冗餘「皆吾親手滅絕所得」（EN 沒有這個補述）→ v3 精簡
- 推薦：🟠 **B**
- 選擇：A / B

### #46 · `YES_CREEPY` · 🟠（Q2=C 個體「我」段）
- EN: `Seeing that I represent your imminent death\nas well as the termination of your entire species\nI think your fear is well justified.\nNonetheless, you require cleansing.`
- Shipped：`既然我代表爾之迫在眉睫之死\n以及爾整族之終結\n我認為爾之恐懼合情合理。\n然，爾仍需淨化。`
- v3：`既然我代表著你迫在眉睫的死亡——\n以及你整個族群的終結——\n我認為你的恐懼合情合理。\n儘管如此，你仍需淨化。`
- 差異分析：
  - Q2=C 個體「我」保留（EN `I represent / I think`）
  - shipped「爾」「之」文言全清除 · 「然」→「儘管如此」
- 推薦：🟠 **B**
- 選擇：A / B

### #47 · `DIE_HUMAN` · 🟠
- EN: `The time has come. You require cleansing.`
- Shipped：`時候到了。 爾需淨化。`
- v3：`時候到了。 你需要淨化。`
- 差異：「爾」→「你」· 「需」→「需要」
- 推薦：🟠 **B**
- 選擇：A / B

### #48 · `PLEADING_IS_USELESS_1` · 🟠
- EN: `In the twenty thousand years of our Mission\nwe have heard more pleas for mercy than you can possibly imagine.\nCivilizations which saw their doom before them called upon their geniuses to calm us\nto no avail.`
- Shipped：`在我等兩萬年之使命中\n我等聽過的求饒之言遠多於爾所能想像。\n看見自身滅亡之文明呼喚其天才來安撫我等\n無效。`
- v3：`在我族兩萬年使命的歷程中——\n我族聽過的求饒之言，遠多於你所能想像。\n親眼看見自身滅亡的文明，召喚他們的天才來安撫我族——\n毫無效果。`
- 差異：全去「我等」「之」「爾」· 加破折號斷句
- 推薦：🟠 **B**
- 選擇：A / B

### #49 · `PLEADING_IS_USELESS_2` · 🟠
- EN: `We are self-sufficient. We need nothing. We want nothing\nbeyond the total destruction of all non-Ur-Quan sentience.`
- Shipped：`我等自給自足。 我等無所需。 我等無所欲\n除了徹底摧毀所有非烏寬之有情智慧。`
- v3：`我族自給自足。 我族無所需。 我族無所欲——\n除了徹底毀滅所有非烏寬的有情智慧。`
- 差異：「我等」→「我族」· 「摧毀」→「毀滅」· 加破折號斷句
- 推薦：🟠 **B**
- 選擇：A / B

### #50 · `PLEADING_IS_USELESS_3` · 🟠（灰色同胞 canonical）
- EN: `The ignominy of slaving we leave to our Kzer-Za cousins.\nWe have no need for inferiors as servants.`
- Shipped：`奴役之屈辱，我等留給我等族兄克澤札。\n我等無需下等者為僕。`
- v3：`奴役的屈辱，我族留給灰色同胞克澤札。\n我族不需要低等者作僕役。`
- 差異：**「我等族兄克澤札」→「灰色同胞克澤札」**（dossier §四 Kohr-Ah 對 Kzer-Za canonical 稱謂）· 全去文言
- 推薦：🟠 **B**
- 選擇：A / B

### #51 · `PLEADING_IS_USELESS_4` · 🟠
- EN: `You are right.\nYou are not our enemy.\nWe have NO enemy\nbeyond the Kzer-Za, our partners in the eternal conflict.\nYou are simply... a spore, a seed.\nToday you are nothing... insignificant.\nBut if allowed to bloom and grow someday...\nsomeday, you might represent a threat to our freedom and security.\nSo we cleanse.`
- Shipped：`爾說得對。\n爾非我等之敵。\n我等無敵\n除了克澤札，我等永恆衝突之伙伴。\n爾不過是… 一顆孢子、一粒種子。\n今日爾不算什麼… 微不足道。\n然若允許今後綻放成長…\n某日，爾或可能對我等之自由與安全構成威脅。\n所以我等淨化。`
- v3：`你說得對。\n你不是我族的敵人。\n我族沒有敵人——\n除了克澤札，我族永恆衝突的伙伴。\n你不過是…… 一顆孢子、一粒種子。\n今日的你什麼都不是…… 微不足道。\n但若容你日後綻放成長……\n某日，你或許能對我族的自由與安全構成威脅。\n所以，我族淨化。`
- 差異：全面去「爾」「我等」「之」· 「然」→「但」· `spore/seed` → **孢子、種子**（canonical）保留
- 推薦：🟠 **B**
- 選擇：A / B

### #52 · `GOODBYE_AND_DIE` · 🟠（dossier §六 例 7 canonical）
- EN: `Before we destroy other thinking beings we share with them this comforting fact\nThis life of yours... which shall end immediately following this statement\nis but one of many lives you will live.\nPerhaps, in your next incarnation\nyou will be born an Ur-Quan.`
- Shipped：`在我等摧毀其他有思生靈之前，我等與之分享此撫慰事實\n爾此一生… 於此聲明之後即將終結\n不過是爾將經歷之眾多生命之一。\n或許，在爾下一世\n爾將轉生為烏寬。`
- v3：`在我族毀滅其他有思生靈之前，我族與他們分享此撫慰的事實——\n你這條生命——將在此段話語結束後立即終結——\n只是你將活過的眾多生命之一。\n也許，在你的下一次轉世——\n你將以烏寬的身分誕生。`
- 差異分析：
  - **dossier §六 例 7 canonical** 直接採用
  - shipped「爾此一生」「爾將轉生」文言全清除
  - 「摧毀」→「毀滅」（EN `destroy`）
- 推薦：🟠 **B**
- 選擇：A / B

### #53 · `GAME_OVER_DUDE` · 🟠
- EN: `Attention human!\nThis broadcast is to inform you of your defeat.\nWe, the Kohr-Ah, have destroyed all the sentient species in this region of space\nand now we have eliminated the Starbase orbiting your planet Earth as well.\nYour efforts to resist us are futile.\nYou are defeated!`
- Shipped：`聞哉，人類！\n此廣播乃通知爾等之敗北。\n我方，柯亞族，已摧毀此星域所有之有情種族\n如今我方亦已消滅繞行爾之地球運行之星際基地。\n爾抗拒我方之努力，徒勞無益。\n爾已敗！`
- v3：`注意，人類！\n此廣播用以通知你們的敗北。\n我族——柯亞——已毀滅此星域所有的有情族群——\n如今，我族也已消滅繞行你們地球的星際基地。\n你們抗拒我族的努力，徒勞無益。\n你們已敗！`
- 差異分析：
  - **「聞哉」→「注意」**（Q1=D 去「哉」· `Attention!` 現代白話）
  - `human!` 保留「人類」（EN 唯一明確使用 · dossier §四 稱謂例外）
  - 「爾等」→「你們」· 「柯亞族」→「柯亞」
  - `you are defeated` → 「你們已敗」（集體 · humanity 全體）
- 推薦：🟠 **B**
- 選擇：A / B

### #54 · `OUT_TAKES` · ✨（現在與永恆之道 canonical · Q6=A 保留 gag）
- EN: `We are the Ur-Quan Kohr-Ah\nThe followers of the Path of Now and Forever!\nYou are filth. We shall cleanse.\nYou WILL be annigilated... I mean annihigated.. damn!\nCUT! CUT! Let's start over!\nHey, mister director... can you PLEASE think of SOME other word besides\nagnigilate... I mean, oh what's the use. I give up.`
- Shipped：`我方乃烏寬柯亞族\n今與永恆之道之追隨者！\n爾為穢物。 我方將淨化。\n爾將被『殮滅』… 我是說『湮滅』… 該死！\nCUT！ CUT！ 重來一次！\n嘿，導演先生… 能『不』能想個其他的字\n除『殲滅』外… 我是說，唉算了。 我放棄。`
- v3：`我族即烏寬柯亞——\n現在與永恆之道的追隨者！\n你就是污穢。 我族將淨化。\n你將被『殮滅』…… 我是說『湮滅』…… 該死！\n卡！ 卡！ 重來一次！\n嘿，導演先生…… 你『能不能』想個別的字——\n除了『殲滅』…… 唉算了。 我放棄。`
- 差異分析：
  - Q6=A **保留 shipped 殮滅/湮滅/殲滅 wordplay**（v0.4 Phase 14c 特別打磨）
  - ✨ **今與永恆之道** → **現在與永恆之道** canonical
  - `CUT! CUT!` → 「卡！ 卡！」（dossier §四 canonical 現代口語）
  - shipped「我方乃」「爾」文言全清除
- 推薦：✨ **B**
- 選擇：A / B

---

## 🔴 語意/voice 差異大（0 tokens）

無 · v3 與 shipped 對 EN 的理解一致 · 差異均為 voice 風格（文言→現代冷酷）與 canonical 對齊。

---

## 批次快答格式

若你想批次快答：

```
🟢 全 A (17 tokens)
🟡 全依推薦 (15 tokens · 混合 A/B)
🟠 全 B (35 tokens · 招牌 icon + 去文言)
✨ 全 B (9 tokens · canonical 升級 · 必須)
```

或逐項挑：

```
#1=A #2=B #6=A #16=B ... (指定 token 編號)
```

或按類別：

```
✨ 全 B · 🟠 全 B · 🟡 全 A · 🟢 全 A
```

---

## Merge 後預期效果

- 完全清除 244 個文言助詞（吾/爾/爾等/乃/哉/之作為助詞）
- Kohr-Ah voice 對齊 dossier v0.7 A 案（極簡冷酷宣告體 · 判決書口吻）
- 對外 canonical 名詞與 Kzer-Za v3 一致（薩瑪特拉 / 感知聯盟 / 現在與永恆之道 / 梅努族）
- 保留 shipped 招牌 icon 資產（淨化 44 / 骨骸坑 / 苦刑器 / OUT_TAKES 殮滅口誤 gag）
- 完全繼承所有 canonical 種族名（柯亞 / 克澤札 / 塔洛族 / 蟾亞 / 尤利族 / 卓爾族 / 苦刑器 / 會話寵）
- 招牌對稱 icon 對齊 dossier §六 例 3（我族做過。 你也做過。 是的，可以。 不。）
- CAPS 三度遞減 icon 對齊 dossier §六 例 6（那些話語！…… 那些話語…… 那些話語……）

---

## Session 決策紀錄

Q1=D · Q2=C · Q3=A · Q4=A · Q5=A · Q6=A · Q7=C · Q8=A（全依推薦）

**v3.1 直譯修訂（追加 · 使用者審視後）**：18 項全採（22 tokens 涉及 · 詳見本檔開頭 v3.1 revision block）

（Session 2026-08-16 · Ur-Quan Kzer-Za v3 completion 之後）
