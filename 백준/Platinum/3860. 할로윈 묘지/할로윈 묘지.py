import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = int(1e9)

def walk(y:int,x:int) -> None:
    res = []
    for i in range(4):
        ny,nx = dy[i] + y, dx[i] + x

        # 범위 밖
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue

        if board[ny][nx] != -1: # 무덤이 아니라면
            res.append((ny,nx,1))
    graph[(y,x)] = res

def loop(y:int, x:int) -> None:
    graph[(y,x)] = [(hole[(y,x)])]

def jump(y:int, x:int) -> None:
    if (y,x) in hole: # 묘비 입구라면
        graph[(y,x)] = [(hole[(y,x)])]
        return
    
    res = []
    for i in range(4):
        ny,nx = dy[i] + y, dx[i] + x

        # 범위 밖
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue

        if board[ny][nx] != -1: # 무덤이 아니라면
            res.append((ny,nx,1))
    graph[(y,x)] = res
    
def bellman(cur_y, cur_x):
    dist = [[INF]*w for _ in range(h)]
    dist[cur_y][cur_x] = 0

    for _ in range(h*w - 1):
        for i in range(h):
            for j in range(w):
                if dist[i][j] == INF or board[i][j] == -1:
                    continue
                for ny, nx, cost in graph[(i,j)]:
                    if dist[ny][nx] > dist[i][j] + cost:
                        dist[ny][nx] = dist[i][j] + cost

    for i in range(h):
        for j in range(w):
            if dist[i][j] == INF or board[i][j] == -1:
                continue
            for ny,nx,cost in graph[(i,j)]:
                if dist[ny][nx] > dist[i][j] + cost:
                    return "Never"
    
    return dist[h-1][w-1] if dist[h-1][w-1] != INF else "Impossible"

while True:
    # 너비, 높이
    w,h = map(int,input().split())
    if w == 0:
        break
    # 0: 잔디, -1: 묘비, 2 : 구멍
    board = [[0]*w for _ in range(h)]
    graph = dict()
    # 묘비 위치
    g = int(input())
    for _ in range(g):
        x,y = map(int,input().split())
        board[y][x] = -1 # 묘비

    e = int(input())
    hole = dict()
    for i in range(e):
        x1,y1,x2,y2,t = map(int,input().split())
        if x1 == x2 and y1 == y2: # 둘이 같다면
            board[y1][x1] = 1 # 무한 뤂 도는건 1
            hole[(y2,x2)] = (y1,x1,t)
            continue
        board[y1][x1] = 2
        board[y2][x2] = 2
        hole[(y1,x1)] = (y2,x2,t)

    for i in range(h):
        for j in range(w):
            if i == h-1 and j == w-1:
                continue
            if board[i][j] == 0: # 잔디
                walk(i,j)
            elif board[i][j] == 1: # 귀신 구멍인데, 자기 위치
                loop(i,j)
            elif board[i][j] != -1: # 묘비가 아니라면, => 귀신 구멍
                jump(i,j)
    graph[(h-1, w-1)] = []
    print(bellman(0,0))