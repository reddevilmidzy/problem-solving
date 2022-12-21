import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
route = [[j for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for x in range(1, n+1):
    graph[x][x] = 0
    route[x][x] = "-"
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][x] + graph[x][j] < graph[i][j]:
                graph[i][j] = graph[i][x] + graph[x][j]
                route[i][j] = route[i][x]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(route[i][j], end=' ')
    print()