def solution(n, lost, reserve):

    for p in lost[:]:
        if p in reserve:
            lost.remove(p)
            reserve.remove(p)
    
    lost.sort()

    for p in lost[:]:
        front, rear = p-1, p+1
        if front in reserve:
            reserve.remove(front)
            lost.remove(p)
        elif rear in reserve:
            reserve.remove(rear)
            lost.remove(p)

    answer =  n - len(lost)
    return answer