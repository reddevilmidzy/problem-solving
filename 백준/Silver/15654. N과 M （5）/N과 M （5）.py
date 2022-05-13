n,m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(*s)
    else:
        for i in arr:
            if i not in s:
                s.append(i)
                dfs()
                s.pop()
dfs()