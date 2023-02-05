import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(start:int, idx:int, cnt:int) -> None:
    if start == idx and cnt >= 2:
        global cycle
        cycle = True
        return
    
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]: # 아직 방문하지 않은 역은 방문
            dfs(start, i, cnt + 1)
            
        elif i == start and cnt >= 2: # 두번 째 방문했고, 시작역이라면
            dfs(start, i, cnt)
        


def bfs():
    queue = deque()
    visited = [-1]*(n+1)

    # 순환역 속하는 역 0으로 설정
    for i in range(1,n+1):
        if stations[i]:
            visited[i] = 0
            queue.append(i)
    
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + 1

    return visited[1:]

n = int(input())
graph = [[] for _ in range(n+1)]
stations = [False]*(n+1)

for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for x in range(1,n+1):
    visited = [False] * (n+1)
    cycle =  False
    dfs(x,x,0)
    if cycle:
        stations[x] = True

print(*bfs(), sep=' ')