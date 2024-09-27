import sys


def binary_search(array, target, start, end):
    mid = (start+end) // 2
    if start > end:
        return mid
    height_sum = 0
    for i in range(n):
        if array[i] > mid:
            height_sum += (array[i] - mid)

    if height_sum < target:
        return binary_search(array, target, start, mid-1)
    elif height_sum > target:
        return binary_search(array, target, mid+1, end)
    else:
        return mid


n, m = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
min_height = 1
max_height = max(heights)
print(binary_search(heights, m, min_height, max_height))


