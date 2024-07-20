import sys

n, m = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip() for _ in range(n))
check_s = list(sys.stdin.readline().rstrip() for _ in range(m))
s_dict = {}
for c in s:
    s_dict[c] = 1

answer = 0
for check_c in check_s:
    try:
        answer += s_dict[check_c]
    except KeyError:
        pass

print(answer)