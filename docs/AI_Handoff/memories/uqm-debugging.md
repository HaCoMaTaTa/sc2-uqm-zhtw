# UQM zh-TW debugging protocol

## FIRST STEP: check game.log before anything else
- User standard invocation: `UrQuanMasters.exe --windowed --addon zh-TW --logfile game.log`
- Log path: `Q:\Dos_G\StarControl2\uqm-work\install\game.log`
- When user reports "menu blank" / "text missing" / any visual issue:
  1. `Get-Content game.log -Tail 80` — read the tail first
  2. Search for: `error|fail|warning|not found|missing|undefined|blocking|crash`
  3. Look for font/resource load messages, and last-thing-printed before hang
- User explicitly asked me to remember this (2026-08-05).

## CRITICAL: Preserve Lua template variables in translations
- English source contains `<% state.sis.getShipName() %>`, `<% state.sis.getCaptainName() %>`, `<% comm.getStarName("Vela", "start colony") %>` (interpolated at runtime).
- **NEVER hardcode the captain/ship/star name into the translation** — must
  preserve the `<% ... %>` template EXACTLY (whitespace within `<%...%>` may
  vary but should stay valid Lua).
- Example bug I made: translated `starship <% state.sis.getShipName() %>` as
  `星艦「柯瓦拉號」` (hardcoded from an old save). Correct: `星艦 <% state.sis.getShipName() %>`.
- **Audit workflow before shipping any comm/*.zh-TW.json**:
  ```pwsh
  # Count templates in English source vs translated JSON
  Select-String -Path "extracted/base/base/comm/<race>/<race>.txt" -Pattern "<%" -SimpleMatch | Measure-Object
  Select-String -Path "translations/<race>.zh-TW.json" -Pattern "<%" -SimpleMatch | Measure-Object
  ```
  Counts must match exactly.
- Also verify no Chinese name accidentally hardcoded:
  `grep -E "柯瓦拉|海斯艦長|艦長海斯|恩澤伐特..艦長" translations/*.json`
  (These specific names appear in comm files only via `getShipName()` /
  `getCaptainName()` / `getStarName()` — if you see a Chinese hardcoded
  version, it's a bug.)

## Menu blank symptom checklist
- If gamestrings.txt translation was applied (Applied XX translations) but
  menu still shows blank: FONT problem, not translation problem.
- Verify shadow-content font dir has content:
  `Get-ChildItem "zh-TW-addon\content\base\fonts\playmenu.fon"` — should have PNGs + kerndat.fnt
- Verify kerndat.fnt first-line token matches target dir name (not source):
  `Get-Content "zh-TW-addon\content\base\fonts\playmenu.fon\kerndat.fnt" -First 1`
  should start with `playmenu.fon`, NOT `computer.fon`.

## When translations show as English (not blank, not garbled)
- Check gamestrings.txt in `zh-TW-addon\content\base\` was actually copied to
  the built zh-TW.uqm zip. Sometimes build stage skips files.
- Check menu.c to see which font is used (`optWhichMenu == OPT_PC`).

## KNOWN ENGINE BUG: report.c strlen vs UTF-8 char count
- **File**: `UQM-MegaMod/src/uqm/planets/report.c:353`
- **Bug**: `MakeReport (ReadOutSounds, StrPtr, (COUNT)strlen (StrPtr));`
  passes byte-count, but `MakeReport` internal loop treats `StrLen` as char
  count (decrements by 1 per char). For CJK (3 bytes/char), StrLen residue
  after content = `2 × CJK_chars`. Loop reads past nul → 0xFF garbage bytes
  → thousands of UTF-8 warnings → memory corruption / crash back to menu.
- **Symptom**: lander/energy reports crash with `Warning: Invalid UTF8 sequence`
  spam in game.log; game returns to main menu.
- **PADDING DOES NOT HELP**: Any 1-byte padding stays 1:1 bytes:chars ratio;
  residue never shrinks. Multi-byte padding makes it worse. Mathematical
  proof: for any content with M CJK chars, residue after processing =
  `(bytes) - (chars processed) - (word boundaries)`. Adding P bytes of pure
  ASCII padding adds P bytes AND P chars → residue delta = 0.
- **Only fix**: rebuild MegaMod with source patch:
  ```c
  // OLD (report.c:353):
  MakeReport (ReadOutSounds, StrPtr, (COUNT)strlen (StrPtr));
  // NEW:
  MakeReport (ReadOutSounds, StrPtr, (COUNT)utf8StringCount ((unsigned char *)StrPtr));
  ```
- **Rendering pipeline for lander reports**:
  - `report.c:337`: `SetContextFont(PlanetInfo.LanderFont)` — uses `lander.fon`
  - `LANDER_FONT` resource: `font.lander = FONTRES:base/fonts/lander.fon`
  - Cell grid = `SpaceJunkFrame[18]` size (native 5×5px = orbitbackground-018.png)
  - `NUM_CELL_COLS = 243/7 = 34`, `NUM_CELL_ROWS = 67/6 = 11` (compile-time)
  - Cell frame override (nav/orbitbackground-018/021.png) worked visually but
    doesn't fix the strlen crash.
- **DEFERRED items awaiting patch (Phase 2)**:
  - `translations/lander/moonbase.zh-TW.json` (already written)
  - `build_zh-TW.ps1` Step 2f (commented out at line 62)
  - `package_zh-TW.ps1` `lander.fon` hybrid shadow entry (commented out)
  - 32 more lander/energy/*.txt reports pending translation

## Android Compose overlay: sibling pointerInput z-order competition
- Two sibling `fillMaxSize().pointerInput` composables at the same
  `PointerEventPass.Main` **compete**; only the one higher in z-order
  actually gets events. Lower sibling event-starves.
- Symptom (v1.4): pinch-to-zoom stopped firing on star map after adding
  StarMapClickDetector as sibling to PinchZoomDetector.
- Fix (v1.5): merge into single `TapAndPinchDetector` that branches on
  pointer count: `>=2 pressed` → pinch, `1 touched` → tap, else idle.
- **Gotcha**: when filtering `event.changes`, use TWO views:
  - `pressed = filter { it.pressed && !it.isConsumed }` for pinch counting
    (must be down)
  - `touched = filter { !it.isConsumed }` for tap tracking (must see
    release transition where `pressed=false`)
  Filtering only by `it.pressed` drops the `ACTION_UP` change, so tap
  release never fires.
- File: `build/android/composeApp/src/androidMain/kotlin/org/megamod/uqm/TouchOverlay.kt`
  `private fun TapAndPinchDetector()` @ line ~610

## AGP gotcha: buildType.ndk.abiFilters is UNIONED, not overriding
- Setting `buildTypes.release.ndk.abiFilters = ["arm64-v8a"]` does NOT
  restrict release to arm64. It gets UNIONED with defaultConfig's
  abiFilters. If defaultConfig lists both, release ships both.
- Symptom: `configureCMakeRelWithDebInfo[arm64-v8a]` runs, but the final
  APK still contains `lib/x86_64/*.so` (packaged from prior debug build
  outputs on disk).
- Reliable fix (v2.0-release): add packaging-level exclude inside the
  release buildType:
  ```kotlin
  buildTypes.getByName("release") {
      packaging {
          jniLibs {
              excludes += "lib/x86_64/**"
          }
      }
  }
  ```

## Android release build: lintVitalRelease blocks on FullBackupContent
- `<full-backup-content>` is a WHITELIST. `<exclude>` sibling paths NOT
  under an `<include>` fire the `FullBackupContent` lint error at
  `lintVitalRelease` (blocks assembleRelease).
- Fix: remove redundant `<exclude>` tags — anything not under an
  `<include>` is implicitly excluded already.
- Same rule for `<data-extraction-rules>` (Android 12+).

## Android APK size ceiling: content packs are the wall
- Debug (v1.4, both ABIs, unstripped, no minify): 404 MB
- Release (v2.0, arm64 only, stripped, R8): 382 MB
- The 22 MB gap is R8 dex shrink + strip DWARF + drop x86_64 .so
- The remaining 374 MB is `uqm-content/` (HD assets + 3DO voice + zh-TW
  fonts). Further shrink requires removing content packs, not build
  tuning.

## Release keystore workflow (uqm-zh-tw)
- Keystore: `Q:\Dos_G\StarControl2\Android\keystore\uqm-zh-tw.jks`
  (OUT of repo — losing it means never being able to publish upgrades)
- Alias: `uqm-zh-tw`, validity 50 years, RSA 2048
- Local password config: `build/android/keystore.properties`
  (gitignored; template is `keystore.properties.example`)
- Gradle silently falls back to debug signing if properties missing or
  contain `CHANGE_ME` placeholder.
- **v1.x (debug-signed) will NOT upgrade to v2.0-release** on-device —
  Android rejects install on signature mismatch. Must uninstall v1.x
  first, then install v2.0-release. From v2.0 onwards upgrades are clean.

## zh-TW gamestrings.txt indices ARE ALIGNED (corrected 2026-08-25)
- **Earlier "index misalignment" diagnosis was WRONG.** I counted non-blank
  non-comment lines, but multi-line values (e.g. `#(NoQuickSave)` value
  spans 3 lines in base, 2 in zh-TW) inflated my counts and created fake
  deltas.
- **Correct method**: `src/libs/strings/getstr.c:294` — each line
  starting with `#` does `slen[++stringI] = 0;`. String index = COUNT OF
  `#(header)` markers, regardless of how many lines each value has.
- Verified 2026-08-25 with proper counting: all 24 segments from
  STAR_STRING_BASE through TDO_MENU_STRING_BASE match perfectly between
  MegaMod 0.8.5 base and zh-TW addon. LABEL section differs (11 vs 370)
  but that's intentional padding to land STAR_POSTFIX_ZH_BASE at
  absolute index 1024 per gamestr.h.
- **"Empty Slot" showing English** in save-load menu is NOT index drift —
  the addon simply has value = "Empty Slot" (untranslated by design).
- **"ENCOUNTER IN Deep Space" in English** on encounter dialog: fixed
  in 8/25 addon commit e2b36ff (SHA256 b05c8c5f...4aef). If still English
  on-device, the extractor cached an older version — force uninstall +
  reinstall to trigger re-extraction.
- v2.3 APK (2026-08-25) contains the correct addon SHA256; no rebuild
  needed.

## Android star-map contextual UI (v2.2 + v2.3)
- pstarmap.c exposes `int uqmStarMapOpen` (set/cleared at StarMap()
  entry/exit) + helper `int uqmGetCurrentActivityLoByte(void)` that
  wraps LOBYTE(GLOBAL(CurrentActivity)) — avoids pulling uqm/globdata.h
  into the out-of-tree android_virtual_joystick.c.
- android_virtual_joystick.c: `Java_..._nativeIsStarMapOpen` (jboolean),
  `Java_..._nativeCurrentActivity` (jint). Polled ~7 Hz.
- Kotlin ACTIVITY_* constants mirror src/uqm/globdata.h enum.
- Direct-star-map button (folded paper map icon, drawn via Canvas)
  appears at TopEnd padding(end=128dp) when activity==3 or 4 AND
  !starMapOpen. On tap: `SDLActivity.onNativeKeyDown/Up ESCAPE` then
  80ms delay then ENTER. Both HyperspaceMenu and Interplanetary
  auto-menu default cursor to STARMAP so the sequence lands cleanly.
- Contextual [SEARCH][MAP_SWITCH][MINUS][PLUS] cluster at TopEnd
  padding(end=24dp) when starMapOpen — Thrust is hidden then so no
  overlap.
- **Layout gotcha**: on ~400dp-tall landscape phones, bottom-right
  column top-edge climbs into top-right corner Y range. Direct button
  end padding=128dp keeps it left of Thrust column X range (which ends
  at end=36+84=120dp).
- **Encounter edge case**: in encounter dialog the activity may still
  be IN_HYPERSPACE but the ESC+ENTER sequence is intercepted by the
  encounter dialog UI (opens ship-select). Not yet handled.
