from sys import stdin
input = stdin.readline

def inclination(a:list[int], b:list[int]) -> tuple[int]:
    return b[0] - a[0], b[1] - a[1]

def ccw(a:list[int], b:list[int], c:list[int]) -> bool:
    v, u = inclination(a, b), inclination(b, c)
    return v[0] * u[1] > v[1] * u[0]

def convex_hull(points: list[list[int]]):
    convex = []
    res = []
    for c in points:
        while len(convex) >= 2:
            a, b = convex[-2], convex[-1]
            if ccw(a, b, c):
                break
            convex.pop()
        convex.append(c)
    global ans
    convex.pop()
    ans.extend(convex)
    return len(convex)+1

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    res = -2
    ans = []
    for __ in range(n//5 + int(n%5!=0)):
        tmp = list(map(int,input().split()))
        for i in range(0,len(tmp)+1//2,2):
            points.append((tmp[i], tmp[i+1]))
    
    points.sort()
    res += convex_hull(points)
    res += convex_hull(points[::-1])
    print(res)
    idx = ans.index(max(ans, key=lambda x:(x[1], -x[0])))
    cnt = res
    while cnt:
        print(*ans[idx])
        cnt -= 1
        idx = (idx-1)%res