# UQM zh-TW debugging protocol

> **來源**:此檔案是 `/memories/repo/uqm-debugging.md` 的公開鏡射。

## FIRST STEP: check game.log before anything else
- User standard invocation: `UrQuanMasters.exe --windowed --addon zh-TW --logfile game.log`
- Log path: `Q:\Dos_G\StarControl2\uqm-work\install\game.log`
- When user reports "menu blank" / "text missing" / any visual issue:
  1. `Get-Content game.log -Tail 80` — read the tail first
  2. Search for: `error|fail|warning|not found|missing|undefined|blocking|crash`
  3. Look for font/resource load messages, and last-thing-printed before hang

## CRITICAL: Preserve Lua template variables in translations
- English source contains `<% state.sis.getShipName() %>`, `<% state.sis.getCaptainName() %>`, `<% comm.getStarName("Vela", "start colony") %>` (interpolated at runtime).
- **NEVER hardcode the captain/ship/star name into the translation** — must
  preserve the `<% ... %>` template EXACTLY (whitespace within `<%...%>` may
  vary but should stay valid Lua).
- Example bug: translated `starship <% state.sis.getShipName() %>` as
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
