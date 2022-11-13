import sys, heapq
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

def crsk(hq):
    cost = 0
    while hq:
        w,u,v = heapq.heappop(hq)
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            cost += w
    return cost

n,m,k = map(int,input().split())
power_plant = list(map(int,input().split()))
graph = []
parent = [i for i in range(n+1)]
for i in power_plant:
    parent[i] = 0

for _ in range(m):
    u,v,w = map(int,input().split())
    heapq.heappush(graph, [w,u,v])

print(crsk(graph))
