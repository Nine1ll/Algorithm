import sys
from collections import deque

add_num = ['0', '1']
ku_apple = "1"


def find_num_bfs(n):
    queue = deque([(ku_apple, 1)])  # 숫자가 '1'일 때 나머지 1을 함께 저장
    visited = set([1])  # 이미 확인한 나머지를 저장

    while queue:
        current_str, remainder = queue.popleft()

        if remainder == 0:
            return current_str

        for d in add_num:
            new_str = current_str + d
            new_remainder = (remainder * 10 + int(d)) % n

            if new_remainder not in visited:
                queue.append((new_str, new_remainder))
                visited.add(new_remainder)

        if len(current_str) > 100:
            return 'BRAK'


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(find_num_bfs(n))
