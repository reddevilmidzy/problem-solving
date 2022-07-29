import sys, heapq
input = sys.stdin.readline


def dijkstra(start, end):
    dis=[1e9]*(n+1)
    dis[start] = 0
    queue = [[0, start]]
    while queue:
        k,u = heapq.heappop(queue)
        if k > dis[u]:
            continue
        for w,v in graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, [dis[v],v])
    return dis[end]



n=int(input())
m=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
depart, arrive = map(int,input().split())

print(dijkstra(depart, arrive))