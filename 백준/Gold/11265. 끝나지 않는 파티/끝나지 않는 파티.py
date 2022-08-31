import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 플로이드 워셜 알고리즘 사용하여 모든 경로에 대하여 최단경로 구함
for x in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                graph[i][j] = min(graph[i][x]+graph[x][j], graph[i][j])

for j in range(m):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] <= c: # 가는 최단경로가 c보다 작다면 
        print('Enjoy other party')
    else:
        print('Stay here')