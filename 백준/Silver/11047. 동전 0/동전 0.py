import sys

n , k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

answer = 0
for i in range(n-1, -1, -1):
    answer += k // coins[i]
    k %= coins[i]

print(answer)

