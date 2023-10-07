from collections import deque
import sys
input = sys.stdin.readline

def bfs(st):
    queue = deque()
    queue.append((st,0))

    while queue:
        cur, pos = queue.popleft()

        for nxt in graph[cur]:
            if visited[nxt] == -1:
                queue.append((nxt, +(pos==0)))
                visited[nxt] = +(pos==0)
            elif visited[nxt] == pos:
                return False
    
    return True

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1]*(n+1)
    
    for st in range(1, n+1):
        if visited[st] == -1:
            visited[st] = 0
            if not bfs(st):
                print("impossible")
                break
    else:
        print("possible")