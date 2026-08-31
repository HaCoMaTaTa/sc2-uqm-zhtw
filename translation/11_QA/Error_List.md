# Error List 錯誤累積清單

> **本檔功能**：**已發現的翻譯錯誤**與**待決議問題**的累積記錄。用於：
> - **翻譯者**：了解已知問題，避免重犯
> - **QA**：追蹤修正狀態
> - **使用者**：批次決策時的清單
> **更新原則**：每次發現新問題**立即補入**；已修正的**標記狀態**。

---

## 一、v0.4 使用者重設種族名（8 個）— **待 Phase 8.6 同步**

**狀態**：**dossier 側已修**（Phase 8.5b 完成），**shipped v0.3 JSON 未同步**。

| shipped v0.3 舊 | v0.4 canonical | 影響的 JSON 檔 |
|---|---|---|
| 撒達許族 → | 撻伐族 | ilwrath.json、shofixti.json、其他多族的 `_notes`／dialogue 交叉引用 |
| 蘇菲斯特族 → | 修烈士族 | shofixti.json、其他多族 |
| 阿姆嘎族 → | 陰嘎族 | spathi.json、其他多族 |
| 葉哈特族 → | 翼哈特族 | yehat.json、pkunk.json、其他多族 |
| 尼亞里族 → | 蟾亞族 | chmmr.json、orz.json、其他多族 |
| 蘇波族 → | 蘇菩族 | supox.json、utwig.json、druuge.json |
| 德魯族 → | 毒賈族 | druuge.json、utwig.json |
| 梅爾諾 → | 梅諾商 | melnorme.json、其他多族 |

**動作**：Phase 8.6 執行時，需**批次替換**所有 `translations/*.zh-TW.json`。

---

## 二、shipped v0.3 `_notes` 誤植

### 2.1 shofixti.json `_notes` 誤植 3 族名

**問題**：`_notes` 記錄「Mycon = 梅蒙族」「VUX = 蛛狂族」——**皆錯**。

**正確**：
- Mycon = 麥孔族（chmmr/arilou.json 主流）
- VUX = VUX（保留原文，無「族」字）
- 蛛狂族 = **Ilwrath**，非 VUX

**狀態**：dossier 已修正；`_notes` 待 Phase 8.6 修正。

**影響**：僅是 `_notes` 記錄錯誤——**dialogue 內文正確**（用「麥孔」「VUX」）。

---

## 三、命名衝突／待決議

### 3.1 三重「復仇者」衝突

| 譯名 | 對應英文 | 對應種族 |
|---|---|---|
| **復仇者號**（有「號」）| Vindicator | 玩家旗艦 |
| **宿敵號（Nemesis）** | Nemesis | 歐茲族 · **v0.5.2 canonical 升級**（舊「復仇者號」廢止）|
| **復仇者**（無「號」） | Avenger | 蛛狂族 |
| **復仇號** | Avatar / Avenger | 查姆族 |
| **復仇艦** | Vindicator（艦級名） | 玩家艦級名（罕見）|

**狀態**：**v0.5.2 已解決撞名**（D11 starbase Reaudit）：Orz Nemesis 改「宿敵號」避開玩家 Vindicator=復仇者號 撞車。詳見 [Ship_Names.md](../07_Glossary/Ship_Names.md) §5.1。

### 3.2 兩個 Torch

| 譯名 | 對應英文 | 對應種族 |
|---|---|---|
| **火炬艦** | Torch | 撻伐族（v0.2 明確） |
| **火炬艦**（暫用） | Fury / Torch？ | 普恩族（待議） |

**狀態**：普恩艦名待 shipped 檔（pkunk.zh-TW.json）確認。目前**暫用「憤怒者」**避開衝突。

**待決策**：Phase 12+ 讀 pkunk.zh-TW.json 確認實際使用。

### 3.3 Chmmr 主艦命名

- **官方英文**：**Avatar**
- **v0.2 中譯**：復仇號
- **Ultronomicon 舊譯**：Avenger

**狀態**：**保留 v0.2「復仇號」**。若日後 shipped 檔明確用 Avatar → 阿凡達，Phase 9 再修訂。

### 3.4 Cutter、Behemoth 具體歸屬

**狀態**：v0.2 vocab 表有譯名（切割艦、巨獸），但**未標明所屬種族**。

**待決策**：Phase 12+ 讀 melee-UI 相關文件確認。

### 3.5 Melnorme 貿易艦名

- **v0.2 未鎖定** melnorme trader 的中譯
- **v0.4**：暫定「梅諾商貿易艦」

**狀態**：暫定，等 shipped melnorme.zh-TW.json 譯完再確認。

### 3.6 Ultron 三個組件的中譯

**已鎖定**：玫瑰球體（Rosy Sphere）

**暫定**：
- Aqua Helix → **水螺旋**（暫定）
- Clear Spindle → **清澈紡錘**（暫定）
- Umgah Hyperspatial Terror → **陰嘎超空間恐懼**（暫定，v0.4 已用陰嘎族）

**狀態**：Phase 8+ 議定。

### 3.7 其他暫定術語

- **Deep Child**（麥孔用來播種／攻擊行星的裝置）→ **深子**（暫定）
- **Excruciator**（烏寬對抗蟾亞的痛楚裝置）→ **極痛裝置**（暫定）

**狀態**：Phase 8+ 議定。

---

## 四、格式錯誤（統計）

**shipped v0.3 JSON 待做的 QA 檢查（Phase 8.6 前）**：

| 檔案 | 待檢項 |
|---|---|
| 所有 18 檔 | v0.4 名詞替換 |
| 所有 18 檔 | 簡體字掃描 |
| 所有 18 檔 | 感嘆詞是否保留原文 |
| orz.zh-TW.json | Orz 星號詞語格式驗證 |
| shofixti.zh-TW.json | 日文人名保留（例外 OK） |

**狀態**：Phase 11 CI 腳本可自動化，執行後補入本清單。

---

## 五、既往修正紀錄（Phase 8.5 期間）

**已修正的 typo**（我 batch 過程中引入、已 revert）：

| Typo | 正確 | 已修正檔 |
|---|---|---|
| 掻（U+63BB） | 撻（U+64BB） | 5 檔（Thraddash 相關） |
| 梅諺（U+8AFA） | 梅諾（U+8AFE） | 13 檔（Melnorme 相關） |
| 蟾譽（U+8B7D）| 蟾蜍（U+8735）| Galactic_History.md |
| 蟾蜜（U+871C）| 蟾蜍（U+8735）| Galactic_History.md |
| 蟾蜵（U+8735）| 蟾蜍 | Fixed_Terms.csv、Race_Names.md（**使用者手動修正**） |
| 克澄（U+6F84）| 克澤（U+6FA4） | Ur_Quan_Kzer_Za.md、Galactic_History.md |
| 克潤（U+6F6A）| 克澤（U+6FA4）| Ur_Quan_Kohr_Ah.md |
| 翞辱（U+7FDE）| 羞辱（U+7F9E） | Thraddash.md |
| 兀／兕 | 兇（U+5147） | Thraddash.md |
| 神諡（U+8AE1）| 神諭（U+8AED） | Ilwrath.md |
| 羞恻 | 羞恥 | Political_System.md |
| 彻底（簡體）| 徹底（U+5FB9） | Ur_Quan_Kohr_Ah.md |
| 鞭払（日語漢字）| 鞭打 | Race_Names.md、Fixed_Terms.csv |
| 圍剤 | 圍剿 | Galactic_History.md |

**狀態**：**全部已修正**。無殘留。

---

## 六、報告新問題

**發現新問題時**，補入本檔對應章節。格式：

```markdown
### X.Y [簡稱]

**位置**：[檔案] / [行號]
**問題**：[描述]
**正確**：[建議]
**狀態**：[待議 / 已修 / 已 Skip]
**備註**：[如有]
```

**Phase 8.6+**：Consistency_Check.py 執行後產出的 report，**新問題**在此累積。

---

## 七、參考來源

- [Consistency_Check.md](Consistency_Check.md) CI 腳本
- [Master_Glossary.md](../07_Glossary/Master_Glossary.md) 權威名詞
- [Forbidden_Translations.md](../07_Glossary/Forbidden_Translations.md) 禁譯清單
- Phase 8.5b 對話（Copilot 執行歷史）
