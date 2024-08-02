import sys


def greatest_common_divisor(A, B):
    while True:
        C = A % B
        if C == 0:
            return B
        A = B
        B = C


a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
molecular = a * d + c * b  # 분자
denominator = b * d  # 분모
gcd = greatest_common_divisor(molecular, denominator)
molecular //= gcd
denominator //= gcd

print(molecular, denominator)
