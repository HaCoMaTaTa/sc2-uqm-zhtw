# extracted/ — MegaMod 基座內容解壓區

這個目錄故意留空。使用者需要先自己解壓 MegaMod content pack 到這裡，
`pipeline/build_zh-TW.ps1` 才能讀取到 `base/gamestrings.txt`、`base/comm/*/*.txt` 等英文原文。

## 為什麼不進 git

- `mm-0.8.5-content.uqm` 是 MegaMod 官方發布的內容，**不屬於本專案**（GPL/CC 未涵蓋）
- 檔案大（40+ MB），走 GitHub Releases 也非本專案該傳的東西
- 使用者應該自己從 MegaMod 官方下載

## 解壓步驟

### 選項 A · 使用 `pipeline/download_megamod.ps1`（推薦）

```powershell
cd path\to\sc2-uqm-zhtw\pipeline
.\download_megamod.ps1 -Preset Minimum       # 只下最小必需（installer + content）
# 或
.\download_megamod.ps1 -Preset Recommended   # 加上 HD、3DO 語音、3DO 音樂
```

下載完後：

```powershell
# 解 mm-0.8.5-content.uqm 到 extracted/
# .uqm 就是 zip，用任何解壓工具或 PowerShell 內建
$src = 'downloads\mm-0.8.5-content.uqm'
Expand-Archive -Path $src -DestinationPath extracted -Force
```

### 選項 B · 手動下載

1. 去 <https://github.com/JHGuitarFreak/UQM-MegaMod/releases>
2. 找 `mm-0.8.5-installer.exe` + `mm-0.8.5-content.uqm`（或 SourceForge <https://sourceforge.net/projects/megamod/files/>）
3. 執行 installer 安裝到 `pipeline/install/`（見 `install/README.md`）
4. 從 `install/content/packages/mm-0.8.5-content.uqm` 用 zip 工具解到本目錄

## 解壓後應有的結構

```
pipeline/extracted/
└── base/
    ├── base/
    │   ├── gamestrings.txt            # 主要 UI 文字
    │   ├── setupmenu.txt
    │   ├── comm/                       # 對白（26 族）
    │   │   ├── commander/commander.txt
    │   │   ├── arilou/arilou.txt
    │   │   └── ...
    │   ├── ships/                      # 種族 SoI 標籤
    │   │   ├── arilou/skiff.txt
    │   │   └── ...
    │   ├── fonts/                      # 原生字型（供 rasterize 拷 Latin 部分）
    │   │   ├── commander.fon/
    │   │   ├── slab.fon/
    │   │   └── ...
    │   └── cutscene/intro/intro.txt   # intro 字幕
    └── ...
```

## 驗證

```powershell
# 這幾個檔案必須存在
Test-Path extracted\base\base\gamestrings.txt
Test-Path extracted\base\base\comm\commander\commander.txt
Test-Path extracted\base\base\fonts\slab.fon\kerndat.fnt
```

三個都 True → OK，可以跑 `build_zh-TW.ps1`。
