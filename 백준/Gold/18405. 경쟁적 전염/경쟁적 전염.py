from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    while queue:
        x,y,cnt,lev = queue.popleft()
        if cnt == S:
            return 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == -1:
                queue.append([nx,ny,cnt+1,lev])
                visited[nx][ny] = cnt
                graph[nx][ny] = lev
            elif cnt == visited[nx][ny]:
                queue.append([nx,ny,cnt+1,lev])
                graph[nx][ny] = min(graph[nx][ny], lev)

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
S,X,Y = map(int,input().split())
queue = deque()
tmp = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            tmp.append([graph[i][j],i,j])
tmp.sort(key=lambda x: (x[0]))

for a,b,c in tmp:
    queue.append([b,c,0,a])
    visited[b][c] = 0

bfs()

print(graph[X-1][Y-1])