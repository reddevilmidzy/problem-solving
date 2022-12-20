import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(graph, v, visited, cnt):
    global ans
    if cnt == 4:
        ans = 1
        return 
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited,cnt+1)
            visited[i] = False

n,m = map(int,input().rstrip().split())
graph = [[] for i in range(n)]
ans = 0
for _ in range(m):
    a,b= map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
if m >= 4:
    for node in range(n):
        visited = [False] * n
        visited[node] = True
        dfs(graph, node, visited, 0)
        if ans == 1:
            break
print(ans)