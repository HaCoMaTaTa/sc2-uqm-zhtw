# downloads/ — MegaMod content pack 下載區

`pipeline/download_megamod.ps1` 會把下載的檔案放在這裡。內容不進 git（40~600 MB）。

## 需要下載什麼

最小可跑：

- `mm-0.8.5-installer.exe`（Windows 安裝檔，含 UrQuanMasters.exe + DLL）
- `mm-0.8.5-content.uqm`（基座內容 · gamestrings + 對白 + 字型）

建議：

- `mm-0.8.5-hd-content.uqm`（HD 圖形，MegaMod 主打）
- `mm-0.8.4-3dovoice.uqm`（3DO 全語音包）
- `uqm-0.8.0-3DOMusicRemastered.uqm`（音樂高清版）

完整清單見 [`../download_megamod.ps1`](../download_megamod.ps1) 內的 `$catalog`。

## 下載流程

```powershell
cd pipeline
.\download_megamod.ps1 -Preset Recommended
# 或指定
.\download_megamod.ps1 -Preset Minimum
```

## 下載完的用途

- **安裝到 install/**：
  ```powershell
  .\downloads\mm-0.8.5-installer.exe /D=<絕對路徑>\pipeline\install
  ```
- **解壓 content 到 extracted/**（見 `../extracted/README.md`）

## 手動下載來源

- MegaMod SourceForge：<https://sourceforge.net/projects/megamod/files/>
- MegaMod GitHub Releases：<https://github.com/JHGuitarFreak/UQM-MegaMod/releases>

## Gitignore

本目錄的 `.uqm` `.exe` `.zip` 都在 `.gitignore` 內。若手動放檔案到這，git 會忽略。
