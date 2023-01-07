from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dag = [0]*(n+1)
res = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    dag[b] += 1

queue = deque()
for i in range(1, n+1):
    if dag[i]==0:
        queue.append(i)

while queue:
    node = queue.popleft()
    res.append(node)
    for i in graph[node]:
        dag[i] -= 1
        if dag[i] == 0:
            queue.append(i)

print(*res)