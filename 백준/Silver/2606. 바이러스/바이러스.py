import sys
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


n = int(sys.stdin.readline())
computer = [0] * (n+1)
network = [[] for _ in range(n + 1)]
connect = int(sys.stdin.readline())
for _ in range(connect):
    c1, c2 = map(int, sys.stdin.readline().split())
    network[c1].append(c2)
    network[c2].append(c1)

bfs(network, 1, computer)
print(sum(computer) - 1)