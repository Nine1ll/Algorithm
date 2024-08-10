import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

josephus = deque([i for i in range(1, n + 1)])
length = len(josephus)
cnt = 0
print_count = 0
while josephus:
    if length == 1:
        print(f"<{josephus.popleft()}>")
        break
    cnt += 1
    p = josephus.popleft()
    if cnt % k == 0:
        print_count += 1
        if print_count == 1:
            print(f"<{p}",end=", ")
        elif print_count == n:
            print(f"{p}>",end="")
        else:
            print(f"{p}", end=", ")
    else:
        josephus.append(p)