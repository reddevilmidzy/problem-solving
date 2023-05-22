from collections import deque
import sys
input = sys.stdin.readline

def bfs(st: int) -> str:
    queue = deque()
    queue.append(st)
    visited = [False]*(n+1)
    visited[st] = True
    if gomgom[st]:
        return "Yes"
    while queue:
        node = queue.popleft()
        if leaf[node]:
            return "yes"
        for nxt in graph[node]:
            if not visited[nxt] and not gomgom[nxt]:
                queue.append(nxt)
                visited[nxt] = True
    return "Yes"

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)

leaf = [len(edge) == 0 for edge in graph]
s = int(input())
gomgom = [False]*(n+1)
nums = list(map(int,input().split()))
for num in nums:
    gomgom[num] = True

print(bfs(1))