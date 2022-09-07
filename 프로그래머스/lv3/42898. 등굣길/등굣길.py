def solution(m, n, puddles):
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    water = [[True]*(m+1) for _ in range(n+1)]
    for x,y in puddles:
        water[y][x] = False
        
    for i in range(1,n+1):
        for j in range(1, m+1):
            if water[i-1][j] and water[i][j-1] and water[i][j]:
                graph[i][j] += (graph[i-1][j] + graph[i][j-1])%1000000007
            elif not water[i][j]:
                pass
            elif not water[i-1][j]:
                graph[i][j] += graph[i][j-1]%1000000007
            elif not water[i][j-1]:
                graph[i][j] += graph[i-1][j]%1000000007

    return graph[n][m]%1000000007