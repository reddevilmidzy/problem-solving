from collections import deque
import sys
sys.setrecursionlimit(10**6)
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(st: int):
    queue = deque()
    visited = [0]*(n+1)
    cnt = 1
    visited[st] = cnt
    queue.append(st)
    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                cnt += 1
                visited[nxt] = cnt
                queue.append(nxt)

    return visited

def dfs(st: int):
    visited = [0]*(n+1)
    cnt = 1
    visited[st] = cnt

    def search(cur: int):
        nonlocal cnt
        for nxt in graph[cur]:
            if not visited[nxt]:
                cnt += 1
                visited[nxt] = cnt
                search(nxt)
    search(st)
    return visited

n = int(input())
edges = []
for i in range(2, (n+2)//2 + 1):
    edges.append((1, i))
for j in range((n+2)//2 + 1, n+1):
    edges.append((2, j))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = edges[_]
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()
# print(*graph)

b = bfs(1)
d = dfs(1)

print(sum([abs(b[i] - d[i]) for i in range(1, n+1)]))

for res in edges:
    print(*res)
