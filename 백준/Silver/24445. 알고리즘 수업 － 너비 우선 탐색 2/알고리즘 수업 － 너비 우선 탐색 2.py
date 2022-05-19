import sys 
from collections import deque
input = sys.stdin.readline

cnt = 0

def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = True
    while queue:
        cnt += 1
        v = queue.popleft()
        order[v] = cnt
        for i in sorted(graph[v], reverse=True):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, r = map(int, input().rstrip().split())
visited = [False for i in range(n+1)]
graph = [[] for i in range(n+1)]
order = [0 for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, r, visited)
print(*order[1:], sep='\n')