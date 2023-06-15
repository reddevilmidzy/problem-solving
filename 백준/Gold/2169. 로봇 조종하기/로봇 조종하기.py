from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0]*(m) for _ in range(n)] for _ in range(2)]

# 첫번째 줄은 -> 만 가능
dp[0][0][0] = board[0][0]
dp[1][0][0] = board[0][0]
for x in range(1, m):
    dp[0][0][x] = dp[0][0][x-1] + board[0][x]
    dp[1][0][x] = dp[1][0][x-1] + board[0][x]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[0][i][j] = max(dp[0][i-1][j], dp[1][i-1][j]) + board[i][j]
            dp[1][i][m-j-1] = max(dp[1][i-1][m-j-1], dp[0][i-1][m-j-1]) + board[i][m-j-1]
        else:
            dp[0][i][j] = max(dp[0][i-1][j], dp[0][i][j-1], dp[1][i-1][j]) + board[i][j]
            dp[1][i][m-j-1] = max(dp[1][i-1][m-j-1], dp[1][i][m-j], dp[0][i-1][m-j-1]) + board[i][m-j-1]

print(max(dp[0][n-1][m-1], dp[1][n-1][m-1]))