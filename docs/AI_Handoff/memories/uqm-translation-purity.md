# UQM zh-TW translation purity gate

## Build gate: `_check_zh_purity.py`
- Runs as `build_zh-TW.ps1` **Step 0** with `--strict` (exit 1 on violation).
- Scans `translations/*.zh-TW.json` (excludes `gamestrings.zh-TW.json`).
- Modes: `--verbose` (show every violation), `--race X` (single race), `--strict` (fail).
- Established after spathi v0.2 caught 69× 「本人」 voice violation + 33× English 「Spathi」 mixed.

## What it checks
1. **Bare English race names** in dialog (Spathi, Ur-Quan, Ilwrath, Yehat, Syreen,
   Shofixti, Umgah, Melnorme, Pkunk, Slylandro, Chenjesu, Mmrnmhrm, Mycon,
   Arilou, Chmmr, Zoq-Fot-Pik, Orz, Androsynth, Utwig, Supox, Thraddash, Druuge,
   Kohr-Ah, Kzer-Za).
2. **Simplified-only chars** (吗/说/让/来/过/会/发/这 etc.). Bilateral chars
   (著/被/曾/面/概/西) EXCLUDED — they exist in both scripts.

## What is NOT checked (intentional style)
- **CJK + ASCII space + CJK** — used as narrative pause per style §9.
  - `commander OK_THE_CAN`: 「── 異星諸邦協和聯盟」dash stately intro
  - `urquan SEND_MESSAGE`: 「爾等 已擅闖 烏寬領空。」 烏寬 stately speech
  - `slylandro`: 「型錄第 2418 號 遠端自我複製 機器人探索探測器」目錄名
  - `pkunk`: 靈性緩慢 pause 節奏(88 處)

## Whitelists
- `ALIEN_WHITELIST` = words kept in English on purpose (v0.3 §5):
  Wezzy-Wezzah, Huffi-Muffi-Guffi, BGAK, PKUNKRA, AIEEEE, HAIL,
  Kyaiee, Har-Har, Hee, Homosap, Hunam, Hootmans, Precursor(s), etc.
- `TOKEN_EXEMPT` = per-token exceptions (self-etymology metadata):
  `pkunk:GENERAL_INFO_NEUTRAL_4` — 「『Pkunk』意為和平」需要展示原詞

## Adding new races
- Add English race name to `RACE_NAMES` list in `_check_zh_purity.py`.
- If new race has alien signature words, add them to `ALIEN_WHITELIST`.
- Run `python _check_zh_purity.py --strict --verbose` before committing.

## Second gate: `_check_lua_templates.py`
- Also runs in `build_zh-TW.ps1` Step 0 with `--strict`.
- Scans Lua template first-args in `<% comm.<helper>("first_arg", ...) %>`
  where `<helper>` ∈ {getColor, getConstellation, getStarName, getPoint, swapIfSeeded}.
- Flags first-args starting with `[A-Za-z]` (English leak in !StarSeed).
- `TEMPLATE_EXEMPT` set: per-token exceptions like
  `pkunk:GENERAL_INFO_SPACE_5:DRACONIS` (mystic shout with inline zh annotation).

## Astronomy vocab standard (v0.3 §4)
- Chinese: 華文天文標準 (船帆座/巨蛇座/英仙座/天龍座/圓規座 etc.).
- Game-specific 音譯: pattern `克魯格γ`, `布拉赫β` (音譯 + Greek letter suffix).
- **Rule**: 首次提及必附英文原文,格式 `中譯 (English)` for star map cross-ref.
- Fixed 14 first-args (commit ebed617): commander×3, pkunk×7, spathi×4.

## v0.3 §5 preserved English (game-invented, not Latin astronomy)
- BugSquirt = 蟲噴星系 (translated per user decision 8C on 2026-08-07).
- Wezzy-Wezzah, Huffi-Muffi-Guffi, BGAK, AIEEEE, HAIL, Kyaiee, Hee, Chrupp,
  PKUNKRA, Nyark = preserved English.

## Canonical zh race names (SOURCE OF TRUTH — never invent variants)
Every translation MUST use these exact strings. `_check_zh_purity.py`
`FORBIDDEN_ZH_VARIANTS` blocks common homophones.

| English | 繁中 canonical | Common wrong variants (blocked) |
|---|---|---|
| Spathi | **史怕族** | 史帕族, 斯帕族, 史巴族 |
| Ur-Quan | **烏寬 / 烏寬族** | 烏爾寬, 奧寬, 烏寬人 |
| Ilwrath | **蛛狂族** | 伊爾拉斯族, 伊瑞斯族 |
| Yehat | **翼哈特族** ★ | 葉哈族, 葉哈特族 (v0.3 舊譯, v0.4 已重設為翼哈特族; v0.2 舊表寫葉哈) |
| Syreen | **塞蓮族** ★ | 賽倫族, 賽蓮族, 塞倫族 (「蓮」= 女性感,呼應塞蓮女妖神話) |
| Shofixti | **修烈士族** ★ | 蘇菲斯特族 (v0.3 舊譯,v0.4 已重設), 蘇菲特族, 蘇菲斯族, 蕭菲斯族, 修飛族 |
| Umgah | **阿姆嘎族** | 昂加族, 烏姆嘎族 |
| Melnorme | **梅爾諾** (no 族) | 米爾諾, 梅諾, 梅爾諾姆 |
| Pkunk | **普恩族** | 普肯族, 普庫族, 朋克族 |
| Slylandro | **斯萊族** | 斯萊蘭德族, 斯萊蘭卓族 |
| Chenjesu | **晶智族** | 陳吉蘇族, 簡結蘇族 |
| Chmmr | **查姆族** | 查嗯族, 克姆族 |
| Mycon | **麥孔族** | 麥空族, 邁孔族 |
| Androsynth | **安卓辛族** | 安卓辛特族, 安卓森族 |
| Arilou (Lalee'lay) | **阿麗露** (no 族) | 阿瑞婁族, 阿麗露族, 阿麗魯 |

### Individuals
| English | 繁中 canonical | Blocked |
|---|---|---|
| Talana | **泰蘭娜** | 泰拉娜, 塔拉娜, 塔蘭娜 |
| Fwiffo | **費佛** | 菲弗, 飛佛 |
| Diani (Talana sister) | **黛安妮** | 迪安妮, 迪安尼 (user override) |

### Places
| English | 繁中 canonical | Blocked |
|---|---|---|
| Gaia | **蓋亞** | 蓋婭, 該亞 |
| Syra | **賽拉** | 塞拉, 賽亞 |
| Spathiwa | **史怕娃** | 史帕娃 |
| Organon | **奧甘農** | 歐甘農, 奧格農 (Mycon trap star, 2026-08-07 user pick B) |

## ROOT CAUSE — 賽倫 vs 塞蓮 inconsistency (recorded 2026-08-07)
1. v0.2 vocab (`SC2-詞彙對照表.md` line 28) locked `Syreen = 塞蓮族`.
2. v0.3 vocab (`SC2-詞彙對照表-v0.3.md`) is 補漏版 — 不重列 v0.2 已有的族名 (see §1.5 note "Talana in v0.2 不重列").
3. During spathi v0.2 audit (2026-08-06), I wrote `Syreen = 賽倫族` in `_notes`
   from memory instead of consulting v0.2 canonical → wrong char (賽 vs 塞).
4. `spathi ABOUT_OTHER_RACES` propagated 賽倫族 into published addon.
5. User caught it during syreen prep (2026-08-07).
6. **Fix**: replaced 賽倫→塞蓮 in spathi.zh-TW.json, added FORBIDDEN_ZH_VARIANTS
   to `_check_zh_purity.py` blocking `賽倫族|賽蓮族|塞倫族` at build gate.

## WORKFLOW RULE (before every new race translation)
1. Read `_analysis/SC2-詞彙對照表.md` (v0.2 full list) — canonical race names.
2. Read `_analysis/SC2-詞彙對照表-v0.3.md` (v0.3 補漏) — patches to v0.2.
3. Check FORBIDDEN_ZH_VARIANTS in `_check_zh_purity.py` — never invent variants.
4. If a race name is missing from both tables, ask user before choosing.
5. NEVER rely on memory alone for canonical names — always grep vocab files first.

## Voice registry style (§9.5)
- Each race has designated self-references documented in each JSON's `_notes`:
  - spathi Fwiffo: 我(主) / 本史怕(儀式 6x) / 我族 / 我方
  - urquan: 本艦 / 我 / 烏寬族 / 爾等(你們)
  - pkunk: 我 / 我族 / 我們普恩族 / 我們
  - shofixti Katana: 我(主) / 蘇菲斯特族
  - slylandro: 我族 / 我們斯萊族
  - commander Hayes: 我 / 本星際基地
- Voice cross-checks with `_notes` block should be part of code review.
