import sys
from collections import deque

night_move = [(-2, 1), (-2, -1), (2, 1), (2, -1),
              (-1, 2), (-1, -2), (1, 2), (1, -2)]


def move_check(x, y):
    return 0 <= x < l and 0 <= y < l


def bfs(x, y, tx, ty):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        mx, my = q.popleft()
        for dx, dy in night_move:
            nx, ny = mx + dx, my + dy
            if move_check(nx, ny):
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[mx][my] + 1
                    q.append((nx, ny))

                    if nx == tx and ny == ty:
                        break


t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())  # 체스판의 크기 l * l
    visited = [[0] * l for _ in range(l)]
    now_x, now_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())
    bfs(now_x, now_y, target_x, target_y)
    print(visited[target_x][target_y] - 1)