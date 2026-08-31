# SC2 zh-TW Level 3 Audit 深度審視政策

**觸發詞**（使用者說任何一個就要遵循此完整流程）：
- "深度審視" / "深度 audit" / "深度掃"
- "依 audit-policy 做 Level 3 深度審視"
- "依 audit-policy 做 Level 3+ 深度審視"（觸發 6 層全跑，特別強調 voice 定量）
- "讀順度深度審視"
- "Voice 定量稽核" / "voice audit"（僅觸發第 6 層）

**背景**：Phase 14c 期間發現 pkunk/ilwrath 有很多讀順度問題和漏翻，使用者反覆提醒。
不能只做「v0.4 rename + 感嘆詞政策」的表層掃。

## 完整 6 層檢查（每族審視必做）

### 第 1 層 · v0.4 canonical
- 蘇菲斯特→修烈士 / 葉哈特→翼哈特 / 阿姆嘎→陰嘎 / 梅爾諾→梅諾商
- 撒達許→撻伐 / 尼亞里→蟾亞 / 蘇波族→蘇菩族 / 德魯族→毒賈族
- 梅蒙→麥孔（誤植修正）
- Master_Glossary.md 為權威

### 第 2 層 · 簡體字 + 繁簡混用
- 用 `_check_zh_purity.py` 但**列表可能不夠完整**
- 手動抽查：后（should be 後 for after）/ 面（should be 麵 for noodle）/ 里（should be 裡 for inside）/ 只（should be 隻 for counter）/ 干（should be 幹）/ 于（should be 於）
- 若使用者說「有簡體字」但 checker 找不到 → 請使用者指出**具體 token / 具體字**

### 第 3 層 · 感嘆詞/口頭禪 Phase 14b/14c 政策
- 情緒感嘆詞、招牌狀聲詞、族群口頭禪一律「中譯＋（原文）」全形括號註記
- 首次出現原則：同 token 內同一詞重複，僅首次註記
- Alien_Speech_Rule §1.4 例外（**不加英文註記**）：
  - Orz `*星號詞*` 格式
  - 已有慣例中譯的專有名詞（Dogar→多加、Kazon→卡宗、田中、武士刀）
  - Lua template first argument
- 宗教核心用語（Juffo-Wup、Frungy 等）**不再保留原文**——應嘗試中譯提選項給使用者挑
- 品牌 gag（1-900-PKUNKRA 等）**應台灣化**

### 第 4 層 · 讀順度深度審視（**最容易漏，必做**）
必須用 `_extract_tokens.ps1` 對照英文原文：
- **直譯痕跡**：英文語序中譯（"so that must" → 「以致必令」，"and more importantly" → 「以及更重要的是」）
- **English syntax bleeding**：逗號位置錯亂、修飾語順序詭異
- **生硬用字**：現代口語詞 vs 該族 voice 衝突（例：Ilwrath 用「音箱」/「優質」/「就不會」——太現代口語）
- **奇怪搭配**：「脂肪被子」/「塗抹全身表面」/「示意他們（指涉物件）」
- **分行斷點錯位**：`\n` 切斷詞組（如「該\n頻道」）
- **英文 pun 丟失**：`Doggone`/`Quasar`/`Dayglo`/`Crayon` 這類玩家嘲弄諧音要保留 gag 精神

**做法**：至少抽 15-20 tokens 用 `_extract_tokens.ps1` 對照英文原文逐句檢查，別只看中文。

### 第 5 層 · Voice consistency + dossier 對照
- 讀 `02_Races/<Race>.md` dossier §四 語言風格 / §五 中文化規則
- 檢查該族 voice 是否一致（例：Ilwrath 應用汝/汝等，不是您/您們）
- 檢查自稱、稱訪客用詞
- 檢查感嘆句式（Ilwrath 用「聽哉」「觀之」、Shofixti 用「俺」）
- **若 dossier 與 Master_Glossary 衝突** → 以 Master_Glossary 為權威，並提示使用者更新 dossier
- **⚠️ v0.7 P0 8 族例外**（Yehat/Shofixti/Kzer-Za/Kohr-Ah/VUX/Chenjesu/Chmmr/Dnyarri）：dossier §四 目前為誤標「文言化」，需先參照 `StarControl2_TW_Localization/00_Project_Control/Dossier_Voice_Audit_2026-08-15.md` 之新語體定位，**不可**直接沿用 dossier 舊定位。若該族尚未做 dossier 修訂 → 提示使用者先修 dossier 再做 audit。

### 第 5.5 層 · **排版 icon 檢查**（v0.7 新增 · 2026-08-15）
sa-matra 對白庫實測，多族原文之**排版格式本身是招牌 icon**，中譯必須複製或用等效手法：

| 族 | 原文排版 icon | 中譯對應手法 | 檢查方式 |
|---|---|---|---|
| Chmmr | 全大寫 `WE ARE FREE!` | 全部包 **粗體** 或超正式命令體 | grep JSON 是否有粗體或極度神諭化句式 |
| Chenjesu (pre-fusion) | 全小寫 `we are the chenjesu` | 現代冥想體 + 無感嘆句 | grep 是否有多餘驚嘆號 |
| Ilwrath | 每個實詞首字大寫 `We Have Spent Many Years` | 齊整化「、」分隔句 + 儀式化動詞 | grep 是否有現代口語進行式 |
| Ilwrath 邪神廣播 | 極端 ALL CAPS `WORSHIP US!` | 全部包**粗體強調** | grep 是否用普通字重 |
| Dnyarri 心控 | `-<GO KILL YOURSELF!>-` 括號 | 保留 `-<...>-` 括號 + 中譯 | grep JSON 是否含 `-<` |
| Slylandro Probe | 全大寫 `THIS PROBE IS PROGRAMMED` | 機械化 + 粗體 | 檢查是否有情緒詞 |
| Umgah 心控 | `ALL. CAPS. WITH. PERIODS.` | 每句以「。」分隔 + 全部粗體 | grep JSON 是否句號密集 |
| Zoq-Fot-Pik | 三方交錯 Zoq/Fot/Pik | 三方前綴一定要保留 | grep 是否有 `佐格：/佛特：/皮克：` |

### 第 6 層 · Voice 定量稽核（**必做，跳過 = Level 3 未完成**）

**觸發條件**：任何 Level 3 audit 一律執行，無例外。第 5 層的「觀察式檢查」不夠，必須用**數字**驗證。

**步驟**：
1. **統計自稱次數**（regex 掃 JSON）：我方 / 我族 / 我等 / 我們 / 咱們 / 咱倆 / 該族專屬自稱 / 單獨『我』
2. **對照該族 dossier §四「自稱」列表**：dossier 列的自稱如果 JSON 完全沒用 → 🔴 高嚴重度
3. **異常門檻**：
   - 任一自稱 >50 次 → 強制按 EN 情境分類
   - 任一自稱占比 >60% → 必然 voice 塌陷，強制細分
4. **情境分類表**（依 EN 原文）：
   - ① 官方廣播 / ② 軍事作戰 / ③ 身世自述 / ④ 集體悲痛 / ⑤ 文化比較
   - ⑥ 個人日常 / ⑦ 親密調情 / ⑧ 情報通報
5. 每個受影響 token 給 Pre → Post 建議
6. 執行後 Post-fix 統計，確認 voice 分布多樣化

**血淚教訓**：
- 2026-08-09 syreen 首次 audit 我方 183 次占比 58%，第 5 層只寫「some 我方 awkward」帶過
- 使用者質疑「翻譯用很多我方字眼… 失去了這種族的感覺」
- 才做定量：183 → 57；我族 7 → 116；我等姐妹 0 → 8；咱倆 0 → 13
- 教訓：dossier 列的自稱如「我等姐妹」「本族女兒」若 JSON 用 0 次 → 一定塌陷了

## 種族 Voice Red Flags（Level 3 前先看，避免同類塌陷）

**⚠️ v0.7 全族審計後**（2026-08-15）：以下 8 族 dossier §四 需先按 `StarControl2_TW_Localization/00_Project_Control/Dossier_Voice_Audit_2026-08-15.md` 修訂後才能做 audit：**Yehat / Shofixti / Kzer-Za / Kohr-Ah / VUX / Chenjesu / Chmmr / Dnyarri**。若未修訂就 audit 會複製舊誤標的「文言化」。

| 族 | 塌陷風險詞 | 應該用什麼 voice |
|---|---|---|
| **syreen** | 我方濫用 | 我族/我等姐妹/咱倆/失家之族（母系氏族+姐妹情+悼母星）|
| **spathi** | 我方濫用 | 小的/本蟹/敝下/發抖語（膽小鬼）|
| **thraddash** | 我方濫用 | 本戰士/本英雄/自誇語（戰士自誇）|
| **VUX** | 我方濫用 | 敝下/賤VUX/自貶語 + **勢利眼傲慢+嘔吐感反應**（v0.7 修，見 audit）|
| **druuge** | 我方濫用 | 敝商會/本商團/商賈語（商人）|
| **melnorme** | 我方濫用 | 敝方/信息掮客語（商人+資訊仲介）|
| **arilou** | 直白俗氣 | 古典飄渺/委婉/暗示式 + **UFO/新時代玄學參考**（v0.7 補）|
| **supox** | 我方濫用 | 本群/群落/根系語 + **Mirror Mimicry**（v0.7 補）|
| **umgah** | 我方濫用 | 本團塊/本膠質 + **Pidgin 缺主詞冠詞**（v0.7 補）|
| **zoq-fot-pik** | 單一自稱 | 三聲部各有自稱！Zoq/Fot/Pik 三種 voice |
| **chmmr** | 全大寫 icon 缺失 | 融合前小寫平靜 `we are the chenjesu`；融合後**全大寫神諭體** `WE ARE FREE!`（v0.7 修）|
| **ilwrath** | 現代口語詞 + 首字大寫 icon 缺失 | 我等/本族蛛狂/宗教莊嚴 + **齊整化「、」分隔句** 模擬原文首字大寫；邪神廣播 **ALL CAPS 粗體**（v0.7 補）|
| **orz** | * 星號詞縮水 | *星號詞* 保留；歐茲/歐茲們（非我方）|
| **kohrah** | 誤用文言判斷句 | **極簡冷酷宣告式現代** `We cleanse.` → 「我方只淨化。」；淨化教義詞 cleanse/filth（v0.7 修，非「吾等」）|
| **yehat** | 誤標「文言化」 | **蘇格蘭勇士古老腔 + 鳥類擬聲 BRAAK!/AWK!**（v0.7 修，非「吾/爾/汝」）|
| **shofixti** | 誤標「文言化」 | **熱血 anime 武士 + 現代粗口 + 日式感嘆** Kyaiee!/Banzai!（v0.7 修）|
| **kzerza** | 誤用「吾等/爾等」 | **本平台 + 我方 + 你 + 現代極正式命令體**（v0.7 修）|
| **chenjesu** (pre-fusion) | 誤標「文言」 | **全小寫詩意冥想體**（v0.7 修）|
| **dnyarri** | 誤標「文言主宰」 | 假模式=**現代諂媚+毒舌黑色**（monkey-boy）；心控=**`-<CAPS>-` 括號命令**（v0.7 修）|

## 報告格式

每族審視完必給使用者：
1. **通過的檢查** ✅（快速列）
2. **🔴 高嚴重度**（必修）
3. **🟡 中嚴重度**（政策決定/選項）
4. **🟢 低嚴重度**（可選）
5. **📚 文件不一致**（dossier 與 Master_Glossary 衝突需修）
6. **對每個 🟡 提供 3-5 個選項**（音譯 / 意譯 / 混合）+ 我推薦哪個
7. **對每個讀順度問題附英文原文對照**（不然使用者會質疑「你確定英文是這樣？」）

## 血淚教訓

- 2026-08-09 shofixti/commander/urquan/slylandro/pkunk/spathi 第一次做審視時 **只掃了第 1-3 層**，使用者連續回報漏翻（Dogar/Kazon）和讀不順 → 才發現要做第 4-5 層
- 2026-08-09 syreen 首次 audit **跳過第 6 層**（我方 183 次未察覺）→ 使用者質疑「翻譯用很多我方字眼 失去了這種族的感覺」→ 才建立第 6 層強制稽核
- 使用者最不能忍受的：**表面說「全部通過」但實際還有一堆讀不順的地方 / voice 塌陷**
- 使用者最能接受的：**列出所有問題 + 給選項 + 對照英文原文說明 + 定量統計**
- **2026-08-10 靜默漏譯陷阱**：發現 `translations/{arilou,chmmr,druuge,supox,syreen}.zh-TW.json` 存在且 audit 完成，但 `build_zh-TW.ps1` **沒有對應的 `translate_ui.py` 步驟**，也沒 include 到 `$chars` 池。這 5 族的 audit 修正**過去所有 build 都沒打包**，玩家看到的是舊版舊譯，audit-policy checker 完全看不出來。
  - **教訓**：完成 audit 後，`Get-ChildItem zh-TW-addon\content\base\comm -Directory` 檔案數必須 == translations 資料夾 comm JSON 數。差異就是漏翻。
  - **防呆**：新增 audit 完成 checklist：`_check_build_coverage.py`（未來寫），確保 每個 comm JSON 都有對應 build step + comm .txt 產出。
- **2026-08-10 urquan token=2 anomaly**：`urquan.zh-TW.json` 只翻了 1 個 token (SEND_MESSAGE, Sol 護盾邊界警告錄音)。EN `urquan.txt` 實際有 **76 tokens** 包括 URQUAN_STORY (Kzer-Za lore 40+ 行) / HELLO_SAMATRA / hypnosis dialog / GENERAL_INFO_1-4 / OUT_TAKES 等。使用者確認**為早期測試用，未來單獨開專案**翻譯剩 74 tokens。
  - **教訓**：Line-count checker PASS 不代表全譯——只驗證 JSON 內 token 的行數，不會警告 EN 有但 JSON 沒有的 token。
  - **待辦**：Urquan Kzer-Za 主線 74 tokens 未譯，需新 dossier §9.5（Kzer-Za voice：僵化階級/絕對主義/現在與永恆之道擬古）+ canonical 詞彙 (Dnyarri=崔亞里, Sentient Milieu=賢者盟, Path of Now and Forever, Eternal Doctrine, Yuptar) + 逐 token 翻譯 + layout 對齊。等同於單獨大 phase。

- **2026-08-11 Round 5 完成 · 26/26 races Level 3 audited 100%**
  (session 998e6e56 turn 226). 從此不再全族重掃,只做 delta retrofit / canonical
  升級。累積 3286 tokens 稽核。**若使用者未來說「深度審視 X」而 X 已 Round 5
  過**,先確認是「Round 5 之後的 regression」還是「全新未 audit」,別重工。

- **2026-08-11 血淚教訓 · 視覺相似字 typo 陷阱 (session 998e6e56 turn 226)**
  `_check_zh_purity.py` 只掃 dialog 主體,**不掃 _notes**。
  Melnorme retrofit 中把 `諸` (U+8AF8, 諸多) 打成 `諾` (U+8AFE, 承諾) →
  Alliance name_2 「異星諸邦協和聯盟」變「異星諾邦協和聯盟」(3 檔連錯)。
  **必查對照**:諾/諸 · 塔/特 · 茨/茲 · 悦/悅 (SIMPLIFIED trap) · 竞 (只用於竞技)
  · 熘/溜 · 諸多相似字。批次 retrofit 完成後**一定要**跑
  `python -c "import unicodedata; ..."` 逐字 Unicode dump 抽查關鍵詞。

- **2026-08-15 v0.7 全族 dossier §四 語體審計血淚教訓**
  Utwig Rebuild-Compare 中發現 dossier §四 舊定位「莎士比亞式悲劇詠嘆調」與 sa-matra.net 對白庫**實證不符**——原文為 Jack Vance 現代學術華麗+Douglas Adams 冷幽默，**無** thou/thee/thy 古語。擴大審計 25 族後發現 **8 族被系統性誤標「文言化」**（Yehat/Shofixti/Kzer-Za/Kohr-Ah/VUX/Chenjesu/Chmmr/Dnyarri）。
  - **教訓**：dossier §四 是**憑印象寫**還是**憑實證寫**要看得出來。凡是宣稱「文言化」的族，一律**先跑 sa-matra 驗證**。若原文無 thou/thee/thy 而是 We/You + 抽象名詞 → 是**現代正式**，不是文言。
  - **教訓**：原文的**排版格式本身是 icon**（全大寫/全小寫/首字大寫/`-<CAPS>-`/Pidgin），舊 audit-policy 沒把這列入檢查 → 已在第 5.5 層補強。
  - **教訓**：兩形態雙人格族（Utwig/Dnyarri/Chmmr/Umgah）需 dossier §四 分段寫；一段式描述會失真。
  - **權威追蹤**：`StarControl2_TW_Localization/00_Project_Control/Dossier_Voice_Audit_2026-08-15.md`（證據）+ `Dossier_Revision_Progress.md`（進度）。
  - **待辦**：P0 8 族 dossier + shipped JSON 尚未修訂（Utwig 已完成 v0.7 作為修訂範本）。

- **2026-08-16 Rebuild_And_Compare.md v0.7.1 新增階段 2.5 · 順暢度自審 Read-Aloud Pass**
  使用者於多族 Rebuild-Compare 執行後回報「直譯不順暢」殘留，需在**產 diff 前**先自查。新流程：
  - **階段 2 clean-room 翻完 → ⑤ 3-gate verify → ⑥ Read-Aloud Pass 自審 → 產 v2.json → 階段 3 diff**
  - 自審清單 7 節：§4.5.1 英文語法殘留（被動語態/長定語/一個那個/連詞/名詞化/時間狀語）· §4.5.2 中文語感（代詞冗餘/量詞/是的句/重複疊詞/口語書面/兩字動詞）· §4.5.3 標點英化（半形/... → …… / -- → ——/中英空格）· §4.5.4 Voice/dossier 一致性（稱謂漂移/招牌詞漏套）· §4.5.5 Read-Aloud Test · §4.5.6 邊界（不動 canonical/招牌/情緒）· §4.5.7 self-fix log
  - **邊界原則**：命中清單 → AI 自己改 · 產 `_selfaudit_<race>_v2_readaloud.md` audit trail；兩種譯法皆通 → 保留 rebuild 版列 🟠 交使用者；動 canonical/招牌 → 升 🔴
  - **新增參數**：`read-aloud: 完整/保守/跳過`（預設完整）
  - **新失敗情境 D**：使用者不同意某些 self-fix 時可 `#N=撤回` 從 partial-K.json 拿回原譯
  - **AI 血淚**：直譯生硬（如「訊息被送出了」「這是一個絕無僅有的機會」）若不先自查，會塞爆 🟠 diff 浪費使用者決策時間 · 也污染 audit trail

- **2026-08-17 UI 詞彙統一 audit 血淚教訓（Outfit Ship 模組名英文事件）**
  用戶回報 Outfit Ship 右下角紅框模組名保留英文（FUEL TANK / CREW POD / ...）。分析後發現：
  1. **根因**：`gamestrings.txt` 有兩個大小寫版模組名段 —— `DOS_STARBASE`（小寫如 `Fuel Tank`）已翻譯，`TDO_STARBASE`（全大寫如 `FUEL TANK`）在 JSON 中**完全缺失 key** → translate_ui.py match 不到 → 保留英文。
  2. **系統性衝突**：TDO 段翻譯提案時，發現**四方詞彙不一致**：
     - `melnorme.zh-TW.json`（P0 audit shipped 對話）主流用「離子波砲/火獄穿甲炮/濕婆熔爐」
     - `gamestrings.zh-TW.json` DOS 段（早期未參考 shipped）用「離子束槍/地獄鑽砲/濕婆熔爐」
     - `setupmenu.zh-TW.json`（模組選項）用「火獄穿甲炮模組/濕婆熔爐模組」
     - `Tech_Names.md`（權威表格）用「地獄砲/希瓦爐」等未被 shipped 採用
  - **教訓 1**：新增 UI 元素前 · **必先掃 shipped comm 對白 + gamestrings JSON + setupmenu** 找既有譯法 · 避免翻新譯造成不一致（同一詞可能已有 3-4 種譯法並存）
  - **教訓 2**：**採 shipped-preference 策略**修 canonical —— shipped 對白已與玩家熟悉度綁定 · 修 `Tech_Names.md` 對齊 shipped 而非反過來
  - **教訓 3**：`gamestrings.zh-TW.json` 的 KEY 對應 `#(ID)` 括號內 · **大小寫敏感**（`Fuel Tank` ≠ `FUEL TANK`）· 檢查漏譯要**看原文 gamestrings.txt 所有 `#(...)` 段是否都在 JSON 有對應 key**
  - **教訓 4**：module.fon 這種點陣字型 addon **可能被字型 pipeline 略過**（Outfit Ship 事件中 `_build_hd_fonts.ps1` 擴充了 30+ 個字型但跳過 module.fon · 幸運的是 HD addon 已有 3035 glyphs 覆蓋所需中文字元）· 新增 UI 中譯前**必驗證對應字型 addon 中文字元覆蓋率**
  - **待辦**：建議未來寫一個 `_check_ui_terminology.py` 掃**所有** shipped translations + Tech_Names + Ship_Modules · 找同英文詞的多譯法衝突 · 定期產出 audit 報告

## 特別注意

- **不要臆測**——不確定用字就對照英文原文
- **不要「覺得OK」就跳過**——生硬中譯會破壞遊戲體驗
- **使用者說「還有簡體字」時** → 別急著反駁「checker 說 0」，先問「哪個 token / 哪個字」
- **每族審視至少花 20 tokens 對照英文原文** 才叫 Level 3
- **每族審視必須跑 Voice 定量統計** 才能宣稱 Level 3 完成
- **dossier §四建議的自稱 JSON 用 0 次** → 必然塌陷，flag 為 🔴
