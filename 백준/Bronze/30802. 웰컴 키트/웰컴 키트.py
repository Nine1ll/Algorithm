import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int,sys.stdin.readline().split())

t_counts = 0
for size in sizes:
    if size % t == 0:
        t_counts += size // t
    else:
        t_counts += size // t + 1

print(t_counts)
print(n // p, n % p)