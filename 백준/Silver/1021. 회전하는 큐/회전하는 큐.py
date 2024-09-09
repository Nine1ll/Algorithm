import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
pop_elements = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0
for ele in pop_elements:
    while True:
        if queue[0] == ele:
            queue.popleft()
            break
        else:
            if queue.index(ele) <= len(queue)//2:
                queue.rotate(-1)
                answer += 1
            else:
                queue.rotate(1)
                answer += 1
print(answer)