from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)+7

def bfs(st_node:int) -> list[int]:
    queue = deque()
    queue.append([st_node, INF])
    visited = [INF]*(N+1)
    visited[st_node] = 0

    while queue:
        node, reco = queue.popleft()

        for next, cost in graph[node]:
            if visited[next] == INF:
                visited[next] = min(cost,reco)
                queue.append([next, min(cost,reco)])
    
    return visited[1:]

N,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
tot = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[q].append([p,r])
    graph[p].append([q,r])

for _ in range(Q):
    k,v = map(int,input().split())
    ans = 0
    if tot[v] == []:
        tot[v] = bfs(v)

    for r in tot[v]:
        if r >= k:
            ans += 1
    print(ans)