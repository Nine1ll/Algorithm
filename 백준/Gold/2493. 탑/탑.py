import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

stack = []  # (index, height)
answer = [0] * n

for i, height in enumerate(towers, start=1):  # index를 1부터 시작
    # 현재 탑보다 낮은 탑은 수신 불가 → 스택에서 제거
    while stack and stack[-1][1] < height:
        stack.pop()

    # 스택이 남아있으면, 그 탑이 수신 가능
    if stack:
        answer[i-1] = stack[-1][0]

    # 현재 탑을 스택에 추가
    stack.append((i, height))

print(*answer)