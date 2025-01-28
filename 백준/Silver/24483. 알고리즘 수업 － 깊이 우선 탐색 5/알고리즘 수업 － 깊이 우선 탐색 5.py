import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()


visited = [False] * (n + 1)
d = [-1] * (n + 1)
d[r] = 0

cnt = 1
t = [0] * (n + 1)

def dfs(cur: int) -> None:
    global cnt

    t[cur] = cnt
    visited[cur] = True
    cnt += 1

    for nxt in graph[cur]:
        if not visited[nxt]:
            d[nxt] = d[cur] + 1
            dfs(nxt)

dfs(r)
print(sum([t[i]*d[i] for i in range(1, n + 1)]))
