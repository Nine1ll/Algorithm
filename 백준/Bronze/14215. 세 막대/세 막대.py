import sys
# 가장 큰 둘레


def check_tri():
    return max_num < sum(numbers)


numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
max_num = numbers.pop()

if check_tri():
   pass
else:
    while True:
        max_num = max_num - 1
        if check_tri():
            break

print(max_num + sum(numbers))