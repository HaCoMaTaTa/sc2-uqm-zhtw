"""Apply C task (A) STAR MAP + 全域 UI 21 條 translations to gamestrings.zh-TW.json.

Also retrofit setupmenu.zh-TW.json 「自動導航」→「自動駕駛」 to align with new AUTO-PILOT canonical.

Rules recap:
  1. AUTO-PILOT → 自動駕駛 (canonical, user-chosen)
  2. Escape Unit → 逃生單元 (short version of 緊急超躍逃生單元)
  3. R.U. → keep R.U. (user-chosen)
  4. AMPLIFIED PRECURSOR BOMB → 增幅先驅者炸彈 (canonical A; Master_Glossary L87 + chmmr 增幅)
  5. ESCAPE POD → 逃生艙
  6. Error 404: Universe Not Found → 錯誤 404：宇宙不存在

Composer names Rush AX / Mark Vera keep as English (proper nouns).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GS = ROOT / "translations" / "gamestrings.zh-TW.json"
SM = ROOT / "translations" / "setupmenu.zh-TW.json"

# 21 條 STAR MAP + 全域 UI
UI_TRANSLATIONS = {
    # NAVIGATION (5)
    "OUT OF FUEL":    "燃料耗盡",
    "AUTO-PILOT":     "自動駕駛",
    "Fuel:":          "燃料:",
    "Fuel Use:":      "燃料消耗:",
    "->":             "->",   # arrow symbol, keep as-is

    # STATUS (1) — Add-> is used in SIS status panel
    "Add->":          ":增加->",  # matches original ":Add->" prefix colon

    # QUITMENU (3)
    "Really Quit":    "確定離開?",
    "Escape Unit":    "逃生單元",
    "Game Paused":    "遊戲暫停",

    # OPTION (2)
    "Very slow":      "極慢",
    "Very fast":      "極快",

    # LABEL (5)
    "NO LIMIT":                     "無限制",
    "EMPTY SLOT":                   "空槽位",
    "R.U.":                         "|1|R.U.",
    "AMPLIFIED PRECURSOR BOMB":     "|-2|增幅先驅者 |-1|炸彈",
    "ESCAPE POD":                   "|1|逃生艙",

    # MAINMENU 系統訊息 (5)
    # NOTE: match source line-count exactly (translate_ui strict mode)
    "must restart": (
        "你所做的變更必須\n"                     # 1
        "重新啟動遊戲才能生效。\n"               # 2
        "\n"                                     # 3 (blank)
        "遊戲即將關閉——\n"                      # 4
        "我方為造成不便致歉!"                    # 5
    ),
    "Addon not found...": (
        "此選項對應之 addon 包\n"               # 1
        "未於 content 資料夾內的\n"              # 2
        "addons 目錄中找到。\n"                  # 3
        "\n"                                     # 4 (blank)
        "此選項將\n"                             # 5
        "回復至預設值。"                         # 6
    ),
    # source is "Page %d of %d" followed by 3 blank lines (total 4 lines); pad accordingly
    "Page of":                      "第 %d 頁 / 共 %d 頁\n\n\n\n",
    "Main Menu Music by":           "主選單音樂由",
    "Error 404: Universe Not Found": "錯誤 404：宇宙不存在",
}


def apply_gs():
    data = json.loads(GS.read_text(encoding="utf-8"))
    new = updated = 0
    for k, v in UI_TRANSLATIONS.items():
        existed = k in data and data[k] and data[k].strip()
        data[k] = v
        if existed:
            updated += 1
        else:
            new += 1

    # marker note
    marker = "v0.7 C(A) — STAR MAP + 全域 UI 21 條 (NAVIGATION/STATUS/QUITMENU/OPTION/LABEL/MAINMENU 系統訊息, 2026-08-14)"
    if "_notes" in data and isinstance(data["_notes"], list) and marker not in data["_notes"]:
        data["_notes"].append(marker)

    GS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"gamestrings.zh-TW.json: {new} new + {updated} updated (total {len(UI_TRANSLATIONS)} keys)")


def retrofit_setupmenu():
    """Replace 自動導航→自動駕駛 in setupmenu.zh-TW.json values (align with AUTO-PILOT canonical).

    Excludes _notes list to keep the marker line intact across re-runs.
    """
    data = json.loads(SM.read_text(encoding="utf-8"))
    changed = 0
    for k, v in list(data.items()):
        if k.startswith("_"):
            continue  # skip notes / comments so marker isn't self-retrofitted
        if isinstance(v, str) and "自動導航" in v:
            data[k] = v.replace("自動導航", "自動駕駛")
            changed += 1
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, str) and "自動導航" in item:
                    v[i] = item.replace("自動導航", "自動駕駛")
                    changed += 1

    marker = "v0.7 C(A) retrofit — 自動導航→自動駕駛 (對齊 gamestrings AUTO-PILOT canonical, 2026-08-14)"
    if "_notes" in data and isinstance(data["_notes"], list) and marker not in data["_notes"]:
        data["_notes"].append(marker)

    SM.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"setupmenu.zh-TW.json: {changed} 自動導航→自動駕駛 retrofit")


if __name__ == "__main__":
    apply_gs()
    retrofit_setupmenu()
