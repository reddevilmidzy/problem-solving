# 간선은 정확이 두번 사용
# 정점은 두번이상

import sys, heapq
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

n,p = map(int,input().split())
parent = [i for i in range(n+1)]
cost = [0] + [int(input()) for _ in range(n)]
hq = []

for _ in range(p):
    u,v,w = map(int,input().split())
    heapq.heappush(hq, (2*w+cost[u]+cost[v], u,v,w))

nodes = [0]*(n+1)
ans = min(cost[1:])

while hq:
    dist,u,v,w = heapq.heappop(hq)
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        ans += dist
print(ans)