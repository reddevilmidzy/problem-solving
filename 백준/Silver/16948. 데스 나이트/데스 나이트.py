from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(a:int,b:int)-> int:
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append([a,b])
    visited[a][b] = 0
    while queue:
        r,c = queue.popleft()
        
        for i in range(6):
            nx = r+dx[i]
            ny = c+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == -1:
                queue.append([nx,ny])
                visited[nx][ny] = visited[r][c] + 1
    return visited[r2][c2]

n =int(input())
r1,c1,r2,c2 = map(int,input().split())

print(bfs(r1,c1))