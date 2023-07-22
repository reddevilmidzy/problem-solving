import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())
for _ in range(t):
    r,c = map(int,input().split())
    graph = []
    parent = [i for i in range(r*c)]
    ans = 0

    for i in range(r):
        tmp = list(map(int,input().split()))
        for j in range(c-1):
            graph.append((tmp[j], i*c+j, i*c+j+1))

    for i in range(r-1):
        tmp = list(map(int,input().split()))
        for j in range(c):
            graph.append((tmp[j], i*c+j, i*c+j+c))
    graph.sort()

    for cost, a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ans += cost

    print(ans)