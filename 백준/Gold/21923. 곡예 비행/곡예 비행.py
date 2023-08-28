import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cost = [list(map(int,input().split())) for _ in range(n)]
INF = sys.maxsize

u_dp = [[-INF]*m for _ in range(n)]
d_dp = [[-INF]*m for _ in range(n)]

u_dp[n-1][0] = cost[n-1][0]
d_dp[-1][-1] = cost[-1][-1]

for j in range(m):
    for i in range(n-1,-1,-1):
        if i==n-1 and j==0: continue
        if j == 0:
            u_dp[i][j] = u_dp[i+1][j] + cost[i][j]
        elif i == n-1:
            u_dp[i][j] = u_dp[i][j-1] + cost[i][j]
        else:
            u_dp[i][j] = max(u_dp[i+1][j], u_dp[i][j-1]) + cost[i][j]

for j in range(m-1, -1, -1):
    for i in range(n-1, -1, -1):
        if i==n-1 and j==m-1: continue
        if i==n-1:
            d_dp[i][j] = d_dp[i][j+1] + cost[i][j]
        elif j==m-1:
            d_dp[i][j] = d_dp[i+1][j] + cost[i][j]
        else:
            d_dp[i][j] = max(d_dp[i][j+1], d_dp[i+1][j]) + cost[i][j]

ans = -INF

for i in range(n):
    for j in range(m):
        ans = max(ans, u_dp[i][j] + d_dp[i][j])

print(ans)