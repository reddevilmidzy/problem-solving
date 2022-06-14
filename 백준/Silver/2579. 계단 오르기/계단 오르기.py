import sys
input = sys.stdin.readline
n = int(input())
stair = [int(input().rstrip()) for i in range(n)]

dp = [0] * (10**4+1)
if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0]+stair[1])
else:
    dp[0]=stair[0]
    dp[1] = max(stair[1], stair[0]+stair[1])
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+stair[i], stair[i-1]+stair[i]+dp[i-3])

    print(dp[n-1])