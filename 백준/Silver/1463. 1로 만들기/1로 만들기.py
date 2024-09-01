import sys

n = int(sys.stdin.readline())
dp = [1e9] * (10 ** 6 + 1)
dp[1], dp[2], dp[3] = 0, 1, 1

for i in range(1, n):
    try:
        dp[i + 1] = min(dp[i+1], dp[i] + 1)
        dp[i * 2] = min(dp[i*2], dp[i] + 1)
        dp[i * 3] = min(dp[i*3], dp[i] + 1)
    except IndexError:
        continue
print(dp[n])