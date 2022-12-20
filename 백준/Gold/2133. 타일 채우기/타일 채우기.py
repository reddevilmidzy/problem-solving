n = int(input())

dp = [0,0,3,0,11] + [0]*(n-4)

for i in range(5, n+1):
    if i%2 == 0:
        dp[i] = dp[i-2]*4 - dp[i-4]

print(dp[n])