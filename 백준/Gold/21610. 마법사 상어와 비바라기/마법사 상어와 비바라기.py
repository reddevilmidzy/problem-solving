from sys import stdin
input = stdin.readline

dy = [0,-1,-1,-1,0,1,1,1]
dx = [-1,-1,0,1,1,1,0,-1]

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

cloud = [(n-1,0), (n-1,1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    d,s = map(int,input().split())
    d-=1
    pre = set()

    for i in range(len(cloud)):
        y,x = cloud[i][0], cloud[i][1]
        ny,nx = (y+dy[d]*s)%n, (x+dx[d]*s)%n

        a[ny][nx] += 1
        cloud[i] = (ny,nx)
    
    for y,x in cloud:
        cnt = 0
        pre.add((y,x))
        for i in range(1, 8, 2):
            ny,nx = y+dy[i], x+dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if a[ny][nx]: cnt += 1

        a[y][x] += cnt
    
    cloud.clear()

    for r in range(n):
        for c in range(n):
            if a[r][c] >= 2 and (r,c) not in pre:
                a[r][c] -= 2
                cloud.append((r,c))

print(sum(map(sum, a)))