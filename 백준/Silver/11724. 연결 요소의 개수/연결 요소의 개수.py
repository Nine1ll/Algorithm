import sys
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

j = 0
if m == 0:
    j = n
else:
    for k in range(1, n+1):
        if not visited[k]:
            j += 1
            bfs(graph, k, visited)

print(j)
