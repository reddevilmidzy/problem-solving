import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
ans = "NO"
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False for i in range(m)] for j in range(n)]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

def bfs(x,y):
    queue= deque()
    visited[y][x] = True
    queue.append([x,y])
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if -1 < nx < m and -1 < ny < n:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append([nx,ny])

for start in range(m):
    if graph[0][start] == 0 and not visited[0][start]:
        bfs(start,0)
for end in range(m):
    if visited[-1][end]:
        ans = "YES"
        break
print(ans)