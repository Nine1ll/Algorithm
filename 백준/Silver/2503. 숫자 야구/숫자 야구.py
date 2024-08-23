import sys


def value_count(mh, ys):
    def strike_count(m, n):
        stk = 0
        for i in range(3):
            if m[i] == n[i]:
                stk += 1
        return stk

    def ball_count(m, n):
        bll = 0
        for i in range(3):
            if m[i] in n and n[i] != m[i]:
                bll += 1
        return bll

    return strike_count(mh, ys), ball_count(mh, ys)


n = int(sys.stdin.readline())
numbers = [str(num) for num in range(100, 999 + 1)
           if "0" not in str(num)
           and str(num)[0] != str(num)[1]
           and str(num)[0] != str(num)[2]
           and str(num)[1] != str(num)[2]]

answer = []
for i in range(n):
    num_mh, strike, ball = sys.stdin.readline().split()
    result = []
    if i == 0:
        for num_ys in numbers:
            st, bl = value_count(num_mh, num_ys)
            if st == int(strike) and bl == int(ball):
                answer.append(num_ys)
    else:
        for num_ys in answer:
            st, bl = value_count(num_mh, num_ys)
            if st == int(strike) and bl == int(ball):
                result.append(num_ys)

        answer = result.copy()

print(len(answer))