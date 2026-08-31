# Chmmr Rebuild-Compare Diff Report (2026-08-17)

> **Race**: `chmmr` (Chenjesu pre-fusion + Chmmr post-fusion 兩 voice)
> **Files**: `translations/chmmr.zh-TW.v3.json` (rebuild) vs `translations/chmmr.zh-TW.json` (shipped v0.4 Phase 14c++)
> **Workflow**: `09_AI_Prompt/Rebuild_And_Compare.md` v0.7.1
> **Dossiers**: `02_Races/Chenjesu.md` v0.7 (全小寫詩意冥想體) + `02_Races/Chmmr.md` v0.7 (全大寫神諭體)

---

## 統計

- Total tokens: **78** (28 pre-fusion Chenjesu + 50 post-fusion Chmmr)
- 🟢 完全相同 (identical): **12** (15.4%) — 不列細節
- 🟡 微調 (等價): **~28** (35.9%) — 標點/語序/近義字
- 🟠 措辭改變: **~14** (17.9%) — 選字差異，語意等價
- 🔴 語意/voice 差異大: **0** (0%)
- ✨ v0.7 canonical 升級: **~24** (30.8%) — dossier v0.7 + Q&A 決策
- Line-count: ✅ 78/78 對齊
- Purity: ✅ 0 pollution / 0 simp / 0 variant
- Lua template: ✅ 0 suspicious

---

## 決策依據（Q&A 於 partial-1 前確定）

| # | 決策 | 說明 |
|---|---|---|
| Q1 | A | Chenjesu pre-fusion 自稱：`我等` (全依 dossier) |
| Q2 | A | Chmmr post-fusion 自稱：`我等` (全依 dossier) |
| Q3 | A | Chmmr 全大寫 icon：JSON 用短句+密集感嘆號（無 `**bold**`） |
| Q4 | A | Chenjesu 刪節號：`……` 全形雙點 |
| Q5 | A | Sa-Matra 統一 `薩瑪特拉`（無連字號，對齊 v3 生態圈 6 族） |
| Q6 | A | annihilation toroid → `殲滅環`（軍事語域+精簡） |
| Q7 | A | crucible of sentience → `意識的熔爐`（v0.7 dossier canonical） |
| Q8 | B | once and future ally → `昔日與未來的盟友`（僅去「之」→「的」） |
| Q9 | B | 玩家 response 情境切換 `我方/我`（政治正式=我方 · 搞笑俏皮=我 · 中性=我方） |
| Q10 | A | 3 partials（依 voice 邊界） |

---

## 全域 canonical 升級（適用多 tokens · 一併列出）

| 舊 (shipped) | 新 (v3) | 出現次數 | 依據 |
|---|---|---|---|
| 吾等 | 我等 | 45 | Q2 dossier v0.7 §四 · 全 post-fusion |
| 吾 | 我 | 45 | Q2 dossier v0.7 · 廢除文言助詞 |
| 我方 (pre-fusion) | 我等 | ~25 | Q1 dossier §四 · 静穆冥想 icon |
| 之 (助詞) | 的/當中/以前/在…裡 | 35 | v0.7 文言助詞禁令 |
| 乃 | 是/即/便 | 4 | v0.7 文言助詞禁令 |
| 爾 | 你 | 4 | v0.7 文言助詞禁令 |
| 薩-瑪特拉 | 薩瑪特拉 | 28 | Q5 · 對齊 Kzer-Za/Kohr-Ah/Dnyarri/Utwig/Yehat/final v3 |
| 融合程序 | 融合工程 | 7 | dossier §四 canonical (廢弱化) |
| 湮滅環 | 殲滅環 | 2 | Q6 · 軍事語域升級 |
| 覺識的坩堝 | 意識的熔爐 | 1 | Q7 · dossier v0.7 canonical |
| 昔日與未來之盟友 | 昔日與未來的盟友 | 2 | Q8 · 去「之」 |
| 本融合體 | 我等 | 3 | dossier v0.7 §四 明令廢除 |
| 育巢艦 | 母巢艦 | 3 | Master_Glossary L175 primary canonical |
| 行星工具 | 星體工程器 | 1 | Master_Glossary L117 v0.7 canonical |
| 甚善 | 好 | 1 | 廢除文言副詞 |
| … (單刪節號) | …… (雙全形) | ~30 | Q4 · Chenjesu 靜穆冥想 icon |
| 無。 (DEAD_SILENCE) | 否。 | 1 | Q3 · dossier §四 §六 例 2 短命令 icon |
| 可以。 (YES) | 是。 | 1 | Q3 · dossier 短命令 icon 對稱「否」 |

---

## 差異項（🟢 12 tokens 不列 · 66 changed tokens 逐項）

### #1 · WHY_YOU_HERE_1 · ✨ 全域升級 + Chenjesu icon 到位

**英文原文**:
> we are the chenjesu... we are the mmrnmhrm\
> we do not understand how you have penetrated the slave shield or why\
> but in doing so you have interrupted the process\
> explain this intrusion.

**Shipped**:
> 我方為晶智族… 我方為姆姆族\
> 我方不解你如何穿透奴役護盾，亦不解原因\
> 然而你如此為之，已中斷了融合程序\
> 請說明這次入侵。

**Rebuild v3**:
> 我等即晶智族…… 我等即姆姆族\
> 我等不明白你如何穿透了奴役護盾，也不明白你為何前來\
> 然而你此舉，已打斷了融合工程\
> 請說明此番闖入。

**差異分析**：
- ✨ Q1「我方→我等」(3×) + Q4「… → ……」(2×) + 融合程序→融合工程 + 「亦不解原因→也不明白你為何前來」（切近 EN `or why` 兼顧「你為何前來」的動機層次）+「這次入侵→此番闖入」（更貼 EN `intrusion` 智者語氣）
- v3 完全對應 dossier §六 範例 1（僅奴役護盾用生態圈 canonical，未採 dossier 範例的「奴役防護罩」）

**推薦**：B (v3) — 招牌 pre-fusion icon 完整到位

---

### #2 · WHY_YOU_HERE_2 · ✨ 全域升級

**英文原文**：
> once more you interfere with the process... why?

**Shipped**：
> 你又一次干擾了融合程序… 為什麼？

**Rebuild v3**：
> 你又一次干擾了融合工程…… 為何？

**差異分析**：融合程序→融合工程 (Q1 dossier) + 「… → ……」(Q4) + 「為什麼→為何」（更凝練，符合智者語氣）

**推薦**：B (v3) — 全依 Q1/Q4

---

### #3 · WHY_YOU_HERE_3 · ✨ 全域升級 + 廢「乃」

**英文原文**：
> your presence here is painful to us... what is it you wish?

**Shipped**：
> 你出現在此對我方**乃**是痛苦… 你想要什麼？

**Rebuild v3**：
> 你出現在此，對我等而言是痛苦…… 你所求為何？

**差異分析**：廢「乃」(文言) + 加逗號斷句 + Q1 我方→我等 + Q4 …→…… +「你想要什麼→你所求為何」（更貼 `what is it you wish` 的正式感）

**推薦**：B (v3)

---

### #4 · WHY_YOU_HERE_4 · ✨ 同 #3（重複 token）

Shipped 與 v3 差異同 #3 · 保持一致。

**推薦**：B (v3)

---

### #6 · HYBRID_PROCESS · ✨ 全域升級 + Q7 意識的熔爐

**英文原文**：（21 行 long lore dump · 略）

**Shipped 主要文言污染**：
- 我方 × 8 (應 Q1→我等) · 之 × 6 (含「相似之處/稱之為/薩-瑪特拉之武器/於此遙距之外/我方向貴族發出/所計畫之事/我方投降之前」) · 覺識的坩堝 × 1 · 薩-瑪特拉 × 4 · 融合程序 × 0 (此 token 只用 `process` 未直譯)

**Rebuild v3**（22 行 · 對應 EN 逐段）：
- Q1 我方→我等 (全段) + Q7「覺識的坩堝→意識的熔爐」(在此 token 首次出現) + Q5 薩-瑪特拉→薩瑪特拉 × 4 + 全部「之」清除 + 「你們一族」代替「貴族」（貴族原文只是 `your people`，貴族含 nobility 誤解）
- 招牌保留：「意為『偉大戰利』」（Sa-Matra = great trophy 招牌釋名）+「刀槍不入」（生動比喻）+「焚化」（vivid destruction）
- 育巢艦→母巢艦（Master_Glossary primary canonical）

**推薦**：B (v3) — canonical + voice 全升級到位

---

### #8 · CANT_HELP · ✨ 全域升級 + 廢除本融合體

**英文原文**：（14 行 · 略）

**Shipped 主要問題**：
- 「本融合體開始了兩族、兩種文化之合成」→ dossier v0.7 明令廢除「本融合體」
- 混用「我方/吾等」（前段我方後段吾等 · 邏輯不一致）
- 「進入奴役護盾」→ 應為「被封印於世界上，共處奴役護盾之下」（`encased in slave shield` 是封印，不是進入）
- 「蛹殼」→ EN 是 `cocoon`（繭），前面 `chrysalis` 是「蛹」，此處「殼」多餘

**Rebuild v3**：
- Q1 全段我等 + 廢除「本融合體」→「我等」+ Q4 …→…… + 融合程序→融合工程
- 「一同進入此星球的奴役護盾」→「一同被封印於這顆世界上——共處一片奴役護盾底下」（更精確 `encased` 語意）
- 「一為結晶生命，另一為純粹機械」→「一為晶體，另一為純粹機械」（更貼 EN `crystalline`）
- 「一新的混合種族」→「一個嶄新的混合種族」（加量詞更順）
- 「離開牠的蛹殼」→「離開牠的蛹」（去多餘字）

**推薦**：B (v3)

---

### #9 · why_no_help · 🟢 幾乎相同（已修 ？！）

**英文原文**：
> But why can't you help us now?!

**Shipped**：
> 但為什麼你們現在不能幫忙？！

**Rebuild v3**：
> 但為什麼你們現在不能幫忙？！

**差異分析**：v3 與 shipped 相同（已在自審時修回 ？！）

**推薦**：A = B（identical after fix）

---

### #10 · LONG_TIME · ✨ Q1 我方→我等 + 之清除

**英文原文**：
> the complete synthetic hybridization of the chenjesu and the mmrnmhrm species\
> will require approximately thirty-five of your earth years\
> this extended duration is necessary because our synthesis mechanisms\
> are dependent exclusively on the light of our sun for energy.

**Shipped**：
> 晶智族與姆姆族兩族的完全合成融合\
> 將需要約你方地球年三十五年**之久**\
> 此漫長時程有其必要，因為我方的融合機制\
> 完全依賴我方恆星的光作為能源。

**Rebuild v3**：
> 晶智族與姆姆族兩個物種的完全合成融合\
> 將需要以你們地球年計算約三十五年那麼久\
> 此漫長時程有其必要，因為我等的合成機制\
> 完全依賴我等恆星的光作為能源。

**差異分析**：Q1 我方→我等 · 之久→那麼久 · 融合機制→合成機制（更貼 EN `synthesis mechanisms` · dossier 有 canonical）· 「兩族→兩個物種」（EN `species`）

**推薦**：B (v3)

---

### #11 · what_if_more_energy · 🟡 微調

**英文原文**：
> What if we could find some way to get you more energy? Would that speed things up?

**Shipped**：
> 如果我方能想辦法給你們更多能源呢？ 那樣能加速嗎？

**Rebuild v3**：
> 如果我方有辦法給你們更多能源呢？ 那樣能加速嗎？

**差異分析**：「能想辦法」vs「有辦法」— 等價，語感略異

**推薦**：A (shipped) — shipped「能想辦法」略帶「主動嘗試」感，v3「有辦法」更平實

---

### #12 · DANGER_TO_US · ✨ 全域升級

**英文原文**：
> what you describe is theoretically possible\
> but it would pose a great danger to us\
> the process must be executed as planned... or it may fail catastrophically\
> we would be destroyed.

**Shipped**：
> 你所描述**之事**理論上可能\
> 但那對我方會構成極大危險\
> 程序必須按原計畫執行… 否則可能災難性失敗\
> 我方將被摧毀。

**Rebuild v3**：
> 你所描述的事，理論上可能\
> 但那會對我等構成極大的危險\
> 此工程必須按原計畫執行…… 否則可能災難性失敗\
> 我等將被摧毀。

**差異分析**：Q1 我方→我等 · 之→的 · Q4 …→…… · 「程序→此工程」(dossier canonical) · 加逗號斷句

**推薦**：B (v3)

---

### #14 · WHAT_ADVICE · ✨ 全域升級 + 招牌 icon 到位

**英文原文**：
> our wisdom is available... detail your need.

**Shipped**：
> 我方**之**智慧可用… 詳述你的需求。

**Rebuild v3**：
> 我等的智慧隨時可用…… 說明你的需要。

**差異分析**：Q1 我方→我等 · 之→的 · Q4 …→…… · 「可用→隨時可用」（`available` 隱含「隨時」）· 「詳述→說明」（`detail` 這裡是動詞 `describe`）
- 對應 dossier §六 範例 3 完全一致

**推薦**：B (v3)

---

### #16 · DEFEAT_LIKE_SO · ✨ Q5 + 微調

**英文原文**：（5 行 · 略）

**Shipped 主要問題**：薩-瑪特拉 × 1 → 薩瑪特拉 (Q5)

**Rebuild v3**：
> 你必須設法摧毀薩瑪特拉\
> 為此，你將需要一件強大的武器，足以摧毀整顆行星\
> 但這還不夠\
> 你還需要某種方式分散烏寬族的注意\
> 好讓你有機會使用這件武器。

**差異分析**：Q5 · 「能摧毀→足以摧毀」（語氣更堅定）· 「該武器→這件武器」（避免文書化「該」）· 加逗號斷句

**推薦**：B (v3)

---

### #18 · SCARY_BUT_USEFUL · ✨ 全域升級

**英文原文**：（5 行 · 略）

**Shipped 主要問題**：我方 × 1 · 之 × 1（「古老血脈之一」）· 牠 × 2（vs `it` 中性）

**Rebuild v3**：
> 我等僅由傳說知曉蟾亞族\
> 傳說中將他們描述為邪惡與殘忍的化身\
> 若曾有惡魔存在，艦長，那便是蟾亞族\
> 然而，若你所擁有者，確實是這古老血脈裡的一員\
> 他的心靈力量或許能用來迷惑烏寬族。

**差異分析**：Q1 我方→我等 · 之→裡的一員 · 「牠→他」（EN `its mental power` — 心靈力量代詞用他更貼 sentient 描述）· 「其中描述→傳說中將他們描述為」（前置主語更順）· 「或可用於→或許能用來」（更口語）

**推薦**：B (v3)

---

### #19 · what_about_bomb · 🟡 微調

**英文原文**：
> I got this huge bomb-thing from a race called the Utwig. Is it really a weapon?

**Shipped**：
> 我從一個叫憂特族的種族得到一個巨大的炸彈物件。 那真的是武器嗎？

**Rebuild v3**：
> 我從一個叫憂特族的種族**那裡**拿到一個巨大的炸彈物件。 那真的是武器嗎？

**差異分析**：「得到→那裡拿到」（加「那裡」+「拿到」更口語）

**推薦**：A (shipped) 或 B (v3) — 皆通 · 略偏 shipped 精簡

---

### #20 · ABOUT_BOMB · ✨ Q5 + 措辭優化

**英文原文**：（4 行 · 略）

**Shipped**：薩-瑪特拉 × 1

**Rebuild v3**：
> 你所說的裝置，是一顆巨大的物質反物質炸彈\
> 若你啟動過它，此武器已將你的艦艇以及方圓五百公里內的一切殲滅殆盡\
> 此武器的破壞力，使其適用於你這輩子將承擔的最重大任務\
> 抵銷薩瑪特拉——烏寬族那近乎無敵的戰鬥平台。

**差異分析**：Q5 · 加逗號斷句 · 「將已殲滅→已將…殲滅殆盡」(語序更順) · 「最重要的任務→最重大任務」+ em-dash 引出同位語

**推薦**：B (v3)

---

### #21 · what_about_sun_device · 🟡 Q4 + 微調

**英文原文**：
> I er... borrowed a device from the Mycon. Do you know what it is?

**Shipped**：
> 我… 呃… 從麥孔族那『借』來了一個裝置。 你們知道那是什麼嗎？

**Rebuild v3**：
> 我…… 呃…… 從麥孔族那裡『借』來了一個裝置。 你們知道那是什麼嗎？

**差異分析**：Q4 …→…… (2×) + 「那『借』→那裡『借』」（雖然「那」代地方也通，但「那裡」更清楚）

**推薦**：B (v3)

---

### #22 · ABOUT_SUN_DEVICE · ✨ Q1 我方→我等

**Shipped**：我方 × 1

**Rebuild v3**：
> 我等無法辨識此裝置\
> 但它看似一件先驅者的工具，能輻射出巨量能源。

**差異分析**：Q1 · 「似乎是→看似一件」(加量詞)

**推薦**：B (v3)

---

### #23 · what_about_samatra · ✨ Q5

**Shipped**：薩-瑪特拉 → **Rebuild v3**：薩瑪特拉

**推薦**：B (v3) — Q5 canonical

---

### #24 · ABOUT_SAMATRA · ✨ Q5 + Q6 + 全域升級 + Q4

**英文原文**：（6 行 · 略）

**Shipped 主要問題**：我方 × 2 · 薩-瑪特拉 × 1 · 湮滅環 × 1 · 「數秒之內」

**Rebuild v3**：
> 我等僅親眼見過它一次，當時它蹂躪了我等最強大的艦隊\
> 它比你的艦艇大好幾倍\
> 其焦痂船殼上突出著一群不尋常的武器\
> 但薩瑪特拉最危險的特徵，是它的殲滅環……\
> 此武器能從恆星系的另一側汽化艦艇\
> 或在短短數秒內，於行星上劃開廣大的毀滅帶。

**差異分析**：Q1 · Q5 · Q6 湮滅環→殲滅環 · Q4 …→…… · 「自→從」(更口語) · 「數秒之內→短短數秒內」(避免 之 · 加「短短」強調時間之短)

**推薦**：B (v3) — 一次性升 4 canonical

---

### #25 · enough_advice · 🟡 微調

**Shipped**：謝謝！ → **Rebuild v3**：謝了！

**差異分析**：「謝謝」（禮貌）vs「謝了」（隨性）— EN `Thanks!` 非正式，v3 更貼

**推薦**：A (shipped) 或 B (v3) — 玩家風格個人偏好

---

### #26 · OK_ENOUGH_ADVICE · ✨ 全域升級

**Shipped**：我方 × 1

**Rebuild v3**：
> 雖然你出現在此是痛苦的闖入\
> 無論何時你有需要，我等永遠會提供指引，艦長。 

**差異分析**：Q1 · 「入侵→闖入」（vs #1「請說明此番闖入」保持 canonical 統一 · shipped 這裡用「入侵」不一致）· 「你需要→你有需要」（更順口）· 「都會給予建議→永遠會提供指引」（EN `will always provide advice` — 用「永遠會」更貼 `always`，「指引」比「建議」更帶 Chenjesu 智者感）

**推薦**：B (v3) — 對應 dossier §六 範例 4

---

### #28 · GOODBYE_SHIELDED · ✨ Q8 + Q4 + 全域升級 + 招牌 icon

**英文原文**：
> goodbye once and future ally, human... when the process is complete and we emerge from our chrysalis\
> i shall tell your grandchildren of our conversation this day.

**Shipped**：
> 再見，昔日與未來**之**盟友，人類… 融合程序完成、我方破繭而出時\
> 我將把今日這場對話說給你的孫輩聽。

**Rebuild v3**：
> 再會，昔日與未來的盟友，人類…… 當融合工程完成、我等自繭中羽化\
> 我將把今日這場對話，訴說給你的孫輩聽。

**差異分析**：Q8 之→的 · Q4 …→…… · Q1 我方→我等 · 融合程序→融合工程 · 「再見→再會」（Chenjesu 智者風格 · 對應 dossier §六 範例 5「再會，曾經與未來的盟友，人類……」）· 「破繭而出→自繭中羽化」（更詩意，貼 dossier 「羽化」canonical）· 「說給→訴說給」

**推薦**：B (v3) — 對應 dossier §六 範例 5

---

### #29 · WE_ARE_FREE · ✨ 招牌 icon 完整到位（v3 修訂關鍵 token）

**英文原文**：
> WE ARE FREE!\
> YOU HAVE FLOODED OUR SYNTHESIS MECHANISMS WITH A WEALTH OF RADIANT ENERGY.\
> WHAT WAS SUPPOSED TO TAKE DECADES HAS BEEN ACCOMPLISHED IN SECONDS.\
> THE PROCESS IS INCOMPLETE, YET WE HAVE EMERGED.\
> WE ARE THE CHMMR.

**Shipped**：
> 吾等破繭而出！\
> 是**爾**以豐沛**之**輻射能傾注吾等融合機制。\
> 本當數十年**之**工，於數秒**之**間告成。\
> 程序未竟，吾等已現。\
> 吾等即查姆。（Chmmr）

**Rebuild v3**：
> 我等即獲自由！\
> 你已將豐沛的輻射能量，灌注入我等的合成機制！\
> 原本需耽時數十年的工程，短短數秒內便已告成！\
> 融合工程尚未圓滿。 然而我等已然羽化。\
> 我等即查姆族。

**差異分析**：Q2 吾等→我等 (×5) · 之 × 3 全清 · 爾→你 · 「破繭而出→即獲自由」（EN 首句 `WE ARE FREE!` 是 icon · shipped 錯譯為「破繭而出」是後幾句才有的意象）· Q3 「傾注→灌注入」+ 感嘆號補齊（EN 只有第一句有 !，v3 加到第 2、3 句形成 icon 密集感嘆節奏）· 「即查姆。（Chmmr）→即查姆族。」（去中括號英文，因族名已在 #1 首介）
- 對應 dossier §六 範例 1

**推薦**：B (v3) — 招牌爆發 icon 完整實現

---

### #32 · i_am_savior · 🟡 語序微調

**Shipped**：我是試圖拯救銀河的那個人。 → **Rebuild v3**：我是那個試圖拯救銀河的人。

**差異分析**：語序 shift（前置「那個」）· 微差

**推薦**：A (shipped) — shipped「試圖拯救銀河的那個人」更英雄感 · v3「那個試圖拯救銀河的人」略平淡

---

### #33 · i_am_silly · 🟡 Q4 + 微調

**Shipped**：我是誰？ 我？ 呃… 該死！ 我剛忘了。 → **Rebuild v3**：我是誰？ 我嗎？ 呃…… 該死！ 我剛忘了。

**差異分析**：Q4 …→…… · 「我？→我嗎？」（單「我？」略突兀，v3 加「嗎」更順）

**推薦**：B (v3)

---

### #34 · WHY_HAVE_YOU_FREED_US · ✨ Q2 + 融合工程 + 招牌 icon

**英文原文**：
> WHY HAVE YOU INTERRUPTED THE PROCESS?!!!

**Shipped**：
> 你為何中斷了程序？！！ (2 個感嘆號)

**Rebuild v3**：
> 你為何打斷了融合工程？！！！ (3 個感嘆號)

**差異分析**：程序→融合工程 · 「中斷→打斷」(與 #1「打斷了融合工程」保持 canonical) · 感嘆號補齊為 3 個（EN `?!!!` 是招牌 icon · shipped 少一個）
- 對應 dossier §六 範例 5

**推薦**：B (v3)

---

### #35 · WILL_HELP_ANALYZE_LOGS · ✨ 全域升級 · 對稱命令句到位

**英文原文**：（17 行 · 略）

**Shipped 主要問題**：吾等 × 12 · 之 × 5 (「極大之需 / 護盾之下 / 吾等之所能 / 護盾之前 / 敗烏寬族之道」) · 爾 × 2 · 乃 × 1 · 甚善 × 1

**Rebuild v3**：（17 行 · 略）

**關鍵差異**：
- Q2 吾等→我等 (全段) + 之/爾/乃全清 + 甚善→好 (廢文言副詞)
- 「你的優先事項→你的優先目標」+「你最終的目標→你的最終目標」形成對稱結構（`THIS MUST BE YOUR PRIORITY. THIS MUST BE YOUR EVENTUAL GOAL.` dossier §六 範例 3 招牌對稱句節奏）
- 「完成。」→「就緒。」+「程序完成了。→作業完成。」（EN `THERE. THE PROCESS IS COMPLETE.` 這裡的 process 指掃描動作，非融合 · shipped 誤譯為「程序完成」讓玩家困惑）

**推薦**：B (v3) — 招牌對稱句 icon 到位 + 修 process 指涉錯誤

---

### #36 · YOU_KNOW_SAMATRA · ✨ Q5

**Shipped**：薩-瑪特拉 → **Rebuild v3**：薩瑪特拉 · 「可以告訴你→足以推知」(更貼 EN `necessary to tell you` 推理感)

**推薦**：B (v3)

---

### #37 · DONT_KNOW_ABOUT_SAMATRA · ✨ Q5 + 微調

**Shipped**：薩-瑪特拉 × 1 · 「其他族→族群」(避免「族」重複)

**Rebuild v3**：
> 你需要定位烏寬族的薩瑪特拉艦。\
> 若你自己找不到，去問問那些接近烏寬族的族群。\
> 或許他們會知曉。

**差異分析**：Q5 + 「其他族→族群」+「會知道→會知曉」（智者語氣）

**推薦**：B (v3)

---

### #38 · NEED_DISTRACTION · ✨ Q5 + 微調

**Shipped**：薩-瑪特拉 × 2 · 「必然→必定」·「到足夠距離→、達到足夠的距離」(斷句更順)

**Rebuild v3**：
> 薩瑪特拉必定戒備森嚴。\
> 為讓你能夠接近薩瑪特拉、達到足夠的距離\
> 你必須製造某種干擾。

**推薦**：B (v3)

---

### #39 · HAVE_TALKING_PET · ✨ Q2 + Q5

**Shipped**：吾等 × 1 · 薩-瑪特拉 × 1 · 「並摧毀它→並將其摧毀」(語氣更堅定)

**Rebuild v3**：（略）

**推薦**：B (v3)

---

### #40 · NEED_WEAPON · ✨ 全域升級 · 語序改良

**Shipped 主要問題**：吾等 × 3 · 薩-瑪特拉 × 1 · 乃 × 1

**Rebuild v3**：
> 要擊敗烏寬族，你必須先摧毀薩瑪特拉戰鬥平台。\
> 我等能設想的唯一方式，是由你在近距離內、緊鄰戰鬥平台\
> 引爆一枚巨大的爆裂裝置。\
> 我等相信，唯一能產生足夠破壞力的武器\
> 是一枚物質反物質炸彈。 但我等無法自行建造。

**差異分析**：Q2 · Q5 · 廢除乃 · 語序重組：把「近距離」提前，讓「引爆」動詞留在句末（EN 節奏是先地點後動作 · v3 讀起來更順）· 「乃物質反物質炸彈→是一枚物質反物質炸彈」+加逗號拆句

**推薦**：B (v3)

---

### #41 · HAVE_BOMB · ✨ 全域升級 + em-dash 引出同位語

**Shipped**：吾等 × 2 · 薩-瑪特拉 × 1

**Rebuild v3**：
> 你擁有一枚反物質炸彈。 這很好。\
> 然而，若你曾啟動它，此裝置將已殲滅你的艦艇\
> 以及方圓五百公里內的一切。\
> 即便如此，我等仍必須改良此裝置，以我等的水晶科技增幅其威力。\
> 如此，此武器的破壞潛力，便適用於\
> 你這輩子將承擔的最重大任務——\
> 抵銷薩瑪特拉，烏寬族那近乎無敵的戰鬥平台。

**差異分析**：Q2 · Q5 · 「但若→然而，若你曾」(語氣更慎重) · em-dash 引出同位語「最重大任務——抵銷薩瑪特拉」(增強節奏感)

**推薦**：B (v3)

---

### #42 · RETURN_WHEN_READY · ✨ Q2 + 之清除

**Shipped**：吾等所描述**之**資源時 → **Rebuild v3**：我等所述的資源

**推薦**：B (v3)

---

### #43 · YOU_ARE_READY · ✨ Q4 + 微調

**Shipped**：你準備妥當了… → **Rebuild v3**：你已準備妥當……

**差異分析**：Q4 …→…… · 加「已」貼近 EN `YOU ARE READY` 的完成態

**推薦**：B (v3)

---

### #44 · further_assistance · 🟡 微調

**Shipped**：你們現在能給我方進一步的協助嗎？ → **Rebuild v3**：你們現在能給我方更進一步的協助嗎？

**差異分析**：「進一步→更進一步」— shipped 已足夠，v3 加「更」略嘴軟

**推薦**：A (shipped)

---

### #45 · NO_FURTHER_ASSISTANCE · ✨ Q2

**Shipped**：吾等 × 1 · 之前 → **Rebuild v3**：我等 + 以前

**推薦**：B (v3)

---

### #46 · tech_help · 🟡 微調

**Shipped**：願與我方分享嗎？ → **Rebuild v3**：願意與我方分享嗎？

**差異分析**：「願→願意」(v3 更口語)

**推薦**：A (shipped) 或 B (v3) — 皆通

---

### #47 · USE_OUR_SHIPS_BEFORE · ✨ 全域升級

**Shipped 主要問題**：吾等 × 2 · 之 × 2「足夠之查姆艦長 / 所建造之任何艦艇」· 爾 × 1 · 育巢艦 × 1

**Rebuild v3**：
> 我等將提供你一款新型戰艦的設計圖…… 化身艦\
> 並附以足夠的查姆艦長，以指揮你所建造的任何艦艇。\
> 化身級戰艦，遠比我等的母巢艦或 X 型艦更為有效。\
> 在稱職者手中，此艦可擊敗太空中任何艦艇。

**差異分析**：Q2 · Q4 · 之→的 · 爾→你 · 育巢艦→母巢艦（Master_Glossary primary canonical）· 「有效得多→遠比…更為有效」(語氣更堅定)

**推薦**：B (v3) — 但注意育巢艦→母巢艦是 Master_Glossary 判斷，若使用者偏好 shipped 育巢艦則選 C 客製

---

### #49 · PRECURSOR_WEAPON · ✨ Q2 + 星體工程器 canonical

**Shipped 主要問題**：吾等 × 1 · 之手 × 1 · 行星工具

**Rebuild v3**：
> 有傳聞說有這樣一件裝置，一件先驅者的星體工程器\
> 可在 <% comm.swapIfSeeded("遠向 ", "接近 ") %><% comm.getConstellation("銀河核心", "bomb") %>（THE CORE） 某處找到……\
> …… 掌握在一個非敵對的外星種族手中。\
> 目前我等無法提供更多資訊。

**差異分析**：Q2 · Q4 · 之手→手中 · 「行星工具→星體工程器」（Master_Glossary L117 v0.7 utwig Rebuild-Compare canonical）

**推薦**：B (v3) — 星體工程器是全 Utwig 統一 canonical

---

### #50 · where_distraction · 🟡 微調

**Shipped**：才可能 → **Rebuild v3**：才有可能

**差異分析**：加「有」語氣稍緩

**推薦**：A (shipped) — shipped 已通順

---

### #51 · PSYCHIC_WEAPONRY · ✨ Q2 + 之清除

**Shipped**：吾等 × 1 · 之策略 × 1

**Rebuild v3**：
> 我等在研究中發現，烏寬族對心靈操縱特別敏感。\
> 你最佳的策略是尋找此類武器。\
> 須留意，多數心靈武器並非機械造物。\
> 它們通常是有智慧的生命形式，且經常懷有敵意。

**差異分析**：Q2 · 之→的 · 「尋覓→尋找」(去書面感)

**推薦**：B (v3)

---

### #52 · what_now · 🟡 微調

**Shipped**：所以接下來會怎樣？ → **Rebuild v3**：那麼，接下來會怎樣？

**差異分析**：「所以→那麼」(EN `So what happens now?` · v3「那麼」比「所以」更口語)

**推薦**：B (v3) 或 A (shipped) — 皆通

---

### #53 · WE_WILL_IMPROVE_BOMB · ✨ Q5

**Shipped**：薩-瑪特拉 × 1 · 「妥當去執行→妥當，可承擔」

**Rebuild v3**：
> 你已完全準備妥當，可承擔這項任務。\
> 你有充分的機會摧毀薩瑪特拉\
> 並同時阻止烏寬族與柯亞族。

**差異分析**：Q5 · 「去執行→可承擔」（更神諭感）

**推薦**：B (v3)

---

### #54 · MODIFY_VESSEL · ✨ Q2 + 加逗號斷句

**Shipped**：吾等 × 2

**Rebuild v3**：
> 我等現在將把先驅者武器與我等自身的水晶增幅系統，裝配到你的艦艇上。\
> 藉由將你旗艦一部分的融合能源，導入該武器的點火室\
> 其破壞力，將被大幅倍增。

**差異分析**：Q2 · 3 處加逗號斷句（Chmmr 神諭節奏 icon）

**推薦**：B (v3)

---

### #55 · wont_hurt_my_ship · ✨ Q5

**Shipped**：薩-瑪特拉 → **Rebuild v3**：薩瑪特拉

**推薦**：B (v3) — Q5 canonical

---

### #56 · WILL_DESTROY_IT · 🟠 措辭改變 · 招牌 icon 到位

**英文原文**：
> YOUR VESSEL WILL BE TOTALLY ANNIHILATED.

**Shipped**：
> 你的艦艇將被完全殲滅。

**Rebuild v3**：
> 你的飛船，將被完全殲滅。

**差異分析**：「艦艇→飛船」+ 加逗號斷句
- dossier §六 範例 4 明確用「你的飛船，將被完全殲滅。」
- 「艦艇」是 formal 軍事詞；「飛船」是 vessel 的通俗譯，更中性（Chmmr 神諭平淡告知）
- 加逗號讓短句節奏更冷酷

**推薦**：B (v3) — 對應 dossier §六 範例 4 招牌冷酷 icon

**替代**：若使用者堅持「艦艇」一致性，可選 C = 「你的艦艇，將被完全殲滅。」（保留逗號斷句 icon）

---

### #57 · bummer_about_my_ship · 🟡 微調

**Shipped**：我猜也沒辦法改變這件事 → **Rebuild v3**：我想我方也沒辦法改變這件事

**差異分析**：「我猜→我想我方」(v3 加 我方 略嘴軟)

**推薦**：A (shipped) — shipped「我猜」更貼 EN `I don't suppose` 的隨性 · Q9=B 判定此為「搞笑俏皮」用 我 · shipped 已符合

---

### #58 · DEAD_SILENCE · ✨ Q3 短命令 icon

**英文原文**：
> NO.  

**Shipped**：
> 無。 

**Rebuild v3**：
> 否。 

**差異分析**：Q3 短命令 icon · dossier §四「NEGATIVE.」→「否。」canonical · shipped「無」是 `Nothing` 而非 `No`，語意錯
- 對應 dossier §六 範例 2 招牌短拒 icon

**推薦**：B (v3) — 語意 canonical 修正

---

### #60 · USE_OUR_SHIPS_AFTER · ✨ 全域升級 + Q5

**Shipped 主要問題**：吾等 × 3 · 薩-瑪特拉 × 1

**Rebuild v3**：
> 由於我等的改裝，將使你的旗艦顯著削弱\
> 你可能需要額外的戰鬥載具作為保護\
> 讓你能接近薩瑪特拉、足以引爆武器。\
> 我等將提供你我等新的化身級戰艦的設計圖。\
> 在稱職者手中，此艦足以與烏寬族、柯亞族的艦艇匹敵。

**差異分析**：Q2 · Q5 · 加逗號斷句 · 「及→、」(頓號更整齊)

**推薦**：B (v3)

---

### #61 · proceed · 🟠 措辭改變

**英文原文**：
> Very well. Proceed with the modifications.

**Shipped**：
> 好的。 繼續進行改裝。

**Rebuild v3**：
> 好。 開始改裝吧。

**差異分析**：「好的→好」（短一字 · 稍冷）· 「繼續進行改裝→開始改裝吧」（「繼續」是誤譯 · `proceed` 是「開始/推進」不是「繼續」；v3「開始改裝吧」+「吧」加親切感）

**推薦**：B (v3) — 語意修正

---

### #62 · TAKE_2_WEEKS · ✨ Q2 + 加逗號斷句

**Shipped**：吾等 × 1 · 「日期約為兩週後→預計約於兩週後完成」

**Rebuild v3**：
> 你艦艇的改裝，預計約於兩週後完成。\
> 為讓你與你的人類同伴，能在星際基地做任何必要的準備\
> 我等現在將立即把你與你的船員送回地球。\
> 祝你好運，艦長。

**差異分析**：Q2 · 加逗號斷句 · 「完成日期約為兩週後→預計約於兩週後完成」(語序更順)

**推薦**：B (v3)

---

### #63 · HELLO_AFTER_BOMB_1 · ✨ Q2

**Shipped**：吾等 × 1 · 「問候你→我等問候你」(v3 加主詞)

**Rebuild v3**：我等問候你，人類艦長。 你需要我等提供什麼？

**差異分析**：Q2 · 加主詞「我等」呼應 EN `WE GREET YOU` + 「你需要吾等什麼→你需要我等提供什麼」(語意更清楚)

**推薦**：B (v3)

---

### #65 · whats_up_after_bomb · 🟡 之→以後

**Shipped**：之後 → **Rebuild v3**：以後

**推薦**：B (v3) — 清除 之

---

### #66 · GENERAL_INFO_AFTER_BOMB_1 · ✨ 全域升級 + Q5 + 加逗號斷句

**Shipped 主要問題**：吾等 × 3 · 薩-瑪特拉 × 2 · 「柯亞族之戰」有之 · 「戰利」不完整（應為「戰利品」）

**Rebuild v3**：（12 行 · 略）

**關鍵差異**：
- Q2 · Q5 (2×) · 之清除 (「柯亞族之戰→柯亞族的戰爭」)
- 「有→是的」（`YES` 更完整）
- 「一:→一：」+「二:→二：」（半形冒號→全形）
- 加逗號斷句多處
- 「神聖戰利→神聖戰利品」（`sacred trophy` 完整）
- 「吾等就能與吾等盟友聯手擊敗→我等便能與我等的盟友聯手，擊敗」(加逗號)

**推薦**：B (v3)

---

### #67 · GENERAL_INFO_AFTER_BOMB_2 · ✨ Q2 + Q5

**Shipped**：吾等 × 2 · 薩-瑪特拉 × 2

**Rebuild v3**：
> 我等已將所知的一切告訴你。\
> 前往 <% comm.getConstellation("巨爵座", "samatra") %>（CRATERIS） 星座。 找到薩瑪特拉。 動用蟾亞族的力量。\
> 摧毀薩瑪特拉！

**差異分析**：Q2 · Q5 · 「已告訴你吾等所知一切→已將所知的一切告訴你」(語序更順)

**推薦**：B (v3)

---

### #68 · what_do_after_bomb · 🟡 微調

**Shipped**：所以現在我該做什麼？ → **Rebuild v3**：那，現在我該做什麼？

**差異分析**：「所以→那，」(EN `So NOW what do I do?` · v3 更貼 `so` 語氣)

**推薦**：B (v3) 或 A (shipped) — 皆通

---

### #69 · DO_AFTER_BOMB · ✨ Q5 + 之→時

**Shipped**：薩-瑪特拉 × 2 · 「陷入混亂之際」

**Rebuild v3**：
> 尋找薩瑪特拉的位置。 以最高速度飛往那裡！\
> 動用蟾亞族的力量，當烏寬族陷入混亂時，摧毀薩瑪特拉！

**推薦**：B (v3)

---

### #70 · bye_after_bomb · 🟡 加逗號

**Shipped**：希望結束後我能再見到你們。 → **Rebuild v3**：希望結束後，我能再見到你們。

**推薦**：A (shipped) — shipped 已通順，v3 加逗號更明顯，二者皆可

---

### #71 · GOODBYE_AFTER_BOMB · ✨ 招牌 icon 到位

**英文原文**：
> YOU ARE PREPARED. WITH COURAGE AND FORTUNE AT YOUR SIDE YOU WILL BE VICTORIOUS.

**Shipped**：
> 你已準備妥當。 有勇氣與運氣相伴，你將獲勝。

**Rebuild v3**：
> 你已準備完畢。 有勇氣與命運相隨，你將獲勝。

**差異分析**：「妥當→完畢」（EN `PREPARED` = 準備完畢，妥當偏「合適」）· 「運氣→命運」（`FORTUNE` = 命運/機運 · 有神明感）· 「相伴→相隨」
- 對應 dossier §六 範例 6

**推薦**：B (v3) — 神諭祝福 canonical

---

### #72 · bye · 🟠 措辭改變 + 之清除

**英文原文**：
> Farewell. We will be back when we've got everything we need.

**Shipped**：
> 再會。 我方湊齊所需之物後會回來。

**Rebuild v3**：
> 再會。 我方湊齊所需的一切後，就會回來。

**差異分析**：之物→的一切 · 加逗號 · 加「就」

**推薦**：B (v3) — 清除之

---

### #73 · GOODBYE · ✨ Q2

**Shipped**：吾等等候你的回歸。 → **Rebuild v3**：我等等候你的回歸。

**推薦**：B (v3)

---

### #74 · perhaps_not_install · 🟡 Q4 + 微調

**Shipped**：呃… 我其實還需要處理幾件事。 我方能延後改裝嗎？

**Rebuild v3**：呃…… 我其實還有幾件事要處理。 我方能延後改裝嗎？

**差異分析**：Q4 …→…… · 「還需要處理幾件事→還有幾件事要處理」(語序更口語)

**推薦**：B (v3)

---

### #75 · YES · ✨ Q3 短命令 icon

**英文原文**：
> YES.

**Shipped**：
> 可以。 

**Rebuild v3**：
> 是。 

**差異分析**：Q3 短命令 icon · 「可以→是」對稱 DEAD_SILENCE 的「否」形成 是/否 binary icon

**推薦**：B (v3) — icon 對稱

**替代**：C = 「可。」(若想更文言典雅)

---

### #76 · serious_1 · 🟠 措辭改變 + 之清除

**Shipped**：我方奮力想把所有種族從烏寬族**之下**解放。 我方需要你們的協助。

**Rebuild v3**：我方正努力將所有種族，從烏寬族的統治下解放出來。 我方需要你們的協助。

**差異分析**：之下→的統治下 · 「奮力想把→正努力將…解放出來」(語意更完整 · 「奮力想」暗示未行動，「正努力」是正在做的)

**推薦**：B (v3)

---

### #77 · serious_2 · 🟡 加逗號

**Shipped**：你們是我方贏回聯盟自由的關鍵。 → **Rebuild v3**：你們，是我方贏回聯盟自由的關鍵。

**差異分析**：加逗號斷句（正式外交口吻）· 玩家對神諭 Chmmr 的莊重宣告

**推薦**：A (shipped) 或 B (v3) — 皆通

---

## 附錄：🟢 12 identical tokens（不需決策）

以下 tokens shipped 與 v3 完全相同：
1. #5 find_out_whats_up
2. #7 need_help
3. #13 need_advice
4. #15 how_defeat_urquan
5. #17 what_about_tpet
6. #27 bye_shielded
7. #30 WHO_ARE_YOU
8. #31 i_am_captain
9. #48 where_weapon
10. #59 other_assistance
11. #64 HELLO_AFTER_BOMB_2
12. #78 silly

---

## Merge 建議

**若使用者批量決策**：
- 🟠 全依推薦（大多 = B v3）
- 🟡 全依推薦（各 half A/B · 皆通）
- ✨ 全 B (canonical 升級無爭議)
- 🟢 保留 shipped (自動 A)

**若逐項決策**，請以格式回覆：`#1=B  #2=B  #3=A  ...` 或 `🟡 全 A · 🟠 全依推薦 · ✨ 全 B`

Merge 後將：
1. Purity check `python _check_zh_purity.py --strict --race chmmr`
2. Backup shipped: `chmmr.zh-TW.pre-rebuild.bak`
3. Overwrite `chmmr.zh-TW.json` with merged version
4. Build + package `.\package_zh-TW.ps1`

---

**Total diff entries**：66 (54 needing decision + 12 🟢 auto-preserve)
