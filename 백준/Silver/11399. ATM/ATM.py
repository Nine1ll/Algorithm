import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
answer = 0
for i in range(n):
    answer += sum(times[:i+1])

print(answer)