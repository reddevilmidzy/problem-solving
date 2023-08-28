from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def tarjan(cur):
    global idx,num
    idx += 1

    d[cur] = idx
    visited[cur] = True
    stk.append(cur)

    parent = d[cur]

    for nxt in graph[cur]:
        if d[nxt] == -1:
            parent = min(parent, tarjan(nxt))
        elif visited[nxt]:
            parent = min(parent, d[nxt])
    
    if parent == d[cur]:
        scc = []
        while True:
            node = stk.pop()
            visited[node] = False
            scc.append(node)
            scc_idx[node] = num

            if node == cur:break
        
        num += 1
        scc_list.append(scc)
    
    return parent

def topology(adj:list[list[int]], dag:list[int]):

    if dag.count(0) != 1:
        return False
    queue = deque()
    queue.append((num-1,0))
    depth = [0]*num
    while queue:
        cur,level = queue.popleft()
        if depth[level] != 0:
            return False
        depth[level] += 1
        for nxt in adj[cur]:
            dag[nxt] -= 1
            if dag[nxt] == 0:
                queue.append((nxt, level+1))

    return True

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
d = [-1]*(n+1)
visited = [False]*(n+1)
stk = []
idx = 0
num = 0
scc_idx = dict()
scc_list = []

for _ in range(m):
    v,w = map(int,input().split())
    graph[v].append(w)

for cur in range(1, n+1):
    if d[cur] == -1:
        tarjan(cur)

adj = [[] for _ in range(num)]
dag = [0]*num

for cur in range(1, n+1):
    for nxt in graph[cur]:
        if scc_idx[cur] != scc_idx[nxt]:
            adj[scc_idx[cur]].append(scc_idx[nxt])
            dag[scc_idx[nxt]] += 1

if topology(adj, dag):
    print(len(scc_list[-1]))
    print(*sorted(scc_list[-1]))
else:
    print(0)