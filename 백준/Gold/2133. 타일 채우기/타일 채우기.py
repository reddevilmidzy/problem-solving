n=int(input())
dp=[1,0,3]+[0]*(n-2)
for i in range(4,n+1,2):
    dp[i]=dp[i-2]*4-dp[i-4]
print(dp[n])