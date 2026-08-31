# Spathi Rebuild-Compare Diff Report · v2 vs shipped v0.4

**日期**: 2026-08-15
**方法**: [Rebuild_And_Compare.md](../StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md) 5 階段流程
**shipped 版本**: v0.4 Phase 14c+ Level 3+ (2026-08-10)
**v2 版本**: clean-room dossier-aligned (2026-08-15)

---

## Executive Summary

- Total tokens: 135
- 🟢 完全相同: **0 (0.0%)**
- ✨ Canonical 升級: 見 §B
- 🟠 措辭改變: 大量(系統性 voice 差異驅動)
- 🔴 語意差異: 少數
- 🟡 微調: 剩餘

**核心發現**:v2 clean-room 產出的譯文和 shipped 存在**系統性 voice pool 分歧**——shipped v0.4 Phase 14c+ 選用「小的/敝方」為主的 retrofit voice,但當前 [Fwiffo.md v0.5 dossier §四](../StarControl2_TW_Localization/03_Characters/Fwiffo.md) 已鎖定「平安族的我/一個/不才/卑微的我/費佛我本人」為 canonical,**dossier 完全沒列「小的」**。

這意味著 shipped 的 voice pool 是**已跟 dossier 脫節的舊 retrofit**。本次 Rebuild-Compare 提供**重新校準 dossier**的機會。

⚠️ **關鍵決策(§A · 一次拍板影響 100+ tokens)**:是否要跟 dossier 對齊?

---

## Section A · 系統性 Voice Pool 分歧(⭐ 最重要,一次拍板影響 100+ tokens)

### Voice 對照表

| 情境 | Shipped v0.4 (2026-08-10) | v2 (dossier v0.5) | Dossier 列的 canonical |
|---|---|---|---|
| Fwiffo 個人求饒/膽小 | **小的** (40+ 處) | **一個 / 卑微的我** | 「一個」「卑微的我」 ✅ v2 對齊 |
| Fwiffo 敘事身世 | 小的(仍用) | **費佛我本人 / 一個** | 「費佛我本人」 ✅ v2 對齊 |
| Fwiffo 官僚假禮貌 | **在下** (3 處) | (無明確對應) | (dossier 未列) |
| Fwiffo 個人 identity 強調 | **本史怕** | (無) | (dossier 未列) |
| Spathi 集體代言 | **敝方 / 敝族** (55+ 處) | **我族 / 我等平安族** | 「我族」「我等平安族」 ✅ v2 對齊 |
| Fwiffo 虛張聲勢/軍事 | **我方** (THOUSANDS/HATE 等) | 一個 (內斂) | (dossier 未特別列此情境) |
| 玩家 hostile response | 我方(部分)/你 | **老子 / 你這** (Style_Guide §二) | Style_Guide §二 對嗆用「老子」✅ v2 對齊 |

### 差異 root cause

shipped `_notes` 記錄:
> ===== v0.4 Phase 14c+ Level 3+ Voice 重塑修訂 (2026-08-10) =====
> M0:A2v2 Voice 分布重塑(我方 110 → ~15, 我 143 → ~110)依 EN 情境分類:
>   Fwiffo 個人極度膽小求饒:**小的**(新增,40+處)
>   Fwiffo 官僚假禮貌:**在下**(新增,3處)
>   Fwiffo 代表族群謙稱:**敝方**(新增,55+處)

這個 2026-08-10 retrofit **早於** [Fwiffo.md v0.5 dossier](../StarControl2_TW_Localization/03_Characters/Fwiffo.md) 定案(v0.5 才鎖定「一個/平安族的我/費佛我本人」)。因此 shipped 的 voice pool 是**過渡期選擇**,已被更新的 dossier 覆蓋但未 retrofit。

### Macro 決策選項

| 選 | 策略 | 影響範圍 | 建議 |
|---|---|---|---|
| **🅰️ 完全對齊 dossier(採用 v2)** | 全面用「一個/我族/費佛我本人」取代「小的/敝方/在下/本史怕」 | 100+ tokens | ⭐ **推薦**:重新校準 dossier canonical;風險是 shipped 已上線讀者可能習慣「小的」 |
| **🅱️ 保留 shipped voice(拒絕 v2)** | 維持「小的/敝方/在下」 | 僅接受 v2 的 canonical升級 + 讀順度優化 | 保守;但代表 dossier 需 retrofit 為「小的」 |
| **🆎 混合式** | shipped voice 主軸+挑選 v2 的少數 token 更新(如 Fwiffo bio ABOUT_MYSELF 用「費佛我本人」加強儲存感) | 15-30 tokens | 中間路線,需逐 token 挑 |

⚠️ 若選 🅰️,則 §B/§C 大量 diff 自動採用 v2;若選 🅱️,§B/§C 只處理少數 canonical 升級。

**我的推薦**: 🅰️ 完全對齊 dossier — 因為:
1. Dossier 是當前 canonical source of truth,shipped 的 voice pool 是 2 個月前的過渡設計
2. v2 的「一個」比 shipped 的「小的」更符合原文 Fwiffo 拐彎自貶的味道(「小的」偏中國古裝腔;「一個」有更疏離的第三人稱感,匹配 Fwiffo 心理逃避)
3. Sync dossier + shipped 減少未來繼續分歧的風險

---

## Section B · Canonical 名詞升級(v2 有,shipped 無/舊)

### B1 · v0.4 已鎖 canonical 但 shipped 用了舊譯 ✨

| 詞 | Shipped 用 | v2 用(Master_Glossary canonical) | Token 位置 |
|---|---|---|---|
| **fallow** (as adj.) | **休耕**(直譯,錯誤) | **禁足奴族** ✅ v0.4 canonical | WHEN_URQUAN_ARRIVED, UMGAH_TRICK |
| **encrustling** | **稚殼**(創譯) | **甲殼幼體** ✅ Safe_Ones canonical | SORRY_ABOUT_THAT, ABOUT_MYSELF, DREW_SHORT_STRAW |

**推薦 🅰️ ✨全 B(v2)** — 都是統一到最新 canonical。

### B2 · 首次出現英文註記(v0.5.2 Phase 14c/14d 全譯政策)

v0.5.2 政策要求特殊詞首次出現加「中譯(English)」註記。Shipped 只做了 Phase 14c 政策(Wezzy-Wezzah/AIEEEE/Snork/Hunam/Hootmans/Huge-glands/Homosap 有註記),但**其他新詞未加**。v2 補齊。

| 詞 | Shipped | v2 |
|---|---|---|
| StarRunner | 星奔號(無英文) | 星奔號(StarRunner) |
| Spathiwa (首次於 SORRY_ABOUT_THAT) | 史怕瓦(無英文) | 史怕瓦(Spathiwa) |
| Yuffo (首次於 COORDINATES_ARE) | 尤佛(無英文) | 尤佛(Yuffo) |
| Ganymede | 木衛三(無英文) | 木衛三(Ganymede) |
| Titan | 土衛六(無英文) | 土衛六(Titan) |
| Pluto (首次於 what_doing_on_pluto_1) | 冥王星(無英文) | 冥王星(Pluto) |
| Winky's Happy Night | 眨眼快樂夜(無英文) | 眨眼小子的歡樂夜(Winky's Happy Night) |
| FunRom | **FunRom**(裸英文) | 樂趣光碟(FunRom) |
| Grand Master Planet Eaters | 大宗噬星者(無英文) | 星球吞噬大宗師(Grand Master Planet Eaters) |
| Killmaster 18 | 殺手大師 18 號(無英文) | 殺戮大師 18 號(Killmaster 18) |
| Tuffa-Yuf | 塔法-尤夫(無英文) | 塔法-優夫(Tuffa-Yuf) |
| Pwappy | 帕皮(無英文) | 帕比(Pwappy) |
| Mister Nasty | 惡劣先生(無英文) | 兇巴巴先生(Mister Nasty) |
| Yipes! | 呀!(無英文) | 我的媽呀!(Yipes!) |
| Aghk! | 呃啊!(無英文) | 呃啊!(Aghk!) |

**特殊 case: FunRom** — Shipped 保留裸英文 `音頻 FunRom`,違反 v0.5.2 Phase 14c 全譯政策。v2 中譯為「樂趣光碟(FunRom)」符合政策。

**推薦 🅰️ ✨全 B(v2)** — 全面對齊 Phase 14c/14d 全譯政策。

### B3 · Q&A 決策項(Q1-Q13 已使用者確認)

| Q | 名詞 | Shipped | v2(使用者 Q&A 確認) |
|---|---|---|---|
| Q1 | StarRunner | **星奔號** ✅ | 星奔號 ✅ **相同** |
| Q2 | Puun-Taffy | 抽命籤(Puun-Taffy) | **普恩塔菲(Puun-Taffy)** ⚠️ 不同 |
| Q2 | Ta Puun stick | 抽命籤(Ta Puun) | **塔普恩短籤(Ta Puun stick)** ⚠️ 不同 |
| Q3a | Grand Master Planet Eaters | 大宗噬星者 | **星球吞噬大宗師** ⚠️ 不同(v2 加「師」) |
| Q3b | Killmaster 18 | 殺手大師 18 號 | **殺戮大師 18 號** ⚠️ 不同(v2「殺戮」代「殺手」) |
| Q4 | Winky's Happy Night | 眨眼快樂夜 | **眨眼小子的歡樂夜** ⚠️ 不同(v2 加「小子」) |
| Q5 | FunRom | (裸英文 FunRom) | **樂趣光碟(FunRom)** ⚠️ v2 中譯 |
| Q6 | Tuffa-Yuf | 塔法-尤夫 | **塔法-優夫** ⚠️ 不同(v2「優」代「尤」——避免與 Yuffo=尤佛同字) |
| Q7a | Snork-snork-snork! | 嗤——嗤——嗤!(Snork-snork-snork!) | **呼嚕呼嚕呼嚕!(Snork-snork-snork!)** ⚠️ 不同 |
| Q7b | Yipes! | 呀! | **我的媽呀!(Yipes!)** ⚠️ 不同 |
| Q7c | Aghk! | 呃啊! | **呃啊!(Aghk!)** ✅ **相同(僅補英文)** |
| Q8 | Mister Nasty | 惡劣先生 | **兇巴巴先生(Mister Nasty)** ⚠️ 不同 |
| Q9 | Hootmans | 猴人族 | **吼漢** ⚠️ 不同(諧音鏈) |
| Q9 | Huge-glands | 大鼻族 | **糊腺** ⚠️ 不同(諧音鏈) |
| Q9 | Hunams | 認類(Hunams) | 認類(Hunams) ✅ **相同**(canonical) |
| Q10 | AIEEEE! | 嗚咿——! | **呀依依依依──!** ⚠️ 不同(對齊 Aiee=呀依 canonical) |
| Q11 | Pwappy | 帕皮 | **帕比(Pwappy)** ⚠️ 不同(比 vs 皮) |
| Q12a | Ganymede | 木衛三(無英文) | **木衛三(Ganymede)** ⚠️ v2 補英文 |
| Q12a | Titan | 土衛六(無英文) | **土衛六(Titan)** ⚠️ v2 補英文 |
| Q12b | Circini | 圓規座和錢德拉塞卡 | **圓規座與錢德拉塞卡** ⚠️ 「和」→「與」 |
| Q13 | Fwiffo 自稱系 | 小的/敝方/我方混用 | **一個/我族/費佛我本人** (dossier v0.5) |

**推薦**: Q&A 決策已使用者確認 → 全採 v2 canonical(即 ✨全 B)。

### B4 · Homosap 補譯

| 詞 | Shipped | v2 |
|---|---|---|
| Homosap | **智猿人(Homosap)** | **智人(Homosap)** |

⚠️ 「智人」是生物學正式名(Homo sapiens 中文標準譯),shipped 的「智猿人」是創譯。EN 「Homosap」是 Fwiffo 用學術術語充胖子,「智人」較符合此定位。

**推薦 A(shipped「智猿人」)還是 B(v2「智人」)?** 這是可以討論的細節。Shipped 的「智猿人」帶有「假裝很懂生物但誤植」的 gag 感,反而更 Fwiffo。**若你偏好「智猿人」保留 gag ,選 A;若你偏好「智人」對齊生物學,選 B。**

---

## Section C · 精選 Featured Token Diffs(15 個關鍵 token)

以下 15 個 tokens 差異最大,值得逐項比較。

### C1 · SORRY_ABOUT_THAT · 🟠 措辭改變

**Shipped**:
```
注意，體積龐大、又兇又狠、明顯擺出攻擊姿態盤旋頭頂的外星艦:
請、請千萬別誤會── 小的乃艦長費佛。
小的知道您要拷問小的,敝方就趕快把這件事了結吧。
小的母星史怕瓦的座標是 <% ... %>…
```

**v2**:
```
致明顯呈攻擊姿態、盤旋於上方的巨大、兇惡、敵意外星艦艇:
這位是史怕族艦長費佛。
一個知道您必將拷打卑微的我,那就別廢話、我們現在就把這事了結吧。
一個母星史怕瓦(Spathiwa)的座標是 <% ... %>…
```

**差異分析**:
- Voice: 小的 → 一個/卑微的我(§A macro)
- 開場:shipped「請、請千萬別誤會」是額外添加(EN 無此句);v2「這位是史怕族艦長費佛」更貼 EN「This is Spathi Captain Fwiffo」
- 「乃艦長費佛」偏文言;v2「這位是」更口語
- 首介:v2 補「史怕瓦(Spathiwa)」英文註記

**推薦**: 🅰️ B(v2) — voice + 更貼 EN + 英文註記全上

### C2 · WEZZY_WEZZAH · 🟡 微調

**Shipped**:
```
當然,最為仁慈的毀滅者,眾所周知,在離開這凡塵螺旋之前
所有史怕族都必須完成短暫而深刻的 辭世禱(Wezzy-Wezzah) 儀式 才能確保安全的來世
讓敝方履行這項要求 您也將在敝方美麗的來世獲得永生
那來世絕對保證沒有同樣長生的怪物 否則會把小的倆都吃了。
```

**v2**:
```
當然、當然,最仁慈的毀滅者,眾所周知,在離開這凡俗生死之螺旋之前,
所有史怕族都必須完成那簡短卻感人肺腑的辭世禱(Wezzy-Wezzah)儀式,以確保能安穩前往來世,
而如果您允許我族完成此項要求,您也將在我族美麗的來世獲賜永生 ——
該來世絕對保證沒有同樣長生不死的怪獸,前來吞食我們兩個。
```

**差異分析**:
- Shipped「凡塵螺旋」vs v2「凡俗生死之螺旋」(Safe_Ones dossier canonical 是 mortal helix=凡俗生死之螺旋)
- Voice: 敝方 → 我族(§A macro)
- 韻律:v2 用破折號 —— 增強節奏(shipped 用空格分隔)

**推薦**: 🅰️ B(v2) — dossier canonical 對齊

### C3 · ABOUT_MYSELF (Fwiffo 身世) · 🟠 措辭改變

Shipped 用「小的」大約 25+ 次,「女性親長」「男性親長」偏正式;v2 用「一個/費佛我本人」混合 + 更自然稱謂「父親/母親」。

Shipped 節錄:「小的男性親長必須辛勤工作養家...女性親長對小的們所有人都溫柔慈愛」
v2 節錄:「一個的父親得非常辛勤地工作養家...一個的母親對我們每一個都溫柔慈愛」

**差異分析**:
- v2 用「父親/母親」更順口(EN「male parent / female parent」是笨拙術語,兩版都可以;但 shipped 直譯「男性親長」帶點僵硬感)
- Voice: 小的 → 一個(§A macro)

⚠️ **保留 shipped 的「男性親長/女性親長」也有其理**:EN 用「male parent / female parent」而非「father / mother」,可能是 Fwiffo 這種學術式表達的膽小逃避感。**若你想保留這個 flavor,選 shipped 版**;若你想順化,選 v2 版。

**推薦**: 🅰️ 🟠 B(v2) — 順化,但可保留部分 shipped 語法(如「男性親長」)

### C4 · WHEN_URQUAN_ARRIVED · ✨ Canonical

**Shipped**:「或者成為『**休耕**』種族」
**v2**:「或成為「**禁足奴族**」」

**差異**: shipped 用「休耕」是農業直譯(fallow field=休耕地),但 Master_Glossary v0.4 canonical **Fallow Slave = 禁足奴族**。shipped 未升級。

**推薦**: 🅰️ ✨ B(v2) — canonical 升級

### C5 · UMGAH_TRICK · ✨ Canonical(fallow 同上)

**Shipped**:「代表『**休耕奴役**』」
**v2**:「示意「**禁足奴族**」」

同 C4,canonical 升級。**推薦 🅰️ ✨ B(v2)**

### C6 · DREW_SHORT_STRAW · 🟠 措辭 + Canonical

**Shipped**:「儀式 抽命籤(Puun-Taffy)」... 「抽到最短的那根 抽命籤(Ta Puun) 棒」
**v2**:「儀式 —— 普恩塔菲(Puun-Taffy)」... 「抽到塔普恩短籤(Ta Puun stick)裡最短的那一根」

**差異**:
- Q2 使用者已確認:普恩塔菲 / 塔普恩短籤
- shipped 兩個名字都翻「抽命籤」(意譯統一);v2 兩個名字用不同音譯(區分兩者)

**推薦**: 🅰️ B(v2) — 依 Q2 使用者確認

### C7 · SET_UP_BASE · ✨ Canonical(FunRom 全譯)

**Shipped**:「一片梅諾商出品的音頻 **FunRom** 叫做『眨眼快樂夜』」
**v2**:「一份梅諾商賣的音訊**樂趣光碟(FunRom)**,那份光碟叫做「**眨眼小子的歡樂夜(Winky's Happy Night)**」」

**差異**:
- FunRom: shipped 裸英文(違反 Phase 14c);v2 中譯 + 首介英文
- Winky's Happy Night: shipped 無英文註記;v2 補英文
- 「眨眼快樂夜」vs「眨眼小子的歡樂夜」

**推薦**: 🅰️ ✨ B(v2) — 對齊 Phase 14c 全譯政策

### C8 · GENERAL_INFO_SPACE_1 (Umgah 廣播 3 人) · 🟠 措辭

**Shipped**:
```
大宗噬星者
無法名狀的賈德·魔怪
以及殺手大師 18 號。
```

**v2**:
```
星球吞噬大宗師(Grand Master Planet Eaters)、
無法名狀的賈德·魔怪(Jud the Ineffable Vug)、
以及殺戮大師 18 號(Killmaster 18)。
```

**差異**:
- Q3a: 大宗噬星者(shipped)vs 星球吞噬大宗師(v2) — Q3a 已使用者選 A(v2)
- Q3b: 殺手大師 18 號(shipped)vs 殺戮大師 18 號(v2) — Q3b 已使用者選 A(v2)
- v2 補英文首介

**推薦**: 🅰️ B(v2) — 依 Q3 使用者確認

### C9 · INIT_NEUTRAL_HELLO_SPACE (Hootmans/Huge-glands/Hunams gag) · 🔴 Voice 差異

**Shipped**:
```
我被我方舊敵人 **猴人族(Hootmans)** 平滑而敵對的臉所歡迎
不對… **大鼻族(Huge-glands)**,不對,我想起來了,**認類們(Hunams)**!
```

**v2**:
```
一個被我族的老敵人 —— **吼漢(Hootmans)** —— 那光滑而敵意的臉迎接
不對……是**糊腺(Huge-glands)**,不對,一個想起來了,是**認類(Hunams)**!
```

**差異(策略性)**:
- **Shipped 策略**:意譯(Hootmans=猴人族/Huge-glands=大鼻族)——保留視覺形象笑點
- **v2 策略**:諧音(Hootmans=吼漢/Huge-glands=糊腺)——形成 rèn lèi 音鏈(吼漢→糊腺→認類)漸近正確發音

**兩者互斥**——V2 諧音鏈的優點是**中文讀者感受到 Fwiffo 是在「試著念出人類發音」而失敗**,更貼原文誤讀 gag;缺點是「吼漢」「糊腺」對中文讀者的字面理解較模糊。Shipped 意譯的優點是**中文讀者秒懂**「猴人族」是描述人類外表,「大鼻族」是描述人類特徵;缺點是丟失了 Fwiffo「嘗試發音失敗」的原意。

⚠️ **這是 🔴 語意差異——需你抉擇**:

- **A(shipped)**: 猴人族/大鼻族/認類們 — 意譯,秒懂
- **B(v2)**: 吼漢/糊腺/認類 — 諧音,對齊 EN 誤讀 gag
- **C**: 混合(如 Hootmans 用「吼漢」諧音,Huge-glands 用「大鼻族」意譯)

我的推薦: **B(v2)** — 因為 EN gag 的核心就是「Fwiffo 記不住 Human 這個字怎麼念」,諧音鏈更貼原意。但你已在 Q9 選了 B(v2),故此點沿用 Q9 決策。

### C10 · SUBSEQUENT_ALLIED_HELLO_SPACE (Tuffa-Yuf) · 🟡 微調

**Shipped**:「塔法-**尤夫**」
**v2**:「塔法-**優夫**(Tuffa-Yuf)」

**差異**: Q6 已使用者選 A(v2)。「優」代「尤」是為了避免與 Yuffo=尤佛同字混淆。**推薦 🅰️ B(v2)**

### C11 · ALWAYS_PREPARED (AIEEEE!) · 🟠 措辭

**Shipped**:「**嗚咿——!(AIEEEE!)** 不! 請仁慈!」
**v2**:「**呀依依依依──!(AIEEEE!)** 不!請發發慈悲!」

**差異**:
- Q10 已使用者選 A(v2 呀依依依依)
- 對齊 Fwiffo.md canonical: Aiee=呀依,長版加「依依依」
- Shipped「嗚咿」是另一種擬聲策略

**推薦**: 🅰️ B(v2) — 依 Q10 + dossier canonical

### C12 · BLAZE_IS (Snork-snork-snork!) · 🟠 措辭

**Shipped**:「**(嗤——嗤——嗤!(Snork-snork-snork!))**」
**v2**:「**(呼嚕呼嚕呼嚕(Snork-snork-snork)!)**」

**差異**:
- Q7a 已使用者選 A(v2 呼嚕呼嚕呼嚕)
- Shipped「嗤——嗤——嗤」是不屑冷笑感;v2「呼嚕呼嚕呼嚕」是得意鼻嗤感
- 上下文:Fwiffo 講 Shofixti 自爆殺 Ur-Quan,是**幸災樂禍**——v2「呼嚕」更幸災樂禍(shipped「嗤嗤嗤」偏冷嘲)

**推薦**: 🅰️ B(v2) — 依 Q7a

### C13 · YIPES · 🟠 措辭

**Shipped**:「**呀!**」(短促,無英文)
**v2**:「**我的媽呀!(Yipes!)**」(台式感嘆詞 + 英文)

**差異**: Q7b 已使用者選 A(v2)。Humor_Rule §5.3 允許 Fwiffo 輕度台式口語(荒謬感)。

**推薦**: 🅰️ B(v2) — 依 Q7b

### C14 · SUBSEQUENT_ANGRY_HELLO_SPACE (Mister Nasty) · 🟠 措辭

**Shipped**:「啊,**惡劣先生**回來了」
**v2**:「啊,**兇巴巴先生(Mister Nasty)**又來了」

**差異**: Q8 已使用者選 A(v2)。「兇巴巴」台式輕度挖苦,更貼 Fwiffo 荒謬 flavor。

**推薦**: 🅰️ B(v2) — 依 Q8

### C15 · GENERAL_INFO_SPACE_2 (Circini and Chandrasekhar) · 🟡 微調

**Shipped**:「圓規座**和**錢德拉塞卡 (Circini and Chandrasekhar)」
**v2**:「圓規座**與**錢德拉塞卡」

**差異**: 「和」→「與」;shipped 有補「(Circini and Chandrasekhar)」在 constellation 尾,v2 無(因為已在 Lua first-arg 內)。

**推薦**: 🅰️ B(v2) — 更古典

---

## Section D · 應用建議

### D1 · Macro 策略

⭐ **主推薦: 🅰️ 完全對齊 dossier(採用 v2 全部)**

理由:
1. **Dossier 是 canonical source of truth** — Fwiffo.md v0.5 是最新,shipped 的「小的」voice pool 是 2 個月前 retrofit 未跟上
2. **v2 已通過 3-gate** — purity/line-count/Lua template 全 PASS
3. **v2 補齊了多個 canonical 升級** — 禁足奴族(vs 舊「休耕」)/ 甲殼幼體(vs 舊「稚殼」)/ FunRom 中譯 / 首介英文全套
4. **Q&A 決策已使用者確認** — Q1-Q13 全套已定,直接採用即可

### D2 · 保留 shipped 的哪些?

即使選 🅰️,我建議**保留 shipped 的幾個微調**:

| 項目 | 決定 | 理由 |
|---|---|---|
| Homosap → 智猿人(shipped) or 智人(v2)? | **⚠️ 你選** | Shipped「智猿人」帶假裝懂生物的 gag;v2「智人」對齊生物學。二選一都可 |
| ABOUT_MYSELF「男性親長/女性親長」 | **⚠️ 你選** | Shipped 保留 EN「male parent」笨拙感;v2 順化為「父親/母親」。二選一都可 |

### D3 · 若採 🅰️,實際步驟

1. Backup shipped: `Copy-Item translations\spathi.zh-TW.json translations\spathi.zh-TW.pre-rebuild.bak`
2. 覆蓋 shipped: `Copy-Item translations\spathi.zh-TW.v2.json translations\spathi.zh-TW.json -Force`
3. 更新 `_notes` 加入 v0.6 Rebuild-Compare 記錄
4. 3-gate 再驗一次(purity/line-count/Lua)
5. `.\build_zh-TW.ps1` + `.\package_zh-TW.ps1`
6. 交遊戲內驗證(冥王星登陸→ Fwiffo → 招募 → 太空聯盟)

### D4 · 若採 🅱️(不改)

- 廢棄 `spathi.zh-TW.v2.json`(或保留為 alternate reference)
- 不動 shipped
- 但**強烈建議**至少採用以下 4 個 ✨ canonical 升級:
  - WHEN_URQUAN_ARRIVED / UMGAH_TRICK: 休耕 → 禁足奴族
  - SORRY_ABOUT_THAT / ABOUT_MYSELF / DREW_SHORT_STRAW: 稚殼 → 甲殼幼體
  - SET_UP_BASE: 「音頻 FunRom」→「樂趣光碟(FunRom)」
  - 各 token 首次名詞附英文註記(Yuffo/Spathiwa/Ganymede/Titan/StarRunner/Pwappy/Tuffa-Yuf)

---

## 使用者決策回覆格式

```
Macro: A / B / AB(混合)
Homosap: 智猿人 / 智人
ABOUT_MYSELF「男性親長」: 保留 / 順化為「父親」
```

**或批次快答**:
```
全 A (dossier 對齊) · Homosap 智人 · ABOUT_MYSELF 順化
```

---

**⏸️ 等你回覆後進入 Phase 4:merge → 3-gate → 覆蓋 shipped → build + package。**
