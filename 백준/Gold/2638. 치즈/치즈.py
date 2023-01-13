from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 외부 탐색
def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    outside[a][b] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not graph[nx][ny] and not outside[nx][ny]:
                queue.append([nx, ny])
                outside[nx][ny] = True


def melt():
    while queue_to_melt:
        x,y = queue_to_melt.popleft()
        four = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue_to_melt.append([nx,ny])
                visited[nx][ny] = True
            if outside[nx][ny]:
                four += 1
        
        if four >= 2:
            tmp[x][y] = 1
            graph[x][y] = 0

def will_melt(x,y):
    four = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        four += 1
    return four >= 2

ans = 0
while True:   
    outside = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    tmp = [[0]*m for _ in range(n)]
    melted = 0
    queue_to_melt = deque()
    a,b = 0,0
    flag = False

    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                bfs(i,j)
                break

    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                melted += 1
            elif will_melt(i,j):
                visited[i][j] = True
                queue_to_melt.append([i,j])

    if melted == n*m:
        break
    melt()
    ans += 1

print(ans)