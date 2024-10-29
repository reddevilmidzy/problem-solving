import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = []
for i in range(1, m+1):
    u,v = map(int,input().split())
    nums.append((u, i))
    nums.append((v, i))
nums.sort()

k = n % (2*m)
if not k:
    k = 2*m

print(nums[k-1][1])
