# UQM zh-TW workspace tools (2026-08-05)

## Git baseline
- Workspace root: `Q:\Dos_G\StarControl2\`
- Initial commit: `5225fef` "Initial baseline: SC2 zh-TW project at 2.7% translation coverage"
- Latest: run `git log --oneline` to see
- `.gitignore` excludes UQM-MegaMod/ (own repo), DOS binaries, OCR pages,
  build outputs, python venvs, downloads, snapshots
- User works alone; commit early, commit often

## Tools I built
### `uqm-work/_dashboard.py`
- NPC translation coverage report
- Scans extracted (28 NPCs) vs translations/ vs shadow content vs packaged addon
- Prints console table sorted by (status, risk); flags high-risk NPCs
  (font too small, width too narrow)
- Options: `--md` (write _dashboard.md), `--json`, `--next N`

### `uqm-work/_selfverify_all.py`
- Pre-flight check for all NPCs. Non-zero exit if RED.
- Phase A (JSON static): heuristic patterns (LONG_CJK_RUN, LEAD_ELLIPSIS_HEAVY)
  — DOWNGRADED to GREEN when Phase B sim can run (sim is authoritative)
- Phase B (sim): 1:1 port of _simulate_count_lines.py, per-NPC font + width
- Phase C (font): kerndat.fnt name-token integrity
- Phase D (log): scans install/game.log for crash patterns
- Options: `--npc <race>`, `--strict`, `--no-log`, `--verbose`, `--no-color`
- Depends on: `_dashboard.py` (imports it for NPC scanning)

### Backup snapshots
- `_snapshots/YYYYMMDD_HHMMSS/` — my safety copies before risky edits

## CRITICAL: 大量 CJK 重寫時避免 \uXXXX 硬編碼
- 用 `multi_replace_string_in_file` 大量重寫繁中譯文時，若手打 `\uXXXX` unicode escape，容易記憶錯字碼
- **實測 2026-08-18 yehat P2 rewrite**：22 處錯碼 (嚐↔嚇/猛↔猗/嚥↔嚈/呱↔呉/彻↔徹/齣↔齒/恪↔恆/撒↔撇/樁↔橁/膀↔膚 等)
- **正解**：`replace_string_in_file` 或 `multi_replace_string_in_file` 的 `newString` 欄位**直接貼繁中字元**，不用 `\uXXXX`
- **驗證方法**：完成後跑集合差集 `set(new_text) - set(bak_text)` 過濾 CJK 範圍 (0x3400-0x9FFF)，任何「新出現但原文沒有」的 CJK 字元都要人工檢視
- 完整 diff detection script: `uqm-work/_count_emdash.py` + `_count_asterisks.py`（可擴充）
- ChinesePunctuation cheatsheet: `——` U+2014 · `*` U+002A · `**` markdown（**引擎不解析,除 Orz**）

## 引擎 markup 支援真相 (2026-08-18 verified)
- **`**bold**` markdown 在引擎中不解析**（[UQM-MegaMod/src/uqm/comm.c:338](../../UQM-MegaMod/src/uqm/comm.c)）
- 只有 Orz 對話 (`AlienConv == ORZ_CONVERSATION`) 用 `*char*` 觸發 font-swap 顯示 computer.fon 高亮
- 其他所有種族的 `**word**` 被畫成字面 `*word*`（yehat.fon/0002a.png = 100 bytes 有此 glyph）
- **shipped 譯文 pre-existing 濫用**：orz 848 lone `*`（合法）· umgah 76 pair · yehat 70 · yehatrebels 70 · safeones 38 · arilou 18 lone (icon)
- 規範已補至 [Dialogue_Rule.md §5.1.2](../../StarControl2_TW_Localization/08_Translation_Rules/Dialogue_Rule.md)

## `——` (em dash U+2014) 濫用問題 (2026-08-18)
- Shipped 譯文中譯自加 `——` 434 對 vs 英文原文 `--` 73 = 過量 +495%
- 主要濫用檔：yehat 116, yehatrebels 204, talkingpet 105, kohrah 94, vux 66, pkunk 53
- **P2 策略**：CAPS 詞用副詞升級或粗體換行；CAPS 句宣言用感嘆密度 `！！！`；hyphen 節拍用 `。` 句號節拍；一般停頓用 `，`；hesitation 用 `……`；icon 包夾用空格
- yehat pilot 完成：116→0 pairs · 70→0 `**` · 3-gate PASS
- 規範已補至 [Dialogue_Rule.md §5.1.1](../../StarControl2_TW_Localization/08_Translation_Rules/Dialogue_Rule.md)
- Now that git is set up, mostly redundant but harmless
- Gitignored

## NPC AlienTextWidth (SD mode, px)
Computed from units.h + comm.h + <race>c.c:
- SIS_TEXT_WIDTH = 240 (SD: CanvasWidth=320, STATUS_WIDTH=64, minus safe/text offsets)
- FULL = 240 (shofixti, slylandro, starbase)
- STD = 224 (most races: SIS_TEXT_WIDTH - 16)
- TWO_THIRDS = 149 (yehat, yehatrebels: STD * 2/3)
- HALF = 112 (vux, zoqfotpik: STD >> 1)
- FIXED143 = 143 (commander/starbase hardcoded)

## Real findings from tools (2026-08-05)
- `urquan.SEND_MESSAGE[page 7]` → INFINITE_LOOP potential.
  User hasn't triggered this scene in game yet (only 1 translation packaged).
  Text: 11 lines of pure CJK ending with 。 no ASCII spaces → SplitSubPages
  adds "..." to each, then engine _count_lines wraps CJK-only → loop.
  FIX: space-wrap the SEND_MESSAGE translation (add ASCII spaces within lines).

## MegaMod CLI cheat flags (verified v0.8.5 build 2026-06-06)
Use these to speed up in-game validation:
- `--bubblewarp` — teleport anywhere on Starmap
- `--loadgame` — boot to load screen directly
- `--skipintro`, `--infinitefuel`, `--infiniteru`, `--kohrstahp`
- `--headstart`, `--unlockships`, `--infinitecredits`
- `--melee` — direct to Super Melee
- `--nohqencounters` — no HyperSpace random battles
Combined: launches straight into a save with unlimited fuel/RU/time,
then bubble-warp to any race homeworld for first-contact test.

## Progress
- Total dialog tokens across 28 NPCs: 3547
- Translated: 95 (2.7%) as of baseline
- Only commander (94) + urquan (1 SEND_MESSAGE, has bug)
- Recommended next order (low-risk first, from _dashboard.py):
  slylandro → shofixti → pkunk → robot → safeones
  = 699 tokens = brings coverage to ~22%
