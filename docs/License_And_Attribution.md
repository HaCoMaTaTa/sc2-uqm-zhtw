# 授權說明與致謝 · License and Attribution

> 本專案採**分離授權**：程式碼採 GPL-2.0、內容資產採 CC BY-NC-SA 2.5。
> 這是遵循上游 UQM/MegaMod 的授權方案。

---

## 一、快速對照

| 資產類別 | 授權 | 你能做什麼 | 條件 |
|---|---|---|---|
| **引擎源碼**（`patches/*.patch` 修改 UQM-MegaMod）| GPL-2.0 | 自由用/改/散布 | 衍生作品也必須 GPL；分發 APK/exe 時提供源碼取得方式 |
| **腳本**（`pipeline/*.py`, `*.ps1`, `scripts/*.ps1`）| GPL-2.0 | 同上 | 同上 |
| **翻譯文字**（`translation/`, `pipeline/translations/*.zh-TW.json`）| CC BY-NC-SA 2.5 | 自由用/改/散布 · 但**只能非商業** | 標明原作者 · 衍生作品用相同授權 |
| **字型 raster**（`pipeline/zh-TW-addon/content/base/fonts/*.png`）| CC BY-NC-SA 2.5 | 同上 | 同上 |
| **圖示 / 美術**（`android/_icon_candidates/*.png`）| CC BY-NC-SA 2.5 | 同上 | 同上 |
| **遊戲說明書**（`docs/Game_Manual_zh-TW.md`）| CC BY-NC-SA 2.5 | 同上 | 同上 |
| **開發文件**（本檔、SOP、README）| CC BY-NC-SA 2.5 | 同上 | 同上 |

## 二、我可以...

### ✅ 可以

- 免費下載、複製、分享 APK / PC zip 給朋友
- 上傳到個人網盤（Dropbox, Google Drive, MediaFire）分享連結
- 在論壇（PTT, Discord, Reddit）貼下載連結
- 錄製遊戲實況影片並上傳 YouTube/Twitch（含被動廣告收入者見下方細則）
- Fork 本 repo · 修改翻譯 · 發自己的 fork release
- 用本專案的翻譯做二次創作（同人小說、影片、藝術）· 前提是**非商業**
- 商業媒體引用**做評論、報導、教育用途**（fair use）

### ❌ 不可以

- **賣 APK / PC 版本**（無論是收費下載、訂閱、廣告變現）
- **上架 Google Play Store 商業版**（Play 商業平台性質與 CC-NC 有衝突 · 見下方分析）
- **重製美術/翻譯後改成閉源商業產品**（違反 GPL 與 CC-SA）
- **移除原作/上游/本 repo 署名**（違反 GPL §1 與 CC BY）
- **用於任何商業廣告代言 / 推廣付費服務**

## 三、Google Play Store 上架的風險分析

**為什麼不上架**：

1. **CC BY-NC-SA 的 NonCommercial 定義爭議**
   - CC 官方對「NC」定義：「以商業利益或金錢報酬為主要目的」
   - Google Play 是**商業應用商店**，開發者協議、平台本身有廣告 SDK 生態
   - 即使 App 完全免費，被權利人（Toys for Bob / UQM Team / MegaMod 作者）主張「商業分發」而檢舉，可能下架
   - 學界與律師意見分歧，**保守做法就是不上**

2. **商標問題**
   - 「Ur-Quan Masters」「Star Control」是 Toys for Bob / Activision 的商標
   - CC 授權不涵蓋商標
   - Play Store 上架需要 App 名稱識別，可能被商標爭議下架

3. **GPL 合規負擔加大**
   - Play Store 上架的 App 需提供源碼取得方式（GPL §3）
   - 本 repo 已提供 · 但 Play 用戶不會自動看到 · 需在 App 內附連結

4. **上游作者未明確授權**
   - UQM Team 與 MegaMod 作者沒公開表態「同意粉絲上架 Play」
   - 沒同意就上，法律上灰色

**建議**：
- 僅走 **GitHub Releases** + **個人分享**（100% 安全）
- F-Droid 可能接受（若 F-Droid 決定接受 CC-NC）· 但至今 F-Droid 對 CC-NC 資產仍偏保守

**參考**：
- CC 官方 NC FAQ: <https://creativecommons.org/faq/#does-my-use-violate-the-noncommercial-clause-of-the-licenses>
- UQM 上游 team 曾釋出 Android APK 於 SourceForge（非 Play Store）

## 四、實況主 / 影片創作者

**歡迎錄影上傳 YouTube/Twitch/bilibili**，但請：

### ✅ OK
- 標題或影片說明附上原作 + 本專案連結
- 頻道有訂閱 / 廣告收入（YouTube 分潤機制屬於「頻道收入」非 App 商業化）
- 打賞 / Super Chat / 抖內

### ⚠️ 建議諮詢
- 影片被廣告主明確贊助（可能牽涉商業推廣）
- 拿本專案的翻譯或美術做二次商業周邊（貼紙、T-shirt、遊戲手把包裝）

### ❌ 不 OK
- 把 APK 上傳到有付費下載機制的平台（含變相付費：付費會員專屬連結等）
- 收費授權其他人「代下載」

## 五、翻譯修改與二次發布

**歡迎 fork！** 但請：

1. **保留原始署名**（本 repo 作者 + 上游）
2. **公開你的修改**（fork 到 GitHub 即符合 SA）
3. **相同授權**：你的 fork 也用 GPL-2.0（程式碼）+ CC BY-NC-SA 2.5（內容）
4. **公開 diff**：在 fork README 註明「基於 [本 repo] · 修改了 A/B/C」

若你想**併回主 repo**，開 PR，我會很開心地 review。

## 六、GPL-2.0 源碼取得方式

依 GPL §3(a)：

> Accompany [the distributed executable] with the complete corresponding machine-readable source code

我們透過**本 GitHub repo 本身**提供源碼：

- **引擎源碼** = `patches/UPSTREAM_COMMIT.txt` 記錄的上游 commit（`dc2a4e6`）+ 本 repo `patches/*.patch`
- **腳本源碼** = 本 repo `pipeline/`, `scripts/`

任何拿到本 repo APK / PC zip 的人，可以：
```
1. 點 GitHub Repo URL（在 README、APK about 頁）
2. Clone 或下載 zip
3. 跑 scripts/setup_upstream.ps1 → 就是完整源碼
```

若本 repo 未來下架，可透過：
- Internet Archive Wayback Machine 保留的快照
- 上游 <https://github.com/JHGuitarFreak/UQM-MegaMod> commit `dc2a4e6`
- 本 repo 授權以 CC BY-NC-SA 2.5 允許轉載，你也可以自己保留一份備份

## 七、CC BY-NC-SA 2.5 署名格式

**在你的作品中**（影片、二創、fork）建議這樣寫：

```
本翻譯內容衍生自：
- 原作 Star Control II / The Ur-Quan Masters
  (© 1992 Toys for Bob · Fred Ford, Paul Reiche III)
- UQM 開源引擎 (Ur-Quan Masters Team)
- MegaMod 分支 (JHGuitarFreak)
- 繁體中文化 (激戰M星雲II) : [repo URL]

授權：Creative Commons BY-NC-SA 2.5
      https://creativecommons.org/licenses/by-nc-sa/2.5/deed.zh_TW
```

**在你的 fork README** 建議這樣寫：

```
This is a fork of [sc2-uqm-zhtw](https://github.com/...).
Modifications:
- Fixed X in Y
- Added Z

Original credits: see NOTICE / AUTHORS.md
License: GPL-2.0 (code) + CC BY-NC-SA 2.5 (content)
```

## 八、完整授權原文位置

- **GPL-2.0**：[`../LICENSE`](../LICENSE)（GNU 官方原文）
- **CC BY-NC-SA 2.5**：<https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode>
- **中文摘要**：[`../LICENSE.CONTENT`](../LICENSE.CONTENT)
- **第三方致謝**：[`../NOTICE`](../NOTICE)
- **貢獻者**：[`../AUTHORS.md`](../AUTHORS.md)

## 九、常見問題

**Q**：我可以把 APK 燒進我賣的 Android 遊戲主機嗎？
**A**：不可以。硬體綁定 APK = 商業分發。

**Q**：我可以在同人展做 USB 隨身碟送人嗎（免費）？
**A**：可以。免費贈品 = 非商業。建議 USB 內附 NOTICE 文字檔。

**Q**：我可以做繁中版的攻略書（收費）嗎？
**A**：攻略本身你寫的原創內容 = 你的著作。若引用本專案的翻譯，屬於「引用/fair use」通常 OK。若直接複製大段翻譯 = 需要遵守 CC-SA 授權（=攻略書也要 CC-SA）。

**Q**：Play Store 上架真的完全不行嗎？
**A**：主要卡在 CC-NC。若你能取得**上游 UQM team + MegaMod 作者的明確書面授權**，且解決 Ur-Quan Masters 商標，理論上可以。但這是律師層級的問題，不建議個人玩家嘗試。

**Q**：可以捐款支持專案嗎？
**A**：目前沒開放。若未來開，會用「Ko-fi / 開源贊助」而非賣 App。

## 十、聯絡

有授權疑問請開 GitHub Discussion 或 Issue。
