import sys
input = sys.stdin.readline

def dist(a:list[int], b:list[int]) -> int:
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def ccw(p1, p2, p3):
    return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def cccw(p1, p2, p3, p4):
    tmp = p4[:]
    tmp[0] -= (p3[0] - p2[0])
    tmp[1] -= (p3[1] - p2[1])
    return ccw(p1, p2, tmp)

def convex_hull(points:list[list[int]]) -> int:
    convex = []
    for c in points:
        while len(convex) >= 2 and ccw(convex[-2], convex[-1], c) <= 0:
            convex.pop()
        convex.append(c)

    return convex

def solve(pos:list[list[int]]):
    upper = convex_hull(pos)
    lower = convex_hull(pos[::-1])
    lp,rp = 0, len(lower)-1
    convex = upper[:-1] + lower[:-1] # 반시계

    m = len(convex)
    res = 0
    j = 1
    a = convex[0]
    b = convex[1]

    for i in range(m):
        while j+1 != i and cccw(convex[i], convex[(i+1)%m], convex[j%m], convex[(j+1)%m]) > 0:
            if dist(convex[i], convex[j%m]) > res:
                res = dist(convex[i], convex[j%m])
                a = convex[i]
                b = convex[j%m]
            j += 1
        
        if dist(convex[i], convex[j%m]) > res:
            a = convex[i]
            b = convex[j%m]
            res = dist(convex[i], convex[j%m])
    return *a,*b

t = int(input())
for _ in range(t):
    n = int(input())
    pos = [list(map(int,input().split())) for _ in range(n)]
    pos.sort()
    
    print(*solve(pos))