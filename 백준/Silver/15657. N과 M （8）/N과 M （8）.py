n,m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(*s)
    else:
        for i in arr:
            s.append(i)
            if len(s) > 1:
                if s[-1] >= s[-2]:
                    dfs()
                    s.pop()
                else:
                    s.pop()
            else:
                dfs()
                s.pop()        
dfs()