import sys
input = sys.stdin.readline
INF = int(1e9)

# input()
r,c = map(int,input().split())
n = int(input())
nums = dict()
# (y,x,r,c)
# 왼쪽위, 오른쪽아래
for _ in range(n):
    a,v,h = map(int,input().split())

    if a not in nums:
        nums[a] = (INF,INF,-INF,-INF)
    
    y1,x1,y2,x2 = nums[a]
    
    nums[a] = (min(y1,v),min(x1,h),max(y2,v),max(x2,h))

res = []
for key,val in nums.items():
    y1,x1,y2,x2 = val

    res.append((key,( abs(y1-y2)+1)*(abs(x1-x2)+1)))
res.sort(key=lambda x:(-x[1],x[0]))
print(*res[0])