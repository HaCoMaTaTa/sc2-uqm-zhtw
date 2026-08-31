# android/ — Android APK 移植資料

本資料夾只放**跨機器可攜的元資訊**。Android SDK、JDK、keystore、APK 產物、build log 都不進 repo。

## 內容

| 檔案 | 用途 |
|---|---|
| `README.md` | 本檔（Android 資料夾入口）|
| `00_Porting_Plan.md` | Android 移植 v0.1 決策文件（Stage 0 → 6）|
| `_gen_composite.py` | 主圖示合成（Sa-Matra + 中文標題 + 星空）|
| `_gen_icon_candidates.py` | 5 個候選 icon 生成（A~E）|
| `_gen_pure_icon.py` | 純圖示（無文字）版本 |
| `_gen_thrust_candidates.py` | 觸控 UI thrust 按鈕候選 |
| `_gen_thrust_round2.py` | Thrust 按鈕第二輪 |
| `_install_icons.py` | 佈署到 `res/mipmap-*/`（5 密度全套）|
| `_install_thrust_icon.py` | Thrust 圖示安裝 |
| `_icon_candidates_starmap.py` / `.ps1` | 星圖示範用 icon |
| `_stage0_verify.ps1` | 23 項 stage 0 環境檢查 |
| `plan/` | 4 個 stage runbook (00~03) |
| `research/` | 4 個研究報告（upstream/local/gradle/emulator）|
| `references/` | 參考文件（`Gork_Reponse.md` 等；SDK/JDK zip 已排除）|
| `_icon_candidates/` | 20 個 icon 候選 PNG（<2 MB, 保留視覺參考）|
| `keystore.properties.example` | 簽章設定範本（實檔在 gitignore 外）|

## 不進 repo 的檔案（見 [../.gitignore](../.gitignore)）

- `sdk/` — Android SDK 幾 GB
- `jdk21/` — Adoptium Temurin 21 約 300 MB
- `keystore/` — **簽章密鑰**（機密，遺失就無法升版 apk）
- `release/*.apk` — APK 產物（走 GitHub Releases）
- `screenshots/`, `screen_*.png`, `p*_*.png` — 開發截圖
- `_tmp*/`, `_verify_*/` — 驗證中間物
- `build-*.log`, `_commit_message_*.txt` — 本地日誌
- `references/*.zip` — commandline tools + JDK 壓縮包

## Icon 生成流程（可重跑）

```powershell
$env:PYTHONIOENCODING = 'utf-8'
python _gen_icon_candidates.py  # 產 A~E 5 個候選
python _gen_composite.py        # 合成 E+A（Sa-Matra + 中文標題）
python _install_icons.py        # 佈到 res/mipmap-*/（5 density + adaptive）
```

## 環境設定

詳見 [../docs/AI_Handoff/memories/android-build.md](../docs/AI_Handoff/memories/android-build.md)：

```powershell
$env:ANDROID_HOME  = 'Q:\path\to\Android\sdk'
$env:JAVA_HOME     = 'Q:\path\to\Android\jdk21\jdk-21.0.12.1+1'
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\cmdline-tools\latest\bin;$env:ANDROID_HOME\emulator;C:\msys64\usr\bin;$env:Path"
```

## Build APK

```powershell
# 前置：跑過 ../scripts/setup_upstream.ps1 準備好 ../UQM-MegaMod/
cd Q:\path\to\UQM-MegaMod\build\android
.\gradlew.bat --no-daemon :composeApp:assembleRelease --console=plain
# 產物：build/android/composeApp/build/outputs/apk/release/*.apk
```

亦可用 [../scripts/build_android.ps1](../scripts/build_android.ps1) 自動處理環境變數。
