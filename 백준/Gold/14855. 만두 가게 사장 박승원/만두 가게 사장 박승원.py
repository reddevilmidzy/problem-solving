import sys
input = sys.stdin.readline

n,m,c0,d0 = map(int,input().split())

nums = [[0,0,0,0]] + [list(map(int,input().split())) for _ in range(m)]
# a,b,c,d = 남은 속, 필요한 속, 필요한 밀가루, 판매금액

dp = [[0]*(n + 1) for _ in range(m + 1)]
# dp[i][j] = i번째 만두 j 밀가루
# print(nums)

for j in range(c0, n + 1):
    dp[0][j] = (j//c0) * d0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        can = nums[i][0] // nums[i][1]
        for k in range(0, can + 1):
            if j - nums[i][2]*k >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j-nums[i][2]*k] + nums[i][3]*k)
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[m][n])