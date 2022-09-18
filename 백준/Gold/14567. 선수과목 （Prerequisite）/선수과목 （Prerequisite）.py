from collections import deque
n,m = map(int,input().split())

table = [[] for _ in range(n+1)]
res = [0]*(n+1)
pre = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    table[a].append(b)
    pre[b] += 1

queue = deque()
for i in range(1, n+1):
    if pre[i]==0:
        queue.append([i,1])

while queue:
    node,cnt = queue.popleft()
    res[node] = cnt
    for i in table[node]:
        pre[i] -= 1
        if pre[i] == 0:
            queue.append([i,cnt+1])

print(*res[1:])