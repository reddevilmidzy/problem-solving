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

n,m = map(int,input().split())
hq = [list(map(int,input().split())) for _ in range(m)]
hq.sort(key=lambda x:-x[2])
st,ed = map(int,input().split())
parent = [i for i in range(n+1)]

for a,b,c in hq:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

        if find(parent, st) == find(parent, ed):
            print(c)
            break