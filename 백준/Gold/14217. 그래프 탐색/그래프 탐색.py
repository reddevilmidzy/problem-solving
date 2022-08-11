import sys
from collections import deque
input =sys.stdin.readline

def bfs():
    queue = deque()
    visited = [-1]*(n+1)
    visited[1] = 0
    queue.append([1, 0])
    while queue:
        now,dis = queue.popleft()
        for i in graph[now]:
            if visited[i]==-1:
                visited[i] = dis+1
                queue.append([i, dis+1])
    return visited[1:]

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

q = int(input())
for _ in range(q):
    a,i,j = map(int,input().split())
    if a==1:
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)

    print(*bfs())