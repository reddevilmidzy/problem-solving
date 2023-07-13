import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
res = set()
def back(s):
    if len(s)==m:
        res.add(' '.join(map(str,s)))
        return
    
    for i in range(n):
        s.append(nums[i])
        back(s)
        s.pop()

back([])
ans =[]
for i in sorted(res):
    ans.append(list(map(int,i.split())))

for i in sorted(ans):
    print(*i)