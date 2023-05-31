import sys
from functools import cmp_to_key as c
input = sys.stdin.readline

k,n = map(int,input().split())
nums = [input().rstrip() for _ in range(k)]
max_num = sorted(nums,key=lambda x:(-len(x), -int(x)))[0]

nums.extend([max_num]*(n-k))
def cmp(x,y): return -int(x+y >= y+x)
def solve(nums: list[str]):
    return int("".join(sorted(nums, key=c(cmp))))
print(solve(nums))