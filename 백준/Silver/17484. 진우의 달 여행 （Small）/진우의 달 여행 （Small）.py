INF = int(1e9)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(m)]] + [[[INF,INF,INF] for _ in range(m)] for _ in range(n)]

for i in range(1,n+1):
    for j in range(m):
        if j < m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + board[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + board[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + board[i-1][j]

print(min(map(min, dp[n])))