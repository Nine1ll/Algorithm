# 보물
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()

answer = 0
for v in a: # O(N)
    value = max(b) # O(N)
    b.remove(value) # O(N)
    answer += v * value

print(answer)