import sys
import heapq

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    number = int(sys.stdin.readline())
    heapq.heappush(cards, number)

answer = 0
while True:
    if len(cards) == 1:
        break
    add = heapq.heappop(cards) + heapq.heappop(cards)
    answer += add
    heapq.heappush(cards, add)

print(answer)