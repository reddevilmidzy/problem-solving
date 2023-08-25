mod=10**6
dp=[[1],[1,1,0],[2,1,1]]
for i in range(3,1001):
	dp.append([sum(dp[i-1])%mod,dp[i-1][0],dp[i-1][1]])

n = int(input())
ans = sum(dp[n])
for i in range(n):
	ans += sum(dp[i])*sum(dp[n-i-1])
	ans %= mod

print(ans)