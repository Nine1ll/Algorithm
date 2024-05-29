def solution(s):
    pcnt = 0
    ycnt = 0
    s = s.lower()
    for c in s:
        if c == 'p':
            pcnt += 1
        if c == 'y':
            ycnt += 1
    answer = True if pcnt == ycnt else False    
    return answer