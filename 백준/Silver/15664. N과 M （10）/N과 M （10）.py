import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nums = sorted(list(map(int,input().rstrip().split())))
res = []
ans = []
def dfs():
    if len(ans)==m:
        tmp = []
        for i in sorted(ans):
            tmp.append(nums[i])
        if tmp not in res:
            res.append(tmp)
    for idx in range(n):
        if idx not in ans:
            ans.append(idx)
            dfs()
            ans.pop()
dfs()

for i in sorted(res):
    print(*i)