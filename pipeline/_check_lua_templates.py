# -*- coding: utf-8 -*-
"""Audit Lua template first-argument English residuals in translations.

In !StarSeed (default vanilla) mode, these Lua helpers return the FIRST argument
LITERALLY:
  <% comm.getColor("prime_arg", "plot_arg") %>
  <% comm.getConstellation("prime_arg", "plot_arg") %>
  <% comm.getStarName("prime_arg", "plot_arg") %>
  <% comm.getPoint("prime_arg", "plot_arg") %>
  <% comm.swapIfSeeded("A_arg", "B_arg") %>

If prime_arg is English (e.g. "blue star"), it leaks into the CJK dialog in-game.
This scans all translations for prime_args that start with ASCII letters.

Usage: python _check_lua_templates.py [--strict] [--verbose]
"""
import argparse
import json
import re
import sys
from pathlib import Path

# Lua helpers where FIRST arg leaks literal in !StarSeed
LUA_HELPERS = [
    'getColor',
    'getConstellation',
    'getStarName',
    'getPoint',
    'swapIfSeeded',
]

# Per-token exemptions where English first-arg is intentional
# (e.g. mystic shout with in-line Chinese annotation nearby).
# Format: '<race>:<token>:<first_arg>' (exact match).
TEMPLATE_EXEMPT = {
    'pkunk:GENERAL_INFO_SPACE_5:DRACONIS',  # 極樂大喊「DRACONIS(天龍座)！！！！」
}

# Pattern to match: <% comm.<helper>("first_arg", ...) %> — capture first_arg
# Also supports single-quoted args
HELPER_PATTERN = re.compile(
    r'<%\s*comm\.(' + '|'.join(LUA_HELPERS) + r')\s*\(\s*["\']([^"\']*)["\']',
)


def scan_file(path):
    """Return list of (token, helper, first_arg, context)."""
    race = path.stem.replace('.zh-TW', '')
    d = json.loads(path.read_text(encoding='utf-8'))
    hits = []
    for tok, val in d.items():
        if tok.startswith('_') or not isinstance(val, str):
            continue
        for ln in val.split('\n'):
            for m in HELPER_PATTERN.finditer(ln):
                helper, arg = m.group(1), m.group(2)
                # Flag if first arg starts with ASCII letter (English residual)
                if arg and re.match(r'^[A-Za-z]', arg):
                    if f'{race}:{tok}:{arg}' in TEMPLATE_EXEMPT:
                        continue
                    hits.append((tok, helper, arg, ln.strip()[:130]))
    return hits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--race')
    args = parser.parse_args()

    tdir = Path('translations')
    if args.race:
        files = [tdir / f'{args.race}.zh-TW.json']
        if not files[0].exists():
            files = sorted(tdir.rglob(f'{args.race}.zh-TW.json'))
    else:
        # v1.0.9: rglob to catch subdirs (lander/, bio/, …)
        files = sorted(tdir.rglob('*.zh-TW.json'))
        files = [f for f in files if f.stem != 'gamestrings.zh-TW']

    total = 0
    print('=' * 68)
    print('Lua template first-arg (English residual) check')
    print('=' * 68)

    for path in files:
        if not path.exists():
            continue
        hits = scan_file(path)
        race = path.stem.replace('.zh-TW', '')
        status = 'FAIL' if hits else 'PASS'
        print(f'  [{status}] {race:12} suspicious first-args: {len(hits)}')
        total += len(hits)

        if hits and args.verbose:
            for tok, helper, arg, ctx in hits[:30]:
                print(f'    [{tok}] {helper}("{arg}", ...)')
                print(f'      ctx: {ctx}')
            if len(hits) > 30:
                print(f'    ... 還有 {len(hits)-30} 個')

    print('=' * 68)
    print(f'總計: {total} 個可疑 English 首參數')
    print('=' * 68)

    if args.strict and total:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
