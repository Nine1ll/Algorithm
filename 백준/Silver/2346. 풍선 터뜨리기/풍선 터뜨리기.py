import sys
from collections import deque

n = int(sys.stdin.readline())
balloons = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))  # 풍선 위치와 숫자를 함께 저장

answer = []
while balloons:
    idx, move = balloons.popleft()  # 풍선의 위치와 숫자를 추출
    answer.append(idx)  # 결과 리스트에 위치를 추가
    
    if move > 0:  # 오른쪽 이동
        move -= 1  # 현재 위치는 이미 제거되었으므로 1만큼 감소
    balloons.rotate(-move)  # deque를 사용하여 풍선을 회전

print(*answer)
