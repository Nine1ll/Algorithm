import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
least_queue = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x:  # 0이 아니면
        heappush(least_queue, x)
    else:  # 0이면
        if least_queue:
            print(heappop(least_queue))
        else:
            print(0)
