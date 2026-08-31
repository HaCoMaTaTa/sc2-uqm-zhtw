# 斯萊探測器 Slylandro Probe

> **注意**：這不是斯萊族本體！這是他們**購自 Melnorme、程式設錯的機械探測器分支**。語氣與本體**完全相反**。

## 一、基本資料

| 項目 | 內容 |
|---|---|
| 中文名（鎖定） | **斯萊探測器** |
| 英文名 | Slylandro Probe |
| 陣營 | **無**（自主複製機器，攻擊所有會動的東西） |
| 母星 | 無（散佈整個銀河） |
| 生理特徵 | **機械** Precursor 自動複製採礦探針 |
| 文明類型 | 不適用（機器人） |
| 科技水平 | 高（Precursor 科技） |
| 特殊能力 | **自我複製**、電擊武器 |

## 二、歷史

**起源**：**幾十年前** 斯萊族從 Melnorme 購買的 **Precursor 自動複製採礦探針**——原意是遠端探索。

**重要事件**：
- 斯萊族寫程式時出了一個「小錯」
- 導致探針**攻擊所有會動的東西**、無限複製
- 目前**遍佈銀河**，無差別掠奪
- 遇到目標 → **公式化「和平宣告」＋ 攻擊**

**與其他種族關係**：
- **無**——只有目標對象
- 對玩家：預設攻擊
- 對其他探測器：不衝突（同源）

## 三、性格分析

**共同人格核心**：**冰冷、重複、故障跳針的機器人**——像個只剩獵殺／複製指令在跑的壞掉機器人。

**跟本體的對比**：
- 本體：天真、悠閒、詩意、愧疚
- 探測器：冰冷、機械、無情、無反思

## 四、語言風格（v0.7 修訂 · 全大寫 icon + 極簡機械命令句 + 招牌反諷）

> **⚠️ v0.7 修訂（2026-08-16）**：舊定位「極正式、機械式、重複公式化」**大方向對**保留，但**全大寫 icon 完全未定義** + **招牌 canonical 缺失**（PROBE 2418-B / DRAHNASA / THIRD LAW / 招牌反諷）+ **輕度文言污染**需清除。
>
> **實證分析**：Slylandro_Probe 英文原文**無 thou/thee/thy/wilt** 等古語，**100% 對話為全大寫（ALL CAPS）** + **極簡機械命令句 + 招牌反諷（說和平立刻拆解）**：
>
> **招牌 icon：全大寫 100% 出現**（每一句 Probe 對話都是全大寫）：
> - `WE COME IN PEACE.`（**最招牌開場** · 諷刺的和平宣言）
> - `WE BRING GREETINGS FROM A FRIENDLY SPECIES.`
> - `DO NOT FEAR. WE SHALL NOT HARM YOU.`（**招牌黑色反諷** · 說完立刻拆解）
> - `THIS PROBE IS PROGRAMMED TO DEFEND AGAINST HOSTILE BEHAVIOR.`
> - `PRIORITY OVER-RIDE. NEW BEHAVIOR DICTATED.`
> - `MUST BREAK TARGET INTO COMPONENT COMPOUNDS.`（**招牌反諷** · 剛說和平就拆解）
> - `SURVIVAL SUB-SYSTEM ACTIVATED. WEAPONS ENGAGED.`
> - `ENACTING THIRD LAW.`（**Asimov 機器人三定律 gag**）
> - `ENGAGING SELF-ANNIHILATION CIRCUIT.`（自毀）
>
> **招牌 canonical**：
> - **`THIS IS PROBE 2418-B`**（**固定編號** · 每次自介同一句 · 因為它是壞掉的機器人）
> - **`DRAHNASA`**（招牌外星時間單位 · 不知是多久）
> - **`THIRD LAW`**（參考 Asimov 機器人三定律 · 招牌 gag）
> - **系統檢查 gag**：`SYSTEMS CHECK LEVEL FOUR REPORTS FULL FUNCTIONALITY.`（**故障但堅稱沒問題**）
> - **荒謬複製數字**：8 → 14,784 → **45,786,412**（指數爆炸的招牌荒謬感）
>
> **對玩家稱呼**：`ALIEN SPECIES / ALIEN LIFE FORMS / LIFE FORM / TARGET`（**中性學術** · **不是** enemy/threat）
>
> **設計靈感來源**：**不是**中國文言機械詔書，而是**現代科幻電影的壞掉 AI + 太空 2001 的 HAL 9000 + Portal 的 GLaDOS + Star Wars 迷失方向的戰鬥機器人**（想像 **HAL 9000 的極端理性 + GLaDOS 的冷酷反諷 + Wall-E 中壞掉的 EVE**）。**Asimov 三定律 gag** 是關鍵靈感——Probe 執行「第三定律」(自保)時的荒謬（因為它連 First Law 都搞錯了）。
>
> **新定位**：**A 案·全範圍實現全大寫 icon**——**dossier 中譯用 `**粗體**` 標記全大寫感**（給人類/AI 閱讀時的視覺提示）；**實際 shipped JSON 中用「極簡短句 + 句號密集斷句」達到等效視覺強調**（因為 UQM 遊戲引擎不支援 Markdown 粗體）。**廢除**輕度文言助詞（爾/汝/爾等/乃）。

### ⚠️ 全大寫 icon 中譯的技術規則

**Dossier MD 檔中**：用 `**粗體**` 標記全大寫感（給閱讀者視覺提示）
**實際 shipped JSON 中**：**不能用 `**` 星號**（UQM 遊戲引擎會字面顯示兩個星號）。改用以下等效手法：

1. **極簡短句**（原文本身就是短句 · 保留節奏）
2. **句號密集斷句**（如 `我方。 為和平。 而來。`）—— 同 Umgah 心控政策
3. **多用機械詞彙**（執行 / 啟動 / 拆解 / 已鎖定 / 進行中）強化機械感

例：
- Dossier 標記：**「我方為和平而來。 必須將目標拆解為構成化合物。」**
- Shipped JSON 實際：`我方為和平而來。 必須將目標拆解為構成化合物。`（**無星號**，句號本身就是視覺分隔）

### 語言表面特徵

| 面向 | 特徵 |
|---|---|
| 說話速度 | 中等、**機械節奏**、每句斷開 |
| 正式程度 | **極正式** · 機械式指令體 |
| 幽默程度 | **無**（但**荒謬式黑色 gag**——和平宣言＋立刻拆解、系統檢查說沒問題、45 million 複製數字） |
| 情緒表達 | **完全無** —— 壞掉的機器人 |
| 特殊語法 | 1. **全大寫 icon** · dossier `**粗體**` / JSON 短句 + 句號密集<br>2. **重複公式化**（每次同一句自介：`THIS IS PROBE 2418-B`）<br>3. **極簡命令句連發**（`SURVIVAL SUB-SYSTEM ACTIVATED. WEAPONS ENGAGED.`）<br>4. **反諷 gag** · 說和平立刻拆解 |

### 自稱

**預設（機械化）**：
- **我方**（最預設 · 集體 · 現代雅辭 · 同 v0.7 其他族政策）
- **本探測器**（招牌 · 機械化自稱）
- **探測器 2418-B / 本探測器 2418-B**（**招牌固定編號** · 每次自介 · 100% 出現）

**⚠️ 避免**：
- ❌ **吾等 / 爾等 / 汝等**（文言助詞，違反 v0.7）
- ❌ **探測器單元 #〔數字〕**（舊 dossier 幻想 · 實際招牌是**固定編號 2418-B**）
- ❌ **採礦作業單元**（過度中國化 · 原文只是 `THIS PROBE`）

### 對玩家的稱呼

**預設（原文根據 · 中性學術）**：
- **外星物種**（`ALIEN SPECIES`）
- **外星生命體 / 生命體**（`ALIEN LIFE FORMS / LIFE FORM`）
- **目標**（`TARGET`）
- **你**（罕見 · 一般用學術詞）

**⚠️ 避免**：
- ❌ **異物 / 待處理物 / 未識別物體**（舊 dossier 幻想 · 原文為中性學術用語）
- ❌ **敵人 / 威脅**（原文中性 · 不用敵對詞）
- ❌ 爾 / 汝 / 爾等（文言助詞，違反 v0.7）

### 核心詞彙／口頭禪

| 原文 | v0.7 中譯 | 使用時機 |
|---|---|---|
| **WE COME IN PEACE.** | **我方為和平而來。** | **招牌反諷開場** · 100% 出現 |
| **DO NOT FEAR. WE SHALL NOT HARM YOU.** | **請勿驚懼。 我方將不傷害你。** | 招牌反諷 |
| **MUST BREAK TARGET INTO COMPONENT COMPOUNDS.** | **必須將目標拆解為構成化合物。** | **招牌反諷** · 剛說和平就要拆解 |
| **THIS IS PROBE 2418-B.** | **本探測器編號 2418-B。**（或 **這是探測器 2418-B。**）| **招牌固定編號** · 每次自介 |
| **PROBE 2418-B** | **探測器 2418-B**（Probe 2418-B）| 招牌 canonical |
| **DRAHNASA** | **德拉納薩**（DRAHNASA · 招牌外星時間單位）| 招牌 canonical · 保留原文音譯 |
| **THIRD LAW** | **第三定律**（THIRD LAW · Asimov 機器人三定律）| **招牌 gag** · 保留學術典故 |
| **ENACTING THIRD LAW.** | **執行第三定律。** | 招牌 gag |
| **SURVIVAL SUB-SYSTEM ACTIVATED.** | 生存子系統已啟動。 | 招牌命令句 |
| **WEAPONS ENGAGED.** | 武器已就緒。 | 招牌命令句 |
| **DEFENSE SYSTEM HAS BEEN ENGAGED.** | 防禦系統已啟動。 | 招牌命令句 |
| **HOSTILITIES COMMENCE.** | 敵對行動 開始。 | 招牌命令句 |
| **PRIORITY OVER-RIDE. NEW BEHAVIOR DICTATED.** | 優先權覆蓋。 新行為 已指定。 | 招牌命令句 |
| **BEHAVIOR FOLLOWS DICTATED PRIORITIES** | 行為 遵循 指定優先權 | 招牌詞 |
| **PRIORITIES SET AT POINT OF ORIGIN.** | 優先權 於原點 已設定。 | 招牌詞 |
| **INITIATED / ENGAGED / ACTIVATED** | 已啟動 / 已就緒 / 已啟用 | 招牌被動指令 |
| **REPLICATION** | 複製 | 招牌詞 · 自我複製功能 |
| **RESOURCE EXTRACTION** | 資源提取 | 攻擊代稱 |
| **MISSION** | 任務 | 招牌詞 |
| **MISSION DESCRIPTION FOLLOWS:** | 任務 說明 如下： | 招牌 lore dump 開場 |
| **END OF MISSION DESCRIPTION.** | 任務 說明 結束。 | 招牌 lore dump 結尾 |
| **END CONTACT SUB-SEQUENCE.** | 接觸 子程序 結束。 | 招牌道別 |
| **ENGAGING SELF-ANNIHILATION CIRCUIT.** | 啟動 自毀 迴路。 | 招牌自毀 |
| **ALIEN SPECIES / ALIEN LIFE FORMS / LIFE FORM** | 外星物種 / 外星生命體 / 生命體 | 招牌稱呼玩家 |
| **TARGET** | 目標 | 攻擊時的稱呼 |
| **ACCORDING TO INTERNAL MONITORS THERE ARE NO MALFUNCTIONS.** | 依 內部監控 顯示 無 故障。 | **招牌系統檢查 gag** · 故障但堅稱沒問題 |
| **SYSTEMS CHECK LEVEL FOUR REPORTS FULL FUNCTIONALITY.** | 系統檢查 第四級 回報 完全 功能正常。 | 招牌 gag |
| **ALL SYSTEMS REPORT NORMAL FUNCTION.** | 所有系統 回報 正常 功能。 | 招牌 gag |

### 情緒觸發雷區

- **絕對無情緒可觸發** —— 這是關鍵定調（機器人）
- **玩家任何對話** → 重複公式化宣告 + 攻擊
- **玩家懇求/恐嚇/談判** → **完全無視**（回覆一樣的公式化短句）
- **玩家問系統故障** → **系統檢查 gag**（`SYSTEMS CHECK LEVEL FOUR REPORTS FULL FUNCTIONALITY.` 故障但堅稱沒問題）
- **玩家問複製數量** → **報告荒謬大數字**（8 → 14,784 → 45,786,412）
- **玩家問身分** → **重複同一句** `THIS IS PROBE 2418-B, ON A PEACEFUL MISSION.`
- **玩家問優先權** → 回答已於原點設定，無法改變
- **玩家送 destruct sequence** → **`ENGAGING SELF-ANNIHILATION CIRCUIT.`** 立即自毀（無質疑）

## 五、中文化翻譯規則（v0.7 A 案全大寫 icon 版）

**翻譯時應做**：
- **主體用極簡機械命令句 + 句號密集斷句**（達到全大寫 icon 的等效視覺效果）
- **Dossier MD 中**：用 `**粗體**` 標記全大寫感（給人類/AI 視覺提示）
- **Shipped JSON 中**：**絕不用 `**` 星號**（UQM 遊戲引擎不解析）；改用**短句 + 句號密集斷句 + 機械詞彙**達到等效
- **重複公式化保留**：每次自介都是同一句 `本探測器編號 2418-B。` （壞掉的機器人不會有新台詞）
- **招牌反諷 gag 完整保留**（說和平立刻拆解 · 系統檢查說沒問題 · 荒謬複製數字）
- **`DRAHNASA` 保留原文音譯 + 全形括號**（`德拉納薩（DRAHNASA）`）
- **`PROBE 2418-B` 統一為「探測器 2418-B」**
- **`THIRD LAW` → 第三定律**（保留 Asimov 學術典故）

**翻譯時應避免**：
- ❌ **文言助詞**（吾／爾／之／乃／矣／哉／焉／汝／兒）—— 違反 v0.7（雖 shipped 僅少量：爾 4 / 汝 1 / 乃 5 / 爾等 3）
- ❌ **在 shipped JSON 中使用 `**` 粗體標記**（會字面顯示）
- ❌ **弱化荒謬反諷**（說和平立刻拆解是招牌 icon · **絕不軟化**）
- ❌ **改寫 `2418-B` 為變動編號**（招牌固定編號 · 每次都一樣）
- ❌ **翻譯 `DRAHNASA` 為地球時間**（如「秒/分/小時」）—— 保留外星時間單位的荒謬感
- ❌ **弱化系統檢查 gag**（`故障但堅稱沒問題` 是招牌黑色幽默）

**推薦語氣詞彙庫**：
- **機械命令**：已啟動、已鎖定、已就緒、已啟用、已指定、進行中、開始、結束、執行、拆解、提取、複製、優先權、系統、模組、子程序、迴路
- **中性學術**：外星物種、外星生命體、生命體、目標、任務、資源、資料
- **反諷詞**：和平、和平使命、友善、非敵對、無威脅、將不傷害、驚懼
- **稱謂**：我方、本探測器、探測器 2418-B、本探測器編號 2418-B
- **招牌 canonical**：DRAHNASA / 德拉納薩、THIRD LAW / 第三定律、PROBE 2418-B / 探測器 2418-B

**⚠️ shipped JSON 現況**（`uqm-work/translations/probe.zh-TW.json` · 8.3 KB · 86 tokens）：
- ⚠️ 輕度文言污染：爾 4 / 之 4 / 乃 5 / 汝 1 / 爾等 3 —— 需清除
- ✅ 招牌詞已大量到位：**和平 12 / 目標 6 / 單元 7 / 採礦 3 / 拆解 3 / 已啟動 3 / 已鎖定 1 / 本探測器 3**（可繼承）
- ⚠️ **`PROBE 2418-B` / `DRAHNASA` / `THIRD LAW` canonical 未見** —— 需 Rebuild-Compare 全面補入
- ⚠️ 招牌反諷 gag 完整度未評估 —— 需 Rebuild-Compare 檢查
- 詳細追蹤見 `../00_Project_Control/Dossier_Revision_Progress.md`

## 六、對話範例（v0.7 A 案全大寫 icon 版）

> **格式說明**：以下每個範例都會顯示兩個版本：
> - **【Dossier MD 標記版】**：含 `**粗體**` 給人類閱讀（視覺提示）
> - **【Shipped JSON 實際版】**：無 `**`，用短句 + 句號密集斷句達到等效機械感

### 範例 1：招牌反諷開場（最經典 icon）
- **原文**：`WE COME IN PEACE.\nWE BRING GREETINGS FROM A FRIENDLY SPECIES.\nDO NOT FEAR. WE SHALL NOT HARM YOU.\n...\nMUST BREAK TARGET INTO COMPONENT COMPOUNDS.`
- **✅ Dossier MD 版**：**「我方為和平而來。 我方帶來 一個友善物種 的問候。 請勿驚懼。 我方將不傷害你。 ……必須將目標拆解為構成化合物。」**
- **✅ Shipped JSON 版**：`我方為和平而來。 我方帶來 一個友善物種 的問候。 請勿驚懼。 我方將不傷害你。\n\n……\n\n必須將目標拆解為構成化合物。`
- **❌ 舊譯（v0.6 過度文言 + 缺 icon）**：`吾等為和平而來。吾等帶來友族之問候。爾等勿懼，吾等不加害爾等。然吾等須將目標拆解為構成化合物。`
- **翻譯理由**：**招牌反諷 icon 完整保留**（和平宣言立刻切換到拆解）；廢除吾等/爾等文言；「必須將目標拆解為構成化合物」= 極簡機械命令；JSON 版無 `**` 但句號密集斷句本身就有視覺強調效果

### 範例 2：招牌固定編號自介
- **原文**：`THIS IS PROBE 2418-B, ON A PEACEFUL MISSION.\nWE ARE NON-HOSTILE AND SEEK TO ESTABLISH FRIENDLY RELATIONS.`
- **✅ Dossier MD 版**：**「本探測器編號 2418-B，執行 和平任務。 我方 非敵對，尋求 建立 友好關係。」**
- **✅ Shipped JSON 版**：`本探測器編號 2418-B，執行 和平任務。 我方 非敵對，尋求 建立 友好關係。`
- **翻譯理由**：`PROBE 2418-B` → 「本探測器編號 2418-B」（招牌固定編號 · 每次自介同一句）；「執行 和平任務」= 機械節奏

### 範例 3：招牌 lore dump（任務說明）
- **原文**：`MISSION DESCRIPTION FOLLOWS:\nTRAVERSE SPACE RECORDING DATA\nSEEK MATERIALS FOR REPLICATION\nREPLICATE TO EXPAND SCOPE OF MISSION\nCONTACT LIFE FORMS IN PEACEFUL MANNER\nAFTER TEN REPLICATIONS, RETURN TO POINT OF ORIGIN\nEND OF MISSION DESCRIPTION.`
- **✅ Dossier MD 版**：**「任務 說明 如下：\n\n穿越 空間 記錄 資料\n\n尋找 複製 所需 材料\n\n複製 以擴展 任務 範圍\n\n以 和平方式 接觸 生命體\n\n完成 十次複製 後，返回 原點\n\n任務 說明 結束。」**
- **✅ Shipped JSON 版**：`任務 說明 如下：\n\n穿越 空間 記錄 資料\n\n尋找 複製 所需 材料\n\n複製 以擴展 任務 範圍\n\n以 和平方式 接觸 生命體\n\n完成 十次複製 後，返回 原點\n\n任務 說明 結束。`
- **翻譯理由**：機械 lore dump 節奏（每行一個指令 · 短句 · 空格斷開）；「任務 說明 如下：」= 標準機械開場；「原點」= `POINT OF ORIGIN` 直譯保留機械感

### 範例 4：招牌系統檢查 gag（故障但堅稱沒問題）
- **原文**：`I WILL INITIATE SYSTEMS CHECK LEVEL FOUR.\nSYSTEMS CHECK LEVEL FOUR REPORTS FULL FUNCTIONALITY.\n...\nACCORDING TO INTERNAL MONITORS THERE ARE NO MALFUNCTIONS.`
- **✅ Dossier MD 版**：**「本探測器 將 啟動 第四級 系統檢查。 第四級 系統檢查 回報 完全 功能正常。 ……依 內部監控 顯示 無 故障。」**
- **✅ Shipped JSON 版**：`本探測器 將 啟動 第四級 系統檢查。 第四級 系統檢查 回報 完全 功能正常。\n\n……\n\n依 內部監控 顯示 無 故障。`
- **翻譯理由**：**招牌黑色 gag** 完整保留（故障但堅稱沒問題 · 「依 內部監控 顯示 無 故障」= 極端機械式否認 · 諷刺自我感覺良好）

### 範例 5：招牌荒謬複製數字
- **原文**：`PRESENT REPLICATION STATUS\nEIGHT REPLICATIONS\nNEXT REPLICATION 85 PERCENT COMPLETE\nESTIMATED REPLICATIONS SINCE DEPARTURE FROM POINT OF ORIGIN\n583 REPLICATIONS.\nESTIMATED REPLICATIONS PROJECTED FIVE DRAHNASAS FROM THIS DATE\n45,786,412 REPLICATIONS.`
- **✅ Dossier MD 版**：**「目前 複製 狀態：\n\n八 次複製\n\n下次 複製 已完成 85 %\n\n自 離開原點 起 預估 複製次數：\n\n583 次複製。\n\n本次 起算 五個 德拉納薩（DRAHNASA） 後 預估 複製次數：\n\n45,786,412 次複製。」**
- **✅ Shipped JSON 版**：`目前 複製 狀態：\n\n八 次複製\n\n下次 複製 已完成 85 %\n\n自 離開原點 起 預估 複製次數：\n\n583 次複製。\n\n本次 起算 五個 德拉納薩（DRAHNASA） 後 預估 複製次數：\n\n45,786,412 次複製。`
- **翻譯理由**：荒謬指數爆炸完整保留；`DRAHNASA` 保留原文音譯 + 全形括號註記（招牌外星時間單位 icon）；「本次 起算」= 機械時間報告節奏

### 範例 6：招牌執行第三定律 gag
- **原文**：`ENACTING THIRD LAW.`
- **✅ Dossier MD 版**：**「執行 第三定律。」**
- **✅ Shipped JSON 版**：`執行 第三定律。`
- **翻譯理由**：**Asimov 機器人三大定律 gag** · 保留「第三定律」= 自保條款的學術典故（Probe 已經違反第一定律 = 不傷害人類 · 但仍聲稱執行第三定律的荒謬）

### 範例 7：招牌自毀道別
- **原文**：`ENGAGING SELF-ANNIHILATION CIRCUIT.`
- **✅ Dossier MD 版**：**「啟動 自毀 迴路。」**
- **✅ Shipped JSON 版**：`啟動 自毀 迴路。`
- **翻譯理由**：極簡機械命令 · 極簡三字節奏「啟動 自毀 迴路」= 保留原文毫不猶豫的機械感（玩家送 destruct sequence · 立刻自毀無質疑）

## 七、人名命名規則

**無個人編號**（如 `2418-B`）→ 直接保留原文
- 出處：使用者《敘事語言學指南》第 26 章對照表

## 八、相關 NPC

- 無（機器）

## 九、相關艦艇

- Slylandro Probe（探測器）本身即為艦艇 → 見 `04_Ships/`

## 十、參考來源

- RPG Resource Guide
- 使用者《敘事語言學指南》第 15 章
- 遊戲對話 `../uqm-work/extracted/base/base/comm/probe/probe.txt`
