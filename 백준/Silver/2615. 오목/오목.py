n = 19
s = [list(map(int,input().split())) for _ in range(n)]

dy = (0,1,1,1, 0,-1,-1,-1)
dx = (1,0,-1,1, -1,0,1,-1)

r,c = 0,0

def is_win(y:int, x:int, d:int) -> bool:
    global r,c
    res = []
    py,px = y+dy[d+4],x+dx[d+4]
    if py < 0 or px < 0 or py >= n or px >= n: pass
    elif s[y][x] == s[py][px]: return False
    cnt = 1
    ny,nx = y,x
    res.append((ny,nx))
    while cnt < 5:
        cnt += 1
        ny += dy[d]
        nx += dx[d]
        res.append((ny,nx))
        if ny < 0 or nx < 0 or ny >= n or nx >= n: return False
        if s[ny][nx] != s[y][x]: return False        

    ny += dy[d]
    nx += dx[d]
    res.sort(key=lambda x:x[-1])
    if ny < 0 or nx < 0 or ny >= n or nx >= n: 
        r,c = res[0]
        return True
    if s[ny][nx] != s[y][x]: 
        r,c = res[0]
        return True
    return False

def solve():
    for i in range(n):
        for j in range(n):
            if s[i][j] and any(is_win(i,j,d) for d in range(4)):
                    print(s[i][j])
                    print(r+1, c+1)
                    return

    print(0)
    return

solve()