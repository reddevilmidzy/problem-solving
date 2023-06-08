import sys
input = sys.stdin.readline

n = int(input())
if not n: print(0); exit(0)
nums = [int(input()) for _ in range(n)]
nums.sort()
cut = n*15//100 + (n*15%100>=50)
mom = (n-2*cut)
tot = sum(nums[cut:n-cut])
avg = tot//mom + (tot%mom >= mom/2)

print(avg)
