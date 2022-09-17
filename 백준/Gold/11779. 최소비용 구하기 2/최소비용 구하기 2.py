import heapq
import sys
input = sys.stdin.readline

def dijkstra(start,end):
    INF = int(1e9)
    distance = [INF]*(n+1)
    distance[start] = 0
    global root
    h = []
    heapq.heappush(h,(start,0))
    while h:
        node, dist = heapq.heappop(h)
        if distance[node] < dist:
            continue

        for u,v in graph[node]:
            if dist+v < distance[u]:
                # print('node',node, 'u',u)
                root[u] = [node]
                distance[u] = dist+v
                heapq.heappush(h, (u, dist+v))
    # print('root',root)
    return distance[end]

def dfs(start):
    global route
    route.append(start)
    for i in root[start]:
        dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
root = [[] for _ in range(n+1)]
route = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end= map(int,input().split())

print(dijkstra(start, end))
dfs(end)
print(len(route))
print(*reversed(route))