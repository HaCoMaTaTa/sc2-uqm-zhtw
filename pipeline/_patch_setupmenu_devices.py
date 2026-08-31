"""
Quick fix for setupmenu.zh-TW.json:
- Adds 6 missing device translations (Phase 1 CHOICES completeness).
- Directly patches the multi-line CHOICES entry.

Canonical race names (per _check_zh_purity.py):
  Utwig = 憂特族, Shofixti = 修烈士族, Umgah = 陰嘎族,
  Syreen = 塞蓮族, Slylandro = 斯萊族, Ur-Quan = 烏寬族
"""

import json
from pathlib import Path

JSON_PATH = Path(r"Q:\Dos_G\StarControl2\uqm-work\translations\setupmenu.zh-TW.json")

# English line -> Chinese translation
DEVICE_TRANSLATIONS = {
    "Utwig Bomb": "憂特族炸彈",
    "Shofixti Maidens": "修烈士少女",
    "Umgah Hyperwave Broadcaster": "陰嘎超波發送器",
    "Syreen Shuttle": "塞蓮穿梭機",
    "Slylandro Self-Destruct Code": "斯萊自毀密碼",
    "Ur-Quan Warp Pod": "烏寬曲速艙",
}


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    if "CHOICES" not in data:
        print("[ERROR] CHOICES key not found in JSON")
        return 1

    choices = data["CHOICES"]
    lines = choices.split("\n")
    replaced = []

    new_lines = []
    for line in lines:
        stripped = line.rstrip()
        if stripped in DEVICE_TRANSLATIONS:
            new_lines.append(DEVICE_TRANSLATIONS[stripped])
            replaced.append(stripped)
        else:
            new_lines.append(line)

    data["CHOICES"] = "\n".join(new_lines)

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[OK] Replaced {len(replaced)} device names:")
    for r in replaced:
        print(f"  - {r} -> {DEVICE_TRANSLATIONS[r]}")

    missed = set(DEVICE_TRANSLATIONS.keys()) - set(replaced)
    if missed:
        print(f"[WARN] Not found in CHOICES: {missed}")

    return 0


if __name__ == "__main__":
    exit(main())
