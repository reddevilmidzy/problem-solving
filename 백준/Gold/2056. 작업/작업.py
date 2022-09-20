from collections import deque
import sys
input = sys.stdin.readline

n= int(input())
cost = [0]
deg = [0]*(n+1)
ans = [0]*(n+1)
graph = [[] for _ in range(n+1)]
queue = deque()
for i in range(1,n+1):
    nums = list(map(int,input().split()))
    cost.append(nums[0])
    for j in range(2,nums[1]+2):
        deg[i] += 1
        graph[nums[j]].append(i)

for i in range(1,n+1):
    if deg[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    ans[node] += cost[node]
    for i in graph[node]:
        deg[i] -= 1
        ans[i] = max(ans[i], ans[node])
        if deg[i]==0:
            queue.append(i)
print(max(ans))