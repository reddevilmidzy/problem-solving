import sys
input=sys.stdin.readline

def solve(k):
    res=tot
    for num in nums:
        if num<k:
            res+=q
        elif k+r < num:
            res-=p
    #break 집어넣기
    return res >= s

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
tot=sum(nums)
p,q,r,s=map(int,input().split())

res=-1
st=1
ed=int(1e12)

while st<=ed:
    mid=(st+ed)//2
    if solve(mid):
        res=mid
        ed=mid-1
    else:
        st=mid+1
print(res)