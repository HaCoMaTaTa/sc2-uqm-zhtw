"""Trace IT_WAS_ABANDONED page 1 in detail."""
import sys
sys.path.insert(0, r'Q:\Dos_G\StarControl2\uqm-work')
from _simulate_count_lines import get_line_within_width, char_width, CHAR_SPACE, count_lines

text = '...這麼多年 我方一直聽 他們胡言亂語的 廣播 竟從未 起疑。'
MAX_WIDTH = 143

def trace_count(text, max_width):
    ptr = 0
    num_lines = 0
    seen = set()
    while num_lines < 20:
        num_lines += 1
        if ptr in seen:
            print(f'  [{num_lines}] REVISIT ptr={ptr} → INFINITE LOOP')
            return
        seen.add(ptr)
        remaining = text[ptr:]
        if not remaining:
            print(f'  [{num_lines}] empty → done ({num_lines-1} lines)')
            return
        char_count, next_offset, eol = get_line_within_width(remaining, max_width, (1 << 16) - 1)
        line_text = remaining[:char_count]
        print(f'  [{num_lines}] ptr={ptr}, drew {char_count} chars {line_text!r}, next_offset={next_offset}, eol={eol}')
        if eol:
            print(f'  → eol → done ({num_lines} lines)')
            return
        ptr = ptr + next_offset

print(f'Text: {text!r}')
trace_count(text, MAX_WIDTH)
