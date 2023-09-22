import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = nums[0]+nums[-1]

l,r = 0,n-1

while l < r:
    diff = nums[l]+nums[r]
    if abs(diff) < abs(ans):
        ans = diff
    if diff < 0:
        l += 1
    elif diff > 0:
        r -= 1
    else:
        break

print(ans)