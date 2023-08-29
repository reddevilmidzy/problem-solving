import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra():
    dist = [INF]*(d+1)
    hq = []
    heapq.heappush(hq, [0, 0])
    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        
        for nxt, time in road[node]:
            if dist[nxt] > cost + time:
                dist[nxt] = cost + time
                heapq.heappush(hq, [dist[nxt], nxt])
    return dist[d]

n,d = map(int,input().split())
road = [[[i+1,1]] for i in range(d+1)]
road[d] = []

for _ in range(n):
    st,ed,cost = map(int,input().split())
    if ed > d:
        continue
    road[st].append([ed, cost])
print(dijkstra())