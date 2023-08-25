import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)

d = [-1]*(n+1)
stk = []
visited = [False]*(n+1)
idx = 0
ans = False

def dfs(cur):
    global idx
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
        scc = 0
        while True:
            node = stk.pop()
            visited[node] = False
            scc += 1
            if cur == node: break

        if scc == n:
            global ans
            ans = True
    return parent

for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)
print(["No","Yes"][ans])