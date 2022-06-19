n = int(input())
dp = [i for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,int(n**0.5)+1):
        if 0<=i-j**2:
            dp[i] = min(dp[i-j**2]+1, dp[i])
print(dp[n])