from collections import deque
import sys
input = sys.stdin.readline

n,m,x,y = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

odd = [False]*(n+1)
even = [False]*(n+1)

def bfs(st):
    queue = deque([(st, 0)])
    
    while queue:
        cur, cnt = queue.popleft()
        if cnt >= y: continue
        for nxt in graph[cur]:
            if cnt%2 != 0:
                if not even[nxt]:
                    even[nxt] = True
                    queue.append((nxt, cnt+1))
            else:
                if not odd[nxt]:
                    odd[nxt] = True
                    queue.append((nxt, cnt+1))

    if y%2 == 0:
        return even
    return odd

res = bfs(x)

if sum(res) == 0:
    print(-1)
else:
    for i in range(1, n+1):
        if res[i]:
            print(i, end=' ')