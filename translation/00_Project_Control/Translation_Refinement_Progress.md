# 翻譯精修進度追蹤（v3.1+ 精修 audit 階段）

> **本檔功能**：追蹤各族 zh-TW.json 於 melnorme audit 流程確立後的 **v3.1+ 精修進度**（含直譯修正、canonical shipped bug 修復、pronoun align、hex typo 掃描）。
> **維護方式**：每完成一 Batch 或整族收尾即更新對應 row 的日期與狀態。
> **與姊妹檔區別**：本檔非 dossier 或 Rebuild-Compare 追蹤，而是**後 rebuild-compare 深度精修**追蹤。姊妹檔 `Dossier_Revision_Progress.md` 記錄 v0.7 Rebuild-Compare 完成度。

**最後更新**：2026-08-30（melnorme v3.1.7 + mycon v3.1 + syreen v3.1 + pkunk v3.1 + slylandro v3.1 + utwig v3.2 + druuge v3.1 + umgah v3.1 + zoqfotpik v3.1 + safeones v3.1 + kohrah v3.1.1 + thraddash v3.1.1 + supox v3.1.1 + chmmr v3.1.2 + vux v3.1.3 + talkingpet v3.1.4 + yehat v3.1.4 + yehatrebels v3.1.4 + shofixti v3.1.4 完成 · probe 待啟動）

---

## 一、狀態代號

| 代號 | 意義 |
|---|---|
| ✅ | 精修全族完成 |
| 🟡 | 精修進行中 |
| ⏳ | 已排入計畫，待啟動 |
| — | 不適用 / 無需 |
| 🔴 | 發現 shipped canonical bug（急需處理）|

---

## 二、精修方法論摘要（自 melnorme 建立）

**Batch 節奏**：15 batches × ~19 tokens/batch（大檔）or 12-24 batches（依規模）  
**每 Batch 流程**：
1. 讀取當批 tokens + EN 原文
2. 生成 audit 表（🔴 CRITICAL / 🟡 significant / 🟢 minor / 💚 already-good）
3. 使用者 pick（A/B/C/D 或 `根據上下文分析`）
4. 應用 edits（**純 CJK 字串優先**，避免 `\uXXXX` hex escape）
5. 每批後 hex sweep + purity check
6. 每 Batch 後 commit 保護

**Session-累積 hex typo 避雷模式**（12 patterns · 全族必掃）：
- `嬱`（U+5B31）誤替 `咱`（U+548B）
- `瞌`（U+778C）誤替 `瞧`（U+77A7）
- `嫀`（U+5AC0）誤替 `嫌`（U+5ACC）
- `諥`、`诫`（U+8BEB, 簡體）誤替 `趁`（U+8DBB）
- `賱`（U+8CE0）誤替 `賈`（U+8CC8）
- `脱`（U+8131, 簡體）誤替 `脫`（U+812B）
- `骷髝` shipped 錯字 → `骷髏`/`陰險詭計`
- `顓`（U+9852）誤替 `顆`（U+9846）量詞
- `螾`（U+87BE, 蟲）誤替 `蟾`（U+8722）canonical
- `身軍`（U+8ECD）誤替 `身軀`（U+8EC0）

**跨族 canonical 修復參考**（melnorme 已完成）：
- 深淵之子 → 深層幼體（Master_Glossary v0.7 rename）
- 毒賱族 → 毒賈族（U+8CE4 shipped hex typo · Master_Glossary L316-321）
- 螾亞 → 蟾亞（U+87BE shipped hex typo · Master_Glossary Dnyarri）

---

## 三、優先順序矩陣（20 族 + 已完成 melnorme）

### 🔴 CRITICAL — 立即修（shipped canonical bug）

| # | 族 | Ver | Tokens | shipped bug 掃描 | 文言污染 | 精修狀態 | 進度 | Commits |
|---|---|---|---|---|---|---|---|---|
| 1 | ~~mycon~~ | v3.1 | 109 | ✅ 深淵之子×3 保留於 `_notes` only（dialog clean）| — | ✅ 完成 | 12/12 | `b826110` |
| 2 | ~~syreen~~ | v3.1 | 127 | ✅ dialog clean（深淵之子 只在 `_notes` 歷史紀錄）| 0 | ✅ 完成 | 13/13 | `7c48886` |

### 🟠 HIGH — 老版本 + 高文言污染

| # | 族 | Ver | Tokens | shipped bug | 文言 | 狀態 | 備註 |
|---|---|---|---|---|---|---|---|
| 3 | ~~pkunk~~ | v3.1 | 180 | clean | 21 (否保留 A-decision) | ✅ 完成 | `17c1659` + `67afcd6` · 3 sem + typography |
| 4 | ~~slylandro~~ | v3.1 | 114 | ✅ 3已修（噦/寧生者/喉）| 8 (保留 dossier canonical) | ✅ 完成 | `e59c2db` · 13 sem + typography sweep |
| 5 | ~~utwig~~ | v3.2 | 114 | v0.7 rebuild + re-audit clean | 0 wenyan | ✅ 完成 | `0dede36 ~ 753a6f0` (v3.1 base 4 commits · 38 sem + 386 typography) + `7e4319e` (v3.2 re-audit 11 batches · 115 edits) · W1 語意誤譯修正 (你們一轉頭→本族一背過身) · P15 canonical (陰黑表親) · dossier §四 現代學者式憂鬱華麗長句 對齊 |
| 6 | probe | v0.1 | 86 | clean | 8 | ⏳ 下一目標 | Slylandro Probe 短小 |
| 7 | ~~druuge~~ | v3.1 | 105 | clean (v0.7 shipped) | 17 wenyan (爾/乃/莫/予) + A2 法律體保留 | ✅ 完成 | `9f946b2` · 45 sem · A2+B1+C1 · 新立打破第四牆 pronoun 例外規則 |
| 7 | druuge | v? | 105 | clean | 8 | ~~⏳~~ | canonical 大變（melnorme audit 影響）|
| 8 | ~~shofixti~~ | v3.1.4 | 91 | v0.7 4-batch deep refinement | 0 wenyan | ✅ 完成 | `653c24d` · 26 edits (Batch 0 8 + Batch 1 7 + Batch 2 7 + Batch 3 6-1) · anime 熱血漫畫武士 + 田中/武士刀雙 palette + 現代粗口 · 姓名歧義釐清 + 諷刺尾殺 + palette 收斂 + Dhrang bilingual gloss canonical override · Unicode hazard 3 pairs 加入 memory (俺/俱 · 唉/唐 · 喂/喵) |
| 9 | ~~safeones~~ | v3.1 | 143 | clean (v0.5 shipped) | 4 爾 + 4 之 (全 canonical/idiom) | ✅ 完成 | `b0eae3c` · 35 semantic + 3 typo 修 (1 shipped 愚蠶→愚蠢 + 2 我誤打即修) + 1 dossier 維護 · Batch 0-6 143 tokens 100% audited · **新立 Unicode 字形辨識風險清單** (賣/賨、醇/醬、誼/誰、蠢/蠶、芙/苙) |
| 10 | ~~umgah~~ | v3.1 | 85 | clean (v0.7 shipped) | 1 爾 + 3 之 (心控 canonical) | ✅ 完成 | `5788146` · 158 edits · A1+B2+C心控莯文中間號+D1 · 新立艦艇命名仲裁規則 |

### 🟡 MEDIUM — v0.7/v3 已精修但可能有殘餘

| # | 族 | Ver | Tokens | shipped bug | 文言 | 狀態 | 備註 |
|---|---|---|---|---|---|---|---|
| 11 | ~~zoqfotpik~~ | v3.1 | 334 | clean (v0.7 shipped) | 3 爾 + 6 之 (全 canonical/idiom) | ✅ 完成 | `5d204bf` · 4 net + 3 canonical revert · Master_Glossary v0.5.2 對齊 · **99% canonical PASS 率** · 新立 Master_Glossary 仲裁規則 v2 |
| 12 | ~~thraddash~~ | v3.1.1 | 152 | v0.7 v3 rebuild (2026-08-17) | 20 semantic + 299 typography + 2 canonical align + 1 typo 修 | ✅ 完成 | `6e5cb88` · 289 A1 半形→全形逗號 + 10 F1 edge cases + Batch 1-6 v0.7 文言殘留澈底清除 + 毀滅之輪 metaphor + Rhyme4 -ng 韻重寫 · 新立字形風險 撃/沒 |
| 13 | ~~talkingpet~~ | v3.1.4 | 112 | v0.7 rebuild clean | 0 wenyan | ✅ 完成 | `6f58bdc` · 51 semantic edits · Batch 0-3 四輪深度審核 · Mode 1/2/3/4 sub-modes 全保留 · Ouchy-oochy canonical 更新 (哎唷呢喃→唉喲喂啊) · dossier v0.7 A 案對齊 |
| 14 | ~~vux~~ | v3.1.3 | 102 | v0.7 rebuild (2026-08-16) clean | 0 wenyan | ✅ 完成 | `4977b58` + `c3d64c8` + `0ed5381` · 8+13+9 = 30 semantic edits · Batch 0-3 四輪深度審核 · ZEX/主族雙 voice palette 全保留 · 新立字形風險 聰 (U+8070 繁體) vs 聡 (U+806A 日文 shinjitai) |
| 15 | ilwrath | v3 | 109 | clean | 1 | ⏳ | 蛛狂族 |
| 16 | ~~supox~~ | v3.1.1 | 93 | clean | 1 (共汲於→飲於同) | ✅ 完成 | `7a51cab` · 15 semantic + 1 typo 修 (沒點→沾點 U+6C92→U+6CBE) · Batch 0-6 v0.7 v3 clean-room 深度審核 · 情勢發展/禾苗遭鐮割/雙葉飲於同根 · 新立字形風險 沾/沒 |
| 17 | ~~chmmr~~ | v3.1.2 | 78 | v0.7 rebuild (2026-08-17) clean | 0 wenyan | ✅ 完成 | `c0d80a3` + `56fce17` · 4+25 semantic edits · Batch 0-3 四輪深度審核 · shipped 耽時→耗時 typo 修 (WE_ARE_FREE dossier §六 canonical alignment) · pre-fusion + post-fusion 雙 voice palette 全保留 · 新立字形風險 耽/耗 |
| 18 | ~~yehat~~ | v3.1.4 | 68 | v0.7 rebuild clean | 0 wenyan (爾等已清) | ✅ 完成 | `297cbdb` · 49 edits (15 semantic + 19 typography sweep + 9 Batch 1 + 6 Batch 2) · Batch 0-2 三輪深度審核 · A+C 混合版 蘇格蘭中世紀勇士 + 「本」字集體感 + 鳥鴴中英雙寫 + 保皇派/叛軍派 sub-modes 對齊 |
| 19 | ~~kohrah~~ | v3.1.1 | 76 | v3.1 clean-room (2026-08-16) | 8 semantic + 4 typo | ✅ 完成 | `e4c78b9` · BONE_PILE shipped typo (骸骸→骨骸 × 4) + THEN_DIE 4 修 + 語境對齊 · 新立字形風險 骨/骸 |
| 20 | ~~yehatrebels~~ | v3.1.4 | 34 | v0.7 rebuild clean | 0 wenyan | ✅ 完成 | `7d4540a` · 32 edits (Batch 0 27 + Batch 1 5) · A+C 混合叛軍派 熱血革命 + 蒼宇彼方 canonical + typography sweep + 玩家對白多餘逗號清理 · dossier 繼承 yehat |

### ✅ 已完成

| # | 族 | Ver | Tokens | Semantic edits | Pronoun align | Commits | 完成日期 |
|---|---|---|---|---|---|---|---|
| — | **melnorme** | **v3.1.7** | 281 | **141** | **171 处** | `cd5f09e ~ e08f533`（8 commits） | 2026-08-27 |
| — | **mycon** | **v3.1** | 109 | **10 sem + 4 em dash 正規化** | — | `b826110`（1 commit）| 2026-08-27 |
| — | **syreen** | **v3.1** | 127 | **5 sem + 2 Q1=B/typo** | — | `7c48886`（1 commit）| 2026-08-27 |
| — | **pkunk** | **v3.1** | 180 | **3 sem + typography (93 ? + 32 paren)** | — | `17c1659` + `67afcd6`（2 commits）| 2026-08-27 |
| — | **slylandro** | **v3.1** | 114 | **13 sem (3 🔴 錯字/誤譯/漏譯) + typography (6 進)** | — | `e59c2db`（1 commit）| 2026-08-27 |
| — | **utwig** | **v3.1** | 115 | **38 sem (30 之 X Y 純文言修 · 4 痛哉 P5 · 2 語境不合直譯重寫 · 2 typography 漏網) + 386 typography (parens/commas/colons/semicolons)** | — | `0dede36 ~ 753a6f0`（4 commits · Batch 0/0.1/0.2/content）| 2026-08-28 |
| — | **druuge** | **v3.1** | 105 | **45 edits (44 sem + 1 typography) · A2 法律體保留· B1 wenyan 全修 · C1 Depart Q11=B · canonical alignment (涓滞/屎屈/惡徒小偷騙子/黑心賤/污穢的海盜) · 新立打破第四牆 pronoun 例外規則 (OUT_TAKES)** | — | `9f946b2`（1 commit）| 2026-08-28 |

---

## 四、melnorme 精修成果總覽（範本參考）

| Commit | 版本 | 條數 | 內容 |
|---|---|---|---|
| `cd5f09e` | v3.1 | 72 | Batches 1-8 |
| `55de265` | v3.1.1 | 171 | Pronoun align（我方→敝方 NPC lines）|
| `42f74f8` | v3.1.2 | 17 | Batch 9（4 🔴 CRITICAL OK_BUY_EVENT_7）|
| `177b5fb` | v3.1.3 | 14 | Batch 10（ALIEN_RACE_1~10）|
| `cc5d579` | v3.1.4 | 22 | Batch 11（4 🔴 深層幼體/螾亞/身軍）|
| `5d71b64` | v3.1.5 | 11 | Batch 12（NEW_TECH 系列）|
| `81de2d2` | v3.1.6 | 4 | Batch 13（CHARITY/裝備/Alliance）|
| `e08f533` | v3.1.7 | 1 | Batch 14+15 + dossier `_notes` ENUMERATE 澄清 |

**發現的 shipped bugs 已修復（12+）**：
- 毒賱族 → 毒賈族 × 7（OK_BUY_EVENT_7）
- 顓 → 顆（量詞錯字）
- 骷髝 → 陰險詭計
- 甘賣 → 脫手
- 深淵之子 → 深層幼體（v0.7 canonical rename）
- 螾亞 → 蟾亞 × 11（HISTORY_6+7 hex typo）
- 身軍 → 身軀（錯字）
- 指揮官 → 艦長（canonical align）

---

## 五、每族精修流程 checklist

### 開工 checkin
- [ ] 讀取 dossier `02_Races/<Race>.md`
- [ ] 讀取 `translations/<race>.zh-TW.json` 全檔
- [ ] 掃描 shipped bugs（深淵之子/螾亞/毒賱等）
- [ ] 統計 wenyan hits (吾/爾/汝/乃/矣/哉/焉/兒/莫)
- [ ] 統計 pronoun (我方/敝方/我族/吾等 等) 分布
- [ ] 規劃 batch 數量與範圍

### 每 Batch
- [ ] 讀取 N tokens + EN 原文
- [ ] 生成 audit 表
- [ ] 使用者 pick
- [ ] 應用 edits（純 CJK · 避免 `\uXXXX`）
- [ ] Hex sweep（12 pattern）
- [ ] Purity + Lua + JSON 驗證
- [ ] Commit（帶完整 commit message）

### 收尾
- [ ] 全檔 hex sweep
- [ ] 3-gate PASS 確認
- [ ] 更新本進度表 row（狀態、日期、條數、commits）
- [ ] 檢查是否影響 dossier `_notes`
- [ ] Master_Glossary 若有新 canonical 待補則登記

---

## 附錄：本 session 建立的 audit 方法沿革

1. **melnorme 是第一個「深度精修」對象** — 建立了 15-batch audit + 反問決策 + hex typo 自 correction 流程
2. **中途 revert 事件教訓** — 另一 session 覆蓋檔案導致 Batches 1-7 遺失 63 條 edits，透過對話記錄以純 CJK 字串重建。以後**每 batch 後必 commit** 已成 SOP
3. **Runtime code investigation** — 從 `melnorm.c` 確認 ENUMERATE_HUNDRED/THOUSAND compositional 設計，avoids blindly follow dossier notes
4. **Pronoun canonical align 是獨立步驟** — 發現 shipped 常有 我方 vs 敝方 canonical 不 sync（melnorme 234 處 pronoun align）
