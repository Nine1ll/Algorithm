import sys


def greatest_common_divisor(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    n = greatest_common_divisor(a,b)
    if n == 1:
        print(a * b)
    else:
        print(a*b//n)