import sys


def solution(n):
    if n == 1:
        return triangle[0][0]
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0] + dp[0][0]
    dp[1][1] = triangle[1][1] + dp[0][0]

    for i in range(2, n):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][i] = triangle[i][i] + dp[i - 1][i - 1]
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])

    return max(dp[n - 1])


n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
print(solution(n))