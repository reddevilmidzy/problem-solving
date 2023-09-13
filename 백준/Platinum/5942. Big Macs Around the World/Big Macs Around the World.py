import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman(st:int, ed:int, val:int):
    dist = [INF for _ in range(n+1)]
    dist[st] = val

    for _ in range(n-1):
        for u,v,w in graph:
            if dist[u] != INF and dist[u] * w < dist[v]:
                dist[v] = dist[u] * w

    for u,v,w in graph:
        if dist[u] * w < dist[v]:
            return 0
    return dist[ed]

n,m,val,st,ed = input().rstrip().split()
n = int(n)
m = int(m)
val = float(val)
st = int(st)
ed = int(ed)
graph = []
for _ in range(m):
    u,v,w = map(float,input().split())
    graph.append((int(u),int(v),w))

print(bellman(st,ed,val))
