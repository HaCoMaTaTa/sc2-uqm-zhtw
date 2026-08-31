# 中文化過程回憶錄 · Localization Journey

> 這不是技術文件，是給後續維護者的 warning + celebration。
> 記錄從 2026-08-04 動工到 v3.8 release 的血淚教訓，共 3547 tokens / 34 patches / 20+ dossier / 100+ commits。

---

## 為何做這個專案

Star Control 2 是我心中永遠的太空歌劇宇宙。1992 年的遊戲，1990 年代已有非官方繁中版流傳，但基於 3DO/DOS 版本，畫質粗糙、翻譯是簡體轉繁體（很多用詞怪異）。

MegaMod 分支重新整合了 HD 資產、修了很多 QoL bug，但沒有繁中化。而且原作者對「翻譯」這件事有一種近乎執念的品味 — Jack Vance 華麗辭藻 + Douglas Adams 冷幽默 + 26 個種族各有招牌 voice — 一般機翻或懶惰的音譯會**毀掉**這個宇宙。

於是動手做「配得上原作 voice 的繁中化 + Android 移植」。目標：
- 對話：像**台灣人在同一情境會怎麼罵人 / 求饒 / 讚嘆**
- 敘事：保留 Jack Vance 學究感，但別用文言
- Voice：每族有招牌自稱、感嘆詞、句式節奏 · 不塌陷成千篇一律的「我方」

---

## 技術踩雷 Top 10

### 1. Zip64 EOCD → patch 007（2026-08-10 血淚）

MegaMod UIO 只支援 ZIP32。翻到 29 族時 zh-TW.uqm 累積 83k+ files 觸發 PowerShell `Compress-Archive` 自動切 Zip64 → 遊戲 log 直接說「Function not implemented, 0 available addon packs」，全英文顯示。

修法：patch 007 給 MegaMod 加了 ~50 行 Zip64 EOCD Record 解析。首次驗證通過那一刻整個 addon 一次全部亮起，超激動。

### 2. CJK 無空格觸發 `_count_lines` 無限迴圈（2026-08-05 血淚）

引擎 comm.c 的 word-wrap 只斷 ASCII 空格。CJK 一整行是一個「word」寬 > AlienTextWidth 時，`getLineWithinWidth` 回 FALSE 但**沒推進 pStr** → do-while 死迴圈，`BatchGraphics` 攔著 DCQ mutex，渲染執行緒卡死。

症狀超級誤導：voice OGG 播放完美，然後才 crash。花了 4 個小時 debug 才鎖定。

修法：**space-wrap**（CJK 塊間插入 ASCII 空格）+ patch 006 讓 CJK 自成 word boundary。

### 3. commander.fon 9px 對 CJK 太小

原版每個種族有專屬字型檔 · commander.fon 只有 9px（Latin 字型），CJK 塞不進去。試了縮 CJK 到 9px = 讀不清；試了直接跳字型 = 缺 glyph。

最終方案：**shadow-content 重定向** — 把 `base/fonts/commander.fon/` 目錄改用 computer.fon (15px) 的 raster 產物 + 改 kerndat.fnt 第一個 token 對齊資料夾名。這樣做需要每次翻新族都重跑一次 rasterize。

### 4. `\n` 過多切碎 OGG 音訊

`SplitSubPages` 用 `\n` 切 comm 對話成「頁」，每頁對應一段 OGG 音訊 offset。若你為了 CJK wrap 加了額外 `\n` → 頁數翻倍 → 音訊 slice 超過 OGG EOF → 崩潰。

規則：**保持與英文原文一樣的 `\n` 數量**，用 ASCII 空格做 CJK 內部斷點。

### 5. Lua template first-arg 英語洩漏

`<% comm.getColor("blue", "rainbow 4") %>` 在 vanilla StarSeed=false 直接回第一個參數字面 → 中譯遊戲會冒出「blue」。

規則：first-arg 要中譯（`"藍色"`），plot arg 隨便。寫了 `_check_lua_templates.py` 當閘門。

### 6. 字型 kerndat.fnt 第一 token 必須對齊資料夾名

複製 A.fon 內容到 B.fon 目錄後忘記改 kerndat 第一行 → 引擎 crash「renderer thread blocking on DCQ」。debug 過程只看到 stack trace 說 blocking，完全沒提示 kerndat。

修法：`package_zh-TW.ps1` 內加 `$fontRedirects` 自動改。

### 7. HD 模式改 SD 字型無效（2026-08-13 血淚）

使用者玩 HD (`--addon mm-hd --addon zh-TW --addon zh-TW-hd`)，我改 `zh-TW.uqm` 內的 pkunk.fon，使用者截圖回饋「完全沒感覺」。花半個 session 才發現 HD 靠 `zh-TW-hd.uqm` 覆蓋所有字型。

規則：改字型前**必須先問使用者玩 SD / HD**。寫進 AI_BUILD_GUIDE.md 首頁。

### 8. 34 個引擎 patch 的血淚（每一個都有故事）

我最愛的：
- **patch 008** CJK scan report hang · 幾乎所有 lander 報告都會凍結 · 花 6 小時定位到 report.c word-scan loop
- **patch 018** Android SDL2 NULL guard · emulator 假 focus loss 事件觸發跨平台 upstream bug
- **patch 021~025** Android 虛擬 joystick · 讓觸控搖桿變成 SDL GameController · UQM `create_joystick` gate 才會通過

### 9. Android JBR 25 vs Gradle 8.14.3 = Java 版本地獄（2026-08-22 血淚）

Android Studio Meerkat 內建 JBR = **OpenJDK 25.0.2**。Gradle 8.14.3 只支援到 Java 24。跑 gradlew 就報「What went wrong: 25.0.2」訊息完全誤導。

解法：強制用 Adoptium Temurin 21 zip，`JAVA_HOME` 指到獨立 JDK 21，Studio IDE 內用 JBR，CLI Gradle 用 Temurin。

### 10. mm-hd.uqm 頂層資料夾結構（2026-08-24 血淚）

打包 mm-hd 時把 `mm-hd/mm-hd.rmp` 攤平為 `mm-hd.rmp` + `battle/` + `comm/`... → 引擎把每個子資料夾當成獨立 addon 掛載，變成「11 available addon packs: battle, comm, cutscene, fonts, lander, nav, planets, ships, ui, zh-TW, zh-TW-hd」而不是 3 個。

規則：**必須要有 `mm-hd/` 頂層資料夾包起來**，同 `zh-TW.uqm` 的 `zh-TW/uqm.rmp` 結構。

---

## 翻譯風格踩雷 Top 5

### 1. dossier §四「文言化」誤標（2026-08-15 v0.7 全族審計）

發現至少 8 族 dossier 舊版把「莎士比亞式悲劇詠嘆調 / 文言判斷句 / 吾等爾等」當成招牌 voice，但 sa-matra.net 對白庫實測**原文根本沒有** thou/thee/thy。原文是 Jack Vance 現代學術華麗 + Douglas Adams 冷幽默，是**現代英語的正式書面**，不是仿古。

教訓：**dossier §四 是「憑印象」還是「憑實證」寫要看得出來**。凡是宣稱「文言化」的族，一律先跑 sa-matra 驗證。

修訂範圍：Yehat / Shofixti / Kzer-Za / Kohr-Ah / VUX / Chenjesu / Chmmr / Dnyarri 共 8 族全 dossier + shipped JSON 重譯。

### 2. Voice 塌陷 · 「我方」濫用（2026-08-09 syreen 血淚）

第一次 syreen audit 表面通過，但使用者質疑「翻譯用很多我方字眼… 失去了這種族的感覺」。跑定量統計：「我方 183 次 / 佔比 58%」。

塞蓮應是母系氏族+姐妹情+悼母星，應該用「我族 / 我等姐妹 / 咱倆 / 失家之族」，結果全塌成「我方」。修完統計：183→57 · 我族 7→116 · 我等姐妹 0→8 · 咱倆 0→13。

教訓：加了 **audit 第 6 層 · Voice 定量稽核**，任何 audit 一律強制跑，不能只做「觀察式檢查」。

### 3. Ship_Names.md vs Master_Glossary 衝突（2026-08-28 血淚）

Umgah audit 時只查 Ship_Names.md 說「無人機」誤導，實際 canonical 是「蜂機艦」（Master_Glossary 才對）。
Zoqfotpik 一樣 · dossier v0.7 寫「刺激者號」但 Master_Glossary v0.5.2 更新為「刺針號」→ 3 處誤修需 revert。

教訓：canonical 決策前一律先 grep Master_Glossary + 檢查日期戳。優先度：Master_Glossary > Ship_Names > dossier。

### 4. 視覺相似字 typo（100+ 次）

Batch replace 常犯的錯：

| 目標 | 誤打 | 場景 |
|---|---|---|
| 諸多 | 諾邦 | Alliance name |
| 賈德 | 賣德 | 賈德魔怪 |
| 醜聞 | 醬聞 | safeones |
| 蠢貨 | 蟲貨 | yehat |
| 骨骸 | 骸骨 | kohrah |
| 撻伐 | 沒伐 | thraddash |
| 沾點 | 沒點 | supox |

`_check_zh_purity.py` 只擋簡體字，這些「typo but still 繁中」全部漏掉。必須人眼再讀一次。

### 5. 音譯 vs 意譯選擇

例子：Frungy 錦標賽（芙戎奇）· Kyaiee!（殺呀！）· Dogar & Kazon（多加 & 卡宗）· PKUNKRA（普恩喇，一個 1-900 廣告 gag）...

規則：
- 神明/宗教核心用語 · 音譯 · 保留原文粗體
- 情緒感嘆詞 · 意譯+全形括號註英文原文（首次出現）
- 品牌 gag（1-900-PKUNKRA）· 台灣化（1-900-普恩喇）
- 有慣例中譯的專有名詞 · 直接用中文（田中、武士刀、Dogar → 多加）

---

## 統計數字

- **翻譯 tokens 總量**：3547（跨 28 個 NPC 對白 + UI + gamestrings）
- **完成度**：99.5%（僅剩 Urquan Kzer-Za 主線 74 tokens 未譯 · 待另案）
- **引擎 patches**：34 個（PC 6 個 · Android 12 個 · 星圖 3 個 · 其他 13 個）
- **Race Level 3 audits**：26 族全數完成
- **dossier §四 修訂**：P0 9 族 + P1 7 族 + P2 3 族 = 19 族 v0.7 修訂完成
- **git commit**：150+ 次（PC 中文化 + Android 移植合計）
- **Android APK 版本迭代**：v1.0 → v3.8（40+ 中間版本）· 每次都有 delta improvement
- **PC ZIP 版本迭代**：v1.0-rc1 → v1.0.12
- **開發時間**：2026-08-04 → 2026-08-31 · 約 4 週集中衝刺

## 給後續維護者的建議

1. **改 canonical 前先 grep Master_Glossary**（血淚 3 次）
2. **改字型前先問使用者玩什麼模式**（HD/SD/3DO）
3. **audit 一律跑第 6 層 voice 定量**，別跳
4. **batch replace 完人眼再讀一次**，purity gate 抓不到 typo
5. **Lua template `<%...%>` 完全不動**
6. **加 shipped 之前 grep 其他 shipped 找既有譯法**，避免 4 種譯法並存
7. **改 Android build 前先讀 android-build.md**，JBR vs JDK 是必踩坑
8. **重要決定給選項讓使用者挑**，不要臆測

## 最感謝的事

- **Toys for Bob** · Fred Ford & Paul Reiche III · 你們造了一個永遠不會過時的宇宙
- **UQM Team** · 讓這個宇宙開源，讓我們粉絲能碰
- **JHGuitarFreak & MegaMod team** · HD 資產、Android scaffold、Kzer-Za 主線擴充
- **sa-matra.net** · 對白庫實證資料的權威來源
- **Ark Pixel / Fusion Pixel** · 開源像素字型救了 CJK 顯示的命
- **本次的 AI 協作**（Claude 家族）· 4 週密集配合，一起 debug 一起 audit 一起 rewrite
- **未來下載這個 apk 玩的玩家** · 希望你玩得開心，若翻譯哪裡怪，開個 issue，我修

**願星辰之火，永不熄滅。**
