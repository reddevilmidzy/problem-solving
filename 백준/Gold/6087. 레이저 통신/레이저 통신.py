import sys, heapq
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]
INF = int(1e9)

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= m

def dijkstra(y:int, x:int, r:int, c:int):
    hq = []
    heapq.heappush(hq, (-1, -1, y, x))
    distance = [[[INF]*m for _ in range(n)] for _ in range(2)]
    distance[0][y][x] = 0
    distance[1][y][x] = 0

    while hq:
        cnt,d,y,x = heapq.heappop(hq)
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if out_of_range(ny,nx): continue
            if board[ny][nx] == "*": continue
            if i == d and distance[i%2][ny][nx] > cnt:
                distance[i%2][ny][nx] = cnt
                heapq.heappush(hq, (cnt, d, ny, nx))
            elif i != d and distance[i%2][ny][nx] > cnt + 1:
                distance[i%2][ny][nx] = cnt + 1
                heapq.heappush(hq, (cnt+1, i, ny, nx))
    return min(distance[0][r][c], distance[1][r][c])

m,n = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(n)]
point = []

for y in range(n):
    for x in range(m):
        if board[y][x] == "C":
            point.append(y)
            point.append(x)
print(dijkstra(point[0], point[1], point[2], point[3]))