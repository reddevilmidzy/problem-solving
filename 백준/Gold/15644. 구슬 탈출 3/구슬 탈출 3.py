from collections import deque
import sys
input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,1,0,-1]
INF = int(1e9)
d = {0:"D", 1:"R", 2:"U", 3:"L"}
def go_ahead(y:int, x:int, i:int, pre_y:int, pre_x:int) -> tuple:
    # # 안만나고, 앞에꺼랑 부딪히지 않을 때까지
    while board[y+dy[i]][x+dx[i]] != "#" and not (y+dy[i] == pre_y and x+dx[i] == pre_x):         
        y,x=y+dy[i],x+dx[i]
        if board[y][x] == "O":
            # 구멍으로 빠짐
            return INF,INF,True
    return y,x,False

def move(y:int,x:int,r:int,c:int,i:int):
    if (i < 2 and (y,x) < (r,c)) or (1 < i and (y,x) > (r,c)):    
        r,c,blue = go_ahead(r,c,i,-1,-1)
        y,x,red = go_ahead(y,x,i,r,c)
    else:
        y,x,red = go_ahead(y,x,i,-1,-1)
        r,c,blue = go_ahead(r,c,i,y,x)
    
    # red 만 잘 빠짐 게임 종료
    if red and not blue:
        return y,x,r,c,True
    elif blue: # 이 방향은 실패, 파랑이 빠짐
        return INF, INF, INF, INF, False
    return y,x,r,c,False

def bfs(y:int,x:int,r:int,c:int):
    queue = deque()
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[y][x][r][c] = True
    queue.append((y,x,r,c,0,""))

    while queue:
        y,x,r,c,cnt,path = queue.popleft()
        if cnt >= 10: continue
        for i in range(4):
            ny,nx,nr,nc,flag = move(y,x,r,c,i)
            if flag: # 성공
                return f"{cnt + 1}\n{path+d[i]}"
            elif ny != INF and  not visited[ny][nx][nr][nc]:
                queue.append((ny,nx,nr,nc,cnt+1, path+d[i]))
                visited[ny][nx][nr][nc] = True
    return -1

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
r_r,r_c,b_r,b_c = -1,-1,-1,-1
oy,ox = -1,-1
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            r_r,r_c = r,c
        elif board[r][c] == "B":
            b_r,b_c = r,c

print(bfs(r_r,r_c,b_r,b_c))