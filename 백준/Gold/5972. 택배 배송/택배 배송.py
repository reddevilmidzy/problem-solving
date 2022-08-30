import heapq, sys
input = sys.stdin.readline

def dijkstra(start, end):
    dist = [INF]*(end+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dis,now = heapq.heappop(q)
        if dist[now] < dis:
            continue

        for i in graph[now]:
            cost = i[1]+dis
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist[end]

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print(dijkstra(1, n))