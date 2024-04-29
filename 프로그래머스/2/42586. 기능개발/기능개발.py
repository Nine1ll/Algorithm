import math
from collections import deque

def solution(progresses, speeds):
    n = len(progresses)
    days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(n)]

    answer = []
    count = 0
    max_day = days[0]
    for i in range(n):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]
    
    answer.append(count)
    
    return answer
