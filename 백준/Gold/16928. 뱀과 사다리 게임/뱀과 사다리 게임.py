import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        x =  queue.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx < 101:
                move = graph[nx]
                if visited[move] == 0:
                    queue.append(move)
                    visited[move] = visited[x] + 1
                    if move == 100:
                        return

n,m = map(int,input().rstrip().split())
graph = [j for j in range(101)]
visited = [0 for k in range(101)]

for i in range(n+m):
    x,y = map(int,input().rstrip().split())
    graph[x] = y

bfs()
print(visited[100]-1)