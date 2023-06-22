from sys import stdin
input = stdin.readline

d = [(1,0), (0,1), (-1,0), (0,-1)]
r,c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]
ans = [["."]*c for _ in range(r)]

for y in range(r):
    for x in range(c):
        if board[y][x] == "X":
            cnt = 0
            for dy,dx in d:
                ny,nx = dy+y,dx+x
                if ny < 0 or nx < 0 or ny >= r or nx >= c:
                    cnt += 1
                elif board[ny][nx] == ".":
                    cnt += 1
            if cnt < 3:
                ans[y][x] = "X"
min_r, min_c, max_r, max_c = 10,10,0,0

for y in range(r):
    for x in range(c):
        if ans[y][x] == "X":
            min_r = min(min_r, y)
            max_r = max(max_r, y)
            min_c = min(min_c, x)
            max_c = max(max_c, x)

for y in range(min_r, max_r+1):
    for x in range(min_c, max_c+1):
        print(ans[y][x], end='')
    print()