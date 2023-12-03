from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def high(s:str) -> int:
    if s.isupper():
        return ord(s)-ord('A')
    return ord(s)-ord('a')+26

def cost(cur:int, nxt:int) -> int:
    return max(1, nxt - cur) ** 2

dx = (0,0,1,-1)
dy = (1,-1,0,0)
n,m,t,d = map(int, input().split())
grid = [list(map(high, input().rstrip())) for _ in range(n)]

graph = dict()
rev_graph = defaultdict(list)
distance = dict()
rev_distace = defaultdict(int)

for y in range(n):
    for x in range(m):
        distance[(y, x)] = INF
        graph[(y, x)] = []
        rev_distace[(y, x)] = INF
        rev_graph[(y, x)] = []

        for k in range(4):
            ny, nx = y+dx[k], x+dy[k]
            if 0<=ny<n and 0<=nx<m and abs(grid[y][x]-grid[ny][nx]) <= t:
                graph[(y, x)].append(((ny, nx), cost(grid[y][x], grid[ny][nx])))
                rev_graph[(y, x)].append(((ny, nx), cost(grid[ny][nx], grid[y][x])))
            
def dijkstra(distance, graph):
    hq = [(0, (0, 0))]
    distance[(0, 0)] = 0

    while hq:
        cost, cur = heappop(hq)

        if distance[cur] < cost:
            continue

        for nxt, nxt_cost in graph[cur]:
            if distance[nxt] > cost + nxt_cost:
                distance[nxt] = cost + nxt_cost
                heappush(hq, (distance[nxt], nxt))

dijkstra(distance, graph)
dijkstra(rev_distace, rev_graph)

res = distance[(0, 0)]
for i in range(n):
    for j in range(m):
        if distance[(i, j)] + rev_distace[(i, j)] <= d:
            res = max(res, grid[i][j])

print(res)