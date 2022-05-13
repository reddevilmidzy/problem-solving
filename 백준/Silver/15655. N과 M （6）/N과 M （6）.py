n,m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
s = []
res = []
def dfs():
    #print(res,s)
    if len(res) == m and sorted(res) not in s:
        print(*res)
        s.append(sorted(res))
    else:
        for i in arr:
            if i not in res:
                res.append(i)
                dfs()
                res.pop()
dfs()