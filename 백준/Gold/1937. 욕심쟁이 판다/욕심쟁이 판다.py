def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]>board[x][y]:
                    dp[x][y] = max(dfs(nx,ny) + 1, dp[x][y])
        return dp[x][y]

N = int(input())
dx = (-1,1,0,0)
dy = (0,0,-1,1)
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if dp[x][y] == -1:
            dfs(x,y)

print(max(map(max,dp)))