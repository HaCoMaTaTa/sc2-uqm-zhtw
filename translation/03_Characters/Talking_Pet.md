# 會話寵 · 蟾亞 Talking Pet (device) / neo-Dnyarri

> **本檔為 SC2 comm 特定發言角色 dossier**。指的是玩家在陰嘎（Umgah）星系救出、後來加入 Vindicator 貨艙的**唯一清醒 Dnyarri 個體**（Ultronomicon 學術稱之 **neo-Dnyarri**）；他在 `comm/talkingpet/talkingpet.txt` 中發言。

## 一、基本資料

| 項目 | 內容 |
|---|---|
| 中文名（鎖定） | **會話寵**（表面身分，v0.4 canonical）／**蟾亞**（真身，古代身分）|
| 英文名 | Talking Pet (device) ／ neo-Dnyarri（Ultronomicon 學術詞，遊戲內不出現）|
| 種族 | [蟾亞族 Dnyarri](../02_Races/Dnyarri.md) |
| 陣營 | 名義：烏寬翻譯工具（vestigial）／實際：玩家的合作勒索者（意外覺醒）|
| 身分／職位 | **銀河唯一清醒的 Dnyarri**（他自稱「I am the only intelligent Dnyarri left」）|
| 玩家關係 | **主線關鍵夥伴**：Vindicator 貨艙住客→ Sa-Matra 決戰時心靈干擾烏寬  |
| 首次登場 | 玩家探索 Beta Orionis I（陰嘎母星），發現整個陰嘎族被他心靈控制 |
| 主要出場檔案 | `../uqm-work/extracted/base/base/comm/talkingpet/talkingpet.txt`（112 tokens）|

## 二、背景故事（**蟾亞族三形態時間軸**）

```
時間軸    形態                智能         心靈控制    數量
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
20,000 年前  ① 原始蟾亞 Dnyarri    極高（暴君）   全開       已滅絕（僅存 Glilandy）
現代         ② 會話寵 Talking Pet  零（被閹割）   無         每艘無畏艦/掠奪者各 1 隻
SC2 中期     ③ 本個體 neo-Dnyarri  完整（回復）  弱化可用   唯一
```

### 這個個體的復甦過程

1. 曾是普通「會話寵」，服役於某艘烏寬無畏艦
2. 該艦被柯亞黑戰船擊落，墜毀於 **Alpha Pavonis 系**
3. **阿麗露**發現他快死了，帶回準空間家園治療；治療失敗
4. 阿麗露轉託**陰嘎族**（生物工程專家）修復
5. 陰嘎族在**改造他腦部**過程中，**意外恢復其祖先基因記憶**——完整的 Dnyarri 智能與古代記憶湧回
6. 他隨即**心靈控制整個陰嘎族**，成為星域幕後主宰
7. 計畫用**假造烏寬指令**騙史怕族攻擊 VUX 引發連鎖戰爭復仇烏寬
8. 玩家介入（Taalo shield 保護免疫）→ 心靈控制失效 → 他被迫改為**勒索合作**

### 官方 wiki 對應 canonical

- **Homeworld（Ultronomicon）**：Glilandy（**格利蘭第**）— 烏寬圍城滅絕蟾亞族的最後據點
- **他自稱的母星**：**Benteflork（本鐵佛克）**— **可能是謊言或個人出身地**，dossier 註記待確認
- **他的分類名**：Ultronomicon `Talking Pet (device)` 對應 wiki 的**neo-Dnyarri**學術詞

## 三、性格分析（**單一但多面向個體**）

**核心人格**：**清醒的古代暴君 + 現代諷刺口氣 + 諂媚勒索大師 + 傷痛民族主義者**——被 Taalo shield 壓制心靈控制後，切換為**用嘴皮子生存的機會主義者**。

**深層心理**：他**真心相信自己種族被 Ur-Quan 虐待**（POOR_DNYARRI 的悲情有據，撇除他祖先當年虐待其他種族的事實）；他**真心想復仇**；但也**真心自私**——只要能達成復仇，什麼都可以妥協。**他知道自己是騙子**，但他認為**騙子有時候也講對的話**。

**價值觀**：
- 最重視：**對烏寬的復仇**（兩萬年的祖傳仇恨）
- 最忌諱：**Taalo shield**（心靈控制被壓制的無力感）
- 最擅長：**諷刺挖苦**、**諂媚談判**、**在承認撒謊時反而顯得可信**

## 四、語言風格（**八種切換模式**，實測 EN talkingpet.txt 分類）

| Mode | 場景 | Voice 特徵 | 代表 tokens |
|---|---|---|---|
| **① 假身分** | 首次接觸假裝無害 | 「和平生物、友善外星生命」 | JUST_TALKING_PET / DID_NOTHING / GOOD_FOR_YOU |
| **② 心靈控制指令** | 覺醒時發布催眠命令 | 古老命令式 `-<COMMAND>-` | OH_NO_YOU_DONT / EXPLAIN_NOTHING / HYPNOTIZE_AGAIN_1-4 |
| **③ 求饒賣萌** | 玩家亮劍 | 「不要！我是最後一個！」+ 「Ouchy-oochy」 | PLEASE_DONT / LETS_MAKE_A_DEAL |
| **④ 諂媚合作** | 加入貨艙後 | 「我是**你的**騙子」自貶反諂媚 | TRUST / YOUR_BONELESS_DWEEB / COMING_ABOARD |
| **⑤ 貨艙抱怨** | 貨艙裡無聊 | 現代口語 + 荒謬吐槽（Mozart / Iggy Pop）| GENERAL_INFO_ONBOARD_1-8 |
| **⑥ 悲情敘事** | 揭示 Dnyarri 身世 | 古代自稱「吾等」+ 民族傷痛 | POOR_DNYARRI / ITS_TRUE / ABOUT_HISTORY / ABOUT_WAR |
| **⑦ 諷刺辱罵** | 玩家問蠢問題 | 「猿猴子」/「哭啥」/「無語」 | DO_THIS / STUPID_FOP / NOT_POWERS_BUT_FLOWERS |
| **⑧ 破第四道牆** | 結尾/彩蛋 | 「我被鎖在裡面！」+「續集預告」| CYBORG_PEP_TALK / HUMAN_PEP_TALK / OUT_TAKES |

### 自稱池（Q6 canonical）

| 情境 | 自稱 |
|---|---|
| **常態 default**（Mode 4/5/7/8）| **我** |
| **自傲時**（覺醒感）| **本座** |
| **假身分**（Mode 1）| **小的** / **無害的譯者** |
| **心靈控制指令**（Mode 2, `-<COMMAND>-`）| （命令句無自稱，用「爾等」對玩家）|
| **悲情敘事古代自稱**（Mode 6）| **吾等蟾亞族** / **我族** / **吾族** |
| **求饒賣萌**（Mode 3）| **我** / **本座**（「本座是最後一個」）|

### 對玩家的稱呼

| 情境 | 稱呼 |
|---|---|
| **假身分/合作**（Mode 1/4）| **艦長** / **偉大的艦長** |
| **心靈控制指令**（Mode 2）| **爾等** / **無知蟲豸** / **猿猴子（monkey-boy）** |
| **諷刺**（Mode 7）| **人類** / **蠢蛋** / **哭夭鬼（blubbering fop）** |
| **貨艙抱怨**（Mode 5）| **艦長**（帶不耐煩）|
| **悲情/敘事**（Mode 6）| **艦長**（真誠）|

### 核心詞彙／口頭禪 canonical

| 原文 | 中譯 | canonical 來源 | 使用時機 |
|---|---|---|---|
| Talking Pet | **會話寵** | Master_Glossary v0.4 | 表面身分 |
| Dnyarri | **蟾亞（族）** | Master_Glossary v0.4 | 真身/種族 |
| neo-Dnyarri | *（不直譯，通篇用「會話寵」/「蟾亞」交替）* | Q2 決策 | Ultronomicon 學術用 |
| Sentient Milieu | **感知聯盟** | Master_Glossary v0.3 | 古代跨族政體 |
| Taalo | **塔洛族** | Master_Glossary v0.4 | 唯一免疫心靈控制族 |
| Taalo shield | **塔洛盾** | **v0.5 canonical**（本次確認） | 玩家防禦心靈控制 |
| Taalo device | **塔洛裝置** | **v0.5 canonical**（本次確認） | 貨艙裡的裝置實體 |
| Benteflork | **本鐵佛克（Benteflork）** | **v0.5 canonical**（本次確認） | 他自稱的母星，可能撒謊 |
| Glilandy | **格利蘭第（Glilandy）** | **v0.5 canonical**（本次確認） | Ultronomicon 官方 Dnyarri 母星（本 SC2 dialog 未出現，dossier ref only）|
| Sa-Matra | **薩瑪特拉** | 通用 canonical | Precursor 戰鬥平台 |
| HyperWave 'Caster | **超波廣播器** | spathi/umgah canonical | 陰嘎族的通訊器 |
| Ur-Quan slave raider | **烏寬奴役襲擊艦** | **v0.5 canonical**（本次確認） | 兩萬年前劫掠蟾亞母星 |
| Excruciator | **極痛裝置** | 通用 canonical | Ur-Quan 反抗心靈控制的工具 |
| psychic compulsion | **心靈操控** / **心靈控制** | 通用 | Dnyarri 招牌能力 |
| mental compulsion | **心靈操控** | 通用 | 同上 |
| lobotomize / castrate（mind）| **智能閹割** | v0.5 casual coinage | Ur-Quan 對 Dnyarri 的懲罰 |
| genetic memory | **基因記憶** | 通用 | 他覺醒後恢復的記憶 |
| Ha-ha-ha! | **哈哈哈！** | 保留擬聲 | 招牌笑聲 |
| *sigh* | **（嘆氣）** | 通用擬態 | Mode 3/4 崩潰前 |
| _Gasp_ | **（喘氣）** | dossier §四 | Mode 1 假身分擬態 |
| Aieee! | **啊咦！** 保留原文 | dossier §5.1 canonical | 極度驚訝 |
| Woof woof! | **汪汪！** | 通用擬聲 | Mode 3/4 賣萌反諷 |
| Ouchy-oochy | **哎唷呢喃** | v0.5 casual coinage | 撒嬌痛痛 |
| boneless dweeb | **軟骨呆瓜** | v0.5 canonical | 玩家對他的辱罵 |
| monkey-boy | **猿猴子** | v0.5 canonical | 他辱罵玩家（保留 monkey / boy 意象）|
| blubbering fop | **哭夭鬼** | v0.5 casual coinage | 他譏諷玩家 |
| Big deal! | **大不了** / **有啥了不起** | v0.5 現代口語 | 招牌不屑 |
| bummer | **靠**（強度看情境）| v0.5 現代口語 | Mode 5/6 抱怨 |
| Dang! | **啐！** / **靠！** | v0.5 現代口語 | 挫敗感嘆 |
| Yeah, that's the ticket! | **對嘛，就是這樣！** | v0.5 現代口語 | Mode 8 破第四道牆 |
| Frankly | **老實說** | 現代口語 | Mode 5/6 |
| Ha! | **哈！** 保留 | 通用 | 短笑 |
| Feh! | **啐！** | 通用 | 貶抑感嘆 |

### 特殊格式：心靈控制指令 `-<COMMAND>-`

**格式**：EN 用 `-<ALL CAPS COMMAND!>-` 標記催眠指令（強制被催眠者行動）。

**Q4=A canonical**：保留 `-<...>-` bracket + 內容中譯（保留急迫命令感）

**範例**：
- `-<SEEK DEATH AT THE HANDS OF YOUR ENEMY!>-` → `-<去尋死於敵人之手！>-`
- `-<GET LOST IN A BAD NEIGHBORHOOD!>-` → `-<迷失於險惡之地！>-`
- `-<GO GET YOURSELF KILLED!>-` → `-<讓自己去送死！>-`
- `-<NOW GO AWAY AND PICK A FIGHT!>-` → `-<即刻離去挑起爭端！>-`
- `-<FIND SOMEONE WHO WILL KILL YOU!>-` → `-<尋一人願殺爾者！>-`
- `-<LEAVE ME ALONE!>-` → `-<離本座遠去！>-`
- `-<DIDN'T YOU MEAN TO ASK ABOUT FLOWERS?>-` → `-<爾意欲詢問花朵之事？>-`

### 情緒觸發雷區

- 玩家沒有 Taalo shield → **立刻催眠殺意**（EXPLAIN_NOTHING）
- 玩家有 Taalo shield → **假裝改邪歸正 → 承認撒謊 → 諂媚合作**（LETS_MAKE_A_DEAL）
- 玩家問「Talking Pets 不是無腦嗎？」→ **殺意瞬間爆發**（OH_NO_YOU_DONT）
- 玩家提到 Taalo → **痛苦回憶祖先羞辱**（ABOUT_WAR「For fun, they would roll over our children!」）
- 貨艙抱怨無人回應 → **越來越荒謬的抱怨**（GENERAL_INFO_ONBOARD_5「MOZART & IGGY POP 400 遍」）
- Sa-Matra 決戰 → **突然變膽小**（DO_THIS「AND IGNORE THOSE THOUSANDS OF DREADNOUGHTS!」）

## 五、中文化翻譯規則

**翻譯時應做**：
- **依 Mode 切換 voice**——同一 token 內若有情緒切換要明顯（如 LETS_MAKE_A_DEAL 一段長 rant 中間切換 3-4 次）
- **心靈控制指令 `-<...>-` bracket 保留**，內容用**古老命令式**中文（爾等 / 尋一人 / 即刻）
- **貨艙抱怨允許現代口語**（Big deal / bummer / Ouchy-oochy）
- **悲情敘事用古代自稱**（吾等蟾亞族 / 我族）
- **假身分保留幼童化痕跡**（「小的」/「無害的譯者」）
- **諷刺挖苦用「猿猴子」/「哭夭鬼」/「軟骨呆瓜」等 canonical 侮辱詞**
- **破第四道牆彩蛋**（CYBORG_PEP_TALK「我被鎖在裡面」/ OUT_TAKES 續集預告）**盡量保留 gag 精神**
- **`I am **YOUR** boneless dweeb!`** 的**強調對比**用粗體：「本座是**你的**軟骨呆瓜」

**翻譯時應避免**：
- ❌ 一味用「爾等蟾亞」（只有心靈控制場合用；日常應該用「我」）
- ❌ 一味用「（喘氣）（發抖）」（幼童化只有假身分場合）
- ❌ 現代網路哏（「84」「魔怔」「破防」等）── v0.5 canonical 允許中量現代口語但**避免當代網路用語**
- ❌ 把「Ha-ha-ha!」翻成「呵呵」（要保留「哈哈哈！」的諷刺感）
- ❌ 讓他顯得單純可憐（他是**騙子**+**倖存者**，不是萌角色）
- ❌ 把 `-<COMMAND>-` 拆成一般句子（那是**特殊格式**必留 bracket）

**推薦語氣詞彙庫**：
本座、我、小的、爾等、吾等蟾亞族、猿猴子、無知蟲豸、軟骨呆瓜、哭夭鬼、哈哈哈、啊咦、啐、靠、大不了、有啥了不起、老實說、汪汪、哎唷呢喃、拜託、心靈控制、心靈操控、感知聯盟、塔洛盾、極痛裝置、基因記憶、智能閹割、（喘氣）、（嘆氣）

## 六、對話範例（依 EN talkingpet.txt 實際內容）

### 範例 1：Mode ② 心靈控制指令（覺醒揭曉）
- **原文**（`OH_NO_YOU_DONT`）：
  ```
  Oh... you know about that, do you?
  Oh well, I guess that means I will have to kill you now.
  I can't permit you to reveal my transformation
  the Ur-Quan might find out, and then my plans for revenge will be ruined.
  Well, I tried to spare your life, Captain, but you were just too curious
  so now:
  -<SEEK DEATH AT THE HANDS OF YOUR ENEMY!>-
  ```
- **建議譯文**：
  ```
  喔…… 爾知道啦？
  唉，那本座只好殺爾了。
  本座不容爾洩漏本座之覺醒
  烏寬若得知，本座的復仇大計便毀了。
  唉，本座已試著饒爾一命，艦長，可爾實在太好奇
  那如今：
  -<去尋死於敵人之手！>-
  ```
- **翻譯理由**：Mode ② 覺醒古老口氣，用「本座」自稱、「爾」稱玩家；`-<COMMAND>-` 保留 bracket 中譯

### 範例 2：Mode ④ 諂媚合作（自貶反諂）
- **原文**（`YOUR_BONELESS_DWEEB`）：
  ```
  Yes, Captain. I am a lying, boneless, toady dweeb
  but I am YOUR lying, boneless, toady dweeb!
  ```
- **建議譯文**：
  ```
  沒錯，艦長。 我是個撒謊的、軟骨的、諂媚的呆瓜
  可我是**你的**撒謊軟骨諂媚呆瓜！
  ```
- **翻譯理由**：Mode ④ 諂媚，用「我」自稱；「boneless dweeb」→「軟骨呆瓜」canonical；「**YOUR**」→ 粗體「**你的**」保留 EN 反諂媚強調

### 範例 3：Mode ⑤ 貨艙抱怨（現代口語）
- **原文**（`GENERAL_INFO_ONBOARD_5`）：
  ```
  I am slowly going insane, Captain!
  I don't know if you are aware of this
  but there are music loops which play down here, CEASELESSLY!
  ...
  I mean, Mozart and Iggy Pop are fine, for alien noise-makers
  but PLEASE!... CHANGE THE MUSIC BEFORE I GO MAD!
  ```
- **建議譯文**：
  ```
  我快瘋了，艦長！
  不知道你發現了沒
  這下面有音樂循環播放，**無止盡地**！
  ...
  我是說，莫札特和伊基·帕普（Iggy Pop）作為外星人的噪音製造者算不錯
  可**拜託**！…… 在我發瘋之前**換首歌吧**！
  ```
- **翻譯理由**：Mode ⑤ 現代口語（「快瘋了」/「拜託」/「換首歌吧」）；Mozart 譯「莫札特」，Iggy Pop 音譯保留原名（rock 樂手，玩家可能認識）

### 範例 4：Mode ⑥ 悲情敘事（古代自稱）
- **原文**（`POOR_DNYARRI` 節錄）：
  ```
  I was a Dnyarri -- a member of a peaceful alien race, whose intelligence the Ur-Quan had long ago `shut off'
  via cruel biogenetic manipulation.
  I am the only intelligent Dnyarri left in this galaxy, Captain.
  Now do you understand my lust for vengeance?
  ```
- **建議譯文**：
  ```
  我是蟾亞族一員 —— 一個和平的外星種族，吾等之智能被烏寬於久遠之前『關閉』
  藉由殘忍的生物基因操縱。
  我是這銀河中僅存的清醒蟾亞，艦長。
  如今爾可明白本座復仇之慾？
  ```
- **翻譯理由**：Mode ⑥ 悲情敘事切換自稱：「我」（現代敘事）+ 「吾等」（古代族群）+ 「本座」（覺醒古人）；「long ago `shut off'」→ 「久遠之前『關閉』」保留單引號的 sinister quotation

### 範例 5：Mode ① 假身分（幼童化）
- **原文**（`JUST_TALKING_PET` 節錄）：
  ```
  I am, uh, a peaceful creature, a friendly alien life form. The Ur-Quan call us `talking pets'.
  Until recently, I was employed on a Dreadnought starship as a translator.
  ```
- **建議譯文**：
  ```
  小的呀，呃，是個和平的生物，友善的外星生命體。 烏寬稱吾輩為『會話寵』。
  不久前，小的還在一艘無畏艦星艦上擔任譯者。
  ```
- **翻譯理由**：Mode ① 假身分用「小的」自稱、「吾輩」集體卑稱；「Ur-Quan call us」→ 「烏寬稱吾輩為」保留他撇清自己與烏寬的距離感

### 範例 6：Mode ⑧ 破第四道牆（gag 精神）
- **原文**（`OUT_TAKES`）：
  ```
  So! You probably thought I was dead... DIDN'T YOU!?
  Well I'm not! I got away from the ship at the last second
  and now I'm REALLY going to cause some trouble!
  In fact, that's what the sequel is going to be about!
  ...
  It will have gratuitous alien sex scenes!
  It's gonna be great!
  ```
- **建議譯文**：
  ```
  嘿！ 爾大概以為本座死了…… **對不對**！？
  哈，可惜沒有！ 本座在最後一秒鐘逃離了艦艇
  現在本座**真的**要搞出點麻煩！
  事實上，續集就是要講這個！
  ...
  會有多餘的外星性愛場面！
  一定很棒！
  ```
- **翻譯理由**：Mode ⑧ 混合「本座」（自傲）+ 「爾」（觀眾角度，破牆感）；`gratuitous alien sex scenes` 直譯保留 gag；「gonna」→「要」保留口語感

## 七、相關人物 / 種族

- **[蟾亞族 Dnyarri](../02_Races/Dnyarri.md)**：他的祖先種族（他是唯一清醒者）
- **[會話寵（generic Talking Pet）](../02_Races/Dnyarri.md#會話寵形態)**：他的原本身分（在無畏艦當譯者）
- **[烏寬克澤札 Ur-Quan Kzer-Za](../02_Races/Ur_Quan_Kzer_Za.md)**：他祖先的暴虐奴役者、他復仇的目標
- **[烏寬柯亞 Ur-Quan Kohr-Ah](../02_Races/Ur_Quan_Kohr_Ah.md)**：擊落他的無畏艦、後來屠殺陰嘎族毀他計畫
- **[陰嘎族 Umgah](../02_Races/Umgah.md)**：意外修復他智能的族群；被他心靈控制當復仇工具；後被 Kohr-Ah 屠殺
- **[阿麗露 Arilou](../02_Races/Arilou.md)**：從無畏艦廢墟救出他、送交陰嘎修復
- **[塔洛族 Taalo](../02_Races/Others/Taalo.md)**：唯一免疫心靈控制族；他祖先被「roll over children」的仇恨對象
- **[史怕族 Spathi](../02_Races/Spathi.md)**：他計畫用假造烏寬指令騙其攻擊 VUX 引發戰爭
- **[VUX](../02_Races/VUX.md)**：他計畫報復的第一波對象

## 八、canonical 決策記錄（v0.5, 2026-08-10）

| 項目 | v0.5 canonical | 決策來源 |
|---|---|---|
| Talking Pet (device) | **會話寵 / 蟾亞 dual-identity** | Q2 使用者確認 dual-identity |
| Dnyarri (species) | **蟾亞族** | Master_Glossary v0.4 已鎖 |
| neo-Dnyarri | **不直譯，通篇用「會話寵」/「蟾亞」交替** | Q2 dossier 內部備註 |
| Benteflork | **本鐵佛克（Benteflork）** + 註「可能撒謊」| Q3 使用者決定 |
| Glilandy | **格利蘭第（Glilandy）** | v0.5 canonical，Ultronomicon 官方 homeworld |
| Sentient Milieu | **感知聯盟** | Master_Glossary v0.3 已鎖 |
| Taalo shield | **塔洛盾** | v0.5 canonical |
| Taalo device | **塔洛裝置** | v0.5 canonical |
| Ur-Quan slave raider | **烏寬奴役襲擊艦** | v0.5 canonical |
| Excruciator | **極痛裝置** | 通用 canonical |
| psychic compulsion | **心靈操控** | 通用 |
| lobotomize | **智能閹割** | v0.5 canonical |
| `-<COMMAND>-` 心靈控制指令格式 | **保留 `-<...>-` bracket + 中譯古命令式** | Q4=A 使用者決定 |
| Voice pool: 常態 | **我 / 本座** | Q6 使用者確認 |
| Voice pool: 假身分 | **小的 / 無害的譯者 / 吾輩** | Q6 使用者確認 |
| Voice pool: 心靈控制 | **爾等 / 無知蟲豸 / 猿猴子（monkey-boy）** | Q6 使用者確認 |
| Voice pool: 悲情敘事 | **吾等蟾亞族 / 我族 / 吾族** | Q6 使用者確認 |
| 現代口語允許度 | **中量允許**（Ouchy-oochy / bummer / dang），避免網路哏 | Q5 使用者確認 |

## 九、參考來源

- **Ultronomicon（Star Control 官方 wiki）** via Wayback Machine
  - [Dnyarri](https://web.archive.org/web/20250919030928/https://wiki.starcontrol.com/index.php/Dnyarri) — 兩萬年前奴役感知聯盟、Kzer-Za 發現痛苦解脫、Ur-Quan 逆轉屠殺
  - [Talking Pet](https://web.archive.org/web/20250918054027/https://wiki.starcontrol.com/index.php/Talking_Pet) — generic 翻譯工具族群
  - [Talking Pet (device)](https://web.archive.org/web/20250918054027/https://wiki.starcontrol.com/index.php/Talking_Pet_(device)) — **本個體 canonical**（neo-Dnyarri）
  - [Glilandy](https://web.archive.org/web/20250919030928/https://wiki.starcontrol.com/index.php/Glilandy) — Dnyarri 最後據點（烏寬圍城處）
- 遊戲對話 `../uqm-work/extracted/base/base/comm/talkingpet/talkingpet.txt`（112 tokens）
- [02_Races/Dnyarri.md](../02_Races/Dnyarri.md)（種族基礎 voice + 兩形態分類）
- `07_Glossary/Master_Glossary.md`（Dnyarri = 蟾亞族 v0.4 / Talking Pet = 會話寵 v0.4 / Taalo = 塔洛族 v0.4）
- `Reference_Material/激戰MS星雲 II 繁體中文化敘事語言學與種族在地化翻譯全指南.md`（Dnyarri 章節）
