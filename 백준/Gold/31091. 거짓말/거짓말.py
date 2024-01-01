from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
one = bisect_left(nums,1)
ms = []
ps = []
for num in nums:
    if num <= 0:
        ms.append(-num)
    else:
        ps.append(num)

ms.reverse()
m = len(ms)
res = []
for i in range(n+1):
    ps_r = bisect_right(ps,i)
    ms_l = bisect_left(ms,i)
    if (m-ms_l)+ps_r+i==n:
        res.append(i)
print(len(res))
print(*res)