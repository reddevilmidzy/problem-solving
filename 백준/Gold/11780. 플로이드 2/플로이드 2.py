import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

graph =[[INF]*(n+1) for _ in range(n+1)]
route = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c


for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][x]+graph[x][j] < graph[i][j]:
                graph[i][j] = graph[i][x]+graph[x][j]
                
                route[i][j] = route[i][x][:] + [x] + route[x][j][:]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(0)
        elif graph[i][j] == INF:
            print(0)
        else:
            print(len(route[i][j])+2, i, *route[i][j], j)
