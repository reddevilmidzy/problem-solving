from collections import deque
import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= m

def bfs(r:int, c:int) -> int:
    visited[r][c] = 0
    queue = deque()
    queue.append((r,c,0))
    
    while queue:
        y,x,d = queue.popleft()

        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if out_of_range(ny,nx): continue
            if visited[ny][nx] == -1 and board[ny][nx] == 1:
                queue.append((ny,nx,d+1))
                visited[ny][nx] = d+1

def solve():
    for r in range(n):
        for c in range(m):
            if board[r][c] == 2:
                bfs(r,c)
                return
                
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

solve()

for i in range(n):
    for j in range(m):
        print(visited[i][j] if board[i][j] else 0, end=' ') # board[i][j] 가 0이 아니라면 visited 출력
    print()