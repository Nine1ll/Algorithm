import sys
from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def move_check(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    distance[y][x] = 0
    while queue:
        mx, my = queue.popleft()
        for dx, dy in dxy:
            nx, ny = mx + dx, my + dy
            if move_check(nx, ny):
                if distance[ny][nx] == -1:  # 안갔어
                    if chart[ny][nx] != 0:
                        queue.append((nx, ny))
                        distance[ny][nx] = distance[my][mx] + 1
                    else:
                        distance[ny][nx] = 0


n, m = map(int, sys.stdin.readline().split())  # row = y, col = x
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start_y, start_x = next((i, row.index(2)) for i, row in enumerate(chart) if 2 in row)

distance = [[-1] * m for _ in range(n)]

bfs(start_x, start_y)
for i in range(n):
    for j in range(m):
        if chart[i][j] == 0:
            distance[i][j] = 0

for d in distance:
    print(*d)
