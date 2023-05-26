# 파이똥 억까 멈춰
from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n,m,k = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(n)]
queue = deque()
queue.append((0,0,1,0)) # y,x,dist,cnt
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = True
while queue:
    y,x,dist,cnt = queue.popleft()
    if y == n-1 and x == m-1:
        print(dist)
        exit()
    for dy,dx in d:
        ny,nx = dy+y, dx+x
        if ny<0 or nx<0 or ny>=n or nx>=m: continue

        if board[ny][nx] == '0' and not visited[cnt][ny][nx]:
            queue.append((ny,nx,dist+1,cnt))
            visited[cnt][ny][nx] = True
        elif board[ny][nx] == '1' and cnt < k and not visited[cnt+1][ny][nx]:
            if dist%2 == 1: # 현재 낮
                queue.append((ny,nx,dist+1,cnt+1))
                visited[cnt+1][ny][nx] = True
            else:
                queue.append((y,x,dist+1,cnt))
print(-1)