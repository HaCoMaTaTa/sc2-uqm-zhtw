"""Add CAT_*_OPT_*_DESC translations for visible menu items.

Priority: descriptions shown at bottom of Setup menu screens.
Covers: CAT_53 (Difficulty), CAT_54 (Extended Lore), CAT_59 (Button Icons),
        CAT_63 (Star Background), CAT_67 (HD Animations), CAT_70 (Engine Color),
        CAT_72 (Kohr-Ah DeCleansing), CAT_81 (Platform UI), CAT_82 (Starmap Seeding).
"""
import json
from pathlib import Path

JSON_PATH = Path("translations/setupmenu.zh-TW.json")

NEW_DESCS = {
    # CAT_53 Difficulty
    "CAT_53_OPT_0_DESC": "原版難度，如原作設計。",
    "CAT_53_OPT_1_DESC": "各種調整讓 UQM 更容易上手。",
    "CAT_53_OPT_2_DESC": "&!僅供老手！新手勿選！\n大量調整讓玩法對老手\n更具挑戰性。",
    "CAT_53_OPT_3_DESC": "從主選單開始新遊戲時\n再選擇你想要的難度。",

    # CAT_54 Extended Lore (both OPT_0/1 have identical text in English)
    "CAT_54_OPT_0_DESC": "延伸原作事件的額外故事內容。\n基於 0xDEC0DE 製作的 Extended Mod。\n&!完整新增清單請見 readme。",
    "CAT_54_OPT_1_DESC": "延伸原作事件的額外故事內容。\n基於 0xDEC0DE 製作的 Extended Mod。\n&!完整新增清單請見 readme。",

    # CAT_59 Button Icons
    "CAT_59_OPT_0_DESC": "選單與 UI 中顯示鍵盤按鍵。",
    "CAT_59_OPT_1_DESC": "選單與 UI 中顯示 Xbox 手把按鍵。",
    "CAT_59_OPT_2_DESC": "選單與 UI 中顯示 PlayStation DualSense 按鍵。",
    "CAT_59_OPT_3_DESC": "選單與 UI 中顯示 Switch Pro 手把按鍵。",

    # CAT_63 Star Background
    "CAT_63_OPT_0_DESC": "行星系內的星空背景\n將呈現 DOS 版風格。",
    "CAT_63_OPT_1_DESC": "行星系內的星空背景\n將呈現 3DO 版風格。",
    "CAT_63_OPT_2_DESC": "行星系內的星空背景\n將呈現預設 UQM 風格。",
    "CAT_63_OPT_3_DESC": "行星系內的星空背景\n將呈現預設 HD-mod 風格。",

    # CAT_67 HD Animations
    "CAT_67_OPT_0_DESC": "HD 版超空間星辰、重力井、準空間傳送門\n與恆星系太陽忠實對應原版素材\n但不做動畫。",
    "CAT_67_OPT_1_DESC": "HD 版超空間星辰、重力井、準空間傳送門\n與恆星系太陽將有動畫效果。",

    # CAT_70 Flagship Engine Color
    "CAT_70_OPT_0_DESC": "旗艦引擎顯示為綠色（PC 版樣式）。",
    "CAT_70_OPT_1_DESC": "旗艦引擎顯示為紅色（3DO 版樣式）。",

    # CAT_72 Kohr-Ah DeCleansing (both OPT_0/1 have identical text)
    "CAT_72_OPT_0_DESC": "柯亞死亡進軍從 2155 年起算 100 年後開始。\n死亡進軍已開始後此選項無效。\n請改用「柯亞停手」選項。",
    "CAT_72_OPT_1_DESC": "柯亞死亡進軍從 2155 年起算 100 年後開始。\n死亡進軍已開始後此選項無效。\n請改用「柯亞停手」選項。",

    # CAT_81 Platform UI
    "CAT_81_OPT_0_DESC": "調整 UI 縮放以呈現忠實 DOS 版外觀。\n適用 16:10 螢幕比例。\n&!啟用時將停用多項不相容功能。",
    "CAT_81_OPT_1_DESC": "在視窗周圍加入邊框，以極致忠實\n呈現 3DO 版。適用 4:3 螢幕比例。\n&!啟用時將停用多項不相容功能。",
    "CAT_81_OPT_2_DESC": "預設 UQM 呈現方式。\n適用 4:3 螢幕比例。",

    # CAT_82 Starmap Seeding
    "CAT_82_OPT_0_DESC": "原版遊戲,如榮耀創始者所編寫。（預設）",
    "CAT_82_OPT_1_DESC": "隨機化行星資源與恆星系的生成。",
    "CAT_82_OPT_2_DESC": "隨機化梅諾商所在位置、\n彩虹世界、準空間傳送門,\n以及行星資源與恆星系生成。",
    "CAT_82_OPT_3_DESC": "隨機化所有劇情事件於星圖上的位置,\n包括母星、艦隊位置、對話與遺物,\n以及行星資源與準空間。",
}


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    added = 0
    replaced = 0
    for key, val in NEW_DESCS.items():
        if key in data:
            data[key] = val
            replaced += 1
        else:
            data[key] = val
            added += 1

    data["_desc_v1"] = "v0.7 補齊: CAT_53/54/59/63/67/70/72/81/82 OPT_*_DESC (Setup 選單底部說明)。"

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Added {added} new DESC entries, replaced {replaced} existing.")


if __name__ == "__main__":
    main()
