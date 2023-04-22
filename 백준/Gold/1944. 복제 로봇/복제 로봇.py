from collections import deque
import sys, heapq
input = sys.stdin.readline

dy = [0,1,-1,0]
dx = [1,0,0,-1]

def bfs(idx:int, r:int, c:int):
    queue = deque()
    queue.append((r, c, 0))

    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True

    while queue:
        y,x,cnt = queue.popleft()
        if (board[y][x] == "S" or board[y][x] == "K") and keys[(y,x)] != idx:
            heapq.heappush(hq, (cnt, idx, keys[(y,x)])) # idx에서 y,x 까지 걸리는거리 cnt
        
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] != "1" and not visited[ny][nx]:
                queue.append((ny,nx,cnt+1))
                visited[ny][nx] = True

def find(parent:list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(n)]
keys = dict()
idx = 1
hq = []
candy = []
parent = [i for i in range(m+2)]
ans = 0
edges = m
for i in range(n):
    for j in range(n):
        if board[i][j] == "S" or board[i][j] == "K":
            keys[(i,j)] = idx
            candy.append((idx,i,j))
            idx += 1

for idx, r, c in candy:
    bfs(idx, r, c)

while hq:
    cost, a, b = heapq.heappop(hq)

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += cost
        edges -= 1
    
        if not edges:
            print(ans)
            break
else:
    print(-1)