import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    


t = int(input())
for _ in range(t):
    n,m,p,q = map(int,input().split())
    parent = [i for i in range(n+1)]
    edges = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    edges.sort()
    edge = 0
    for w,u,v in edges:
        if min(u,v) == min(p,q) and max(u,v) == max(p,q):
            if edge == n-1:
                print("NO")
                break
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            edge += 1
    else:
        print("YES")