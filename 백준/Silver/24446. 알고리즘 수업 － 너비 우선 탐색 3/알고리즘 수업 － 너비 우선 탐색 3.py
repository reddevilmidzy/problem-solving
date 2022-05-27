import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().rstrip().split())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
order = [-1 for i in range(n+1)]
for i in range(m):
    u,v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    queue = deque()
    queue.append((r, 0))
    visited[r] = True
    order[r] = 0
    while queue:
        q, cnt = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                order[i] = cnt + 1
                queue.append((i, cnt+1))

bfs()
print(*order[1:], sep='\n')