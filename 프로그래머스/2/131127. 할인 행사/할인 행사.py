# 언제 시작하면 원하는 물건을 모두 살 수 있나?
def solution(want, number, discount):
    dic = {}
    answer = 0

    for start_num in range(len(discount)-9):
        discount_days = discount[start_num:start_num + 10] 
        for i in range(len(want)):
            dic[want[i]] = number[i]

        for item in discount_days:
            if item in dic:
                dic[item] -= 1
            else:
                dic[item] = -1
        
        count = 0
        for value in dic.values():
            if value > 0:
                count += 1
        
        if count == 0:
            answer+=1
            
    return answer
