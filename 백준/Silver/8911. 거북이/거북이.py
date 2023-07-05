from sys import stdin
input = stdin.readline

t = int(input())
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

for _ in range(t):
    cmd = input().rstrip()
    r,c,d = 500, 500, 0 
    min_r, max_r = 500, 500
    min_c, max_c = 500, 500

    for i in cmd:
        if i == "F":
            r += dy[d]
            c += dx[d]
        elif i == "B":
            r += dy[(d+2)%4]
            c += dx[(d+2)%4]
        elif i == "L":
            d = (d-1)%4
        else:
            d = (d+1)%4

        min_r = min(min_r, r)
        max_r = max(max_r, r)

        min_c = min(min_c, c)
        max_c = max(max_c, c)

    print((max_r - min_r) * (max_c - min_c))