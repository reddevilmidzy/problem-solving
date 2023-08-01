def dfs(y, x):
    if dp[y][x] != -1: return dp[y][x]
    else:
        dp[y][x] = 1
        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<n and 0<=nx<n:
                if board[y][x] < board[ny][nx]:
                    dp[y][x] = max(dp[y][x], dfs(ny,nx)+1)    
        return dp[y][x]

dy = (-1,1,0,0)
dx = (0,0,-1,1)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if dp[y][x] == -1:
            dfs(y,x)

print(max(map(max, dp)))