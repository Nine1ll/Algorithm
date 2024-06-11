import sys


def divisor(num):
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def solution(divisors, num):
    result = f"{num}"
    if sum(divisors) == n:
        result += " = "
        for idx, ele in enumerate(divisors):
            if idx == len(divisors) - 1:
                result += str(ele)
            else:
                result += str(ele) + " + "
    else:
        result += " is NOT perfect."

    return result


while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    print(solution(divisor(n), n))