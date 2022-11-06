import sys
input = sys.stdin.readline

t = int(input())

dp = [-1, 0, 1, 2]

for i in range(4, 21):
    dp.append((i-1)*(dp[i-1]+dp[i-2]))

for _ in range(t):
    n = int(input())
    print(dp[n])