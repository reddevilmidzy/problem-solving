import sys
nums = sys.stdin.readlines()

m = 250
dp = [0] * (m + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 3
res = []
for i in range(3, m + 1):
    dp[i] = dp[i-1] + dp[i-2]* 2

for num in nums:
    n = int(num.rstrip())
    res.append(dp[n])
print(*res,sep='\n')