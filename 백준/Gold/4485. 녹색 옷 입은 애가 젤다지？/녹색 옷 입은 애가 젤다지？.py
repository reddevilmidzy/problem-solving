import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [0,1,-1,0]
dy = [1,0,0,-1]
prbm = 1
def dijkstra(a,b):
    q = []
    heapq.heappush(q, [graph[a][b], a,b])
    distance[a][b] = graph[a][b]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, [cost, nx,ny])
    return distance[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF]*(n) for _ in range(n)]
    print(f'Problem {prbm}: {dijkstra(0,0)}')
    prbm += 1