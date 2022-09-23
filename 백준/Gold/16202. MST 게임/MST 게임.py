import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m,k = map(int,input().split())
ans = [0]*(k)
edges = []
span = 0
spanning = []

for i in range(1,m+1):
    y,z = map(int,input().split())
    #heapq.heappush(edges, [i, y, z])
    edges.append([i,y,z])

for res in range(k):
    parent = [i for i in range(n+1)]
    for i,y,z in edges:
        # print(i, y, z)
        if find_parent(parent, y) != find_parent(parent, z):
            union_parent(parent, y, z)
            span += 1
            spanning.append(i)
        if span==n-1:
            break
    if span==n-1:
        ans[res] = sum(spanning)
        span = 0
        spanning = []
        edges.pop(0)
    else:
        break    
print(*ans)