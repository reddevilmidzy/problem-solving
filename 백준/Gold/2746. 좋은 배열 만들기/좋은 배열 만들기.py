from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int,input().split())))
res = 0
tot = sum(nums)

tmp = tot - nums[-1] - nums[-1]
for i in range(n-1):
    val = tmp - nums[i]
    l = bisect_left(nums, val, i + 1, n - 1)
    r = bisect_right(nums, val, i + 1, n - 1)
    res += r - l

tmp = tot - nums[-1] - nums[-2]

for i in range(n-2):
    if tmp - nums[i] == nums[-2]:
        res += 1

tmp = tot - nums[-1] - nums[-2] - nums[-3]
if tmp == nums[-3]:
    res += 1

print(res)