# install/ — MegaMod 遊戲安裝區

`pipeline/install/` 是 MegaMod 完整遊戲安裝目錄。內容不進 git（~200 MB）。

## 安裝步驟

### 選項 A · 使用官方 installer

```powershell
cd pipeline
.\downloads\mm-0.8.5-installer.exe /D=<絕對路徑>\pipeline\install
# /D=<path> 是 NSIS installer 的 silent install 參數，路徑必須絕對
```

例：
```powershell
.\downloads\mm-0.8.5-installer.exe /D=Q:\Projects\sc2-uqm-zhtw\pipeline\install
```

### 選項 B · 交互安裝

雙擊 `mm-0.8.5-installer.exe`，安裝目標選 `pipeline\install\`。

### 選項 C · 手動解壓（若 installer 不可用）

MegaMod 是 NSIS 安裝包，內部是 zip：
```powershell
# 用 7-Zip 解
& 'C:\Program Files\7-Zip\7z.exe' x downloads\mm-0.8.5-installer.exe -oinstall
```

## 安裝後應有的結構

```
pipeline/install/
├── UrQuanMasters.exe            # 主 exe（我們會用 patched 版蓋過）
├── SDL2.dll / *.dll             # 依賴
├── mm-pc.cfg / mm-3do.cfg       # 設定檔
├── AUTHORS.txt / COPYING.txt    # 授權
└── content/
    ├── version
    ├── gamecontrollerdb.txt
    ├── packages/
    │   ├── mm-0.8.5-content.uqm       # 基座
    │   └── ...
    └── addons/                          # 這裡放我們的 zh-TW.uqm
```

## 替換 exe 為 patched 版

自 build 完 UQM-MegaMod 後：
```powershell
Copy-Item ..\UQM-MegaMod\UrQuanMasters.exe install\UrQuanMasters.exe -Force
# 若你 build 出 -zip64 版
Copy-Item ..\UQM-MegaMod\UrQuanMasters-zip64.exe install\UrQuanMasters-zip64.exe -Force
```

或建捷徑：
```powershell
New-Item -ItemType Junction -Path install -Target Q:\path\to\existing\MegaMod\install
```

## 執行遊戲

```powershell
cd install
.\UrQuanMasters-zip64.exe --windowed --addon zh-TW --logfile game.log
```

## 移除

直接刪整個 `install/` 目錄。存檔在 `%APPDATA%\uqm\`（若你不指定 `--configdir`）。
