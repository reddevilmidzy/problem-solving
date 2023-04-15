import sys
input = sys.stdin.readline

dy = [0,1,-1,0]
dx = [1,0,0,-1]

def spread(i:int, j:int,a:list[list[int]], res:list[list[int]]) -> None:

    cnt = 0
    for k in range(4):
        ny,nx = dy[k] + i, dx[k] + j
    
        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            continue

        if a[ny][nx] != -1:
            cnt += 1
            # 인접한 방향 확산된 미세먼지 양
            res[ny][nx] += a[i][j]//5

    res[i][j] += a[i][j] - (a[i][j]//5)*cnt

def diffusion(a:list[list[int]], res: list[list[int]]) -> None:
    
    up_row = 0
    down_row = 0
    flag = False
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                spread(i,j,a,res)
            elif a[i][j] == -1 and not flag: # 공기청정기 위치
                res[i][j] = -1
                res[i+1][j] = -1
                flag = True
                up_row = i
                down_row = i+1
    up_clean(up_row, res)
    down_clean(down_row, res)

def up_clean(row:int, res:list[list[int]]) -> None:
    
    res[row][0] = 0
    r_idx = row
    c_idx = 0

    while r_idx > 0:
        res[r_idx][c_idx] = res[r_idx-1][c_idx]
        r_idx -= 1

    while c_idx < c - 1:
        res[r_idx][c_idx] = res[r_idx][c_idx+1]
        c_idx += 1
    
    while r_idx < row:
        res[r_idx][c_idx] = res[r_idx+1][c_idx]
        r_idx += 1
    
    while c_idx > 0:
        res[r_idx][c_idx] = res[r_idx][c_idx-1]
        c_idx -= 1

    res[row][0] = -1
    res[row][1] = 0
    

def down_clean(row:int, res:list[list[int]]) -> None:

    res[row][0] = 0
    r_idx = row
    c_idx = 0

    while r_idx < r - 1:
        res[r_idx][c_idx] = res[r_idx+1][c_idx]
        r_idx += 1

    while c_idx < c - 1:
        res[r_idx][c_idx] = res[r_idx][c_idx+1]
        c_idx += 1

    while r_idx > row:
        res[r_idx][c_idx] = res[r_idx-1][c_idx]
        r_idx -= 1
    
    while c_idx > 0:
        res[r_idx][c_idx] = res[r_idx][c_idx-1]
        c_idx -= 1

    res[row][0] = -1
    res[row][1] = 0
r,c,t = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]

for day in range(t):
    res = [[0]*c for _ in range(r)]
    diffusion(a, res)
    a = res[::]
print(sum(map(sum, a))+2)