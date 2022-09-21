# 백트래킹 풀이
import sys
input =sys.stdin.readline

def dfs(start,arr,won,visited):
    if start==b:
        candi.append(sorted(arr.copy())[-1])

    for nex,mon in graph[start]:
        if mon<=won and not visited[nex]:
            arr.append(mon)
            visited[nex] = True
            dfs(nex,arr,won-mon,visited)
            visited[nex] = False
            arr.pop()


n,m,a,b,c = map(int,input().split())
h = []
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[a] = True
candi = []
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

dfs(a,h,c,visited)

print(sorted(candi)[0] if candi else -1)