import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n+1)

for _ in range(n - 1):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                answer[i] = v
                visited[i] = True


bfs(graph, 1, visited)

for node_index in range(2, n+1):
    print(answer[node_index])