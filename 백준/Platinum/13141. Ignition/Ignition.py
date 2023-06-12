from sys import stdin

input = stdin.readline
INF = 1e9

n,m = map(int,input().split())
adj = [[INF]*(n+1) for _ in range(n+1)]
edges = []

def floyd():
    for x in range(1, n+1):
        adj[x][x] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if adj[i][j] > adj[i][x] + adj[x][j]:
                    adj[i][j] = adj[i][x] + adj[x][j]


for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((u,v,w))
    if adj[u][v] > w:
        adj[u][v] = w
        adj[v][u] = w
floyd()

ans = INF
for x in range(1, n+1):
    cur = 0
    for u,v,w in edges:
        tmp = (w+adj[x][u]+adj[x][v])/2
        if tmp > cur:
            cur = tmp
    if cur < ans:
        ans = cur
    
print(ans)