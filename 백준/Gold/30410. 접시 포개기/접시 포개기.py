import sys, math
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

res = max(nums)
tmp = []
pre = nums[0]
cnt = 1
for i in range(1, n):
    if pre != nums[i]:
        tmp.append((pre,cnt))
        cnt = 1
        pre = nums[i]
    else:
        cnt += 1

tmp.append((pre,cnt))

new_nums = []

for val,cnt in tmp:
    if val == 1:
        if cnt % 2 == 0:
            new_nums.append((2, cnt//2))
        else:
            new_nums.append((1, cnt))
    else:
        new_nums.append((2, cnt))

nums.clear()
pre = 0
for val,cnt in new_nums:
    if val == 2:
        pre += cnt
    else:
        if pre:
            nums.append((2, pre))
        nums.append((val, cnt))
        pre = 0
if pre:
    nums.append((2, pre))

k = 0
if nums[0][0] == 2:
    nums.insert(0, (1, 0))
if nums[-1][0] == 2:
    nums.append((1, 0))

if len(nums) == 1:
    k = nums[0][1]//2
for i in range(1, len(nums)-1, 2):
    k = max(k, nums[i][1] + (nums[i+1][1]//2) + (nums[i-1][1]//2))

if k:
    print(2**(int(math.log2(k)) + 1))
else:
    print(res)