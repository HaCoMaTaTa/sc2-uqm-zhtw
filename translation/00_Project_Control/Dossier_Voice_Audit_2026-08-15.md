# Dossier 語體審計總表 — v0.7 系統性審視（2026-08-15）

> **本檔功能**：對 25 個種族 dossier `§四 語言風格` 之定位進行**實證審計**——以 [sa-matra.net](https://www.sa-matra.net/quotes/) 對白庫為 ground truth，比對現行 dossier §四 是否與原文語體吻合。
> **背景**：Utwig 完成 v0.7 修訂後（舊定位「莎士比亞式悲劇詠嘆調」被證誤，改為「現代學者式憂鬱華麗長句 + 官僚報告體 + 冷式反諷」），使用者要求對全種族做同樣審視。
> **產出定位**：本檔為**證據存檔**，不含決策；決策追蹤見 [Dossier_Revision_Progress.md](Dossier_Revision_Progress.md)。

**審計方法**：
1. 讀取每族 `02_Races/<Race>.md` §四 現行「說話速度／正式程度／幽默程度／情緒表達／特殊語法」
2. 抓取 sa-matra.net `/quotes/<race>` 對白全文
3. 對比：dossier 定位是否與原文語體（含**排版格式 icon**）吻合？
4. 分類：✅ 正確 / ⚠️ 需微調 / ❌ 重大錯誤 / 🔍 需查證

---

## 一、總結（Executive Summary）

**25 族審計結果分類**：

| 分類 | 族數 | 名單 |
|---|---|---|
| ✅ **正確** | 10 | Druuge, Melnorme, Orz, Pkunk, Slylandro（主族）, Spathi, Supox, Thraddash, Utwig（已 v0.7 修）|
| ⚠️ **需微調** | 7 | Ilwrath, Umgah, Slylandro_Probe, Syreen, Arilou, Mycon, Zoq_Fot_Pik |
| ❌ **重大錯誤（P0）** | 8 | **Chenjesu, Yehat, Shofixti, Ur_Quan（Kzer-Za）, Ur_Quan_Kohr_Ah, VUX, Dnyarri, Chmmr** |
| 🔍 **需查證** | 2 | Androsynth（滅絕、無 dialog）, Mmrnmhrm（sa-matra 無單獨 URL）|

**核心系統性發現**：

**現行 dossier 中「文言化」被過度濫用**——8 族之中就有 6 族被誤標為「文言化」。實證：SC2 英文是 1992 年**現代英語**，全庫**沒有** thou / thee / thy / wilt / hast。原文的「莊嚴感」實際來自：
- **正式現代英語 + 大量抽象名詞**（官樣、公文、學術）
- **排版格式 icon**（全大寫、全小寫、首字大寫、括號心控等）
- **獨特擬聲詞或方言腔調**（蘇格蘭、日式、宗教頌歌）

而不是「吾/爾/之/乃/矣/哉」等文言助詞。

---

## 二、審計證據明細

### 2.1 ❌ 重大錯誤（P0 — 需 Utwig 級別修訂）

| # | 族 | Dossier §四 現況 | Sa-Matra 實測特徵 | 建議修訂方向 |
|---|---|---|---|---|
| 1 | **Chenjesu** | 極正式、**文言化**（文白折衷） | **全小寫詩意冥想體**：`we are the chenjesu... we are the mmrnmhrm`；現代英語詩化排版；冷靜哲思 | 廢止「文言」；新定位「**全小寫破格詩意獨白 + 沉思冥想現代體**」 |
| 2 | **Yehat** | 極正式、**文言化** + 封建詞彙 | **蘇格蘭勇士腔**：`ye/fer/canna/'Tis/yer`；**鳥類擬聲**：`BRAAK!/AWK!/HISS!/HOOT!`；中世紀騎士榮譽 | 廢止「文言」；新定位「**蘇格蘭勇士古老腔 + 鳥類擬聲 + 中世紀騎士榮譽**」（Braveheart / Robert Burns 風） |
| 3 | **Shofixti** | **文言化** + 日式時代劇 | **熱血 anime 武士 + 現代英語粗口**：`leprous, non-functional sex organ`；**日式感嘆詞**：`Kyaiee!/Hyai!/Banzai!` | 廢止「文言」；新定位「**熱血 anime 武士 + 現代粗口 + 日式感嘆詞**」 |
| 4 | **VUX** | 極正式、**宮廷式** | **勢利眼傲慢 + 嘔吐感反應**：`Augh! You are even uglier...`；**現代口語毒舌**；ZEX 個體 = 變態華麗 | 廢止「宮廷式」；新定位「**勢利眼傲慢 + 嘔吐感 + 現代口語毒舌**；ZEX 為變態華麗詩意分支」 |
| 5 | **Ur_Quan Kzer_Za** | 極正式、帝國宣示式（含**文言判斷句**） | **極正式現代英語 + 帝國宣示 + 命令口吻**：`Your independence is too dangerous for us to tolerate` | 移除「文言判斷句」；改為「**極正式現代命令體 + 教義宣示**」 |
| 6 | **Ur_Quan_Kohr_Ah** | 極短促、極簡冰冷、**用文言判斷句** | **極簡冷酷宣告式現代英語**：`We do not kill. We cleanse.` / `You are filth.`；淨化教義口吻 | 移除「文言判斷句」；改為「**極簡冷酷宣告 + 淨化教義詞彙**（cleanse/filth/purify）」 |
| 7 | **Dnyarri / Talking Pet** | 幼童化 + 古代主宰（**兩形態雙人格**） | **假模式**：現代諂媚 + 毒舌黑色反諷（`monkey-boy` / `boneless toady dweeb`）；**心控模式**：`-<CAPS BRACKETS>-` 命令 | 廢止「幼童化+古代主宰」；新定位「**假模式現代諂媚+毒舌黑色**」+「**心控模式 `-<CAPS>-` 括號命令**」 |
| 8 | **Chmmr** | 極正式，**神諭感** | **全大寫神諭體**：`WE ARE FREE! YOU HAVE FLOODED OUR SYNTHESIS MECHANISMS`；融合後高姿態 | 補充「全大寫」+「融合宣告口吻」細節 |

### 2.2 ⚠️ 需微調（P1 — 大方向對，細節需補）

| 族 | 現行 dossier | 應補充 / 修正 |
|---|---|---|
| **Ilwrath** | 禱詞感 + 宗教儀式化 | ➕ **每個實詞首字大寫**（`We Have Spent Many Years Gleefully Preying On The Pkunk`）—— **這是招牌 icon**（原文 100% 這樣排版）；另加「愉悅殺戮 + 邪教狂喜」<br>➕ 邪神 Dogar/Kazon **廣播用極端 ALL CAPS**（`WORSHIP US!`） |
| **Umgah** | 粗俗黑色荒謬 | ➕ **PIDGIN 缺主詞冠詞語法**（`we not allowed do`, `it against Ur-Quan Laws`）<br>➕ 心控時 **`ALL. CAPS. WITH. PERIODS.`** |
| **Slylandro_Probe** | 極正式機械式 | ✅ 大致對；補**全大寫格式**（`THIS PROBE IS PROGRAMMED`）需明確寫入 |
| **Syreen (Talana)** | 半正式優雅、姐妹情、**古典感** | ⚠️ 「古典感」誤導；實為**現代女性軍事指揮官口語 + 調情式 + 深沉哀傷**（多用現代口語如 `Sweet Cakes` / `Cowabunga`） |
| **Arilou** | 半正式、詩意 | ➕ **UFO/新時代玄學參考**（Roswell / Men in Black / Celts）；`*time*` 星號強調；橢圓省略號重 |
| **Mycon** | 禱詞式短句 + 大量刪節號 | ✅ 大致對；補**深時意識恍惚獨白**（`I died 57,283 years ago`） |
| **Zoq_Fot_Pik** | 極快、口語、插科打諢 | ✅ 對；補「**三方交錯對白**」需視覺 marking（Zoq/Fot/Pik 各行一詞）；「Frungy!」招牌 |

### 2.3 ✅ 正確（無需大修）

| 族 | Dossier | 評 |
|---|---|---|
| **Druuge** | 商業敬語、極正式、反諷質感 | ✅ 對 · 可補「**企業律師合同體 + 法規條款**」細節 |
| **Melnorme** | 高階商務、精練機智 | ✅ 對 · 綠光個體幽默感明確 |
| **Orz** | 星號詞語 | ✅ **完全對** |
| **Pkunk** | 新時代嘻皮 + 狂熱靈修 | ✅ **完全對** |
| **Slylandro（主族）** | 半正式詩意悠閒 + 溫和自嘲 | ✅ 對（主族與 Probe 分開；Probe 見 P1） |
| **Spathi（Fwiffo）** | 卑躬屈膝、免責頭、拜託拜託 | ✅ **完全對** |
| **Supox** | 極正式優雅 + 植物意象 | ✅ 對 · 補「**Mirror Mimicry**」（Supox 會鏡像模仿玩家的自介方式） |
| **Thraddash** | 粗魯自嘲、`SNORT!`、狂妄 | ✅ 對 · 補「**HARG! HARG! HARG!** 大笑」+「教師模式時的 pig latin / rhyme / wacky 荒謬」 |
| **Utwig** | v0.7 已完成修訂（2026-08-15） | ✅ 本次審計即由 Utwig 修訂案觸發，作為所有其他族的**修訂模型範本** |

### 2.4 🔍 需查證

| 族 | 情況 |
|---|---|
| **Androsynth** | SC2 中已滅絕，無 dialog；dossier「機械節奏、冷硬」為推測，暫難以驗證 |
| **Mmrnmhrm** | sa-matra 無單獨 URL；資料合併於 Chenjesu URL（前段 pre-transformation dialog）；dossier「機械精確、簡潔」大致對 |

---

## 三、系統性教訓（適用於所有種族審計）

### 3.1 「文言化」被濫用（8 族被誤標！）

**問題根源**：現行 8 族 dossier 都將「莊嚴感」等同於「用文言助詞」。但 SC2 英文是 1992 年**現代英語**，**沒有** thou / thee / wilt / hast 等古語。

**正確作法**：要「莊嚴感」用**正式現代中文**：
- **公文體**（「委員會調查已正式聲明」）
- **命令體**（「立即撤離戰區」）
- **詩意獨白體**（「我們曾漫步於群星之間」）
- **宗教頌歌體**（「聖光普照大地」）

**不是**「吾/爾/之/乃/矣/哉/焉」。

### 3.2 原文的**文字排版本身也是 icon**（必須複製）

| 族 | 排版特徵 |
|---|---|
| **Chenjesu**（pre-Chmmr） | **全小寫** `we are the chenjesu` |
| **Ilwrath** | **每個實詞首字大寫** `We Have Spent Many Years` |
| **Ilwrath 邪神廣播** | **極端 ALL CAPS** `WORSHIP US!` |
| **Chmmr** | **全大寫神諭體** `WE ARE FREE!` |
| **Slylandro Probe** | **全大寫** `THIS PROBE IS PROGRAMMED` |
| **Umgah 心控** | **`ALL. CAPS. WITH. PERIODS.`** |
| **Dnyarri 心控** | **`-<ANGLE BRACKETS CAPS>-`** 命令括號 |
| **Kohr-Ah** | 極短句 + 淨化教義詞 |
| **Zoq-Fot-Pik** | **三方交錯**（Zoq/Fot/Pik 各行一詞） |

**這些排版格式在中譯時必須複製、或用等效手法呈現**，不能夷平為統一句式。

### 3.3 原文含大量**現代口語 idiom**（不要文言化）

實測見於原文的現代口語：
- `Sweet Cakes` / `Cowabunga` (Syreen)
- `monkey-boy` / `boneless toady dweeb` (Dnyarri)
- `puny human` / `stupid alien dog` (Thraddash)
- `Cripes!` / `Frungy!` (Zoq-Fot-Pik)
- `leprous, non-functional sex organ` (Shofixti Tanaka)

**中譯要用台灣現代口語對應**（見 `08_Translation_Rules/Style_Guide.md` §3.1），**不要文言化**。

### 3.4 兩形態雙人格族需分別定位

以下族有兩形態，**兩形態的語體差異很細**，dossier §四 應分兩段寫：

| 族 | 形態 A | 形態 B |
|---|---|---|
| **Utwig** | Ultron 損壞（憂鬱期） | Ultron 修復（狂喜期） |
| **Dnyarri** | 假 Talking Pet 諂媚模式 | 心控真形態命令模式 |
| **Chmmr** | Chenjesu / Mmrnmhrm（融合前） | Chmmr（融合後全大寫神諭） |
| **Umgah** | 一般粗俗黑色荒謬 | 蟾亞附身時心控點斷句 |

---

## 四、審計方法論（給未來 session 參考）

**若要對某族再次做本審計**，步驟：

1. **抓 dossier §四**：`grep_search` on `02_Races/<Race>.md` §四 說話速度/正式程度/幽默程度/情緒表達/特殊語法
2. **抓原文對白**：`fetch_webpage("https://www.sa-matra.net/quotes/<race>")`（族名對照：見附錄）
3. **交叉比對 6 個維度**：
   - 是否有 thou / thee / thy 等古語？→ 若無，則不能標「文言化」
   - 是否有特殊排版格式（大小寫/括號/星號）？→ 必列入
   - 是否有現代口語 idiom？→ 對照台灣現代口語
   - 是否有兩形態？→ 是否已分段
   - 幽默類型是否標對？（見 `08_Translation_Rules/Humor_Rule.md`）
   - 情緒觸發雷區是否對應原文情境？
4. **產出**：dossier §四 修訂草稿；記錄到 `Dossier_Revision_Progress.md`

**Sa-Matra URL 對照**：
| Dossier 族名 | Sa-Matra URL 片段 | 備註 |
|---|---|---|
| Androsynth | (無 URL) | 已滅絕 |
| Arilou | `arilou` | |
| Chenjesu | `chmmr`（合併） | 前段為 pre-transformation dialog |
| Chmmr | `chmmr` | |
| Dnyarri | `dnyarri` | |
| Druuge | `druuge` | |
| Ilwrath | `ilwrath` | |
| Melnorme | `melnorme` | |
| Mmrnmhrm | `chmmr`（合併） | |
| Mycon | `mycon` | |
| Orz | `orz` | |
| Pkunk | `pkunk` | |
| Shofixti | `shofixti` | |
| Slylandro | `slylandro` | 主族 |
| Slylandro_Probe | `slylandro` | 同 URL 內 |
| Spathi | `spathi` | |
| Supox | `supox` | |
| Syreen | `syreen` | |
| Thraddash | `thraddash` | |
| Umgah | `umgah` | |
| Ur_Quan（Kzer-Za） | `ur-quan` | 帶連字號 |
| Ur_Quan_Kohr_Ah | `kohr-ah` | 帶連字號 |
| Utwig | `utwig` | v0.7 已修 |
| VUX | `vux` | |
| Yehat | `yehat` | 含 Yehat Rebels |
| Zoq_Fot_Pik | `zoqfotpik` | |

---

## 五、下一步

**執行追蹤**：見 [Dossier_Revision_Progress.md](Dossier_Revision_Progress.md)

**修訂優先順序建議**：
1. **P0 · 高優先**（可能已污染 shipped JSON）：Yehat → Shofixti → Ur-Quan/Kzer-Za → Ur-Quan/Kohr-Ah → VUX → Chenjesu/Chmmr → Dnyarri
2. **P1 · 中優先**（僅補細節，不改核心方向）：Ilwrath, Umgah, Syreen, Arilou
3. **P2 · 低優先**（可選）：Zoq_Fot_Pik, Slylandro_Probe, Thraddash 排版明確化

---

**文件版本**：v1.0（2026-08-15 建立）
**建立者**：Utwig Rebuild-Compare workshop 觸發之全族審計
**權威來源**：sa-matra.net 對白庫（`fetch_webpage` 於 2026-08-15）
