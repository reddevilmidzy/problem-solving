import sys
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][x] + graph[x][j]:
                graph[i][j] = graph[i][x] + graph[x][j]

s = int(input())
for _ in range(s):
    a, b = map(int,input().split())
    if graph[a][b] == graph[b][a]:
        print(0)
    elif graph[a][b] > graph[b][a]:
        print(1)
    elif graph[a][b] < graph[b][a]:
        print(-1)