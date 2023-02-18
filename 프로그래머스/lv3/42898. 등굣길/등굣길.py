def solution(m, n, puddles):
    DIV = 1000000007
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    water = [[False]*(m+1) for _ in range(n+1)]
    for x,y in puddles:
        water[y][x] = True
        
    for i in range(1,n+1):
        for j in range(1, m+1):
            if not water[i-1][j] and not water[i][j-1] and not water[i][j]:
                graph[i][j] += (graph[i-1][j] + graph[i][j-1])%DIV
            elif water[i][j]:
                pass
            elif water[i-1][j]:
                graph[i][j] += graph[i][j-1]%DIV
            elif water[i][j-1]:
                graph[i][j] += graph[i-1][j]%DIV

    return graph[n][m]%DIV