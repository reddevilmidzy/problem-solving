import sys,heapq
input = sys.stdin.readline

INF = int(1e9)

v,e,x = map(int,input().rstrip().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,dis = map(int,input().rstrip().split())
    graph[a].append([b,dis])

def dijkstra(start):
    q = []
    distance = [INF]*(v+1)

    heapq.heappush(q, [0,start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)