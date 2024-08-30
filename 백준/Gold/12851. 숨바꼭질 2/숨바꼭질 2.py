import sys
from collections import deque

move = [-1, 1, 2]


def move_check(x):
    return 0 <= x <= 100_000


def bfs(x):
    global cnt
    queue = deque([x])
    visited[x] = 0
    while queue:
        mx = queue.popleft()
        if visited[k] <= visited[mx] and visited[k] != -1:
            break

        for dx in move:
            if dx != 2:
                nx = mx + dx
            else:
                nx = 2 * mx
            if move_check(nx):
                if visited[nx] == -1 or visited[nx] == visited[mx] + 1:
                    visited[nx] = visited[mx] + 1
                    queue.append(nx)

                    if nx == k:
                        cnt += 1


cnt = 0
n, k = map(int, sys.stdin.readline().split())
visited = [-1] * (100_000 + 1)

bfs(n)
if cnt == 0:
    cnt = 1
print(visited[k])
print(cnt)
# 걷는다 : x + 1, x -1
# 순간이동한다 : 2 * x
