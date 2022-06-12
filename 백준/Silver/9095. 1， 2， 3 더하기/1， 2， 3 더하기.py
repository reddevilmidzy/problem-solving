import sys
input = sys.stdin.readline
dp = [-1] * 11
for i in range(1, 11):
    if i < 3:
        dp[i] = i
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for i in range(int(input())):
    print(dp[int(input())])