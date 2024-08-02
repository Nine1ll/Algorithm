import sys

sys.setrecursionlimit(10 ** 5 + 1)


def dfs(graph, v, visited):  # 제귀함수 깊이 문제
    global rank
    visited[v] = rank
    rank += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


edge, vertex, start_edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(edge + 1)]
for _ in range(vertex):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()

visited = [0] * (edge + 1)
rank = 1
dfs(graph, start_edge, visited)

for i in range(1, len(visited)):
    print(visited[i])
