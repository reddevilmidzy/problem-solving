from collections import deque
import sys, heapq
input = sys.stdin.readline

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def bfs(i:int, j:int, id: int) -> None:
    queue = deque()
    queue.append([i,j])
    visited[i][j] = id

    while queue:
        y, x = queue.popleft()
        land.append((y,x,id))
        for k in range(4):
            ny,nx = dy[k]+y, dx[k]+x

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if not visited[ny][nx] and board[ny][nx]:
                queue.append([ny,nx])
                visited[ny][nx] = id


def dfs(ny: int, nx:int, dirc: int, id:int, cnt: int):
    # 범위 밖
    if ny < 0 or nx < 0 or ny >= n or nx >= m:
        return
    # 물
    # 자기 땅이 아닐때
    if visited[ny][nx] != id:
        # 물
        if not visited[ny][nx]:
            dfs(ny + dy[dirc], nx + dx[dirc], dirc, id, cnt+1)
        
        elif cnt >= 2: # 2 이상이고, 다른 땅
            heapq.heappush(hq, [cnt, id, visited[ny][nx]])
            return
        else:
            return

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list[int], a: int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
hq = []
land = []
id = 1
ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j]:
            bfs(i,j,id)
            id += 1

parent = [i for i in range(id)]
edges = id - 2

# 다리 찾기
for y, x, idx in land:
    for d in range(4):
        dfs(y + dy[d],x + dx[d], d,idx,0)

while hq:
    cost, a, b = heapq.heappop(hq)
    if find(parent, a) != find(parent, b):
        ans += cost
        union(parent, a, b)
        edges -= 1

    if not edges:
        print(ans)
        break
else:
    print(-1)
