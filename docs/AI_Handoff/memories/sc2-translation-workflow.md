# SC2 zh-TW translation workflow (Phase 14+)

## User interaction style (observed 22× in session 998e6e56, 2026-08-14)
User's canonical prompt prefix: **「優化題詞後執行 不臆測 有問題請問我」**
Meaning: 1) Refine my raw prompt into a cleaner internal task, 2) Never guess
when facts are ambiguous, 3) Ask before deciding on style / canonical choices.
**Practical rules for me**:
- When user asks "X 該怎麼做", always emit a 3-5 option comparison table
  (A/B/C with pros/cons + my recommendation) before doing anything irreversible.
- User answers by single letter ("A", "B", "C") or short list ("1.自動駕駛
  2.逃生單元 ..."). Preserve that number/letter mapping in follow-up.
- Never bury decisions in prose. Never invent canonical names — always grep
  `07_Glossary/Master_Glossary.md` first.
- If user says "OK 先做 X" — do only X, do not chain to Y/Z uninvited.
- If user reports symptom + you have ≥2 possible causes → give a 3-column
  outcome table (「結果 | 意義 | 下一步」) and let user run test to disambiguate.

## Star name postfix translation (C task B, ~150 條 pending as of 2026-08-14)
`gamestrings.txt` L1-1553 contains Greek prefix + Latin genitive postfix pairs.
**5-category rules** (recovered from session 998e6e56 turn 313):
1. **希臘字母前綴不譯**: Alpha/Beta/Gamma/... keep as-is (star map wants α β γ style)
2. **拉丁屬格 → 中文星座名**: Cassiopeiae=仙后座, Corvi=烏鴉座, Vulpeculae=狐狸座,
   Herculis=武仙座, Pavonis=孔雀座, Draconis=天龍座 (華文天文標準)
3. **專名星 → 中文專名/音譯**: Betelgeuse=參宿四, Procyon=南河三, Sol=太陽/索爾,
   Arcturus=大角星
4. **天文學家人名 → 音譯**: Brahe=第谷, Lalande=拉朗德, Krueger=克呂格,
   Cerenkov=切連科夫, Gorno=戈爾諾
5. **顯示寬度限制**: STAR MAP 右下星系名欄位窄,4-5 CJK 已滿。超長要縮寫。
**Trap**: STAR SEARCH (F6) 可能只吃 ASCII → 翻星座名前先驗證輸入介面是否支援 CJK,
不支援就只翻按鈕/UI 保留搜尋是 ASCII。

## Recover from Copilot Chat "Invalid string length" (V8 max string)
- Cause: session accumulated too much context (attachments + tool outputs).
- **Recovery playbook** (verified 2026-08-14 recovering session `998e6e56`):
  1. Open new chat in same workspace
  2. `session_store_sql` → `SELECT ... FROM sessions ORDER BY updated_at DESC`
     to find the dead session id
  3. Query last 12 `turns` for user_message + first 800 chars of assistant_response
     to get last plan/decision
  4. Query `session_files WHERE turn_index >= <last-100>` for touched files
  5. Reconstruct handoff summary and continue from there
- **Prevention**: don't attach 3+ large files at once, don't request full-JSON
  dumps in chat, ask for `replace_string_in_file` diffs instead.

## Pipeline is 2-stage — package alone is NOT enough
- `build_zh-TW.ps1`: JSON → staged `.txt` (in `zh-TW-addon/content/base/comm/<race>/<race>.txt`)
- `package_zh-TW.ps1`: staged `.txt` → `.uqm` zip → copy to `install/content/addons/zh-TW.uqm`
- **Trap**: running only package packages stale staged files. JSON changes never reach game.
- **Fix landed 2026-08-08 (Phase 14c)**: `package_zh-TW.ps1` now auto-invokes build (skip with `-SkipBuild`).

## PowerShell `Compress-Archive` host bug
- On this environment, `Compress-Archive` progress rendering triggers a truncated
  error like `Compress-Archive [The archive file 'Q:\...zh-TW-add.]` that aborts
  the pipeline. Output stops mid-way and `.uqm` never gets created.
- **Fix**: set `$ProgressPreference = 'SilentlyContinue'` before Compress-Archive.
- Now baked into `package_zh-TW.ps1` top-of-script.

## Level 3 Reaudit workflow (Phase 14a-b)
- Prompts: `StarControl2_TW_Localization/09_AI_Prompt/{Reaudit_Dialogue,Translate_Dialogue,QA_Check}.md`
- Process: 1) diff report with 🔴🟡🟢 severity, 2) user picks per-issue, 3) apply, 4) build+package, 5) in-game verify
- One race at a time — user preference.
- Verify script pattern: `_verify_uqm.ps1` extracts race .txt from packaged .uqm and counts key substrings.
- **Round 5 完成 (2026-08-11, session 998e6e56 turn 226): 26/26 races Level 3 audited 100%**.
  13 canonical 升級 (Nemesis→宿敵號 / Corridor Nine→通道九號 / Eluder→迴避者 /
  Alliance name_2/3/4 statements / Vega→織女星 / Jud the Vug→賈德魔怪 /
  Organon→歐加農 / Arcturus→大角星 etc). 從此開始只做 delta retrofit,不重新 audit。

## Narrative / lander scan translation (Translate_Lore.md)
- Prompt: `09_AI_Prompt/Translate_Lore.md` (for scan reports + narrative, NOT dialog).
- 32 lander scan reports 已全數翻譯 (2026-08-13 → 14, commits `bbe7f67 1c17556 a2a13ff`).
- Location cross-ref (recovered from session 998e6e56 turn 307):
  - chmmrbase/chmmrhome → Procyon (南河三)
  - shofixtibase → Delta Gorno (戈爾諾座 δ)
  - spathimonument → Beta Herculis (武仙座 β)
  - syreenbase → Betelgeuse (參宿四)
  - syreenvault → Epsilon Camelopardalis (鹿豹座 ε)
  - urquanwreck → Alpha Pavonis (孔雀座 α)
  - zfpcolony → Alpha Tucanae (杜鵑座 α)
  - androsynth_ruins / excavationsite / stele → 多處先驅者遺跡
- **Requires patch 008** (CJK scan report hang fix) — see uqm-font-hacks.md.

## v0.4 race name canonical (Phase 8.5b)
- Shofixti = 修烈士族 (NOT 蘇菲斯特)
- Yehat = 翼哈特族 (NOT 葉哈特)
- Mycon = 麥孔族 (NOT 梅蒙 — was translator error)
- VUX = VUX (NOT 蛛狂族 — that's Ilwrath)
- Umgah=陰嘎 / Thraddash=撻伐 / Dnyarri=蟾亞 / Supox=蘇菩 / Druuge=毒賈 / Melnorme=梅諾商
- Authority: `StarControl2_TW_Localization/07_Glossary/Master_Glossary.md`

## Interjection policy v0.4 Phase 14b (2026-08-08)
- Old: keep pure English (`Kyaiee!` unchanged)
- New: **中譯＋（原文）** format: `Kyaiee!` → `殺呀！（Kyaiee!）`
- Full-width parens; original punct/case preserved inside
- First-occurrence-only within same token (don't spam annotation)
- Exceptions: Orz `*asterisk words*`, religion (Juffo-Wup/Frungy)
- Authority: `Alien_Speech_Rule.md §1.1`
- Shipped translations: Kyaiee!=殺呀！/ Hyai!=唉呀！/ HYAIEEE!=嗚呀啊──！/ Ha!=哈！/ Banzai!=萬歲！
- Pending Phase 14d: Aieee!, AIEE!, Lykeee-lieee!, hee-hee-hee, Ho-ho-ho, SNORT!

## PowerShell pitfall: long inline commands with CJK + nested quotes hang
- Very long one-liners with CJK strings and nested `$(...)` interpolation get
  stuck at PS continuation prompt (`>>`) — parser thinks command incomplete.
- **Solution**: use script files (`_verify_*.ps1`, `_apply_*.ps1`) instead of
  inline. Faster to iterate and no quote/CJK escaping issues.

## Terminal cwd hazard: package script leaves cwd inside `_stage`
- After running `.\package_zh-TW.ps1`, terminal cwd may be `zh-TW-addon\_stage`
  (Push-Location without matching Pop in some code paths).
- **Habit**: always `Set-Location Q:\Dos_G\StarControl2\uqm-work` before verify
  scripts, or use absolute paths.

## Multi_replace unicode escape traps (CRITICAL)
- When multi_replace has CJK escape sequences (\uXXXX), typos in the hex nibbles
  produce visually-plausible but semantically-wrong chars. Even LLM-generated
  \uXXXX sequences can be off by 1-2 hex digits, producing garbage.
- **Real cases encountered**:
  - `\u4ff9=俹` (correct: `\u4ffa=俺`)
  - `\u81a3=膣` (correct: `\u81ba=膺`)
  - `\u558a=喊` (correct: `\u5594=喔`)  ← Phase 14c ilwrath
  - `\u986f=顟` (correct: `\u986b=顫`)  ← Phase 14c ilwrath
  - `\u77de=矞` (correct: `\u779e=瞞`)  ← Phase 14c ilwrath
  - `\u8ce4=賤` (correct: `\u8ced=賭`)  ← Phase 14c ilwrath
  - `\u8127=脧` (correct: `\u8139=脹`)  ← Phase 14c ilwrath
  - `\u5410=吐` (correct: `\u541e=吞`)  ← Phase 14c ilwrath
  - `\u7169=煦` (correct: `\u715e=煞`)  ← Phase 14c ilwrath
  - `\u88d2=裒` (correct: `\u8892=袒`)  ← Phase 14c ilwrath
  - `\u6085=悦` (correct: `\u608a=悅`) SIMPLIFIED! ← Phase 14c ilwrath
  - `\u5583=喃` (correct: `\u5598=喘`)  ← Phase 14c ilwrath
  - `\u5586=喆` (correct: `\u5594=喔`)  ← 2026-08-25 spathi v0.7
  - `\u8e8d=躍` (correct: `\u8e6a=躪`)  ← 2026-08-25 spathi v0.7
  - `\u5f7b=彻` (correct: `\u5fb9=徹`) SIMPLIFIED! ← 2026-08-25 spathi v0.7
  - `\u806a=聪` (correct: `\u8070=聰`) SIMPLIFIED! ← 2026-08-25 spathi v0.7
  - `\u8feb=迫` (correct: `\u8ff4=迴`)  ← 2026-08-25 spathi v0.7
  - `\u5507=唇` (correct: `\u5509=唉`)  ← 2026-08-25 spathi v0.7
  - `\u8827=蠧` (correct: `\u868a=蜊`)  ← 2026-08-25 spathi v0.7 (twice: ABOUT_US, YIPES)
  - `\u81a9=膩` (correct: `\u81a4=膛`)  ← 2026-08-25 spathi v0.7
  - `\u7827=砧` (correct: `\u7825=砥`)  ← 2026-08-25 spathi v0.7
  - `\u5561=啡` (correct: `\u554a=啊`)  ← 2026-08-25 spathi v0.7
  - `\u8afe=諾` (correct: `\u8af8=諸`)  ← 2026-08-25 spathi v0.7
  - `\u9414=鐔` (correct: `\u93df=鏟`)  ← 2026-08-25 spathi v0.7
  - `\u5be2=寢` (correct: `\u5bd2=寒`)  ← 2026-08-25 spathi v0.7
  - `\u869d=蚻` (correct: `\u873b=蛻`)  ← 2026-08-25 spathi v0.7 (twice)
  - `\u642f=搯` (correct: `\u640f=搏`)  ← 2026-08-25 spathi v0.7
  - `\u5636=嘶` (correct: `\u563f=嘿`)  ← 2026-08-25 spathi v0.7
  - `\u8da3=趣` (correct: `\u8da5=趟`)  ← 2026-08-25 spathi v0.7
  - `\u5143=元` (correct: `\u4f4d=位`)  SEMANTIC! 五單元 vs 五單位 ← 2026-08-26 starbase v0.7
  - `\u5768=坨` (correct: `\u5862=塢`)  ← 2026-08-26 starbase v0.7 (twice: 船坨)
  - `\u7328=猨` (correct: `\u7329=猩`)  ← 2026-08-26 starbase v0.7
  - `\u9ec4=黄` (correct: `\u9ec3=黃`)  SIMPLIFIED! ← 2026-08-26 starbase v0.7 (twice)
  - `\u8131=脱` (correct: `\u812b=脫`)  VARIANT — traditional strongly prefers 脫 ← 2026-08-26 starbase v0.7
  - `\u57a1=垡` (correct: `\u57ae=垮`)  SEMANTIC! 壓垡 vs 壓垮 ← 2026-08-26 starbase v0.7
  - `\u61c2=懂` (correct: `\u6182=憂`)  ← 2026-08-26 starbase v0.7 (懂特炸彈)
  - `\u5636=嘶` (correct: `\u568e=嚎`)  ← 2026-08-26 starbase v0.7 (電子嘶叫 vs 電子嚎叫)
  - `\u87ec=蟬` (correct: `\u8a20?=蠢`)  ← 2026-08-26 starbase v0.7 (蟬謠言)
  - `\u8ce4=賤` (correct: `\u8cc8=賈`)  ← 2026-08-26 starbase v0.7 (毒賤族 vs 毒賈族)
  - `\u7db3=綳` (correct: `\u7dbb=綻`)  ← 2026-08-26 starbase v0.7 (破綳 vs 破綻)
  - `\u5ac0=嫀` (correct: `\u5acc=嫌`)  SEMANTIC! 不嫀多 vs 不嫌多 ← 2026-08-26 orz v0.5
- **spathi v0.7 lesson**: In a 5-batch audit doing 166 edits via multi_replace with
  \uXXXX, 9 typos slipped through 3 gate iterations before being caught. Two of them
  (彻, 聪) were caught by `_check_zh_purity.py` simp gate. Seven others (喆/躍/迫/唇/
  蠧/膩/砧/啡/諾/鐔/寢/蚻/搯/嘶/趣) are Traditional CJK — pass purity but WRONG WORD.
  User must catch these by re-reading the text — automated gates cannot help.
- **starbase v0.7 lesson**: 10-batch audit with ~96 edits added another 12 hex typos.
  Some were SEMANTIC errors (五單元 vs 五單位, 壓垡 vs 壓垮, 破綳 vs 破綻) that would
  ship as gibberish. **User must always visually re-read every token after
  multi_replace with \uXXXX escapes**. Purity gate catches only simplified chars,
  NOT semantic mistranslations from hex nibble typos.
- **urquan v0.9 lesson (2026-08-26)**: 9-batch audit with 59 semantic edits caught
  5 PRE-EXISTING shipped typos from v0.7 v3 rebuild-compare (2026-08-16):
    - SOUNDS_FAMILIAR 噪夢→噩夢 (SEMANTIC noisy vs nightmare)
    - SOUNDS_FAMILIAR 開啓→開啟 (VARIANT)
    - SUBSEQUENT_URQUAN_WAKE_UP 脱→脫 (VARIANT/SIMPLIFIED)
    - SUBSEQUENT_URQUAN_WAKE_UP 僥倣→僥倖 (SEMANTIC imitation vs fortunate)
    - NO_STOP_MEETING 彿彿→彷彿 (SEMANTIC first-char broken)
  These slipped through v0.7 v3 rebuild-compare AND v0.8 phase-2 refinement AND
  never triggered purity gate. Only manual re-read + typo sweep at end of audit
  caught them.
- **orz v0.5 lesson (2026-08-26)**: 9-batch A 保守派 audit with 58 semantic edits
  had NEW hex typo introduced during batch 6:
    - NEUTRAL_HOMEWORLD_HELLO_1 嫀→嫌 (SEMANTIC \u5ac0 vs \u5acc, agent
      hex nibble typo during multi_replace)
  Caught by post-batch grep sweep before commit. Added to typo pattern list.
  Also: orz has canonical `HYUIVBHJHG` untranslatable dimension verb per dossier
  §5 — v0.5 audit added `（那個維度動詞）` apposition to help CN reader without
  losing canonical joke.
- **arilou v3.1 lesson (2026-08-26)**: 9-batch A 案 (現代美式 UFO 玄學) audit
  with 40 semantic edits. 0 hex typos (all edits used plain-CJK
  multi_replace + replace_string_in_file, avoiding \uXXXX escapes). Key new
  category discoveries:
  1. **Icon 誤用陷阱**: shipped 曾把 ARILOU_HINTS_1『被強行離身』(soul departure /
     dimensional 分魂 icon) 濫用到 HOSTILE_GOODBYE_2「我們拒絕離身」— 此處
     `leave` 只是「離場」。修為「我們並不選擇離去」。**規則**：招牌 icon 詞
     (孤立在 dossier canonical 集裡的) 必須全檔案 grep,確認每處 EN 原文的
     語義都真是那個 icon,否則要退回普通譯法。
  2. **排版 bug（換行位置錯誤）**: shipped ABOUT_TPET L1-2「都花在\n，該怎麼說呢，」
     — `\n` 後緊接逗號,產生斷句 bug。修為「都花在…… 該怎麼說呢……」用
     `……` 順化獨白。**檢查點**：grep `\\n，|\\n。|\\n！|\\n？` 找換行後緊接
     全形標點的錯位。
  3. **星號 icon 生態圈補漏**: EN `*between*` 是玄學星號 icon (與 *time* 同組),
     shipped 譯「彼域」丟失星號。修為「*間隙*」保留 icon。**規則**：EN `*word*`
     必須映射到 ZH `*詞*`,不可只譯文字丟星號。
  4. **register 一致**: EN 用中性 `a survivor`,shipped 譯「一位倖存者」(敬語)
     後接「一隻會話寵」,量詞衝突。修為「一名倖存者」(中性)。
  5. **suspect 弱信心**: `we suspect` = 「推想」不是「懷疑」(後者帶疑心)。
  6. **文法微修**: `just as easily` = 「同樣輕易」不能省 `as`;
     `posture` 雙關取抽象「立場」而非字面「姿態」;
     `discern` = 「看清」不是「揣度」(guess);
     `scoutship` = 「偵察艇」不是「探勘小艇」(prospecting = 採礦探勘)。
- **NEW MANDATORY GATE for future rebuild-compare / re-audit**: Add a final
  hex-typo sweep step BEFORE commit, using the accumulated typo pattern list in
  this memory file (`噪夢|僥倣|彿彿|脱|開啓|俹|膣|喊|顟|矞|脧|裒|悦|喃|喆|躍|
  彻|聪|迫|唇|蠧|膩|砧|啡|諾|鐔|寢|蚻|搯|嘶|趣|五單元|船坨|猨|黄|壓垡|電子嘶叫|
  蟬謠|毒賤|破綳|懂特` etc.). Any hit = must fix or verify context.
- **躍 false positive**: `躍入超空間`= "leap into hyperspace" 太空躍遷術語, 躍 是
  合法繁中字 (\u8e8d, meaning to jump/leap). Only flag typo if not in valid
  hyperspace/leap context. Same char code as recorded typo but usage differs.
- **STRONG PREFERENCE**: For multi-line CJK edits, prefer:
  1. `replace_string_in_file` with actual CJK chars in oldString/newString
  2. PowerShell `$content.Replace('原詞', '新詞')` script — actual chars
  3. AVOID passing long \uXXXX escaped strings through JSON tool params
- **Mandatory post-apply verification** for any batch CJK edit:
  ```powershell
  # Sweep for common typo patterns after multi_replace
  $suspects = @('俹','膣','喊','顟','矞','賤','脧','吐食','雙煦','偏裒','不悦','取悦','脧','喃息')
  foreach ($s in $suspects) { $n = count in file; if $n > 0 → FLAG }
  ```
- **Even simplified chars can get injected** via wrong hex escapes (悦 vs 悅).
  Always sweep for common simplified after batch edits.
