from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

board = [list(input().rstrip()) for _ in range(n)]

d = ((0,-1), (0,1), (1,0), (-1,0))

bomb = [[float('inf')] * m for _ in range(n)]
bomb[0][0] = 0

queue = deque([(0,0,0)]) # cnt, y, x, board

# 개쩌는 아이디어였다...
# 8d
while queue:
    cnt, y, x = queue.popleft()
    if y==n-1 and x==m-1:
        break
    if bomb[y][x] < cnt: continue

    for dy,dx in d:
        ny,nx = y + dy, x + dx

        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if board[ny][nx] == '.' and bomb[y][x] < bomb[ny][nx]:
            bomb[ny][nx] = bomb[y][x]
            queue.appendleft((bomb[ny][nx], ny, nx))
    
    for ddy,ddx in ((0,k), (0,-k), (-k,0), (k,0)):
        for i in range(-k+1, k):
            ny = y + ddy + (i if ddy == 0 else 0) 
            nx = x + ddx + (i if ddx == 0 else 0)

            if ny < 0 or nx < 0 or ny >= n or nx >=m: 
                ny = max(0, ny)
                nx = max(0, nx)
                ny = min(ny, n - 1)
                nx = min(nx, m - 1)

            if bomb[y][x] + 1 < bomb[ny][nx]:
                bomb[ny][nx] = bomb[y][x] + 1
                queue.append((bomb[ny][nx], ny, nx))

print(bomb[n-1][m-1])

