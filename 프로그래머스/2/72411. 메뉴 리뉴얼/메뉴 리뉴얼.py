# 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 최소 2가지 이상의 단품메뉴
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for num in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), num)
            menu += comb
        counter = Counter(menu)
        if len(counter) != 0 and max(counter.values()) != 1:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
        
    return sorted(answer)