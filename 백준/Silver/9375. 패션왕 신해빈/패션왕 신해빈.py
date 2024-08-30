import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    clothes = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, types = sys.stdin.readline().rstrip().split()
        try:
            clothes[types].append(name)
        except KeyError:
            clothes[types] = [name]
    answer = 1
    for key in clothes.keys():
        comb = len(clothes[key])
        answer *= (comb + 1)

    print(answer - 1)