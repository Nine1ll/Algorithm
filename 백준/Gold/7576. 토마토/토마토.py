import sys
from collections import deque

days = 0
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# x,y
n, m = map(int, sys.stdin.readline().split())
tomatoes = []
for _ in range(m):
    tomatoes.append(list(map(int, sys.stdin.readline().rstrip().split())))
visited = [[False] * n for _ in range(m)]


def move_check(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs():
    global days
    queue = deque()

    for i in range(m):
        for j in range(n):
            if tomatoes[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        for _ in range(len(queue)):
            mx, my = queue.popleft()
            for dx, dy in dxy:
                nx, ny = mx + dx, my + dy
                if move_check(nx, ny):
                    if not visited[nx][ny] and tomatoes[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        tomatoes[nx][ny] = tomatoes[mx][ny] + 1
        days += 1

    for row in tomatoes:
        if 0 in row:
            days = -1
            break


bfs()
print(days - 1 if days != -1 else -1)
