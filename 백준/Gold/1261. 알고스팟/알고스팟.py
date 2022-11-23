import sys, heapq
input = sys.stdin.readline

m, n = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

dx = [0,1,-1,0]
dy = [1,0,0,-1]
INF = int(1e9)
distance = [[INF]*(m) for _ in range(n)]



def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0)) # cost, x, y
    distance[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if x == n-1 and y == m-1:
            print(dist)
            return
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or ny >= m or nx >= n:
                continue
            if dist+graph[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(q, (dist+graph[nx][ny], nx, ny))

dijkstra()