import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def dfs(y:int, x:int) -> int:
    if dp[y][x]: return dp[y][x]

    dp[y][x] = 1

    for i in range(4):
        ny,nx = dy[i]+y, dx[i]+x
        if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
        if board[y][x] < board[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny,nx)+1)
    
    return dp[y][x]

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for r in range(n):
    for c in range(n):
        dfs(r,c)

print(max(map(max, dp)))