import sys
input = sys.stdin.readline

def pos():
    global board, boxs, goal

    y,x = -1,-1
    for i in range(n):
        for j in range(m):
            if board[i][j] == "w":
                board[i][j] = "."
                y,x = i,j
            elif board[i][j] == "W":
                board[i][j] = "+"
                goal.add((i,j))
                y,x = i,j
            elif board[i][j] == "b":
                board[i][j] = "."
                boxs.add((i,j))
            elif board[i][j] == "B":
                board[i][j] = "+"
                goal.add((i,j))
                boxs.add((i,j))
            elif board[i][j] == "+":
                goal.add((i,j))


    return y,x    

# d = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
dy = {"U":-1, "D":1, "R":0, "L":0}
dx = {"U":0, "D":0, "R":1, "L":-1}
idx = 0

while True:
    n,m = map(int,input().split())
    if not n: break    
    idx += 1
    board = [list(input().rstrip()) for _ in range(n)]
    cmds = list(input().rstrip())
    boxs = set()
    goal = set()
    y,x = pos()
    flag = "incomplete"

    for i in cmds:
        if not (boxs - goal): 
            flag = "complete"
            break

        ny,nx = y+dy[i], x+dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m : continue

        if (ny,nx) in boxs:
            bny,bnx = ny+dy[i],nx+dx[i]
            
            if bny < 0 or bnx < 0 or bny >= n or bnx >= m: continue
            if (bny,bnx) in boxs or board[bny][bnx] == "#": continue

            boxs.remove((ny,nx))
            boxs.add((bny,bnx))
            y,x = ny,nx

        elif board[ny][nx] == "." or board[ny][nx] == "+":
            y,x = ny,nx
        elif board[ny][nx] == "#": continue
        
    if not (boxs - goal): 
        flag = "complete"
    
    for r,c in goal:
        board[r][c] = "+"
    
    for r,c in boxs:
        if board[r][c] == "+":
            board[r][c] = "B"
        else:
            board[r][c] = "b"
    
    if board[y][x] == "+":
        board[y][x] = "W"
    else:
        board[y][x] = "w"


    print(f"Game {idx}: {flag}")

    for res in board:
        print("".join(res))
