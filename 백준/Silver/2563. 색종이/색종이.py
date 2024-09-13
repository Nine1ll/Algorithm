import sys

input = sys.stdin.readline
space = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    start_x, start_y = map(int, input().split())
    for i in range(start_x-1, start_x + 9):
        for j in range(start_y-1, start_y + 9):
            space[j][i] = 1

answer = 0
for i in range(100):
    answer += sum(space[i])

print(answer)