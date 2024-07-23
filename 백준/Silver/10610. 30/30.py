import sys

k = list(map(int, sys.stdin.readline().rstrip()))
if 0 not in k:
    print(-1)
else:
    if sum(k) % 3 != 0:
        print(-1)
    else:
        k.sort(reverse=True)
        print("".join(str(x) for x in k))