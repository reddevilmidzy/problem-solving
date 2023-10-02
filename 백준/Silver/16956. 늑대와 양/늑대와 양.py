import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def solve():
    for y in range(n):
        for x in range(m):
            if board[y][x] == "W":
                for i in range(4):
                    ny,nx = y+dy[i],x+dx[i]
                    if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                    if board[ny][nx] == "S":
                        return False
                    if board[ny][nx] == ".":
                        board[ny][nx] = "D"
    
    return True

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

if solve():
    print(1)
    for i in range(n):
        print("".join(board[i]))
else:
    print(0)