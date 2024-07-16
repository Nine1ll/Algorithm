import sys

money = int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]
left = 1000 - money

answer = 0
for coin in coins:
    if left == 0:
        break
    answer += left // coin
    left -= coin * (left // coin)
print(answer)
