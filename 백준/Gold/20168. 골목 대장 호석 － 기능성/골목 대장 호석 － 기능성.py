# from collections import deque
# import heapq
import sys
input =sys.stdin.readline

# INF = int(1e9)

# def dijkstra(start,end):
#     q = []
#     heapq.heappush(q, (0, start,c))
#     dist = [INF]*(n+1)
#     dist[start] = 0
#     while q:
#         cost,node,now = heapq.heappop(q)
#         if cost>dist[node]:
#             continue
#         if cost>now:
#             continue

#         for nex,mon in graph[node]:
#             if dist[node]+mon < dist[nex]:
#                 dist[nex] = dist[node]+mon
#                 heapq.heappush(q,(mon,nex))
#     return dist


def dfs(start,arr,won,visited):
    #print(start,arr)
    if start==b:
        #arr.sort(reverse =True)
        candi.append(sorted(arr.copy())[-1])
        # print('arr',arr)
        #return
    for nex,mon in graph[start]:
        if mon<=won and not visited[nex]:
            arr.append(mon)
            visited[nex] = True
            dfs(nex,arr,won-mon,visited)
            visited[nex] = False
            arr.pop()


n,m,a,b,c = map(int,input().split())
h = []
# heapq.heappush(h, (a,0))
graph = [[] for _ in range(n+1)]
takeit = [0]*(n+1)
visited = [False]*(n+1)
visited[a] = True
candi = []
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

dfs(a,h,c,visited)

print(sorted(candi)[0] if candi else -1)