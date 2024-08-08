import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
value = 0

jewelry = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

jewelry.sort()
bags.sort()

hq = []
for bag in bags: # 가방 마다
    while jewelry and jewelry[0][0] <= bag: # 보석이 남아있나요? 그리고 보석 무게가 허용 가능한 수치인가요?
        heapq.heappush(hq, -jewelry[0][1]) # 가치가 큰 것을 먼저 빼야하는데, 최소 힙으로 구현하니까 음수로 만들어서 최대 힙으로 만듬
        heapq.heappop(jewelry) # 가능하면 일단 빼

    if hq:# 가방 개수 생각해서 넣을 수 있는 것들 중 최대한 가방에 넣음
        value -= heapq.heappop(hq)

print(value)