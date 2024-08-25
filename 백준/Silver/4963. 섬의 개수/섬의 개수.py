import sys
from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1),
       (-1, -1), (-1, 1), (1, -1), (1, 1)]


def move_check(x, y):
    return 0 <= x < w and 0 <= y < h


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    while queue:
        mx, my = queue.popleft()
        for dx, dy in dxy:
            nx, ny = mx + dx, my + dy
            if move_check(nx, ny):
                if not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))


while True:
    island_count = 0
    w, h = map(int, sys.stdin.readline().split())  # x,y
    if w == h == 0:
        break
    land = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(h):  # y
        for j in range(w):  # x
            if not visited[i][j]:
                if land[i][j] == 1:
                    bfs(x=j, y=i)
                    island_count += 1
                else:
                    visited[i][j] = True
    print(island_count)
