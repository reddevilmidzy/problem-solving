from functools import cmp_to_key
n = int(input())
nums = list(map(str,input().split()))

def cmp(x,y):
    if x+y >= y+x:
        return -1
    return 1

def solve(nums: list[str]):
    return int("".join(sorted(nums, key=cmp_to_key(cmp))))

print(solve(nums))