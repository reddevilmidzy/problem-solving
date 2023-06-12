from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        x,y,r = map(int,input().split())
        dx1,dy1 = (x1 - x)**2, (y1 - y)**2
        dx2,dy2 = (x2 - x)**2, (y2 - y)**2

        r1 = dx1 + dy1
        r2 = dx2 + dy2
        r = r**2
        if (r1 > r and r2 < r) or (r1 < r and r2 > r): # r1 은 원 밖에 r2 는 원 안에
            ans += 1
    print(ans)