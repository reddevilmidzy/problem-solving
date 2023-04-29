import sys
input = sys.stdin.readline

def solve():
    for i in range(n):
        for j in range(i):
            if nums[i][1] > nums[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return n - max(dp)
n = int(input())
nums = sorted([list(map(int,input().split())) for _ in range(n)])
dp = [1]*n

print(solve())