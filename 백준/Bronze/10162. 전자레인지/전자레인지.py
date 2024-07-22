import sys

t = int(sys.stdin.readline())

buttons = [300, 60, 10]
counts = []
for button in buttons:
    cnt = t // button
    counts.append(cnt)
    t %= button

if t != 0:
    print(-1)
else:
    print(*counts)

