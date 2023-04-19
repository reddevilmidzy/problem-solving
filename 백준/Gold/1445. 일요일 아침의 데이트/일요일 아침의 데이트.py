import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def is_there_trash(y:int,x:int) -> int:
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if board[ny][nx] == 'g':
            return 1
    return 0

def in_trash(y:int, x:int) -> int:
    return 1 if board[y][x] == 'g' else 0

def dijkstra(st_y:int, st_x:int):
    ed_y,ed_x = -1,-1

    distance = [[[INF, INF]]*m for _ in range(n)]
    near_trash = is_there_trash(st_y, st_x)
    distance[st_y][st_x] = [0, 0]

    hq = []
    heapq.heappush(hq, [0, 0, st_y,st_x])

    while hq:
        cnt, near, y, x  = heapq.heappop(hq)
        if board[y][x] == 'F':
            ed_y,ed_x = y,x

        if [cnt, near] > distance[y][x]:
            continue
        
        for i in range(4):
            ny,nx = dy[i] + y, dx[i] + x

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 'F':
                if distance[ny][nx] > [distance[y][x][0], distance[y][x][1]]:
                    distance[ny][nx] = [distance[y][x][0], distance[y][x][1]]
                    heapq.heappush(hq, [distance[y][x][0], distance[y][x][1], ny, nx])
                continue

            if in_trash(ny,nx):
                if distance[ny][nx] > [distance[y][x][0] + in_trash(ny,nx), distance[y][x][1]]:
                    distance[ny][nx] = [distance[y][x][0] +  in_trash(ny,nx), distance[y][x][1]]
                    heapq.heappush(hq, [distance[y][x][0] + in_trash(ny,nx), distance[y][x][1], ny, nx])
            else:
                if distance[ny][nx] > [distance[y][x][0] + in_trash(ny,nx), distance[y][x][1]+is_there_trash(ny,nx)]:
                    distance[ny][nx] = [distance[y][x][0] +  in_trash(ny,nx), distance[y][x][1]+is_there_trash(ny,nx)]
                    heapq.heappush(hq, [distance[y][x][0] + in_trash(ny,nx), distance[y][x][1]+is_there_trash(ny,nx), ny, nx])

    return distance[ed_y][ed_x]
n,m = map(int,input().split())

board = [list(map(str,input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            print(*dijkstra(i,j))
            break