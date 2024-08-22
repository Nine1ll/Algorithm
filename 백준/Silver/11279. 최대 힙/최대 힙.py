import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
max_heap = []
for _ in range(n):
    calculate = int(sys.stdin.readline())
    if calculate == 0:
        try:
            print(-heappop(max_heap))
        except IndexError:
            print(0)
    else:
        heappush(max_heap, -calculate)