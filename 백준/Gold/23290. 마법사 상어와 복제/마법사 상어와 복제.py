import sys
input = sys.stdin.readline

# 보면 각각의 방향도 dict로 바꾸면 중복 처리 안해도 될듯ㅇㅇ

def set_board():
    res = dict()
    for i in range(n):
        for j in range(n):
            res[(i,j)] = {k:0 for k in range(8)}
    return res

def move():
    global tmp
    tmp = []

    for y in range(n):
        for x in range(n):            
            for z in board[(y,x)]:
                # board[y][x] 에 z 방향을 보고있는 물고기
                if not board[(y,x)][z]: continue
                # 방향 찾기
                for w in range(8):
                    ny,nx = y+d_fish[z][0],x+d_fish[z][1]
                    # 상어위치 아니고, 범위 안에 있고, 물고기 냄새 없으면
                    if (ny,nx)!=(r,c) and (0<=ny<n and 0<=nx<n) and smell[ny][nx] == 0:
                        copy_board[(ny,nx)][z] += board[(y,x)][(z+w)%8]
                        tmp.append((ny,nx,z, "pre",y,x)) # ny,nx 에 board[(y,x)[z]] 마리 추가
                        break
                    z = (z-1)%8
                else: # 움직이지 못함
                    copy_board[(y,x)][z] += board[(y,x)][z]
    # print(tmp)
    # tmp 가 이번 이동에서 이동한 물고기 행적
    #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 

def move_sh(r:int,c:int):
    res = []
    for moving in way:
        y,x = r,c
        cnt = 0
        pre = set() # 이게 좀 비효율적..?
        for i in moving:
            y,x = d_shark[i][0]+y, d_shark[i][1]+x
            if y < 0 or y >= n or x < 0 or x >= n: break # 이 루트로 이동 불가
            if (y,x) not in pre:
                cnt += sum(copy_board[(y,x)].values())
            pre.add((y,x))
        else:
            res.append((cnt, moving))
    res.sort(key=lambda x:(-x[0], x[1]))

    y,x = r,c
    # 상좌하우

    for i in res[0][1]:
        y,x = d_shark[i][0]+y, d_shark[i][1]+x

        if sum(copy_board[(y,x)].values()):
            copy_board[(y,x)] = {j:0 for j in range(8)}
            smell[y][x] = 3
    return y,x


def bt(s:list[int]) -> None:
    if len(s) == 3:
        global way
        way.append(s[:])
        return
    for i in range(4):
        s.append(i)
        bt(s)
        s.pop()

# 전처리

n = 4
board = set_board()
copy_board = set_board()
d_fish = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
d_shark = [(-1,0), (0,-1), (1,0), (0,1)]
way = []
smell = [[0]*n for _ in range(n)]

m,s = map(int,input().split())
for _ in range(m):
    y,x,z = map(int,input().split())
    board[(y-1,x-1)][z-1] += 1

r,c = map(int,input().split())
r-=1
c-=1

bt([])

while s:
    tmp = []
    # 물고기 이동
    move()
    # 상어 이동
    r,c = move_sh(r,c)

    for i in range(n):
        for j in range(n):
            # 냄새 없애기
            if smell[i][j]:
                smell[i][j] -= 1
            for k in range(8):
                board[(i,j)][k] += copy_board[(i,j)][k]

    copy_board = set_board()
    s -= 1

print(sum([sum(board[(i,j)].values()) for i in range(n) for j in range(n)]))