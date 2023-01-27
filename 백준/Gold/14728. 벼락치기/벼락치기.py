import sys
input = sys.stdin.readline

n,t = map(int,input().split())
gazy = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if j - gazy[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-gazy[i][0]]+gazy[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][t])