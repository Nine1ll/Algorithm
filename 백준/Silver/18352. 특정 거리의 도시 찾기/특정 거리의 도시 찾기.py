import sys
from collections import deque


def bfs(graph, start_city, visited):
    queue = deque([start_city])
    visited[start_city] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1


n, m, k, x = map(int, sys.stdin.readline().split())
road = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    road[start].append(end)

visited = [-1] * (n+1)
bfs(road, x, visited)
if k not in visited:
    print(-1)
else:
    for city, value in enumerate(visited):
        if value == k:
            print(city)

