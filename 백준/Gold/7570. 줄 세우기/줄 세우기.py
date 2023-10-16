import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = {num:0 for num in nums}
dp[min(nums)-1] = 0
for num in nums:
    dp[num] = dp[num-1] + 1

print(n - max(dp.values()))