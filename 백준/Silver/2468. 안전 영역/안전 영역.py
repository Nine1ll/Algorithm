import sys
from collections import deque

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move_check(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y, water):
    queue = deque()
    queue.append((x, y))
    if location[x][y] > water:
        is_submerged[x][y] = 1
    while queue:
        mx, my = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx + mx, dy + my
            if move_check(nx, ny):
                if not is_submerged[nx][ny] and location[nx][ny] > water:
                    is_submerged[nx][ny] = 1
                    queue.append((nx,ny))


n = int(sys.stdin.readline())
location = []
max_height = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    max_height = max(max(line), max_height)
    location.append(line)

max_location = 0
for submerged_height in range(max_height):
    cnt = 0
    is_submerged = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not is_submerged[i][j] and location[i][j] > submerged_height:
                bfs(i, j, submerged_height)
                cnt += 1
    max_location = max(max_location,cnt)
print(max_location)