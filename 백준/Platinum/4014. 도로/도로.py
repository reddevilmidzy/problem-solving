import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], u:int, v:int) -> None:
    u = find(parent, u)
    v = find(parent, v)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v


def union_find(edges:list[list[int]]):
    cnt = 0
    parent = list(range(n+1))
    free = n-1
    for u,v,w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            cnt += 1
            free -= w
            if cnt == n-1: break
    
    return free
     
n,m,k = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[-1])

min_mst = union_find(edges[::-1])
max_mst = union_find(edges)

if k < min_mst or max_mst < k:
    print("no solution")
else:
    cnt = 0
    parent = list(range(n+1))
    standard = list(range(n+1))

    res = []

    for u,v,w in edges[::-1]:
        if not w: break
        if find(standard, u) != find(standard, v):
            union(standard, u, v)
            cnt += 1


    for u,v,w in edges:
        if w: break
        if find(standard, u) != find(standard, v):
            union(standard, u, v)
            union(parent, u, v)
            res.append((u,v,w))
            k -= 1
    

    for u,v,w in edges:       
        if not k: break
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            res.append((u,v,w))
            k -= 1
    
    for u,v,w in edges[::-1]:
        if not w: break
        if find(parent, u) != find(parent, v):
            union(parent,u,v)
            res.append((u,v,w))

    for ans in res:
        print(*ans)