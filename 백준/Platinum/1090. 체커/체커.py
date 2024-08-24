import sys

n = int(sys.stdin.readline())
coordinate_x, coordinate_y = [], []
coordinate = []
answer = [1e9 for i in range(64)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))
    coordinate_x.append(x)
    coordinate_y.append(y)

for x in coordinate_x:
    for y in coordinate_y:
        distance = []
        for nx, ny in coordinate:
            distance.append(abs(nx - x) + abs(ny - y))
        distance.sort()
        sum = 0
        for i in range(len(coordinate)):
            sum += distance[i]
            answer[i] = min(answer[i], sum)

for i in range(n):
    print(answer[i], end=' ')
