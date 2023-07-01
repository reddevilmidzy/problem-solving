import sys
input = sys.stdin.readline

def inclination(a:list[int], b:list[int]) -> tuple[int]:
    return b[0] - a[0], b[1] - a[1]

def ccw(a:list[int], b:list[int], c:list[int]) -> bool:
    v, u = inclination(a, b), inclination(b, c)
    return v[0] * u[1] > v[1] * u[0]

def convex_hull(points: list[list[int]]):
    convex = []
    for c in points:
        while len(convex) >= 2:
            a, b = convex[-2], convex[-1]
            if ccw(a, b, c):
                break
            convex.pop()
        convex.append(c)
    
    return len(convex)

n, res = int(input()), -2
points = [list(map(int,input().split())) for _ in range(n)]
points.sort()

res += convex_hull(points)
res += convex_hull(points[::-1])
print(res)