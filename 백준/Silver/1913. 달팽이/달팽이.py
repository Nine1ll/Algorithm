import sys

n = int(sys.stdin.readline())
find_num = int(sys.stdin.readline())

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 하 좌 상 우
snail = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
x, y = 0, 0
root = 0

result_coordinate = []
for i in range(n**2, 0, -1):
    if i == find_num:
        result_coordinate = [x, y]
    snail[y][x] = i
    dx, dy = x + direction[root][0], y + direction[root][1]
    if dx >= n or dx < 0 or dy >= n or dy < 0 or snail[dy][dx] != 0:
        root = (root+1) % 4

    x, y = x + direction[root][0], y + direction[root][1]


for s in snail:
    print(*s)
print(result_coordinate[1] + 1, result_coordinate[0] + 1)
