from itertools import combinations
from collections import deque
import sys, copy
input = sys.stdin.readline

dx = (0,1,-1,0)
dy = (1,0,0,-1)

def bfs(virus:deque) -> int:
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    res = 0
    for r,c in virus:
        res += 1
        queue.append((r,c))
        visited[r][c] = True

    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            ny,nx = dy[i] + y, dx[i] + x

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 0 and not visited[ny][nx]:
                res += 1
                visited[ny][nx] = True
                queue.append((ny,nx))

    return n*m - res - cnt - 3

def build_wall(w: tuple):
    for r,c in w:
        board[r][c] = 1

def break_wall(w: tuple):
    for r,c in w:
        board[r][c] = 0

# 0:빈칸, 1: 벽, 2: 바이러스
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
virus = deque()
wall = []
cnt = 0
ans = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0: # 벽을 세울 수 있음
            wall.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))
        else:
            cnt += 1
for w in combinations(wall, 3):
    build_wall(w)
    ans.append(bfs(virus))
    break_wall(w)
    
print(max(ans))