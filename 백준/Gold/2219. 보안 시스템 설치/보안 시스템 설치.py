import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
ans = [0]*(n+1)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)
    graph[b][a] = min(graph[b][a], c)

for i in range(1,n+1):
    graph[i][i] = 0

for x in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][x]+graph[x][j] < graph[i][j]:
                graph[i][j] = graph[i][x] + graph[x][j]

res = [INF,0]
for i in range(1,n+1):
    if res[0] > sum(graph[i][1:]):
        res[0] = sum(graph[i][1:])
        res[1] = i
print(res[1])