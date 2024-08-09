import sys
from collections import deque

zone = 0
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
painting = []


def move_check(x, y):
    return 0 <= x < len(painting) and 0 <= y < n


def bfs(x, y, visit):
    global zone
    queue = deque()
    queue.append((x, y))
    color = painting[x][y]
    visit[x][y] = True

    while queue:
        mx, my = queue.popleft()
        for dx, dy in dxy:
            nx, ny = mx + dx, my + dy
            if move_check(nx, ny):
                if not visit[nx][ny] and color == painting[nx][ny]:
                    queue.append((nx, ny))
                    visit[nx][ny] = True
    zone += 1


n = int(sys.stdin.readline())
for _ in range(n):
    painting.append(list(sys.stdin.readline().rstrip()))
visited = [[False] * len(painting[0]) for _ in range(n)]
visited_cb = [[False] * len(painting[0]) for _ in range(n)]

for i in range(n):
    for j in range(len(painting)):
        if not visited[i][j]:
            bfs(i, j, visited)
print(zone, end=" ")
zone = 0

for i in range(n):
    for j in range(len(painting)):
        if painting[i][j] == 'R' or painting[i][j] == 'G':
            painting[i][j] = 'A'

for i in range(n):
    for j in range(len(painting)):
        if not visited_cb[i][j]:
            bfs(i, j, visited_cb)

print(zone)
