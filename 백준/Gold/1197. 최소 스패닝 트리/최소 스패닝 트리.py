import heapq, sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
edges = []
parent = [i for i in range(v+1)]
ans = 0
for _ in range(e):
    a,b,c = map(int,input().split())
    heapq.heappush(edges, (c,a,b))

while edges:
    cost,a,b = heapq.heappop(edges)
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += cost
print(ans)