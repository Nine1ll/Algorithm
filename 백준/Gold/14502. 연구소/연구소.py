import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
maxv = 0
safe_areas = []
virus_areas = []
directions = [(0,1),(-1,0),(0,-1),(1,0)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            safe_areas.append((i, j))
        elif arr[i][j] == 2:
            virus_areas.append((i, j))
def bfs(): # 바이러스 번지는 공간 체크 
    ch = [[False]*m for _ in range(n)]
    q = deque(virus_areas)
    cnt = len(safe_areas)-3 # 벽 개수
    for i, j in virus_areas:
        ch[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            xx, yy = x+dx, y+dy
            if 0 <= xx < n and 0 <= yy < m and not arr[xx][yy] and not ch[xx][yy]:
                ch[xx][yy] = True
                q.append((xx, yy))
                cnt -= 1
    return cnt

def dfs(l, start):
    global maxv
    if l == 3:
        maxv = max(maxv, bfs())
        return
    for i in range(start, len(safe_areas)):
        x, y = safe_areas[i]
        arr[x][y] = 1
        dfs(l+1, i+1)
        arr[x][y] = 0

dfs(0, 0)
print(maxv)