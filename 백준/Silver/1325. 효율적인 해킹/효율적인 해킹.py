import sys
from collections import deque
input = sys.stdin.readline

def bfs(com):
    ans = 0
    queue = deque()
    queue.append(com)
    visited[com] = True
    while queue:
        hack = queue.popleft()
        for i in graph[hack]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                ans += 1
    res[com] = ans

n,m = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
res = dict()
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    graph[b].append(a)

# print(graph)
for c in range(1, n+1):
    visited = [False for _ in range(n+1)]
    bfs(c)
max_hack = max(res.values())
for k,val in res.items():
    if val==max_hack:
        print(k, end=' ')
# print(res)