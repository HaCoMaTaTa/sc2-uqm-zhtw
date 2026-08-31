# Translation Memory 翻譯記憶

> **本檔功能**：**shipped v0.3 產品譯文**作為 translation memory 的**使用方法**。已翻譯的 JSON 是最佳的**譯法參考**——本檔說明如何利用它。
> **物理路徑**：`uqm-work/translations/*.zh-TW.json`

---

## 一、什麼是 Translation Memory (TM)

在專業翻譯中，**Translation Memory** 是**已翻譯過的原文-譯文對**的資料庫。翻譯者遇到新文本時，可**查找相似的既有譯法**，確保**一致性**。

SC2 專案的 TM 分兩類：

| 類型 | 來源 | 用途 |
|---|---|---|
| **shipped v0.3 JSON** | `uqm-work/translations/*.zh-TW.json` | **已在遊戲中運作**的譯文；翻新內容或審查時的黃金標準 |
| **Race dossier 對話範例** | `02_Races/[Race].md` §六 | 該族的**理想**譯法示範（含翻譯理由） |

---

## 二、shipped v0.3 JSON 一覽

**現行已翻譯的族**（18 檔）：

| JSON 檔 | 種族 | 狀態 |
|---|---|---|
| `arilou.zh-TW.json` | 阿麗露 | v0.3 已 shipped |
| `chmmr.zh-TW.json` | 查姆族 | v0.3 已 shipped |
| `commander.zh-TW.json` | 海斯艦長 | v0.3 已 shipped |
| `druuge.zh-TW.json` | 毒賈族（原德魯族） | v0.3 已 shipped，需 v0.4 rename |
| `gamestrings.zh-TW.json` | 系統文字 | v0.3 |
| `ilwrath.zh-TW.json` | 蛛狂族 | v0.3 |
| `intro.zh-TW.json` | 開場敘事 | v0.3 |
| `kohrah.zh-TW.json` | 烏寬柯亞 | v0.3 |
| `orz.zh-TW.json` | 歐茲族 | v0.3 |
| `pkunk.zh-TW.json` | 普恩族 | v0.3 |
| `setupmenu.zh-TW.json` | 設定選單 | v0.3 |
| `shofixti.zh-TW.json` | 修烈士族（原蘇菲斯特族） | v0.3，需 v0.4 rename |
| `slylandro.zh-TW.json` | 斯萊族 | v0.3 |
| `spathi.zh-TW.json` | 史怕族 | v0.3 |
| `supox.zh-TW.json` | 蘇菩族（原蘇波族） | v0.3，需 v0.4 rename |
| `syreen.zh-TW.json` | 塞蓮族 | v0.3 |
| `urquan.zh-TW.json` | 烏寬克澤札 | v0.3 |
| `yehat.zh-TW.json` | 翼哈特族（原葉哈特族） | v0.3，需 v0.4 rename |

**未翻譯的族**（9 檔待翻）：

| 種族 | 對應 comm 檔案 |
|---|---|
| **Androsynth** 安卓辛族 | `androsynth/` |
| **Chenjesu** 晶智族 | `chenjesu/` |
| **Mmrnmhrm** 姆姆族 | `mmrnmhrm/` |
| **Mycon** 麥孔族 | `mycon/` |
| **Talking Pet / Dnyarri** 蟾亞族／會話寵 | `talkingpet/` |
| **Thraddash** 撻伐族 | `thraddash/` |
| **Umgah** 陰嘎族 | `umgah/` |
| **Utwig** 憂特族 | `utwig/` |
| **VUX** VUX | `vux/` |
| **Zoq-Fot-Pik** 佐-佛-皮 | `zoqfotpik/` |
| **Melnorme** 梅諾商 | `melnorme/` |
| **Yehat Rebels** 翼哈特叛軍 | `yehatrebels/` |
| **Safe Ones** 平安族（史怕自稱） | `safeones/` |
| **Robot** 機器人 | `robot/` |
| **Starbase** 星際基地 UI | `starbase/` |
| **Melnorme** 梅諾商 | `melnorme/` |
| **Probe** 斯萊探測器 | `probe/` |

---

## 三、翻譯新族時的 TM 查找步驟

### 3.1 查該族已有沒有現行譯文

```powershell
# 檢查 uqm-work/translations/ 是否有該族的 zh-TW.json
Get-ChildItem uqm-work/translations/*.zh-TW.json | Where-Object { $_.Name -match "orz|melnorme" }
```

### 3.2 若有，先讀該族 shipped 譯文

- 是 v0.3 → v0.4 canonical，**先做名詞替換**
- 是 v0.4 → 直接沿用譯法（一致）

### 3.3 若無，讀該族 dossier `02_Races/[Race].md`

- **§六 對話範例** 有理想譯法示範
- **§五 中文化翻譯規則** 有應做／應避免的清單
- **§四 語言風格** 有自稱／稱呼玩家／核心詞彙／情緒觸發雷區

### 3.4 查跨族相似句型

若原文有**跨族相似對白模式**（如「別打了—— 我不是烏寬！」在多族出現），**參考已翻族的 shipped 譯文**確保一致：

```powershell
# 找出「別打了」在多族的譯法
Select-String -Path uqm-work/translations/*.zh-TW.json -Pattern "別打了"
```

---

## 四、TM 使用原則

### 4.1 shipped v0.3 譯名 → v0.4 需 rename

**v0.4 使用者重設 8 個種族名**（Phase 8.5b）：

| shipped v0.3 舊 | v0.4 canonical |
|---|---|
| 撒達許族 | 撻伐族 |
| 蘇菲斯特族 | 修烈士族 |
| 阿姆嘎族 | 陰嘎族 |
| 葉哈特族 | 翼哈特族 |
| 尼亞里族 | 蟾亞族 |
| 蘇波族 | 蘇菩族 |
| 德魯族 | 毒賈族 |
| 梅爾諾 | 梅諾商 |

**翻新內容時**：**一律用 v0.4 canonical**；**參考 shipped v0.3** 時要**同步替換**這些名詞。

### 4.2 shipped v0.3 譯法優先

**非種族名的譯法**（動詞、形容詞、句式），若 shipped v0.3 有既定譯法，**優先沿用**（除非 v0.4 明文更新）。

**理由**：
- shipped 已在遊戲中運作，玩家已熟悉
- 保留一致性避免翻譯風格漂移

**範例**：
- shipped v0.3 用「戰略性撤退」翻 `strategic retreat` → 新譯也用
- shipped v0.3 用「爾等蟲豸」翻 `mindless worm` → 新譯也用

### 4.3 shipped v0.3 譯法**不採用**的情境

- **明顯錯誤**（如簡體字混入）→ 修正
- **v0.4 明文更新**（如 8 個種族名）→ 替換
- **shipped 譯法有爭議**（見 [Error_List.md](../11_QA/Error_List.md)）→ 依 [Master_Glossary.md](../07_Glossary/Master_Glossary.md) 為準

---

## 五、跨族對照學習

### 5.1 相似人格模式

若新族與已翻族**人格類型相似**，參考已翻族的譯法：

| 已翻族 | 相似的新族 | 借鑒重點 |
|---|---|---|
| 蛛狂族（狂信禱詞）| 麥孔（宗教有機）| 禱詞句式、儀式化 |
| 憂特族（憂鬱雙階段）| 待新族 | 兩期切換手法 |
| 修烈士族（田中/武士刀）| 待新族 | 兩人 voice 對比 |

### 5.2 玩家 response 沿用

**玩家 response 台式順口通則** 各族共通——已翻族的玩家 response 譯法可**直接沿用**：

```powershell
# 找 dont_attack 在各族的譯法（都是玩家對嗆／和解 response）
Select-String -Path uqm-work/translations/*.zh-TW.json -Pattern '"dont_attack"'
```

---

## 六、TM 的限制

### 6.1 shipped v0.3 有錯誤

**已知問題**（會在 [Error_List.md](../11_QA/Error_List.md) 累積）：

- shipped v0.3 `_notes` 有些誤植（如 shofixti.json 說「Mycon = 梅蒙族」，實際主流是「麥孔族」）
- 部分 Lua template 內的 star name fallback 未 CJK 化

### 6.2 shipped v0.3 用舊 canonical

**8 個 v0.4 重設** 尚未同步到 shipped。翻新族時**用 v0.4**，不要沿用 shipped 的舊名。

---

## 七、TM 更新流程

**每翻完新族後**：

1. 譯文放進 `uqm-work/translations/[race].zh-TW.json`
2. `_notes` 加入版本標記（見 [Dialogue_Rule.md](../08_Translation_Rules/Dialogue_Rule.md) §八）
3. **git commit** 該檔（便於未來追溯）
4. 若發現該族的**新譯法可作範例**→ 補入 `02_Races/[Race].md` §六 對話範例

---

## 八、參考來源

- shipped v0.3 譯文：`uqm-work/translations/*.zh-TW.json`
- [Master_Glossary.md](../07_Glossary/Master_Glossary.md)
- [Forbidden_Translation.md](Forbidden_Translation.md)（本目錄）
- [Error_List.md](../11_QA/Error_List.md)
