import sys

seasoned_price, fried_price, half_price, x, y = map(int, sys.stdin.readline().split())
min_quantity = min(x, y)
min_one_one_price = min(seasoned_price + fried_price, half_price * 2)
answer = min_quantity * min_one_one_price

# 남은 수량 털기
left_seasoned, left_fried = x - min_quantity, y - min_quantity
if left_seasoned > 0:
    answer += min(left_seasoned * seasoned_price,  left_seasoned* half_price * 2)
else:
    answer += min(left_fried * fried_price,  left_fried* half_price * 2)

print(answer)