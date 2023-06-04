import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]
# print(mat[0][0]*mat[0][1]*mat[1][1] + mat[0][0]*mat[2][0]*mat[2][1])
# print(mat[1][0]*mat[1][1]*mat[2][1] + mat[0][0]*mat[0][1]*mat[2][1])

for diff in range(n):
    for i in range(n-diff-1):
        j = i+diff+1
        dp[i][j] = INF
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+(mat[i][0]*mat[k][1]*mat[j][1]))

print(dp[0][n-1])