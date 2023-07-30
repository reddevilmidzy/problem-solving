from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s:int,e:int) -> list[int]:
    hq = []
    distance = [INF]*(n+1)
    distance[s] = 0
    heappush(hq, (0, s))
    while hq:
        dist, cur = heappop(hq)
        if distance[cur] < dist: continue

        for nxt, wgt in graph[cur]:
            if distance[nxt] > dist + wgt and can_use[nxt]:
                distance[nxt] = dist + wgt
                heappush(hq, (distance[nxt], nxt))

    # 단순히 최단 경로 구하기
    return distance


def bfs(s:int, e:int) -> int:
    queue = deque()
    queue.append((s, 0, [s])) # cur, dist
    visited = [False]*(n+1)
    visited[s] = True

    res = []
    while queue:
        cur, dist, rot = queue.popleft()
        if cur == e:
            res.append(rot)
            continue
        for nxt, wgt in graph[cur]:
            if dist + wgt == distance[nxt] and can_use[nxt] and (nxt == e or not visited[nxt]):
                queue.append((nxt, dist+wgt, rot + [nxt]))
                if nxt != e: visited[nxt] = True

    res.sort()
    return res[0]

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
can_use = {i:True for i in range(1, n+1)}

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

for i in range(1,n+1):
    graph[i].sort()

s,e = map(int,input().split())

distance = dijkstra(s,e)
ans = distance[e]

route = bfs(s,e)

for i in route:
    can_use[i] = False

# 시작점 끝점 원복
can_use[s] = True
can_use[e] = True

distance = dijkstra(s,e)
ans += distance[e]

print(ans)