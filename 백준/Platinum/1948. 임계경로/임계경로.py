from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    back = [[] for _ in range(n+1)]

    cnt = [0]*(n+1)

    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        back[v].append((u,w))
        cnt[v] += 1

    st,ed = map(int,input().split())

    time = [0]*(n+1)
    queue = deque([st])
    while queue:
        node = queue.popleft()
        for nxt,wth in graph[node]:
            cnt[nxt] -= 1
        
            if time[nxt] < time[node] + wth:
                time[nxt] = time[node] + wth

            if not cnt[nxt]:            
                queue.append(nxt)

    queue.append(ed)
    edges = 0

    while queue:
        node = queue.popleft()

        for nxt,wgh in back[node]:
            if time[node] - time[nxt] == wgh:
                if cnt[nxt]:
                    edges += 1
                    continue
                queue.append(nxt)
                cnt[nxt] = 1
                edges += 1
    return time[ed], edges
print(*solve(),sep='\n')