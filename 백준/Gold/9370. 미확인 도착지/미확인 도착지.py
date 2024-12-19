from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = float('inf')

def dijkstra(st: int):
    hq = []

    distance = [INF] * (n + 1)
    distance[st] = 0
    heappush(hq, (distance[st], False, st))
    used = [False] * (n + 1)

    while hq:
        dist, vis, cur = heappop(hq)
        if distance[cur] < dist: continue
        for nxt,cost in graph[cur]:
            tmp = vis

            if (cur,nxt) == (g,h) or (nxt,cur) == (g,h):
                tmp = True

            if dist+cost < distance[nxt]:
                distance[nxt] = dist + cost
                used[nxt] = tmp
                heappush(hq, (distance[nxt], tmp, nxt))
            elif not used[nxt] and tmp and cost+dist==distance[nxt]:
                used[nxt] = tmp
                heappush(hq, (distance[nxt], tmp, nxt))
            
    return sorted([i for i in dest if used[i]])

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    dest = [int(input()) for _ in range(k)]

    dist = dijkstra(s)
    print(*dist)