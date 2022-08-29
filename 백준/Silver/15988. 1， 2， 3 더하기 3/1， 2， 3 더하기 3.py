import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]
max_num = max(nums)
if max_num < 4:
    dp = [0,1,2,4]
else:
    dp = [0]*(max_num+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, max_num+1):
        dp[i] = (dp[i-3]+dp[i-2]+dp[i-1])%1000000009

for k in nums:
    print(dp[k])