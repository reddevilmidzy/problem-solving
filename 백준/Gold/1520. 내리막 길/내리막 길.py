import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

m,n = map(int,input().rstrip().split())
dx = (0,1,-1,0)
dy = (1,0,0,-1)
graph = [list(map(int,input().rstrip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < m and -1 < ny < n:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0,0))