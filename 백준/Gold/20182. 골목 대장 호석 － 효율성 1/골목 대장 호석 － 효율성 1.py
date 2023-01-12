import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for nex, cost in graph[now]:
            if dist + cost < distance[nex] and dist + cost <= c:
                distance[nex] = dist + cost
                max_coin[nex] = max(max_coin[nex], cost)
                heapq.heappush(hq, (dist+cost, nex))
    return max_coin[end] if max_coin[end] else -1


n, m, a, b, c = map(int, input().split())
distance = [INF] * (n+1)
max_coin = [0] * (n+1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

print(dijkstra(a, b))