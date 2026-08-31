# AI Handoff — 給下一位接手的 AI

> **一句話**：新的 AI 進來時，讀完本檔 + 5 個關鍵文件就能接續翻譯 / 修 bug / build 發布。
> **必讀**：本檔 → 第 1 節「5 分鐘上手」

## 1. 5 分鐘上手 · 必做 checklist

```
□ 讀 [../README.md](../../README.md) 了解專案輪廓
□ 讀本檔第 2 節「使用者風格與規則」
□ 讀 prompts/_MAIN_PROMPT_SC2_zh-TW.md — 翻譯總設定
□ 遇到 audit / 深度審視 → 讀 memories/audit-policy.md
□ 遇到 build / package / crash → 讀 memories/uqm-debugging.md + uqm-font-hacks.md
□ 遇到 Android → 讀 memories/android-build.md
```

## 2. 使用者風格與規則（重要）

- **提示詞前綴**：使用者每個 session 通常開頭寫「**優化題詞後執行 不臆測 有問題請問我**」
  - 意思：refine → ask on ambiguity → propose plan → wait for approval → execute
- **決策方式**：
  - 使用者對每個「多選題」用**單字母/短編號**回答（A / B / C 或 1./2./3.）
  - AI 提出 🟡/🟠/🔴 severity 分類的差異報告，使用者按顏色決定「全 A / 全 B / 覆蓋幾個」
- **不臆測 canonical**：
  - 音譯 vs 意譯 → 一律先查 `translation/07_Glossary/Master_Glossary.md`
  - 找不到 → 提 3-5 個選項給使用者挑，不要自己決定
- **不動 Lua template**：`<% comm.getStarName(...) %>` 這種模板嚴禁改
- **繁中而非簡中**：使用者是台灣人，用「軟體 / 星艦 / 艦長 / 螢幕」不用「軟件 / 宇宙船 / 船長 / 屏幕」

詳細規則見 [memories/sc2-translation-workflow.md](memories/sc2-translation-workflow.md)。

## 3. 目錄結構

```
docs/AI_Handoff/
├── README.md              ← 本檔（AI 入口）
├── memories/              ← 11 個 repo memory（跨 session 血淚教訓）
│   ├── audit-policy.md              · Level 3 深度審視 6 層 checker
│   ├── android-build.md             · Android build 全紀錄（stage 0~6）
│   ├── dossier-revision-status.md   · dossier §四 修訂進度 (P0/P1/P2)
│   ├── sc2-translation-workflow.md  · 使用者風格 + pipeline 血淚
│   ├── starmap-zh-tw.md             · 星圖繁中化技術
│   ├── uqm-build.md                 · MSYS2 MINGW32 build
│   ├── uqm-debugging.md             · game.log + Lua template + report.c
│   ├── uqm-font-hacks.md            · 34 個字型 + patches 007/009/010/011
│   ├── uqm-tools.md                 · dashboard + selfverify + CJK 陷阱
│   ├── uqm-translation-purity.md    · purity gate + canonical race names
│   └── uqm-translation-style.md     · voice / OUT_TAKES / Unicode 陷阱
│
├── session-notes/         ← 3 個過去 session 的重要決策快照
│   ├── audit-progress.md            · Round 5 audit 進度
│   ├── ilwrath-v3-decisions.md      · Ilwrath v3 rebuild 決策
│   └── thraddash-rebuild.md         · Thraddash 升級 P0 全面重寫
│
└── prompts/               ← AI 翻譯提詞（10 個範本）
    ├── _MAIN_PROMPT_SC2_zh-TW.md    · ★ 主提詞（翻譯總監人設）
    ├── Translate_Dialogue.md        · 對話翻譯
    ├── Translate_Lore.md            · 敘事/掃描報告翻譯
    ├── Translate_Race.md            · 種族 dossier 翻譯
    ├── Translate_Item.md            · 物品/科技命名翻譯
    ├── Reaudit_Dialogue.md          · 對話重審（Level 3）
    ├── Rebuild_And_Compare.md       · 重建+對照 workflow
    ├── QA_Check.md                  · QA 檢查清單
    ├── Terminology_Audit.md         · 術語稽核
    └── Cross_Race_Dialog_Audit.md   · 跨族對白稽核
```

## 4. 常見任務 → 從哪找起

| 任務 | 起點文件 |
|---|---|
| 翻譯一個新種族的對白 | prompts/_MAIN_PROMPT + prompts/Translate_Dialogue + memories/uqm-translation-style |
| 深度審視某族既有翻譯 | memories/audit-policy（6 層流程）+ prompts/Reaudit_Dialogue |
| 種族全面重譯 | prompts/Rebuild_And_Compare + memories/dossier-revision-status |
| 修 build/package 錯誤 | memories/uqm-build + memories/uqm-debugging |
| 修 CJK 顯示問題 / 溢出 | memories/uqm-font-hacks（重要！有 8 個死結案例）|
| Android APK 相關 | memories/android-build（stage 0~6 完整流程 + 34 個 patch）|
| 星圖中文化 | memories/starmap-zh-tw + prompts/Translate_Lore |
| 使用者「深度審視 X」 | memories/audit-policy → 觸發 6 層 checker，別跳步 |
| 使用者發現「有簡體字/typo」 | memories/uqm-translation-style Unicode 陷阱清單 |

## 5. Voice registry 速查（每族自稱）

| 族 | 主自稱 | 場合 | 誤用陷阱 |
|---|---|---|---|
| Utwig 憂特 | 我族 / 我方 / 本監督團 | 全族現代學者+官樣文 | ✗ 文言「吾/爾/之/乃」 |
| Kzer-Za 烏寬 | 本艦 / 我方 / 我 | drone 冰冷征服者 | ✗ 「本平台/本領主」（v0.9 廢除）|
| Kohr-Ah | 我方 / 我族 | 極簡冷酷宣告 | ✗ 文言判斷句「吾等淨化」|
| Yehat 翼哈特 | 本騎士 / 吾族 | 蘇格蘭勇士古老腔 + BRAAK! | ✗ 「吾/爾/汝」 |
| Shofixti 修烈士 | 俺（田中）/ 本人（武士刀）| 熱血 anime 武士 | ✗ 文言化 |
| VUX | 我族 VUX / 本官(ZEX) | 主族現代口語毒舌 + ZEX 上將官樣 | ✗ 「爾等」 |
| Chmmr | 我等 | 全大寫神諭爆發 | ✗ 「吾等」post-fusion |
| Chenjesu | 我等 | 全小寫詩意冥想 | ✗ 感嘆號、驚嘆句 |
| Dnyarri 蟾亞 | 本尊（覺醒）/ 我（假甦醒）| villain 黑色 + `-<CAPS>-` 心控 | ✗ 「本座」（廢除）|
| Ilwrath 蛛狂 | 本族蛛狂 / 我等 | 宗教莊嚴 + 「、」分隔 + 首字大寫 icon | ✗ 現代口語「音箱/優質」|
| Syreen 塞蓮 | 我族 / 我等姐妹 / 咱倆 | 母系氏族+姐妹情+悼母星 | ✗ 「我方」濫用 |
| Spathi 史怕 | 小的 / 本蟹 / 敝下 | 膽小鬼+發抖語 | ✗ 「我方」濫用 |
| Thraddash 撻伐 | 本戰士 / 本英雄 | 戰士自誇 + Great Teacher 反轉 | ✗ 過度文言 |
| Melnorme 梅諾商 | 敝方 | 商人+資訊仲介 | ✗ 「我方」濫用 |
| Druuge 毒賈 | 敝商會 | 商賈語 + Statute 法律條款 | ✗ 「我方」濫用 |
| Arilou 阿麗露 | 我族 | 古典飄渺 + UFO/新時代玄學 | ✗ 直白俗氣 |
| Supox 蘇菩 | 本群 / 群落 | 根系語 + Mirror Mimicry | ✗ 「我方」 |
| Umgah 陰嘎 | 本團塊 | Pidgin 缺主詞冠詞 + 心控 CAPS PERIODS | ✗ 「我方」濫用 |
| Zoq-Fot-Pik | 三聲部各異 | 三方連續拌嘴 · 一行一句 | ✗ 單一自稱 |
| Orz 歐茲 | 歐茲 / 歐茲們 | *星號詞* 保留 · 非「我方」 | ✗ 星號縮水 |
| Pkunk 普恩 | 我族 | 靈性緩慢 · 88 處 pause 節奏 | ✗ 節奏太快 |
| Slylandro 斯萊 | 我族 | 氣態原住民好奇熱情 | ✗ 冷淡 |

## 6. 血淚教訓（別再犯）

1. **`\uXXXX` escape 手打錯字** — 100+ 個實錄，例如 `\u5ac0=嫀` vs `\u5acc=嫌`。**永遠貼實際 CJK 字元**，不要打 unicode escape
2. **HD 模式改 SD 字型無效** — 使用者玩 HD 時，改 `zh-TW.uqm` 的字型完全沒感覺（HD 靠 `zh-TW-hd.uqm` 覆蓋）
3. **視覺相似字 typo** — 賈/賣、諾/諸、蠢/蠶、骨/骸、撻/沒、沾/沒——batch replace 後必手動 grep
4. **不要用 `**` markdown 粗體** — 引擎不解析（除 Orz `*星號詞*`），會字面顯示星號
5. **Lua template 別動** — `<% comm.getStarName(...) %>` 改壞就整族錯位
6. **`\n` 過多切碎 OGG** — 保持與英文原文一致的 `\n` 數量，用空格 wrap
7. **CJK 無空格觸發無限迴圈** — `commander.fon` AlienTextWidth=143px 場景 · 用 space-wrap 或 patch 006

## 7. 我做完事情要告訴使用者什麼

- **簡潔** · 使用者不想看長篇大論
- **結構化** · 用表格與 checklist
- **具體** · 哪個檔案、哪一行、哪個 canonical
- **給選項** · 若有多方案，A/B/C + 我推薦哪個 + 理由
- **對照英文原文** · 讀順度問題附 EN 原文，避免使用者質疑

## 8. 何時要「先確認再做」

- 動 `Master_Glossary.md`（權威 canonical）→ 一定要確認
- 動 dossier §四 語體定位 → 一定要確認
- 動 100+ 個 tokens 的 batch replace → 先給 dry-run 清單
- 觸控 UI 佈局改動 → 先給草圖或 mock（Android）
- Push 到 GitHub → **一定要確認**
- 動任何 keystore/簽章相關 → **絕對不能自作主張**

---

**Happy translating!** 這個專案累積了 3547 tokens 的翻譯 + 34 個引擎 patch + 20 章 dossier 的心血，麻煩你接手時謹慎為之。有疑問就問使用者，不要臆測。
