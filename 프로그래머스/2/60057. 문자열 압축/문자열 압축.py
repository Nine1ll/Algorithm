def solution(string):
    min_length = 10000
    for i in range(1, len(string) // 2 + 1):  # 자르는 단위
        cnt = 1
        answer = ""
        for j in range(0, len(string) - i + 1, i):
            now = string[j:j + i]
            next = string[j + i:j + i * 2]
            if now == next:
                cnt += 1
            else:  # now =/= next
                if cnt <= 1:
                    answer += now
                else:
                    answer += f"{str(cnt)}{now}"
                cnt = 1
                if len(next) < i:
                    answer += next

        if min_length > len(answer):
            min_length = len(answer)

    if min_length == 10000:
        min_length = 1

    return min_length

