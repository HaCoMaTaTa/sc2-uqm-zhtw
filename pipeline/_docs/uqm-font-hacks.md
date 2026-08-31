# UQM/MegaMod font hacks (Star Control 2 zh-TW project)

> **來源**:此檔案是 `/memories/repo/uqm-font-hacks.md` 的公開鏡射。

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
  - `uqm-work/_selfverify_all.py` — all-NPC pre-flight, imports _dashboard.py

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
