import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(cur):
    global idx, num
    idx += 1

    d[cur] = idx
    stk.append(cur)
    visited[cur] = True

    parent = d[cur]

    for nxt in graph[cur]:
        if d[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif visited[nxt]:
            parent = min(parent, d[nxt])
    
    if parent == d[cur]:
        scc = []
        while True:
            node = stk.pop()
            scc.append(node)

            visited[node] = False
            scc_idx[node] = num
            if cur == node: break
        num += 1
        res.append(scc)
    
    return parent

n,m = map(int,input().split())

d = [-1]*(2*n+1)
stk = []
visited = [False]*(2*n+1)
scc_idx = [0]*(2*n+1)
idx = 0
num = 0
res = []

graph = [[] for _ in range(2*n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[-a].append(b)
    graph[-b].append(a)


for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)
    if d[-cur] == -1:
        dfs(-cur)

res = []

for i in range(1, n+1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
    res.append(+(scc_idx[i] < scc_idx[-i]))
else:
    print(1)
    print(*res)