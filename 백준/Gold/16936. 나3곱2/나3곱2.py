import sys

n = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
# 3으로 나누거나, 2를 곱하거나
reverse_calculate = {number: [number * 3,
                              number // 2 if number % 2 == 0 else -1] for number in B}
order = {b: [] for b in B}

for b in B:  # 100
    for cal in reverse_calculate[b]:  # 100
        if cal in reverse_calculate.keys():  # 2
            order[b].append(cal)
# print(order)
start_number = 0
for key, value in order.items():
    if len(value) == 0:
        start_number = key

for i in range(len(B)):
    if i == 0:
        print(start_number, end=" ")
    else:
        for key, value in order.items():
            if start_number in value:
                start_number = key
                print(start_number, end=" ")