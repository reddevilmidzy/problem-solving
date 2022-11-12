import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int,input().split())))

#res = int(1e9)*3
res = []
ans = int(1e9)*3

for i in range(n-2):
    l,r = i+1, n-1
    while l<r:
        s = nums[i]+nums[l]+nums[r]
        if abs(s)<ans:
            res = [nums[i],nums[l],nums[r]]
            ans = abs(s)
        if s>0:
            r-=1
        elif s<0:
            l+=1
        else:
            print(nums[i],nums[l],nums[r])
            exit()
print(*res)