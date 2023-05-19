from collections import deque
import sys
input = sys.stdin.readline

dy = (1,0,0,-1)
dx = (0,1,-1,0)

def bfs(i:int, j: int) -> None:
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    tot = 0
    route = []

    while queue:
        y,x = queue.popleft()
        tot += a[y][x]
        route.append((y,x))

        for k in range(4):
            ny,nx = dy[k]+y, dx[k]+x

            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue

            if not visited[ny][nx] and l <= abs(a[y][x] - a[ny][nx]) <= r:
                queue.append((ny,nx))
                visited[ny][nx] = True

    if len(route) > 1:
        change = tot//len(route)
        for y,x in route:
            a[y][x] = change
        global move
        move = True    

n,l,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)

    if not move:
        break

    ans += 1
print(ans)