import sys
input = sys.stdin.readline

n,q = map(int,input().split())
nums = sorted(list(map(int,input().split())))

pre_fix = [0,nums[0]]

for i in range(2,n+1):
    pre_fix.append(pre_fix[i-1]+nums[i-1])
for _ in range(q):
    l,r = map(int,input().split())
    print(pre_fix[r]-pre_fix[l-1])