import sys

input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n  # 0 ~ n -1 까지
for i in range(1,n):
    for j in range(i):
        if soldiers[j] > soldiers[i]: # 앞이 더 큰 경우
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))