import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
INF = int(1e9)
routes = []

def bt(s):
    if len(s) == n:
        routes.append(s[::])
        return
    for i in range(n):
        if i not in s:
            s.append(i)
            bt(s)
            s.pop()
    return

bt([0])
res = INF

for route in routes:
    tmp = 0
    for i in range(n-1):
        if graph[route[i]][route[i+1]] != 0:
            tmp += graph[route[i]][route[i+1]]
        else:
            break
    else:
        if graph[route[n-1]][0] != 0:
            res = min(tmp + graph[route[n-1]][0], res)
print(res)