from collections import deque
import sys
input = sys.stdin.readline

def bfs(node:int) -> int:
    queue = deque()
    queue.append((node, 0))
    visited = [False]*n
    visited[node] = True
    res = 0
    while queue:
        cur,cnt = queue.popleft()
        res += 1
        for nxt in graph[cur]:
            if not visited[nxt] and cnt + 1 <= 2:
                queue.append((nxt, cnt+1))
                visited[nxt] = True
    
    # 자기 자신 뺀 값
    return res-1 

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        if a[i][j] == "Y":
            graph[i].append(j)
            graph[j].append(i)

res = 0
for node in range(n):
    tmp = bfs(node)
    if res < tmp:
        res = tmp
print(res)