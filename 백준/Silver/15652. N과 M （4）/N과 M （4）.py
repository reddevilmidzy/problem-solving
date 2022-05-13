n, m = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    else:
        for i in range(1, n+1):
            s.append(i)
            if len(s) > 1:
                if s[-1] < s[-2]:
                    s.pop()
                else:     
                    dfs()
                    s.pop()
            else:
                dfs()
                s.pop()
dfs()