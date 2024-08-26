import sys

board = sys.stdin.readline().rstrip().split('.')
answer = []

for pol in board:
    length = len(pol)
    a_count = length // 4
    b_count = (length % 4) // 2
    if (length % 4) % 2 != 0:
        answer = None
        break
    answer.append('AAAA'*a_count + 'BB' * b_count)

if answer is not None:
    print(".".join(answer))
else:
    print(-1)