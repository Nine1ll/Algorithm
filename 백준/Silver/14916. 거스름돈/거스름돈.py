import sys

money = int(sys.stdin.readline())

five = money // 5
cnt = 0
if money % 5 == 0:
    cnt = money // 5
else:
    while True:
        if five < 0:
            cnt = -1
            break
        last = money - 5 * five
        if last % 2 == 0:
            cnt = five + last // 2
            break
        else:
            five -= 1

print(cnt)