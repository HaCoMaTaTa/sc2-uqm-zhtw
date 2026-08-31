"""Complete remaining CAT_*_OPT_*_DESC translations for setupmenu.zh-TW.json.

Covers 154 non-empty untranslated DESCs across 67 CATs.
v0.7 D — 2026-08-14 batch.
"""
import json
from pathlib import Path

JSON_PATH = Path("translations/setupmenu.zh-TW.json")

# CAT_*_OPT_*_DESC translations. Multi-line uses \n. Preserve &! (red macro).
TRANSLATIONS = {
    # CAT_16 Audio Quality
    "CAT_16_OPT_0_DESC": "低音質。\n&!變更後 UQM 將重新啟動。",
    "CAT_16_OPT_1_DESC": "中音質。\n&!變更後 UQM 將重新啟動。",
    "CAT_16_OPT_2_DESC": "高音質。\n&!變更後 UQM 將重新啟動。",
    # CAT_17 Slave Shield
    "CAT_17_OPT_0_DESC": "奴役護盾維持靜態發光,\n模擬 PC 版樣式。\n&!僅影響 UQM 球面樣式",
    "CAT_17_OPT_1_DESC": "奴役護盾脈動閃爍,\n模擬 3DO 版樣式。\n&!僅影響 UQM 球面樣式",
    # CAT_18 1P/2P control (same desc)
    "CAT_18_OPT_0_DESC": "控制超級戰鬥的 1P 玩家,\n以及完整遊戲全程。",
    "CAT_18_OPT_1_DESC": "控制超級戰鬥的 1P 玩家,\n以及完整遊戲全程。",
    # CAT_19 Manual/Auto icons
    "CAT_19_OPT_0_DESC": "手動設定按鈕圖示",
    "CAT_19_OPT_1_DESC": "自動偵測按鈕圖示",
    # CAT_20 Control template
    "CAT_20_OPT_0_DESC": "\n\n選擇要編輯的控制配置範本。",
    "CAT_20_OPT_1_DESC": "\n\n選擇要編輯的控制配置範本。",
    # CAT_21 Precursor Remix
    "CAT_21_OPT_0_DESC": "不載入先驅者重製音樂包。\n\n&!變更後 UQM 將重新啟動。",
    "CAT_21_OPT_1_DESC": "以先驅者製作的現代配樂\n覆蓋 PC 或 3DO 音軌。\n&!變更後 UQM 將重新啟動。",
    # CAT_22 3DO Speech
    "CAT_22_OPT_0_DESC": "不載入 3DO 語音包,\n使用較接近 PC 版的劇本。",
    "CAT_22_OPT_1_DESC": "使用 3DO 語音。差異之處\n劇本較接近 3DO 版。",
    # CAT_23 Aspect Ratio
    "CAT_23_OPT_0_DESC": "允許任意螢幕比例。\n非 4:3 視窗中畫面可能被拉伸。\n&!目前僅 OpenGL 模式下有意義。",
    "CAT_23_OPT_1_DESC": "以 4:3 比例顯示遊戲,\n即使視窗非 4:3。\n&!目前僅 OpenGL 模式下有意義。",
    # CAT_24 Kohr-Stahp
    "CAT_24_OPT_0_DESC": "字面上讓柯亞族停在原地。\n啟用時柯亞影響圈不移動,\n即使時限已到亦然。",
    "CAT_24_OPT_1_DESC": "字面上讓柯亞族停在原地。\n啟用時柯亞影響圈不移動,\n即使時限已到亦然。",
    # CAT_25 God Modes
    "CAT_25_OPT_0_DESC": "不套用無敵模式,您仍可能受傷。",
    "CAT_25_OPT_1_DESC": "戰鬥中玩家控制的星艦\n按下武器或特殊按鈕時能量回滿。\n&!(僅對 AI 對手與劇情有效)",
    "CAT_25_OPT_2_DESC": "無限生命 + 無限能量的結合,\n戰鬥內外全程無敵模式。\n&!(僅對 AI 對手與劇情有效)",
    # CAT_26 Time Dilation
    "CAT_26_OPT_0_DESC": "時間正常流動。",
    "CAT_26_OPT_1_DESC": "時間流速降為六分之一。\n超空間 = 30 秒\n星際間 =  3 分鐘",
    "CAT_26_OPT_2_DESC": "時間流速加快五倍。\n超空間 = 1 秒\n星際間 =  6 秒",
    # CAT_27 Bubble Warp
    "CAT_27_OPT_0_DESC": "瞬間曲速跳躍至星圖任一位置。\n燃料仍會照常消耗。",
    "CAT_27_OPT_1_DESC": "瞬間曲速跳躍至星圖任一位置。\n燃料仍會照常消耗。",
    # CAT_28 Unlock Ships
    "CAT_28_OPT_0_DESC": "解鎖劇情中原本無法取得的所有艦艇。",
    "CAT_28_OPT_1_DESC": "解鎖劇情中原本無法取得的所有艦艇。",
    # CAT_29 Head Start
    "CAT_29_OPT_0_DESC": "開局艦隊即有 Fwiffo、儲藏艙含一單位放射性元素、\n月球基地已探索、\n可較快解鎖星際基地。",
    "CAT_29_OPT_1_DESC": "開局艦隊即有 Fwiffo、儲藏艙含一單位放射性元素、\n月球基地已探索、\n可較快解鎖星際基地。",
    # CAT_30 Auto Detect Icons
    "CAT_30_OPT_0_DESC": "手動選擇按鈕圖示顯示。",
    "CAT_30_OPT_1_DESC": "自動偵測按鈕圖示顯示。\n\n&!此選項將保留於存檔中。",
    # CAT_31 Infinite RU
    "CAT_31_OPT_0_DESC": "劇情模式中給予近乎無限的資源單位。\n\n不會保留於存檔。",
    "CAT_31_OPT_1_DESC": "劇情模式中給予近乎無限的資源單位。\n\n不會保留於存檔。",
    # CAT_32 Skip Intro
    "CAT_32_OPT_0_DESC": "略過廠標、開場畫面與開場動畫。",
    "CAT_32_OPT_1_DESC": "略過廠標、開場畫面與開場動畫。",
    # CAT_33 Fuel Range Indicators
    "CAT_33_OPT_0_DESC": "僅顯示單一基本燃料範圍指示。",
    "CAT_33_OPT_1_DESC": "額外顯示一個燃料圈,\n表示到達目的地時剩餘燃料範圍。\n(以淺灰色虛線圈顯示)",
    "CAT_33_OPT_2_DESC": "額外顯示一個燃料橢圓,\n表示可返回太陽系的臨界點。\n(以淺灰色實心橢圓顯示)",
    "CAT_33_OPT_3_DESC": "同時顯示目的地燃料範圍\n以及回太陽系的臨界點橢圓。",
    # CAT_34 Menu Music
    "CAT_34_OPT_0_DESC": "在主選單、Setup 選單與\n超級戰鬥選單中播放音樂。",
    "CAT_34_OPT_1_DESC": "在主選單、Setup 選單與\n超級戰鬥選單中播放音樂。",
    # CAT_35 Show Nebulae
    "CAT_35_OPT_0_DESC": "啟用時,恆星系背景將顯示\n星雲雲霧。",
    "CAT_35_OPT_1_DESC": "啟用時,恆星系背景將顯示\n星雲雲霧。",
    # CAT_36 Orbiting Planets
    "CAT_36_OPT_0_DESC": "啟用時,行星與衛星將隨時間\n在各自軌道上移動。",
    "CAT_36_OPT_1_DESC": "啟用時,行星與衛星將隨時間\n在各自軌道上移動。",
    # CAT_37 Textured Planets
    "CAT_37_OPT_0_DESC": "啟用時,行星將以完整紋理顯示。",
    "CAT_37_OPT_1_DESC": "於恆星系中顯示美麗的紋理化行星。",
    # CAT_38 Date Format
    "CAT_38_OPT_0_DESC": "日期顯示如下:\n\nFEB 17·2155",
    "CAT_38_OPT_1_DESC": "日期顯示如下:\n\n02·17·2155",
    "CAT_38_OPT_2_DESC": "日期顯示如下:\n\n17 FEB·2155",
    "CAT_38_OPT_3_DESC": "日期顯示如下:\n\n17·02·2155",
    # CAT_39 Infinite Fuel
    "CAT_39_OPT_0_DESC": "劇情模式中給予近乎無限的燃料。",
    "CAT_39_OPT_1_DESC": "劇情模式中給予近乎無限的燃料。",
    # CAT_40 Partial Pickup
    "CAT_40_OPT_0_DESC": "礦物若大於登陸艇剩餘容量,\n將部分拾取。\n生物資料若超過容量則不拾取。",
    "CAT_40_OPT_1_DESC": "礦物若大於登陸艇剩餘容量,\n將部分拾取。\n生物資料若超過容量則不拾取。",
    # CAT_41 In-Game Help Menus
    "CAT_41_OPT_0_DESC": "掃描或於行星移動時顯示礦物價值,\n並於星圖上顯示星圖按鍵/按鈕。",
    "CAT_41_OPT_1_DESC": "掃描或於行星移動時顯示礦物價值,\n並於星圖上顯示星圖按鍵/按鈕。",
    # CAT_42 Resolution
    "CAT_42_OPT_0_DESC": "原版與 HD 圖形的預設解析度。\n原版為 320x240\nHD 為 1280x960",
    "CAT_42_OPT_1_DESC": "縮放至 640x480 解析度。",
    "CAT_42_OPT_2_DESC": "縮放至 960x720 解析度。",
    "CAT_42_OPT_3_DESC": "縮放至 1280x960 解析度。\nHD 的原生解析度。",
    "CAT_42_OPT_4_DESC": "縮放至 1600x1200 解析度。",
    "CAT_42_OPT_5_DESC": "縮放至 1920x1440 解析度。",
    "CAT_42_OPT_6_DESC": "使用自訂解析度。",
    # CAT_43 Infinite Credits
    "CAT_43_OPT_0_DESC": "給予近乎無限的梅諾商星幣。",
    "CAT_43_OPT_1_DESC": "給予近乎無限的梅諾商星幣。",
    # CAT_44 Hazard Colors
    "CAT_44_OPT_0_DESC": "行星掃描檢視時,溫度、氣候與地質\n危險程度以顏色文字顯示嚴重度。",
    "CAT_44_OPT_1_DESC": "行星掃描檢視時,溫度、氣候與地質\n危險程度以顏色文字顯示嚴重度。",
    # CAT_45 Custom Border
    "CAT_45_OPT_0_DESC": "受 Clay 的「SC2 Redo」概念設定啓發的替代 UI",
    "CAT_45_OPT_1_DESC": "受 Clay 的「SC2 Redo」概念設定啓發的替代 UI",
    # CAT_46 Interplanetary Alien Ambience
    "CAT_46_OPT_0_DESC": "位於某外星種族影響圈內的\n恆星系時所播放的音樂",
    "CAT_46_OPT_1_DESC": "位於某外星種族影響圈內的\n恆星系時所播放的音樂,\n但僅於發現該外星種族後生效",
    "CAT_46_OPT_2_DESC": "位於某外星種族影響圈內的\n恆星系時所播放的音樂,\n無論是否曾遇過該種族",
    # CAT_47 Volasaurus Remixes
    "CAT_47_OPT_0_DESC": "Volasaurus 製作的完整重製音樂集。\n覆蓋 PC、3DO 或先驅者音軌。\n&!變更後 UQM 將重新啟動。",
    "CAT_47_OPT_1_DESC": "Volasaurus 製作的完整重製音樂集。\n覆蓋 PC、3DO 或先驅者音軌。\n&!變更後 UQM 將重新啟動。",
    # CAT_48 Show Whole Fuel Value
    "CAT_48_OPT_0_DESC": "以小數形式顯示完整燃料值。",
    "CAT_48_OPT_1_DESC": "以小數形式顯示完整燃料值。",
    # CAT_49 Directional Joystick
    "CAT_49_OPT_0_DESC": "一般控制",
    "CAT_49_OPT_1_DESC": "戰鬥中艦艇面向左類比搖桿方向",
    "CAT_49_OPT_2_DESC": "戰鬥中艦艇面向右類比搖桿方向",
    "CAT_49_OPT_3_DESC": "戰鬥中艦艇面向左類比搖桿方向,\n並於轉向完成後自動推進",
    "CAT_49_OPT_4_DESC": "戰鬥中艦艇面向右類比搖桿方向,\n並於轉向完成後自動推進",
    # CAT_50 Melee Zoom (Android)
    "CAT_50_OPT_0_DESC": "戰鬥中在三段縮放級距間切換。\n\n模擬 PC 版戰鬥 | 僅 Android",
    "CAT_50_OPT_1_DESC": "以最近鄰縮放器連續縮放戰鬥視角。\n\n模擬 3DO 版戰鬥 | 僅 Android",
    "CAT_50_OPT_2_DESC": "以雙線性縮放器連續縮放戰鬥視角。\n\n模擬 3DO 版戰鬥 | 僅 Android",
    "CAT_50_OPT_3_DESC": "以三線性縮放器連續縮放戰鬥視角。\n\n模擬 3DO 版戰鬥 | 僅 Android",
    # CAT_51 Lander Hold Size
    "CAT_51_OPT_0_DESC": "登陸艇最大礦物容量,\n如 PC 版:升級前 64 單位",
    "CAT_51_OPT_1_DESC": "登陸艇最大礦物容量,\n如 3DO 版:升級前 50 單位",
    # CAT_52 Screen Transitions
    "CAT_52_OPT_0_DESC": "畫面轉場為瞬間切換。\n淡入淡出使用加減混合模式。\n&!SDL1 版本淡入淡出永遠為 Alpha 混合",
    "CAT_52_OPT_1_DESC": "畫面轉場為交叉淡入淡出。\n淡入淡出使用 Alpha 混合模式。\n&!SDL1 版本淡入淡出永遠為 Alpha 混合",
    # CAT_55 Nomad Mode
    "CAT_55_OPT_0_DESC": "&!僅供老手!新手勿選!\n強制「無星際基地」模式,\n供追求最極端挑戰的專家玩家。",
    "CAT_55_OPT_1_DESC": "&!僅供老手!新手勿選!\n強制「無星際基地」模式，供追求挑戰的專家玩家，\n附少量便利機制輔助。",
    "CAT_55_OPT_2_DESC": "&!僅供老手!新手勿選!\n基本殘酷「無星際基地」模式,\n供專家玩家,無任何額外便利機制。",
    # CAT_56 Game Over Cutscenes
    "CAT_56_OPT_0_DESC": "各種遊戲結束序列的電影式幻燈片。",
    "CAT_56_OPT_1_DESC": "各種遊戲結束序列的電影式幻燈片。",
    # CAT_57 NPC Ship Orientation
    "CAT_57_OPT_0_DESC": "NPC 艦艇圖示於星際內視圖時\n面向其行進方向。\n您可能遭遇的神秘探測器也會「翻滾」。",
    "CAT_57_OPT_1_DESC": "NPC 艦艇圖示於星際內視圖時\n面向其行進方向。\n您可能遭遇的神秘探測器也會「翻滾」。",
    # CAT_58 Alt Orz Font
    "CAT_58_OPT_0_DESC": "為歐茲對白中的\n*無法翻譯*部分啟用替代字型",
    "CAT_58_OPT_1_DESC": "為歐茲對白中的\n*無法翻譯*部分啟用替代字型",
    # CAT_60 Smart Auto-Pilot
    "CAT_60_OPT_0_DESC": "智慧自動導航會找到目前恆星系\n最快的離開路徑,並於進入超空間時\n已面向設定的座標方向。",
    "CAT_60_OPT_1_DESC": "智慧自動導航會找到目前恆星系\n最快的離開路徑,並於進入超空間時\n已面向設定的座標方向。",
    # CAT_61 Sphere Scan Overlay
    "CAT_61_OPT_0_DESC": "行星依當前掃描的顏色著色,\n如原版 PC 版樣式。",
    "CAT_61_OPT_1_DESC": "行星不依當前掃描的顏色著色,\n如 3DO 版樣式。",
    # CAT_62 Planet Style
    "CAT_62_OPT_0_DESC": "星際內視圖中的行星將呈現\n類似 DOS 版的行星配色與陰影。\n&!(僅在停用行星紋理時適用)",
    "CAT_62_OPT_1_DESC": "星際內視圖中的行星將呈現\n類似 3DO 版的行星配色與陰影。\n&!(僅在停用行星紋理時適用)",
    # CAT_64 Scanning Style
    "CAT_64_OPT_0_DESC": "掃描為靜態顯示,物件以隨機順序彈出,\n類似 PC 版樣式。",
    "CAT_64_OPT_1_DESC": "掃描由上而下掃描地圖,\n依序揭示物件,類似 3DO 版樣式。",
    # CAT_65 Non-Stop Oscilloscope
    "CAT_65_OPT_0_DESC": "示波器顯示當前外星語音或音樂,\n視語音是否啟用而定。",
    "CAT_65_OPT_1_DESC": "外星人停止說話時，示波器切換為顯示音樂。\n(語音啟用時生效)",
    # CAT_66 Oscilloscope Style
    "CAT_66_OPT_0_DESC": "示波器顯示類似 PC 版樣式",
    "CAT_66_OPT_1_DESC": "示波器顯示類似 3DO 版樣式",
    # CAT_68 Lander View Style
    "CAT_68_OPT_0_DESC": "登陸艇視圖顯示於畫面右下,\n登陸艇詳情位於行星地圖左側。\n模擬 PC 版樣式。",
    "CAT_68_OPT_1_DESC": "登陸艇視圖顯示於行星地圖上方,\n登陸艇詳情位於畫面右下。\n模擬 3DO 版樣式。",
    # CAT_69 Planet Map Textures
    "CAT_69_OPT_0_DESC": "掃描畫面的行星紋理、礦物與能量位置\n將呈現 3DO 版樣式。\n&!此選項會被自訂種子取代",
    "CAT_69_OPT_1_DESC": "掃描畫面的行星紋理、礦物與能量位置\n將呈現 UQM 版樣式。\n&!此選項會被自訂種子取代",
    # CAT_71 No HyperSpace Encounters
    "CAT_71_OPT_0_DESC": "超空間中不會遭遇任何外星種族。",
    "CAT_71_OPT_1_DESC": "超空間中不會遭遇任何外星種族。",
    # CAT_73 No Melee Obstacles
    "CAT_73_OPT_0_DESC": "超級戰鬥中無行星或小行星。\n\n&!僅本地對戰。",
    "CAT_73_OPT_1_DESC": "超級戰鬥中無行星或小行星。\n\n&!僅本地對戰。",
    # CAT_74 Show Visited Stars
    "CAT_74_OPT_0_DESC": "已訪恆星於星圖上將變暗,\n以星圖游標懸停時,\n其名稱將以括號顯示。",
    "CAT_74_OPT_1_DESC": "已訪恆星於星圖上將變暗,\n以星圖游標懸停時,\n其名稱將以括號顯示。",
    # CAT_75 Unscaled View HD
    "CAT_75_OPT_0_DESC": "恆星系視圖將以原版 4 倍縮放\n呈現軌道點與恆星。\n模擬原版外觀,但以 HD 呈現。",
    "CAT_75_OPT_1_DESC": "恆星系視圖將以未縮放的軌道點\n與恆星呈現,模擬 Team 6014\n於 2012 年發行的 HD-mod Beta 外觀。",
    # CAT_76 Sphere Style
    "CAT_76_OPT_0_DESC": "掃描球面呈現 DOS 版樣式",
    "CAT_76_OPT_1_DESC": "掃描球面呈現 3DO 版樣式",
    "CAT_76_OPT_2_DESC": "掃描球面呈現 UQM 版樣式",
    # CAT_77 Slaughter Mode
    "CAT_77_OPT_0_DESC": "啟用時,擊落敵艦可影響\n特定外星種族的影響圈範圍。\n&!警告:即使停用,受影響的影響圈仍會保留於存檔",
    "CAT_77_OPT_1_DESC": "啟用時,擊落敵艦可影響\n特定外星種族的影響圈範圍。\n&!警告:即使停用,受影響的影響圈仍會保留於存檔",
    # CAT_78 Advanced Auto-Pilot
    "CAT_78_OPT_0_DESC": "進階自動導航會找出穿越超空間或\n準空間的最省成本路徑,並代為駕駛。",
    "CAT_78_OPT_1_DESC": "進階自動導航會找出穿越超空間或\n準空間的最省成本路徑,並代為駕駛。",
    # CAT_79 Super-Melee Ship Descriptions
    "CAT_79_OPT_0_DESC": "於超級戰鬥主選單中選艦時將於畫面下方\n顯示 Star Control 1 風格的簡短艦艇說明。",
    "CAT_79_OPT_1_DESC": "於超級戰鬥主選單中選艦時將於畫面下方\n顯示 Star Control 1 風格的簡短艦艇說明。",
    # CAT_80 Music Resume
    "CAT_80_OPT_0_DESC": "音樂續播已停用",
    "CAT_80_OPT_1_DESC": "從上次中斷處續播 UQM 音樂,\n無定時器於一段時間後\n將音樂重設回開頭。",
    # CAT_83 Sphere Colors
    "CAT_83_OPT_0_DESC": "外星族群影響圈的預設顏色。(預設)",
    "CAT_83_OPT_1_DESC": "外星族群影響圈的自訂鮮明顏色。",
    # CAT_84 Scatter Elements
    "CAT_84_OPT_0_DESC": "登陸艇爆炸時,將貨艙中\n一定百分比的元素散布至行星地表。",
    "CAT_84_OPT_1_DESC": "登陸艇爆炸時,將貨艙中\n一定百分比的元素散布至行星地表。",
    # CAT_85 Show Lander Upgrades
    "CAT_85_OPT_0_DESC": "探索行星時顯示登陸艇升級圖形。",
    "CAT_85_OPT_1_DESC": "探索行星時顯示登陸艇升級圖形。",
    # CAT_86 Fleet Point System
    "CAT_86_OPT_0_DESC": "根據戰鬥值限制艦隊艦艇數量。\n最高點數 60 (簡單 90、困難 30)\n加上每個盟友種族艦艇值的 2 倍額外點數 (簡單 3 倍、困難 1 倍)。",
    "CAT_86_OPT_1_DESC": "根據戰鬥值限制艦隊艦艇數量。\n最高點數 60 (簡單 90、困難 30)\n加上每個盟友種族艦艇值的 2 倍額外點數 (簡單 3 倍、困難 1 倍)。",
    # CAT_125 Ship Seeding
    "CAT_125_OPT_0_DESC": "外星種族駕駛其正常艦艇。",
    "CAT_125_OPT_1_DESC": "外星族群將依自訂種子\n從三類艦艇中隨機指派。",
    # CAT_126 Ship Storage Queue
    "CAT_126_OPT_0_DESC": "艦艇可寄放於星際基地稍後領回,\n無法加入旗艦時贈送艦艇會直接送往星際基地。",
    "CAT_126_OPT_1_DESC": "艦艇可寄放於星際基地稍後領回,\n無法加入旗艦時贈送艦艇會直接送往星際基地。",
    # CAT_127 Shipyard Captain Names
    "CAT_127_OPT_0_DESC": "啟用時,造船廠內艦艇上方將顯示艦長名稱。",
    "CAT_127_OPT_1_DESC": "啟用時,造船廠內艦艇上方將顯示艦長名稱。",
    # CAT_128 DOS Side Menu
    "CAT_128_OPT_0_DESC": "造船廠採購時 SIS 顯示視窗被側選單視窗取代,\n僅限 DOS 平台(預設)。",
    "CAT_128_OPT_1_DESC": "造船廠採購時 SIS 顯示視窗被 DOS 風格側選單視窗取代,\n所有平台皆生效。",
    # CAT_129 HyperSpace Color
    "CAT_129_OPT_0_DESC": "將超空間中的紅色調變更為指定版本。\nDOS 顏色為較淺的紅色調。\n3DO 顏色為較深的紅色調。",
    "CAT_129_OPT_1_DESC": "將超空間中的紅色調變更為指定版本。\nDOS 顏色為較淺的紅色調。\n3DO 顏色為較深的紅色調。",
}


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    added = 0
    for key, val in TRANSLATIONS.items():
        if key not in data:
            data[key] = val
            added += 1
        else:
            data[key] = val

    data["_D_batch"] = "v0.7 D — 補齊 CAT_16..129 剩餘 DESC (154 個非空條目, 2026-08-14)。"

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"D batch applied: {added} new + updated to {len(TRANSLATIONS)} DESCs.")


if __name__ == "__main__":
    main()
