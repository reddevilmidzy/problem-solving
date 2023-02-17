import sys
input = sys.stdin.readline

def calculate(nums: list[int], money: int):
    res = 0
    for num in nums:
        if num <= money:
            res += num
        else:
            res += money
    return res

n = int(input())
nums = list(map(int,input().split()))
m = int(input())

st,ed = 0, max(nums)
ans = 0
while st<=ed:
    mid = (st+ed)//2
    cal_num = calculate(nums, mid)
    if cal_num < m:
        st = mid +1
        ans = max(ans, mid)
    elif cal_num > m:
        ed = mid - 1
    else:
        ans = max(ans, mid)
        break
print(ans)