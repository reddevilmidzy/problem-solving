import sys
input = sys.stdin.readline

def inclination(a:list[int], b:list[int]) -> tuple[int]:
    return b[0]-a[0], b[1]-a[1]

def ccw(a:list[int], b:list[int], c:list[int]) -> bool:
    v,u = inclination(a,b), inclination(b,c)
    return v[0]*u[1] >= v[1]*u[0]

def convex_hull(pos:list[list[int]]):
    global excape
    convex = []
    for c in pos:
        while len(convex) >= 2:
            a,b = convex[-2], convex[-1]
            if ccw(a,b,c): break
            convex.pop()
        convex.append(c)
    
    for y,x in convex:
        if y == 0.0 and x == 0.0:
            excape = True
            break

def dist(y:int, x:int) -> float:
    return y/2,  x/2

n = int(input())
bomb = [list(map(int,input().split())) for _ in range(n)]
pos = [(0.0,0.0)]
for y,x in bomb:
    pos.append(dist(y,x))
pos.sort()
excape = False

convex_hull(pos)
convex_hull(pos[::-1])

print(["No","Yes"][excape])