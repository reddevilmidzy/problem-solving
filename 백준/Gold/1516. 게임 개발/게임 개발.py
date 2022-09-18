from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
deg = [0]*(n)
cost = []
ans = [0]*(n)
for i in range(n):
    tmp = list(map(int,input().split()))
    cost.append(tmp[0])
    for j in tmp[1:-1]:
        graph[j-1].append(i)
        deg[i] += 1

queue = deque()
for i in range(n):
    if deg[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    ans[node] += cost[node]
    for i in graph[node]:
        deg[i] -= 1
        ans[i] = max(ans[i], ans[node])
        if deg[i] == 0:
            queue.append(i)

print(*ans,sep='\n')