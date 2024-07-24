import sys

n, m = map(int,sys.stdin.readline().split())
union_set = {}

for i in list(map(int, sys.stdin.readline().split())):
    union_set[i] = 1

for i in list(map(int, sys.stdin.readline().split())):
    try:
        union_set[i] -= 1
    except KeyError:
        union_set[i] = 1

print(sum(union_set.values()))