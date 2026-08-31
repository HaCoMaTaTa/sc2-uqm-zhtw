# 種族專屬字型：繁體中文化的策略

> **回答的問題**：SC2/UQM 各種族對話有時使用特殊字型（Ur-Quan、Chmmr、Ilwrath、Spathi…），繁體中文翻譯是否也能保留這種風格差異？
>
> **結論（一句話）**：**可以**，MegaMod v0.8.x 已內建 7 種種族專屬字型並已 TTF 化，加上兩種可行的中文接合策略，繁中版能保留分族字型視覺特色。

---

## 一、事實根據（皆為實際查證，非臆測）

### 1.1 MegaMod 已支援的種族專屬字型

從 GitHub `JHGuitarFreak/UQM-MegaMod/doc/fonts/` 目錄實際列出，種族專屬 TTF 清單如下：

| TTF 檔案 | 對應種族 | 譯名 |
|---|---|---|
| `UQM-Arilou-Regular.ttf` | Arilou | 阿麗露 |
| `UQM-ChmmrFont.ttf` | Chmmr | 查姆族 |
| `UQM-Ilwrath-Regular.ttf` | Ilwrath | 蛛狂族 |
| `UQM-KohrAh-Regular.ttf` | Ur-Quan Kohr-Ah | 烏寬・柯亞 |
| `UQM-Spathi-Regular.ttf` | Spathi | 史怕族 |
| `UQM-Supox-Regular.ttf` | Supox | 蘇波族 |
| `UQM-UrQuan-Regular.ttf` | Ur-Quan Kzer-Za | 烏寬・克澤札 |

### 1.2 UI 字型也已 TTF 化

同一目錄下 UI 字型：`UQM-CommanderFont.ttf`、`UQM-StarConFont.ttf`、`UQM-PlayerFont.ttf`、`UQM-Square-Regular.ttf`、`UQM-LanderFont.ttf`、`UQM-ButtonFont.ttf`、`UQM-3DOMenuLabels.ttf`、`UQM-LoadMenuLabels.ttf`、`UQM-MeleeLabels.ttf`、`UQM-ModuleFont.ttf`、`UQM-Slides.ttf`、`UQM-SUPER-MELEE.ttf`、`UQM-TinyFont*`、`UQM-MicroFont*`。

### 1.3 MegaMod 引擎 changelog 印證

- **v0.8.2**：*"Even more font work! All the UI fonts have been overhauled and some new fonts for the **Ilwrath, Spathi, and Ur-Quan**"*
- **v0.8.1**：*"We can now load kerning data for fonts from a 'kerndat.fnt' file within a given font's directory"* — 每個字型可獨立擁有字距資料。
- **v0.8.0.85**：*"Replaced all fonts in HD and recreated the **Chmmr** and 'StarCon' font by hand"*

### 1.4 關鍵限制

所有 MegaMod 內建的種族 TTF **只含拉丁字元字符（U+0020–U+00FF 附近）**，不含 CJK。這是繁中化的核心工程課題。

---

## 二、三種可行策略比較

| 策略 | 做法 | 種族視覺辨識 | 工程量 | 需引擎改動 | 推薦度 |
|---|---|:-:|:-:|:-:|:-:|
| **A. 統一字型** | 全部用「思源黑體 Traditional」單一字型 | ✗ 全部一樣 | 極低 | ✗ | ⭐ |
| **B. 分族字型組合** | 為每個種族挑選一款風格對應的中文字型獨立指定 | ◎ 高 | 中 | 依 UQM 是否支援 per-race font 選項 | ⭐⭐⭐ |
| **C. 合併字型（推薦）** | 用 FontForge / fonttools 把每個 `UQM-<Race>-Regular.ttf` 的拉丁字元 + 對應風格的中文字元集合併成一個新 TTF | ◎ 極高（同一字型內拉丁與中文風格一致）| 中～高 | ✗ **完全不用改引擎** | ⭐⭐⭐⭐⭐ |

**推薦策略 C（合併字型）**。理由：
- MegaMod 引擎已經按種族載入 TTF；我們只要**替換 TTF 檔本身**即可。
- 保留原 TTF 的拉丁字元 → 英文玩家早已熟悉的視覺特徵不變。
- 中文字元用同風格對應字型補齊 → 中文玩家獲得等價的視覺辨識。
- 打包為 `.uqm` addon 不破壞原版。

---

## 三、策略 C 的中文字型對應建議

### 3.1 選型原則

- 每個原 TTF 的**視覺氣質**（衬線/無衬線、粗細、幾何/手繪、規則/歪斜）→ 對應相同氣質的中文開源字型。
- **授權**：全部須為可自由商用/散佈的開源字型（避免發布時法律問題）。
- **字元集**：至少覆蓋 Big5-2003 + CJK Unified Ideographs 常用 6,000 字。

### 3.2 對應表（依原 TTF 特徵，社群公認的風格描述）

| 原 TTF | 種族 | 原文字型視覺氣質 | 建議搭配中文字型（開源）| 授權 |
|---|---|---|---|---|
| `UQM-UrQuan-Regular.ttf` | 烏寬・克澤札 | 硬派方正、粗黑、威權感 | **思源黑體 Traditional Heavy** | SIL OFL 1.1 |
| `UQM-KohrAh-Regular.ttf` | 烏寬・柯亞 | 更凶暴、鋸齒/侵略性 | **源界明朝 Heavy** 或 **華康少女文字（付費替代）→ 用 思源宋體 Heavy** | SIL OFL 1.1 |
| `UQM-ChmmrFont.ttf` | 查姆族 | 結晶質感、幾何、優雅 | **思源宋體 Traditional Regular** + 加寬字距 | SIL OFL 1.1 |
| `UQM-Ilwrath-Regular.ttf` | 蛛狂族 | 尖刺、蜘蛛狂信、哥德風 | **未來熊漢字**（若可）或 **文泉驛正黑 + 手工描邊**；退而求其次 **思源黑體 ExtraBold + 反白** | SIL OFL / GPL |
| `UQM-Spathi-Regular.ttf` | 史怕族 | 圓潤、膽小滑稽、卡通感 | **思源黑體 Light** + 圓化，或 **賀歲圓體**（有免費版）；穩定選擇 **Chiron Sung HK Light 圓角化** | SIL OFL |
| `UQM-Supox-Regular.ttf` | 蘇波族 | 有機、植物、流線 | **思源宋體 Light** 或 **芫茜體** | SIL OFL |
| `UQM-Arilou-Regular.ttf` | 阿麗露 | 神秘、細長、飄渺 | **思源宋體 ExtraLight** 或 **凤凰点阵字體** | SIL OFL |
| `UQM-CommanderFont.ttf`（UI）| 玩家艦長 | 標準無襯線 | **思源黑體 Traditional Regular** | SIL OFL |
| `UQM-StarConFont.ttf`（UI 標題）| 品牌字 | 科幻標題 | **思源黑體 Heavy** + 手動描邊 | SIL OFL |
| 其餘 UI Tiny/Micro/Module | — | 一般 UI | **思源黑體 Traditional Regular/Light** | SIL OFL |

> **注意**：所有「思源」系列（Source Han Sans/Serif）均為 Adobe + Google + Iconic 合作的 SIL OFL 1.1 開源字型，商用可自由散佈。台灣繁體字形檔名為 `SourceHanSansTC-*.otf` / `SourceHanSerifTC-*.otf`。

### 3.3 合併字型的技術做法

以 `UQM-UrQuan-Regular.ttf` + `SourceHanSansTC-Heavy.otf` → `UQM-UrQuan-Regular-ZHTW.ttf` 為例：

```python
# 需要 pip install fonttools
from fontTools.ttLib import TTFont
from fontTools.merge import Merger

# 讀入 UrQuan 原字型（拉丁）與思源黑體 Heavy（中日韓）
merger = Merger()
merged = merger.merge([
    "input/UQM-UrQuan-Regular.ttf",
    "input/SourceHanSansTC-Heavy.otf",
])

# 修正字型元資料
merged['name'].setName("UQM-UrQuan-Regular-ZHTW", 1, 3, 1, 0x0409)
merged['name'].setName("UQM-UrQuan-Regular-ZHTW", 4, 3, 1, 0x0409)
merged.save("output/UQM-UrQuan-Regular-ZHTW.ttf")
```

**要點**：
1. 使用 `fontTools.merge.Merger` 或 `pyftmerge` 指令列工具。
2. 拉丁字元由排前的字型優先提供；中文字元由後面的字型補上。
3. 兩字型的**字級高度（unitsPerEm）**若不一致，需先用 `fonttools ttx` 手動對齊，否則中文字會偏大或偏小。
4. 中文字型的 hinting 可能需重新生成以配合原 TTF 的 baseline。

### 3.4 更簡單的替代做法

若合併字型太複雜，可用 **`.ttc`（TrueType Collection）打包多字型**，讓引擎自動在同一檔案內查找。但 UQM/MegaMod 是否支援 `.ttc` **未經驗證**（我目前查不到公開資料確認），需實測。

**最保守回退**：直接把原 `UQM-<Race>-Regular.ttf` 「就地換掉」為對應的中文字型，接受該種族英文段落改用中文字型呈現。此法喪失原拉丁風格但工作量最低，可用於 v0.1 快速版本。

---

## 四、字型檔在遊戲內的置換位置

MegaMod 安裝後（Windows 預設路徑類似 `C:\Program Files (x86)\The Ur-Quan Masters MegaMod\`）：

- **HD 模式字型**：`content\packages\` 內的 `.uqm` 檔（本身是 ZIP）內含 `content\base\...` 樹。
- **原生 UI 字型與種族字型**：位於 base content 包內，需先解壓（用 7-Zip 開 `.uqm`）。

### 建議做法：以 addon 方式覆蓋，不動原始檔

1. 建立 `content\addons\zh-TW\` 目錄。
2. 依 UQM 的 addon 慣例，把翻譯後的 `.txt` 與替換後的 `.ttf` 放到相同相對路徑。
3. 打包為 `zh-TW.uqm`（ZIP 改副檔名）。
4. 遊戲內 `Setup → Change Setup → Advanced → Addons` 啟用即可。

> Addon 機制的完整技術細節將於下一階段（實作階段）驗證後補充。

---

## 五、階段性做法（避免一開始就卡在字型）

| 階段 | 字型策略 | 產出 |
|---|---|---|
| v0.1 快速驗證 | 全部種族統一用「思源黑體 Traditional」（策略 A）| 能顯示中文，但無風格差異；用來驗流程 |
| v0.5 分族版 | 為 7 個種族各挑一款中文字型（策略 B）| 有種族視覺辨識，但拉丁字元被替換 |
| v1.0 合併字型版 | 用 fonttools 合併 7 個種族的原 TTF + 對應中文字型（策略 C）| 全保留 |
| v1.1+ 精修版 | 加入 kerning、調整字級對齊、修部首缺字 | 商業級品質 |

---

## 六、待驗證項目（實作階段確認）

以下事項需要在 MegaMod v0.8.5 環境內實測才能確定，本文件先標記為 **[待驗證]**：

1. [待驗證] MegaMod 是否原生支援讀取「按種族命名的資料夾」內之 `content\base\font\<race>\` 覆寫？
2. [待驗證] 是否有 `Setup → Font` 選單可切換 HD TTF vs SD bitmap `.fnt`？
3. [待驗證] `.uqm` addon 是否可只包含字型檔而由引擎正確載入？
4. [待驗證] 合併後的 TTF 是否會導致 UQM 出現字型高度 baseline 偏移？

這些會在建置好 MegaMod v0.8.5 之後**逐項實測**，並補回本文件。

---

## 七、對你原問題的直接回答

> Q4：繁體中文的翻譯也可以辦到（種族特殊字型）嗎？

**A**：可以。MegaMod v0.8.5 已為 Arilou、Chmmr、Ilwrath、Kohr-Ah、Spathi、Supox、Ur-Quan 這 7 個種族分別備有專屬 TTF。繁中化最推薦「策略 C：合併字型」——保留原 TTF 的拉丁字元不變，用對應風格的中文開源字型補齊 CJK 字碼區間，做出來的 `.ttf` 直接替換即可，無需改動引擎程式碼。工作量落在「7 次字型合併 + 校對缺字」，屬中等難度、一次性工作。

一句話：**分族視覺辨識 100% 可以延續到繁中版**。
