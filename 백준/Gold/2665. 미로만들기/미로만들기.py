import sys, heapq
input = sys.stdin.readline

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def bfs():
    q = []
    heapq.heappush(q, [0,0,0])
    visited = [[n*n]*n for _ in range(n)]
    while q:
        cnt, x, y = heapq.heappop(q)
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[ny][nx] and visited[ny][nx] > cnt:
                visited[ny][nx] = cnt
                heapq.heappush(q, [cnt, nx, ny])
            if not board[ny][nx] and visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                heapq.heappush(q, [cnt+1, nx, ny])

    return visited[n-1][n-1]

n = int(input())
board = [list(map(int,input().rstrip())) for _ in range(n)]
print(bfs())