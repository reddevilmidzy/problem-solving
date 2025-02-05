import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dy = (0, 1, -1, 0)
dx = (1, 0, 0, -1)

visited = [[False]*m for _ in range(n)]
def bfs(r:int, c:int) -> int:
    queue = deque()
    visited[r][c] = True
    queue.append((r,c))

    tot = 0
    while queue:
        y,x = queue.popleft()
        if graph[y][x] == ".":
            tot += 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            
            if not visited[ny][nx] and not graph[ny][nx].isalpha():
                queue.append((ny,nx))
                visited[ny][nx] = True
        
    return tot



cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != "X" and graph[i][j].isalnum():
            tmp = bfs(i,j)
            if tmp:
                cnt += 1

left = 0 
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == ".":
            left += 1

print(cnt, left)        