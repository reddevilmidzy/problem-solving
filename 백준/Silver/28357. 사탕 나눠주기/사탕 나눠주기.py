import sys
input = sys.stdin.readline

def canbe(x):
    res = 0
    for num in nums:
        if num > x:
            res += num-x
        else:
            break

    return res <= k

n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse=True)

st,ed = 0, nums[0]
res = 0

while st <= ed:
    mid = (st+ed)//2
    if canbe(mid):
        res = mid
        ed = mid - 1
    else:
        st = mid + 1

print(res)