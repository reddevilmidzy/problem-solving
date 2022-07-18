import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [0]*(n)

for i in range(n):
    if i == 0:
        dp[0] =nums[0]
    elif i == 1:
        dp[1]= nums[0]+nums[1]
    elif i == 2:
        dp[2] = max(dp[1],nums[1]+nums[2], nums[0]+nums[2])
    else:
        dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i-1]+nums[i],dp[i-1])
print(dp[-1])