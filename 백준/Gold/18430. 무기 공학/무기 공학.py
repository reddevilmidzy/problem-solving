import sys
input = sys.stdin.readline

dy = (1,-1,-1,1)
dx = (-1,-1,1,1)

def bt(y:int, x:int, tot:int, visited:list[list[bool]]) -> None:
    global ans
    if ans < tot:
        ans = tot
    
    if y>=n and x>=m: return

    for k in range(4):
        for i in range(max(0, y-1), n):
            for j in range(max(0, x-1), m):
                ly, lx = dy[k]+i, j
                ry, rx = i, dx[k]+j
                if ly < 0 or rx < 0 or ly >= n or rx >= m: continue
                if not visited[i][j] and not visited[ly][lx] and not visited[ry][rx]:
                    visited[ly][lx] = True
                    visited[ry][rx] = True
                    visited[i][j] = True
                    bt(i,j,tot+board[i][j]*2+board[ly][lx]+board[ry][rx],visited)
                    visited[ly][lx] = False
                    visited[ry][rx] = False
                    visited[i][j] = False

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0
visited = [[False]*m for _ in range(n)]
bt(0,0,0,visited)
print(ans)