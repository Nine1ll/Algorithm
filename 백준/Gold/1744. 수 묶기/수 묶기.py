import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
negative = []
positive = []
one = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num <= 0:
        heappush(negative, num)
    elif num > 1:
        heappush(positive, -num)
    else:
        one.append(num)

max_sum = 0
while len(negative) > 1:
    max_sum += heappop(negative) * heappop(negative)

while len(positive) > 1:
    max_sum += heappop(positive) * heappop(positive)

if len(negative) > 0:
    max_sum += heappop(negative)

if len(positive) > 0:
    max_sum -= heappop(positive)

max_sum += sum(one)
print(max_sum)

