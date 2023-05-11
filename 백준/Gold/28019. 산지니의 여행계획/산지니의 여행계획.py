import sys, heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b) 
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def dfs(cur: int, pre: int, dist: int):
    global max_dist
    max_dist = max(max_dist, dist)
    for nxt, cost in graph[cur]:
        if nxt != pre:
            dfs(nxt, cur, dist+cost)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
hq = []
parent = [i for i in range(n+1)]
visited = [0]*(n+1)
tot = 0 # 총 도로의 합
max_dist = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(hq, (-c,a,b))

st = int(input())
edges = n-1

while hq:
    c,a,b = heapq.heappop(hq)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        graph[a].append((b, -c))
        graph[b].append((a, -c))
        edges -= 1
        tot += -c
        if not edges:
            break

dfs(st,-1,0)

print(tot*2 - max_dist)