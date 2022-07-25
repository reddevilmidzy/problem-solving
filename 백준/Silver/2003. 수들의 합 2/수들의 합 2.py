import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nums=list(map(int,input().rstrip().split()))
ans=0
i,j=0,0
while i<n and j<n:
    if sum(nums[i:j+1])==m:
        ans+=1
        i+=1
    elif sum(nums[i:j+1])<m:
        j+=1
    else:
        i+=1
print(ans)