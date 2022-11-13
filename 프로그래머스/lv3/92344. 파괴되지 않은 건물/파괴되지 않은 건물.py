def solution(board, skill):
    n = len(board)
    m = len(board[0])
    answer = 0
    graph = [[0]*(m+1) for _ in range(n+1)]

    for s_type, r1, c1, r2, c2, degree in skill:
        if s_type == 1:
            graph[r1][c1] -= degree
            graph[r1][c2+1] += degree
            graph[r2+1][c1] += degree
            graph[r2+1][c2+1] -= degree
        else:
            graph[r1][c1] += degree
            graph[r1][c2+1] -= degree
            graph[r2+1][c1] -= degree
            graph[r2+1][c2+1] += degree
            
    for i in range(n):
        for j in range(m):
            graph[i][j+1] += graph[i][j]
    
    for j in range(m):
        for i in range(n):
            graph[i+1][j] += graph[i][j]
            if graph[i][j] + board[i][j] >= 1:
                answer += 1

    return answer