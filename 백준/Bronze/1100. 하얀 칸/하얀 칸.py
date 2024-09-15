import sys

answer = 0
for i in range(8):
    board = sys.stdin.readline().strip()
    if i % 2 == 0:
        answer += board[::2].count('F')
    else:
        answer += board[1::2].count('F')
print(answer)