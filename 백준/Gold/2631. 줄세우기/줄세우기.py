n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [1]*n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(n - max(dp))