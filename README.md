# uqm-megamod-zhTW · 激戰M星雲II 繁體中文化

> **繁體中文（台灣用語）版** of *Star Control II: The Ur-Quan Masters* (MegaMod 分支)
> **PC** + **Android** 雙平台 · 3547 tokens 翻譯 · 26 族 Level 3 audit · 34 個引擎 patch

---

## English Summary

This is a **Traditional Chinese (Taiwan)** localization of *Star Control II: The Ur-Quan Masters*, based on the [MegaMod](https://github.com/JHGuitarFreak/UQM-MegaMod) fork.

- **PC (Windows)**: patched 32-bit exe with Zip64 addon support + CJK font rasterization + 34 engine patches
- **Android (7.0+)**: full native NDK port with touch overlay, virtual joystick, star-map click-to-jump, IME text input
- **Content**: full dialog translation for 26 races (~3547 tokens) with race-specific voice registers, all UI menus, star-map labels, lander scan reports, intro/outro subtitles

**Licensing** (mirrors upstream): source under **GPL-2.0**, content under **CC BY-NC-SA 2.5**.
Not intended for Play Store distribution (CC-NC clause). Free side-load and personal sharing welcomed.

**Quick start**: See [`docs/SOP_Rebuild_And_Release.md`](docs/SOP_Rebuild_And_Release.md) or scroll to 「快速開始」below.

---

## 一、專案簡介

*Star Control 2* (1992) 是 Toys for Bob (Fred Ford + Paul Reiche III) 的太空歌劇經典。開源引擎 **The Ur-Quan Masters (UQM)** 讓這個宇宙延續下去，**MegaMod** 分支再加上 HD 資產、QoL bug fix、Android build scaffold。

本專案在 MegaMod 之上補完：

- **完整繁中對白** · 26 個種族全 Level 3 audit · 每族有招牌 voice
- **PC Windows 中文化版**（.zip 一鍵解壓即玩，含 patched exe）
- **Android APK**（觸控 UI + 中文 IME + 星圖點擊跳位）
- **34 個引擎 patch**（Zip64 / CJK font / CJK word-wrap / lander scan / Android build / touch overlay ...）

## 二、下載

### 最新版

| 平台 | 檔案 | 大小 | 說明 |
|---|---|---:|---|
| **PC Windows** | `SC2-zhTW-v1.0.12.zip` | ~200 MB | 綠色版 · 解壓即玩 |
| **Android** | `激戰M星雲II-v3.8-release.apk` | ~380 MB | side-load only · 見安裝說明 |
| **Debug APK** | `激戰M星雲II-v3.8-debug.apk` | ~400 MB | 給 QA / 除錯用 |

前往 [**Releases 頁面**](https://github.com/[repo owner]/uqm-megamod-zhTW/releases/latest) 下載。

**驗證檔案完整性**：
- 每個檔案附 `.sha256` sidecar
- APK 也有 [VirusTotal 掃描報告](docs/Security_Scan_Report.md)

### 系統需求

| 平台 | 最低 | 建議 |
|---|---|---|
| PC | Win 7 · OpenGL 2.0 · 400MB 空閒 | Win 10/11 · OpenGL 3.0+ · 1GB |
| Android | 7.0 · 1GB RAM · 900MB 空閒 | 8.0+ · 2GB · Snapdragon 660+ |

## 三、快速開始

### 玩家（只想玩）

- **PC** → 讀 [`docs/PC_Install_Guide.md`](docs/PC_Install_Guide.md)
- **Android** → 讀 [`docs/Android_Install_Guide.md`](docs/Android_Install_Guide.md)

### 開發者（想改譯 / 重建）

```powershell
# 1. Clone
git clone https://github.com/[repo owner]/uqm-megamod-zhTW.git
cd uqm-megamod-zhTW

# 2. 環境檢查
.\scripts\first_time_setup.ps1

# 3. 一鍵準備 upstream + patches
.\scripts\setup_upstream.ps1 -Execute

# 4. 完整 PC build
.\scripts\build_pc.ps1 -Version v1.0.13 -Execute

# 5. 完整 Android build
.\scripts\build_android.ps1 -BuildType Release
```

詳細 SOP → [`docs/SOP_Rebuild_And_Release.md`](docs/SOP_Rebuild_And_Release.md)

## 四、專案結構

```
uqm-megamod-zhTW/
├── README.md                          ← 本檔
├── LICENSE                            ← GPL-2.0（源碼）
├── LICENSE.CONTENT                    ← CC BY-NC-SA 2.5（內容）
├── NOTICE                             ← 第三方致謝
├── AUTHORS.md
├── CHANGELOG.md
│
├── docs/                              ← 使用者/開發者文件
│   ├── SOP_Rebuild_And_Release.md     ← ★ 完整重建 SOP
│   ├── Game_Manual_zh-TW.md           ← 遊戲說明書
│   ├── Localization_Journey.md        ← 中文化過程回憶錄
│   ├── PC_Install_Guide.md            ← PC 版安裝說明
│   ├── Android_Install_Guide.md       ← 手機版安裝說明
│   ├── License_And_Attribution.md     ← 授權合規細節
│   ├── Security_Scan_Report.md        ← APK 安全掃描報告
│   ├── PUSH_FROM_ANOTHER_MACHINE.md   ← 另一台電腦推送指引
│   └── AI_Handoff/                    ← ★ 給後續 AI 接手
│       ├── memories/                  ←   11 個 repo memory
│       ├── session-notes/             ←   3 個舊 session 決策
│       └── prompts/                   ←   10 個 AI 提詞範本
│
├── translation/                       ← ★ 翻譯知識庫（原 StarControl2_TW_Localization）
│   ├── 00_Project_Control/  01_World_Lore/  02_Races/
│   ├── 03_Characters/       04_Ships/       05_Technology/
│   ├── 06_Locations/        07_Glossary/    08_Translation_Rules/
│   ├── 09_AI_Prompt/        10_Translation_Memory/  11_QA/
│   └── Reference_Material/  ← 純 md，PDF/PNG 已排除
│
├── pipeline/                          ← ★ Build/verify pipeline（原 uqm-work/）
│   ├── build_zh-TW.ps1                ← SD 全流程
│   ├── package_zh-TW.ps1              ← 打包 zh-TW.uqm
│   ├── _release_full_zh-TW.ps1        ← 一鍵 PC release
│   ├── _build_hd_fonts.ps1            ← HD 字型
│   ├── _package_hd_addon.ps1          ← 打包 zh-TW-hd.uqm
│   ├── translations/                  ← 166 個 zh-TW.json 譯文
│   └── ... 72 py + 6 ps1
│
├── patches/                           ← ★ 34 個引擎 patch
│   ├── UPSTREAM_COMMIT.txt            ← 鎖定 upstream SHA
│   ├── 001-report-cjk-fixes.patch
│   ├── ... (31 patches)
│   └── README.md
│
├── android/                           ← ★ Android 元資訊
│   ├── 00_Porting_Plan.md
│   ├── _gen_composite.py              ← 圖示生成
│   ├── plan/  research/  references/  ← 移植計畫文件
│   ├── _icon_candidates/              ← 20 個 icon 候選
│   └── keystore.properties.example
│
├── scripts/                           ← ★ 一鍵腳本
│   ├── setup_upstream.ps1  / .sh      ← Clone + patch upstream
│   ├── build_pc.ps1                   ← PC 全流程
│   ├── build_android.ps1              ← Android 全流程
│   ├── verify_and_scan.ps1            ← SHA256 + VirusTotal
│   └── first_time_setup.ps1           ← 環境檢查
│
└── .github/                           ← Issue/PR 樣板 + CI workflow
    ├── workflows/
    └── ISSUE_TEMPLATE/
```

## 五、涵蓋範圍

| 內容 | 完成度 |
|---|---|
| NPC 對白（26 族 / 3473 tokens）| ✅ 100% Level 3 |
| Kzer-Za 主線（74 tokens）| ❌ 待另案 |
| Setup 選單 | ✅ |
| 星圖標籤 + F6 中文別名搜尋 | ✅ patch 009/011/031 |
| Lander 掃描報告（32 個）| ✅ patch 008 修 hang |
| 種族 SoI 標籤 | ✅ patch 010 |
| Intro/Outro 字幕 | ✅ |
| 存讀檔畫面 | ✅（存檔位置說明為英文）|
| 戰鬥模組名 | ✅ |
| 主選單 | ✅ |

## 六、平台狀態

| 平台 | 狀態 | 版本 | 說明 |
|---|---|---|---|
| **Windows (PC)** | ✅ Stable | v1.0.12 | 32-bit exe · patched · Zip64 支援 |
| **Android** | ✅ Stable | v3.8 | arm64-v8a · Modern + Classic touch mode |
| **macOS** | 🚧 Untested | - | UQM 支援但本專案未驗證 |
| **Linux** | 🚧 Untested | - | 同上 |
| **iOS** | ❌ 不支援 | - | Apple 政策 + 上游無 iOS scaffold |

歡迎 macOS/Linux 玩家 fork 補齊。

## 七、授權

- **引擎源碼**（`patches/*.patch`, `pipeline/*.{py,ps1}`, `scripts/*.ps1`）→ **GPL-2.0**（見 [LICENSE](LICENSE)）
- **翻譯內容 / 字型 / 圖示 / 文件**（`translation/`, `pipeline/translations/`, `android/_icon_candidates/`, `docs/`）→ **CC BY-NC-SA 2.5**（見 [LICENSE.CONTENT](LICENSE.CONTENT)）
- **上游 UQM 引擎** → GPL-2.0（[UQM Team](https://sc2.sourceforge.net/)）
- **上游 MegaMod** → GPL-2.0 + CC BY-NC-SA 2.5（[JHGuitarFreak](https://github.com/JHGuitarFreak/UQM-MegaMod)）
- **原著 Star Control II** © 1992 Toys for Bob（Fred Ford, Paul Reiche III）

**簡言之**：免費用、免費改、免費散布 · 保留署名 · 相同授權分享 · 不能商業用。

**Play Store 上架**：不建議（見 [License_And_Attribution.md](docs/License_And_Attribution.md) §三）。

## 八、貢獻

- **翻譯錯誤** → [開 Issue](https://github.com/[repo owner]/uqm-megamod-zhTW/issues/new?template=translation_correction.md)
- **技術 bug** → [開 Issue](https://github.com/[repo owner]/uqm-megamod-zhTW/issues/new?template=bug_report.md) · 附 `game.log` / `uqm_log.txt`
- **Pull Request** → 先讀 [`docs/SOP_Rebuild_And_Release.md`](docs/SOP_Rebuild_And_Release.md) 與 [`docs/AI_Handoff/README.md`](docs/AI_Handoff/README.md)
- **翻譯風格** → 依 [`translation/08_Translation_Rules/`](translation/08_Translation_Rules/) 規範

## 九、致謝

- **Toys for Bob** · Fred Ford, Paul Reiche III · 原著
- **UQM Team** · 開源引擎
- **JHGuitarFreak & MegaMod team** · HD 資產、Android scaffold、Kzer-Za 主線擴充
- **Saibuster** · Android 版主選單音樂
- **Ark Pixel / Fusion Pixel** · 開源 CJK 像素字型
- **sa-matra.net** · 對白庫實證資料
- **本專案作者** · 繁體中文化與 Android 移植
- **AI 協作**（Claude / GPT-4）· 依使用者提詞執行翻譯與程式修改

完整致謝見 [`NOTICE`](NOTICE) 與 [`AUTHORS.md`](AUTHORS.md)。

## 十、聯絡

- Issues → GitHub Issues
- 討論 → GitHub Discussions
- 授權疑問 → 見 [`docs/License_And_Attribution.md`](docs/License_And_Attribution.md)

**願星辰之火，永不熄滅。** ✨
