import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
nums = list(map(int,input().split()))
dp = [INF]*(n)
if nums[0]!=0:
    dp[0] = 0
    for i in range(1,nums[0]):
        dp[i] = 1
elif n==1 and nums[0]==0:
    dp[0] = 0

for i in range(n):
    if dp[i] != INF:
        for j in range(1, nums[i]+1):
            if i+j<n:
                dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[-1] if dp[-1] != INF else -1)