# Patch 009 · STAR_POSTFIX_ZH_BASE 最終翻譯表 (149 條, FROZEN 2026-08-14)

**格式**: `Aurigae（御夫座）` — 英文原文 + 全形括號中譯 (per Q1=C, 使用者刻意雙軌: UI 英文首利於星圖對照, 對話仍中文首)
**Prefix**: `Alpha` / `Beta` / ... 保英文 (per Q2=A)
**引擎輸出**: `Alpha Aurigae（御夫座）` (Prefix + 空格 + 譯文)
**來源優先序**: Master_Glossary > **shipped 對話** > Place_Names > Translate_Lore > 華文天文學會標準 > 音譯
**shipped 對話 canonical 一律優先於文字規範**(避免玩家看到前後不一)

## 最終決策鎖定 (2026-08-14)

| ID | 決策 | 值 | 依據 |
|---|---|---|---|
| Q1 | 格式 | `English（中文）` | 使用者刻意雙軌設計 |
| Q2 | Prefix | 保英文 | Alpha/Beta/... 不譯 |
| Q3 | 涵蓋 | 全 132 條 | 一致性 |
| Q4 | UNKNOWN | 未知 | |
| Q5 | 15 條航點 To X.Y | 保英文 | |
| Q6 | Falayalaralfali | 法拉雅拉拉法利 | shipped v0.3 arilou canonical |
| Q7 | Save/Options | 保英文 | 對齊 1.3 星圖 |
| F1 | Luyten | **盧伊登** | shipped starbase.zh-TW.json L151 |
| F2 | Brahe | **第谷** | shipped starbase.zh-TW.json L151;需 retrofit Master_Glossary |
| F3 | 拉朗德 _notes | 保留現狀 | 不影響 shipped |
| D1 | Kepler | 克卜勒 | 台灣通用 |
| D2 | Olber | 奧伯 | SC2 無 s |
| D4 | Wolf | 沃爾夫 | 天文學家音譯 |
| D5 | Zeeman | 日曼 | 手冊 OCR canonical |
| D6 | Mira | 米拉 | 手冊 OCR L175 |
| D7 | Metis | 米蒂斯 | 木衛十六譯名 |
| D8 | Illuminati | 光明會 | 通用譯 |
| D9 | Squidi | 史奎迪 | §5.2 音譯 |
| D10 | Almagest | 阿爾馬蓋斯特 | §5.2 音譯 |
| D11 | Hyperion | 海珀利翁 | 土衛七譯名 |
| D12 | Sol | 太陽系 | shipped canonical (9 處) |
| D13 | Krueger | 克魯格 | shipped Pkunk 母星 |

---

## 圖例

- 🔒 canonical 鎖定 (Master_Glossary / Place_Names)
- 📘 華文天文學會標準 (weiwen astronomy standard)
- 👤 天文學家/歷史人物音譯 (standard scholarly)
- 🎮 遊戲原創星群 (Translate_Lore §5.2 音譯不加座字)
- ⚠️ 需你決定 (見末尾清單)

---

## STAR_STRING_BASE 索引 0-131 (constellation/star names, 132 條)

| # | English | 譯文 | 分類 | 備註 |
|---|---|---|---|---|
| 0 | Vega | 織女星 | 🔒 | Master_Glossary v0.5.2 (取代 v0.5.1「織女一」) |
| 1 | Antliae | 唧筒座 | 📘 | 華文天文標準 (Antlia = 唧筒座) |
| 2 | Apodis | 天燕座 | 📘 | Apus = 天燕座 |
| 3 | Aquarii | 寶瓶座 | 📘 | Aquarius = 寶瓶座 (非「水瓶座」) |
| 4 | Aquilae | 天鷹座 | 📘 | Aquila = 天鷹座 |
| 5 | Arae | 天壇座 | 📘 | Ara = 天壇座 |
| 6 | Arietis | 白羊座 | 📘 | Aries = 白羊座 |
| 7 | Aurigae | 御夫座 | 📘 | Auriga = 御夫座 |
| 8 | Trianguli | 三角座 | 📘 | Triangulum = 三角座 |
| 9 | Caeli | 雕具座 | 📘 | Caelum = 雕具座 |
| 10 | Camelopardalis | 鹿豹座 | 🔒 | Master_Glossary; session_workflow syreenvault → Epsilon Camelopardalis |
| 11 | Cancri | 巨蟹座 | 📘 | Cancer = 巨蟹座 |
| 12 | Brahe | 第谷 | 🔒 | F2=B: shipped starbase.zh-TW.json L151「第谷（Brahe）星系」;需 retrofit Master_Glossary + Place_Names |
| 13 | Kepler | 克卜勒 | 👤 | 標準天文學家譯名 (德國 Johannes Kepler);⚠️ 也可音譯「克普勒」 |
| 14 | Copernicus | 哥白尼 | 👤 | 標準 (波蘭 Nicolaus Copernicus);Syreen 新家園 Beta Copernicus 已 shipped |
| 15 | Capricorni | 摩羯座 | 📘 | Capricornus = 摩羯座 |
| 16 | Carinae | 船底座 | 📘 | Carina = 船底座 |
| 17 | Cassiopeiae | 仙后座 | 📘 | Cassiopeia = 仙后座 |
| 18 | Tucanae | 杜鵑座 | 🔒 | Master_Glossary Alpha Tucanae = 杜鵑座α;Zoq-Fot-Pik 母星 |
| 19 | Cephei | 仙王座 | 📘 | Cepheus = 仙王座 |
| 20 | Ceti | 鯨魚座 | 📘 | Cetus = 鯨魚座 |
| 21 | Crateris | 巨爵座 | 🔒 | Master_Glossary Delta Crateris = 巨爵座δ |
| 22 | Circini | 圓規座 | 📘 | Circinus = 圓規座 |
| 23 | Columbae | 天鴿座 | 📘 | Columba = 天鴿座 |
| 24 | Chandrasekhar | 錢德拉塞卡 | 👤 | 標準 (印度裔美籍 Subrahmanyan Chandrasekhar, 1983 Nobel);人名音譯不加座 |
| 25 | Sagittae | 天箭座 | 📘 | Sagitta = 天箭座 |
| 26 | Cygnus | 天鵝座 | 📘 | Cygnus = 天鵝座 (格式異常,其他都用 genitive Cygni; 保留 SC2 原拼) |
| 27 | Corvi | 烏鴉座 | 🔒 | Master_Glossary Beta Corvi = 烏鴉座β |
| 28 | Chamaeleonis | 蝘蜓座 | 📘 | Chamaeleon = 蝘蜓座 |
| 29 | Equulei | 小馬座 | 📘 | Equuleus = 小馬座 |
| 30 | Delphini | 海豚座 | 📘 | Delphinus = 海豚座 |
| 31 | Doradus | 劍魚座 | 📘 | Dorado = 劍魚座 |
| 32 | Monocerotis | 麒麟座 | 📘 | Monoceros = 麒麟座 |
| 33 | Crucis | 南十字座 | 📘 | Crux = 南十字座 |
| 34 | Eridani | 波江座 | 📘 | Eridanus = 波江座 (注意: Procyon 不屬此,見 Forbidden_Translations §98) |
| 35 | Fornacis | 天爐座 | 📘 | Fornax = 天爐座 |
| 36 | Geminorum | 雙子座 | 📘 | Gemini = 雙子座 |
| 37 | Altair | 牛郎星 | 📘 | α Aquilae Altair = 牛郎星 (華文常用; 亦作「河鼓二」古星宿名) |
| 38 | Antares | 心宿二 | 🔒 | v0.3 詞彙表 SC2-詞彙對照表-v0.3 line 145 |
| 39 | Horologii | 時鐘座 | 📘 | Horologium = 時鐘座 |
| 40 | Hydrae | 長蛇座 | 📘 | Hydra = 長蛇座 |
| 41 | Andromedae | 仙女座 | 📘 | Andromeda = 仙女座 |
| 42 | Groombridge | 葛倫布利吉 | 🔒 | Master_Glossary shipped |
| 43 | Lacertae | 蝎虎座 | 📘 | Lacerta = 蝎虎座 |
| 44 | Leonis | 獅子座 | 📘 | Leo = 獅子座 |
| 45 | Hyades | 畢宿星團 | 🔒 | Master_Glossary v0.5.2 (取代舊「畢宿ζ」) |
| 46 | Leporis | 天兔座 | 📘 | Lepus = 天兔座 |
| 47 | Librae | 天秤座 | 📘 | Libra = 天秤座 |
| 48 | Lipi | 里比 | 🎮 | ⚠️ 遊戲原創星群;音譯依 §5.2 不加座;Yehat 家園「Alpha Lipi」附近 |
| 49 | Lyncis | 天貓座 | 🔒 | Master_Glossary v0.5.1 Delta Lyncis = 天貓座δ (VUX Beast) |
| 50 | Fomalhaut | 北落師門 | 📘 | α Piscis Austrini Fomalhaut = 北落師門 (華文標準,獨立恆星無座字) |
| 51 | Menkar | 天囷一 | 📘 | α Ceti Menkar = 天囷一 (華文星宿) |
| 52 | Microscopii | 顯微鏡座 | 📘 | Microscopium = 顯微鏡座 |
| 53 | Draconis | 天龍座 | 🔒 | Master_Glossary shipped v0.3 |
| 54 | Orionis | 獵戶座 | 📘 | Orion = 獵戶座 (Translate_Lore §5.1 例) |
| 55 | Normae | 矩尺座 | 📘 | Norma = 矩尺座 |
| 56 | Octantis | 南極座 | 📘 | Octans = 南極座 |
| 57 | Ophiuchi | 蛇夫座 | 📘 | Ophiuchus = 蛇夫座 |
| 58 | Muscae | 蒼蠅座 | 📘 | Musca = 蒼蠅座 |
| 59 | Pavonis | 孔雀座 | 🔒 | Master_Glossary Alpha Pavonis = 孔雀座α (Yehat 母星) |
| 60 | Pegasi | 飛馬座 | 📘 | Pegasus = 飛馬座 |
| 61 | Persei | 英仙座 | 🔒 | Master_Glossary shipped v0.3 |
| 62 | Phoenicis | 鳳凰座 | 📘 | Phoenix = 鳳凰座 |
| 63 | Pictoris | 繪架座 | 📘 | Pictor = 繪架座 |
| 64 | Piscium | 雙魚座 | 📘 | Pisces = 雙魚座 |
| 65 | Hyginus | 希吉努斯 | 👤 | 羅馬天文學家 Gaius Julius Hyginus 標準音譯;不加座 |
| 66 | Puppis | 船尾座 | 📘 | Puppis = 船尾座 |
| 67 | Pyxidis | 羅盤座 | 📘 | Pyxis = 羅盤座 |
| 68 | Reticuli | 網罟座 | 📘 | Reticulum = 網罟座 |
| 69 | Arianni | 阿里安尼 | 🎮 | ⚠️ 遊戲原創 (Syreen 舊母星星域;手冊 OCR L812 有提;§5.2 音譯不加座);Syreen dossier 有註「後改譯為哥白尼β星域」但那是 retcon,gamestrings 保留原名 |
| 70 | Sagittarii | 人馬座 | 📘 | Sagittarius = 人馬座 (華文標準,非「射手座」通俗) |
| 71 | Scorpii | 天蠍座 | 📘 | Scorpius = 天蠍座 |
| 72 | Sculptoris | 玉夫座 | 📘 | Sculptor = 玉夫座 |
| 73 | Scuti | 盾牌座 | 📘 | Scutum = 盾牌座 |
| 74 | Serpentis | 巨蛇座 | 🔒 | Translate_Lore §5.1 例 |
| 75 | Sextantis | 六分儀座 | 🔒 | Master_Glossary shipped v0.3 §287 |
| 76 | Tauri | 金牛座 | 📘 | Taurus = 金牛座 (Ilwrath 母星 Alpha Tauri) |
| 77 | Telescopii | 望遠鏡座 | 📘 | Telescopium = 望遠鏡座 |
| 78 | Bootis | 牧夫座 | 📘 | Bootes = 牧夫座 (α Bootis 為 Arcturus) |
| 79 | Olber | 奧伯 | 👤 | ⚠️ 天文學家 Heinrich Olbers (1758-1840, 德);SC2 拉丁化拼作 Olber (無 s);音譯建議「奧伯」;⚠️ 標準「奧伯斯」 vs SC2 拼寫「奧伯」 |
| 80 | Centauri | 半人馬座 | 🔒 | Master_Glossary Alpha Centauri = 半人馬座α |
| 81 | Ptolemae | 托勒密 | 👤 | 希臘化 Ptolemy 標準譯「托勒密」;SC2 拉丁 Ptolemae 保譯托勒密 |
| 82 | Gorno | 戈爾諾 | 🎮 | 遊戲原創;Shofixti.md L10 shipped canonical Delta Gorno 1 = 戈爾諾δ 1 (無座字,§5.2) |
| 83 | Velorum | 船帆座 | 🔒 | Vela/Velae 已鎖船帆座;Velorum 是同 constellation genitive plural 別式 |
| 84 | Virginis | 室女座 | 📘 | Virgo = 室女座 (華文標準,非「處女座」通俗) |
| 85 | Volantis | 飛魚座 | 📘 | Volans = 飛魚座 |
| 86 | Vulpeculae | 狐狸座 | 🔒 | Master_Glossary |
| 87 | Lalande | 拉朗德 | 👤 | 法國天文學家 Joseph Jérôme Lalande;standard 音譯;Androsynth 舊母星 Alpha Lalande |
| 88 | Luyten | 盧伊登 | 🔒 | F1=C: shipped starbase.zh-TW.json L151「盧伊登（Luyten）恆星群」|
| 89 | Indi | 印第安座 | 📘 | Indus = 印第安座 |
| 90 | Lacaille | 拉卡耶 | 👤 | 法國 Nicolas Louis de Lacaille;standard 音譯 |
| 91 | Giclas | 吉克拉斯 | 🔒 | Master_Glossary shipped v0.3 ilwrath.json |
| 92 | Krueger | 克魯格 | 🔒 | Pkunk.md L10 shipped canonical Gamma Krueger 1 = 克魯格γ 1;⚠️ 注意 standard 為「克呂格」(德國 Adalbert Krüger) — 但採 shipped canonical |
| 93 | Lyrae | 天琴座 | 📘 | Lyra = 天琴座 (α Lyrae = Vega) |
| 94 | Wolf | 沃爾夫 | 👤 | ⚠️ 天文學家 Max Wolf (德);standard 音譯;⚠️ 亦可依 §5.2 rule 直接音譯「沃爾夫」 |
| 95 | Saurus | 索魯斯 | 🎮 | ⚠️ 遊戲原創 (拉丁 Saurus = 蜥蜴根詞);§5.2 音譯 |
| 96 | Raynet | 雷奈特 | 🎮 | ⚠️ 遊戲原創;§5.2 音譯;⚠️ 亦可「雷內特」 |
| 97 | Zeeman | 日曼 | 🔒 | Master_Glossary Zeeman-Vela = 日曼-微拉 (手冊 OCR);⚠️ Translate_Lore §5.2 例作「齊曼」— 建議採手冊 canonical 日曼 |
| 98 | Vela | 船帆座 | 🔒 | Master_Glossary v0.2 (亦作「微拉」when 單一恆星;此處作 postfix 用 座名) |
| 99 | Mira | 蒭藁增二 | 📘 | ⚠️ ο Ceti Mira 華文星宿「蒭藁增二」;手冊 OCR L175 稱「米拉」(SC2 語境);⚠️ 建議天文標準「蒭藁增二」 |
| 100 | Cerenkov | 契倫科夫 | 🔒 | Master_Glossary v0.5.1 Alpha Cerenkov = 契倫科夫α (VUX ZEX 流亡地) |
| 101 | Mersenne | 梅森 | 👤 | 法國 Marin Mersenne;standard 音譯 |
| 102 | Maksutov | 馬克蘇托夫 | 👤 | 蘇聯光學家 Dmitri Maksutov;standard 音譯 |
| 103 | Klystron | 克里斯壯 | 🔒 | Translate_Lore §5.2 例 |
| 104 | Metis | 米蒂斯 | 🎮 | ⚠️ 提詞 L208 列為原創;希臘神話 Metis 為智慧女神;⚠️ 標準「墨提斯」/木衛十六「米蒂斯」 |
| 105 | Mensae | 山案座 | 📘 | Mensa = 山案座 |
| 106 | Illuminati | 光明會 | 🎮 | ⚠️ 提詞 L208 列為原創;通用「光明會」;⚠️ 亦可意譯「啟明者」 |
| 107 | Vitalis | 維塔利斯 | 🎮 | ⚠️ 遊戲原創 (拉丁 Vitalis = 生命);§5.2 音譯 |
| 108 | Herculis | 武仙座 | 📘 | Hercules = 武仙座 (Safe_Ones High Council L221 mentioned) |
| 109 | Gruis | 天鶴座 | 📘 | Grus = 天鶴座 |
| 110 | Squidi | 史奎迪 | 🎮 | ⚠️ 遊戲原創 (英文 Squid = 章魚);§5.2 音譯;⚠️ 亦可意譯「章魚」 |
| 111 | Almagest | 阿爾馬蓋斯特 | 🎮 | ⚠️ 遊戲原創引托勒密《至大論》書名;§5.2 音譯;⚠️ 亦可意譯「至大論」 |
| 112 | Alcor | 開陽增一 | 📘 | 大熊座 80 Alcor = 開陽增一 (華文星宿) |
| 113 | Algol | 大陵五 | 📘 | β Persei Algol = 大陵五 (華文星宿) |
| 114 | Betelgeuse | 參宿四 | 🔒 | Master_Glossary v0.2 §4 |
| 115 | Aldebaran | 畢宿五 | 📘 | α Tauri Aldebaran = 畢宿五 (華文星宿) |
| 116 | Achernar | 水委一 | 📘 | α Eridani Achernar = 水委一 (華文星宿) |
| 117 | Procyon | 南河三 | 🔒 | Master_Glossary v0.2 §4 (Forbidden §98 明列非「波江座」) |
| 118 | Rigel | 參宿七 | 🔒 | Master_Glossary |
| 119 | Bellatrix | 參宿五 | 📘 | γ Orionis Bellatrix = 參宿五 (華文星宿) |
| 120 | Mizar | 開陽 | 📘 | ζ UMa Mizar = 開陽 (華文星宿) |
| 121 | Hyperion | 海珀利翁 | 🎮 | ⚠️ 遊戲原創引希臘神提坦 (太陽神之父);§5.2 音譯;⚠️ 標準「許珀里翁」;⚠️ 土衛七譯「海珀利翁」 |
| 122 | Regulus | 軒轅十四 | 📘 | α Leonis Regulus = 軒轅十四 (華文星宿) |
| 123 | Organon | 歐加農 | 🔒 | Master_Glossary v0.5 (Q8 mycon 2026-08-10 canonical) |
| 124 | Pollux | 北河三 | 📘 | β Geminorum Pollux = 北河三 (華文星宿) |
| 125 | Capella | 五車二 | 📘 | α Aurigae Capella = 五車二 (華文星宿) |
| 126 | Deneb | 天津四 | 🔒 | Translate_Lore §5.3 |
| 127 | Canopus | 老人星 | 📘 | α Carinae Canopus = 老人星 (華文星宿) |
| 128 | Sirius | 天狼星 | 🔒 | Master_Glossary v0.2 §4 |
| 129 | Sol | 太陽系 | 🔒 | ⚠️ Master_Glossary Sol/Sol System = 太陽系;Translate_Lore §5.3 = 太陽;⚠️ 建議「太陽系」(與 in-game 「Sol」實際指整個太陽系一致) |
| 130 | Arcturus | 大角星 | 🔒 | Master_Glossary v0.5.2 |
| 131 | Lentilis | 蘭提利斯 | 🎮 | ⚠️ 遊戲原創;§5.2 音譯 |

---

## STAR_STRING_BASE 索引 132 (special)

| # | English | 譯文 | 分類 | 備註 |
|---|---|---|---|---|
| 132 | UNKNOWN | 未知 | — | Q4=A |

---

## STAR_STRING_BASE 索引 133-147 (waypoint coords, per Q5=B 保英文)

| # | English | 譯文 |
|---|---|---|
| 133-147 | `To X.Y : A.B` | (保英文,不翻) |

## STAR_STRING_BASE 索引 148 (Falayalaralfali, per Q6)

| # | English | 譯文 | 備註 |
|---|---|---|---|
| 148 | Falayalaralfali | 法拉雅拉拉法利 | 🔒 Master_Glossary shipped v0.3 arilou.json (Arilou 母星,準空間中) |

---

# ⚠️ 需你決策的模糊項 (13 個)

以下依 Master_Glossary + Translate_Lore + 華文天文標準交叉檢視後,仍有多選項的條目。**格式 A/B/C 請回覆你的選擇**:

## D1 · Kepler (index 13)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 克卜勒 | 華文通用標準 (德國 Johannes Kepler);台灣天文教科書、行星定律皆用 |
| B | 開普勒 | 中國大陸標準;台灣少用 |

## D2 · Olber (index 79)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 奧伯 | SC2 拼寫是 Olber (無 s), 音譯到位;貼合 §5.2 遊戲用法 |
| B | 奧伯斯 | 標準天文譯 (Heinrich Olbers 有 s);較長 |

## D3 · Luyten (index 88)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 路登 | Translate_Lore §5.2 明列例 |
| B | 呂騰 | 荷蘭語標準 (Willem Luyten) |

## D4 · Wolf (index 94)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 沃爾夫 | 天文學家 Max Wolf 音譯;§5.2 rule |
| B | 沃夫 | 短音節版本 |
| C | 狼 | 意譯 (與 Wolf 359 常譯法);較不像人名 |

## D5 · Zeeman (index 97)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 日曼 | Master_Glossary Zeeman-Vela = 日曼-微拉 (手冊 OCR canonical) |
| B | 齊曼 | Translate_Lore §5.2 例 |
| C | 塞曼 | 台灣物理課本標準 (Zeeman effect = 塞曼效應) |

## D6 · Mira (index 99)

| 選項 | 譯文 | 依據 |
|---|---|---|
| A | 蒭藁增二 | 華文星宿標準 (ο Ceti Mira);較古典 |
| **B** ⭐ | 米拉 | 手冊 OCR L175 「米拉(Mira)」;SC2 語境常用;短 |

## D7 · Metis (index 104)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 米蒂斯 | 木衛十六 Metis 常用譯名;§5.2 音譯 |
| B | 墨提斯 | 希臘神話智慧女神標準譯 |
| C | 蜜蒂絲 | 較女性化音譯 |

## D8 · Illuminati (index 106)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 光明會 | 廣泛通用譯;session_workflow 舊 memory 有「Alpha 光明會」印象 |
| B | 光明幫 | 較幽默 |
| C | 啟明者 | 較文雅 |
| D | 依魯米那提 | 純音譯,不假借既有詞 |

## D9 · Squidi (index 110)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 史奎迪 | §5.2 音譯 |
| B | 章魚 | 意譯 (Squid = 章魚);較幽默 |
| C | 烏賊 | 意譯 (Squid = 烏賊) |

## D10 · Almagest (index 111)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 阿爾馬蓋斯特 | §5.2 音譯 |
| B | 至大論 | 意譯 (Ptolemy 天文著作標準譯名);較典雅但與 SC2 星群語境不符 |

## D11 · Hyperion (index 121)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 海珀利翁 | 土衛七標準譯名;§5.2 音譯 |
| B | 許珀里翁 | 希臘神話 Titan 標準譯 (太陽神 Helios 之父) |
| C | 亥伯龍 | 拜倫詩作《海珀利翁》另譯 |

## D12 · Sol (index 129)

| 選項 | 譯文 | 依據 |
|---|---|---|
| **A** ⭐ | 太陽系 | Master_Glossary Sol/Sol System = 太陽系;in-game 「Sol」實際指整個太陽系 |
| B | 太陽 | Translate_Lore §5.3 (單獨恆星 Sol → 太陽) |
| C | 索爾 | 純音譯 |

## D13 · Krueger vs Kepler 音譯風格一致性 (參考)

Krueger = 克魯格 (Pkunk shipped canonical)
- 若採德語標準 = 克呂格 (Adalbert Krüger)
- 若採 SC2 shipped canonical (Pkunk 母星) = 克魯格

**建議 A** = 克魯格 (依 shipped canonical, 不改 Pkunk 母星命名)

---

## 一致性 sanity check

依上面選擇的預設 (⭐), 產出的 postfix 完整範例:

- `Alpha Aurigae（御夫座）`
- `Beta Cassiopeiae（仙后座）`
- `Sol（太陽系）` (Prefix=0, no leading space)
- `Alpha Krueger（克魯格）`
- `Alpha Lalande（拉朗德）`
- `Delta Vulpeculae（狐狸座）`
- `Beta Copernicus（哥白尼）`
- `Alpha Zeeman（日曼）`
- `Falayalaralfali（法拉雅拉拉法利）` (Prefix=0)
- `UNKNOWN（未知）`
