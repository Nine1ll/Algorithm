import sys
from collections import deque


def function6(q):
    if len(q) == 0:
        return 1
    else:
        return 0


queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == '1':
        queue.appendleft(int(order[1]))
    elif order[0] == '2':
        queue.append(int(order[1]))
    elif order[0] == '3':
        if function6(queue):
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == '4':
        if function6(queue):
            print(-1)
        else:
            print(queue.pop())
    elif order[0] == '5':
        print(len(queue))
    elif order[0] == '6':
        print(function6(queue))
    elif order[0] == '7':
        if function6(queue):
            print(-1)
        else:
            print(queue[0])
    else:
        if function6(queue):
            print(-1)
        else:
            print(queue[-1])
