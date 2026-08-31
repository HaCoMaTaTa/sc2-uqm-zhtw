# pipeline/ — 繁中化 build/verify 流程

本資料夾內容整理自 `uqm-work/`（原開發工作區）中所有已 git-tracked 的檔案（排除 OCR 專用與純本地診斷腳本）。

## 快速上手（新機器完整重建流程）

```powershell
# 前置：先跑 ../scripts/setup_upstream.ps1 準備好 ../UQM-MegaMod/
cd Q:\path\to\uqm-megamod-zhTW\pipeline

# 1. 首次或翻譯有更新 → 產出 SD addon
.\build_zh-TW.ps1        # JSON → txt + rasterize 字型 → shadow content
.\package_zh-TW.ps1      # shadow content → zh-TW.uqm（會呼叫 build 若需要）

# 2. 想要 HD 字型（1280×960 UI）
.\_build_hd_fonts.ps1    # rasterize HD 字型（39 個 · 約 3 分鐘）
.\_package_hd_addon.ps1  # 打包 zh-TW-hd.uqm（Compress-Archive · 約 10 分鐘）

# 3. 一鍵 PC release
.\_release_full_zh-TW.ps1 -Version v1.0.13 -Execute
# → 產出 release/output/SC2-zhTW-v1.0.13.zip + .sha256
```

## 目錄結構

| 路徑 | 內容 |
|---|---|
| `*.ps1`（6 個）| SD/HD build/package/release 主流程 |
| `*.py`（72 個）| 翻譯套版、字型 rasterize、純度閘、行數驗證、字元池、單字補入 |
| `translations/`（166 JSON）| 每族 zh-TW.json 譯文本體 + `lander/` 掃描報告 |
| `zh-TW-addon/`（3 md）| shadow-content 說明（**content 目錄由 build 產生**，git 不追蹤）|
| `_docs/`（3 md）| 早期整理的工具說明（部分內容已升到 `docs/AI_Handoff/`）|
| `_scripts/`（多檔）| 一次性輔助 py + ps1（screenshot / patch 工具）|
| `_terms/`（21 詞彙 JSON + md）| 詞彙抽取結果（`_dashboard.py` 也用）|

## 核心腳本速覽

### 主流程

- **`build_zh-TW.ps1`** — SD 全流程：JSON→txt + rasterize 到 shadow content
  - 內建 Step 0 `_check_zh_purity.py --strict` + `_check_lua_templates.py --strict`
- **`package_zh-TW.ps1`** — 打包 `zh-TW-addon/content/` 成 `zh-TW.uqm`
  - 預設自動 invoke `build_zh-TW.ps1`；`-SkipBuild` 可跳過
  - `-SkipHybridUI` 走 ZIP32（相容 vanilla exe，未套 patch 007 時用）
- **`_release_full_zh-TW.ps1`** — 打包完整 PC release zip
  - `-Execute` 才真跑，預設 DryRun

### HD 專屬

- **`_build_hd_fonts.ps1`** — 39 個 HD 字型 rasterize 到 `_stage_hd_fonts/`
- **`_package_hd_addon.ps1`** — 打包 HD addon `zh-TW-hd.uqm`
- **`_patch_hd_add_char.py <字>`** — 免全量重跑，單字補入 39 個 HD 字型

### 翻譯套版 / rasterize

- **`translate_ui.py`** — JSON 值填入英文 `.txt` 對應區塊
- **`translate_intro.py`** — intro 動畫字幕翻譯
- **`rasterize_font.py`** — TTF→PNG 字型 glyph 產生器（含 `--cjk-scale`, `--vertalign-adjust`）

### 純度閘 / 驗證

- **`_check_zh_purity.py --strict`** — 掃簡體字 + bare English race name + 禁用譯法
- **`_check_lua_templates.py --strict`** — 掃 Lua template first-arg 英語洩漏
- **`_verify_line_counts.py`** — JSON token 行數對齊 EN 原文
- **`_verify_line_widths.py`** — 每 `\n` 分行寬度 ≤ AlienTextWidth
- **`_verify_space_wrap.py`** — space-delimited 每 chunk 寬度合法
- **`_verify_v032.py`** — 打包完成後最終驗收
- **`_simulate_count_lines.py`** — 模擬引擎 `_count_lines()`，找無限迴圈頁

### 覆蓋率與進度

- **`_dashboard.py`** — 全 NPC 翻譯狀態總覽（風險 + 建議下一族）
- **`_selfverify_all.py --no-log`** — 全 NPC pre-flight 檢查（Phase A/B/C/D）

### 星圖 / 招牌 icon

- **`_append_star_postfix_zh.py`** — 產出 STAR_POSTFIX_ZH_BASE=1024 對應中譯條目
- **`_apply_race_zh_labels.py`** — 每族 SoI 中文 label（patch 010）
- **`_apply_starmap_ui.py`** — 星圖 UI 中文 marker

## 補充規範

- **翻譯風格** → [../translation/08_Translation_Rules/](../translation/08_Translation_Rules/)
- **AI 提詞** → [../translation/09_AI_Prompt/](../translation/09_AI_Prompt/)（副本亦在 [../docs/AI_Handoff/prompts/](../docs/AI_Handoff/prompts/))
- **踩坑心得** → [../docs/AI_Handoff/memories/](../docs/AI_Handoff/memories/)
- **工作區歷史** → [`_docs/uqm-tools.md`](_docs/uqm-tools.md), [`_docs/uqm-font-hacks.md`](_docs/uqm-font-hacks.md), [`_docs/uqm-debugging.md`](_docs/uqm-debugging.md)
- **完整重建 SOP** → [../docs/SOP_Rebuild_And_Release.md](../docs/SOP_Rebuild_And_Release.md)

## 已知未進 repo 的檔案

以下 uqm-work 資產**未複製**到本 repo：

- `install/`（MegaMod 遊戲安裝，使用者自行安裝）
- `extracted/`（從 `.uqm` 解出的 base content，跑 SOP 自動生）
- `downloads/`, `_downloads/`（安裝檔與字型 TTF，部分商業授權）
- `zh-TW-addon/content/`（52k build 產物 PNG，跑 `build_zh-TW.ps1` 生成）
- `zh-TW-addon/_stage*/`, `zh-TW-addon/_intermediate/`（build 中間產物）
- `_stage_hd_fonts/`（HD 字型中間產物）
- `_snapshots/`, `_ocr_*`, `_rpg_*`（OCR / 快照 / 實驗）
- `release/`（打包 zip 走 GitHub Releases）
- OCR 專用 py（`ocr_manual_*.py`, `merge_ocr_pages.py` 等）
- 一次性診斷腳本（`_diag_first_hayes.ps1`, `_diag_minimal.ps1`）

## 檔案數統計（本 repo pipeline/）

- Python 腳本：72
- PowerShell 腳本：6
- 翻譯 JSON：166（含 `translations/lander/`）
- 文件 md：36
- 詞彙 JSON：21（`_terms/`）
- 總大小：約 7.6 MB
