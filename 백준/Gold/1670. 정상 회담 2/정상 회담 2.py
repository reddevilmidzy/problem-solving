mod = 987654321
n = int(input())//2
dp = [0]*(5001)
dp[0] = 1

for i in range(1, n+1):
    for j in range(i):
        dp[i] += (dp[j]%mod)*(dp[i-1-j]%mod) % mod
        dp[i] %= mod
    dp[i] %= mod

print(dp[n])