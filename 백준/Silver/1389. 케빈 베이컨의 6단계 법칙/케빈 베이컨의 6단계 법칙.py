import sys
from collections import deque
input = sys.stdin.readline

def bfs(v, visited):
    queue = deque()
    queue.append([v,0])
    visited[v] = True
    ans = []
    while queue:
        k,cnt = queue.popleft()
        ans.append(cnt)
        #print('k', k, 'cnt',cnt)
        for i in graph[k]:
            if not visited[i]:
                visited[i] = True
                queue.append([i,cnt+1])
    return sum(ans)
n,m = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
res = []
for f in range(1, n+1):
    visited = [False for _ in range(n+1)]
    res.append(bfs(f, visited))
print(res.index(min(res))+1)