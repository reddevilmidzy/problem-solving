from collections import deque
import sys
input = sys.stdin.readline
INF = -int(1e9)

def bellman(start, end):
    dist = [INF for _ in range(n+1)]
    ans = [n]
    dist[start] = 0
    go = [0]*(n+1)
    for i in range(n-1):
        for u,v,w in graph:
            if dist[u] != INF and dist[u] + w > dist[v]:            
                go[v] = u
                dist[v] = dist[u] + w
                
    for u,v,w in graph:
        if dist[u] != INF and dist[u] + w > dist[v]:
            if bfs(u,end):
                return [-1]
    tmp = n
    
    for i in range(n):
        if tmp==1:
            break
        ans.append(go[tmp])
        tmp = go[tmp]
    return reversed(ans)

def bfs(start, end):
    visit = [False]*(n+1)
    visit[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node==end:
            return True
        for i in route[node]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
    return False

n,m = map(int,input().split())
graph = []
route = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph.append([u,v,w])
    route[u].append(v)
print(*bellman(1, n))