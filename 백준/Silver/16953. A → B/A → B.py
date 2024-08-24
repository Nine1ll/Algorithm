import sys
from collections import deque


def bfs(start_number, target_number):
    queue = deque()
    queue.append((start_number, 1))
    while queue:
        num, cnt = queue.popleft()
        mul_two, plus_one = num * 2, int(str(num) + '1')
        if mul_two == target_number or plus_one == target_number:
            return cnt + 1
        else:
            if mul_two < target_number:
                queue.append((mul_two, cnt + 1))

            if plus_one < target_number:
                queue.append((plus_one, cnt + 1))


a, b = map(int, sys.stdin.readline().split())
result = bfs(a,b)
if result is None:
    print(-1)
else:
    print(result)