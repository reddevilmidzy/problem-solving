import sys
input = sys.stdin.readline
"""
10: 5
11: 6
12: 6
13: 7
14: 7
15: 7
16: 8
17: 9
18: 9
19: 10
20: 10
"""
n = int(input())
dp = [[0]*2 for _ in range(max(3, n) + 1)]

# 0 비우기
# 1 채우기
# dp[1][0] = 1
# dp[1][1] = 1

# dp[2][0] = 1
dp[2][1] = 1

for i in range(3, n+1):
    dp[i][0] = dp[i//2-(i%2==0)][0] + dp[i//2][0] + 1
    dp[i][1] = dp[i-1][0] + 1

print(max([1+dp[i][1]+dp[n-i-1][1] for i in range(n)]))