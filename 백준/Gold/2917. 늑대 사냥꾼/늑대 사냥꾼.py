import sys, heapq
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
dx = [0,1,-1,0]
dy = [1,0,0,-1]

# + 까지 거리 탐색 bfs
def dist_hut(queue: deque) -> None:
    while queue:
        cnt, y, x = queue.popleft()
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if dist[ny][nx] == INF or dist[ny][nx] < cnt - 1:
                dist[ny][nx] = cnt - 1
                queue.append((cnt - 1, ny, nx))

def dijkstra(st_y:int, st_x:int):
    distance = [[INF]* m for _ in range(n)]
    distance[st_y][st_x] = dist[st_y][st_x]
    hq = []
    heapq.heappush(hq, [dist[st_y][st_x], st_y,st_x]) # 자기가 위치한 곳에서도 오두막 세야하나
    while hq:
        cnt,y,x = heapq.heappop(hq)
        if distance[y][x] < cnt:
            continue
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue

            if distance[ny][nx] > max(dist[ny][nx], cnt):
                distance[ny][nx] = max(dist[ny][nx], cnt)
                heapq.heappush(hq, [distance[ny][nx], ny, nx])

    return -distance[r][c]

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
r,c = -1,-1
st_y, st_x = -1,-1
dist = [[INF]*m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == "+":
            dist[i][j] = 0
            queue.append((0,i,j))
        elif board[i][j] == "V":
            st_y,st_x = i,j
        elif board[i][j] == "J":
            r,c = i,j

dist_hut(queue)

print(dijkstra(st_y,st_x))