from collections import deque
import sys
input = sys.stdin.readline
dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

# @진원지, .일반도로, *내진설계안됨, #내진설계됨, |방파제
n,m = map(int,input().split())
board = [input().rstrip() for _ in range(n)]
queue = deque()
build = [[0]*m for _ in range(n)]

tmp = 0
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "@":
            visited[i][j] = True
            queue.append((i,j))
        elif board[i][j] == "*":
            tmp += 1
            build[i][j] = 1
        elif board[i][j] == "#":
            tmp += 1
            build[i][j] = 2
tot = tmp
while queue:
    y,x = queue.popleft()

    for i in range(4):
        for k in range(1, 2 + (board[y][x] == "@")):
            ny,nx = k*dy[i]+y, k*dx[i]+x
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if board[ny][nx] == "|": break

            if build[ny][nx] > 0:
                build[ny][nx] -= 1
                if not build[ny][nx]:
                    tmp -= 1
                    queue.append((ny,nx))

print(tot - tmp, tmp)