import sys

t = int(sys.stdin.readline())
dp = [1] * 100
dp[3] = dp[0] + dp[2]
dp[4] = dp[3]
dp[5] = dp[0] + dp[4]
for i in range(6, 100):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n-1])
