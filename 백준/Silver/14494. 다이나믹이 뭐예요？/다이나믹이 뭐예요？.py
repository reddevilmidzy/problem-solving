n,m = map(int, input().split())
dp = [[0 for i in range(n+1)] for j in range(m+1)]
dp[1][1] =1

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i-1][j] + dp[i-1][j-1] + dp[i][j-1]

print(dp[m][n]%(10**9+7))