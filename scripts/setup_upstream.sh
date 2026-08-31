#!/usr/bin/env bash
# =====================================================================
# setup_upstream.sh — Linux/macOS 版本（對應 setup_upstream.ps1）
#
# Usage:
#   ./scripts/setup_upstream.sh                   # DryRun
#   ./scripts/setup_upstream.sh --execute
#   ./scripts/setup_upstream.sh --execute --force
#   ./scripts/setup_upstream.sh --execute --target-path /path/to/UQM-MegaMod
#   ./scripts/setup_upstream.sh --execute --fork-url 'https://github.com/USER/uqm-megamod-zhTW.git'
#
# 這個腳本 **不** apply patches/*.patch。
# 原因見 patches/UPSTREAM_COMMIT.txt § patches/*.patch 的角色。
# =====================================================================

set -euo pipefail

EXECUTE=0
FORCE=0
TARGET_PATH=""
FORK_URL=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --execute) EXECUTE=1; shift ;;
        --force) FORCE=1; shift ;;
        --target-path) TARGET_PATH="$2"; shift 2 ;;
        --fork-url) FORK_URL="$2"; shift 2 ;;
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
if [[ $EXECUTE -eq 0 ]]; then
    echo "Mode:         DryRun (加 --execute 才實跑)"
else
    echo "Mode:         Execute"
fi
echo ""

command -v git >/dev/null || { echo "找不到 git，請先安裝"; exit 1; }
echo "OK  git found: $(command -v git)"

PINNED_FILE="$REPO_ROOT/patches/UPSTREAM_COMMIT.txt"
[[ -f "$PINNED_FILE" ]] || { echo "找不到 $PINNED_FILE"; exit 1; }
PINNED_SHA="$(grep -oE '^[a-f0-9]{40}$' "$PINNED_FILE" | head -n1)"
[[ -n "$PINNED_SHA" ]] || { echo "無法從 UPSTREAM_COMMIT.txt 解析 SHA"; exit 1; }
echo "OK  Pinned SHA: $PINNED_SHA"

if [[ -z "$FORK_URL" ]]; then
    FORK_URL="$(grep -oE 'https://github\.com/[^ ]+UQM-MegaMod[^ ]*\.git' "$PINNED_FILE" | head -n1)"
fi

if [[ "$FORK_URL" == *CHANGE_ME_TO_YOUR_GITHUB_USER* ]]; then
    echo ""
    echo "警告：Fork URL 是佔位符：$FORK_URL"
    echo ""
    echo "專案作者尚未把 UQM-MegaMod push 到 GitHub。請完成以下之一："
    echo "  1. 依 docs/PUSH_UQM_MEGAMOD_FORK.md 建立 fork · 更新 UPSTREAM_COMMIT.txt"
    echo "  2. 或用 --fork-url 手動指定："
    echo "     ./scripts/setup_upstream.sh --execute --fork-url 'https://github.com/YOUR/uqm-megamod-zhTW.git'"
    if [[ $EXECUTE -eq 1 ]]; then
        exit 1
    fi
fi
echo "OK  Fork URL: $FORK_URL"

if [[ $EXECUTE -eq 0 ]]; then
    echo ""
    echo "DryRun 完畢。加 --execute 執行以下動作："
    if [[ -d "$TARGET_PATH" ]]; then
        echo "  1. git fetch existing → $TARGET_PATH"
        [[ $FORCE -eq 1 ]] && echo "     (--force) git reset --hard + git clean -fdx"
    else
        echo "  1. git clone $FORK_URL → $TARGET_PATH"
    fi
    echo "  2. git checkout $PINNED_SHA"
    echo "  3. （不套 patches——patches 已被 committed 到 fork branch）"
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
    CURRENT_REMOTE="$(git remote get-url origin 2>/dev/null || echo '')"
    if [[ "$CURRENT_REMOTE" != "$FORK_URL" ]]; then
        echo "  Remote origin 目前指向: $CURRENT_REMOTE"
        echo "  改指向 fork: $FORK_URL"
        git remote set-url origin "$FORK_URL"
    fi
    git fetch origin
    popd >/dev/null
else
    echo "→ Clone $FORK_URL → $TARGET_PATH ..."
    mkdir -p "$(dirname "$TARGET_PATH")"
    if ! git clone "$FORK_URL" "$TARGET_PATH"; then
        echo ""
        echo "Clone 失敗。可能原因："
        echo "  1. Fork URL 錯誤或該 repo 尚未建立"
        echo "  2. 網路連不到 GitHub"
        echo "  3. 需要驗證（private repo？）"
        echo ""
        echo "詳見 docs/PUSH_UQM_MEGAMOD_FORK.md § 疑難排解"
        exit 1
    fi
fi

echo "→ Checkout $PINNED_SHA ..."
pushd "$TARGET_PATH" >/dev/null
if ! git checkout "$PINNED_SHA"; then
    echo ""
    echo "Checkout 失敗。SHA $PINNED_SHA 不在 fork 內。"
    echo "解法：見 docs/PUSH_UQM_MEGAMOD_FORK.md § 疑難排解"
    exit 1
fi
popd >/dev/null

echo ""
echo "=== 完成 ==="
echo "MegaMod ready at: $TARGET_PATH"
echo "Commit: $PINNED_SHA"
echo ""
echo "此時 $TARGET_PATH 內含："
echo "  - JHGuitarFreak/UQM-MegaMod 官方源碼"
echo "  - 34 個 CJK/Android 引擎 patch（已 committed 為分支歷史）"
echo "  - Android build scaffold + 觸控 UI + 虛擬 joystick"
echo "  - 品牌化資產（icon / manifest）"
echo ""
echo "下一步："
echo "  cd $REPO_ROOT/pipeline"
echo "  pwsh ./build_zh-TW.ps1 && pwsh ./package_zh-TW.ps1"
