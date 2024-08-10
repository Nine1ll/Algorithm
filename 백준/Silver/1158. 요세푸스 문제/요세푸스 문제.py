import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

josephus = deque([i for i in range(1, n + 1)])
cnt = 0

answer = []
while josephus:
    cnt += 1
    p = josephus.popleft()
    if cnt % k == 0:
        answer.append(p)
    else:
        josephus.append(p)

result = ", ".join(map(str,answer))
print("<" +result +">")