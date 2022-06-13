import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
max_num = 0

for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    max_num = max(max_num, max(graph[i]))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b,value, visited):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1< nx < n and -1 < ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

res = 0
for i in range(max_num):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i,visited)
                cnt += 1

    if res < cnt:
        res = cnt
print(res)