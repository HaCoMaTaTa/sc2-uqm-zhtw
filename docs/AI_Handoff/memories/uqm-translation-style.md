# UQM zh-TW translation style (Star Control 2)

## Core principle
Player response and NPC dialog have DIFFERENT translation modes:
- **NPC dialog**: Match the character's voice — as weird/formal/vulgar as original.
- **Player response**: Say what a Taiwanese speaker would say in the same situation. NEVER literal char-by-char translation.

Full guide: [Star Control II GUS - Manual/SC2_繁中化_AI翻譯提詞.md](Star%20Control%20II%20GUS%20-%20Manual/SC2_繁中化_AI翻譯提詞.md) §9

## Player response pronoun switching (situational)
- Formal self-intro → 「我是 X 艦長」/「我方」
- Angry retort → 「老子」/「你」/「你這」
- Neutral conversation → 「我方」/「我」

## English coined-idiom → Taiwan equivalent (must-check list)
| English | ✗ literal | ○ Taiwan-natural |
|---|---|---|
| roof-rabbit | 屋頂兔 | **小兔崽子** |
| vapor city (for you) | 化為蒸氣 | **灰飛煙滅** |
| donkey breath | 驢子口臭 | **臭嘴巴** |
| butt blasted | 屁股被轟爛 | **被打得屁滾尿流** |
| non-functional sex organ | 非功能性生殖器 | **陽痿無膽的廢物** |
| bloodless sack of decaying flesh | 一袋腐肉 | **腐肉袋** (compound noun, don't split) |
| toothless, piebald, impotent | 無牙、花斑、陽痿 | **缺牙、雜毛、硬不起來** |

## Abstract EN nouns → context-appropriate ZH (added 2026-08-28 utwig)
When character evaluates the Captain, EN uses abstract nouns that don't map to their academic ZH equivalents. Pick word that matches **social evaluation register**, not dictionary translation.
| English (context) | ✗ dictionary | ○ contextual |
|---|---|---|
| your ethics are sound (character evaluation) | 你的倫理健全 | **你的品格亦屬端正** / **你的德行光明** |
| well-deserved (facial appliance status) | 你自己應得的面具 | **早該屬於你的面具** |
| the meaning for our continued existence | 憂特之存續意義 | **憂特族存續的意義** |
| destructive device of dignity (Utwig bomb) | 尊嚴之毀滅性裝置 | **承載本族尊嚴的毀滅裝置** |
| destructive device of dignity | (context: symbolic honor) → NOT "dignity's device" |
**Flag rule**: If EN has `[abstract noun] of/is [abstract noun]` and ZH direct translation feels academic/detached, propose 3-5 register-appropriate options.

## OUT_TAKES 打破第四牆 pronoun 例外規則 (added 2026-08-28 druuge)
Star Control 2 每族的 `OUT_TAKES` token 播於遊戲結局字幕 · 模仿電影 NG 花絮 · **14 族 100% 有此 token · 10 族明顯打破第四牆**（角色跳出跟導演/設計師/觀眾對話）。

**通則**：OUT_TAKES **允許 pronoun 打破 dossier canonical** · 依「跳出角色的程度」選擇：
- **完全跳出角色**（演員/工作人員身分講話）→ 用「我」/「本人」現代自然（例：Supox「當憂特配角很辛苦」/ Druuge 談合約 / Thraddash「史匹柏」）
- **保留角色 canonical 反諷**（角色本人吐槽自己節目）→ 保留招牌自稱（例：Orz「歐茲」/ Pkunk「我族」/ Yehat「本騎士」/ Talkingpet「本尊」）
- **混合場景**（部分敘述跳出 · 部分情緒吶喊維持角色）→ c4 策略：合約/敘述用「本人」· 情緒吶喊保留「我」（例：Druuge OUT_TAKES 本 audit）

**特殊案例**：
- **Urquan OUT_TAKES**：不是 Kzer-Za 本體！是**螢幕角落的小翻譯員**（獨立角色）· 用「我」正確 · 不套用 Kzer-Za「本平台」canonical
- **Kohrah OUT_TAKES**：內建混合（前段「我族即烏寬柯亞」+ 後段 NG「卡！重來一次！」用「我」）· 遊戲設計本身就標示了跳出點

**識別 flag**：EN 出現 `sequel / director / creative control / producer / royalties / license / script / dialog / rehearsal` 或 `1-900-XXX` 廣告或 fourth-wall breaking phrases → 提示考慮 pronoun 例外

## Ship 命名 canonical 仲裁規則 (added 2026-08-28 umgah, updated 2026-08-28 zoqfotpik)
**權威優先順序**（**依 date 判斷 · 最新為準**）：
1. **`07_Glossary/Master_Glossary.md`** 是**所有專有名詞 canonical 最終權威** (Single Source of Truth)
   - v0.5.2 (2026-08-11) / v0.7 (2026-08-15) / v0.8 (2026-08-18) 為最新版本
   - **覆蓋所有其他來源** — Ship_Names.md/dossier/舊 canonical 均次之
2. **`07_Glossary/Ship_Names.md`** — 但**可能過期**，如與 Master_Glossary 衝突以 Master_Glossary 為準
3. **`04_Ships/<Faction>_Ships.md`** 檔
4. **`Translate_Item.md`** 命名理由文檔
5. **族 dossier (02_Races/<Race>.md) 核心詞彙表**（**優先度最低**，容易與 Master_Glossary 衝突）

**已知案例**：
- `Umgah Drone`：族 dossier 詞彙表寫「無人機」誤導 · **實際 canonical 為「蜂機艦」**（Ship_Names.md L30 · Hierarchy_Ships.md L67 · Translate_Item.md L35 皆確認）
- **`Zoq-Fot-Pik Stinger`：Ship_Names.md L49 寫「刺激者號」但 Master_Glossary v0.5.2 L507 明訂「取代舊『刺激者號』」→ 最新 canonical 為「刺針號」** (2026-08-28 umgah audit 誤用 Ship_Names.md 導致 · 已在 zoqfotpik audit 修正)
- **Yip/Tun canonical**: dossier v0.7 「依普/圖恩」為過期 · Master_Glossary v0.5.2 「葉普/屯」為最新
- **Frungy canonical**: 「芙戎奇」（芙 U+8299 · Master_Glossary 上顯示可能誤植為「苙戎奇」但實際 shipped 用 芙戎奇）

## Unicode 字形辨識風險清單 (added 2026-08-28 safeones)
編輯時務必用 grep 驗證這些視覺相似字：
| 正確 | 誤植 | 說明 |
|---|---|---|
| 芙 (U+8299 hibiscus) | 苙 (U+82D9 plant) | 芙戎奇 · shipped canonical |
| 蠢 (U+8822 stupid) | 蠶 (U+8836 silkworm) | 愚蠢 · safeones YOUR_BEHAVIOR shipped 誤字修 |
| 賈 (U+8CC8 surname Jia) | 賣 (U+8CE3 sell) | 賈德·魔怪 · safeones GENERAL_INFO_1 我 U2 replacement 誤打 |
| 醜 (U+919C ugly) | 醬 (U+91AC sauce) | 醜聞 · safeones GENERAL_INFO_1 我 U2 replacement 誤打 |
| 誼 (U+8ABC friendship) | 誰 (U+8AB0 who) | 友誼 · safeones CC1 replacement 誤打 |
| 骨 (U+9AA8 bone) | 骸 (U+9AB8 remains) | 骨骸坑 · kohrah BONE_PILE shipped 誤字 (× 4 處) |
| 撻 (U+6483 lash/hit) | 沒 (U+6C92 sink) | 撻伐族 · thraddash HELLO_PIG_LATIN_1 我 CC1 replacement 誤打 |
| 沾 (U+6CBE dip) | 沒 (U+6C92 sink) | 沾點起司醬 · supox thanks_now_we_eat_you shipped 誤字 (沒點→沾點) |
| 牽 (U+727D lead) | 犧 (U+72A7 sacrifice) | 犧牲 · zoqfotpik THANKS_FOR_RESCUE9 shipped 誤字修 |
| 耗 (U+8017 consume) | 耽 (U+803D delay) | 耗時 · chmmr WE_ARE_FREE 招牌 shipped 誤字 (耽時→耗時 · 對齊 dossier §六 範例 1 canonical) |
| 聰 (U+8070 clever · 繁體) | 聡 (U+806A shinjitai · 日文變體) | 聰明 · vux Batch 1 replacement oldString 誤打日文變體導致失敗 · 中譯必用 U+8070 |
| 竭 (U+7AED exhaust) | 竞 (U+7ADE simplified) | 竭力 · yehat Batch 2 Q25 replacement oldString 誤打簡體導致失敗 · 中譯必用 U+7AED |
| 鑿 (U+947F chisel) | 鿰 (U+9FF0 rare) | 確鑿 · yehat Batch 0 rewrite typo · U+9FF0 極少用 |
| 嚥 (U+56A5 swallow) | 嚈 (U+5688 rare) | 吞嚥 · yehat Batch 0 GENERAL_INFO_SPACE_3 rewrite typo |
| 羞 (U+7F9E shame) | 翞 (U+7FDE bird sound rare) | 羞愧 · yehat Batch 0 rewrite typo |
| 唉 (U+5509 sigh) | 唐 (U+5510 Tang dynasty) | 唉/sorry_about_revolution · yehat Batch 0 typography sweep rewrite typo |
| 蠢 (U+8822 stupid) | 蟲 (U+87F2 insect) | 蠢貨 · yehat Batch 0 bye_royalist rewrite typo (also different from safeones 蠢/蠶 case) |
**workflow**：使用 multi_replace_string_in_file 時 · 若 newString 含罕見/複雜字 · 修完立即 grep 驗證所有專有名詞 · **特別注意 U+8xxx 和 U+9xxx 區域的視覺相似字**（賈/賣、醜/醬、誼/誰、蠢/蠶、骨/骸、撻/沒）· **檢查 _notes canonical vs token 用字一致性**

**檢查腳本 pattern**：
```powershell
# 檢查所有相關詞在 Master_Glossary 的最新 canonical
grep -E "詞A|詞B|詞C" StarControl2_TW_Localization/07_Glossary/Master_Glossary.md
```

**血淚教訓（2026-08-28）**：
- Umgah audit 時只查 Ship_Names.md 誤把「蜂機艦」當過期，實則相反
- Zoqfotpik audit 時基於 Ship_Names.md「刺激者號」+ dossier「依普/圖恩」進行 canonical 對齊，實則 Master_Glossary v0.5.2 更新為「刺針號/葉普/屯」→ 3 處誤修需 revert
- **新 workflow**：所有 canonical 決策前先 grep Master_Glossary + 檢查日期戳

## Avoid character classes
- Medical/anatomical: 陽痿 → 硬不起來 · 生殖器 → 命根子/傳宗玩意
- Biological: 雌性個體 → 女性同胞 · 種族 (dialog) → 族 (shorter)
- Literary/archaic: 淌鼻涕 → 流鼻涕 · 爾艦 → 你艦 · 汝 → 你
- Chinese-Mainland-only chars technically 繁體 but unnatural in TW: 蔫 → 軟趴趴/硬不起來

## Space wrapping (post-patch-006)
- `getLineWithinWidth` in `comm.c` now treats CJK as word boundary → **CJK-CJK spaces NOT needed for wrap**
- Keep spaces only at: Lua template borders, CJK↔ASCII boundaries, natural punctuation-nearby
- **CRITICAL**: don't split compound nouns with spaces
  - ✗ `軟趴 貧血 一袋 腐肉 的 烏寬` (reader can't parse structure)
  - ○ `軟趴趴貧血的腐肉袋烏寬`

## Character voice registry (per-race pronoun setting)
Recorded in each `translations/<race>.zh-TW.json` `_notes`:
- **田中 Tanaka** = 熱血 anime 武士戰士 → 自稱「俺」+ 常喊 Kyaiee!
- **武士刀 Katana** = 姊姊，冷靜穩重 → 自稱「本人」(contrast with 田中's 俺)
- **海斯 Cdr. Hayes** = 地球奴役星站指揮官 → 正式軍語，「我方」
- **Ur-Quan Kzer-Za drone** = 冰冷征服者 →「本平台」+「爾等」
- **Slylandro** = 氣態原住民 → 好奇熱情，第三人稱「我族」
- **Utwig 憂特族** (v0.7 v3 v2 shipped, 2026-08-16):
  - 舊定位「莎士比亞式悲劇詠嘆調」**錯**——Sa-Matra 對白庫實測 Utwig 無 thou/thee/thy/倒裝/韻文,只是現代學術冗長句+官樣文
  - 開發者 Paul Reiche 明確受 **Jack Vance** 影響 (Wikipedia SC2 條目)
  - **正確定位**: 「現代學者式憂鬱華麗長句 + 官僚報告體 + 冷式反諷」= 哲學崩潰的高知識份子集體憂鬱症
  - **自稱 palette v2** (v3 v2 分布): 我方 49 · 我 108 · 我們 75 · 我們憂特 23 · 本族 103 · 憂特一族 5 · 本監督團 2 · 本代表 1
  - **稱訪客**: 你/你們(預設); 仁慈的星際旅人/神聖之艦長/厄創聖徒(戲劇性)
  - **避免**: 文言古語(吾/爾/之/乃/哉/矣/焉)——與原文語域不符
  - **保留**: 痛哉!/唉/*嘆息*(少量點綴);冷式自嘲(`Ha ha, don't worry. Hey! I laughed!`)必譯保留
  - **面具 canonical v2 (2026-08-16)**: M1=例行辛勞事務面具/M2=星辰代表容貌/M3=至極羞恥面具/M9=狂喜歡騰彈跳面具/M14=啟示歡騰躍舞/M15=哀悼陣亡袍澤;其餘保留 shipped 去「之」精簡版
  - **Q1 感嘆詞 v0.7 update**: Oh, woe! 與 Alas! 併合為「痛哉！」(不再用「悲夫！」)
  - **shipped bug 修**: `#(why_you_here)`, `#(hey_wait_got_ultron)`, `#(what_now_homeworld)` 玩家對白 shipped 誤用「爾等」→ v3 v2 全改「你們」

## Unicode hazard 清單 (multi_replace 常見形近字錯誤 · updated 2026-08-30)
| 目標字 | Unicode | 常誤打成 | 誤打 Unicode | 場景 |
|---|---|---|---|---|
| 俺 | U+4FFA | 俱 | U+4FF1 | 田中/修烈士自稱 |
| 唉 | U+5509 | 唐 | U+5510 | 感嘆詞 Hyai! |
| 喂 | U+5582 | 喵 | U+55B5 | 田中呼叫/罵人 |
| 竭 | U+7AED | 竞 | U+7ADE | 竭盡 |
| 鑿 | U+947F | 鿰 | U+9FF0 | 鑿岩 |
| 嚥 | U+56A5 | 嚈 | U+5688 | 嚥氣 |
| 羞 | U+7F9E | 翞 | U+7FDE | 羞辱 |
| 蠢 | U+8822 | 蟲 | U+87F2 | 大蠢材 |
| 呀 | U+5440 | 呑 | U+5451 | 呀哈！ |
| 竟 | U+7ADF | 竞 | U+7ADE | 究竟/竟然（`竞`為簡體!） |
| 兮 | U+516E | 克 | U+514B | 神祕兮兮 |
| 眷 | U+7737 | 瞊 | U+778A | 眷顧 |
| 喘 | U+5598 | 喃 | U+5583 | 喘不過氣 |
| 馭 | U+99AD | 駭 | U+99ED | 駕馭 |
| 蹦 | U+8E66 | 蕂/蕃 | U+8574/U+8543 | 歡蹦亂跳 |
| 俯 | U+4FEF | 仰 | U+4EF0 | 俯身飛撲 |

**規則**: 用 `\u` escape 之前先 lookup Unicode · 若不確定 · 用 `replace_string_in_file` 加 plain-text UTF-8 chars。

## Utility script
- `uqm-work/_strip_cjk_spaces.py` — regex removes `[CJK][space]+[CJK]` (skips `_notes` block).
  Post-patch-006 you can strip all spacing-wrap after translating.

## Package sanity check
- `package_zh-TW.ps1` has auto-detect for stale ZIP (compare stage marker size vs zip entry).
  If mismatch (e.g. `Compress-Archive` file-lock silently fails on 2nd run) → auto-retry.
- Confirmed root cause 2026-08-06 when back-to-back build+package produced stale `zh-TW.uqm`.

## Verified races (as of 2026-08-06)
- commander (94 tokens) — GREEN
- urquan (12 tokens) — GREEN
- slylandro (114 tokens, v0.3 retrofit) — GREEN
- **shofixti** (91 tokens, v0.2 台式順口 rewrite) — GREEN, in-game verified
- Total 311/3547 = 8.8%

## Q1/Q2/Q4/Q5 decisions log (shofixti workshop 2026-08-06)
- Q1=A situational pronoun switch (adopted globally)
- Q2=A Taiwan-natural colloquial (adopted globally)
- Q4=A Katana=「本人」 (contrast with 田中's 俺)
- Q5 five specific fixes recorded in shofixti.zh-TW.json `_notes`
