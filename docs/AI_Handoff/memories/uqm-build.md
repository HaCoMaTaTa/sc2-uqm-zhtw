# UQM-MegaMod 從原始碼編譯 (Windows/MSYS2 MINGW32)

## 環境需求
- MSYS2 (`C:\msys64`)
- **MINGW32 subsystem** (32-bit)，不是 UCRT64！
- 套件：`mingw-w64-i686-{toolchain,cmake,ninja,pkgconf,SDL2,SDL2_mixer,SDL2_net,libpng,zlib,libvorbis,libogg}`
- 為何 32-bit：原始 MegaMod exe 就是 32-bit (i386)，配套 DLL 都是 32-bit。
  64-bit build 會在 zip 掛載 `.uqm` 時 access violation crash（`uio_getFileSystemHandler` 後 `handler->mount()`），可能 off_t/size_t bit-width mismatch。
- 套件 SDL2_image 在 i686 沒有 → 但 UQM 不需要（只用 SDL2 + libpng 直接處理）。

## 常見卡點
1. **sparse-checkout 缺 build/**：先 `git sparse-checkout set src build`
2. **內嵌組合語言 32-bit 舊 scaler 編不過**：`cmake -DUQM_PLATFORM_ACCEL=OFF`
3. **64-bit build zip mount crash**：改用 MINGW32 subsystem
4. **make vs mingw32-make**：用 `ninja` 直接
5. **⚠️ src/uqm/gamestr.h 與 content pack 不匹配**：June 6 之後 upstream commit `7c392b5` (Jul 6) 把 `ELEMENTS_STRING_COUNT` 從 133 改成 135，但 `mm-0.8.5-content.uqm` (Jun 6 版本) 的 `gamestrings.txt` 還只有 133 elements。編出來的 exe 讀 `MAINMENU_STRING_BASE + 69` 會偏移 +2 → 主選單缺「New Game/Load Game」+ 顯示 netplay 文字。修法：改回 `#define ELEMENTS_STRING_COUNT 133`（symptom：主選單只有 3 個 item 且看到 Netplay 亂碼）。
6. **content pack 與 src 版本錯配 (general)**：發生此類 offset 問題時，先數 gamestrings.txt 實際 `#(...)` 數量對比每個 `_STRING_COUNT` 常數

## 一鍵 build 指令
```powershell
& "C:\msys64\usr\bin\bash.exe" -lc @"
export MSYSTEM=MINGW32
source /etc/profile
cd /q/Dos_G/StarControl2/UQM-MegaMod
rm -f CMakeCache.txt build.vars && rm -rf CMakeFiles
cmake . -G Ninja -DUQM_PLATFORM_ACCEL=OFF -DCMAKE_BUILD_TYPE=Release && ninja
"@
```

## 產出
- Release: `UrQuanMasters.exe` ~2.6 MB (PE32 i386，與原始 exe 尺寸一致)
- Debug: `UrQuanMastersDebug.exe` ~12 MB

## 首次 configure ~32 秒；首次 build ~2-3 分鐘；增量 rebuild <30 秒

## Deploy 到 install
```powershell
$install = "Q:\Dos_G\StarControl2\uqm-work\install"
# 一次性備份原始 exe
if (-not (Test-Path "$install\UrQuanMasters.exe.original")) {
  Copy-Item "$install\UrQuanMasters.exe" "$install\UrQuanMasters.exe.original"
}
Copy-Item "Q:\Dos_G\StarControl2\UQM-MegaMod\UrQuanMasters.exe" "$install\UrQuanMasters.exe" -Force
# 32-bit DLLs 應保留原本 install\ 內的（原生已存在，不用換）
```

