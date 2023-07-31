from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s:int, d:int) -> list[int]:
    hq = []
    distance = [INF]*n
    distance[s] = 0
    heappush(hq, (0, s))

    while hq:
        dist, cur = heappop(hq)
        if dist > distance[cur]: continue

        for nxt, wgt in graph[cur]:
            if dist + wgt < distance[nxt] and not visited[cur][nxt]:
                distance[nxt] = dist + wgt
                heappush(hq, (distance[nxt], nxt))
        
    return distance

def dfs(s:int, d:int) -> None:
    stk = [d]

    while stk:
        cur = stk.pop()
        if cur == s: continue

        for pre,wgt in re_graph[cur]:
            if distance[cur] == distance[pre] + wgt and not visited[pre][cur]:
                stk.append(pre)
                visited[pre][cur] = True
while True:
    n,m = map(int,input().split())
    if n == 0: break
    s,d = map(int,input().split())
    graph = [[] for _ in range(n)]
    re_graph = [[] for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
        re_graph[v].append((u,p))

    distance = dijkstra(s, d)
    dfs(s,d)
    distance = dijkstra(s,d)
    print(distance[d] if distance[d] != INF else -1)