import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

r_stk = []
r_idx = [n] * n
l_stk = []
l_idx = [-1] * n

for i in range(n):
    while r_stk and nums[r_stk[-1]] > nums[i]:
        r_idx[r_stk.pop()] = i
    r_stk.append(i)

    while l_stk and nums[l_stk[-1]] > nums[n - i -1]:
        l_idx[l_stk.pop()] = n - i - 1
    l_stk.append(n-i-1)

pre = [0]
for num in nums:
    pre.append(pre[-1] + num)

res = 0

for i in range(n):
    res = max(res, nums[i] * (pre[r_idx[i]] - pre[l_idx[i]+1]))

print(res)
