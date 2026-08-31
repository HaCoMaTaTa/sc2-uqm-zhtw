# zh-TW MegaMod patches (independent, apply order: 001, 002)

These patches modify `UQM-MegaMod` source to support CJK (Traditional Chinese) content.
Each patch is minimal and independently reversible. Apply with `git apply patches/NNN-*.patch` from the MegaMod source root.

## 001-report-cjk-fixes.patch

Two fixes to `src/uqm/planets/report.c` (the lander/energy discovery reports):

### 001a. strlen → utf8StringCount for MakeReport
The `MakeReport` internal loop treats `StrLen` as a UTF-8 character count (decrement per char) but the call site passes `strlen(StrPtr)` which is a byte count. For CJK (3 bytes/char) this creates a residue of `2 × CJK_chars` after the string ends. Loop then reads past nul into memory → thousands of UTF-8 warnings → memory corruption / game exit.

Fix: pass `utf8StringCount(StrPtr)` instead of `strlen(StrPtr)`.

### 001b. Adaptive cell grid size
Report renders text on a fixed 34×11 cell grid whose step is derived from `SpaceJunkFrame[18]` (`nav/orbitbackground-018.png`) which is natively 5×5px. When an addon overrides that PNG to a bigger size for CJK glyph breathing room (e.g. 8×10), the 34-cols × new step overflows the report display area.

Fix: at the start of `MakeReport`, recompute cell col/row counts from the frame's actual `extent.width/height + 1` so that any override PNG stays within the display bounds.

## 002-gamestr-elements-count-june-content.patch

`src/uqm/gamestr.h`: revert `ELEMENTS_STRING_COUNT` from 135 back to 133.

Upstream commit `7c392b5` (Kruzen, 2026-07-06 — "New floating message above lander in playable area if its cargo or data bank is full") added 2 new element strings and bumped this count. But the packaged content pack `mm-0.8.5-content.uqm` (dated 2026-06-06) predates that commit and only contains 133 element strings. The mismatch shifts every subsequent `_STRING_BASE` by +2, causing e.g. the main menu to skip "New Game" and "Load Game" and instead bleed Netplay banner text (`Awaiting incoming connection...`) where those items should appear.

Fix: match the content pack.

**When to remove this patch**: when the packaged content pack is updated to include the 2 new element strings (probably in MegaMod 0.8.6+).

---

## How to apply from a fresh clone

```bash
cd UQM-MegaMod
git apply patches/001-report-cjk-fixes.patch
git apply patches/002-gamestr-elements-count-june-content.patch

# then MSYS2 MINGW32 build (see repo/uqm-build.md)
cmake . -G Ninja -DUQM_PLATFORM_ACCEL=OFF -DCMAKE_BUILD_TYPE=Release && ninja
```

## 007-uio-zip64-eocd.patch

`src/libs/uio/types.h` + `src/libs/uio/uioutils.h` + `src/libs/uio/zip/zip.c`: add Zip64 EOCD Record support to UIO's zip mount layer.

### Symptom

zh-TW addon with **> 65,535 entries** (triggered by rasterizing many CJK-carrying fonts) is silently packed as Zip64 by PowerShell `Compress-Archive` and 7-Zip. UIO refuses to mount:

```
Error: Zip64 .zip files are not supported.
Warning: Could not mount 'zh-TW.uqm': Function not implemented.
0 available addon packs.
```

Root cause: `zip_fillDirStructureCentral()` in `zip.c` reads the standard EOCD's 16-bit `numEntries` field. When entry count > 65535, ZIP producers set this to the Zip64 sentinel `0xFFFF` and store the real count in a Zip64 EOCD Record. The original code aborts on the sentinel instead of reading Zip64.

### Fix

1. `types.h`: add `uio_uint64` / `uio_sint64` type aliases (`unsigned long long`).
2. `uioutils.h`: add `makeUInt64()` inline helper (8-byte little-endian to uio_uint64).
3. `zip.c` `zip_fillDirStructureCentral()`:
   - Widen `numEntries` from `uio_uint16` → `uio_uint64`.
   - When standard EOCD reports 0xFFFF entries or 0xFFFFFFFF CD offset, fall back to reading Zip64 EOCD Locator (20 bytes before std EOCD) → Zip64 EOCD Record → real 64-bit numEntries + startCentralDir.

Only handles Zip64 at the archive-level (EOCD). Individual files must still be < 4 GB (Zip64 sentinels in central directory entries not handled — would need extra field parsing). For our zh-TW addon this is fine: individual PNG glyphs are ~200 bytes each, well under any limit.

### Test matrix (verified)

| Scenario | Result |
|---|---|
| ZIP32 addon (< 65535 entries) | ✅ mounts (regression) |
| ZIP32 base pack `mm-0.8.5-content.uqm` | ✅ mounts (regression) |
| Zip64 addon (83,706 entries, our full zh-TW) | ✅ **mounts** (previously failed) |
| Non-Zip64 files across the codebase | ✅ no behavior change |

### Deployment

Built and shipped as `install/UrQuanMasters-zip64.exe` (parallel to original `UrQuanMasters.exe`).
Launch with: `.\UrQuanMasters-zip64.exe --windowed --addon zh-TW`

---

## Content-layer fixes (no source patch needed)

Certain issues live in `mm-0.8.5-content.uqm/base/gamestrings.txt` where the maintainer used fullwidth CJK punctuation (U+FF0E `．`) or fullwidth Latin (U+FF24 `Ｄ`) as "elegant typography". These have no glyphs in `slab.fon` (banner) or render at CJK width in our tiny.bold.fon hybrid shadow, causing □ display or size mismatch.

Overridden in `translations/gamestrings.zh-TW.json`:
- `#(ENTERING PLANETARY ORBIT...)` — replaced `． ． ．` with ASCII `...` and translated
- `#(DAT)` — replaced `ＤＡT` (2 fullwidth + 1 ASCII) with pure ASCII `DAT`
- Missing compound mineral translations (Iron Compounds → 鐵化物, etc.) added
