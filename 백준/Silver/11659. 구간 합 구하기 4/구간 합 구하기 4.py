import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0 for i in range(len(numbers)+1)]
for j in range(n):
    prefix_sum[j + 1] = prefix_sum[j] + numbers[j]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start-1])
