n,k = map(int,input().split())
dp = [[1] for _ in range(n)]
for i in range(1, n):
    for j in range(1, len(dp[i-1])):
        dp[i].append(dp[i-1][j-1]+dp[i-1][j])
    dp[i].append(1)

print(dp[n-1][k-1])