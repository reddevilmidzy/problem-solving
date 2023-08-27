import sys, heapq
sys.setrecursionlimit((2*10**5)+85000)
input = sys.stdin.readline

def dfs(cur):
    global idx, num
    idx += 1

    d[cur] = idx
    visited[cur] = True
    stk.append(cur)

    parent = d[cur]

    for nxt in graph[cur]:
        if d[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif visited[nxt]:
            parent = min(parent, d[nxt])
    
    if parent == d[cur]:
        cost = 0
        while True:
            node = stk.pop()
            topology[node] = num
            visited[node] = False
            cost += money[node]
            if node == cur: break

        scc_cost.append(cost)    
        num += 1
    return parent

def dijkstra():

    hq = []
    distance = [0]*(num)
    distance[topology[s]] =  -scc_cost[topology[s]]
    heapq.heappush(hq, (-scc_cost[topology[s]], topology[s]))

    while hq:
        cnt, node = heapq.heappop(hq)

        if distance[node] < cnt: continue
        for nxt in dag[node]:
            if distance[nxt] > cnt-scc_cost[nxt]:
                distance[nxt] = cnt-scc_cost[nxt]
                heapq.heappush(hq, (distance[nxt], nxt))
    return distance

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
d = [-1]*(n+1)
visited = [False]*(n+1)
stk = []
topology = dict()
scc_cost = []
idx = 0
num = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

money = [0] + [int(input()) for _ in range(n)]
s,p = map(int,input().split())
food = list(map(int,input().split()))

for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)

dag = [[] for _ in range(num)]

for cur in range(1, n+1):
    for nxt in graph[cur]:
        if topology[cur] != topology[nxt]:
            dag[topology[cur]].append(topology[nxt])

distance = dijkstra()

res = 0

for ed in food:
    if res > distance[topology[ed]]:
        res = distance[topology[ed]]
print(-res)