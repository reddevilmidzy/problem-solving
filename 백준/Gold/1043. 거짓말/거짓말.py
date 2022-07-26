import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
peo=list(map(int,input().rstrip().split()))
party=[list(map(int,input().rstrip().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
queue=deque()
for i in party:
    per=i[1:]
    for j in per:
        graph[j].extend(per) # 익스텐드 한거 셋으로 없애줌

for k in range(n+1):
    graph[k] = list(set(graph[k])-{k})    # 차집합
#print(graph)

for v in peo[1:]:
    visited[v] = True
    queue.append(v)
#print(visited)

def bfs():
    while queue:
        q=queue.popleft()
        for v in graph[q]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)

bfs()
res=set()
ans=0
#print(visited)
for q in range(n+1):
    if visited[q]:
        res.add(q)

for c in party:
    if set(c[1:])==set(c[1:])-res:
        ans+=1
print(ans)