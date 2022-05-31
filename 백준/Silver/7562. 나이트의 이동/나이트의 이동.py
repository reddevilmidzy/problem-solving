import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs():
    queue= deque()
    queue.append((x1, y1, 0))
    pan[x1][y1] = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx and nx < l and -1 < ny and ny < l:
                if pan[nx][ny] == 0:
                    pan[nx][ny] = 1
                    queue.append((nx, ny, cnt+1))
            if nx == x2 and ny == y2:
                return cnt + 1
                
for i in range(int(input())):
    l = int(input().rstrip())
    pan = [[0 for i in range(l)] for j in range(l)]
    x1,y1 = map(int, input().rstrip().split())
    x2,y2 = map(int, input().rstrip().split())
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        print(bfs())