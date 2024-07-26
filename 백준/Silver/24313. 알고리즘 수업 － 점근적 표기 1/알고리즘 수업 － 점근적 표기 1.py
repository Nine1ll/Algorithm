import sys

beta, alpha = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
min_n = int(sys.stdin.readline())

fx = beta * min_n + alpha
gx = min_n
if fx <= c * gx and beta <= c:
    print(1)
else:
    print(0)
