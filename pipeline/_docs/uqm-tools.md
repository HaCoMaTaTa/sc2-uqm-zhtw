# UQM zh-TW workspace tools (2026-08-05)

> **來源**:此檔案是 `/memories/repo/uqm-tools.md` 的公開鏡射,供其他 AI/人類接手時閱讀。
> 若你在 memory 環境中,請直接讀 memory 版本。

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
- `_snapshots/YYYYMMDD_HHMMSS/` — safety copies before risky edits
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
- `urquan.SEND_MESSAGE[page 7]` → INFINITE_LOOP potential (FIXED in commit ce42c23).
  Root cause: 11 lines of pure CJK ending with 。 no ASCII spaces → SplitSubPages
  adds "..." to each, then engine _count_lines wraps CJK-only → loop.
  Fix: space-wrap the SEND_MESSAGE translation (add ASCII spaces within lines).

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
- Translated: 95 (2.7%) as of baseline; 106 after urquan fix
- commander (94) + urquan (12 lines of SEND_MESSAGE, verified GREEN)
- Recommended next order (low-risk first, from _dashboard.py):
  slylandro → shofixti → pkunk → robot → safeones
  = 699 tokens = brings coverage to ~22%
