import sys
input = sys.stdin.readline

def cutting(h):
    res = 0
    for num in nums:
        if num-h > 0:
            res += num - h
        else:
            break
    return res

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())), reverse=True)

st,ed = 0, max(nums)
while st <= ed:
    mid = (st+ed)//2
    if cutting(mid) >= m:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)