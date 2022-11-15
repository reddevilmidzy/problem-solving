import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
v,e = map(int,input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]

ans = INF
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c


for x in range(1, v+1):
    graph[x][x] = 0
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] > graph[i][x] + graph[x][j]:
                graph[i][j] = graph[i][x] + graph[x][j]

for i in range(1, v+1):
    for j in range(1, v+1):
        if i!=j and graph[i][j] != INF and graph[j][i] != INF:
            ans = min(ans, graph[i][j]+graph[j][i])

print(ans if ans != INF else -1)