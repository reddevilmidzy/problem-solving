import sys
input = sys.stdin.readline

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def ccw(a,b,c):
    return a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])

def cccw(a,b,c,d):
    tmp = d[:]
    tmp[0] -= (c[0] - b[0])
    tmp[1] -= (c[1] - b[1])
    return ccw(a,b,tmp)

def convex_hull(points):
    res = []
    for p in points:
        while len(res) >= 2 and ccw(res[-2], res[-1], p) <= 0:
            res.pop()
        res.append(p)
    return res

def solve():
    upper = convex_hull(points)
    lower = convex_hull(points[::-1])
    convex = upper[:-1] + lower[:-1]

    m = len(convex)
    res = 0
    j = 1

    for i in range(m):
        while j+1 != i and cccw(convex[i], convex[(i+1)%m], convex[j%m], convex[(j+1)%m]) > 0:
            if dist(convex[i], convex[j%m]) > res:
                res = dist(convex[i], convex[j%m])
            j+= 1
        
        if dist(convex[i], convex[j%m]) > res:
            res = dist(convex[i], convex[j%m])
    return res

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
points.sort()

print(solve())