import sys

a, b = map(int, sys.stdin.readline().split())
answer = 1
for i in range(2, min(a,b)+1):
    while a % i == 0 and b % i == 0:
        answer *= i
        a, b = a//i, b//i
answer *= a * b
print(answer)