import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (p+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nex, cost in graph[now]:
            if dist + cost < distance[nex]:
                distance[nex] = dist + cost
                heapq.heappush(q, (dist+cost, nex))

    return distance

c,p,pb,pa1,pa2 = map(int,input().split())
graph = [[] for _ in range(p+1)]
for _ in range(c):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

distance_a = dijkstra(pb)
distance_b = dijkstra(pa1)
distance_c = dijkstra(pa2)
print(min(distance_a[pa1] + distance_b[pa2], distance_a[pa2] + distance_c[pa1]))