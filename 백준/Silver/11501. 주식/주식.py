import sys
input = sys.stdin.readline

def solve(nums):
    res = 0
    max_stock = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < max_stock:
            res += max_stock - nums[i]
        else:
            max_stock = nums[i]
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    print(solve(nums))