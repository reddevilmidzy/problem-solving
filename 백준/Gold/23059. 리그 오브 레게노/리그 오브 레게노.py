import sys
from collections import deque
input = sys.stdin.readline

def topology() -> dict:
    queue = deque()
    res = dict()
    for item in items:
        if item not in edges:
            queue.append((item,0))

    while queue:
        item, cnt = queue.popleft()
        if cnt in res:
            res[cnt].append(item)
        else:
            res[cnt] = [item]
        if item in graph:
            for nxt in graph[item]:
                edges[nxt] -= 1
                if edges[nxt] == 0:
                     queue.append((nxt, cnt+1))
    return res

n = int(input())
graph = dict()
edges = dict()
items = set()

for _ in range(n):
    a,b = input().rstrip().split()
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    if b in edges:
        edges[b] += 1
    else:
        edges[b] = 1
    items.add(a)
    items.add(b)

order = topology()

if len(items) != sum([len(i) for i in order.values()]):
    print(-1)
else:
    for ans in order.values():
        print(*sorted(ans), sep='\n')