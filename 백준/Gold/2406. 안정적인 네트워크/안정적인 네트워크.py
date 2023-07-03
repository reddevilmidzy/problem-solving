from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: list[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

graph = [[] for _ in range(n)]
parent = [i for i in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    union(parent, x, y)

cost = [list(map(int,input().split())) for _ in range(n)]
hq = []
for i in range(1, n):
    for j in range(i+1, n):
        heappush(hq, (cost[i][j], i+1, j+1))

ans_edges = []
res = 0

while hq:
    dist, a, b = heappop(hq)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += dist
        ans_edges.append(f"{a} {b}")

print(res, len(ans_edges))
if ans_edges: print(*ans_edges, sep='\n')