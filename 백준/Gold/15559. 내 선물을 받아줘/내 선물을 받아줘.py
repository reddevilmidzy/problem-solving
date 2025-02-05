import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

d = {"N":(-1,0), "W":(0,-1), "E":(0,1), "S":(1,0)}

n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

def find(parent: list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def dfs(y:int, x:int, z:int):

    visited[y][x] = z
    dy, dx = d[graph[y][x]]
    ny, nx = dy + y, dx + x

    if visited[ny][nx] == -1:
        dfs(ny, nx, z)
    

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            dfs(i, j, cnt)
            cnt += 1

edges = []
for y in range(n):
    for x in range(m):

        dy, dx = d[graph[y][x]]
        ny, nx = dy + y, dx + x

        if visited[y][x] != visited[ny][nx]:
            edges.append((visited[y][x], visited[ny][nx]))


parent = [i for i in range(cnt)]
for u,v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)

for x in range(cnt):
    find(parent, x)

print(len(set(parent)))