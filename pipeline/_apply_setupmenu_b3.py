"""B3: complete remaining setupmenu.zh-TW.json translations.

Adds:
1. All missing CAT_*_OPTS (65 categories)
2. Fixes CAT_53_OPTS (Difficulty) which was partially English
3. Rewrites CHOICES with all English items translated
"""
import json
from pathlib import Path

JSON_PATH = Path("translations/setupmenu.zh-TW.json")

# Missing CATs (values are `\n`-joined options)
NEW_CATS = {
    # Slave Shields
    "CAT_17_OPTS": "靜態\n脈動",
    # Placeholder — skip CAT_18
    # Icon Auto-Detect
    "CAT_19_OPTS": "手動\n自動偵測",
    # Melee ship display order
    "CAT_20_OPTS": "1P 玩家（下方）\n2P 玩家（上方）",
    # Aspect Ratio
    "CAT_23_OPTS": "任意\n強制 4:3",
    # Time Dilation
    "CAT_26_OPTS": "正常\n慢速\n快速",
    # Fuel Range Indicators
    "CAT_33_OPTS": "無額外指示\n目的地燃料範圍\n回太陽系燃料範圍\n啟用全部範圍指示",
    # Date Format
    "CAT_38_OPTS": "原版 (MMM DD·YYYY)\nMM·DD·YYYY\nDD MMM·YYYY\nDD·MM·YYYY",
    # Resolution
    "CAT_42_OPTS": "預設\n640x480\n960x720\n1280x960\n1600x1200\n1920x1440\n自訂",
    # Directional Joystick
    "CAT_49_OPTS": "一般控制\n左搖桿方向\n右搖桿方向\n左搖桿自動推進\n右搖桿自動推進",
    # Lander Cargo
    "CAT_51_OPTS": "PC 版容量\n3DO 版容量",
    # Screen Transitions (DOS/3DO)
    "CAT_52_OPTS": "DOS\n3DO",
    # Difficulty (fix — was partially English)
    "CAT_53_OPTS": "原版\n簡單\n困難\n開始時選擇",
    # Button Icons
    "CAT_59_OPTS": "鍵盤\nXbox\nPlayStation\nSwitch Pro",
    # Sphere Scan Overlay
    "CAT_61_OPTS": "陰影\n平面",
    # Planet Style
    "CAT_62_OPTS": "PC\n3DO",
    # Star Background
    "CAT_63_OPTS": "PC\n3DO\nUQM\nHD-mod",
    # Scanning Style
    "CAT_64_OPTS": "PC\n3DO",
    # Oscilloscope Style
    "CAT_66_OPTS": "PC\n3DO",
    # HD Animations
    "CAT_67_OPTS": "靜態\n動畫",
    # Lander View Style
    "CAT_68_OPTS": "PC\n3DO",
    # Planet Map Textures
    "CAT_69_OPTS": "3DO\nUQM",
    # Flagship Engine Color
    "CAT_70_OPTS": "綠色引擎\n紅色引擎",
    # Sphere Style
    "CAT_76_OPTS": "PC\n3DO\nUQM",
    # Platform UI
    "CAT_81_OPTS": "DOS\n3DO\nUQM",
    # Starmap Seeding
    "CAT_82_OPTS": "Prime\n行星\nMRQ\n星種",
    # Ship Seeding
    "CAT_83_OPTS": "預設\n自訂",
    # HyperSpace color (DOS/3DO)
    "CAT_129_OPTS": "DOS\n3DO",
}

# CAT_87..CAT_111 = Device toggles (Do Nothing / Remove Device / Add Device)
for n in range(87, 112):
    NEW_CATS[f"CAT_{n}_OPTS"] = "不變更\n移除裝置\n新增裝置"

# CAT_112..CAT_124 = Upgrade toggles (Do Nothing / Remove Upgrade / Add Upgrade)
for n in range(112, 125):
    NEW_CATS[f"CAT_{n}_OPTS"] = "不變更\n移除升級\n新增升級"


# CHOICES: full retranslation (map English → Chinese for the remaining items)
CHOICES_MAP = {
    "Starmap Seeding":              "星圖種子",
    "Sphere Colors":                "領域顏色",
    "Scatter Elements":             "散布元素",
    "Show Lander Upgrades":         "顯示登陸艇升級",
    "Fleet Point System":           "艦隊點數系統",
    "Portal Spawner":               "傳送門生成器",
    "Talking Pet":                  "話語寵物",
    "Sun Device":                   "太陽裝置",
    "Rosy Sphere":                  "玫瑰球體",
    "Aqua Helix":                   "水靈螺旋",
    "Clear Spindle":                "透明軸",
    "Ultron (Broken)":              "厄創（損壞）",
    "Ultron (Semi-Broken)":         "厄創（半損壞）",
    "Ultron (Semi-Fixed)":          "厄創（半修復）",
    "Ultron (Fixed)":               "厄創（修復）",
    "Burvixese Hyperwave 'Caster":  "布維超波發送器",
    "Taalo Protector":              "泰洛護盾",
    "Egg Casing 1":                 "蛋殼 1",
    "Egg Casing 2":                 "蛋殼 2",
    "Egg Casing 3":                 "蛋殼 3",
    "VUX Beast":                    "復克斯獸",
    "Wimbli's Trident":             "溫比三叉戟",
    "Glowing Rod":                  "發光棒",
    "Lunar Base":                   "月球基地",
    "Lander Speed":                 "登陸艇速度",
    "Lander Cargo":                 "登陸艇容量",
    "Lander Rapid Fire":            "登陸艇連射",
    "Lander Bio Shield":            "登陸艇生物護盾",
    "Lander Quake Shield":          "登陸艇地震護盾",
    "Lander Lightning Shield":      "登陸艇閃電護盾",
    "Lander Heat Shield":           "登陸艇熱能護盾",
    "Point Defense Module":         "點防禦模組",
    "Fusion Blaster Module":        "融合爆能模組",
    "Hi-Eff Fuel Module":           "高效燃料模組",
    "Tracking Module":              "追蹤模組",
    "Hellbore Cannon Module":       "地獄鑽炮模組",
    "Shiva Furnace Module":         "濕婆熔爐模組",
    "Ship Seeding":                 "艦艇種子",
    "Ship Storage Queue":           "艦艇儲存佇列",
    "Shipyard Captain Names":       "造船廠艦長名稱",
    "DOS Side Menu":                "DOS 側選單",
}


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    # 1. Add new CATs (won't overwrite existing keys unless CAT_53)
    added = 0
    fixed = 0
    for key, val in NEW_CATS.items():
        if key in data:
            if key == "CAT_53_OPTS":
                data[key] = val
                fixed += 1
        else:
            data[key] = val
            added += 1

    # 2. Retranslate CHOICES
    choices = data["CHOICES"].split("\n")
    replaced = 0
    still_english = []
    for i, line in enumerate(choices):
        if line in CHOICES_MAP:
            choices[i] = CHOICES_MAP[line]
            replaced += 1
        elif line.isascii() and any(c.isalpha() for c in line):
            still_english.append(line)
    data["CHOICES"] = "\n".join(choices)

    # 3. Add note
    data["_B3_CHOICES_CATS"] = "v0.7 B3: 補齊剩餘 CHOICES 英文項 + 65 個未翻譯 CAT_*_OPTS。"

    # Write back preserving key order
    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"B3 done:")
    print(f"  Added {added} new CAT_*_OPTS entries")
    print(f"  Fixed {fixed} existing entries (CAT_53)")
    print(f"  Retranslated {replaced} CHOICES items")
    if still_english:
        print(f"  WARNING: {len(still_english)} CHOICES items still English:")
        for s in still_english:
            print(f"    - {s}")


if __name__ == "__main__":
    main()
