import sys

n = int(sys.stdin.readline())

scores = []
for i in range(n):
    scores.append(int(sys.stdin.readline()))
cnt = 0
for j in range(n-1, 0, -1):
    score, previous_score = scores[j], scores[j-1]
    if score <= previous_score:
        scores[j-1] -= (abs(score - previous_score) + 1)
        cnt += (abs(score - previous_score) + 1)
print(cnt)