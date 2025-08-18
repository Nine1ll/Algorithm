def solution(t, p):
    length_of_p = len(p)
    answer = 0
    
    for i in range(0,len(t) - length_of_p + 1):
        part = t[i:i+length_of_p]
        # print(part, p)
        if int(part) <= int(p):
            answer += 1
            
    return answer