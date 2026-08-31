# Consistency Check 一致性檢查（CI 腳本模板）

> **本檔功能**：**自動化檢查** shipped 譯文 JSON 是否**符合 canonical**。提供 Python 腳本模板，可整合到 CI/CD 流程。
> **對照**：手動 QA 用 [09_AI_Prompt/QA_Check.md](../09_AI_Prompt/QA_Check.md)；本檔用於**自動化**。

---

## 一、腳本目標

檢查每一個 `uqm-work/translations/*.zh-TW.json` 是否：

- ✅ **無 v0.4 舊譯**（撒達許、蘇菲斯特、阿姆嘎…等 8 個）
- ✅ **無 v0.2 更舊譯**（修飛、葉海特、姆嘎…等 8 個）
- ✅ **無簡體字**（龙、华、万…30 個）
- ✅ **無日語漢字**（払、桜、剣…10 個；Shofixti 例外）
- ✅ **感嘆詞保留原文**（Kyaiee!、SNORT! 未被翻譯）
- ✅ **Orz 星號詞語格式正確**（`*詞語*`）
- ✅ **Lua template 完整**（`<% ... %>` 未斷裂）
- ✅ **JSON 語法有效**
- ✅ **鎖定譯名對照**（Fixed_Terms.csv 中的 English → 中譯正確使用）

---

## 二、Python 腳本模板

**建議檔案位置**：`11_QA/consistency_check.py`

**依賴**：Python 3.10+（含標準 json 模組）

```python
#!/usr/bin/env python3
"""
consistency_check.py — SC2 shipped v0.3+ 譯文一致性檢查

用法：
  python consistency_check.py --file uqm-work/translations/orz.zh-TW.json
  python consistency_check.py --all
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

# ============================================================
# 常數：禁譯清單
# ============================================================

# v0.4 使用者重設種族名（shipped v0.3 舊 → v0.4 新）
FORBIDDEN_V03_RACE_NAMES = {
    "撒達許族": "撻伐族",
    "撒達許": "撻伐",
    "蘇菲斯特族": "修烈士族",
    "蘇菲斯特": "修烈士",
    "阿姆嘎族": "陰嘎族",
    "阿姆嘎": "陰嘎",
    "葉哈特族": "翼哈特族",
    "葉哈特": "翼哈特",
    "尼亞里族": "蟾亞族",
    "尼亞里": "蟾亞",
    "蘇波族": "蘇菩族",
    "德魯族": "毒賈族",
    "梅爾諾": "梅諾商",
}

# v0.2 更舊譯名
FORBIDDEN_V02_RACE_NAMES = {
    "修飛族": "修烈士族",
    "葉海特族": "翼哈特族",
    "姆嘎族": "陰嘎族",
    "迪亞里族": "蟾亞族",
    "斯拉達族": "撻伐族",
    "柯耳阿": "柯亞族",
    "蒼捷蘇族": "晶智族",
    "梅爾諾姆": "梅諾商",
    "梅諾族": "梅諾商",
}

# 使用者新指南變體（絕對禁止）
FORBIDDEN_GUIDE_VARIANTS = {
    "奧茲族": "歐茲族",
    "斯帕蒂族": "史怕族",
    "烏爾寬": "烏寬族",
    "烏爾-庫安": "烏寬族",
    "陳傑蘇族": "晶智族",
    "卡姆爾族": "查姆族",
    "凱姆爾族": "查姆族",
}

# 簡體字檢測（常見 30 個）
SIMPLIFIED_CHARS = set("龙华万义从会学图网头无专众东车见说该谁难阴阳长门彻声时过让现们")

# 日語漢字（Shofixti 例外）
JAPANESE_KANJI = set("払桜剣弘応労楽仮舎気")

# 應保留原文的感嘆詞
PRESERVED_INTERJECTIONS = [
    "Kyaiee!", "Hyai!", "HYAIEEE!", "Ha!",
    "Aieee!", "AIEE!",
    "Lykeee-lieee!", "hee-hee-hee", "Ho-ho-ho",
    "SNORT!", "Banzai!",
]

# 常見感嘆詞的中文擬音（可能是被誤翻的線索）
INTERJECTION_MIS_TRANSLATIONS = {
    "凱伊": "Kyaiee!",
    "凱耶": "Kyaiee!",
    "海衣": "Hyai!",
    "海！": "Hyai!",  # 需上下文判斷
    "阿伊": "AIEE!",
    "里啟": "Lykeee-lieee!",
    "嘿嘿嘿": "hee-hee-hee",
    "哼嘶": "SNORT!",
}

# 特定 Shofixti/JSON 例外（允許出現的日語漢字）
SHOFIXTI_ALLOWED_KANJI = set()  # 田中/武士刀/蘿蔔 都用繁體字，無日語專屬

# ============================================================
# 檢查函數
# ============================================================

def load_fixed_terms(csv_path: Path) -> dict[str, str]:
    """從 Fixed_Terms.csv 載入 English → 中譯對照。"""
    mapping = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            eng = row["english"].strip()
            chi = row["chinese"].strip()
            if eng and chi:
                mapping[eng] = chi
    return mapping


def check_forbidden_names(text: str, forbidden: dict[str, str], label: str) -> list[dict]:
    """檢查是否有禁譯名詞。回傳問題清單。"""
    issues = []
    for bad, good in forbidden.items():
        if bad in text:
            issues.append({
                "type": f"forbidden_name_{label}",
                "severity": "high",
                "found": bad,
                "suggested": good,
                "message": f"含有禁譯「{bad}」，應改為「{good}」",
            })
    return issues


def check_simplified_chars(text: str) -> list[dict]:
    """檢查簡體字。"""
    issues = []
    found_chars = set()
    for char in text:
        if char in SIMPLIFIED_CHARS:
            found_chars.add(char)
    if found_chars:
        issues.append({
            "type": "simplified_chars",
            "severity": "high",
            "found": "".join(sorted(found_chars)),
            "message": f"含有簡體字：{''.join(sorted(found_chars))}",
        })
    return issues


def check_japanese_kanji(text: str, allow_shofixti: bool = False) -> list[dict]:
    """檢查日語漢字。Shofixti 檔案允許例外。"""
    issues = []
    allowed = SHOFIXTI_ALLOWED_KANJI if allow_shofixti else set()
    found_chars = set()
    for char in text:
        if char in JAPANESE_KANJI and char not in allowed:
            found_chars.add(char)
    if found_chars:
        issues.append({
            "type": "japanese_kanji",
            "severity": "medium",
            "found": "".join(sorted(found_chars)),
            "message": f"含有日語漢字：{''.join(sorted(found_chars))}（應用繁體字）",
        })
    return issues


def check_lua_template(text: str) -> list[dict]:
    """檢查 Lua template 完整性（成對 <% %>）。"""
    issues = []
    open_count = text.count("<%")
    close_count = text.count("%>")
    if open_count != close_count:
        issues.append({
            "type": "lua_template_broken",
            "severity": "high",
            "message": f"Lua template 不成對：`<%` × {open_count}, `%>` × {close_count}",
        })
    return issues


def check_orz_asterisk(text: str) -> list[dict]:
    """檢查 Orz 星號詞語格式（單獨的 * 不成對）。"""
    issues = []
    asterisks = text.count("*")
    if asterisks % 2 != 0:
        issues.append({
            "type": "orz_asterisk_unpaired",
            "severity": "medium",
            "message": f"Orz 星號 * 不成對（總數 {asterisks}）",
        })
    return issues


def check_json_syntax(json_path: Path) -> tuple[bool, str]:
    """檢查 JSON 語法。"""
    try:
        with open(json_path, encoding="utf-8") as f:
            json.load(f)
        return True, ""
    except json.JSONDecodeError as e:
        return False, str(e)


# ============================================================
# 主檢查邏輯
# ============================================================

def check_file(json_path: Path, fixed_terms: dict[str, str]) -> dict:
    """檢查單一 JSON 檔。"""
    result = {
        "file": str(json_path.name),
        "issues": [],
        "stats": {"tokens": 0, "high_issues": 0, "medium_issues": 0, "low_issues": 0},
    }

    # 1. JSON 語法檢查
    valid, err = check_json_syntax(json_path)
    if not valid:
        result["issues"].append({
            "type": "json_syntax_error",
            "severity": "high",
            "message": f"JSON 語法錯誤：{err}",
        })
        return result

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    is_shofixti = "shofixti" in json_path.name.lower()

    for key, value in data.items():
        # 跳過 _notes（是譯者記錄，不進遊戲）
        if key.startswith("_"):
            continue

        # value 可能是 str 或 list（有些 name_1..4 用 list）
        if isinstance(value, list):
            text = " ".join(str(v) for v in value)
        else:
            text = str(value)

        result["stats"]["tokens"] += 1

        # 收集這個 token 的所有問題
        token_issues = []

        token_issues.extend(check_forbidden_names(text, FORBIDDEN_V03_RACE_NAMES, "v0.3"))
        token_issues.extend(check_forbidden_names(text, FORBIDDEN_V02_RACE_NAMES, "v0.2"))
        token_issues.extend(check_forbidden_names(text, FORBIDDEN_GUIDE_VARIANTS, "guide"))
        token_issues.extend(check_simplified_chars(text))
        token_issues.extend(check_japanese_kanji(text, allow_shofixti=is_shofixti))
        token_issues.extend(check_lua_template(text))
        token_issues.extend(check_orz_asterisk(text))

        # 附加 token 位置
        for issue in token_issues:
            issue["token"] = key
            result["issues"].append(issue)
            severity = issue.get("severity", "low")
            result["stats"][f"{severity}_issues"] += 1

    return result


def format_report(result: dict) -> str:
    """格式化檢查報告。"""
    lines = []
    lines.append(f"# {result['file']} 檢查報告\n")
    stats = result["stats"]
    lines.append(
        f"**總 tokens**：{stats['tokens']} | "
        f"**高優先**：{stats['high_issues']} | "
        f"**中優先**：{stats['medium_issues']} | "
        f"**低優先**：{stats['low_issues']}\n"
    )

    if not result["issues"]:
        lines.append("✅ **無問題**")
        return "\n".join(lines)

    # 分組：高中低
    by_severity = {"high": [], "medium": [], "low": []}
    for issue in result["issues"]:
        by_severity.setdefault(issue.get("severity", "low"), []).append(issue)

    for severity in ("high", "medium", "low"):
        if not by_severity[severity]:
            continue
        title = {"high": "高優先", "medium": "中優先", "low": "低優先"}[severity]
        lines.append(f"\n## {title}\n")
        for issue in by_severity[severity]:
            token = issue.get("token", "-")
            msg = issue.get("message", issue.get("type", ""))
            found = issue.get("found", "")
            lines.append(f"- **[{token}]** {msg}")
            if found:
                lines.append(f"  - 發現：`{found}`")
            if "suggested" in issue:
                lines.append(f"  - 建議：`{issue['suggested']}`")

    return "\n".join(lines)


# ============================================================
# 命令列入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="SC2 譯文一致性檢查")
    parser.add_argument("--file", type=Path, help="檢查單一 JSON 檔")
    parser.add_argument("--all", action="store_true", help="檢查所有 translations/*.zh-TW.json")
    parser.add_argument(
        "--fixed-terms",
        type=Path,
        default=Path("StarControl2_TW_Localization/07_Glossary/Fixed_Terms.csv"),
        help="Fixed_Terms.csv 路徑",
    )
    parser.add_argument(
        "--translations-dir",
        type=Path,
        default=Path("uqm-work/translations"),
        help="translations 目錄",
    )
    args = parser.parse_args()

    fixed_terms = {}
    if args.fixed_terms.exists():
        fixed_terms = load_fixed_terms(args.fixed_terms)

    files_to_check = []
    if args.file:
        files_to_check = [args.file]
    elif args.all:
        files_to_check = list(args.translations_dir.glob("*.zh-TW.json"))
    else:
        parser.error("必須指定 --file 或 --all")

    total_high = 0
    for json_path in files_to_check:
        result = check_file(json_path, fixed_terms)
        print(format_report(result))
        print()  # 分隔線
        total_high += result["stats"]["high_issues"]

    # 若有高優先問題，退出碼 1（可用於 CI gate）
    sys.exit(1 if total_high > 0 else 0)


if __name__ == "__main__":
    main()
```

---

## 三、使用方式

### 3.1 檢查單一檔

```powershell
# 從專案根目錄執行
python StarControl2_TW_Localization/11_QA/consistency_check.py `
    --file uqm-work/translations/orz.zh-TW.json
```

### 3.2 全域掃描

```powershell
python StarControl2_TW_Localization/11_QA/consistency_check.py --all
```

### 3.3 整合到 build pipeline

在 `uqm-work/build_zh-TW.ps1` 或 `package_zh-TW.ps1` 開頭加：

```powershell
python StarControl2_TW_Localization/11_QA/consistency_check.py --all
if ($LASTEXITCODE -ne 0) {
    Write-Error "QA 檢查未通過，退出碼 $LASTEXITCODE"
    exit 1
}
```

高優先問題會**阻止 build**（exit 1）。

---

## 四、擴充建議

**現行腳本檢查的**：
- 禁譯種族名
- 簡體字
- 日語漢字
- Lua template 完整性
- Orz 星號成對
- JSON 語法

**未來可加**：
- 感嘆詞是否被誤翻（`凱伊` → `Kyaiee!`）
- 空格切分正確性（名詞短語不被拆兩半）—— 需要 NLP 或人工判斷
- 星系名是否附上英文原文（正則檢查）
- 玩家 response 情境切換自稱是否正確（依 token 名關鍵字判斷）

---

## 五、腳本演進紀錄

| 版本 | 日期 | 變更 |
|---|---|---|
| v0.1 | 2026-08-07 | Phase 11 初始模板 |

---

## 六、參考來源

- [09_AI_Prompt/QA_Check.md](../09_AI_Prompt/QA_Check.md) 人工 QA 提詞
- [10_Translation_Memory/Forbidden_Translation.md](../10_Translation_Memory/Forbidden_Translation.md) 禁譯清單
- [07_Glossary/Fixed_Terms.csv](../07_Glossary/Fixed_Terms.csv) CI-parsable canonical
- [08_Translation_Rules/Dialogue_Rule.md](../08_Translation_Rules/Dialogue_Rule.md) §十 自查清單
