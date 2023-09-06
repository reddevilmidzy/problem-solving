from collections import deque

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def bfs(r:int, c:int):
    queue = deque()
    queue.append((r,c,0))
    visited = [[False]*m for _ in range(n)]
    visited[r][c] = True
    tmp = [0,0]
    while queue:
        y,x,cnt = queue.popleft()
        if tmp < [cnt, a[y][x]+a[r][c]]:
            tmp = [cnt, a[y][x]+a[r][c]]
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if not visited[ny][nx] and a[ny][nx]:
                queue.append((ny,nx,cnt+1))
                visited[ny][nx] = True
    return tmp
    
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
res = [0,0]

for r in range(n):
    for c in range(m):
        if a[r][c]:
            tmp = bfs(r,c)
            if res < tmp:
                res = tmp
print(res[1])