import sys

t = int(sys.stdin.readline())

for _ in range(t):
    test_scores = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        test_scores.append(tuple(map(int, sys.stdin.readline().split())))
    test_scores.sort()

    answer = 1
    min_interview_rank = test_scores[0][1]
    for i in range(1, n):
        if test_scores[i][1] < min_interview_rank:
            answer += 1
            min_interview_rank = test_scores[i][1]

    print(answer)