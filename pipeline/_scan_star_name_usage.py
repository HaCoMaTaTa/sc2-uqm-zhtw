"""_scan_star_name_usage.py
Scan all translations/*.zh-TW.json + translations/lander/*.zh-TW.json for star name mentions.
Cross-reference against patch 009 draft to find inconsistencies.

Output: report of what star name each translation uses.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"Q:\Dos_G\StarControl2\uqm-work\translations")

# The 132 star English names from gamestrings.txt STAR_STRING_BASE 0-131
STAR_NAMES_EN = [
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
]

# Chinese renderings we know may appear (for reverse search — catches translations
# that don't include the English original in parens).
STAR_ZH_PATTERNS = [
    # Draft renderings
    "織女星", "拉朗德", "克魯格", "克呂格", "南河三", "參宿四", "天狼星",
    "大角星", "太陽系", "半人馬座", "杜鵑座", "孔雀座", "烏鴉座", "巨爵座",
    "狐狸座", "天龍座", "英仙座", "六分儀座", "船帆座", "微拉", "布拉赫",
    "葛倫布利吉", "日曼", "齊曼", "塞曼", "契倫科夫", "克里斯壯", "光明會",
    "歐加農", "武仙座", "鹿豹座", "畢宿星團", "心宿二", "天貓座", "巨蛇座",
    "獵戶座", "吉克拉斯", "戈爾諾", "戈爾諾座", "法拉雅拉拉法利", "法拉雅拉爾法立",
    "織女一",  # old canonical, should not appear
    "波江座",  # if used for Procyon = wrong
    # Astronomer variants
    "克卜勒", "開普勒", "哥白尼", "錢德拉塞卡", "希吉努斯", "托勒密",
    "拉卡耶", "呂騰", "路登", "梅森", "馬克蘇托夫", "沃爾夫", "沃夫",
    "奧伯", "奧伯斯",
    # Star name variants
    "牛郎星", "河鼓二", "北落師門", "天囷一", "蒭藁增二", "米拉",
    "開陽增一", "大陵五", "畢宿五", "水委一", "參宿五", "開陽",
    "軒轅十四", "北河三", "五車二", "天津四", "老人星", "參宿七",
    "海珀利翁", "許珀里翁",
    # Game-original variants
    "阿里安尼", "米蒂斯", "墨提斯", "史奎迪", "章魚", "烏賊",
    "阿爾馬蓋斯特", "至大論", "維塔利斯", "蘭提利斯", "索魯斯",
    "雷奈特", "里比", "利披",
]

def scan_file(path: Path):
    """Return dict: {star_en: [list of zh contexts], zh_pattern: [contexts]}"""
    try:
        data = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {}
    hits = {}
    # Scan English star names
    for name in STAR_NAMES_EN:
        # Match "Name" as whole word, case-sensitive to avoid false positives on
        # common English words like "Wolf", "Sol", "Mira", "Metis"
        pattern = r'\b' + re.escape(name) + r'\b'
        for m in re.finditer(pattern, data):
            # Get 40 chars context
            start = max(0, m.start() - 30)
            end = min(len(data), m.end() + 40)
            ctx = data[start:end].replace('\n', ' ').replace('  ', ' ')
            hits.setdefault(name, []).append(ctx)
    # Scan Chinese variants
    for zh in STAR_ZH_PATTERNS:
        for m in re.finditer(re.escape(zh), data):
            start = max(0, m.start() - 20)
            end = min(len(data), m.end() + 30)
            ctx = data[start:end].replace('\n', ' ').replace('  ', ' ')
            hits.setdefault(f"[ZH:{zh}]", []).append(ctx)
    return hits

def main():
    output_lines = []
    all_hits = {}  # {file_path: {name: [contexts]}}

    # Scan both comm/dialog JSONs (in translations/) and lander JSONs
    json_files = list(ROOT.glob("*.zh-TW.json")) + list(ROOT.glob("lander/*.zh-TW.json"))
    print(f"Scanning {len(json_files)} JSON files...")
    for jf in json_files:
        h = scan_file(jf)
        if h:
            all_hits[jf.name] = h

    # Aggregate by star name
    star_usage = {}  # {star_name: [(file, ctx), ...]}
    for fname, hits in all_hits.items():
        for star, ctxs in hits.items():
            for c in ctxs:
                star_usage.setdefault(star, []).append((fname, c.strip()))

    # Write report
    report_lines = ["# Star Name Usage Cross-Reference Report", ""]
    report_lines.append(f"Scanned: {len(json_files)} JSON files (translations/*.zh-TW.json + lander/*.zh-TW.json)")
    report_lines.append(f"Total star name mentions: {sum(len(v) for v in star_usage.values())}")
    report_lines.append("")

    # Section 1: English star names found and their translations context
    report_lines.append("## 1. English star names found in translations")
    report_lines.append("")
    for star in STAR_NAMES_EN:
        if star in star_usage:
            report_lines.append(f"### {star} ({len(star_usage[star])} mentions)")
            for (fname, ctx) in star_usage[star][:15]:  # first 15
                report_lines.append(f"- **{fname}**: `...{ctx}...`")
            if len(star_usage[star]) > 15:
                report_lines.append(f"- ... +{len(star_usage[star])-15} more")
            report_lines.append("")

    # Section 2: Chinese variants found (for consistency check)
    report_lines.append("## 2. Chinese star renderings found")
    report_lines.append("")
    for star_key in sorted(star_usage.keys()):
        if star_key.startswith("[ZH:"):
            zh = star_key[4:-1]
            report_lines.append(f"### `{zh}` ({len(star_usage[star_key])} mentions)")
            for (fname, ctx) in star_usage[star_key][:15]:
                report_lines.append(f"- **{fname}**: `...{ctx}...`")
            if len(star_usage[star_key]) > 15:
                report_lines.append(f"- ... +{len(star_usage[star_key])-15} more")
            report_lines.append("")

    out_path = Path(r"Q:\Dos_G\StarControl2\uqm-work\_patch009_starname_usage_report.md")
    out_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Report written to {out_path}")
    print(f"Total: {len(all_hits)} files with mentions")

if __name__ == "__main__":
    main()
