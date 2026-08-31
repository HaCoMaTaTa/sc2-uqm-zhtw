# UQM/MegaMod font hacks (Star Control 2 zh-TW project)

## Star map / hyperspace top-header ZH pattern (patches 009 + 011)
- gamestrings.txt STAR_STRING_BASE (0-148) holds cluster postfix strings (Aurigae,
  Sol, Vega, ..., Falayalaralfali, `UNKNOWN`, 15 waypoint coord strings).
- Engine builds cluster name via `GetClusterName(pSD, buf)` in starmap.c:126:
  `<GAME_STRING(STAR_NUMBER_BASE + Prefix - 1)> ' ' <GAME_STRING(Postfix)>`
- **patch 009** adds parallel `STAR_POSTFIX_ZH_BASE = 1024` (149 zh entries appended
  by `_append_star_postfix_zh.py`) and new function `GetClusterNameLocalized()` that
  reads zh postfix but falls back to English if entry NULL/empty. Format: `English（中文）`.
- **STAR_POSTFIX_ZH_BASE = 1024 fixed** (not chained via LABEL_STRING_BASE +
  LABEL_STRING_COUNT) — content packs vary 813-816 entries, so fixed absolute index
  with build-time padding is safer than compile-time chain.
- Patched call sites (English → Localized), one-line swaps in each:
  - **sis.c:285** (IN_INTERPLANETARY / IN_LAST_BATTLE top header) — patch 009
  - **encount.c:379** (ENCOUNTER-AT screen) — patch 009
  - **pstarmap.c:1812** (star-map cursor-hover top-center header) — patch 011
- Left English intentionally (star-map cross-ref + F6 search work):
  - pstarmap.c:1812 → 2190 area (star-map bottom info panel)
  - pstarmap.c:2140 `FindNextStarIndex` (F6 search reads raw `SDPtr->Postfix`)
  - sis.c:1958 (save-load position label)
  - gameopt.c:1419 (game-menu current location)
- **Rule**: dialog Lua `comm.getStarName / getConstellation` in vanilla !StarSeed mode
  returns first arg literally — does NOT call GetClusterName. So patch 009 does NOT
  affect any dialog rendering.

## Race sphere-of-influence (SoI) zh labels (patch 010)
- Each race has `ships/<race>/<file>.txt` StringTable resource loaded into
  `race_strings`. Engine reads:
  - `race_strings[0]` = full name (e.g. `Ariloulaleelay`) — used only in Androsynth
    war-era map special case (pstarmap.c:1247). Kept English.
  - `race_strings[1]` = long label — **star map SoI + hover tooltip + combat/melee
    ship-stat header + encounter dialog race header**. Replaced with zh (patch 010).
  - `race_strings[2]` = ship class (Dreadnought). Kept English.
  - `race_strings[3+]` = captain names + description. Kept English.
- **Implementation**: pure addon shadow-content — no engine patch. Copy each
  ships/<race>/<file>.txt to `zh-TW-addon/content/base/ships/<race>/<file>.txt`,
  swap only 2nd entry's content line. See `_apply_race_zh_labels.py`.
- `zh-TW-addon/content/base/` is auto-recursively copied by package_zh-TW.ps1 into
  shadow-content — new race files ride along without package script changes.
- **Yehat Rebels edge case**: pstarmap.c:1262 uses **hardcoded C string**
  `yehat_rebels` (7 chars "REBELS ") for civil-war SoI label — not loaded from .txt.
  Would need engine patch. Deferred; kept "REBELS" English.
- **VUX kept English** per Master_Glossary canonical (no zh race name established).

## `|-N|` inline layout tag in gamestrings.txt (LABEL section)
- Syntax: `|-2|WORD1 |-1|WORD2` = draw WORD1 with -2 baseline offset, then WORD2 with -1
- Purpose: stacks label into multiple rows (e.g., SIS cargo `AMPLIFIED PRECURSOR BOMB`
  displays as 3-line vertical `AMPLIFIED / PRECURSOR / BOMB`).
- **CRITICAL**: If label.fon is disabled/redirected AND the string keeps `|-N|`,
  the `|` renders as literal ASCII char and CJK fallback maps it to `一` (one).
- Also: writing translated string in a shape that changes byte layout can
  **shift all subsequent gamestrings.txt line numbers by 1**, causing main
  menu labels to swap by 1 (`Load Game`→New Game etc). Diagnosis by bisect.
- 2026-08-14 case: `AMPLIFIED PRECURSOR BOMB` = `|-2|AMPLIFIED PRECURSOR |-1|BOMB`.
  Chinese B-format = `|-2|增幅先驅者 |-1|炸彈` (preserve tags + space).
  Fallback C-format = `增幅先驅者炸彈` (single line, if B still renders wrong).

## Font kerndat.fnt name-token MUST match directory name
- Font at `base/fonts/foo.fon/` → `kerndat.fnt` first line MUST start with `foo.fon`.
- If you copy `base/fonts/A.fon/` content into `base/fonts/B.fon/` (font-size hack),
  you MUST rewrite `B.fon/kerndat.fnt` first token to `B.fon` else engine crashes
  with "renderer thread blocking on DCQ" when speaker whose font key resolves to B is triggered.
- Automated in `uqm-work/package_zh-TW.ps1` via `$fontRedirects` block.

## `comm.<race>.font` RMP override does NOT work
- Adding `comm.commander.font = FONTRES:base/fonts/computer.fon` in addon uqm.rmp
  causes `Trying to get undefined resource 'comm.commander.<something>'` crashes.
- The engine doesn't accept RMP-level font key remapping for `comm.*` speakers.
- Solution: use shadow-content directory replacement instead (see above).

## Addon shadow-content override structure
- Zip root: `<addon_name>/uqm.rmp` (required for loadAddon to accept it, even if empty)
- Overrides: `<addon_name>/shadow-content/base/<any_path>` — mounted with uio_MOUNT_ABOVE
  on top of base pack, so any file here overrides the same-path base file.
- Source: `prepareShadowAddons()` in `src/options.c` of UQM-MegaMod.

## Fonts too small for CJK glyphs (< 14 px reference PNG height)
| Font          | Latin | UI role (verified by menu.c) |
|---------------|-------|-----------------------------|
| commander.fon | 9 px  | Hayes NPC dialog — redirect to computer.fon |
| player.fon    | 10 px | Player response menu — redirect to computer.fon |
| starcon.fon   | 7 px  | **DrawPCMenu StarConFont** (PC 模式命令選單) + 頂部 "Difficulty:" 標題 |
| playmenu.fon  | 11 px | **Draw3DOMenuText PlayMenuFont** (3DO 模式命令選單) — 使用者用 PC 模式時不需要 |
| label.fon     | 10 px | 面板標題 CARGO/DEVICES/CAPTAIN — shadow 會放大 |
| tiny*.fon     | 7 px  | 小標籤（存檔列日期用這個）|
| micro*.fon    | 11 px | Very small (druuge/melnorme) |
| arilou.fon    | 9 px  | Arilou dialog |
| chmmr.fon     | 10 px | Chmmr dialog |
| umgah.fon     | 8 px  | Umgah dialog |

## PC menu mode uses starcon.fon, NOT playmenu.fon
- `menu.c DrawPCMenu`: `SetContextFont(StarConFont)` = starcon.fon (7px native)
- `menu.c Draw3DOMenuText`: `SetContextFont(PlayMenuFont)` = playmenu.fon (11px native)
- `DrawMenuStateStrings` picks based on `optWhichMenu == OPT_PC`
- **This user runs PC mode** — vertical stacked list of menu items in right-bottom.
- shadow `starcon.fon → computer.fon (15px)` MAKES menu Chinese visible but text overflows
  the PC_MENU_HEIGHT = RES_SCALE(8) slot heavily.

## CJK-viable fonts (rasterize CJK into these)
- slab.fon (34), slides.fon (20), urquan.fon (16), utwig.fon (18),
  syreen.fon (17), kohrah.fon (16), shofixti.fon (16), spathi.fon (15),
  mycon.fon (15), orz.fon (15), computer.fon (15), pkunk.fon (14),
  slylandro.fon (14), yehat.fon (14)

## Line-count safety net for dialog files
- `translate_ui.py` has `--allow-line-mismatch` flag (default: strict).
- **UI/setup files**: use STRICT (default). SUBTITLES/CHOICES/BUTTONS are
  structured arrays that will PANIC the engine on line-count mismatch.
- **Comm dialog files** (`comm/*/*.txt`): CAN use `--allow-line-mismatch` for
  emergency wrapping, BUT strongly prefer keeping same `\n` count as English
  and use ASCII SPACES within lines for CJK word-wrap (see space-wrap section).
  Reason: each `\n` = one SplitSubPages page = one audio slice offset. Extra
  pages force `SoundDecoder_Load()` past OGG EOF for later pages.

## CRITICAL: kerndat.fnt CharSpace field
- `kerndat.fnt` first-line fields: `<name> <Leading> <CharSpace> <KernAmount> <VertAlign>`
- Source: gfxload.c `_GetFontData()` sscanf `"%s %hhu %hhu %hhu %hhd"`.
- **`CharSpace = 2` for commander.fon** (from "commander.fon 14 2 1 4").
  Common oversight: assuming 1. Off-by-one per char × N chars = significant.
- `TextRect` computes width: `sum(disp.width + CharSpace) - CharSpace` (trailing).
- Always verify by reading actual kerndat before validating CJK line widths.

## Space-wrap validator: simulate _count_lines() exactly
- Simple "each word < text_width" check is INSUFFICIENT because SplitSubPages
  adds `...` lead/trail overhead (~28px for commander.fon at CharSpace=2).
- Chunks without spaces (single "word" per line) that ALMOST fit but exceed
  once ellipsis is added trigger infinite loop.
- **`uqm-work/_simulate_count_lines.py`** — reproduces engine's do-while loop
  with actual `getLineWithinWidth()` behavior. Detects if `pStr` fails to
  advance (revisited offset → INFINITE_LOOP). MUST run before packaging any
  CJK comm dialog translation.
- If a single-word line (no space) approaches AlienTextWidth,
  it MUST have at least one internal space (word boundary) for engine to break.

## CRITICAL: sim glyph widths MUST come from PACKAGED addon
- **Wrong**: reading glyph widths from `zh-TW-addon/_stage/` — this folder is
  deleted between builds and doesn't exist during validation. Any missing PNG
  falls back to a placeholder width (e.g. 8px) → sim silently under-estimates
  every CJK char → false-negatives (misses real infinite-loop pages).
- **Right**: read from `install/content/addons/zh-TW.uqm` (the packaged zip).
  This is what the game actually loads. Sim must print warning if any char
  falls back to placeholder width.
- **Workflow**: `build → package → sim` (sim reads from zip). NEVER `build → sim`
  without package in between, because widths sim sees will be wrong.
- Track `_missing` set in sim; if non-empty, DO NOT trust "0 infinite loops".

## PC menu (starcon.fon) glyph positioning — HARD-WON knowledge
- `HotSpot.y = png_height - VertAlign` (gfxload.c:147). So PNG_bottom = baseline.
- `DrawPCMenu` (menu.c) advances `t.baseline.y += PC_MENU_HEIGHT` = RES_SCALE(8).
- Highlight rect: `r.corner.y = baseline_y - PC_MENU_HEIGHT + 2`, height = 7.
  → highlight covers screen rows [baseline_y - 6, baseline_y + 1].
- **Adjacent items overlap = max(0, ink_rows - PC_MENU_HEIGHT)**. Can't avoid
  without either reducing ink or recompiling (PC_MENU_HEIGHT is hardcoded).
- For ink to visually fit inside highlight: ink ≤ 7 rows tall AND positioned
  at PNG rows [png_height-8, png_height-2] approx.
- **Font size choice for PC menu CJK**:
  - 15px Fusion (native) → 7-row overlap, ink extends way above/below highlight
  - 12px Fusion → 4-row overlap, still misaligned
  - 10px Fusion → 2-row overlap, tolerable
  - **8px Fusion (final v0.4.19)** → ink 7 rows, PC_MENU_HEIGHT=8 → **1 row gap**
    and ink aligns nicely with highlight. Very small but readable pixel-art.
- Rasterize params: `--font-size 8 --png-height 10 --latin-bottom 9 --no-aa`.

## CJK Pixel bitmap fonts — coverage & choice matrix
| Font                          | Design | Coverage | Menu 58/58 |
|-------------------------------|--------|----------|------------|
| Ark Pixel 10px zh_tw          | 10 px  | 4252     | 22/58 ❌ (thin coverage) |
| Cubic 11 (ACh-K)              | 11 px  | 10268    | 58/58 ✓ (but thin strokes) |
| **Fusion Pixel 8px zh_hant**  | 8 px   | 27976    | 58/58 ✓ (**used**, aligns) |
| Fusion Pixel 10px zh_hant     | 10 px  | 25069    | 58/58 ✓ (crisp but 2px overlap) |
| Fusion Pixel 12px zh_hant     | 12 px  | 25000+   | 58/58 ✓ (best clarity, 4px overlap) |
- Downloaded to `uqm-work/_downloads/{ark-pixel-10px,fusion-pixel-{8,10,12}px,Cubic_11.ttf}/`.
- rasterize_font.py has `--no-aa` + `--png-height` + `--latin-top/bottom`
  overrides specifically for pixel-font placement control.

## FUTURE OPTIMIZATION: PC menu CJK legibility (backlog)
- Fusion Pixel 8px is **at the readability edge**. Complex chars (讀, 離, 戲)
  look like abstract symbols to some users.
- **Option F** (change setup config `optWhichMenu=OPT_3DO`): use 3DO menu style
  which draws single centered label with playmenu.fon (11px shadow → 15px).
  Would use Fusion Pixel 12 native → beautiful CJK, no overlap since only 1
  label shown at a time. Player loses vertical menu-item overview.
- **Option C** (recompile UQM): change `#define PC_MENU_HEIGHT (RES_SCALE(8))`
  to `RES_SCALE(11)` in menu.c. Then use Fusion 10px CJK. Clean solution but
  needs MSYS2/mingw build environment.
- User accepted current 8px result (v0.4.19) as "acceptable" 2026-08-05.
  Marked as backlog optimization.

## Common overwidth patterns to watch (~150px triggers @ AlienTextWidth=143)
- **Single-word CJK line ending with non-ASCII punct + auto-added `...`**
  Example: `放射性元素礦床。...` (7 CJK + 1 punct + 3 dots = 154px)
  → Fix: split before punct with space, e.g. `放射性元素 礦床。`.
- **Line beginning with lead ellipsis + long word**
  Example: `...我方透過望遠鏡` (3 dots + 6 CJK = 146px, barely over)
  → Fix: split first word, or prefix with short CJK word to absorb `...`.
- **Any 8+ CJK contiguous chars** (8*17 + 7*2 = 150 > 143) — ALWAYS split.

## CRITICAL: comm.c _count_lines() infinite loop with wide CJK "words"
- `commander_desc.AlienTextWidth = RES_SCALE(143)` (px, SD mode; other races vary).
- `commander_desc.AlienTextValign = VALIGN_MIDDLE` triggers `_count_lines()`.
- `_count_lines()` calls `getLineWithinWidth()` which breaks at spaces.
- **CJK has no spaces** → whole line is one "word".
- When CJK "word" width >= AlienTextWidth: `getLineWithinWidth` returns FALSE
  but does NOT advance pStr → `_count_lines` do-while loops forever with
  `BatchGraphics()` holding DCQ mutex → renderer thread deadlocked → fatal error.
- **Symptom**: voice plays fine (`commander-XXX.ogg`), THEN crash with fatal
  error dialog; log shows `Thread 'Unknown' blocking on 'DCQ'`.
- **BEST solution: space-wrap** — insert ASCII spaces between CJK chunks within
  each line. Keeps English's `\n` count for voice cue timing (SplitSubPages
  splits on \n → each page = one voice segment), and spaces let
  getLineWithinWidth do proper word-wrap. Works perfectly with NPC dialog.
- **Second fallback: many `\n`** (works but has TWO caveats — see next section).
- **Validators**:
  - `uqm-work/_verify_line_widths.py` — checks each \n-delimited line
  - `uqm-work/_verify_space_wrap.py` — checks each space-delimited word
  - `uqm-work/_verify_v032.py` — final packaged addon check (widths + line counts)

## CRITICAL: SplitSubPages() page fragmentation from extra \n
- `libs/sound/trackplayer.c:SplitSubPages()` splits comm text on `\r\n`.
- Each page = one audio slice (`SoundDecoder_Load(TrackName, offset, duration)`).
- Duration is `chars * TEXT_SPEED (80ms)`, min 1000ms per page.
- If you insert many `\n` for CJK wrapping, you multiply the page count →
  the OGG file gets sliced into many chunks with cumulative offsets.
- When N pages exceed available audio duration, some decoders load past EOF.
- **Second symptom**: crash AFTER first subtitle displays but voice ends.
- **ADDITIONAL BUG**: SplitSubPages uses `ispunct(text[pos-1])` and
  `isspace(text[pos-1])` on the LAST BYTE (not codepoint). Fullwidth CJK
  punctuation like `！ ？ ， 。` in UTF-8 has last byte 0x81/0x8C etc. —
  NEVER matches ASCII ispunct/isspace → engine ADDS "..." lead/trail to
  every intermediate page. This inflates line width by ~20px.
- **Solution**: keep the SAME `\n` count as English original. Use SPACES
  (ASCII 0x20) within lines for word-wrap.

## Space-wrap methodology for CJK comm dialog
- Preserve English's `\n` count exactly (voice cue alignment).
- Within each line, group CJK into ~4-6 char chunks separated by ASCII spaces.
- Each space-delimited chunk must fit `AlienTextWidth - 20` (~120px for
  commander) since SplitSubPages adds "..." lead/trail.
- Example: `"警告！ 身分不明 星艦！\n我是 地球奴隸行星 星際基地 指揮官海斯。"`
- Lua templates `<%...%>` should be their own space-delimited word.
- Captain name via `<% state.sis.getCaptainName() %>` interpolates to 4-15 ASCII
  chars at runtime (assume max 15 for validation).

## CRITICAL: Lua template first-argument CJK-ify requirement
- `commfuncs.c:487-570` defines three helpers used in comm dialog:
  - `comm.getColor(prime, plot)` — color name for star/planet
  - `comm.getConstellation(prime, plot)` — constellation reference
  - `comm.swapIfSeeded(A, B)` — swap for randomized starmap
- In `!StarSeed` (default vanilla) build path, ALL THREE return the FIRST
  argument LITERALLY. `plot` / `B` args are ONLY used when `StarSeed=true`.
- **Consequence**: `<% comm.getColor("blue", "rainbow 4") %>` renders as
  literal English `blue` in-game when StarSeed=false. Same for
  `comm.getConstellation("blue star", "rainbow 4")` → `blue star`,
  `comm.swapIfSeeded("一顆 ", "一對 ")` → `一顆 `.
- **Fix**: replace English first arg with CJK equivalent:
  - `comm.getColor("blue", ...)` → `comm.getColor("藍色", ...)`
  - `comm.getColor("white", ...)` → `comm.getColor("白色", ...)`
  - `comm.getConstellation("blue star", ...)` → `comm.getConstellation("藍色恆星", ...)`
- swapIfSeeded first arg is fine if already CJK.
- **Symptom**: dialog looks correct in extracted `.txt` file, but
  fragment English word leaks through in-game.
- **Diagnostic**: `Select-String -Pattern 'getColor\("[a-z]|getConstellation\("[a-z]' translations/*.zh-TW.json`
- Verified fix landed in commit `fd1f3cf` (slylandro retrofit 2026-08-06).

## CRITICAL: MegaMod UIO does NOT support Zip64 (addon fails silently) — FIXED in patch 007
- Symptom (original exe): game runs but everything shows in English. Log shows:
  - `Error: Zip64 .zip files are not supported.`
  - `Warning: Could not mount 'zh-TW.uqm': Function not implemented.`
  - `0 available addon packs.` → `Warning: Addon 'zh-TW' not found`
- Root cause: PowerShell `Compress-Archive` (and 7z) auto-switch to Zip64 when:
  - Entry count > 65,535 files
  - Individual file > 4 GB
  - Total archive > 4 GB
- **In this project**: at ~29 CJK-carrying fonts × ~2880 PNGs = ~83,000 files,
  the threshold is exceeded. Vux/mycon/utwig rasterization added Round 2 → over.

### FIX (2026-08-10) — patch 007-uio-zip64-eocd.patch
Modifies MegaMod source (`src/libs/uio/{types.h,uioutils.h,zip/zip.c}`) to add
Zip64 EOCD Record parsing (~50 LoC). Build output: `UrQuanMasters-zip64.exe`
(parallel to original `UrQuanMasters.exe`).

- **Verified**: Zip64 addon (83,706 entries) mounts successfully.
- **Regression tested**: ZIP32 addon + ZIP32 base pack still work.
- **Launch**: `install/UrQuanMasters-zip64.exe --windowed --addon zh-TW`
- **Original exe preserved** for rollback (2026-08-06 build).
- **package_zh-TW.ps1** auto-detects Zip64 via EOCD signature scan and
  prints appropriate message (recommend patched exe if Zip64, or ZIP32
  fallback via `-SkipHybridUI`).

### Fallback (if patched exe unusable): -SkipHybridUI
`package_zh-TW.ps1 -SkipHybridUI` drops 7 hybrid UI font redirects
(starcon/tiny/tiny.bold/tiny.cond/micro/label/lander) → saves ~20K files
→ total ~63,576 files < 65,535 limit → ZIP32 preserved → original exe mounts.
Impact: UI panels (cargo/devices/planet-info/lander/setup) revert to English.
Dialog + main menu + slides + rasterized dialog fonts all remain Chinese.


## 單字增補：_patch_hd_add_char.py（免全量重建）
- 情境：譯文只多出 1-2 個新 CJK 字，全量跑 `_build_hd_fonts.ps1` (~15 分鐘) 過重
- 用法：`python _patch_hd_add_char.py 橢` — 對 39 個 HD 已 stage 字型逐一：
  1. 用同一個 ref-font（含 pkunk +10 vertShift、UI 字型 0.85 cjk-scale）
  2. rasterize_font.py `--chars <字>` 到 temp dir
  3. 只複製產生的 `<lowercase_hex>.png` 到 `_stage_hd_fonts/<font>/`
- **不需改 kerndat.fnt**：rasterize_font.py 也不會為新 CJK 加 advance 條目，
  引擎依 PNG 寬度預設 advance。
- 完成後直接跑 `_package_hd_addon.ps1` 打包 zh-TW-hd.uqm。
- **實測 2026-08-14**: Setup CAT DESC 「橢」補 39 字型 ≈ 15 秒，比全量快 60x。

## CRITICAL: HD 字型改動要改 zh-TW-hd.uqm，不是 zh-TW.uqm
- Addon 掛載順序 (低→高覆蓋): base → mm-hd → zh-TW → zh-TW-hd
- **HD 模式時 zh-TW-hd 覆蓋一切**，改 zh-TW/base/fonts 對 HD 完全無效
- SD 字型 build: `build_zh-TW.ps1` → `zh-TW.uqm`
- HD 字型 build: `_build_hd_fonts.ps1` → `_stage_hd_fonts/` → `_package_hd_addon.ps1` → `zh-TW-hd.uqm`
- **教訓 2026-08-13**: 花了半個 session 改 SD pkunk.fon 但使用者玩 HD 完全沒感覺
- **未來檢查清單**: 改字型前必問使用者玩 SD/HD/3DO 哪個
- 詳細指引在 `uqm-work/AI_BUILD_GUIDE.md`

## 修對話 top-clipping: 用 kerndat VertAlign shift 而非 cjk-scale
- `--cjk-scale 0.85` 縮 CJK 字大小 → 可讓某些字不溢出但**字變小難讀**
- `--vertalign-adjust N` 直接下移 baseline → **保持字大小**，只把整體下移 N 像素
- HotSpot.y = png_h - VertAlign; ↑VertAlign → ↓HotSpot.y → glyphs draw N rows lower
- **HD pkunk +10 實測成功** (VA 0→10) — 對話上緣呼吸空間與 Hayes 一致
- 副作用: 底部行間可能疊到 (cell_h < PNG_h 時)，但 CJK descender 通常空白，實測 OK
- 常見的 top-clip 對話字元 (需 shift): 我/普/族/首/高/最 (皆有 ascender 上突筆畫)

## CRITICAL: CJK scan report infinite loop + cell size mixup — patch 008
- **Symptom 1 (INFINITE HANG)**: HD lander scan report with CJK text hangs at
  last-page Enter. Debug logs show StrLen stuck at same value while user
  presses Enter repeatedly, [MORE] never advances.
- **Symptom 2 (page-count explosion)**: Same report shows only 2-3 content
  lines per page + [MORE] on HD, requiring 8+ pages for what should be 3.
- **Root cause 1**: `report.c:MakeReport()` word-scan loop
  `while (UniChar_isGraph (...)) pStr = pNextStr` treats entire CJK line as
  one giant "word" (no ASCII space separators). When word_chars > NUM_CELL_COLS,
  `if ((col_cells += word_chars) <= NUM_CELL_COLS)` skips → StrLen never
  decrements → outer `while (StrLen)` infinite loops.
- **Root cause 2**: zh-TW dynamic cell-count calc mixed scales — used
  HD-scaled `frameRect.extent` divided by unscaled `UQM_MAP_WIDTH` /
  `SC2_MAP_HEIGHT` → NUM_CELL_ROWS clamped to minimum 3.

### FIX (2026-08-13) — patch 008 in report.c
1. Cap word_scan at `NUM_CELL_COLS - col_cells` (remaining row space) so CJK
   forces character-wrapping at cell boundaries.
2. `RES_DESCALE()` the frameRect extents in cell-count calc to keep division
   in unscaled space matching original `COL_MULTIPLIER` design (5-6 rows,
   27 cols for 8x10 zh-TW override cell).
3. Defensive `FlushGraphics()` + unbatch before/after `DrawStamp(&saveStamp)`
   restore to keep DCQ pipeline clean.

- **Impact**: Only affects lander scan reports (report.c). Currently only Luna
  moonbase.txt + urquanbase.txt are CJK-translated but ALL future lander
  scan translations (spathimonument, fwiffo, chmmrbase, etc.) need this fix.
- **NOT affected**: comm dialog (uses comm.c, separate word-wrap — see
  `_count_lines` section above).
- **Verified**: Luna moonbase scan displays 5-6 lines per page, ends normally.
- **Debug trace approach**: added `log_add(log_Warning, "[zhtw-report] ...")`
  at each DoDiscoveryReport step + MakeReport page break — invaluable for
  pinpointing exact hang location. Reverted before commit but keep this
  approach in mind for future MegaMod source-level debugging.
- **Commit**: `21f3316 zh-TW patch 008: fix CJK scan report hang + cell size mismatch`
- **Build env**: MSYS2 mingw32 (`C:\msys64\mingw32\bin`), ninja,
  `$env:PATH = "C:\msys64\mingw32\bin;C:\msys64\usr\bin;$env:PATH"` required
  or ninja invokes cc.exe but child processes can't find MSYS DLLs.
