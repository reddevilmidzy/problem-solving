import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nums = sorted(list(map(int,input().rstrip().split())))
res = []
ans = []
def dfs():
    if len(ans)==m:
        pri = ''
        for i in ans:
            pri += str(nums[i])
            pri += ' '
        if pri not in res:
            print(pri)
            res.append(pri)
    for idx in range(n):
        if idx not in ans:
            ans.append(idx)
            dfs()
            ans.pop()
dfs()