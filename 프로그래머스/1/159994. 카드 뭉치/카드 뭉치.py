from collections import deque

def solution(cards1, cards2, goal):
    # FIFO만 되는 상황에서 goal을 도달할 수 있나?
    cards1, cards2 = deque(cards1), deque(cards2)
    
    boolean = True
    for target in goal:
        word1 = ""
        word2 = ""
        if cards1:
            word1 = cards1[0]
        if cards2:
            word2 = cards2[0]
            
        if target == word1:
            cards1.popleft()
        elif target == word2:
            cards2.popleft()
        else:
            boolean = False
            break
    answer = ''
    if boolean:
        answer = "Yes"
    else:
        answer = "No"
    return answer
