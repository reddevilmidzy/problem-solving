import sys
from collections import deque
input =sys.stdin.readline

n,m,h = map(int, input().rstrip().split())
graph = [[list(map(int,input().rstrip().split())) for i in range(m)] for j in range(h)]

queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
# print(graph)
for i in range(h):
    for j in range(m):
        for o in range(n):
            if graph[i][j][o] == 1:
                queue.append([i,j,o])

def bfs():
    while queue:
        z,x,y = queue.popleft()
        #print(x,y)
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            #print(nx,ny,z)
            if -1 < nx < m and -1 < ny < n and -1 < nz < h:
                if graph[nz][nx][ny] == 0:
                    queue.append([nz,nx,ny])
                    graph[nz][nx][ny] = graph[z][x][y] + 1

bfs()
ans = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 0:
                ans = -1
                print(ans)
                exit()
        ans = max(ans, max(graph[i][j]))
print(ans-1)