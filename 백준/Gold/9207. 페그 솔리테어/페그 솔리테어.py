import sys
input = sys.stdin.readline

def dfs(cnt):
    global ans
    if cnt < ans:
        ans = cnt
    if cnt == 1: return
    
    for y in range(n):
        for x in range(m):
            
            if board[y][x] != 'o': continue
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                nny, nnx = ny+dy[i], nx+dx[i]

                if 0<=ny<n and 0<=nx<m and 0<=nny<n and 0<=nnx<m:
                    if board[ny][nx] == 'o' and board[nny][nnx] == '.':
                        board[y][x] = '.'
                        board[ny][nx] = '.'
                        board[nny][nnx] = 'o'
                        dfs(cnt-1)
                        board[nny][nnx] = '.'
                        board[ny][nx] = 'o'
                        board[y][x] = 'o'

t = int(input())
for _ in range(t):
    n,m = 5,9
    board = [list(input().rstrip()) for _ in range(n)]
    input()

    pin = 0
    dy = (1,0,-1,0)
    dx = (0,1,0,-1)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                pin += 1
    ans = pin
    
    dfs(pin)
    print(ans, pin - ans)