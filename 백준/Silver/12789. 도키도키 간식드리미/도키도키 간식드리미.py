import sys
from collections import deque
n = int(sys.stdin.readline())

line = deque(map(int, sys.stdin.readline().split()))
one_space = []
cross_line_num = 0

while cross_line_num < n:
    if not line:
        break

    if line[0] == cross_line_num + 1:
        line.popleft()
        cross_line_num += 1
    else:
        if not one_space:
            one_space.append(line.popleft())
        else:
            if one_space[-1] == cross_line_num + 1:
                one_space.pop()
                cross_line_num += 1
            else:
                one_space.append(line.popleft())

    # print(f"빈 공간 : {one_space}\n대기줄 : {line}\n{cross_line_num}")

if one_space == sorted(one_space, reverse=True):
    print("Nice")
else:
    print("Sad")