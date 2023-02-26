import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

inc_dp = [1]*n
dec_dp = [1]*n
res = [0]*n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and inc_dp[i] < inc_dp[j] + 1:
            inc_dp[i] = inc_dp[j] + 1

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if nums[i] > nums[j] and dec_dp[i] < dec_dp[j] + 1:
            dec_dp[i] = dec_dp[j] + 1
    
    res[i] = dec_dp[i] + inc_dp[i] - 1

print(max(res))