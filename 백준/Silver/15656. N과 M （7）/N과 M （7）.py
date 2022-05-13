n,m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(*s)
    else:
        for i in arr:
            s.append(i)
            dfs()
            s.pop()     
dfs()