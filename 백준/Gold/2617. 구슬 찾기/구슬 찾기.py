import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
board = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    board[b][a] = 1
for x in range(1, n+1):
    board[x][x] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] > board[i][x] + board[x][j]:
                board[i][j] = board[i][x] + board[x][j]
ans = 0
mid = (n+1)//2

for x in range(1, n+1):
    up = len([i for i in board[x] if i != INF and i != 0])
    down = len([board[i][x] for i in range(1, n+1) if board[i][x] != INF and board[i][x] != 0])
    if up >= mid or mid <= down:
        ans += 1

print(ans)