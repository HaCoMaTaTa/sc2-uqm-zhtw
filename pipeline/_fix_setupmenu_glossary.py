"""Apply glossary corrections to setupmenu.zh-TW.json.

Fixes translations that don't match StarControl2_TW_Localization glossary.
User-approved translations (from vscode_askQuestions) also applied.
"""
import json
from pathlib import Path

JSON_PATH = Path("translations/setupmenu.zh-TW.json")

# CHOICES corrections (English → canonical Chinese)
# Only entries where my previous translation was WRONG per glossary.
CHOICES_CORRECTIONS = {
    # was 話語寵物 → 會話寵 (Master_Glossary L56)
    "話語寵物": "會話寵",
    # was 水靈螺旋 → 蔚藍螺旋 (Tech_Names v0.5.2)
    "水靈螺旋": "蔚藍螺旋",
    # was 透明軸 → 澄澈紡錘 (Tech_Names shipped v0.3)
    "透明軸": "澄澈紡錘",
    # was 泰洛護盾 → 塔洛防護罩 (Tech_Names Phase 7)
    "泰洛護盾": "塔洛防護罩",
    # was 地獄鑽炮模組 → 火獄穿甲炮模組 (Master_Glossary L334 v0.5.2)
    "地獄鑽炮模組": "火獄穿甲炮模組",
    # was 融合爆能模組 → 融合爆能砲模組 (Technology_Level.md)
    "融合爆能模組": "融合爆能砲模組",
    # was 復克斯獸 → VUX 獸 (Fixed_Terms: VUX preserved in original)
    "復克斯獸": "VUX 獸",
    # was 擴充故事 → 額外故事內容 (user choice)
    "擴充故事": "額外故事內容",
}


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    # 1. Fix CHOICES
    choices = data["CHOICES"].split("\n")
    changes = 0
    for i, line in enumerate(choices):
        if line in CHOICES_CORRECTIONS:
            new = CHOICES_CORRECTIONS[line]
            print(f"  CHOICES[{i}]: {line!r} -> {new!r}")
            choices[i] = new
            changes += 1
    data["CHOICES"] = "\n".join(choices)

    # 2. Add glossary compliance note
    data["_glossary_v1"] = "v0.7 修正: 對齊 StarControl2_TW_Localization 詞彙表 (Talking Pet/Aqua Helix/Clear Spindle/Taalo/Hellbore/Fusion Blaster/VUX Beast/Extended Lore)。"

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nApplied {changes} CHOICES corrections.")


if __name__ == "__main__":
    main()
