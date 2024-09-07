import sys
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    # n보다 크거나 같은 소수 중에 가장 작은 소수를 찾기
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        if is_prime(n):
            print(n)
            break
        else:
            n += 1