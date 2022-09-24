# 위상정렬로도 풀어보기
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split()) 
    graph[a][b] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for x in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][x]+graph[x][j]:
                graph[i][j] = graph[i][x]+graph[x][j]

ans = 0         
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF and graph[j][i]==INF:
            break
    else:
        ans += 1
print(ans)