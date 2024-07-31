import sys
from collections import deque

n = int(sys.stdin.readline())
queue_stack = list(map(int,sys.stdin.readline().split()))
elements = list(map(int,sys.stdin.readline().split()))

queue = deque()
for index, value in enumerate(queue_stack):
    if value == 0:
        queue.append(elements[index])

m = int(sys.stdin.readline())
append_ele = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    x0 = append_ele[i]
    queue.appendleft(x0)
    print(queue.pop(), end=" ")