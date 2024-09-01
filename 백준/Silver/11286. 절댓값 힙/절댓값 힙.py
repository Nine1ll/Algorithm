import sys
from heapq import heappop, heappush

arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heappush(arr, (abs(x), 1 if x > 0 else -1))
    else:
        try:
            element = heappop(arr)
        except IndexError:
            element = (0, False)
        if element[1] == -1:
            print(-1 * element[0])
        else:
            print(element[0])