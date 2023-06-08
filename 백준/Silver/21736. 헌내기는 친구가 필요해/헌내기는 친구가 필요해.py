from collections import deque
import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= m

def bfs(r:int, c:int) -> int:
    res = 0
    visited = [[False]*m for _ in range(n)]
    visited[r][c] = True
    queue = deque()
    queue.append((r,c))
    
    while queue:
        y,x = queue.popleft()
        if board[y][x] == "P":
            res += 1

        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if out_of_range(ny,nx): continue
            if not visited[ny][nx] and board[ny][nx] != "X":
                queue.append((ny,nx))
                visited[ny][nx] = True
    
    return res if res else "TT"

def solve():
    for r in range(n):
        for c in range(m):
            if board[r][c] == "I":
                return bfs(r,c)

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

print(solve())