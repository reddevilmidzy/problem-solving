from collections import defaultdict
import sys
input = sys.stdin.readline

def twopoint(n,nums,target):
    st = 0
    en = n-1
    ans = defaultdict(int)
    while st<en:
        tsum = nums[st]+nums[en]
        if tsum>target:
            en-=1
            ans[abs(target-tsum)]+=1
        elif tsum<target:
            st+=1
            ans[abs(target-tsum)]+=1
        else:
            ans[abs(target-tsum)]+=1
            st+=1
            en-=1

    
    for i in sorted(ans.keys()):
        return ans[i]

t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    nums = sorted(list(map(int,input().split())))
    print(twopoint(n,nums,k))