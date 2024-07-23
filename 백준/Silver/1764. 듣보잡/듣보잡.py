import sys

n, m = map(int, sys.stdin.readline().split())

listen = {}
for _ in range(n):
    listen[sys.stdin.readline().rstrip()] = 0

for _ in range(m):
    try:
        listen[sys.stdin.readline().rstrip()] += 1
    except KeyError:
        continue
listen = sorted(listen.items())

noone = 0
for i in range(len(listen)):
    noone += listen[i][1]
print(noone)
for key, value in listen:
    if value == 1:
        print(key)

