from collections import deque
import sys
input = sys.stdin.readline

dy = (1,0,-1,0,1,1,-1,-1)
dx = (0,-1,0,1,1,-1,1,-1)

def bfs(r:int, c:int, height:int) -> int:
    queue = deque()
    queue.append((r,c))
    visited[r][c] = True
    res = True
    while queue:
        y,x = queue.popleft()
        for i in range(8):
            ny,nx = dy[i]+y, dx[i]+x
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if board[ny][nx] > height: # 봉우리가 아님
                res = False
            if not visited[ny][nx] and board[ny][nx] == height:
                queue.append((ny,nx))
                visited[ny][nx] = True
    return res

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = 0

for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            ans += bfs(r,c,board[r][c])

print(ans)