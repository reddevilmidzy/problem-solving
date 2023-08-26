import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 16

n = int(input())
parent = [[0]*LOG for _ in range(n+1)]
d = [0] * (n+1)
c = [-1] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dfs(x, depth):
    d[x] = depth
    for y,z in graph[x]:
        if c[y] == -1:
            parent[y][0] = x
            c[y] = c[x] + z
            dfs(y,depth+1)

def set_parent():
    c[1] = 0
    dfs(1, 0)

    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a,b):
    if d[a] > d[b]:
        a,b = b,a
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1<<i):
            b = parent[b][i]

    # lca 가 a임
    # 즉 b가 a의 서브트리
    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

set_parent()
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    par = lca(a,b)
    print(c[a] - c[par] + c[b] - c[par])