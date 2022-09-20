import sys, heapq
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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edges = []
ans = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if a!=b:
        heapq.heappush(edges, [c,a,b])

while edges:
    cost,a,b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += cost
print(ans)