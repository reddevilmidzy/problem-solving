from collections import deque
import sys
sys.setrecursionlimit(10**5)
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
        scc = 0
        while True:
            node = stk.pop()
            topology[node] = num
            visited[node] = False
            scc += 1
            if node == cur: break
        scc_list.append(scc)
        num += 1
    return parent

def dijkstra():
    queue = deque()
    queue.append((topology[s], 0))
    res = 0
    distance = [0]*(num)

    while queue:
        node,cnt = queue.popleft()

        if topology[t] == node:
            if res < cnt+scc_list[node]:
                res = cnt+scc_list[node]
            continue

        for nxt in dag[node]:
            if distance[nxt] < cnt+scc_list[node]:
                queue.append((nxt, cnt+scc_list[node]))
                distance[nxt] = cnt+scc_list[node]

    return res

n,m,s,t = map(int,input().split())
graph = [[] for _ in range(n+1)]

d = [-1]*(n+1)
visited = [False]*(n+1)
idx = 0
num = 0
stk = []
scc_list = []
ans = 0
topology = dict()

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)

dag = [[] for _ in range(num)]

for cur in range(1, n+1):
    for nxt in graph[cur]:
        if topology[cur] != topology[nxt]:
            dag[topology[cur]].append(topology[nxt])   

print(dijkstra())