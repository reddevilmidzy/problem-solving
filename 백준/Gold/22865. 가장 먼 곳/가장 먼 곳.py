import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        
        for next, cost in graph[now]:
            if cost + dist < distance[next]:
                distance[next] = cost + dist
                heapq.heappush(pq, (cost+dist, next))

    return distance

n = int(input())
nums = list(set(map(int,input().split())))
graph = [[] for _ in range(n+1)]
m = int(input())
distance_list = []
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

for i in nums:
    distance_list.append(dijkstra(i))

ans = [0]

for i in range(1, n+1):
    tmp = INF
    for j in range(len(nums)):
        tmp = min(tmp, distance_list[j][i])
    ans.append(tmp)

print(ans.index(max(ans)))