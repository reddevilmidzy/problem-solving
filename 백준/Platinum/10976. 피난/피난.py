import sys
input = sys.stdin.readline
INF = int(1e9)

def make_flow(st:int, ed:int, path:list[int]) -> int:
    cost = INF
    cur = ed

    while cur != st:
        cost = min(cost, capacity[path[cur]][cur]-flow[path[cur]][cur])
        cur = path[cur]
    
    cur = ed
    
    while cur != st:
        flow[path[cur]][cur] += cost
        flow[cur][path[cur]] -= cost
        cur = path[cur]
    
    return cost

def bfs(st:int, ed:int) -> int:
    path = [-1]*(n+1)
    q = [st]

    for u in q:
        for v in graph[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] < 0:
                q.append(v)
                path[v] = u
                if v == ed:
                    return make_flow(st, ed, path)
    return 0


def edmonds_karp(st:int, ed:int) -> int:
    max_flow = 0
    while True:
        cost = bfs(st,ed)
        if cost > 0: max_flow += cost
        else: return max_flow


t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    flow = [[0]*(n+1) for _ in range(n+1)]
    capacity = [[0]*(n+1) for _ in range(n+1)]

    for __ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] += 1
    
    print(edmonds_karp(1, n))