import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
do = []
cnt = 0
res = [0]

for i in range(n):
    do.append(list(map(int,input().rstrip().split())))

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append([x,y])
    do[x][y] = 0
    are = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and do[nx][ny] == 1:
                are += 1
                do[nx][ny] = 0
                queue.append([nx, ny])
    res.append(are)

for x in range(n):
    for y in range(m):
        if do[x][y] == 1:
            are = 1
            bfs(x,y)
            cnt += 1

print(cnt)
print(max(res))