import sys, heapq
input = sys.stdin.readline

def dijkstra(start, end):
    dis=[int(1e9)]*(n+1)
    dis[start]=0
    q = [[0,start]]
    while q:
        k,u = heapq.heappop(q)
        if k > dis[u]:
            continue
        for w,v in graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u]+w
                heapq.heappush(q, [dis[v],v])
    return dis[end]

n,e=map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

first_stop, second_stop=map(int,input().rstrip().split())

first_path = dijkstra(1, first_stop)+dijkstra(first_stop, second_stop)+dijkstra(second_stop,n)
second_path = dijkstra(1, second_stop)+dijkstra(second_stop, first_stop)+dijkstra(first_stop,n)

print(-1 if first_path>=1e9 and second_path>=1e9 else min(first_path, second_path))