from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(st:int) -> list[int]:
    hq = [(0, st)]
    distance = [[INF]*k for _ in range(n+1)]
    distance[st][0] = 0

    while hq:
        dist, cur = heappop(hq)
        if distance[cur][k-1] < dist: continue

        for nxt, cost in graph[cur]:
            if dist + cost < distance[nxt][k-1]:
                distance[nxt][k-1] = dist + cost
                heappush(hq, (distance[nxt][k-1], nxt))
                distance[nxt].sort()

    return [distance[i][k-1] if distance[i][k-1] != INF else -1 for i in range(1, n+1)]

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

print(*dijkstra(1),sep='\n')