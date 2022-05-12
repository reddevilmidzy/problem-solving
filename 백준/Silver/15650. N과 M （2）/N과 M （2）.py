n, m = list(map(int, input().split()))
s = []
res = []
def dfs():
    if len(s) == m:
        if sorted(s) not in res:
            print(' '.join(map(str, s)))
            res.append(sorted(s))
            return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()