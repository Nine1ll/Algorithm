def solution(participant, completion):
    dic = {}
    
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    answer = ''
    for c in completion:
        dic[c] -= 1
    
    for key in dic.keys():
        if dic[key] > 0:
            answer = key
            
    return answer