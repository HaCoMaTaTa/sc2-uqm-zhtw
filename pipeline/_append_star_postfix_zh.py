"""_append_star_postfix_zh.py — Patch 009 支援腳本

用途:
  translate_ui.py 產出 zh-TW-addon/content/base/gamestrings.txt 之後,
  此腳本追加 149 條新 STAR_POSTFIX_ZH_BASE 段落,對應 engine patch 009 新增的
  gamestrings 索引 STAR_POSTFIX_ZH_BASE (= LABEL_STRING_BASE + LABEL_STRING_COUNT)。

順序 (index 0-148, 對應 STAR_STRING_BASE 同排序):
  0-131: 132 條 constellation / star name 中譯
  132  : UNKNOWN
  133-147: 15 條 waypoint coords (保英文,附加以維持索引)
  148  : Falayalaralfali

輸入:
  --gamestrings-json: translations/gamestrings.zh-TW.json (含 _STAR_POSTFIX_ZH 區段)
  --target-txt: zh-TW-addon/content/base/gamestrings.txt (由 translate_ui.py 產出)

輸出:
  改寫 --target-txt, 在檔案尾端追加 149 個 record blocks:
  #(_STAR_POSTFIX_ZH_000)
  <zh_content>


  #(_STAR_POSTFIX_ZH_001)
  <zh_content>
  ...

每個 record 尾端保留 2 個空行 (匹配 translate_ui.py 輸出格式)。
"""
import argparse
import json
import re
import sys
from pathlib import Path


# STAR_STRING_BASE 索引 0-148 的英文原文順序 (from gamestrings.txt)
STAR_KEYS_EN = [
    "Vega", "Antliae", "Apodis", "Aquarii", "Aquilae", "Arae", "Arietis",
    "Aurigae", "Trianguli", "Caeli", "Camelopardalis", "Cancri", "Brahe",
    "Kepler", "Copernicus", "Capricorni", "Carinae", "Cassiopeiae",
    "Tucanae", "Cephei", "Ceti", "Crateris", "Circini", "Columbae",
    "Chandrasekhar", "Sagittae", "Cygnus", "Corvi", "Chamaeleonis",
    "Equulei", "Delphini", "Doradus", "Monocerotis", "Crucis", "Eridani",
    "Fornacis", "Geminorum", "Altair", "Antares", "Horologii", "Hydrae",
    "Andromedae", "Groombridge", "Lacertae", "Leonis", "Hyades", "Leporis",
    "Librae", "Lipi", "Lyncis", "Fomalhaut", "Menkar", "Microscopii",
    "Draconis", "Orionis", "Normae", "Octantis", "Ophiuchi", "Muscae",
    "Pavonis", "Pegasi", "Persei", "Phoenicis", "Pictoris", "Piscium",
    "Hyginus", "Puppis", "Pyxidis", "Reticuli", "Arianni", "Sagittarii",
    "Scorpii", "Sculptoris", "Scuti", "Serpentis", "Sextantis", "Tauri",
    "Telescopii", "Bootis", "Olber", "Centauri", "Ptolemae", "Gorno",
    "Velorum", "Virginis", "Volantis", "Vulpeculae", "Lalande", "Luyten",
    "Indi", "Lacaille", "Giclas", "Krueger", "Lyrae", "Wolf", "Saurus",
    "Raynet", "Zeeman", "Vela", "Mira", "Cerenkov", "Mersenne", "Maksutov",
    "Klystron", "Metis", "Mensae", "Illuminati", "Vitalis", "Herculis",
    "Gruis", "Squidi", "Almagest", "Alcor", "Algol", "Betelgeuse",
    "Aldebaran", "Achernar", "Procyon", "Rigel", "Bellatrix", "Mizar",
    "Hyperion", "Regulus", "Organon", "Pollux", "Capella", "Deneb",
    "Canopus", "Sirius", "Sol", "Arcturus", "Lentilis",
    "UNKNOWN",
    "To 409.1 : 774.8", "To 318.4 : 490.6", "To 921.1 : 610.4",
    "To 567.3 : 120.7", "To 191.0 : 92.6", "To 860.7 : 15.1",
    "To 5.0 : 164.7", "To 611.7 : 413.1", "To 565.8 : 971.2",
    "To 230.2 : 398.8", "To 11.2 : 940.9", "To 775.2 : 890.6",
    "To 36.8 : 633.2", "To 973.5 : 315.3", "To 585.0 : 621.3",
    "Falayalaralfali",
]

assert len(STAR_KEYS_EN) == 149, f"expected 149 entries, got {len(STAR_KEYS_EN)}"

# zh-TW patch 033: ZHTW_TEMPLATE_BASE slots (chained after STAR_POSTFIX_ZH).
# Each entry: (JSON key, English fallback comment).
ZHTW_TEMPLATE_KEYS = [
    ("_ZHTW_TEMPLATE_PORTAL_WAYPOINT_FMT",
     "Portal waypoint hover format (pstarmap.c)"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gamestrings-json", required=True,
                    help="translations/gamestrings.zh-TW.json")
    ap.add_argument("--target-txt", required=True,
                    help="zh-TW-addon/content/base/gamestrings.txt (output of translate_ui.py)")
    args = ap.parse_args()

    js_path = Path(args.gamestrings_json)
    tgt_path = Path(args.target_txt)

    if not js_path.exists():
        print(f"ERROR: JSON not found: {js_path}", file=sys.stderr)
        sys.exit(1)
    if not tgt_path.exists():
        print(f"ERROR: target TXT not found: {tgt_path}", file=sys.stderr)
        sys.exit(1)

    js = json.loads(js_path.read_text(encoding="utf-8"))
    # Extract translations for each STAR_POSTFIX_ZH key
    # JSON keys: "_STAR_POSTFIX_ZH_000" ... "_STAR_POSTFIX_ZH_148"
    missing = []
    entries = []
    for i, en_name in enumerate(STAR_KEYS_EN):
        key = f"_STAR_POSTFIX_ZH_{i:03d}"
        if key not in js:
            missing.append((i, key, en_name))
            entries.append(en_name)  # fallback to English
        else:
            entries.append(js[key])

    if missing:
        print(f"WARNING: {len(missing)} STAR_POSTFIX_ZH entries missing in JSON, using English fallback:")
        for i, key, en in missing[:10]:
            print(f"  #{i} {key} ({en})")
        if len(missing) > 10:
            print(f"  ... +{len(missing)-10} more")

    # Read current target and count existing entries.
    current = tgt_path.read_text(encoding="utf-8")
    header_re = re.compile(r"^#\(", re.MULTILINE)
    existing_count = len(header_re.findall(current))
    print(f"Current gamestrings.txt entry count: {existing_count}")

    # STAR_POSTFIX_ZH_BASE = 1024 (must match gamestr.h). Pad with empty
    # entries so ZH_000 lands at absolute index 1024 regardless of what
    # extracted content pack version is in use.
    STAR_POSTFIX_ZH_BASE = 1024
    if existing_count > STAR_POSTFIX_ZH_BASE:
        print(f"ERROR: existing entries ({existing_count}) exceeds "
              f"STAR_POSTFIX_ZH_BASE ({STAR_POSTFIX_ZH_BASE}). "
              f"Update the constant in gamestr.h and this script.", file=sys.stderr)
        sys.exit(2)
    pad_count = STAR_POSTFIX_ZH_BASE - existing_count
    print(f"Padding {pad_count} empty entries so ZH_000 lands at index {STAR_POSTFIX_ZH_BASE}")

    # Ensure current ends with exactly one blank line before we start appending
    current = current.rstrip("\r\n") + "\n\n"

    lines = []
    # Emit pad entries (empty content but valid #(ID) header)
    for i in range(pad_count):
        lines.append(f"#(_ZHTW_PAD_{i:03d})   -- pad for STAR_POSTFIX_ZH_BASE alignment")
        lines.append("")   # empty content
        lines.append("")
        lines.append("")

    # Emit 149 real ZH postfix records
    for i, (en, zh) in enumerate(zip(STAR_KEYS_EN, entries)):
        rid = f"_STAR_POSTFIX_ZH_{i:03d}"
        lines.append(f"#({rid})   -- {en}")
        for content_line in zh.split("\n"):
            lines.append(content_line)
        lines.append("")   # separator blank line 1
        lines.append("")   # separator blank line 2

    # zh-TW patch 033: emit ZHTW_TEMPLATE_* slots (chained after ZH postfix)
    tmpl_missing = []
    for tmpl_key, comment in ZHTW_TEMPLATE_KEYS:
        rid = tmpl_key
        val = js.get(tmpl_key)
        if val is None:
            tmpl_missing.append(tmpl_key)
            val = ""            # empty -> pstarmap.c falls back to English literal
        lines.append(f"#({rid})   -- {comment}")
        for content_line in val.split("\n"):
            lines.append(content_line)
        lines.append("")
        lines.append("")

    appended = "\n".join(lines) + "\n"
    tgt_path.write_text(current + appended, encoding="utf-8")
    print(f"OK: appended {pad_count} pad + {len(STAR_KEYS_EN)} STAR_POSTFIX_ZH records "
          f"+ {len(ZHTW_TEMPLATE_KEYS)} ZHTW_TEMPLATE records to {tgt_path}")
    zhtw_base = STAR_POSTFIX_ZH_BASE + len(STAR_KEYS_EN)
    print(f"     Final entry indices: 0..{existing_count-1} (base) + "
          f"{existing_count}..{STAR_POSTFIX_ZH_BASE-1} (pad) + "
          f"{STAR_POSTFIX_ZH_BASE}..{zhtw_base-1} (ZH postfix) + "
          f"{zhtw_base}..{zhtw_base + len(ZHTW_TEMPLATE_KEYS) - 1} (ZHTW template)")
    if missing:
        print(f"     ({len(missing)} STAR_POSTFIX_ZH entries used English fallback — check gamestrings.zh-TW.json)")
    if tmpl_missing:
        print(f"     ({len(tmpl_missing)} ZHTW_TEMPLATE slots empty (engine uses hardcoded English): {', '.join(tmpl_missing)})")


if __name__ == "__main__":
    main()
