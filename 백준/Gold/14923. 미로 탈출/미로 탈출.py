from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,-1,0]
dy = [1,0,0,-1]


def bfs(hx, hy, ex, ey):
    queue = deque()
    queue.append([hx,hy,0])
    visited = [[[-1]*m for _ in range(n)] for __ in range(2)]
    visited[0][hy][hx] = 0

    while queue:
        x,y,use = queue.popleft()
        if x == ex and y == ey:
            return visited[use][y][x]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if not board[ny][nx] and visited[use][ny][nx] == -1:
                queue.append([nx, ny, use])
                visited[use][ny][nx] = visited[use][y][x] + 1
            # 보드가 1이고, 아직 부수지 않았고, 방문하지 않았다면

            elif use == 0 and visited[use+1][ny][nx] == -1:
                queue.append([nx,ny, use+1])
                visited[use+1][ny][nx] = visited[use][y][x] + 1

    return -1

n,m = map(int,input().split())
hx,hy = map(int,input().split())
ex,ey = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

print(bfs(hy-1,hx-1,ey-1,ex-1))