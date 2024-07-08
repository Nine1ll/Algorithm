import sys

case_list = ["Equilateral", "Isosceles", "Scalene", "Invalid"]

while True:
    n = list(map(int, sys.stdin.readline().split()))
    set_n = set(n)
    n.sort()
    if sum(n) == 0:
        break

    max_n = n.pop()
    if sum(n) <= max_n:
        print(case_list[3])
    elif len(set_n) == 3:
        print(case_list[2])
    elif len(set_n) == 2:
        print(case_list[1])
    else:
        print(case_list[0])
