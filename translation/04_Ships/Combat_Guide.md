# Super Melee 戰鬥操作指南 Combat Guide

> **本檔涵蓋**：**25 族 melee 艦艇**的操作、武器機制、被動能力、戰術要點——**Super Melee 對戰用**。
> **資料來源**：**雙重交叉驗證**
> 1. UQM MegaMod 原始碼 `src/uqm/ships/<race>/<race>.c` 內的 `RACE_DESC` 結構、`SHIP_INFO` flag bits、preprocess handler
> 2. [Ultronomicon Wiki](https://wiki.uqm.stack.nl/) 每族詳細頁 + [Table of ship values](https://wiki.uqm.stack.nl/Table_of_ship_values)
>
> **譯名規範**：中文艦名／武器名依 [Ship_Names.md](../07_Glossary/Ship_Names.md) v0.5.2 canonical、[Weapon_Systems.md](../05_Technology/Weapon_Systems.md) 鎖定譯名、[Master_Glossary.md](../07_Glossary/Master_Glossary.md) §四。未鎖定的譯名以 *[暫譯]* 標記。
>
> **搭配閱讀**：陣營介紹見 [Alliance_Ships.md](Alliance_Ships.md)、[Hierarchy_Ships.md](Hierarchy_Ships.md)、[Neutral_Ships.md](Neutral_Ships.md)、[Player_Flagship.md](Player_Flagship.md)。

---

## 前言：Super Melee 是什麼？

**Super Melee** 是 Star Control II 內建的**艦艇對戰模式**：玩家從 **25 個艦種**中挑選、組成艦隊（fleet），每艘艦花費一定的**點數**（Melee cost），總點數上限預設 100。兩隊互轟到一方 fleet 全滅。

- **戰場**：無重力太空，中央 1 顆行星（會撞、有引力井 gravity well）
- **視角**：俯視 2D 
- **勝負**：擊沉對方最後一艘艦
- **特色**：每族機制**差異極大**——沒有「什麼艦最強」，只有「什麼艦在什麼手上、對什麼敵人最強」
- **時間單位**：1 秒 ≈ 24 frames（本檔全部冷卻／回能都以 frame 為單位，跟原始碼一致）

---

## 通用操作（PC / Android 對照）

| 動作 | PC 預設鍵 | Android 觸控 UI |
|---|---|---|
| 前進推進（Thrust） | ↑ | 類比搖桿推方向 / D-pad ↑ |
| 左右迴轉（Turn） | ← / → | 類比搖桿橫向 / D-pad ←→ |
| **主武器**（Weapon） | Return / Enter | 螢幕右下「**Weapon**」鍵 |
| **特殊武器**（Special） | Right Shift | 螢幕右下「**Special**」鍵 |
| 退出戰鬥（投降） | Esc | 選單 → Abort |

**注意**：
- 手機版預設**現代控制**（類比搖桿方向即為艦艏方向）
- 若切為**經典控制**（Classic），方向鍵僅左右轉艦、上鍵推進——與 PC 相同
- 玩 Super Melee 時可在**設定 → 控制**切換

**部分艦有非標準按鍵組合**（見各族章節）：
- **Orz Nemesis**：**按住 Special + 方向鍵 = 轉砲塔**（不轉船）· 按住 Special + 按 Fire = 放 Marines
- **Melnorme Trader**：**按住主武器蓄能**（不放）· 蓄越久顏色越深、傷害越高（綠→藍→紫→紅）
- **Kohr-Ah Marauder**：**按住主武器 = 刀刃 disc 向前飛**、**放開 = disc 定住原地追擊**
- **Chenjesu Broodhome**：**按住主武器 = 蓄能發射 whole crystal**、**發射後再按 = 讓晶體提前爆散成碎片**
- **Shofixti Scout**：Glory Device 需**按 3 次 Special 才引爆**（防誤按）
- **Pkunk Fury**：**按住主武器 + 按住轉向鍵**（不推進）= **Death Blossom 全方向散射**

---

## 讀懂數據表

每族的資訊表格為：

**Melee 分數**：N · **船體**：N/N · **能量**：N/N · **回能**：X unit/frame · **迴旋**：Y · **推進**：Z

- **Melee 分數**（Value/pts）：組隊時該艦扣多少點（滿 100）
- **船體**（Crew）：血量（船員數，最大值 / 起始值——多數艦最大=起始，除塞蓮外）
- **能量**（Battery）：能量條上限（起始通常滿）
- **回能**（Regen）：每 frame 自然恢復 N 能量。**特殊**：Pkunk / Slylandro / Utwig / Umgah 有不自然的回能機制，見各族說明
- **迴旋**（Turn rate）：每 frame 可轉的方向格數（16 方向系統）· 0 = 瞬轉
- **推進**（Max speed）：最高速度（world units/frame）· 40+ 為高速艦

每族武器欄：

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | 描述 | N 點 | N frame |
| **特殊** | 描述 | N 點 | N frame |

**冷卻**（refire delay）：發射後多少 frame 才能再發（0 = 每 frame 可發，等於連射）
每族章節底部有 **被動能力**（若有）、**戰術要點**（強項 / 弱點 / 剋星 / 小技巧）。

---

## 一、聯盟艦艇（Alliance）

新自由星系聯盟成員。多為玩家可招募或劇情中加入戰局。

### 1.1 晶智族 · 母巢艦（Chenjesu Broodhome）

**Melee 分數**：28 · **船體**：36/36 · **能量**：30/30 · **回能**：0.2/frame · **迴旋**：慢（0.142）· **推進**：慢（27）

> **定位**：**堡壘型晶體艦**——最重、最慢、能量池最大、雙武器都能反飛彈。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **光子晶體彈**（Photon Crystal Shard）——按住射出**整顆晶體**（傷害 6，一次只能一顆在場）· **發射後再按主武器 = 讓晶體提前爆散為碎片**（每碎片 2 傷）· 碎片可攔截敵飛彈 | 5 | 0（連按可爆散） |
| **特殊** | **DOGI 護艦戰機**（De-energizing Offensive Guided Interceptor）——放出戰機自動撞敵艦，**不造成傷害而是吸走敵方 10 點能量**！最多 4 隻同時 · 每隻 3 HP · 會避開敵艦前方 | **30**（全能量） | 0 |

**戰術**：
- **強項**：**遠距武器一體攻守**——晶體碎片可掃射與攔飛彈；DOGI 是**遊戲內反能量武器最強**（吸能量讓 Yehat/Utwig 護盾/Chmmr Zap 熄火）
- **弱點**：**轉向慢**（Turn 0.142 · 全遊戲第二慢）· 被高速艦繞後打死；DOGI 用一次要花全能量
- **小技巧**：
  - **連按主武器**攔截敵飛彈牆——特別是 Ur-Quan Fusion Bolt、Earthling Nuclear、Spathi BUTT
  - **對 Yehat Terminator 放 DOGI 吸乾能量**——讓 Yehat 開不了盾
  - **對 Utwig Jugger 同樣**——DOGI 吸能讓 Jugger 主炮和盾都空

---

### 1.2 姆姆族 · 變形艦（Mmrnmhrm Transformer / X-Form）

**Melee 分數**：19 · **船體**：20/20 · **能量**：10/10 · **回能**：**X-Wing 0.29、Y-Wing 0.14 /frame**（雙形態不同）· **迴旋**：X-Wing 快（0.33）· Y-Wing 慢（0.07）· **推進**：X-Wing 慢（20）· Y-Wing 極快（50）

> **定位**：**雙形態切換艦**——X-Wing 慢重砲、Y-Wing 快追蹤。切換時消耗全能量。

**X-Wing 形態**（戰機形態）：

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **雙管雷射**（Laser cannons）——短程雙束能量束 · 高傷 | 1 | 0 |
| **特殊** | 切換到 Y-Wing | **10**（全能量） | 0 |

**Y-Wing 形態**（飛彈形態）：

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **雙管追蹤飛彈**（Missiles）——遠距、慢追蹤、單發傷害低 | 1 | 20 |
| **特殊** | 切換到 X-Wing | **10**（全能量） | 0 |

**戰術**：
- **強項**：**X-Wing 貼身雙雷射秒殺輕艦** + **Y-Wing 拉開遠距磨死**——雙形態互補
- **弱點**：**切換消耗全能量**（脆弱期）· 船體只 20
- **小技巧**：
  - **經典打法**：Y-Wing 拉開距離 → 切 X-Wing 逼近 → 連雷射 → 敵艦逃時切回 Y-Wing 追飛彈
  - **VUX Limpet 分別作用兩形態**——X 中被貼 limpet 只影響 X-Wing 機動性、Y-Wing 切換後沒事（Paul Reiche 官方設計）
  - **Y-Wing 加速時切 X-Wing**——會保留 Y-Wing 慣性衝速，一波高傷 strafe run

---

### 1.3 查姆族 · 復仇號（Chmmr Avatar）

**Melee 分數**：30（最貴之一）· **船體**：42/42 · **能量**：42/42 · **回能**：0.5/frame · **迴旋**：0.25 · **推進**：中（35）

> **定位**：**遊戲內單艦最強**——最高船體與能量、瞬回能、雙武器 + 三顆自動 Zap 衛星。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **重型 X 光雷射**（Heavy X-ray Laser）*[暫譯]*——短程 · 每 frame 2 傷 · 按住連續發射 · 每秒可打 24 次！ | 2 | 0 |
| **特殊** | **牽引光束**（Tractor Beam）——**拉近敵艦**（依敵艦質量）· 對**非慣性艦**（Arilou / Guardian Blazer / Slylandro Probe）**無效** | 1 | 0 |

**被動能力**：
- **Zap 衛星**（ZapSats）——**3 顆軌道衛星自動繞艦飛行、自動追瞄敵艦與飛彈**。玩家不用按鍵，衛星自主開火。每顆 10 HP，被打光就沒了。**衛星全滅後 Chmmr 立即變得脆弱**。

**戰術**：
- **強項**：**全能爆表**——高船體 + 高能量 + 高回能 + 雷射每秒 24 打 + 3 顆自動衛星
- **弱點**：**衛星是命根**——被 Shofixti Glory / Utwig 重矛 / Kohr-Ah 刀刃打光就沒有 Zap 支援；**16 方向雷射有盲角**（敵艦可站在雷射線之間死角開火）；**Shofixti 榮耀彈可秒殺 2-3 顆 Zap 衛星**
- **小技巧**：
  - **牽引光束 + 主雷射連鎖**——抓住敵艦拉近 → X 光雷射秒殺（每秒 48 傷）
  - **預先牽引 Arilou 快艇即將傳送的方向**——雖然對 Arilou 本體無效，但可干擾其他敵艦
  - **對 Shofixti 保持距離**——榮耀彈近距爆炸會秒吃 2-3 顆 Zap

---

### 1.4 翼哈特族 · 終結者（Yehat Terminator）

**Melee 分數**：23 · **船體**：20/20 · **能量**：10/10 · **回能**：0.29/frame · **迴旋**：0.33 · **推進**：中（30）

> **定位**：**騎士式對決艦**——雙脈衝砲 + 電力防護罩。攻守全能貼身戰之王。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **雙脈衝砲**（Twin Ion Pulse Cannons）——雙管前置能量彈 · **一波齊射可秒殺 Androsynth Guardian** | 1 | 0（連射） |
| **特殊** | **防護罩**（Force Shield）——展開**能量護盾**擋幾乎所有攻擊 · 只有 **Syreen Song / VUX Limpet / Shofixti Glory Device / 撞行星**能穿 | 1 | 2 |

**戰術**：
- **強項**：**護盾無敵**——擋 Nuclear、BUTT、Plasmoid、Fusion、Fried、Zap Laser 等全部；**主武器連射夠猛**
- **弱點**：**能量條只 10**——長時間開盾會空；被 Chenjesu DOGI 吸乾能量就崩；**護盾不擋自爆與 Limpet**
- **小技巧**：
  - **面對敵艦火力方向開盾 → 對方彈藥用完 → 反擊**
  - **對 Ur-Quan Dreadnought 的融合彈**：開盾接住 → 開砲反擊，經典硬碰硬
  - **警戒 Chenjesu Broodhome 的 DOGI**——DOGI 會吸乾能量讓護盾沒用

---

### 1.5 修烈士族 · 偵察艦（Shofixti Scout）

**Melee 分數**：5（最便宜）· **船體**：6/6（最脆）· **能量**：4/4 · **回能**：0.1/frame · **迴旋**：極快（0.5）· **推進**：快（35）

> **定位**：**神風武士艦**——最便宜、最脆、但**自爆能秒殺任何艦**。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **麻煩鏢**（Mendōkusai Energy Dart）*[暫譯]*——「メンドクサイ」（麻煩）· 弱到只殺 1 名船員 · 但連射夠快 | 1 | 3 |
| **特殊** | **榮耀彈**（Glory Device）——**引爆自艦**！**需按 3 次 Special 才引爆**（防誤按）· 引爆時螢幕會顯示引爆倒數 · **爆炸範圍極廣、傷害極高** · 引爆時大喊「For the Glory of the Empire!」| 0 | 一次性 |

**戰術**：
- **強項**：**分數 5** = 組隊可買 6 艘當「秒殺筒」；**Glory Device 秒殺任何艦**（包括 Chmmr！）
- **弱點**：船體 6，一發 Fusion Bolt 就沒；主武器超弱
- **小技巧**：
  - **衝到敵艦身邊 → 三按 Special → 大喊 Banzai**
  - **對 Chmmr Avatar**：Glory 可**秒殺 2-3 顆 Zap 衛星**；剩下的 Chmmr 就好對付
  - **對 Yehat / Utwig**：護盾**擋不住 Glory**——正面撞上去即可
  - **可秒殺的小艦**（船員少）：Arilou Skiff、Druuge Mauler、Orz Nemesis、Pkunk Fury、Thraddash Torch、Umgah Drone、ZFP Stinger、Slylandro Probe、另一個 Shofixti
  - **AI exploit**：VUX / Umgah / Ur-Quan / Ilwrath 的 AI 有 bug 會被麻煩鏢繞圈耍

---

### 1.6 阿麗露 · 快艇（Arilou Skiff）

**Melee 分數**：16 · **船體**：6/6（極脆）· **能量**：20/20 · **回能**：0.142/frame · **迴旋**：**瞬轉（0.5，等同 0 慣性）**· **推進**：**非慣性 40**（瞬速、瞬停）· **質量**：1（不受重力影響）

> **定位**：**瞬移雷射艇**——自動追蹤雷射 + 傳送。極度靈活、**免疫行星重力**。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **自動追蹤雷射**（Auto-aiming laser）——360 度自動瞄敵艦 · 玩家不用瞄準 · 弱傷但穩打 | 2 | 1 |
| **特殊** | **傳送**（Teleport）——**隨機傳送到戰場任意位置** · **可能傳到行星內或敵艦內 = 秒死**（罕見但致命） | 3 | 2 |

**被動能力**：
- **無慣性 + 免疫重力**——不受行星引力影響，可貼行星飛過去而不被拉入
- **是遊戲內唯一 tractor beam 無效的艦**（連 Chmmr 都拉不動）

**戰術**：
- **強項**：**追蹤雷射不用瞄** + **免疫重力** + **傳送躲彈**
- **弱點**：船體 6 = 一發重砲就沒；傳送**有機率傳到行星／敵艦內秒死**
- **小技巧**：
  - **經典打法**：直接鎖敵艦 → 拿雷射慢慢磨 → 對方接近時傳送逃
  - **行星伏擊**：躲在行星背面 → 敵艦繞過來吃引力井 → 雷射 + 傳送擊敵撤退
  - **對 Chmmr Avatar** 特別強——重力免疫 + 傳送躲雷射 · 但要小心 Zap 衛星（會跟你走）

---

### 1.7 塞蓮族 · 穿透艦（Syreen Penetrator）

**Melee 分數**：13 · **船體**：**12/42**（起始 12、最大 42）· **能量**：16/16 · **回能**：0.142/frame · **迴旋**：0.5 · **推進**：快（36）· **質量**：2（輕）

> **定位**：**唯一「吸敵艦船員」艦**——塞蓮之歌讓敵艦船員叛逃來當自己船員（同時削弱敵艦）。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **粒子束**（Particle Beam Stiletto）——短程能量束 · 每擊殺 2 船員 · 主要用於**最後 KO 抗心控的敵艦長** | 1 | 8 |
| **特殊** | **塞蓮之歌**（Syreen Song）——脈衝一次，**周圍敵艦船員叛逃**（越近吸越多、每次最多 8 人）· 叛逃船員以綠點浮向 Syreen · 若被敵艦回收會回去；若被行星吸入則死亡 · **敵艦被吸下的船員可讓 Syreen 血量增加**（起始 12 可養到 42！） | 5 | 10 |

**被動能力**：
- **船員可長到 42**（起始 12 · 吸敵人船員養到滿）——**唯一自帶回血機制的艦**
- **歌對機械艦無效**（Slylandro Probe · **不影響** Mmrnmhrm——Paul Reiche 說 X-Form 是機械但**會**受歌影響）

**戰術**：
- **強項**：**唯一自帶補血**——對大艦（Ur-Quan 42 船員）狂唱歌能吸滿
- **弱點**：粒子束射程短，需貼身；歌**對 Slylandro Probe 無效**
- **小技巧**：
  - **保持中距離**→ 唱歌吸幾波 → 粒子束收尾
  - **對 Yehat Terminator**：歌**可穿護盾**（護盾擋不住 Syreen Song）！
  - **對 VUX Intruder**：歌**可穿護盾**（同上）
  - **不要離敵艦太近**——敵艦會用主武器把叛逃的船員打死（叛逃船員以浮空綠點回航）

---

### 1.8 地球 · 巡邏艦（Earthling Cruiser）*[暫譯]*

**Melee 分數**：11 · **船體**：18/18 · **能量**：18/18 · **回能**：0.111/frame · **迴旋**：0.5 · **推進**：慢（24）

> **定位**：**經典人類遠距艦**——追蹤核彈 + 點防禦雷射。SC1 傳承。
> **譯名備註**：`Earthling Cruiser` 目前無 canonical · 暫用「**巡邏艦**」（沿用 [Player_Flagship.md](Player_Flagship.md) 內 Tobermoon = 星控巡邏艦 Cruiser 的譯法）· 請 Phase 8 確認

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **核彈飛彈**（"Fire-and-Forget" Nuclear Missile）*[暫譯]*——長距**追蹤飛彈** · 每彈 4 傷 · 可被防禦系統攔截 · 基於冷戰 Peacekeeper 飛彈 | 9 | 10 |
| **特殊** | **點防禦雷射**（Point-Defense Laser）*[暫譯]*——**自動攔截周圍敵飛彈與 asteroid**（不主動攻擊敵艦） · 每雷射 1 傷 · 消耗**固定** 4 能量無論打幾發 · 基於 1980s SDI「星戰」計畫概念 | 4 | 9 |

**戰術**：
- **強項**：**點防禦是遊戲內第二強反飛彈系統**（僅次 DOGI）；核彈追蹤命中傷害大
- **弱點**：核彈冷卻 10 + 9 能量 · 續航壓力大；船體 18 中等；核彈**可能追蹤自己**（若敵艦躲開）
- **小技巧**：
  - **遠距發射核彈** + **保持點防禦開著**——經典 Pillbox 戰法
  - **對 Spathi Eluder** 剋制：核彈追進 Spathi 屁股（Spathi 逃跑時屁股朝向 Cruiser）
  - **對 Slylandro Probe**：點防禦擋不住 Lightning（非彈藥）· Cruiser 挺容易被 Slylandro 玩死
  - **注意反彈**：核彈可能繞回撞自己——點防禦可攔下（但**同時開兩武器**：核彈不會被自己雷射打，但能量會扣兩份）

---

## 二、階層艦艇（Hierarchy）

烏寬戰奴階層成員。多為劇情敵對艦艇，Super Melee 對戰時可自由選用。

### 2.1 烏寬克澤札 · 無畏艦（Ur-Quan Kzer-Za Dreadnought）

**Melee 分數**：30（最貴之一）· **船體**：42/42 · **能量**：42/42 · **回能**：0.14/frame · **迴旋**：慢（0.2）· **推進**：中低（30）· **質量**：10

> **定位**：**戰爭平台**——巨型融合彈 + 自主戰機群。**攻守全能**、遊戲代言艦。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **融合彈**（Fusion Blaster）——追蹤能量彈 · 每彈 **6 傷** · 命中大艦幾乎必秒 | 6 | 6 |
| **特殊** | **自主戰機**（Autonomous Fighters）*[Fighter Bay]*——一次放 2 架小型戰機 · 有生存時限、需回艦補油 · 撞上 asteroid 會死 | 8 | 9 |

**戰術**：
- **強項**：能量池 42 + 追蹤主武器 + 群戰 Fighter；船體 42 硬吃打
- **弱點**：**Fighter 怕**：Chmmr Zap 衛星、Chenjesu 晶體碎片、Yehat 護盾、Earthling 點防禦、Marauder F.R.I.E.D. 環繞火焰；轉向慢
- **小技巧**：
  - **遠距輸出**：放 Fighter 拖住敵艦 → 融合彈連射
  - **對 Slylandro Probe** 特別怕——Lightning 電擊會吸走能量
  - **對 Utwig Jugger**：融合彈打護盾時**能量會被護盾吸走並補給 Utwig**——**慎用！**先耗光 Utwig 能量再開火

---

### 2.2 烏寬柯亞 · 掠奪者（Ur-Quan Kohr-Ah Marauder）

**Melee 分數**：30 · **船體**：42/42 · **能量**：42/42 · **回能**：0.2/frame · **迴旋**：0.2 · **推進**：30 · **質量**：10

> **定位**：**旋轉刀刃屠殺者**——遠距刀刃 + 環繞火環。**近身無死角**、儀式化屠殺。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **旋轉刀刃**（Spinning Blade-Disc）——**按住時 disc 一直向前飛**、**放開時 disc 定住原地**、**敵艦靠近時 disc 會自動追擊**（短距追蹤）· 每 disc 4 傷 · 幾乎無限射程 | 6 | 6 |
| **特殊** | **F.R.I.E.D.**（Fiery Ring of Inevitable and Eternal Destruction）——**環繞艦身的環狀火焰**（不是後方而是全周）· 每個火焰雲 3 傷 · **可撞下敵艦所有飛彈**（包括 Fusion Bolt、Nuclear、BUTT、Plasmoid）· 一次 21 能量（半條） | 21（半能量） | 9 |

**戰術**：
- **強項**：**主武器 disc 可佈陣**——放幾片 disc 讓敵艦困在其中；F.R.I.E.D. 是**遊戲內最強反彈幕**（可撞下 Melnorme 蓄能彈與 Fusion Bolt）
- **弱點**：機動性差；對護盾艦（Yehat / Utwig）disc 傷害被擋
- **小技巧**：
  - **佈陣戰術**：發 4-5 片 disc 圍住敵艦 → disc 自動追擊敵艦 → 幾秒內敵艦死
  - **對 Chmmr Avatar**：F.R.I.E.D. 貼身可**同時打光多顆 Zap 衛星** + 打 Chmmr 本體
  - **對 Shofixti**：F.R.I.E.D. 引爆前秒殺 Shofixti（Glory 沒引就沒了）
  - **對 Utwig Jugger**：**避免用 F.R.I.E.D.**（會被護盾吸能量補給敵艦）

---

### 2.3 麥孔 · 莢艦（Mycon Podship）

**Melee 分數**：21 · **船體**：20/20 · **能量**：40/40（大能量池）· **回能**：0.2/frame · **迴旋**：慢（0.14）· **推進**：中低（27）· **質量**：7

> **定位**：**再生型有機艦**——追蹤電漿團 + 自我修復。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **電漿團**（Homing Plasmoid）——長距**追蹤電漿彈**、隨距離衰減、貼身傷害巨大 · **一次只能一顆在場** · **速度慢到 Podship 可能追過自己的彈**（撞上自己是常見死因）| 20 | 5 |
| **特殊** | **再生船員**（Regenerate crew）——**消耗全部能量**、瞬間補 4 名船員 · 補完後不能立即發射主武器（沒能量） | **40**（全能量） | 0 |

**戰術**：
- **強項**：**唯一能自我補船員**（不用像 Syreen 吸敵人）；電漿團貼身傷害巨大
- **弱點**：**轉向 0.14 慢** + 電漿團會追自己（自殺風險）；補血時能量歸零 = 空窗
- **小技巧**：
  - **保持中距離** → 發電漿 → 敵艦逼近時**轉頭朝後打**（避免撞自己的彈）
  - **對 Zoq-Fot-Pik / Pkunk / Arilou**：他們可以**引誘電漿團回射麥孔本體** = 麥孔自殺
  - **血低時撤退再補**——補完等能量回滿再回戰場

---

### 2.4 史怕 · 迴避者（Spathi Eluder）

**Melee 分數**：18 · **船體**：30/30（高船體）· **能量**：10/10 · **回能**：0.091/frame（慢） · **迴旋**：0.5 · **推進**：**極快（48，全遊戲第二快）**· **質量**：7

> **定位**：**打不贏就跑，跑時朝後打**——高速逃跑 + 屁彈後射。原始碼 flags: `FIRES_FORE | FIRES_AFT | SEEKING_SPECIAL | DONT_CHASE`（前射主 · 後射追蹤特殊 · AI 不追擊）

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **前置機槍**（Forward Mounted Gun）*[暫譯]*——連射低傷小彈（每彈 1 傷）· 射程短、彈速快 · 適合打小艦與**攔敵飛彈** | 2 | 0（連射） |
| **特殊** | **屁彈飛彈**（B.U.T.T. Missile）——**Backwards Utilizing Tracking Torpedo**、**從艦艇後方發射**的追蹤飛彈！每彈 2 傷 · 中距、慢速、可追蹤 | 3 | 7 |

**戰術**：
- **強項**：**推進 48 全遊戲第二快**（僅次 Pkunk）；BUTT 對追擊者最惡毒——**追史怕 = 自尋死路**；船體 30 硬
- **弱點**：主武器很弱；能量條只 10（BUTT 三發就空）；能量回復慢（0.091/f = 每 11 frame 才回 1）
- **小技巧**：
  - **經典打法**：**朝敵艦反方向跑** → 拉開距離 → 敵艦追來時 BUTT 自動命中
  - **對 Chenjesu / Ur-Quan / Chmmr / Utwig**：拿 BUTT 慢慢磨（他們追不上你）
  - **對 Arilou / Skiff / Pkunk / Slylandro Probe**：**你追不上他們**——只能拿前置機槍反射他們的追蹤武器
  - **注意 BUTT 會撞自己**：如果 Eluder 屁股沒完全朝敵艦、BUTT 可能繞回打自己

---

### 2.5 陰嘎 · 蜂機艦（Umgah Drone）

**Melee 分數**：7（很便宜）· **船體**：10/10 · **能量**：**30**（很多！）· **回能**：**「chunk regen」**——武器一段時間沒用會**整條補滿** · 用武器時**回能停止** · **迴旋**：0.2 · **推進**：慢（18）· **質量**：1（超輕）

> **定位**：**惡作劇怪艦**——前置反物質錐 + 瞬速倒退。獨特能量機制。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **反物質錐**（Anti-matter Cone）——前置扇形反物質噴射 · 短距 · 傷害高 · **可攔截大部分敵飛彈** · **不耗能**！但**開啟時能量條停止恢復** | **0** | 0（按住持續） |
| **特殊** | **後退推進器**（Retro-Propulsion）——**瞬間向後高速跳躍**（**非慣性瞬速**）· 消耗大量能量 · 停止時瞬間停下 | 1/frame | 2 |

**戰術**：
- **強項**：**主武器不耗能**（免費輸出）；後退推進**是遊戲內最快移動方式**（非慣性瞬速）
- **弱點**：正常前進超慢（推進 18）· 需要靠後退推進近距離貼身；能量若被榨乾就危險
- **小技巧**：
  - **經典打法**：**後退推進 → 突然停住 → 打開錐 → 敵艦撞上**
  - **「後退進攻」**：面朝敵艦，用後退推進**向後撤** → 拿錐防禦追擊 · **反轉方向 = 用錐往敵艦衝**
  - **對慢艦**（Broodhome / Dreadnought）：後退推進貼臉一波流
  - **拿反物質錐擋 asteroid**：小行星撞過來時 Umgah 質量 1 會被彈飛（可利用彈飛拉開距離）

---

### 2.6 VUX · 入侵者（VUX Intruder）

**Melee 分數**：12 · **船體**：20/20 · **能量**：**40**（大能量池）· **回能**：0.111/frame · **迴旋**：慢（0.142）· **推進**：慢（21）· **質量**：6

> **定位**：**貼身糾纏艦**——雷射為主 + 吸附雷永久減速。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **雷射**（Gigawatt Laser）——短距強力雷射 · 每 frame 打擊 | 1 | 0（按住連續） |
| **特殊** | **吸附雷**（Limpet）——貼在敵艦上**永久減速**（累積）· 每貼一顆 +1 turn_delay、+1 acceleration_delay、-1 acceleration_increment（下限 4）· 速度變 8 就到底 · **可穿 Yehat / Utwig 護盾**！ | 2 | 7 |

**被動能力**：
- **Warp-In**——VUX 出場時**傳送到極接近敵艦的位置**！Super Melee 起始時可能**瞬間貼臉**（如果對手沒動、可能秒殺）

**戰術**：
- **強項**：**Limpet 累積永久減速** · 貼幾顆後**任何快艦（Pkunk / Arilou / Spathi）都變烏龜**；能量池 40 續航好；Warp-in 突襲
- **弱點**：轉向慢 + 推進慢，只擅長貼身；被遠距追蹤武器打慘（Nuclear / Plasmoid / Melnorme 蓄能）
- **小技巧**：
  - **經典打法**：先發 3-4 顆 Limpet → 雷射慢慢磨
  - **對 Spathi Eluder 剋制**：貼 4 顆 Limpet 讓它跑不動 → 雷射秒殺
  - **對 Yehat / Utwig**：Limpet **穿護盾**——他們對 VUX 特別怕
  - **對 Mmrnmhrm**：VUX 特別強——因為 Limpet 只作用當前形態、但持續累積

---

### 2.7 安卓辛 · 守衛艦（Androsynth Guardian）

**Melee 分數**：15 · **船體**：20/20 · **能量**：24/24 · **回能**：0.111/frame · **迴旋**：X-form 慢（0.2）· Blazer form 快（0.5）· **推進**：X-form 中（24）· **Blazer form 極快（60，非慣性瞬速）**· **質量**：6

> **定位**：**雙形態衝擊艦**——泡泡遠距 + Blazer 火球衝撞。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **泡泡彈**（Molecular Acid Bubbles）——酸性泡泡緩慢追蹤 · 每泡 2 傷 · 不會傷自己 · 有慣性移動 | 3 | 0 |
| **特殊** | **燃燒衝撞形態**（Blazer Form）——變身**非慣性高速火球**（推進 60）· **每撞殺 3 名敵艦船員** · **持續消耗** 2 能量/frame 直到能量歸零 → 自動變回普通形態 | 2/frame | 0（連續） |

**戰術**：
- **強項**：**Blazer 撞擊是遊戲內近戰最強單體傷害**；Blazer 卡進敵艦裂縫（Orz 後鰭、Chmmr 翅、Spathi 觸手）**可秒殺**！泡泡遠距壓制
- **弱點**：Blazer 每 frame 2E · 撐不久；正常形態轉向慢
- **小技巧**：
  - **經典打法**：Blazer 撞敵艦裂縫（wedging）——很多艦有結構弱點
  - **對 Chmmr Avatar**：**避免正面 Blazer**——Zap 衛星會打你；從側面 wedge
  - **對 Yehat**：護盾**能擋 Blazer**——泡泡先耗盾再撞
  - **能量低時 Blazer 短跳**：低能量下 Blazer 可**跳一小段** = 突襲或閃避
  - **知名 bug**：Chenjesu DOGI 吸乾 Blazer 能量時，Blazer form 不完全關閉——仍能撞人

---

### 2.8 蛛狂 · 復仇者（Ilwrath Avenger）

**Melee 分數**：10 · **船體**：22/22 · **能量**：16/16 · **回能**：**0.8/frame**（**極快！**）· **迴旋**：0.33 · **推進**：慢（25）· **質量**：7

> **定位**：**隱身火焰突襲艦**——隱身接近 + 近距離火焰噴流。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **火焰噴流**（Hellfire Spout）——短距火焰 · 每 frame 1 傷 · 回能極快可幾乎不間斷噴 | 1 | 0（按住連續） |
| **特殊** | **隱身裝置**（Cloaking Device）——**完全隱形**、自動追蹤武器（Autotracking Laser / DOGI / BUTT / Plasmoid / Nuclear）**失效** · **敵艦看不到 Ilwrath** · 但 Super Melee 鏡頭仍會顯示位置 · **Hellfire 與 Cloak 不能同時**——**開火會自動關 cloak** · 關 cloak 後艦艏會**自動朝敵艦**（無論之前朝哪） | 3 | 13 |

**戰術**：
- **強項**：**回能 0.8/f 全遊戲最快**（可幾乎不間斷噴火）；隱身讓自動追蹤武器失效
- **弱點**：**推進 25 慢**（Ilwrath 阿基里斯腱）；火焰射程極短，需貼身
- **小技巧**：
  - **經典打法**：隱身接近 → 貼上敵艦 → 開火（同時解隱）→ 對方反應不過來
  - **對 Chenjesu Broodhome**：隱身讓 DOGI 追不到（DOGI 靠自動鎖定）
  - **對 Arilou Skiff**：隱身讓自動追蹤雷射失靈——Skiff 幾乎打不到你
  - **無法追上快艦**：Pkunk / Spathi / Slylandro Probe 跑掉時 Ilwrath 追不上——**只能繞行星 gravity whip**
  - **cloak 期間 Ilwrath 玩家會看不清自己朝向**——建議短暫解隱重新定位

---

### 2.9 斯萊探測器（Slylandro Probe）

**Melee 分數**：17 · **船體**：12/12 · **能量**：20（但**初始 0** · 需靠吸 asteroid 補）· **回能**：**0** · **迴旋**：0.5 · **推進**：**極快（60，全遊戲最快加速）**· **質量**：1

> **定位**：**機械電擊艦**——超高速非慣性 + 電擊武器 + 吸 asteroid 補能量。**推進機制獨特**！
>
> **重要**：Melee 版的 Probe 是 `slylandr.c`（不是 `probe/`——後者是星圖遭遇用）。**沒有自我複製**（那是**星圖版**的機制）。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **閃電武器**（Lightning）——短距電擊敵艦 · **開火時 Probe 需接近敵艦** · Ultronomicon 說：「lightning discharge 不是設計為武器，是 Probe 想把敵艦分解為 consumable particles」 | 2 | 17 |
| **特殊** | **能量化 / 吸收隕石**（Energize）*[暫譯]*——**吸收周圍 asteroid**、**一顆隕石補滿整條能量** · 若戰場沒 asteroid 就沒用 | 0 | 20 |

**被動能力**：
- **獨特推進**：**按推進鍵 = 瞬間反向**！（不是加速而是轉向）· Probe 永遠在動、永遠往加速鍵方向漂
- **免疫塞蓮之歌**（機械無心靈）

**戰術**：
- **強項**：**加速 60 全遊戲最快** + **瞬轉** + 吸 asteroid 補能量 = **持久戰之王**；閃電對能量武器艦（Yehat/Utwig）特別怕
- **弱點**：閃電射程短；能量條初始 0（不吸 asteroid 就沒能量開武器）；控制方式難學（大量玩家不熟）
- **小技巧**：
  - **經典打法**：先繞 asteroid 補滿能量 → 電擊敵艦 → 再回找 asteroid
  - **對 Ur-Quan Dreadnought / Chenjesu Broodhome 極強**——他們機動不足追不上你
  - **AI Probe 常見打法（Ultronomicon 引述）**：「close in, evade fire, empty batteries, zip off to find asteroid, repeat」
  - **可躲 Pkunk 的 Death Blossom + Earthling 的核彈**——反射快、非慣性
  - **對 Spathi Eluder**：Spathi 用 BUTT 遠距磨 Probe——**Probe 挺怕**（Spathi 跑得也快）

---

## 三、中立艦艇（Neutral）

未加入任何陣營的獨立艦艇。多為劇情中觸發條件加盟的可買艦。

### 3.1 憂特 · 重砲艦（Utwig Jugger）

**Melee 分數**：22 · **船體**：20/20 · **能量**：20/20 · **回能**：**0**（**只能靠護盾吸傷害回能**！）· **迴旋**：0.5 · **推進**：36 · **質量**：8

> **定位**：**受傷回能反擊艦**——「悲愴即是力量」的物理化：**被打越多能量越滿**。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **能量矛**（Energy Spears）*[暫譯]*——**六管前置能量矛**（一次齊射 6 發廣角）· 每矛殺 1 名敵艦船員 · **不耗能**（無限發射）! | **0** | 7 |
| **特殊** | **憂特防護罩**（Absorption Shield）*[暫譯]*——**擋所有動能與熱能攻擊** · **吸收傷害轉為能量**（每受一擊 = +能量）· **主武器不能與護盾同時開** · 護盾**擋不住**：Chenjesu DOGI（吸能量）、VUX Limpet（穿透）、Melnorme Confusion Ray（穿透）、Shofixti Glory Device（穿透）、撞行星 | 1 | 12 |

**戰術**：
- **強項**：**主武器不耗能**（無限開火）· 護盾吸傷害回能——被打越多能量越滿 · Melnorme 蓄能彈、Ur-Quan Fusion Bolt、Chmmr Zap 都補給 Utwig
- **弱點**：**能量只靠護盾回**——沒被打時能量枯竭；能量矛冷卻 7 frame 慢；行星碰撞是弱點
- **小技巧**：
  - **經典打法**：**主動迎向敵艦火力** → 開護盾吸能 → 敵艦火力停時開矛反擊
  - **對 Ur-Quan Dreadnought**：Fusion Bolt 打護盾直接補能——Utwig 完克 Ur-Quan！
  - **對 Chenjesu Broodhome**：**警戒 DOGI**（吸乾能量）——Utwig 對 Chenjesu 挺難
  - **對 Kohr-Ah Marauder**：F.R.I.E.D. 打護盾也補能量——Utwig 也剋 Kohr-Ah
  - **Ultronomicon 引述**：「Jugger 是遊戲內少數能打贏 Sa-Matra 的艦」（僅次 Pkunk Fury）
  - **弱點反諷**：**Mmrnmhrm 飛彈**（低傷慢速）反而剋 Utwig——每擋一發飛彈耗的能量比補的多！

---

### 3.2 蘇菩 · 鋒刃艦（Supox Blade）

**Melee 分數**：16 · **船體**：12/12 · **能量**：16/16 · **回能**：0.2/frame · **迴旋**：0.5 · **推進**：快（40）· **質量**：4

> **定位**：**四向獨立推進艦**——可**橫向與後向移動而不轉身**，全遊戲最靈活。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **漿團發射器**（Glob Weapon）——酸性漿團連射 · 中距 · 高彈速 · **能量沒了也能繼續射（減緩速率）** | 2 | 1 |
| **特殊** | **四向機動**（Advanced Maneuvering）——**啟動時**：左右鍵變成**橫向平移**、上鍵保持前進 · **可邊平移邊開火** · **不耗能**！ | **0** | 0 |

**戰術**：
- **強項**：**四向推進讓 Supox 邊射邊平移**——躲彈+開火同時進行；漿團連射穩定；即使能量歸零仍能開火（reduce clip）
- **弱點**：船體 12（脆）；漿團傷害不高
- **小技巧**：
  - **經典打法**：開特殊 → 側向繞圈 → 邊繞邊射
  - **反向逃跑**：面朝敵艦、反向推——**Relativity Effect** 讓漿團打敵艦時多一份追擊力
  - **對 Chenjesu Broodhome / Ur-Quan Dreadnought**：四向靈活迂迴、遠距磨
  - **對 Arilou Skiff**：Supox 難命中對方——**貼身用漿團密集開火較好**

---

### 3.3 普恩 · 烈憤艦（Pkunk Fury）

**Melee 分數**：20 · **船體**：8/8（極脆）· **能量**：12/12 · **回能**：**0**（**只能靠罵髒話補能量**！）· **迴旋**：**瞬轉（1）**· **推進**：**極快（64，全遊戲最快）**· **質量**：1

> **定位**：**神風高速三管砲艦 + 復活**——**全遊戲最快** + **罵髒話補能** + **50% 機率復活**。

原始碼 flags: `FIRES_FORE | FIRES_LEFT | FIRES_RIGHT` = 主武器**三個方向同時射**！

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **三連發彈**（Triple-Mounted Minigun）——**前 / 左 / 右三方向同時發射**每次射 3 顆散射彈 · 每彈 1 傷 · **可打下敵飛彈** | 1 | 0（連射） |
| **特殊** | **嘲諷罵髒話**（Insult）——**產生 2 能量**（*不是*消耗！）· 冷卻 16 frame · **是 Pkunk 唯一補能量的方式** | **產出 +2** | 16 |

**被動能力**：
- **復活**（Reincarnation）——**被摧毀時 50% 機率原地滿血滿能量復活**、大喊「I have returned!」 · 一場戰鬥可能復活多次（隨機）
- **無自然 regen**——沒有 taunt 就沒能量

**戰術**：
- **強項**：**推進 64 全遊戲最快** + **瞬轉** + **可復活** + **三方向散射打擊**——Ultronomicon 說「Fury 是打 Sa-Matra 最佳艦」
- **弱點**：船體 8——一發 Fusion / F.R.I.E.D. 就沒；能量恢復慢（每 16 frame 才 +2）
- **小技巧**：
  - **經典打法**：**繞圈打帶跑**——三管齊射範圍廣、拉近打完就跑
  - **Death Blossom**：**按住主武器 + 按住轉向鍵（不推進）** = 原地旋轉三方向掃射 · 對包圍敵艦特別有效 · **但視覺華麗、實際傷害不如手動瞄準**
  - **戰鬥時整場按住 Special**——最大化 taunt 回能
  - **對付 Slylandro Probe**：Probe 能躲 Death Blossom（非慣性）—— 你追不到、他也不追你
  - **側射攻擊 (Broadside)**：飛過敵艦時開火——側管會打到敵艦
  - **對 Sa-Matra**（劇情 boss）：Pkunk 是最強——高速 + 復活可反覆撞衛星

---

### 3.4 撻伐 · 火炬艦（Thraddash Torch）

**Melee 分數**：10 · **船體**：8/8 · **能量**：24/24 · **回能**：0.142/frame · **迴旋**：0.5 · **推進**：中（28）· **質量**：7

> **定位**：**後噴尾焰艦**——尾焰是遊戲內唯一「跑起來會傷追擊者」的武器。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **前置砲**（Mark VI Blaster）——中距能量彈 · 每彈殺 1 名船員 · **不被 Earthling 點防禦、Umgah 反物質錐、Zoq-Fot-Pik 舌頭攔下**（穿透這些） | 2 | 12 |
| **特殊** | **後燃燒尾焰**（Reeunk Afterburner）——**啟動加速**、**尾焰對後方追擊者造成持續傷害**（每個 fireball 殺 2 船員）· **Torch 自己穿過尾焰不受傷** | 1 | 0（按住連續） |

**戰術**：
- **強項**：尾焰是**唯一背後傷害武器**（除 BUTT）；能量 24 續航好；主武器穿透幾種防禦
- **弱點**：主武器冷卻 12 frame 慢；船體 8 脆
- **小技巧**：
  - **經典打法（AI 剋制）**：**在敵艦飛行路徑上撒尾焰**——AI 常直接撞尾焰
  - **對 Ur-Quan Dreadnought**：加速拖尾焰擦過 Dreadnought
  - **對玩家對手**：**尾焰只對 AI 特別有效** · 玩家會主動閃——尾焰變成「撤退能力」
  - **主砲搭配尾焰**：加速閃避後回身開砲——Mark VI 穿透很多防禦
  - **繞行星 gravity whip**——尾焰配 gravity whip 可打大艦

---

### 3.5 毒賈 · 重擊者（Druuge Mauler）

**Melee 分數**：17 · **船體**：14/14 · **能量**：32/32 · **回能**：**0.02/frame**（**極慢**——約 50 frame/1）· **迴旋**：0.2 · **推進**：慢（20）· **質量**：5

> **定位**：**船員換能量狙擊艦**——單發極強重砲 + **反衝力**推自己 + 燒船員回能。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **重砲**（High-recoil Cannon）——單發 6 傷（**與 Fusion Bolt 同 tier**）· **開火時反衝力極大**——自艦被推得比子彈還快！(可撞行星／可當推進器) · 命中敵艦也**推開敵艦** | 4 | 0（可連射） |
| **特殊** | **爐膛**（Furnace）——**扔一名船員進爐膛換 16 能量**（=船員 -1，能量 +16）· Ultronomicon 說：「乍看無用，實際救急關鍵」 | -1 crew → +16 E | 30 |

**戰術**：
- **強項**：**單發 6 傷是遊戲最強單發**（可秒殺 Shofixti/Skiff/Fury/Stinger）；反衝力**是遊戲內獨特推進**——**Mauler 高速倒退 = 誰都追不上**；能量不夠燒船員繼續打
- **弱點**：**回能極慢**（0.02/f）· 冷靜狀態下無法維持火力；船員只 14，燒完就死；行星是致命敵人（反衝可能撞行星）
- **小技巧**：
  - **經典打法**：**面朝敵艦倒退開火**——反衝把 Mauler 推走、砲打敵艦 = 完美打帶跑
  - **對 Chmmr Avatar**：用反衝閃避 Tractor Beam + 猛轟——Ultronomicon 說「Mauler 是 Avatar 剋星之一」
  - **對 Ur-Quan / Chenjesu / Podship 等大艦**：狙擊每彈都要中——Mauler 沒本錢浪費
  - **警戒行星**：反衝把 Mauler 推向行星時**用反彈躲避**（開火反衝反向也可）

---

### 3.6 梅諾商 · 貿易艦（Melnorme Trader）*[暫譯]*

**Melee 分數**：18 · **船體**：20/20 · **能量**：42/42 · **回能**：0.2/frame · **迴旋**：0.2 · **推進**：快（36）· **質量**：7

> **定位**：**蓄能三段砲艦**——按住主武器蓄能，蓄越久傷越高。
>
> **譯名備註**：目前用「**貿易艦**」（Neutral_Ships.md v0.2 暫定）· 請 Phase 8 確認為「梅諾商貿易艦」或其他

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **三段式高能砲**（Variable Power Blaster）——**按住主武器蓄能**、依蓄能顏色決定傷害：<br>**綠**（1 秒）：2 傷<br>**藍**（2 秒）：4 傷<br>**紫**（3 秒）：8 傷<br>**紅**（4 秒滿蓄）：**16 傷**！ · **紅色滿蓄可撞下敵艦 Fusion Bolt 與其他飛彈**（例外：**擋不下 Kohr-Ah F.R.I.E.D.**） · **紅色彈可當「移動盾」邊持有邊行進** | 5 起跳 | 1 |
| **特殊** | **迷亂光束**（Confusion Ray）——**電磁光束打中敵艦時、敵艦停止使用特殊武器與方向控制**（**但仍能開主武器與推進**）· 一段時間內敵艦旋轉失控 | 20 | 20 |

**戰術**：
- **強項**：**滿蓄紅彈 16 傷 = 遊戲內單發最強** + 可擋敵飛彈；能量 42 大池；迷亂光束讓 AI 廢掉
- **弱點**：**蓄能時無回能**（能量投入包裹）· 蓄到紅色時要留 20 能量給迷亂；轉向慢
- **小技巧**：
  - **經典打法**：**遠距蓄紅** → **飛向敵艦時當盾牌** → 接近時放紅彈
  - **對 AI 特強**：迷亂光束**一開 AI 就白吃**（PVP 對玩家不那麼有效——玩家仍能開主武器）
  - **對 Ur-Quan Dreadnought**：紅彈可**同時擋 Fusion Bolt** + **打 Dreadnought 本體**
  - **對 Kohr-Ah Marauder**：**紅彈擋不下 F.R.I.E.D.**——謹慎接近
  - **無法蓄到紅時**：用綠/藍彈快射也可以，但傷害低
  - **知名艦名**：Melnorme 旗艦「Inevitably Successful in All Circumstances」（於所有情境必勝之艦）

---

### 3.7 歐茲 · 宿敵號（Orz Nemesis）

**Melee 分數**：23 · **船體**：16/16 · **能量**：20/20 · **回能**：0.142/frame · **迴旋**：0.5 · **推進**：快（35）· **質量**：4

> **定位**：**旋轉砲塔 + 登艦作戰艦**——砲塔獨立於船身 + 放\*太空探險隊\*登艦。

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **榴彈砲**（Howitzer）——**旋轉砲塔前射砲** · **每砲殺 3 名敵艦船員**（三倍傷害）· **一次連射 2-3 發**後需等能量 | 6 | 5 |
| **特殊** | **\*太空探險隊\***（\*Space Marines\*）——**按住 Special + 按 Fire = 從艦艇後方發射 Marine**（每次 1 個）· Marines 燒穿敵艦船殼進去殺船員 · 每 0.5 秒骰：50% 殺 1 敵船員 / 43.75% 無事 / 6.25% Marine 死 · 每 Marine 平均能殺 9 名敵船員 · **最多 8 個 Marines 場上** | **0**（不耗能） | 12 |

**特殊按鍵操作**（**關鍵！**）：

| 動作 | 按鍵組合 |
|---|---|
| **旋轉砲塔**（不轉船） | **按住 Special + 方向鍵** ← 這是 Orz 招牌操作！ |
| **發射 Marine** | **按住 Special + 按 Fire** |
| **開砲** | 單按 Fire（面朝砲塔方向）|

**戰術**：
- **強項**：**砲塔獨立轉向**——不用轉船就能全方位打；**Marines 是無視護盾的殺手**（Yehat/Utwig 護盾**擋 Marines 但不會殺 Marines**、只反彈）；每砲殺 3 船員暴傷
- **弱點**：**Blazer wedging 剋 Orz**——Guardian Blazer 可卡進 Orz 後鰭裂縫秒殺；船體 16 中等
- **小技巧**：
  - **經典打法**：**保持中距離** → **側面對敵艦**（Orz 側向逃） → **轉砲塔連轟**（不用轉船） → **同時派 Marines 登艦**
  - **對 Ur-Quan Dreadnought**（船員 42）：Marines 特別有效——每 Marine 平均殺 9，兩個就能滅掉 Dreadnought
  - **對 Chmmr Avatar**：**Zap 衛星會攔 Marines**——先打光 Zap 再放
  - **對 Ur-Quan Fighter**：Fighter 會攔 Marines · 榴彈可掃 Fighter
  - **警戒 Androsynth Blazer**——Ultronomicon 說：「Nemesis is ironically especially vulnerable to the Guardian」

---

### 3.8 佐-佛-皮 · 刺激者號（Zoq-Fot-Pik Stinger）

**Melee 分數**：6（極便宜）· **船體**：10/10 · **能量**：10/10 · **回能**：0.2/frame · **迴旋**：0.5 · **推進**：快（40）· **質量**：5

> **定位**：**便宜舌頭刺擊艦**——反物質吐射連射 + **舌頭刺擊貼身武器**（**不是純語音**！）

| 動作 | 效果 | 能量 | 冷卻 |
|---|---|---|---|
| **主武器** | **反物質吐射**（Antimatter Spray Gun）——連續短距吐射 · **不準但可攔截敵飛彈** · 原始碼稱為 "spit" | 1 | 1 |
| **特殊** | **舌頭刺擊**（Tongue Attack）*[暫譯]*——**貼身時從艦艏伸出金屬管刺入敵艦、注入高壓熱電漿造成大量傷害**（**不是純語音！**） · 極短距離、瞬發 · **舌頭可攔截敵艦重砲**（可擋 Mycon Plasmoid / Kohr-Ah Blade / Ur-Quan Fusion Bolt · **擋不下** Melnorme 紅蓄彈與 Kohr-Ah F.R.I.E.D.） | 7 | 6 |

**戰術**：
- **強項**：**分數 6 極便宜**——組隊填空位；**舌頭是遊戲內獨特貼身武器 + 可擋大砲**；速度 40 + 靈活
- **弱點**：船體 10 脆；反物質吐射不準；能量僅 10
- **小技巧**：
  - **對 Mycon Podship**：Ultronomicon 說「Podship 是 ZFP 送分怪」——Podship 慢又轉不好，Stinger 貼身用舌頭秒殺
  - **對 Ilwrath Avenger**：Ilwrath 慢，Stinger 可**打帶跑 + 舌頭 KO**
  - **對 Yehat Terminator**（AI）：吐射射程略長於 Terminator 砲——引誘 Terminator 追、匆匆迴射
  - **對 Chmmr Avatar**：**舌頭是 ZFP 唯一能傷 Chmmr 的方式**——衝進去舔一口就跑
  - **經典戰術（Ultronomicon）**：「showering with pellets is more potent but on occasion it's fun to charge in and lick 'em good」
  - **拿舌頭擋子彈**：面朝敵艦飛彈時舌頭伸出可**擋下 Plasmoid、Kohr-Ah blade、Fusion Bolt**！

---

## 附錄一：Super Melee 剋星速查表

**A 剋 B** = A 對戰 B 有明顯優勢（並非絕對，會依駕駛技術差異）· 資料源自 Ultronomicon 各族 Tactical Overview

| A 艦 | B 艦（被剋） | 為什麼 |
|---|---|---|
| **Shofixti 偵察艦** | Chmmr / Ur-Quan / Kohr-Ah / Yehat / Utwig | **榮耀彈秒殺任何大艦**（護盾擋不住）|
| **Chmmr 復仇號** | 大部分艦 | Zap + 雷射 + 高船體 · 弱點**只有** 自爆與貼身 Blade |
| **Kohr-Ah 掠奪者** | Chmmr / 大部分中艦 | 刀刃陣型 + F.R.I.E.D. 全周 · 貼身無敵 |
| **Spathi 迴避者** | Chenjesu / Ur-Quan / Kohr-Ah | 高速逃 + BUTT 後射 · 大艦追不上 |
| **Chenjesu 母巢艦** | Yehat / Utwig / Ur-Quan | DOGI 吸能讓護盾與武器失效 |
| **Yehat 終結者** | Ur-Quan / Earthling / Podship | 護盾擋飛彈與能量彈；Twin Ion 連射秒 Androsynth |
| **VUX 入侵者** | Spathi / Pkunk / Mmrnmhrm | Limpet 減速 · **穿護盾** · 分別作用兩形態 |
| **Slylandro Probe** | Ur-Quan / Chenjesu / Earthling | 電擊吸能 + 高速非慣性 · 慢艦絕望 |
| **Syreen 穿透艦** | Ur-Quan / Chenjesu（船員多）· Yehat / VUX（歌穿護盾）| 塞蓮之歌吸滿血 |
| **Utwig 重砲艦** | Ur-Quan / Chmmr / Kohr-Ah / Melnorme | 護盾吸大砲能量 · 越打越強 |
| **Ilwrath 復仇者** | Arilou / Chenjesu / Earthling · 弱者 | Cloak 讓自動追蹤武器失效 |
| **Pkunk 烈憤艦** | Sa-Matra、多數敵艦（若運氣好）| 復活 + 全遊戲最快 + 三管齊射 |
| **Ur-Quan 無畏艦** | Shofixti / ZFP / Slylandro | 融合彈追蹤秒殺脆艦 · Fighter 群戰 |
| **Kohr-Ah 掠奪者** | 大多數艦 | Blade + F.R.I.E.D. 全面攻擊 |
| **Melnorme 貿易艦** | AI 對手（迷亂）· Ur-Quan（可擋 Fusion） | 迷亂光束對 AI 極致 |
| **Umgah 蜂機艦** | Kohr-Ah / Chenjesu / Ur-Quan | 反物質錐貼臉 + 後退推進逃 |
| **Androsynth 守衛艦** | Orz / Chmmr / Podship（wedging） | Blazer 卡進裂縫秒殺 |
| **Druuge 重擊者** | Chmmr / Ur-Quan / 大艦 | 反衝倒退狙擊 · 單發最強 |
| **Zoq-Fot-Pik 刺激者號** | Mycon / Ilwrath | 靈活貼身舌頭 + 攔敵彈 |
| **Mmrnmhrm 變形艦** | Utwig（低傷彈剋護盾）| Y-Wing 飛彈耗光 Utwig 護盾能量 |

**特別剋制關係（不對稱）**：

- **Utwig Jugger vs Ur-Quan Dreadnought**：Utwig 完克（Fusion 打護盾補給 Utwig）
- **Chenjesu DOGI vs Yehat/Utwig**：DOGI 讓護盾癱瘓
- **Guardian Blazer vs Orz**：wedging 秒殺 Orz 後鰭
- **VUX Limpet vs Yehat/Utwig**：穿護盾直接減速
- **Syreen Song vs Yehat/VUX**：歌穿護盾直接吸船員
- **Shofixti Glory vs Yehat/Utwig**：Glory 穿護盾直接爆炸

---

## 附錄二：100 點組隊建議（新手向）

**100 點基本 fleet 範例**（Melee 起始預算）：

| 組合名 | 艦隊 | 總分 | 適用 |
|---|---|---|---|
| **平衡入門** | 1 Chmmr (30) + 2 Yehat (46) + 1 Spathi (18) + 1 Shofixti (5) | **99** | 新手，穩定 |
| **高速游擊** | 2 Pkunk (40) + 2 Arilou (32) + 1 Slylandro Probe (17) + 1 Shofixti (5) | **94** | 靈活派 |
| **大艦重砲** | 1 Kohr-Ah (30) + 1 Chmmr (30) + 1 Utwig (22) + 3 Shofixti (15) | **97** | 硬碰硬 |
| **自爆流** | 6 Shofixti (30) + 1 Chmmr (30) + 1 Yehat (23) + 1 Umgah (7) | **90** | 神風流 |
| **反飛彈牆** | 1 Chenjesu (28) + 1 Yehat (23) + 1 Earthling (11) + 1 Chmmr (30) + 1 Shofixti (5) | **97** | 對抗飛彈型敵艦 |
| **舌頭 + 神風** | 5 ZFP (30) + 1 Chmmr (30) + 1 Utwig (22) + 3 Shofixti (15) | **97** | 便宜暴力 |
| **雙形態陷阱** | 1 Melnorme (18) + 2 Mmrnmhrm (38) + 1 VUX (12) + 1 Yehat (23) + 1 Shofixti (5) | **96** | 誘敵 |
| **屁彈風暴** | 3 Spathi (54) + 1 Yehat (23) + 1 Utwig (22) | **99** | 遠距射手 |
| **旋轉屠殺** | 1 Kohr-Ah (30) + 2 Orz (46) + 1 Yehat (23) | **99** | 帶著 Marines 攻堅 |

**組隊原則**：
1. **買 1 艘 30 分主力**（Chmmr / Ur-Quan / Kohr-Ah）當旗艦
2. **買 2-3 艘 15-25 分中主力**補洞（Yehat / Utwig / Orz / Spathi）
3. **買 1-2 艘 5-10 分便宜艦**當「秒殺筒 / 填空位」（Shofixti / ZFP / Thraddash / Ilwrath / Umgah）
4. **避免**：全部低分艦（脆） · 全部高分艦（不夠靈活）

---

## 附錄三：資料來源與譯名對照

**權威資料**（雙重驗證）：

1. **UQM MegaMod 原始碼**：`src/uqm/ships/<race>/<race>.c` 內：
   - `RACE_DESC` 結構的 Super Melee cost、MAX_CREW、MAX_ENERGY、WEAPON_ENERGY_COST、SPECIAL_ENERGY_COST、WEAPON_WAIT、SPECIAL_WAIT、ENERGY_REGENERATION、ENERGY_WAIT、MAX_THRUST、TURN_WAIT、SHIP_MASS 等 macros
   - `SHIP_INFO` 的 `SHIP_TYPE_FLAG` bits：`FIRES_FORE` / `FIRES_AFT` / `FIRES_LEFT` / `FIRES_RIGHT` / `SEEKING_WEAPON` / `SEEKING_SPECIAL` / `POINT_DEFENSE` / `SHIELD_DEFENSE` / `DONT_CHASE`
   - Preprocess handler：`weapon_preprocess`、`special_preprocess`、`postprocess_func`

2. **Ultronomicon Wiki**（<https://wiki.uqm.stack.nl/>）：
   - 每族詳細頁：<https://wiki.uqm.stack.nl/List_of_ships>
   - Super Melee cost 官方表：<https://wiki.uqm.stack.nl/Table_of_ship_values>

**譯名對照**：

| 分類 | 來源檔案 |
|---|---|
| 艦艇級名 | [Ship_Names.md](../07_Glossary/Ship_Names.md) v0.5.2 canonical |
| 武器名 | [Weapon_Systems.md](../05_Technology/Weapon_Systems.md) |
| 種族名 | [Master_Glossary.md](../07_Glossary/Master_Glossary.md) §四 |

**暫定譯名**（待 Phase 8 定稿，本檔以 *[暫譯]* 標記）：

| 英文 | 暫譯 | 說明 |
|---|---|---|
| Earthling Cruiser | 巡邏艦 | 沿用 Cruiser 譯法（Tobermoon 也用此譯） |
| Nuclear Missile | 核彈飛彈 | 直譯 |
| Point-Defense Laser | 點防禦雷射 | 直譯 |
| Melnorme Trader | 貿易艦 | 可能升級為「梅諾商貿易艦」 |
| Absorption Shield (Utwig) | 憂特防護罩 | 與 Yehat Shield 區分 |
| Heavy X-ray Laser (Chmmr) | 重型 X 光雷射 | Ultronomicon 用此名 |
| Mendōkusai Energy Dart (Shofixti) | 麻煩鏢 | 「メンドクサイ」= 麻煩 · 保留哏 |
| Forward Mounted Gun (Spathi) | 前置機槍 | Ultronomicon 描述性名稱 |
| Energy Spears (Utwig) | 能量矛 | Ultronomicon 描述性名稱 |
| Tongue Attack (ZFP) | 舌頭刺擊 | Ultronomicon 稱 "tongue" |
| Energize (Slylandro Probe) | 能量化 / 吸收隕石 | 描述性 |
| Advanced Maneuvering (Supox) | 四向機動 | 描述性 |
| Reeunk Afterburner (Thraddash) | 後燃燒尾焰 | 沿用 Weapon_Systems |
| High-recoil Cannon (Druuge) | 重砲（Druuge） | 與 Utwig 能量矛區分 |

**跟舊版差異**：

- Spathi 迴避者：**主/特殊已修正**（前置機槍 vs BUTT 後射）
- Kohr-Ah 掠奪者：**主/特殊已修正**（刀刃 disc vs F.R.I.E.D. 環繞）
- Pkunk 烈憤艦：**Insult 罵髒話補能量**（非嘲諷）· **復活是被動能力**分開列
- Slylandro Probe：**Energize 吸 asteroid 補能量**（**非自我複製** · 那是星圖版機制）· 反向推進機制
- Orz 宿敵號：**加入 Special + 方向鍵 = 轉砲塔** · **Special + Fire = 放 Marines**
- ZFP 刺激者號：**特殊是舌頭刺擊**（**非純語音無效果**）· 可攔敵艦重砲
- Ilwrath 復仇者：**cloak 與 flame 不能同時**（開火自動關 cloak）
- Chenjesu Broodhome：**主武器蓄能 + 再按爆散** · DOGI **吸能不傷害**
- Umgah Drone：**主武器不耗能但開時停止回能** · **chunk regen**（非持續 regen）
- Utwig Jugger：**主武器 = 能量矛（6 管齊射不耗能）** · 護盾**擋不了 Confusion Ray / Limpet / Glory**
- Mmrnmhrm：**X-Wing = 戰機**、**Y-Wing = 飛彈**（角色已改正）
- Guardian Blazer：**wedging 卡進裂縫可秒殺**
- Melnorme Trader：**蓄能四色**（綠藍紫紅）· 傷害 2/4/8/16
- 所有 Melee 分數皆對照 Ultronomicon [Table of ship values](https://wiki.uqm.stack.nl/Table_of_ship_values) 驗證

---

**譯者備註**：本檔為 SC2 UQM MegaMod 繁體中文化計畫的一部分。若你對戰術描述有異議、發現數據落差、或想補充某族的進階技巧，歡迎在 [GitHub Issues](https://github.com/HaCoMaTaTa/sc2-uqm-zhtw/issues) 提出。
