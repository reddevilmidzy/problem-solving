n,m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
ans = -1

for y in range(n):
    for x in range(m):
        for dy in range(-n, n+1):
            for dx in range(-m, m+1):
                if dy == dx == 0: continue
                ny,nx = y,x
                tmp = 0
                while 0<=ny<n and 0<=nx<m:
                    tmp = tmp*10 + board[ny][nx]
                    ny += dy
                    nx += dx
                    if tmp**0.5 == int(tmp**0.5) and ans < tmp:
                        ans = tmp              
print(ans)