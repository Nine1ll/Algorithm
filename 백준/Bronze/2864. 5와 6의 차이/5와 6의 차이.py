import sys


# 그냥 최대값인 경우 => 모든 5를 6으로 봄
# 최소 값인 경우 => 모든 6을 5로 봄
def replace56(string, lst):
    if '5' in string:
        lst.append(int(string.replace('5', '6')))

    if '6' in string:
        lst.append(int(string.replace('6', '5')))


a, b = sys.stdin.readline().split()
a_comb = [int(a)]
b_comb = [int(b)]

replace56(a, a_comb)
replace56(b, b_comb)
# print(a_comb, b_comb)
print(min(a_comb) + min(b_comb), max(a_comb) + max(b_comb))