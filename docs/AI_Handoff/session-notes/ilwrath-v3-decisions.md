# Ilwrath v0.7 Rebuild-Compare · Q&A 決策 (2026-08-17)

## Q1=A · 主自稱
- **我等** (default 現代雅辭)
- **我族 / 我等蛛狂** (強調族名/儀式化場合)
- **我** (單人)
- **廢除**「本族蛛狂」(v0.4 過度指令式 · dossier 未列)

## Q2=B · 儀式化尊稱點綴 = 全刪
- **不用**「多加與卡宗之血祭者」
- **不用**「蛛狂之刃」

## Q3=C · Hu-Man 混用
- 正式/中性場合 → **人族**
- 貶稱/戲弄場合 → **肉肉人類**(shipped 保留)
- 招牌辱罵句式(dossier §四)→ **軟嫩的人族/醬狀骨頭袋人族**等組合詞

## Q4=A · 貶稱 palette 全採 dossier §四
- Feeble Mammal = **微弱的哺乳動物**
- Flesh Sac = **血肉之袋**
- Flaccid Earthling = **軟趴趴的地球人**
- Squishy Hu-Man = **軟嫩的人族**
- Squishy Bone-Bag Hu-Man = **醬狀骨頭袋人族**
- Blasphemer = **瀆神者** (廢 shipped「褻瀆者」)
- 不虔敬者 = unbelievers

## Q5=A · 招牌 pun 保留 shipped canonical
- WORSHIP → WARSHIP = **崇拜 → 崇艦**
- WE → DWE = **我等 → 窩等**
- YOU → YUUBUU = **你 → 驢** (v0.7 廢汝 · 但保留「驢音近你/汝」pun)
- DILL-RATS = **蒔蘿鼠**

## Q6=A · AIEE! canonical 升級
- shipped「嘶咿——！」→ v3「**啊咿——！（AIEE!）**」

## Q7=C · 邪神 ALL CAPS 廣播 JSON icon = 特殊符號括號
- 用 **【 】** 或 **『 』** 包住 (視句長選)
- 短邪神令 → 【崇拜我等！】
- 長邪神廣播段 → 【聆聽這些話語！ 我等邪惡的子女！ 離開此處！ 尋找新的獵物！】
- 保留原文密集感嘆號節奏

## Q8=A · 儀式化中文宗教句式保留 (非文言助詞)
- **以多加與卡宗之名**
- **奉大能之令** / **奉…之令**
- **觀之——真相昭然！** (For lo, the truth is manifest!)
- **凡…者**
- 這些是**儀式化中文**，非文言助詞，不違反 v0.7

## Q9=B · Fat Jubby / Grah 保留 shipped
- Fat Jubby = **珠貝獸** (shipped 意譯保留)
- Grah = **葛拉獸** (shipped 保留 · 不升 Master_Glossary「格拉獸」)

## Q10=A · 招牌儀式名全 shipped 保留
- Festival of a Thousand Screams = **千嚎大典**
- Ceremony of Consumption = **吞食儀典**
- Chambers of Pain = **苦難廳堂**
- Excruciator = **拷刑者艦**
- Cloak of Darkness = **黑暗披風**
- Avenger = **復仇者星艦**
- Green Eye of Dogar = **多加之綠眼**
- Holy Killing Zone = **神聖屠戮區**
- Deific Duo / Arch-Deific Duo = **雙神 / 至尊雙神**
- Priestly Cabal = **神職教團**
- Acolyte = **侍徒**
- Devivication = **剝生術**
- Mountains of Flesh = **血肉山嶽**
- Zith of the Pelt = **皮毛之齊斯** / Awk of the Seds = **席德之奧克**
- Dark Ages = **黑暗時代**
- Blood gown/Fillet knife/Pain-pots/Poppers = **血袍/剔骨刀/痛楚罐/爆刺器**
- Larval paste = **幼蟲糊**

## Q11=A · 玩家 response 情境切換
- 正式提問 → **我方 / 我**
- 嗆聲挑釁 → **老子 / 你 / 你這**
- 中性對話 → **我 / 我方**
- 廢 shipped 一律「我方」

## Q12=A · 齊整化「、」分隔句大幅使用
- 對應原文 Title Case icon
- 每段對話至少 1-2 處齊整化節奏
- shipped 現有 28 處保留 + 大幅補入

## Q13=B · 儀式化動詞適度使用
- 適度用「施行/奉行/降下/聞達/供奉/獻予/引領/頌讚」
- 避免每句都硬套 · 保留原文自然節奏

## Q14=A · Channel 44 = **44 號頻道** (dossier canonical)
- 廢 shipped「第 44 頻道」

## Q15=A · 招牌辱罵直譯 (dossier §四)

## Q16=A · 3 partials × ~36 tokens

## 完成狀態 (2026-08-17)
- ✅ Partial 1 (36 tokens) · wenyan 全清
- ✅ Partial 2 (31 tokens) · wenyan 全清
- ✅ Partial 3 (42 tokens) · wenyan 全清 · 10 個【】邪神 CAPS 廣播 icon
- ✅ Merge → ilwrath.zh-TW.v3.json (29.1 KB · 109 tokens)
- ✅ 3-gate PASS (purity 0/0/0 · line-count 109/109 · Lua 6/6 CJK)
- ✅ Diff → _reaudit_ilwrath_v3_diff.md (106.3 KB · 109 entries)
  - 🟢 0 · 🟡 14 · 🟠 82 · 🔴 7 · ✨ 6
  - 🔴 全為 false positive (結構重排導致 sim 低 · 語意等價)

## 等待使用者決策 → merge → build+package

## v3.1 Read-Aloud 修訂 (2026-08-17) · ✅ 已 commit
- 使用者反饋「、」過多 + 直譯生硬 (#18/#19 為代表)
- 確認全 A (3 政策批次) → 「、」 430→29 (下降 93%)
- 94/109 tokens Read-Aloud 修訂
- **使用者「全 B」採 v3.1**
- Backup + overwrite + build+package → 37.85 MB addon (2026-08-17 15:51)
- Addon verified: 25 markers OK / 15 obsolete gone (汝/汝等/爾等/嘶咿/雄壯/第 44 頻道/本族蛛狂 全清)
- Commit: 9b7fcc2 (Ilwrath v3.1 · P1 4/7)

## Canonical 專有名詞速查
| 英文 | 中文 | 來源 |
|---|---|---|
| Ilwrath | 蛛狂族 | Master_Glossary L58 |
| Dogar | 多加 | Master_Glossary L333 |
| Kazon | 卡宗 | Master_Glossary L334 |
| Pkunk | 普恩族 | Master_Glossary L62 |
| Ur-Quan | 烏寬族 | shipped |
| Thraddash | 撻伐族 | shipped |
| Umgah | 陰嘎族 | shipped |
| Giclas | 吉克拉斯 | shipped |
| Draconis | 天龍座 | 華文天文標準 |
| Vindicator (玩家旗艦) | 復仇者號 | Master_Glossary L204 (區分 Ilwrath Avenger=復仇者星艦) |
