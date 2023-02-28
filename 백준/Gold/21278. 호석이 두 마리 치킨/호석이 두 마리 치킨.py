import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for x in range(1, n+1):
    for i in range(1, n+1):
        graph[i][i] = 0
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][x] + graph[x][j] < graph[i][j]:
                graph[i][j] = graph[i][x] + graph[x][j]

ans = dict()

for x in range(1, n+1):
    for y in range(x+1, n+1):
        dist = [INF]*(n+1)
        dist[0] = 0
        for i in range(1, n+1):
            dist[i] = min(graph[x][i]*2, graph[y][i]*2)
        
        tot = sum(dist)
        if tot not in ans:
            ans[tot] = [x, y]

key = min(ans.keys())

print(*ans[key], key, sep=' ')