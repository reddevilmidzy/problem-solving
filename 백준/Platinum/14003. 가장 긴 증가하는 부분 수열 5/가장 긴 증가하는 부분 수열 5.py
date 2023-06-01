import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = []
trace = []
ans = []
for num in nums:
    k = bisect_left(dp, num)
    if len(dp) <= k:
        dp.append(num)
        trace.append((len(dp)-1, num))
    else:
        dp[k] = num
        trace.append((k,num))

m = len(dp)
idx = m - 1
for i in range(n-1, -1, -1):
    if trace[i][0] == idx:
        ans.append(trace[i][1])
        idx -= 1

print(m)
print(*ans[::-1])