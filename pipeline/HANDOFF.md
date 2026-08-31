# HANDOFF — Star Control 2 zh-TW 中文化專案

> **給誰讀的**:任何要接手這個專案的人或 AI(尤其是**不能讀 `/memories/repo/`** 的其他 AI session)。
> **一句話**:把 UQM MegaMod 0.8.5 的 28 個 NPC 對話 + UI 翻譯成繁體中文,打包成 `zh-TW.uqm` addon。
> **狀態**(2026-08-06):總 3547 tokens / 已翻 209 / 覆蓋率 **5.9%** (commander/urquan/slylandro GREEN)。
> **翻譯用詞規範**:目前主要規範是 [_analysis/SC2-詞彙對照表-v0.3.md](_analysis/SC2-詞彙對照表-v0.3.md),v0.2 已被 v0.3 取代(v0.3 是 v0.2 的增量補漏 + wiki 交叉驗證修訂)。
> **僅限單人 + AI 開發**(使用者無其他協作者)。

---

## 1. 開場 5 分鐘做這 3 件事

```powershell
cd Q:\Dos_G\StarControl2

# ① 看目前 git 歷史,理解決策脈絡
git log --oneline

# ② 看每個 NPC 的翻譯狀態、風險、建議下一個做誰
cd uqm-work
python _dashboard.py

# ③ 跑 pre-flight 檢查,看有沒有已翻但會 crash 的
python _selfverify_all.py --no-log
```

看完這三個就知道:哪些完成、哪些下一個、有沒有等修的 bug。

---

## 2. 檔案地圖(在哪裡看什麼)

| 你想知道 | 讀這個 |
|---|---|
| 專案總覽 + 技術路線 | [_analysis/SC2-中文化分析報告.md](_analysis/SC2-中文化分析報告.md) |
| 各種族最終中文名 | [_analysis/SC2-種族名稱重新設計.md](_analysis/SC2-種族名稱重新設計.md) |
| **專有名詞統一表(v0.3 主規範)** | [_analysis/SC2-詞彙對照表-v0.3.md](_analysis/SC2-詞彙對照表-v0.3.md) |
| 專有名詞舊版(v0.2 已被取代,僅參考) | [_analysis/SC2-詞彙對照表.md](_analysis/SC2-詞彙對照表.md) |
| 各種族用哪個字型 | [_analysis/SC2-種族專屬字型策略.md](_analysis/SC2-種族專屬字型策略.md) |
| **翻譯決策記錄**(誰要為什麼定案) | [uqm-work/_terms/_decisions.md](uqm-work/_terms/_decisions.md) |
| **詞彙自動抽取結果** | [uqm-work/_terms/_summary.md](uqm-work/_terms/_summary.md) |
| **翻譯 AI 主提詞(必讀)** | [Star Control II GUS - Manual/SC2_繁中化_AI翻譯提詞.md](Star%20Control%20II%20GUS%20-%20Manual/SC2_繁中化_AI翻譯提詞.md) |
| 中文手冊 OCR(參考劇情用,舊譯名不採用) | [Star Control II GUS - Manual/starcontrol2_中文手冊_OCR.md](Star%20Control%20II%20GUS%20-%20Manual/starcontrol2_中文手冊_OCR.md) |
| 工具與 pipeline 說明 | [uqm-work/_docs/uqm-tools.md](uqm-work/_docs/uqm-tools.md) |
| 字型 / 排版 / 死結血淚知識 | [uqm-work/_docs/uqm-font-hacks.md](uqm-work/_docs/uqm-font-hacks.md) |
| Debug 流程(crash / 空白 / 英文顯示) | [uqm-work/_docs/uqm-debugging.md](uqm-work/_docs/uqm-debugging.md) |
| 工作區結構 | [uqm-work/README.md](uqm-work/README.md) |

---

## 3. 每個 NPC 的完整流程(12 步)

> 每步都可以獨立 commit。做完一族再做下一族。

| 步 | 動作 | 工具/檔 | 產物 |
|---|---|---|---|
| 1 | 讀英文原文 | `extracted/base/base/comm/<race>/<race>.txt` | 理解語境 |
| 2 | 讀風格設定 | `SC2_繁中化_AI翻譯提詞.md` | 對應該族語氣 |
| 3 | 產翻譯 JSON(**AI 在對話裡做**) | 寫進 `translations/<race>.zh-TW.json` | JSON |
| 4 | 靜態預檢 | `python _selfverify_all.py --npc <race>` | 抓明顯問題 |
| 5 | Rasterize CJK 到該族字型 | `rasterize_font.py` | shadow font PNG 集 |
| 6 | Build | `.\build_zh-TW.ps1` | shadow content `.txt` |
| 7 | Package | `.\package_zh-TW.ps1` | `install/content/addons/zh-TW.uqm` |
| 8 | 全 Phase 驗證 | `python _selfverify_all.py --npc <race>` | 目標 GREEN |
| 9 | Commit 綠燈 | `git commit -am "translate(<race>): ..."` | 存檔點 |
| 10 | 遊戲內驗證(見下方指令) | `UrQuanMasters.exe --bubblewarp ...` | 人眼看畫面 |
| 11 | 若人眼發現問題 | 修 JSON,回到 6 | |
| 12 | 遊戲驗證通過 commit | `git commit -am "verify(<race>): visual OK"` | 該族完成 |

**AI 平行分工**:步驟 6-7 build+package 約 30-60 秒,可以同時開始讀下一族原文。

---

## 4. 翻譯到底發生在哪?

**在 AI(Copilot / Claude 等)的對話裡。**

- `translate_ui.py` **不是翻譯器**,只是「JSON 套版器」。名字容易誤導,實際做的是「把現成 JSON 值填入英文 `.txt` 對應區塊」。
- 真正翻譯的流程:**使用者 → AI(Copilot 對話) → AI 寫回 `translations/<race>.zh-TW.json`**。
- 沒有任何腳本呼叫翻譯 API。這是 by design(可控、可回顧、可 diff)。
- JSON 格式:
  ```json
  {
    "_notes": ["風格、規則、註記..."],
    "TOKEN_NAME": "中文譯文\\n多行用 \\n 分隔\\nCJK 內部用 ASCII 空格 wrap",
    ...
  }
  ```
- `_notes` 開頭底線,套版器會忽略。

---

## 5. 常用指令(複製即用)

```powershell
# --- 進度 ---
cd Q:\Dos_G\StarControl2\uqm-work
python _dashboard.py                          # 全體狀態
python _dashboard.py --next 5                 # 建議下一批
python _selfverify_all.py --no-log            # 全 NPC pre-flight
python _selfverify_all.py --npc slylandro     # 只查一族

# --- Build / Package(每次改完必跑三步 sequence) ---
.\build_zh-TW.ps1
.\package_zh-TW.ps1
python _selfverify_all.py --no-log

# --- 遊戲內驗證(啟全 cheat + bubblewarp)---
cd install
.\UrQuanMasters.exe `
    --windowed --addon zh-TW `
    --bubblewarp --infinitefuel --infiniteru `
    --kohrstahp --skipintro --loadgame `
    --logfile game.log

# --- Git 安全網 ---
git status                                     # 看有什麼改動
git diff                                       # 看逐行差異
git commit -am "描述"                          # 存檔
git log --oneline -20                          # 近期歷史
git checkout -- <file>                         # 還原單一檔
git reset --hard <commit>                      # 大回溯(危險)
```

---

## 6. 已知會踩的 3 大地雷(必讀)

1. **`_count_lines()` 死結**(CJK 無空格會爆): 每行 CJK 用 ASCII 空格切成 3-5 字 chunk。詳見 [uqm-font-hacks.md#space-wrap-methodology](uqm-work/_docs/uqm-font-hacks.md)。
2. **字型太小 CJK 讀不清**: 9 個字型 <14px 需要 shadow redirect(commander、arilou、chmmr、druuge、melnorme、supox、thraddash、umgah、starbase)。已由 `package_zh-TW.ps1` 的 `$fontRedirects` 自動處理。
3. **Lua template 別硬翻**: `<% state.sis.getCaptainName() %>` 這種 tag 必須原樣保留,不能把艦長中文名寫死。
4. **Lua template 第一參數要 CJK 化**: `comm.getColor("blue", ...)` / `comm.getConstellation("blue star", ...)` / `comm.swapIfSeeded(A, B)` 這三個在 `!StarSeed` 預設路徑會**原樣**回傳第一參數。必須把第一參數改成中文(如 `"藍色"`, `"藍色恆星"`),否則遊戲內會看到英文洩漏。詳見 slylandro retrofit(commit `fd1f3cf`)。

---

## 7. 接手 checklist(30 秒自我確認)

- [ ] 我讀過 `git log --oneline` 了嗎?
- [ ] 我跑過 `python _dashboard.py` 看目前該做誰了嗎?
- [ ] 我跑過 `python _selfverify_all.py --no-log` 看有沒有 RED 待修嗎?
- [ ] 我理解翻譯是**我(AI)自己在對話裡產出後寫回 JSON**,不是任何腳本自動做嗎?
- [ ] 我知道每個 NPC 完成一輪就 commit 一次嗎?
- [ ] 遇到不確定的技術細節,我會先讀 `uqm-work/_docs/` 三份 md 嗎?

打勾完再開始工作。
