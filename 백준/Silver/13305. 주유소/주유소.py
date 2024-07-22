import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

money = 0
for i in range(len(price) - 1):
    if price[i] < price[i + 1]:
        price[i + 1] = price[i]

for j in range(len(length)):
    money += length[j] * price[j]

print(money)
