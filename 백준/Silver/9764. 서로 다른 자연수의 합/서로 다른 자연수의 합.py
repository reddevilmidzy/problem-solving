# dp 1차원으로는 안되는건감..
# dp[i][j-1] => j를 포함하지 않고 i를 만드는 경우
# dp[i][j] + dp[i-1][j-1] => j 포함 i 만들기

import sys
input = sys.stdin.readline
mod = 100999
nums = [int(input()) for _ in range(int(input()))]
INF = max(nums)

def solve(nums: list[int]):
    res = []
    # 0은 암대나 같다붙임 
    dp = [[1]*(INF+1)] + [[0]*(INF+1) for _ in range(INF)]

    for i in range(1, INF+1):
        for j in range(1, INF+1):
            dp[i][j] = dp[i][j-1]
            if i >= j:
                dp[i][j] += dp[i-j][j-1]
                dp[i][j] %= mod
    
    for num in nums:
        res.append(dp[num][num])
    return res
print(*solve(nums))