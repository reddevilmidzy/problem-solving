import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def topology() -> defaultdict:
    queue = deque()
    res = defaultdict(list)
    for item in items:
        if edges[item] == 0:
            queue.append((item,0))

    while queue:
        item, cnt = queue.popleft()
        res[cnt].append(item)
        for nxt in graph[item]:
            edges[nxt] -= 1
            if edges[nxt] == 0:
                queue.append((nxt, cnt+1))
    return res

n = int(input())
graph = defaultdict(list)
edges = defaultdict(int)
items = set()

for _ in range(n):
    a,b = input().rstrip().split()
    graph[a].append(b)
    edges[b] += 1
    items.add(a)
    items.add(b)

order = topology()

if len(items) != sum([len(i) for i in order.values()]):
    print(-1)
else:
    for ans in order.values():
        print(*sorted(ans), sep='\n')