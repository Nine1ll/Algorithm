from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    queue = deque(prices)
    i = 0
    while queue:
        price = queue.popleft()
        for ele in queue:
            if ele >= price:
                # print(price, ele)
                answer[i] += 1
            else:
                answer[i] += 1
                break
        i+=1

    return answer