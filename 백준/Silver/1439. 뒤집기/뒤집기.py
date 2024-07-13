import sys


def solution(string):
    zero, one = 0,0
    while True:
        try:
            zero_index = string.index("0")
        except ValueError:
            zero_index = -1
        try:
            one_index = string.index("1")
        except ValueError:
            one_index = -1

        if zero_index == -1 and one_index != -1:
            one += 1
            # print(zero, one)
            break
        elif zero_index != -1 and one_index == -1:
            zero += 1
            # print(zero, one)
            break

        else:
            if zero_index < one_index:
                string = string[one_index:]
                zero += 1
            else:
                string = string[zero_index:]
                one += 1

        # print(f"{string}, zero : {zero}, one : {one}")
    return min(zero, one)


s = sys.stdin.readline()
print(solution(s))

