import sys


def binary_search(target, start, end):
    global flag
    while start <= end:
        mid = (start + end) // 2
        if int(((y + mid) * 100 / (x + mid))) > target:
            flag = 1
            end = mid - 1
        else:
            start = mid + 1
    return start


x, y = map(int, sys.stdin.readline().split())
z = int(y * 100 / x)
start, end, flag = 1, 10 ** 9 + x, 0

start = binary_search(z, start, end)
if flag:
    print(start)
else:
    print(-1)