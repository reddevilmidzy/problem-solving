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
    graph[a][b] = min(graph[a][b], c)


for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][x]+graph[x][j] < graph[i][j]:
                graph[i][j] = graph[i][x]+graph[x][j]
                route[i][j] = []
                for k in range(len(route[i][x])):
                    route[i][j].append(route[i][x][k])
                route[i][j].append(x)
                for l in range(len(route[x][j])):
                    route[i][j].append(route[x][j][l])


for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
#    print(*graph[i][1:])

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(0)
        elif graph[i][j] == INF:
            print(0)
        else:
            print(len(route[i][j])+2, i, *route[i][j], j)
