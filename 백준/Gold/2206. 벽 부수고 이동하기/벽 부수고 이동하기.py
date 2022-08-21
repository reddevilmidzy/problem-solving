import collections
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    queue = deque()
    visited = [[False for _ in range(m+1)] for __ in range(n+1)]
    visited[1][1] = True
    visited_forbreak = [[False for _ in range(m+1)] for __ in range(n+1)]
    visited_forbreak[1][1] = True
    queue.append([1,1,False,1])
    while queue:
        x,y,b,cnt = queue.popleft()
        # print('x',x,'y',y,'b',b)
        if x == n and y == m:
            return cnt
        if not b:
            # print(111)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 1 or ny < 1 or nx > n or ny > m:
                    continue
                
                if not visited[nx][ny]:
                    if graph[nx-1][ny-1]:
                        queue.append([nx,ny,True,cnt+1])
                    else:
                        queue.append([nx,ny,b,cnt+1])
                    visited[nx][ny] = True

        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 1 or ny < 1 or nx > n or ny > m:
                    continue
                if graph[nx-1][ny-1]==0 and not visited_forbreak[nx][ny]:
                    queue.append([nx,ny,b,cnt+1])
                    visited_forbreak[nx][ny] = True

    return -1

print(bfs())