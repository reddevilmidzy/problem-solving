from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def burn():
    while queue:
        x,y,t = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = t + 1
                queue.append([nx,ny,t+1])
    return visited


def bfs(a,b):
    q = deque()
    q.append([a,b,1])
    while q:
        x,y,c = q.popleft()
        if x == h-1 or y == w-1 or x == 0 or y == 0:
            return c

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] != '#':
                if (c+1 < visit[nx][ny] and visit[nx][ny] != -1) or visit[nx][ny] == 0: 
                    q.append([nx,ny,c+1])
                    visit[nx][ny] = -1
    return 'IMPOSSIBLE'


for _ in range(int(input())):
    w,h = map(int,input().split())
    graph = [list(map(str,input().rstrip())) for _ in range(h)]
    queue = deque()
    visited = [[0]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                queue.append([i,j,1])
                visited[i][j] = 1
            elif graph[i][j] == '@':
                sx,sy = i,j
    visit = burn()
    print(bfs(sx,sy))
    