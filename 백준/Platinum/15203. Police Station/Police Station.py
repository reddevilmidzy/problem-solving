import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur:int) -> int:
    global idx, num, police
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
        tmp = []
        while True:
            node = stk.pop()
            tmp.append(node)
            visited[node] = False
            scc_idx[node] = num
            if cur == node: break

        num += 1
        police = tmp
    return parent

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)

idx = 0
num = 0
stk = []
visited = [False]*(n+1)
d = [-1]*(n+1)
scc_idx = dict()
police = []

for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)

cnt = [0]*num

for cur in range(1, n+1):
    for nxt in graph[cur]:
        if scc_idx[cur] != scc_idx[nxt]:
            cnt[scc_idx[nxt]] += 1

if cnt.count(0) == 1:
    print(len(police))
    print(*sorted(police))
else:
    print("0\n")
