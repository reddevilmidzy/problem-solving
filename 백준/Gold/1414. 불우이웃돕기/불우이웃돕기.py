from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

def find(parent: list[int], x: int) -> int:
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: list[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dist = dict()
hq = []
parent = [i for i in range(n)]
edges = n-1
give = 0

for i in range(97, 123):
    dist[chr(i)] = i - 96
for i in range(65, 91):
    dist[chr(i)] = i - 38


for i in range(n):
    for j in range(n):
        if graph[i][j] != "0":
            heappush(hq, (dist[graph[i][j]], i, j))

while hq:
    cost, a, b = heappop(hq)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        edges -= 1
    else:
        give += cost

print(give if not edges else -1)