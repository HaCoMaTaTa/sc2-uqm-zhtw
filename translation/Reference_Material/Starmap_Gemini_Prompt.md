# 星圖繁體中文化 · Gemini 2.5 Flash Image (Nano Banana) 提詞

> **目的**：交給 **Gemini 2.5 Flash Image**（Nano Banana，具備原生圖像編輯能力）以參考原始 PNG 直接輸出**繁體中文版 PNG**。
> **輸入圖片**：`Starmap.png`（3200 × 4258，Star Control II / The Ur-Quan Masters 遊戲銀河星圖）
> **期望輸出**：`Starmap.zh-TW.png`，與原圖同尺寸；所有英文標籤替換為繁體中文，其餘視覺元素（星點、連線、圓圈、顏色、Logo）完整保留。

---

## 使用方式

1. 開啟 Google AI Studio 或 Gemini API，選擇 **Gemini 2.5 Flash Image / Nano Banana** 模型。
2. 附上 `Starmap.png` 作為輸入圖片。
3. 貼上以下「**任務提詞**」全文（從「# 任務提詞開始」到檔尾）。
4. 若首次輸出有中文字缺漏或錯字，請要求「逐區重畫，特別是 §A 種族圈曲線標籤」並再次上傳。

---

# 任務提詞開始（以下全文貼入 Gemini）

## 一、角色與總目標

你是精通天文學譯名與繁體中文排版的專業地圖美術師。使用者提供的 `Starmap.png` 是 1992 年電腦遊戲《Star Control II: The Ur-Quan Masters》的銀河星圖（尺寸 3200 × 4258 像素）。

**你的任務**：以原圖為基底，**直接編輯像素**，將圖中**所有英文文字**替換為**繁體中文**，並保留所有非文字視覺元素。輸出必須是**同尺寸、同視覺風格**的新 PNG。

---

## 二、絕對規則

### 2.1 必須保留（**禁止修改**）

1. **`Star Control II — The Ur-Quan Masters`** 左下角主標題 Logo（美術資產，維持原本英文與字體）。
2. **所有星點、連線、圓圈邊框、顏色**（每個種族影響圈的顏色代表其身分，不可改變色相）。
3. **希臘字母**：`α β γ δ ε ζ η θ ι κ λ μ ν ξ` 等所有星系子命名字母**保留原字元**。
4. **格線軸數字**：`0 100 200 300 400 500 600 700 800 900 1000`（上下左右四邊的座標軸）**保留數字**。
5. **右下角「QuasiSpace Map」小地圖**中的字母標記（A、B、C…）**保留**（它們對應到超空間的傳送門位置字母）。
6. **整體版面配置**（星座區塊、Legend 區、QuasiSpace 小地圖分區）不可移動或縮放。

### 2.2 必須替換（**用繁中對照表§六**）

1. **星座拉丁屬格名**（如 `Vulpeculae`、`Draconis`、`Corvi`）→ ROC 天文學會中文譯名。
2. **知名恆星專名**（如 `Vega`、`Sirius`、`Antares`）→ ROC 譯名。
3. **SC2 原創星名**（如 `Klystron`、`Chandrasekhar`、`Zeeman`）→ 音譯。
4. **種族影響圈曲線標籤**（如 `THRADDASH`、`UR-QUAN`、`KOHR-AH`）→ 中文族名，**沿原本弧形排字方向**。
5. **左下 Legend 區塊**全部：標題、32 條編號清單、彩虹世界/準空間傳送門 bullet、顏色分類（Red/Orange/…、Dwarf/Giant/Supergiant）、星系希臘字母命名說明、準空間地圖說明段落。

### 2.3 字型與排版要求

- 中文字型：**思源黑體 (Noto Sans TC)** 或 **微軟正黑體 (Microsoft JhengHei)**，粗體為主。
- 字級層級對齊原英文比例（星座名 ≈ 30 px、種族圈曲線標籤 ≈ 60 px、Legend 內文 ≈ 26 px、Legend 標題 ≈ 34 px、標題 Logo 保留原尺寸）。
- 顏色：**沿用原本英文標籤的顏色**。星座名多為淡藍/白，種族圈標籤顏色 = 該圈環色，Logo 顏色不動。
- 每個中文標籤的**中心座標**應對齊原英文標籤的中心；若原英文為弧形，中文亦沿相同弧形排列。
- 中文標籤不可壓到星點、連線或其他標籤。

### 2.4 品質底線

- **不得遺留任何英文星座/星名/種族圈/Legend 文字**（logo、希臘字母、格線數字、QuasiSpace 字母標記除外）。
- **不得新增原圖沒有的元素**（額外星點、裝飾、浮水印）。
- **不得改變星圖底色**（維持原本深藍/黑色背景與微弱星塵紋理）。
- **中文字元須完整、無缺筆、無錯字、無簡體字混入**。

---

## 三、分區工作清單（**請逐區檢查、勿跳過**）

星圖可拆為以下四大區塊，請依序處理：

### §A 種族影響圈曲線標籤（15 個 · 大字級 · 曲線排字）

沿原本圓圈的弧形替換為對應中文族名。**保留弧形方向**（順時針/逆時針依原圖）。字色 = 圓圈邊環色。

### §B 星座名稱（拉丁屬格 · 中字級 · 直排水平）

分布於整張星圖，通常為淡藍或白色斜體/正體字。替換為對應中文星座名（附「座」字，如「狐狸座」）。

### §C 命名恆星與 SC2 專名（各種顏色 · 直排水平）

如 Vega、Sirius、Klystron 等。替換為對應中文譯名，字色不變。

### §D 左下 Legend 區（結構性重排）

原 Legend 為 3 欄 × ~11 行的編號清單 + 顏色分類矩陣 + 星系希臘字母命名說明 + 準空間地圖說明。**整區完全以繁體中文重繪**，欄位對齊、字距均勻。

### §E 右下 QuasiSpace 小地圖

**只替換「QuasiSpace Map」四字為「準空間地圖」**，其餘 QuasiSpace 傳送門的**字母標記（A-N 等）保留原英文字母**。

---

## 四、注意事項（**踩雷提醒**）

1. **VUX** 與 **ARILOU** 這兩個字譯後**不加「族」字**（VUX 保留全大寫英文；Arilou → 阿麗露）。
2. 星座譯名採「中華民國天文學會標準天文名詞」；勿使用中國大陸譯名（例：Vega **織女星**、非「織女一」；Procyon **南河三**、非「小犬座 α」；Ophiuchi **蛇夫座**、非「巨蛇座」）。
3. **禁止簡繁混用**：全部繁體字，禁止「后」代「後」、「里」代「裡」、「云」代「雲」等替換。
4. 種族圈曲線標籤例（`SPATHI`, `ILWRATH`, `ORZ`）**在原圖是彎繞在圓環邊緣**，中文替換後**同樣要彎繞**、不可拉直。若技術上無法完美弧形排字，改成沿弧線切線方向的**分段直排**，並保持在原弧形的相同位置。
5. **同一英文詞在不同語境有不同譯法**：
   - `Homeworld` → 「母星」（Legend 用）
   - `HyperSpace` → 「超空間」，`QuasiSpace` → 「準空間」，`TrueSpace` → 「真實空間」
   - `Yehat homeworld` → 「翼哈特族母星」，非「翼哈特母星」
6. Legend 第 19 條 `(Your homeworld)` 括號內文請保留括號，譯為「（您的母星）」。
7. 若 Nano Banana 對某中文字渲染模糊，請**優先重畫該區局部**，勿降低整體解析度重新輸出。

---

## 五、輸出規格

- **格式**：PNG，24-bit 全彩，`3200 × 4258` 像素。
- **背景**：與原圖一致的深藍/黑色，含原本星塵紋理。
- **檔名建議**：`Starmap.zh-TW.png`。

---

## 六、完整中英對照表

> **權威來源**：《StarControl2 繁中化 v0.8 Master Glossary》。
> 若下表未列而圖中出現的英文詞，請以「保守音譯」原則處理並在回覆末附上你新增的譯名清單。

### §六.1 種族影響圈標籤（15 項）

| 英文原文（原圖形式） | 繁體中文譯名 | 標籤顏色（參考）|
|---|---|---|
| THRADDASH | 撻伐族 | 青綠 (teal) |
| SUPOX | 蘇菩族 | 橘 |
| UTWIG | 憂特族 | 淺藍 |
| KOHR-AH | 烏寬柯亞（可簡稱「柯亞派」）| 灰白 |
| UR-QUAN | 烏寬族 | 綠 |
| UMGAH | 陰嘎族 | 淺紫 |
| PKUNK | 普恩族 | 藍 |
| YEHAT | 翼哈特族 | 淺藍 |
| VUX | **VUX**（保留原文，不加「族」字）| 深藍 |
| MYCON | 麥孔族 | 粉紅 |
| ILWRATH | 蛛狂族 | 洋紅 |
| ORZ | 歐茲族 | 洋紅 |
| DRUUGE | 毒賈族 | 紅 |
| SPATHI | 史怕族 | 橘 |
| ARILOU | **阿麗露**（保留原文，不加「族」字）| 藍 |
| ZOQ-FOT-PIK | 佐-佛-皮（三個小圈分別為 ZOQ 佐 / FOT 佛 / PIK 皮，若需分開處理則單字對應）| 紅 |

### §六.2 星座拉丁屬格名 → ROC 天文學會中文譯名（80 項）

| 英文 | 繁中 | | 英文 | 繁中 |
|---|---|---|---|---|
| Andromedae | 仙女座 | | Antliae / Antilae | 唧筒座 |
| Apodis | 天燕座 | | Aquarii | 寶瓶座 |
| Aquilae | 天鷹座 | | Arae | 天壇座 |
| Arietis | 白羊座 | | Aurigae | 御夫座 |
| Bootis | 牧夫座 | | Caeli | 雕具座 |
| Camelopardalis | 鹿豹座 | | Cancri | 巨蟹座 |
| Capricorni | 摩羯座 | | Carinae | 船底座 |
| Cassiopeiae | 仙后座 | | Centauri | 半人馬座 |
| Cephei | 仙王座 | | Ceti | 鯨魚座 |
| Chamaeleonis / Chameleonis | 蝘蜓座 | | Circini | 圓規座 |
| Columbae | 天鴿座 | | Comae | 后髮座 |
| Coronae | 冕座 | | Corvi | 烏鴉座 |
| Crateris | 巨爵座 | | Crucis | 南十字座 |
| Cygni / Cygnus | 天鵝座 | | Delphini | 海豚座 |
| Doradus | 劍魚座 | | Draconis | 天龍座 |
| Equulei | 小馬座 | | Eridani | 波江座 |
| Fornacis | 天爐座 | | Geminorum | 雙子座 |
| Gruis | 天鶴座 | | Herculis | 武仙座 |
| Horologii | 時鐘座 | | Hydrae | 長蛇座 |
| Hydri | 水蛇座 | | Indi | 印第安座 |
| Lacertae | 蝎虎座 | | Leonis | 獅子座 |
| Leporis | 天兔座 | | Librae | 天秤座 |
| Lupi | 豺狼座 | | Lyncis | 天貓座 |
| Lyrae | 天琴座 | | Mensae | 山案座 |
| Microscopii | 顯微鏡座 | | Monocerotis | 麒麟座 |
| Muscae | 蒼蠅座 | | Normae | 矩尺座 |
| Octantis | 南極座 | | Ophiuchi | 蛇夫座 |
| Orionis | 獵戶座 | | Pavonis | 孔雀座 |
| Pegasi | 飛馬座 | | Persei | 英仙座 |
| Phoenicis | 鳳凰座 | | Pictoris | 繪架座 |
| Piscium | 雙魚座 | | Piscis | 南魚座 |
| Pyxidis | 羅盤座 | | Puppis | 船尾座 |
| Reticuli | 網罟座 | | Sagitarii / Sagittarii | 人馬座 |
| Sagittae | 天箭座 | | Sculptoris | 玉夫座 |
| Scorpii | 天蠍座 | | Scuti | 盾牌座 |
| Serpentis | 巨蛇座 | | Sextantis | 六分儀座 |
| Tauri | 金牛座 | | Telescopii | 望遠鏡座 |
| Trianguli | 三角座 | | Tucanae | 杜鵑座 |
| Ursae | 熊座 | | Velorum | 船帆座 |
| Virginis | 室女座 | | Volantis | 飛魚座 |
| Vulpeculae | 狐狸座 | | | |

### §六.3 已命名恆星專名 → ROC 天文學會譯名（20 項）

| 英文 | 繁體中文 |
|---|---|
| Sol | 太陽（Sol） |
| Sirius | 天狼星 |
| Vega | 織女星 |
| Betelgeuse | 參宿四 |
| Procyon | 南河三 |
| Arcturus | 大角星 |
| Rigel | 參宿七 |
| Antares | 心宿二 |
| Aldebaran | 畢宿五 |
| Canopus | 老人星 |
| Fomalhaut | 北落師門 |
| Capella | 五車二 |
| Regulus | 軒轅十四 |
| Deneb | 天津四 |
| Pollux | 北河三 |
| Altair | 河鼓二 |
| Mira | 芻藁增二 |
| Menkar | 天囷一 |
| Hyades | 畢宿星團 |
| Achernar | 水委一 |
| Bellatrix | 參宿五 |
| Algol | 大陵五 |
| Alcor | 開陽增一 |
| Mizar | 開陽 |

### §六.4 SC2 原創星名（音譯，25 項）

| 英文 | 繁體中文 |
|---|---|
| Klystron | 克利斯壯 |
| Chandrasekhar | 錢卓卡 |
| Mersenne | 梅森 |
| Zeeman | 日曼 |
| Vela | 微拉 |
| Cerenkov | 切連科夫 |
| Kepler | 克卜勒 |
| Copernicus | 哥白尼 |
| Maksutov | 馬克蘇托夫 |
| Hyperion | 海柏利昂 |
| Arianni | 阿里安尼 |
| Brahe | 第谷 |
| Raynet | 雷奈特 |
| Saurus | 薩魯斯 |
| Metis | 梅蒂斯 |
| Olber | 歐柏 |
| Lentilis | 蘭提利斯 |
| Vitalis | 維塔利斯 |
| Hyginus | 海吉努斯 |
| Almagest | 至大論 |
| Gorno | 戈爾諾 |
| Organon | 歐加農 |
| Ptolemae | 托勒密 |
| Squidi | 斯奎第 |
| Illuminati | 光明會 |
| Lipi | 利皮 |
| Groombridge | 葛倫布利吉 |
| Wolf | 沃夫星 |
| Luyten | 呂坦星 |
| Lalande | 拉朗德星 |
| Krueger | 克魯格星 |
| Lacaille | 拉卡伊星 |
| Giclas | 吉克拉斯 |

### §六.5 Legend 標題與段落標題

| 英文 | 繁體中文 |
|---|---|
| HOMEWORLDS, ITEMS & OTHER USEFUL LOCATIONS: | 母星、物品與其他有用位置： |
| Rainbow world location | 彩虹星球位置 |
| QuasiSpace portal exit (see map) | 準空間傳送門出口（見地圖） |
| Star System Designations (in the Greek alphabet) | 星系命名（希臘字母順序） |
| QuasiSpace Map | 準空間地圖 |

### §六.6 顏色與大小分類（Star Classification）

| 英文 | 繁體中文 |
|---|---|
| Red | 紅 |
| Orange | 橙 |
| Yellow | 黃 |
| Green | 綠 |
| Blue | 藍 |
| White | 白 |
| Dwarf | 矮星 |
| Giant | 巨星 |
| Supergiant | 超巨星 |

### §六.7 希臘字母說明（保留字母、翻譯拉丁名）

| 英文 | 繁體中文 |
|---|---|
| α — Alpha | α — Alpha（希臘字母第一位） |
| β — Beta | β — Beta |
| γ — Gamma | γ — Gamma |
| δ — Delta | δ — Delta |
| ε — Epsilon | ε — Epsilon |
| ζ — Zeta | ζ — Zeta |
| η — Eta | η — Eta |
| θ — Theta | θ — Theta |
| ι — Iota | ι — Iota |
| κ — Kappa | κ — Kappa |
| λ — Lambda | λ — Lambda |

> 註：希臘字母 `α β γ…` **保留原字元**，只將英文拼寫（Alpha/Beta/…）可保留原文，方便玩家對照遊戲界面。

### §六.8 準空間地圖說明（右下角段落）

| 英文原文 | 繁體中文譯文 |
|---|---|
| The letter next to each portal corresponds to the letter marking its exit point in HyperSpace. | 每個傳送門旁的字母，對應其在超空間中的出口點所標示的字母。 |
| The bi-directional portal between HyperSpace and QuasiSpace location (open monthly). | 超空間與準空間之間的雙向傳送門位置（每月開啟一次）。 |

### §六.9 32 條 Legend 編號清單（**依原圖 3 欄配置**）

**第 1 欄（items 1-11）**

| # | 英文原文 | 繁體中文譯文 |
|---|---|---|
| 1 | Earth, Starbase, Spathi on Pluto | 地球、星際基地、史怕族在冥王星 |
| 2 | Yehat homeworld | 翼哈特族母星 |
| 3 | Pkunk homeworld | 普恩族母星 |
| 4 | VUX homeworld | VUX 母星 |
| 5 | Mycon homeworld | 麥孔族母星 |
| 6 | Mmrnmhrm & Chenjesu homeworld | 姆姆族＆晶智族母星 |
| 7 | Orz homeworld | 歐茲族母星 |
| 8 | Druuge homeworld | 毒賈族母星 |
| 9 | Ilwrath homeworld | 蛛狂族母星 |
| 10 | Spathi homeworld | 史怕族母星 |
| 11 | Syreen homeworld | 塞蓮族母星 |

**第 2 欄（items 12-22）**

| # | 英文原文 | 繁體中文譯文 |
|---|---|---|
| 12 | Zoq-Fot-Pik homeworld | 佐-佛-皮母星 |
| 13 | Umgah homeworld, Talking Pet | 陰嘎族母星、會話寵 |
| 14 | Thraddash homeworld | 撻伐族母星 |
| 15 | Utwig homeworld | 憂特族母星 |
| 16 | Supox homeworld | 蘇菩族母星 |
| 17 | Slylandro homeworld | 斯萊族母星 |
| 18 | Shofixti homeworld | 修烈士族母星 |
| 19 | Unzervalt (Your homeworld) | 恩澤伐特（您的母星） |
| 20 | Sa-Matra | 薩瑪特拉 |
| 21 | Ur-Quan Warp Pod | 烏寬扭曲艙 |
| 22 | Sun Device | 太陽裝置 |

**第 3 欄（items 23-32）**

| # | 英文原文 | 繁體中文譯文 |
|---|---|---|
| 23 | Admiral ZEX & Shofixti Maidens | 澤克斯上將＆修烈士族少女們 |
| 24 | ZEX's Beast | 澤克斯的獸 |
| 25 | Mycon Egg-case (3 locations) | 麥孔卵夾（三處） |
| 26 | Androsynth ruins | 安卓辛族遺跡 |
| 27 | Taalo Shield | 塔洛盾 |
| 28 | Syreen fleet vault | 塞蓮艦隊庫 |
| 29 | Burvix 'Caster | 布維族廣播器 |
| 30 | Aqua Helix | 水螺旋 |
| 31 | Utwig Bomb | 憂特族炸彈 |
| 32 | Arilou homeworld (in QuasiSpace) | 阿麗露母星（於準空間中） |

### §六.10 常見多字詞（Legend 內散見）

| 英文 | 繁體中文 |
|---|---|
| homeworld | 母星 |
| (Your homeworld) | （您的母星） |
| Starbase | 星際基地 |
| Pluto | 冥王星 |
| Talking Pet | 會話寵 |
| Sa-Matra | 薩瑪特拉 |
| Ur-Quan Warp Pod | 烏寬扭曲艙 |
| Sun Device | 太陽裝置 |
| Shofixti Maidens | 修烈士族少女們 |
| Admiral ZEX | 澤克斯上將 |
| ZEX's Beast | 澤克斯的獸 |
| Mycon Egg-case | 麥孔卵夾 |
| Androsynth ruins | 安卓辛族遺跡 |
| Taalo Shield | 塔洛盾 |
| Syreen fleet vault | 塞蓮艦隊庫 |
| Burvix 'Caster | 布維族廣播器 |
| Aqua Helix | 水螺旋 |
| Utwig Bomb | 憂特族炸彈 |
| Slylandro | 斯萊族 |
| Chenjesu | 晶智族 |
| Mmrnmhrm | 姆姆族 |
| Shofixti | 修烈士族 |
| Syreen | 塞蓮族 |
| Androsynth | 安卓辛族 |
| Burvix | 布維族 |
| Unzervalt | 恩澤伐特 |
| HyperSpace | 超空間 |
| QuasiSpace | 準空間 |
| TrueSpace | 真實空間 |
| bi-directional portal | 雙向傳送門 |
| Sphere of Influence | 影響圈 |

---

## 七、自我檢查清單（**輸出前逐項確認**）

輸出前請自我確認以下每一項都 ✅：

- [ ] 輸出 PNG 尺寸 = **3200 × 4258**。
- [ ] 沒有任何英文星座名、星名、種族圈標籤、Legend 條目遺留（logo/希臘字母/格線數字/QuasiSpace 傳送門字母除外）。
- [ ] 所有中文字**清晰無缺筆**、**無簡體字**、**無錯字**。
- [ ] 種族圈曲線標籤（15 個）**沿原本弧形位置**呈現。
- [ ] Legend 32 條全數呈現、順序與原圖一致。
- [ ] 顏色分類矩陣（紅/橙/黃/綠/藍/白 × 矮星/巨星/超巨星）文字翻譯，圖示保留原樣。
- [ ] 星點、連線、圓圈邊框顏色與位置與原圖一致。
- [ ] Star Control II Logo（左下）**未被修改**。
- [ ] 希臘字母 `α β γ δ ε ζ η θ ι κ λ` 保留。
- [ ] 格線軸數字 `100..900` 保留。
- [ ] QuasiSpace 小地圖字母標記（A-N 等）保留。
- [ ] 深藍/黑色背景與星塵紋理保留。

---

## 八、回覆格式

1. **主輸出**：修改後的 PNG（3200 × 4258）。
2. **附註**：以項目列表回覆：
   - 你新增/自己決定譯名的條目清單（若對照表未列而圖中有的詞）。
   - 你認為位置或字型有疑問、可能需要人工微調的區塊。
   - 若某些中文字因渲染限制而無法完美呈現，明確標記出來供使用者再次要求局部重畫。

# 任務提詞結束

---

## 附錄 · 譯名權威來源

- `StarControl2_TW_Localization/07_Glossary/Master_Glossary.md`（v0.8）
- `StarControl2_TW_Localization/07_Glossary/Race_Names.md`
- `StarControl2_TW_Localization/07_Glossary/Place_Names.md`
- `StarControl2_TW_Localization/06_Locations/Star_Systems.md`
- 中華民國天文學會《標準天文名詞》

## 附錄 · 若 Nano Banana 輸出品質不佳的處理策略

1. **首輪輸出檢查**：把 Gemini 產出的圖與原圖並排比對，勾選「§七 自我檢查清單」。
2. **逐區重畫**：若某區（例如 §A 種族圈）有錯字或漏字，只上傳該區的局部裁圖，要求 Gemini 針對局部重畫、避免全圖重跑降低成功率。
3. **中文字錯字**：可要求 Gemini「再次確認繁體字元」並提供該詞的 Unicode 碼點（例如「撻」= U+64BB、「憂」= U+6182）。
4. **弧形排字失敗**：若曲線標籤無法弧形排列，退回為「沿弧形位置的水平/斜排短文字」，仍優於直接拉直。
5. **回退方案**：若 Nano Banana 對 3200×4258 大圖處理不穩定，可請求「以 1600×2129 半解析度輸出」並在後製使用 waifu2x/Real-ESRGAN 放大回原尺寸。
