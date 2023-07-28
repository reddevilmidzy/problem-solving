from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = [[] for _ in range(n+1)]
need = [0]*(n+1)
ans = [0]*(n+1)
ans[n] = 1
for _ in range(m):
    x,y,k = map(int,input().split())
    edges[x].append((y,k))
    need[y] += 1


queue = deque([n])
origin = [i for i in range(1, n+1) if not edges[i]]

while queue:
    cur = queue.popleft()
    for nxt,cnt in edges[cur]:
        need[nxt] -= 1
        ans[nxt] += cnt*ans[cur]
        if not need[nxt]:
            queue.append(nxt)


for i in origin:
    print(i, ans[i])