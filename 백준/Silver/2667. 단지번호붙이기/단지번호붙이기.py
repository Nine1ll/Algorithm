import sys
from collections import deque

complex_count = 0
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move_check(x, y):
    return 0 <= x < n and 0 <= y < n


def make_complex(x, y):
    global complex_count
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited_check[x][y] = 1
    while queue:
        mx, my = queue.popleft()
        for dx, dy in dyx:
            nx, ny = mx + dx, my + dy
            if move_check(nx, ny) and not visited_check[nx][ny] and houses[nx][ny] == 1:
                visited_check[nx][ny] = 1
                queue.append((nx, ny))
        cnt += 1
    complex_size.append(cnt)
    complex_count += 1


n = int(sys.stdin.readline())
houses = []
for _ in range(n):
    houses.append(list(map(int, sys.stdin.readline().rstrip())))

visited_check = [[0] * n for _ in range(n)]
complex_size = []
for i in range(n):
    for j in range(n):
        if houses[i][j] == 1 and move_check(i, j) and not visited_check[i][j]:
            make_complex(i, j)

complex_size.sort()
print(complex_count)
for size in complex_size:
    print(size)
