# 給 Android session · zh-TW.uqm 同步請求 + gamestrings.txt 誤診澄清

> 產出來源：Windows session (2026-08-25 v1.0 rebuild 之後 · 2026-08-25 22:07 v1.0.1 補譯)
> 用途：貼給另一個負責 Android APK 打包的 chat session · 對齊資產

---

## 🆕 v1.0.1 更新（2026-08-25 22:07）· 請優先取用最新版

**這是最新版 · 覆蓋前面第一節的 v1.0 資料**：

- **路徑**：`Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm`
- **LastWriteTime**：2026/8/25 21:53:55
- **Length**：43,148,939 bytes（41.15 MB）
- **SHA256**：`a6f427d34a53a650151cc9b35472ec13c600506326144187230db2e8ed4aff84`

**相對 v1.0 的新增內容**（commit `8a7350d`）：

- **24 個 Lander 生物名譯**（scope K · BIOLOGICAL_STRING_BASE 段 index 0-25）
  - `Roto-Dendron` → 旋轉樹（Roto-Dendron）
  - `Splort Wort` → 潑濺草（Splort Wort）
  - `Slot Machine Tree` → 吃角子樹（Slot Machine Tree）
  - `Blood Monkey` → 血猴（Blood Monkey）
  - `Zex's Beauty` → 澤克斯的美女（Zex's Beauty）
  - … 共 24 個（`Macrocillia` / `Chicken` 已存 v1.0 內）
- **15 個準空間出口點 waypoints**（STAR_STRING_BASE 段 index 133-147）
  - `To 191.0 : 92.6 (Near Centauri)` → 往 191.0 : 92.6（近半人馬座）
  - `To 11.2 : 940.9 (Near Vega)` → 往 11.2 : 940.9（近織女星）
  - `To 611.7 : 413.1 (Near Metis)` → 往 611.7 : 413.1（近米蒂斯）
  - … 共 15 個 · 全部對齊 STAR_POSTFIX_ZH_BASE canonical 中譯

**字型影響**：Char pool 825550 → 825708 bytes（+11 新 CJK 字元 rasterize：往/近/墨/蒂/等）· 25 個 fonts × 11 chars = 275 新 PNGs。Android APK 打包時字型資產必須用新版 · 否則新字會顯示空白。

**Windows release zip**：`SC2-zhTW-v1.0.1.zip` 352.33 MB · SHA256 `c436e496ab2dc89521eb4bfc3e477ab55dc471ec220f91c8c010c3cca82658da`

---

## 一、Windows 端已產出最新 zh-TW.uqm · 請 Android 端同步使用（v1.0 舊版 · 參考用）

**Source of truth 檔案**（每次 Android APK 打包**必須**使用這個檔 · 但已被 v1.0.1 取代）：

- **路徑**：`Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm`
- **LastWriteTime**：2026/8/25 08:30:55
- **Length**：39,856,467 bytes
- **SHA256**：`b05c8c5f8b36183603e81c1dea760e5ed2e6b814d91c9ff5c0ddfb3fd6148aef`

**此檔內含（v1.0 相對於 rc1 的補譯）**：

- 8/25 commit `e2b36ff` 補 49 個漏譯 keys（scope B/C/D/E/F）：
  - **B 掃描 UI**：`Complete!`, `MINERAL SCAN`, `ENERGY SCAN`, `BIOLOGICAL SCAN`, `MIN.SCAN` / `ENE.SCAN` / `BIO.SCAN` 等 9 個
  - **C 行星類型**：`Gas Giant` → 「氣態巨行星」+ 9 個顏色變體 · `Quasi-Degenerate` / `Super-Dense` 共 12 個
  - **D Sa-Matra 2 個**
  - **E Planet I~XVI 16 個**（羅馬編號保留）
  - **F 遭遇 / 戰鬥 HUD**：`ENCOUNTER IN/AT` = 「遭遇於」、`Deep Space` = 「深空」、`BATTLE GROUP` = 「戰鬥編隊」、`Cdr. Hayes` = 「海斯艦長」、`Remaining Crew:` = 「剩餘船員:」等 10 個

**Android 端請確認**：

1. 目前 APK 內的 zh-TW.uqm SHA256 是否 = 上述 hash
2. 若不 = · 請用 install/ 的檔案取代 · 重建 APK
3. 建議 build script 直接 reference `install/content/addons/zh-TW.uqm` 而不是各自 stage 一份 · 避免雙檔漂移
4. 每次 build 前 verify SHA256 match

---

## 二、你之前提的「gamestrings.txt 索引錯位」問題 · 已澄清為誤診

**你的原始診斷**（節錄）：

> NAMING_STRING_BASE +1, MELEE +1, SAVEGAME +1, OPTION +2, ... NETMELEE +9, LABEL +9

**Windows session 獨立驗證結果**：**索引沒有錯位** · 兩邊完全對齊。

**誤診成因**：你用「非空非 `#` 開頭的行數」count 每個 marker 前的累積數。但 gamestrings.txt 有幾個 records 的 value 佔多行（e.g. `#(NoQuickSave)` base 佔 3 行 · zh-TW 佔 2 行；`#(Hard)` / `#(mouse_err)` 類似）· 導致累計出 -1 / -4 假差異。

**UQM 引擎實際邏輯**（`src/libs/strings/getstr.c:294`）：

```c
if (CurrentLine[0] == '#')
{
    // String header
    slen[++stringI] = 0;    // ← 每個 #(label) 佔 1 index · 不管 value 幾行
}
```

**驗證方式**（給你重跑一次驗證用）：

用「按 `#(label)` 開頭 count」的方法統計每段 record 數 · 兩邊每個 named segment 完全對齊：

| Segment | Base | zh-TW |
|---|---|---|
| STAR_STRING_BASE | 149 | 149 |
| DEVICE_STRING_BASE | 29 | 29 |
| CARGO_STRING_BASE | 14 | 14 |
| ELEMENTS_STRING_BASE | 133 | 133 |
| SCAN_STRING_BASE | 66 | 66 |
| STAR_NUMBER_BASE | 14 | 14 |
| PLANET_NUMBER_BASE | 43 | 43 |
| MONTHS_STRING_BASE | 12 | 12 |
| FEEDBACK_STRING_BASE | 8 | 8 |
| STARBASE_STRING_BASE | 42 | 42 |
| ENCOUNTER_STRING_BASE | 8 | 8 |
| NAVIGATION_STRING_BASE | 9 | 9 |
| NAMING_STRING_BASE | 8 | 8 |
| MELEE_STRING_BASE | 25 | 25 |
| SAVEGAME_STRING_BASE | 10 | 10 |
| OPTION_STRING_BASE | 10 | 10 |
| QUITMENU_STRING_BASE | 5 | 5 |
| STATUS_STRING_BASE | 22 | 22 |
| FLAGSHIP_STRING_BASE | 13 | 13 |
| ORBITSCAN_STRING_BASE | 19 | 19 |
| MAINMENU_STRING_BASE | 74 | 74 |
| NETMELEE_STRING_BASE | 34 | 34 |
| BIOLOGICAL_STRING_BASE | 26 | 26 |
| TDO_MENU_STRING_BASE (= PLAYMENU) | 30 | 30 |
| LABEL_STRING_BASE | 11 | 11 (+ 359 padding 到 STAR_POSTFIX_ZH_BASE=1024) |

**引擎讀到的 index 也完全一致**。你原本的「NAMING+1 到 LABEL+9」偏移表可以整份丟掉。

---

## 三、Empty Slot 顯示英文 · 已定調為「漏譯」不是 index 錯位

- **原因**：zh-TW 的 `#(Empty Slot)` value 就是英文原文 `Empty Slot` · 沒改成中文
- **證據**：zh-TW addon L2254 `#(Empty Slot)` → value `Empty Slot`（跟 base L2232 完全一樣）
- **使用者決策**：**不改** · 空槽英文顯示可接受

---

## 四、Android 側 ENCOUNTER 仍英文 = APK 用了舊 zh-TW.uqm 假設

若你的 Android APK 仍看到 `ENCOUNTER IN` 英文 · 代表 APK 內的 zh-TW.uqm 是 **8/25 e2b36ff commit 之前的版本**（那時還沒補譯 ENCOUNTER）。用第一節提到的最新檔重建即可解決。

---

## 五、Windows 端 v1.0 release zip 資訊（供參考）

- **檔案**：`Q:\Dos_G\StarControl2\uqm-work\release\output\SC2-zhTW-v1.0.zip`
- **SHA256**：`7f877b2c9d1ae5f71c2c81df9b8ccb8cc6f6be7cfe2a967e744e56c317e8afc5`
- **大小**：349.27 MB
- **附加內容**：patch 031 星圖 F6 中文搜尋 + 中文 auto-complete + z→m bug fix
- **UrQuanMasters-zip64.exe**：`Q:\Dos_G\StarControl2\uqm-work\install\UrQuanMasters-zip64.exe` (2026/8/25 09:59:18 · 2,635,264 bytes)

---

## 六、後續建議 · 兩 session 資產共享機制

Windows session 只更新 `install/` + release zip · 不主動去動 Android APK 資產。為避免下次同樣落差 · 建議 Android 端：

1. **Build script 直接 reference `Q:\Dos_G\StarControl2\uqm-work\install\content\addons\zh-TW.uqm`** 作為 asset source · 不 stage 副本
2. **APK build 開頭跑 SHA256 check** · 若與 Windows session 產出 hash 不同 · 記 log 提醒 review
3. **UrQuanMasters-zip64.exe 也是共通資產** · Android 那邊如果編 shared code · 用同一份 `src/uqm/planets/pstarmap.c`（patch 031 已 commit 到 UQM-MegaMod master · commit `206fb7f`）
