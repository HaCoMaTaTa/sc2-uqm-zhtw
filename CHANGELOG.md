# Changelog

本專案採 [Keep a Changelog](https://keepachangelog.com/) 格式 · 版本採 [Semantic Versioning](https://semver.org/)。

---

## [v1.0.12 · Android v3.8] — 2026-08-31

### PC v1.0.12
- **updated**：對齊 Android v3.8 addon 內容
- **updated**：完整 v0.7 dossier 修訂應用（Utwig / Yehat / VUX / Kzer-Za / Kohr-Ah / Chmmr / Chenjesu / Dnyarri 共 8 族 P0 shipped rebuild-compare）

### Android v3.8
- **fixed**：星圖 CJK 別名搜尋（patch 031）
- **fixed**：Lander pickup 文字位置（patch 034）
- **updated**：與 PC v1.0.12 addon 同步

---

## [v1.0.10 · Android v3.7] — 2026-08-30
- Utwig v3.2 audit 完成
- Yehat Rebels 完成
- Shofixti 微修

## [v1.0.9 · Android v3.6] — 2026-08-30
- 對齊 PC/Android build

## [v1.0.7 · Android v3.5] — 2026-08-29
- 觸控 UI 微調
- v1.0.7 addon rebuild

## [Android v3.3-v3.4] — 2026-08-28~29
- v3.3：In-app touch visualization overlay for screencasts
- v3.4：翻譯 revision 全量同步

## [Android v3.2] — 2026-08-28
- 教學 rework：新增「新遊戲提醒」頁
- 精簡星圖按鈕
- 從 hamburger 移除 F6/F7

## [Android v3.1] — 2026-08-28
- Onboarding + help 文字重寫
- 移除「auto-popup keyboard」用語
- 新增 🗺 map button 頁

## [Android v3.0] — 2026-08-28
- 修：SdlIme.toggle/show 走 SDL DummyEdit（IME 語言切換全域可用）

## [Android v2.9] — 2026-08-27
- 首次啟動教學
- Always-available help dialog

## [Android v2.8] — 2026-08-27
- Address v2.7 邊界問題

## [Android v2.7] — 2026-08-26
- Comm 對白全域對齊

## [Android v2.6] — 2026-08-25
- Refactor 結構

## [Android v2.5] — 2026-08-25
- Debug info 移除

## [Android v2.4] — 2026-08-25
- Star map contextual UI

## [Android v2.3] — 2026-08-25
- Gamestrings index 對齊確認（v2.3 addon SHA256 b05c8c5f...4aef）
- Encounter in Deep Space fix

## [Android v2.2 → v2.3 debug/release] — 2026-08-25
- 星圖點擊跳位（patch 004 · pstarmap.c + vcontrol.c）
- 星圖 CJK 別名搜尋（patch 031）

## [Android v2.1] — 2026-08-25
- Release keystore 啟用（`uqm-zh-tw.jks`）
- lintVitalRelease 修：移除 FullBackupContent 冗餘 `<exclude>`
- x86_64 lib 排除（`packaging.jniLibs.excludes += "lib/x86_64/**"`）

## [Android v2.0 release] — 2026-08-24
- 首個 release build（有簽章）
- arm64-v8a only
- R8 minifyEnabled
- 30% 大小縮減

## [Android v1.0 → v1.7] — 2026-08-24
- v1.0: 品牌化 · APK 命名 `激戰M星雲II` · icon 5 密度全套（mdpi ~ xxxhdpi）
- v1.1: Icon 精修
- v1.2: KEEP_SCREEN_ON + Back gesture ESC + 星圖點擊跳位
- v1.3: Thrust 圖示 round 2
- v1.4-1.7: UI 微調

## [Stage 5 HD] — 2026-08-24
- HD 資產打包（mm-hd.uqm 232 MB · zh-TW-hd.uqm 82 MB）
- 觸控 overlay v3（M/C 切換 · pinch-to-zoom · F 熱鍵）
- HD 模式 CLI（`--res=1280x960 --resfactor=2 --scale=bilinear`）
- OverlayPrefs SharedPreferences 持久化

## [Stage 4 P2] — 2026-08-23
- 虛擬 SDL joystick（`SDL_JoystickAttachVirtual` + manual mapping）
- `--dirjoystick=3` 自動轉向
- Touch overlay v2：360° analog stick + Weapon/Special/ESC 按鈕

## [Stage 3 crash fix] — 2026-08-23
- patch 018：sdl2_pure.c NULL guard（跨平台 upstream bug）
- Emulator smoke test 主選單顯示成功

## [Stage 3 · patch 011 + 010] — 2026-08-23
- Content 打包（63.7 MB → `assets/uqm-content/`）
- Kotlin App 殼 + Extraction UI

## [Stage 2] — 2026-08-23
- CJK patches 009 個 committed 到 MegaMod HEAD
- clean rebuild PASS

## [Stage 1] — 2026-08-23
- 首次 Android APK build 成功（`composeApp-debug.apk` 18.54 MB）
- patch 012（format-security）+ 013（libvorbis Xiph URL）+ 014（NDK pin）

## [Stage 0] — 2026-08-22
- Android 環境完備（SDK/NDK/JDK 21/AVD）
- `_stage0_verify.ps1` 23 項全綠

---

## PC-Only 歷史（Android 之前）

### [PC v1.0-rc1 → v1.0.10]
- 26 族 Level 3 audit 全數完成
- 34 個引擎 patch 全套用
- 3547 tokens 翻譯 · 99.5% 覆蓋
- 見 [`docs/Localization_Journey.md`](docs/Localization_Journey.md)

### [Baseline] — 2026-08-04
- Repo 初始化
- 從 `_analysis/` + `Star Control II GUS - Manual/` 重構為結構化知識庫

---

## 未來規劃

- **[TBD] Kzer-Za 主線 74 tokens 翻譯** — 需 dossier §9.5 + canonical + 逐 token 翻譯 + layout 對齊
- **[TBD] iOS port** — 若上游有 SDL2-iOS scaffold
- **[TBD] macOS/Linux 驗證** — 目前理論支援但未實測
- **[TBD] Play Store 上架** — 需先解決 CC-NC + 商標問題（不建議）
