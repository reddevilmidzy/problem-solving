from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = []

for num in nums:
    k = bisect_left(dp, num)
    if len(dp) <= k:
        dp.append(num)
    else:
        dp[k] = num
print(len(dp))