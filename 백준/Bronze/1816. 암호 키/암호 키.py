import sys

min_decimal = 10 ** 6

n = int(sys.stdin.readline())
for _ in range(n):
    s = int(sys.stdin.readline())
    for i in range(2,  min_decimal + 1):
        if s % i == 0:
            print('NO')
            break
        if i == min_decimal:
            print('YES')