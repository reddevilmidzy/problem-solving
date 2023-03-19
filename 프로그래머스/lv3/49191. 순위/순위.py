INF = int(1e9)
def solution(n, results):    
    graph = [[INF]*(n+1) for _ in range(n+1)]

    
    for a, b in results: 
        graph[a][b] = 1

    for x in range(1,n+1):
        graph[x][x] = 0
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

    return ans