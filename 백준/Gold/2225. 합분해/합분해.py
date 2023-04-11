n,k = map(int,input().split())
mod = int(1e9)

dp = [[0]*(n+1) for _ in range(k)]

dp[0] = [1]*(n+1)

for i in range(1, k):
    for j in range(n+1):
        dp[i][j] = sum([dp[i-1][u] for u in range(j+1)])%mod
print(dp[k-1][n])