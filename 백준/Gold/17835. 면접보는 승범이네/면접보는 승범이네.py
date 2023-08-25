import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():

    while hq:
        cost, node = heapq.heappop(hq)
        if cost > distance[node]: continue

        for nxt, dist in graph[node]:
            if dist + cost < distance[nxt]:
                distance[nxt] = dist + cost
                heapq.heappush(hq, (distance[nxt], nxt))
    
    return distance[1:]

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
edges = [list(map(int,input().split())) for _ in range(m)]
edges.sort()
hq = []
distance = [INF]*(n+1)

for i in range(m):
    a,b,c = edges[i-1]
    u,v,w = edges[i]
    if u==a and v==b: continue
    graph[v].append((u,w))

city = list(map(int,input().split()))
tot = []

for i in city:
    heapq.heappush(hq, (0, i))
    distance[i] = 0

ans = dijkstra()
max_val = max(ans)
print(ans.index(max_val)+1, max_val, sep='\n')