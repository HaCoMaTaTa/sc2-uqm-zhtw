#!/usr/bin/env bash
# =====================================================================
# setup_upstream.sh — Linux/macOS 版本
# 對應 setup_upstream.ps1，功能與參數對稱。
#
# Usage:
#   ./scripts/setup_upstream.sh                  # DryRun
#   ./scripts/setup_upstream.sh --execute        # Apply
#   ./scripts/setup_upstream.sh --execute --force
#   ./scripts/setup_upstream.sh --execute --target-path /path/to/UQM-MegaMod
# =====================================================================

set -euo pipefail

EXECUTE=0
FORCE=0
TARGET_PATH=""
UPSTREAM_URL="https://github.com/JHGuitarFreak/UQM-MegaMod.git"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --execute) EXECUTE=1; shift ;;
        --force) FORCE=1; shift ;;
        --target-path) TARGET_PATH="$2"; shift 2 ;;
        --upstream-url) UPSTREAM_URL="$2"; shift 2 ;;
        -h|--help)
            grep '^#' "$0" | sed 's/^# \{0,1\}//'
            exit 0 ;;
        *) echo "未知參數: $1"; exit 1 ;;
    esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
[[ -z "$TARGET_PATH" ]] && TARGET_PATH="$(dirname "$REPO_ROOT")/UQM-MegaMod"

echo ""
echo "=== UQM-MegaMod upstream setup ==="
echo "Repo root:    $REPO_ROOT"
echo "Target path:  $TARGET_PATH"
echo "Upstream URL: $UPSTREAM_URL"
if [[ $EXECUTE -eq 0 ]]; then
    echo "Mode:         DryRun (加 --execute 才實跑)"
else
    echo "Mode:         Execute"
fi
echo ""

command -v git >/dev/null || { echo "找不到 git，請先安裝"; exit 1; }
echo "✔ git found: $(command -v git)"

PINNED_FILE="$REPO_ROOT/patches/UPSTREAM_COMMIT.txt"
[[ -f "$PINNED_FILE" ]] || { echo "找不到 $PINNED_FILE"; exit 1; }
PINNED_SHA="$(grep -oE '^[a-f0-9]{40}$' "$PINNED_FILE" | head -n1)"
[[ -n "$PINNED_SHA" ]] || { echo "無法從 UPSTREAM_COMMIT.txt 解析 SHA"; exit 1; }
echo "✔ Pinned SHA: $PINNED_SHA"

PATCH_FILES=("$REPO_ROOT"/patches/*.patch)
echo "✔ Found ${#PATCH_FILES[@]} patches"
for p in "${PATCH_FILES[@]}"; do echo "    $(basename "$p")"; done
echo ""

if [[ $EXECUTE -eq 0 ]]; then
    echo "DryRun 完畢。加 --execute 執行以下動作："
    if [[ -d "$TARGET_PATH" ]]; then
        echo "  1. git fetch existing → $TARGET_PATH"
    else
        echo "  1. git clone new → $TARGET_PATH"
    fi
    echo "  2. git checkout $PINNED_SHA"
    [[ $FORCE -eq 1 && -d "$TARGET_PATH" ]] && echo "  (--force) 3. git reset --hard + git clean -fd"
    echo "  4. 逐一套用 ${#PATCH_FILES[@]} 個 patch"
    exit 0
fi

if [[ -d "$TARGET_PATH" ]]; then
    echo "→ 目標已存在，執行 git fetch..."
    pushd "$TARGET_PATH" >/dev/null
    if [[ $FORCE -eq 1 ]]; then
        echo "  --force: git reset --hard + git clean -fdx"
        git reset --hard HEAD
        git clean -fdx
    fi
    git fetch origin
    popd >/dev/null
else
    echo "→ Clone $UPSTREAM_URL → $TARGET_PATH ..."
    mkdir -p "$(dirname "$TARGET_PATH")"
    git clone "$UPSTREAM_URL" "$TARGET_PATH"
fi

echo "→ Checkout $PINNED_SHA ..."
pushd "$TARGET_PATH" >/dev/null
git checkout "$PINNED_SHA"

echo ""
echo "→ 套用 ${#PATCH_FILES[@]} 個 patches..."
APPLIED=0
FAILED=()
for p in "${PATCH_FILES[@]}"; do
    name="$(basename "$p")"
    if git apply --check "$p" 2>/dev/null; then
        git apply "$p"
        echo "  ✔ $name"
        APPLIED=$((APPLIED + 1))
    else
        echo "  ✗ $name — apply --check 失敗"
        FAILED+=("$name")
    fi
done
popd >/dev/null

echo ""
echo "=== 完成 ==="
echo "套用成功: $APPLIED / ${#PATCH_FILES[@]}"
if [[ ${#FAILED[@]} -gt 0 ]]; then
    echo "失敗 patches:"
    for f in "${FAILED[@]}"; do echo "  - $f"; done
    echo ""
    echo "可能原因：patch 已 upstream / SHA 過舊 / 衝突"
fi
echo ""
echo "MegaMod ready at: $TARGET_PATH"
echo ""
echo "下一步："
echo "  cd $REPO_ROOT/pipeline"
echo "  pwsh ./build_zh-TW.ps1 && pwsh ./package_zh-TW.ps1"
