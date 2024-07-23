import sys

n = int(sys.stdin.readline())

k = 0
for i in range(n-1):
    k += i*(i+1)//2

print(int(k))
print(3)