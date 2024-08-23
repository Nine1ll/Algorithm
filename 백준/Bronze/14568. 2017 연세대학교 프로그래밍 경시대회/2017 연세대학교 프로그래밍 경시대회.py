import sys

candy = int(sys.stdin.readline())


def condition_check(n, y, t):
    return n > 0 and y > 0 and t > 0 and n > y + 1 and t % 2 == 0 and candy == n + y + t


result = 0
for t in range(1, candy):
    for n in range(1, candy):
        for y in range(1, candy):
            if condition_check(n, y, t):
                result += 1

print(result)