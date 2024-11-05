import sys, math
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

m = nums[-1].bit_length()
res = 0
fill = set(nums)
depth = [0] * (m + 1)
for i in range(n):
    x = nums[i]
    while x > 0:
        x = x >> 1
        if x in fill: break
    else:
        depth[nums[i].bit_length()] += 1

for i in range(1, m+1):
    depth[i] += depth[i-1] * 2
    if depth[i] == 2**(i-1):
        print(res)
        break
    res += 2**(i-1) - depth[i]
else:
    print(-1)

