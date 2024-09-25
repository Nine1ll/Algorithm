import sys

dp = [1] * (1000 + 1)
n = int(sys.stdin.readline())
for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = 2 * dp[i - 1] + 1
    else:
        dp[i] = 2 * dp[i - 1] - 1
print(dp[n] % 10007)
