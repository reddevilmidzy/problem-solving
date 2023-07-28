from collections import deque
import sys
input = sys.stdin.readline

def topology():
    queue = deque()
    order = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        if not edges[i]:
            queue.append((i,1))
            order[i].append(1)

    while queue:
        cur,cnt = queue.popleft()
        if order[cur].count(max(order[cur])) >= 2:
            cnt += 1
        for nxt in graph[cur]:
            edges[nxt] -= 1
            order[nxt].append(cnt)
            if not edges[nxt]:
                queue.append((nxt, cnt))
    
    if order[n].count(max(order[n])) >= 2:
        return max(order[n]) + 1
    return max(order[n])


t = int(input())
for _ in range(t):
    k,n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    edges = [0]*(n+1)
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        edges[v] += 1

    print(k,topology())