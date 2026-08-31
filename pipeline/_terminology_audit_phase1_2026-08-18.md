# Phase 1 · 規範檔內部一致性稽核（2026-08-18）

> 自動化抽取 · 由 `_terminology_audit_extract.py` 產出。
> **shipped-preference 策略**：實際決策應對照 shipped JSON。此報告僅識別「規範檔內部」衝突。

## 統計

- 掃描檔案：`StarControl2_TW_Localization/**/*.{md,csv}` （跳過 Reference_Material · 跳過 Template · 跳過歷史/禁止區段）
- 抽取獨立 canonical 詞：**893** 條
- 表格總列數（含跨檔重複）：**1526** 列
- 內部衝突項：**110**
  - 🔴 高嚴重度（≥3 種譯法並存）：**33**
  - 🟠 中嚴重度（2 種譯法並存）：**77**

---

## 🔴 高嚴重度衝突（33 項）

### #1 · `AIEE!`

- **啊** (1 處)：`02_Races/Zoq_Fot_Pik.md:143`
- **啊咿——！** (1 處)：`02_Races/Ilwrath.md:126`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:38`

### #2 · `Aieee!`

- **Aieee!** (1 處)：`07_Glossary/Fixed_Terms.csv:200`
- **哎唷唷** (1 處)：`02_Races/Druuge.md:186`
- **啊咦！** (1 處)：`03_Characters/Talking_Pet.md:114`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:37`
- **恐懼／驚呼** (1 處)：`07_Glossary/Master_Glossary.md:419`

### #3 · `Alpha Tucanae`

- **杜鵑座** (1 處)：`06_Locations/Star_Systems.md:38`
- **杜鵑座 α** (3 處)：`07_Glossary/Fixed_Terms.csv:172`、`07_Glossary/Master_Glossary.md:272`、`07_Glossary/Place_Names.md:34`
- **阿爾法·杜鵑座** (1 處)：`02_Races/Zoq_Fot_Pik.md:160`

### #4 · `Androsynth`

- **中已滅絕** (2 處)：`00_Project_Control/Dossier_Revision_Progress.md:92`、`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:82`
- **安卓辛族** (2 處)：`07_Glossary/Fixed_Terms.csv:22`、`07_Glossary/Master_Glossary.md:59`
- **無** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:159`

### #5 · `Banzai!`

- **Banzai!** (1 處)：`07_Glossary/Fixed_Terms.csv:209`
- **日式榮譽呼喊** (1 處)：`07_Glossary/Master_Glossary.md:428`
- **萬歲** (2 處)：`02_Races/Shofixti.md:136`、`08_Translation_Rules/Alien_Speech_Rule.md:31`

### #6 · `Chenjesu`

- **全小寫** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:105`
- **全小寫詩意冥想** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:92`
- **合併** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:161`
- **晶智族** (2 處)：`07_Glossary/Fixed_Terms.csv:7`、`07_Glossary/Master_Glossary.md:47`

### #7 · `Chmmr`

- **全大寫神諭體** (2 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:108`、`08_Translation_Rules/Alien_Speech_Rule.md:91`
- **查姆族** (2 處)：`07_Glossary/Fixed_Terms.csv:9`、`07_Glossary/Master_Glossary.md:49`
- **融合前** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:136`

### #8 · `Dnyarri`

- **假** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:135`
- **蟾亞** (2 處)：`02_Races/Ur_Quan_Kzer_Za.md:127`、`03_Characters/Talking_Pet.md:95`
- **蟾亞族** (3 處)：`03_Characters/Talking_Pet.md:304`、`07_Glossary/Fixed_Terms.csv:33`、`07_Glossary/Master_Glossary.md:70`

### #9 · `Excruciator`

- **極痛裝置** (6 處)：`02_Races/Ur_Quan.md:82`、`02_Races/Ur_Quan_Kzer_Za.md:122`、`03_Characters/Talking_Pet.md:106`、`03_Characters/Talking_Pet.md:312`、`07_Glossary/Tech_Names.md:21`、`07_Glossary/Tech_Names.md:151`
- **苦刑器** (1 處)：`07_Glossary/Master_Glossary.md:92`
- **見上** (1 處)：`07_Glossary/Master_Glossary.md:232`

### #10 · `Frungy`

- **Frungy** (1 處)：`07_Glossary/Fixed_Terms.csv:160`
- **佐-佛-皮的無厉頭運動** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:142`
- **保留原文** (1 處)：`09_AI_Prompt/Terminology_Audit.md:136`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:46`
- **苙戎奇** (1 處)：`07_Glossary/Master_Glossary.md:346`

### #11 · `Ha!`

- **Ha!** (1 處)：`07_Glossary/Fixed_Terms.csv:204`
- **哈** (2 處)：`02_Races/Shofixti.md:135`、`08_Translation_Rules/Alien_Speech_Rule.md:30`
- **哈！** (1 處)：`03_Characters/Talking_Pet.md:125`
- **武士刀式挑釁** (1 處)：`07_Glossary/Master_Glossary.md:423`

### #12 · `hee-hee-hee`

- **hee-hee-hee** (1 處)：`07_Glossary/Fixed_Terms.csv:206`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:40`
- **陰險笑聲** (1 處)：`07_Glossary/Master_Glossary.md:425`

### #13 · `Hellbore Cannon`

- **地獄砲** (1 處)：`07_Glossary/Fixed_Terms.csv:140`
- **火獄穿甲炮** (1 處)：`07_Glossary/Master_Glossary.md:366`
- **火獄穿甲砲** (2 處)：`05_Technology/Ship_Modules.md:46`、`07_Glossary/Tech_Names.md:97`

### #14 · `Ho-ho-ho`

- **Ho-ho-ho** (1 處)：`07_Glossary/Fixed_Terms.csv:207`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:41`
- **通用捧腹笑聲** (1 處)：`07_Glossary/Master_Glossary.md:426`

### #15 · `Hyai!`

- **Hyai!** (1 處)：`07_Glossary/Fixed_Terms.csv:202`
- **哎呀** (1 處)：`02_Races/Shofixti.md:131`
- **唉呀** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:28`
- **田中式輕聲驚呼** (1 處)：`07_Glossary/Master_Glossary.md:421`

### #16 · `HYAIEEE!`

- **HYAIEEE!** (1 處)：`07_Glossary/Fixed_Terms.csv:203`
- **嗚呀啊** (2 處)：`02_Races/Shofixti.md:132`、`08_Translation_Rules/Alien_Speech_Rule.md:29`
- **田中式極端咆哮** (1 處)：`07_Glossary/Master_Glossary.md:422`

### #17 · `Ilwrath`

- **每個實詞首字大寫** (2 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:106`、`08_Translation_Rules/Alien_Speech_Rule.md:93`
- **禱詞感** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:56`
- **蛛狂族** (2 處)：`07_Glossary/Fixed_Terms.csv:21`、`07_Glossary/Master_Glossary.md:58`

### #18 · `Juffo-Wup`

- **Juffo-Wup** (1 處)：`07_Glossary/Fixed_Terms.csv:159`
- **不譯** (1 處)：`02_Races/Mycon.md:125`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:45`
- **聖源** (1 處)：`07_Glossary/Master_Glossary.md:345`
- **麥孔宗教核心用語** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:141`

### #19 · `Keel-Verezy`

- **奇維瑞族** (1 處)：`07_Glossary/Master_Glossary.md:385`
- **奇維瑞族/商行** (1 處)：`07_Glossary/Fixed_Terms.csv:156`
- **奇維瑞族／商行** (1 處)：`07_Glossary/Master_Glossary.md:335`

### #20 · `Kohr-Ah`

- **柯亞** (1 處)：`02_Races/Ur_Quan_Kzer_Za.md:126`
- **柯亞族** (2 處)：`07_Glossary/Fixed_Terms.csv:6`、`09_AI_Prompt/Terminology_Audit.md:135`
- **極短句** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:112`

### #21 · `Kyaiee!`

- **Kyaiee!** (1 處)：`07_Glossary/Fixed_Terms.csv:201`
- **殺呀** (2 處)：`02_Races/Shofixti.md:130`、`08_Translation_Rules/Alien_Speech_Rule.md:27`
- **田中式熱血咆哮** (1 處)：`07_Glossary/Master_Glossary.md:420`

### #22 · `Lykeee-lieee!`

- **Lykeee-lieee!** (1 處)：`07_Glossary/Fixed_Terms.csv:205`
- **保留原文** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:525`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:39`
- **蘇格蘭騎士呼喚** (1 處)：`07_Glossary/Master_Glossary.md:424`

### #23 · `Mmrnmhrm`

- **合併** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:167`
- **姆姆族** (2 處)：`07_Glossary/Fixed_Terms.csv:8`、`07_Glossary/Master_Glossary.md:48`
- **無單獨** (2 處)：`00_Project_Control/Dossier_Revision_Progress.md:93`、`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:83`

### #24 · `Nemesis`

- **宿敵號** (2 處)：`07_Glossary/Master_Glossary.md:189`、`07_Glossary/Ship_Names.md:48`
- **復仇者** (1 處)：`04_Ships/Neutral_Ships.md:165`
- **復仇者號** (1 處)：`07_Glossary/Fixed_Terms.csv:77`

### #25 · `Precursors`

- **先驅** (1 處)：`02_Races/Zoq_Fot_Pik.md:165`
- **先驅族** (1 處)：`02_Races/Druuge.md:198`
- **先驅者** (1 處)：`07_Glossary/Fixed_Terms.csv:37`

### #26 · `Sa-Matra`

- **保留原文** (1 處)：`02_Races/Thraddash.md:204`
- **薩瑪特拉** (7 處)：`01_World_Lore/Technology_Level.md:73`、`03_Characters/Talking_Pet.md:103`、`05_Technology/Precursor_Artifact.md:90`、`07_Glossary/Fixed_Terms.csv:122`、`07_Glossary/Master_Glossary.md:207`、`07_Glossary/Master_Glossary.md:230`、`07_Glossary/Tech_Names.md:12`
- **薩馬特拉** (3 處)：`02_Races/Chmmr.md:113`、`02_Races/Ur_Quan_Kohr_Ah.md:124`、`02_Races/Ur_Quan_Kzer_Za.md:120`

### #27 · `SNORT!`

- **SNORT!** (1 處)：`07_Glossary/Fixed_Terms.csv:208`
- **保留原文** (1 處)：`02_Races/Thraddash.md:168`
- **哼嗤鼻聲** (1 處)：`07_Glossary/Master_Glossary.md:427`
- **哼！** (1 處)：`07_Glossary/Master_Glossary.md:332`
- **待譯** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:42`

### #28 · `Syra`

- **保留原文 · 已毀滅的家園** (1 處)：`02_Races/Syreen.md:228`
- **席拉** (3 處)：`07_Glossary/Fixed_Terms.csv:188`、`07_Glossary/Master_Glossary.md:287`、`07_Glossary/Place_Names.md:64`
- **席拉星** (1 處)：`03_Characters/Talana.md:71`

### #29 · `Talking Pet`

- **會話寵** (5 處)：`02_Races/Arilou.md:145`、`02_Races/Umgah.md:141`、`03_Characters/Talking_Pet.md:94`、`07_Glossary/Fixed_Terms.csv:34`、`07_Glossary/Master_Glossary.md:71`
- **會話寵 / 蟾亞** (1 處)：`07_Glossary/Master_Glossary.md:85`
- **會話寵 / 蟾亞 dual-identity** (1 處)：`03_Characters/Talking_Pet.md:303`

### #30 · `Umgah`

- **一般粗俗黑色荒謬** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:137`
- **粗俗黑色荒謬** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:57`
- **陰嘎族** (2 處)：`07_Glossary/Fixed_Terms.csv:18`、`07_Glossary/Master_Glossary.md:55`

### #31 · `Utwig`

- **已完成修訂** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:76`
- **憂特族** (2 處)：`07_Glossary/Fixed_Terms.csv:23`、`07_Glossary/Master_Glossary.md:60`
- **損壞** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:134`

### #32 · `vapor city`

- **化為蒸氣** (1 處)：`09_AI_Prompt/Translate_Dialogue.md:543`
- **化為蒸氣的城市** (1 處)：`08_Translation_Rules/Style_Guide.md:165`
- **灰飛煙滅** (2 處)：`07_Glossary/Fixed_Terms.csv:211`、`07_Glossary/Master_Glossary.md:481`

### #33 · `VUX`

- **VUX** (1 處)：`07_Glossary/Fixed_Terms.csv:20`
- **三字母大寫** (1 處)：`08_Translation_Rules/Naming_Rule.md:175`
- **保留原文** (1 處)：`07_Glossary/Master_Glossary.md:57`

---

## 🟠 中嚴重度衝突（77 項）

### #1 · `Alpha Centauri`

- **半人馬座** (2 處)：`06_Locations/Star_Systems.md:40`、`09_AI_Prompt/Translate_Lore.md:151`
- **半人馬座 α** (2 處)：`07_Glossary/Fixed_Terms.csv:170`、`07_Glossary/Place_Names.md:32`

### #2 · `Alpha Pavonis`

- **孔雀座** (1 處)：`06_Locations/Star_Systems.md:39`
- **孔雀座 α** (3 處)：`07_Glossary/Fixed_Terms.csv:173`、`07_Glossary/Master_Glossary.md:273`、`07_Glossary/Place_Names.md:35`

### #3 · `Aqua Helix`

- **水靈螺旋** (1 處)：`02_Races/Thraddash.md:183`
- **蔚藍螺旋** (2 處)：`07_Glossary/Master_Glossary.md:228`、`07_Glossary/Tech_Names.md:15`

### #4 · `Arilou`

- **半正式** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:60`
- **阿麗露** (2 處)：`07_Glossary/Fixed_Terms.csv:13`、`07_Glossary/Master_Glossary.md:52`

### #5 · `Arilou Lalee'lay`

- **阿麗露·萊蕾** (1 處)：`07_Glossary/Fixed_Terms.csv:14`
- **阿麗露拉利雷** (1 處)：`02_Races/Arilou.md:137`

### #6 · `AWK!`

- **呱** (1 處)：`02_Races/Yehat.md:125`
- **嗄** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:522`

### #7 · `Beta Brahe`

- **布拉赫 β** (1 處)：`07_Glossary/Fixed_Terms.csv:179`
- **第谷 β** (2 處)：`07_Glossary/Master_Glossary.md:279`、`07_Glossary/Place_Names.md:45`

### #8 · `Beta Corvi`

- **烏鴉座** (1 處)：`06_Locations/Star_Systems.md:47`
- **烏鴉座 β** (3 處)：`07_Glossary/Fixed_Terms.csv:174`、`07_Glossary/Master_Glossary.md:274`、`07_Glossary/Place_Names.md:36`

### #9 · `Birthing Fleet`

- **孕育艦隊** (1 處)：`07_Glossary/Master_Glossary.md:130`
- **孵化艦隊** (1 處)：`02_Races/Mycon.md:133`

### #10 · `Blade`

- **鋒刃艦** (2 處)：`04_Ships/Neutral_Ships.md:160`、`07_Glossary/Fixed_Terms.csv:79`
- **鐢刃艦** (2 處)：`07_Glossary/Master_Glossary.md:191`、`07_Glossary/Ship_Names.md:43`

### #11 · `BRAAK!`

- **呐** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:521`
- **呱** (1 處)：`02_Races/Yehat.md:124`

### #12 · `butt blasted`

- **屁滾尿流** (2 處)：`07_Glossary/Fixed_Terms.csv:213`、`07_Glossary/Master_Glossary.md:483`
- **屁股被轟爛** (2 處)：`08_Translation_Rules/Style_Guide.md:167`、`09_AI_Prompt/Translate_Dialogue.md:545`

### #13 · `Clear Spindle`

- **澄澈紡錐** (1 處)：`07_Glossary/Master_Glossary.md:229`
- **澄澈紡錘** (1 處)：`07_Glossary/Tech_Names.md:16`

### #14 · `Consider it, and consider well`

- **好好考慮** (1 處)：`03_Characters/Trade_Master_Greenish.md:73`
- **好好考慮,仔細考慮** (1 處)：`07_Glossary/Master_Glossary.md:388`

### #15 · `Creators`

- **創世者** (1 處)：`07_Glossary/Master_Glossary.md:133`
- **造物主** (1 處)：`02_Races/Mycon.md:143`

### #16 · `Crimson Corporation`

- **紅色財團** (1 處)：`07_Glossary/Fixed_Terms.csv:154`
- **血紅集團** (2 處)：`02_Races/Druuge.md:175`、`07_Glossary/Master_Glossary.md:316`

### #17 · `Deep Child`

- **深子** (1 處)：`07_Glossary/Tech_Names.md:20`
- **深層幼體** (1 處)：`02_Races/Druuge.md:208`

### #18 · `Deep Children`

- **深層幼體** (1 處)：`02_Races/Mycon.md:130`
- **深淵之子** (1 處)：`02_Races/Syreen.md:239`

### #19 · `Delta Crateris`

- **巨爵座** (1 處)：`06_Locations/Star_Systems.md:46`
- **巨爵座 δ** (3 處)：`07_Glossary/Fixed_Terms.csv:175`、`07_Glossary/Master_Glossary.md:275`、`07_Glossary/Place_Names.md:37`

### #20 · `Delta Vulpeculae`

- **狐狸座** (1 處)：`06_Locations/Star_Systems.md:36`
- **狐狸座 δ** (2 處)：`07_Glossary/Fixed_Terms.csv:176`、`07_Glossary/Place_Names.md:38`

### #21 · `Depart`

- **走開** (1 處)：`03_Characters/Admiral_ZEX.md:73`
- **離開。** (1 處)：`02_Races/Druuge.md:170`

### #22 · `Dhrang`

- **Dhrang** (1 處)：`07_Glossary/Fixed_Terms.csv:197`
- **保留原文** (1 處)：`07_Glossary/Master_Glossary.md:468`

### #23 · `donkey breath`

- **臭嘴巴** (2 處)：`07_Glossary/Fixed_Terms.csv:212`、`07_Glossary/Master_Glossary.md:482`
- **驢子口臭** (2 處)：`08_Translation_Rules/Style_Guide.md:166`、`09_AI_Prompt/Translate_Dialogue.md:544`

### #24 · `Druuge`

- **商業敬語** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:68`
- **毒賈族** (2 處)：`07_Glossary/Fixed_Terms.csv:29`、`07_Glossary/Master_Glossary.md:66`

### #25 · `Dynamo`

- **發電機** (1 處)：`01_World_Lore/Technology_Level.md:42`
- **能量發電機模組** (1 處)：`07_Glossary/Master_Glossary.md:373`

### #26 · `ENACTING THIRD LAW`

- **執行第三定律。** (1 處)：`02_Races/Slylandro_Probe.md:130`
- **執行第三定律（自保）。** (1 處)：`07_Glossary/Master_Glossary.md:406`

### #27 · `Epsilon Camelopardalis`

- **鹿豹座** (1 處)：`06_Locations/Star_Systems.md:48`
- **鹿豹座 ε** (1 處)：`07_Glossary/Place_Names.md:42`

### #28 · `Fat Obstreperous Jerks`

- **「肥胖粗俗混蛋」** (1 處)：`07_Glossary/Master_Glossary.md:329`
- **肥屁噪嗔混蛋** (1 處)：`02_Races/Thraddash.md:191`

### #29 · `Fury`

- **憤怒者** (3 處)：`04_Ships/Alliance_Ships.md:140`、`07_Glossary/Fixed_Terms.csv:67`、`07_Glossary/Master_Glossary.md:179`
- **烈憤艦** (1 處)：`07_Glossary/Ship_Names.md:45`

### #30 · `Gamma Vulpeculae`

- **狐狸座** (1 處)：`06_Locations/Star_Systems.md:37`
- **狐狸座 γ** (2 處)：`07_Glossary/Fixed_Terms.csv:177`、`07_Glossary/Place_Names.md:39`

### #31 · `Glory Device`

- **光榮裝置** (1 處)：`02_Races/Shofixti.md:145`
- **榮耀彈** (3 處)：`04_Ships/Alliance_Ships.md:144`、`07_Glossary/Fixed_Terms.csv:102`、`07_Glossary/Master_Glossary.md:233`

### #32 · `Grand-High Poobah`

- **大高酋長** (1 處)：`02_Races/Zoq_Fot_Pik.md:152`
- **尊貴至極的波霸大人** (1 處)：`07_Glossary/Master_Glossary.md:352`

### #33 · `Great Teacher`

- **偉大導師** (1 處)：`07_Glossary/Master_Glossary.md:334`
- **偉大的導師** (1 處)：`02_Races/Thraddash.md:179`

### #34 · `HARG! HARG! HARG!`

- **哈！哈！哈！** (1 處)：`07_Glossary/Master_Glossary.md:333`
- **絕不譯** (1 處)：`02_Races/Thraddash.md:169`

### #35 · `Hee! Hee! Hee!`

- **嘿嘿嘿** (1 處)：`02_Races/VUX.md:179`
- **嘿嘿嘿！** (1 處)：`07_Glossary/Master_Glossary.md:439`

### #36 · `HOOT!`

- **呐** (1 處)：`08_Translation_Rules/Alien_Speech_Rule.md:524`
- **呼** (1 處)：`02_Races/Yehat.md:128`

### #37 · `HyperSpace`

- **超空間** (6 處)：`01_World_Lore/Technology_Level.md:10`、`06_Locations/Star_Systems.md:57`、`07_Glossary/Fixed_Terms.csv:127`、`07_Glossary/Master_Glossary.md:243`、`07_Glossary/Place_Names.md:88`、`07_Glossary/Tech_Names.md:159`
- **超維空間** (1 處)：`02_Races/Arilou.md:139`

### #38 · `HyperWave 'Caster`

- **超波廣播器** (1 處)：`03_Characters/Talking_Pet.md:104`
- **超波播送器** (2 處)：`02_Races/Druuge.md:204`、`07_Glossary/Master_Glossary.md:381`

### #39 · `Iccamullon`

- **Iccamullon** (1 處)：`07_Glossary/Fixed_Terms.csv:196`
- **保留原文** (2 處)：`07_Glossary/Master_Glossary.md:467`、`07_Glossary/Place_Names.md:103`

### #40 · `Melnorme`

- **梅諾商** (2 處)：`07_Glossary/Fixed_Terms.csv:30`、`07_Glossary/Master_Glossary.md:67`
- **高階商務** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:69`

### #41 · `Mmmmmm!`

- **嗯** (1 處)：`02_Races/VUX.md:181`
- **嗯～～～～** (1 處)：`07_Glossary/Master_Glossary.md:445`

### #42 · `Mohorovichic`

- **地殼深處** (1 處)：`07_Glossary/Master_Glossary.md:126`
- **莫氏不連續面** (1 處)：`02_Races/Mycon.md:135`

### #43 · `MORON RATHEAD`

- **照鎖** (2 處)：`08_Translation_Rules/Style_Guide.md:168`、`09_AI_Prompt/Translate_Dialogue.md:546`
- **白痴鼠腦** (2 處)：`07_Glossary/Fixed_Terms.csv:214`、`07_Glossary/Master_Glossary.md:484`

### #44 · `Mycon`

- **禱詞式短句** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:61`
- **麥孔族** (4 處)：`02_Races/Syreen.md:238`、`03_Characters/Talana.md:70`、`07_Glossary/Fixed_Terms.csv:19`、`07_Glossary/Master_Glossary.md:56`

### #45 · `neo-Dnyarri`

- **不直譯** (2 處)：`03_Characters/Talking_Pet.md:96`、`07_Glossary/Master_Glossary.md:86`
- **不直譯，通篇用「會話寵」/「蟾亞」交替** (1 處)：`03_Characters/Talking_Pet.md:305`

### #46 · `Non`

- **異類** (1 處)：`07_Glossary/Master_Glossary.md:121`
- **非** (1 處)：`02_Races/Mycon.md:126`

### #47 · `Orz`

- **星號詞語** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:70`
- **歐茲族** (3 處)：`02_Races/Arilou.md:146`、`07_Glossary/Fixed_Terms.csv:31`、`07_Glossary/Master_Glossary.md:68`

### #48 · `Pkunk`

- **新時代嘻皮** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:71`
- **普恩族** (2 處)：`07_Glossary/Fixed_Terms.csv:25`、`07_Glossary/Master_Glossary.md:62`

### #49 · `Portal Spawner`

- **傳送門生成器** (3 處)：`02_Races/Druuge.md:206`、`05_Technology/Ship_Modules.md:81`、`07_Glossary/Master_Glossary.md:227`
- **傳送門產生器** (1 處)：`02_Races/Arilou.md:142`

### #50 · `PROBE 2418-B`

- **2418-B 號探測器** (1 處)：`07_Glossary/Master_Glossary.md:408`
- **探測器 2418-B** (1 處)：`02_Races/Slylandro_Probe.md:127`

### #51 · `Procyon`

- **南河三** (4 處)：`06_Locations/Star_Systems.md:35`、`07_Glossary/Fixed_Terms.csv:166`、`07_Glossary/Master_Glossary.md:266`、`07_Glossary/Place_Names.md:28`
- **注意** (1 處)：`09_AI_Prompt/Translate_Lore.md:145`

### #52 · `roof-rabbit`

- **小兔崽子** (2 處)：`07_Glossary/Fixed_Terms.csv:210`、`07_Glossary/Master_Glossary.md:480`
- **屋頂兔** (2 處)：`08_Translation_Rules/Style_Guide.md:164`、`09_AI_Prompt/Translate_Dialogue.md:542`

### #53 · `RU`

- **RU** (2 處)：`07_Glossary/Fixed_Terms.csv:135`、`07_Glossary/Tech_Names.md:136`
- **資源單位** (2 處)：`01_World_Lore/Technology_Level.md:33`、`05_Technology/Resource_Elements.md:46`

### #54 · `Shattered Worlds`

- **碎裂世界** (1 處)：`02_Races/Mycon.md:142`
- **碎裂世界群** (1 處)：`07_Glossary/Master_Glossary.md:131`

### #55 · `Shiva Furnace`

- **希瓦爐** (1 處)：`07_Glossary/Fixed_Terms.csv:141`
- **濕婆熔爐** (3 處)：`05_Technology/Ship_Modules.md:53`、`07_Glossary/Master_Glossary.md:367`、`07_Glossary/Tech_Names.md:107`

### #56 · `Shofixti Maidens`

- **修烈士少女** (1 處)：`02_Races/VUX.md:186`
- **修菲少女** (1 處)：`02_Races/Druuge.md:202`

### #57 · `Slylandro`

- **半正式詩意悠閒** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:72`
- **斯萊族** (2 處)：`07_Glossary/Fixed_Terms.csv:27`、`07_Glossary/Master_Glossary.md:64`

### #58 · `Slylandro Probe`

- **全大寫** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:109`
- **斯萊探測器** (2 處)：`07_Glossary/Fixed_Terms.csv:28`、`07_Glossary/Master_Glossary.md:65`

### #59 · `Sol`

- **太陽** (1 處)：`09_AI_Prompt/Translate_Lore.md:143`
- **太陽系** (1 處)：`07_Glossary/Fixed_Terms.csv:161`

### #60 · `Solar Manipulator`

- **太陽操縱器** (1 處)：`02_Races/Mycon.md:134`
- **恆星操控器** (1 處)：`07_Glossary/Master_Glossary.md:122`

### #61 · `Spathi`

- **卑躬屈膝** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:73`
- **史怕族** (2 處)：`07_Glossary/Fixed_Terms.csv:16`、`07_Glossary/Master_Glossary.md:54`

### #62 · `Stinger`

- **刺激者號** (3 處)：`04_Ships/Neutral_Ships.md:166`、`07_Glossary/Fixed_Terms.csv:82`、`07_Glossary/Ship_Names.md:49`
- **刺針號** (1 處)：`07_Glossary/Master_Glossary.md:195`

### #63 · `Storage Bay`

- **儲藏艙** (2 處)：`05_Technology/Ship_Modules.md:36`、`07_Glossary/Tech_Names.md:89`
- **貨艙** (1 處)：`07_Glossary/Master_Glossary.md:372`

### #64 · `Sub-commander DAX`

- **副指揮官達克斯** (1 處)：`07_Glossary/Master_Glossary.md:154`
- **達克斯副指揮官** (1 處)：`02_Races/VUX.md:190`

### #65 · `Supox`

- **極正式優雅** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:74`
- **蘇菩族** (2 處)：`07_Glossary/Fixed_Terms.csv:24`、`07_Glossary/Master_Glossary.md:61`

### #66 · `Syreen`

- **古典感** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:59`
- **塞蓮族** (2 處)：`07_Glossary/Fixed_Terms.csv:15`、`07_Glossary/Master_Glossary.md:53`

### #67 · `Thraddash`

- **撻伐族** (2 處)：`07_Glossary/Fixed_Terms.csv:26`、`07_Glossary/Master_Glossary.md:63`
- **粗魯自嘲** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:75`

### #68 · `Token`

- **原譯** (1 處)：`09_AI_Prompt/Translate_Dialogue.md:247`
- **譯文** (1 處)：`08_Translation_Rules/Humor_Rule.md:405`

### #69 · `Trader / Melnorme Ship`

- **梅諾商貿易艦** (3 處)：`07_Glossary/Master_Glossary.md:194`、`07_Glossary/Master_Glossary.md:384`、`07_Glossary/Ship_Names.md:47`
- **貿易艦** (1 處)：`04_Ships/Neutral_Ships.md:164`

### #70 · `Turning Jet`

- **轉向噴嘴** (1 處)：`05_Technology/Ship_Modules.md:20`
- **轉向噴射器** (1 處)：`07_Glossary/Master_Glossary.md:371`

### #71 · `Ultron`

- **厄創** (7 處)：`01_World_Lore/Technology_Level.md:74`、`02_Races/Druuge.md:193`、`02_Races/Utwig.md:118`、`05_Technology/Precursor_Artifact.md:91`、`07_Glossary/Fixed_Terms.csv:123`、`07_Glossary/Master_Glossary.md:220`、`07_Glossary/Tech_Names.md:13`
- **究極子** (1 處)：`02_Races/Supox.md:196`

### #72 · `Vindicator`

- **復仇者號** (6 處)：`01_World_Lore/Technology_Level.md:72`、`04_Ships/Player_Flagship.md:84`、`05_Technology/Precursor_Artifact.md:95`、`07_Glossary/Fixed_Terms.csv:86`、`07_Glossary/Master_Glossary.md:204`、`07_Glossary/Ship_Names.md:59`
- **復仇艦** (4 處)：`04_Ships/Player_Flagship.md:85`、`07_Glossary/Fixed_Terms.csv:87`、`07_Glossary/Master_Glossary.md:205`、`07_Glossary/Ship_Names.md:60`

### #73 · `Void`

- **虛** (1 處)：`02_Races/Mycon.md:127`
- **虛空** (1 處)：`07_Glossary/Master_Glossary.md:120`

### #74 · `Yuptar`

- **尤普塔** (1 處)：`07_Glossary/Master_Glossary.md:96`
- **尤普塔族** (1 處)：`02_Races/Ur_Quan_Kzer_Za.md:130`

### #75 · `Zebranky`

- **札布蘭奇** (2 處)：`02_Races/Zoq_Fot_Pik.md:151`、`02_Races/Zoq_Fot_Pik.md:161`
- **澤布蘭基** (1 處)：`07_Glossary/Master_Glossary.md:348`

### #76 · `Zeta Persei`

- **英仙座** (2 處)：`02_Races/Druuge.md:209`、`06_Locations/Star_Systems.md:49`
- **英仙座 ζ** (3 處)：`07_Glossary/Fixed_Terms.csv:181`、`07_Glossary/Master_Glossary.md:281`、`07_Glossary/Place_Names.md:43`

### #77 · `Zoq-Fot-Pik`

- **三方交錯** (1 處)：`00_Project_Control/Dossier_Voice_Audit_2026-08-15.md:113`
- **佐-佛-皮** (2 處)：`07_Glossary/Fixed_Terms.csv:32`、`07_Glossary/Master_Glossary.md:69`

---

## 附註

- 本報告是**自動化的第一次通盤掃描**。人工閱讀可能會發現：
  - 某些「衝突」實為 delta（舊 canonical 未更新 · 例如 Fixed_Terms.csv 未追上 Master_Glossary.md）
  - 某些同一 English 在不同語境合法有多譯（例如 Cannon 憂特 vs 毒賈）
  - 「保留原文」與「中譯」共存，通常代表新舊 canonical policy 交替期
- 建議搭配 shipped JSON 對照（Phase 2）決定最終 canonical

