import sys

i = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == p == v == 0:
        break

    answer = (v // p) * l
    if v % p >= l:
        answer += l
    else :
        answer += v%p
    print(f"Case {i}: {answer}")
    i += 1