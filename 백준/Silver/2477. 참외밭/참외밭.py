import sys

'''
좌회전 : 4 -> 2 -> 3 -> 1
안으로 들어간 넓이는 반대의 순서가 나올 경우 우회전했다 = 바로 직전 길이와 지금 길이를 곱해서 전체에서 뺀다.
'''


def turn_left_check(pre, now):
    if pre == 4:
        if now == 2:
            return True
        else:
            return False
    elif pre == 2:
        if now == 3:
            return True
        else:
            return False
    elif pre == 3:
        if now == 1:
            return True
        else:
            return False
    else:
        if now == 4:
            return True
        else:
            return False


k = int(sys.stdin.readline())

transverse, length = 0, 0
pre_direction = 0
directions = []
lengths = []
for _ in range(6):
    d, m = map(int, sys.stdin.readline().split())
    directions.append(d)
    lengths.append(m)
    if d == 4 or d == 3:
        transverse = max(transverse, m)
    else:
        length = max(length, m)

loss = 0
for i in range(6):
    pre_d, now_d = 0, 0
    if i == 5:
        pre_d = directions[5]
        now_d = directions[0]
    else:
        pre_d, now_d = directions[i], directions[i + 1]
    if not turn_left_check(pre_d, now_d):
        if i == 5:
            loss = lengths[i] * lengths[0]
        else:
            loss = lengths[i] * lengths[i+1]

print((transverse * length - loss) * k)