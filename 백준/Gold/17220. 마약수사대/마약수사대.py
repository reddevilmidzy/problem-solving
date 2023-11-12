from collections import deque
import sys
input = sys.stdin.readline

def bfs(node:str):
    global res
    if node in tmp:
        return
    
    queue = deque()
    queue.append(node)
    visited.add(node)
    while queue:
        cur = queue.popleft()
        if cur not in graph: continue
        for nxt in graph[cur]:
            if nxt not in visited and nxt not in tmp:
                queue.append(nxt)
                visited.add(nxt)
                res += 1

n,m = map(int,input().split())
graph = dict()
visited = set()
cnt = dict()
alp = [chr(i) for i in range(65, 65+n)]
res = 0

for _ in range(m):
    x,y = input().rstrip().split()
    if x not in graph:
        graph[x] = []
    graph[x].append(y)
    if y not in cnt:
        cnt[y] = 0
    cnt[y] += 1

tmp = set(input().rstrip().split()[1:])

for node in alp:
    if node not in cnt:
        bfs(node)

print(res)