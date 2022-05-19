import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
cnt = 0
def dfs(graph, v, visited):
    global cnt
    cnt += 1
    visited[v] = True
    order[v] = cnt
    #print(v)
    for i in sorted(graph[v], reverse=True):
        if not visited[i]:
            dfs(graph, i, visited)

n, m, r = map(int, input().rstrip().split())
visited = [False] * (n+1)
graph = [[] for i in range(n+1)]
order = [0 for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, r, visited)
print(*order[1:], sep="\n")