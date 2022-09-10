from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(a,b,c):
    queue = deque()
    queue.append([a,b,c])
    visited[a][b][k] = 1
    while queue:
        x,y,v = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][v]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny>= m:
                continue
            if graph[nx][ny] == 1 and v > 0 and visited[nx][ny][v-1]==0:
                visited[nx][ny][v-1] = visited[x][y][v]+1
                queue.append([nx,ny,v-1])
            if graph[nx][ny] == 0 and visited[nx][ny][v] == 0:
                visited[nx][ny][v] = visited[x][y][v]+1
                queue.append([nx,ny,v])

    return -1

n,m,k = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]    
print(bfs(0,0,k))