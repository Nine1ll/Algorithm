import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

answer = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    answer += a[i]*b[i]

print(answer)