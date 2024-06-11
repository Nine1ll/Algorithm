import sys


def divisor(num):
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return len(divisors)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

ans_sum = 0
ans_min = -1
for i in range(n, m + 1):
    if divisor(i) == 1:
        if ans_sum == 0:
            ans_min = i
        ans_sum += i

if ans_sum != 0:
    print(ans_sum)
print(ans_min)