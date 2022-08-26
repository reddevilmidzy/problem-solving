import sys
import heapq
input = sys.stdin.readline

INF = int(1e9) # 무한
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in com[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for _ in range(int(input())): # 테스트 케이스
    n,d,c = map(int,input().split()) # 컴개수, 의존성개수, 해킹당한 컴
    com = [[] for __ in range(n+1)]
    distance = [INF] * (n+1)
    for i in range(d):
        a,b,s = map(int,input().split())
        com[b].append([a,s])
    cnt = 0
    last = 0
    dijkstra(c)
    for j in distance:
        if j != INF:
            cnt += 1
            last = max(last, j)
    
    print(cnt, last)