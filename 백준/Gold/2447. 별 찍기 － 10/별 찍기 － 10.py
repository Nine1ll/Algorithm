import sys

n = int(sys.stdin.readline())


def make_pattern(n):
    if n == 3:
        return ['***', "* *", "***"]

    pattern = make_pattern(n // 3)
    starts = []

    for pattern_line_one in pattern: # 첫 번째 줄
        starts.append(pattern_line_one * 3)
    for pattern_line_two in pattern: # 두 번째 줄
        starts.append(pattern_line_two + " " * (n // 3) + pattern_line_two)
    for pattern_line_three in pattern: # 세 번째 줄
        starts.append(pattern_line_three * 3)

    return starts


print('\n'.join(make_pattern(n)))