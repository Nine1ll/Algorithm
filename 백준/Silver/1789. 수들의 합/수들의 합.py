import sys

s = int(sys.stdin.readline())
n = 0
while True:
    n += 1
    if n**2 + n - 2*s > 0:
        break

print(n-1)
