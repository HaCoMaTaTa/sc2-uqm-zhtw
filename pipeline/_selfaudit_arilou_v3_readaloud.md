# Arilou Read-Aloud Self-Audit (2026-08-17)

**Rebuild-Compare workflow**: `StarControl2_TW_Localization/09_AI_Prompt/Rebuild_And_Compare.md` §四·階段 2.5
**Target**: `uqm-work/translations/arilou.zh-TW.v3.json`
**pre-fix source**: `uqm-work/translations/arilou.zh-TW.v3.partial-{1,2,3}.json`（未動）

## 統計

- Total tokens: 97
- 命中「直譯生硬」項目: **4**（4.1%）
- 分類：
  - § 4.5.1 英文語法殘留：0
  - § 4.5.2 中文語感問題：**3**（詞義精準度 2 · 語序台化 1）
  - § 4.5.3 標點/排版：0
  - § 4.5.4 Voice / dossier 一致性：**1**（BJ 兒化音 → TW natural）
- 未動 tokens: 93

## 修訂項

### #1 · FRIENDLY_SPACE_HELLO_1 · § 4.5.4 BJ 兒化音違 v0.7 dossier

**pre-fix**:
> 啊…… 我們的人類朋友。 來，讓我們聊**一會兒**吧。

**self-fix**:
> 啊…… 我們的人類朋友。 來，讓我們聊**一會**吧。

**類別**: § 4.5.4 Voice/dossier 一致性 · dossier v0.7 明列 `❌ 兒`（Beijing 兒化音）為禁用文言助詞
**理由**: 「一會兒」是北京話兒化音，TW natural 用「一會」/「一下」。

---

### #2 · THESE_THINGS · § 4.5.2 詞義精準度

**pre-fix**:
> 我們**追求**捕捉 *Nnngn*，但牠們敏捷跳躍。

**self-fix**:
> 我們**試圖**捕捉 *Nnngn*，但牠們敏捷跳躍。

**類別**: § 4.5.2 中文語感問題 · 動詞語義精準
**理由**: 英文 `seek to trap` → 「試圖捕捉」符合 seek 語義（嘗試/追尋目的）；「追求捕捉」讀起來像追求某種抽象目標（如「追求愛」），語感不對。

---

### #3 · ARILOU_HINTS_1 · § 4.5.2 詞義精準度

**pre-fix**:
> 用艦艇與武器…… **血肉與骨骼**…… 不行。

**self-fix**:
> 用艦艇與武器…… **鮮血與骨骼**…… 不行。

**類別**: § 4.5.2 中文語感問題 · 詞義對應原文
**理由**: 英文 `blood and bones` → 「鮮血與骨骼」；「血肉」對應 `flesh`（肉體），不是 `blood`。Arilou 這裡是 elegantly describing 「戰士的付出（鮮血）與遺骸（骨骼）」，不是 flesh。

---

### #4 · WE_NEVER_FRIENDS · § 4.5.2 語序台化

**pre-fix**:
> 艦長，我們一直**與你追求友善的相伴**\
> 儘管我們原本可以輕易地就對你進行那類實驗。

**self-fix**:
> 艦長，我們一直**尋求與你友善相伴**\
> 儘管我們原本可以輕易地就對你進行那類實驗。

**類別**: § 4.5.2 中文語感問題 · 語序台化
**理由**: 英文 `We have sought amiable companionship with you` → 中文順序調整為「尋求 + 與你 + 友善相伴」讀起來像母語人；原譯「與你追求友善的相伴」讀起來有英文 SVO 逐字譯的痕跡（追求「XX 的相伴」定語冗長）。

---

## 未動 tokens 檢查（讀順度已通過）

- **93/97 tokens** 讀順度自審通過（無需自動修訂）
- 「我方」削減 **93%**（shipped 168 → v3 11，全部為 Alliance 政治語境合理保留）
- 「兒」化音 0（fix 後）
- 「爾」3 皆為專名（凱爾特/戈爾諾/羅斯威爾）· 非文言助詞 · purity 檢查已 confirm race=0
- 「之」53 處使用皆為現代 TW natural 連詞（之間/之中/之後/之時/之處/之一）或 Arilou 招牌詩意（容易之地 × 3 · 具形之軍力）· 非文言助詞
- 半形標點：0 殘留
- Lua template：8 全 CJK first-args + count match

## 邊界原則遵守

- ✅ 未動 canonical 詞（如 `*時*` 星號 icon / `*Nnngn*` / `深層幼體` / `教義戰爭`）
- ✅ 未動招牌 UFO 迷因 canonical（MIB 星際戰警 / 藍皮書計畫 / Roswell / Celts / 麥田圈 / 失憶的日子 / Be seeing you...）
- ✅ 未動 dossier §四 4 sub-modes voice icon（Arilou 個體「我」/ 集體「我們」/ 族性「我們阿麗露」）
- ✅ 未讀 shipped 決定 self-fix（4 修訂皆基於英文原文對照 + 中文語感）
- ✅ 保留原文語氣、節奏、資訊密度（不加不減）
