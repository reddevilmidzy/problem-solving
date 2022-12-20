n = int(input())
dp = [0,0,3,0,11] + [0]*(n-4)

for i in range(6, n+1,2):
    dp[i] = dp[i-2]*4 - dp[i-4]

print(dp[n])