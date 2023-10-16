import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = {num:0 for num in nums}
for num in nums:
    if num-1 in dp:
        dp[num] = dp[num-1] + 1
    else:
        dp[num] = 1
print(n - max(dp.values()))