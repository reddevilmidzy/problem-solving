from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(st:int, ed:int):
    INF = float('inf')
    hq = []
    hq.append((0,st))
    dist = [INF for _ in range(n+1)]
    dist[st] = 0
    
    while hq:
        cost, cur = heappop(hq)
        if dist[cur] < cost: 
            continue

        for nxt, nxt_cost in graph[cur]:
            if dist[nxt] > cost + nxt_cost:
                dist[nxt] = cost + nxt_cost
                heappush(hq, (dist[nxt], nxt))

    res = dist[ed]

    for c in range(k):
        dp, dist = dist, [INF for _ in range(n+1)]

        for x in range(1, n+1):
            if dp[x] == INF: continue
            for y, cost in graph[x]:
                dist[y] = min(dist[y], dp[x] - cost)

        hq = [(-dist[x], x) for x in range(1,n+1)]
        heapify(hq)

        while hq:
            cost, cur = heappop(hq)
            cost = -cost
            if dist[cur] < cost: continue

            for nxt, nxt_cost in graph[cur]:
                if dist[nxt] > dist[cur] + nxt_cost:
                    dist[nxt] = dist[cur] + nxt_cost
                    heappush(hq, (-dist[nxt], nxt))

        res = min(res, dist[ed])

    return res

print(dijkstra(1,n))