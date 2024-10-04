import sys
from heapq import heappop, heappush, heapify

numbers= []
n = int(sys.stdin.readline())
for _ in range(n):
    for ele in list(map(int, sys.stdin.readline().split())):
        heappush(numbers, ele)
        if len(numbers) > n:
            heappop(numbers)

print(heappop(numbers))