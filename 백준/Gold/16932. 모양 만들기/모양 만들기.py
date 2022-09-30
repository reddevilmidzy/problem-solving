from collections import deque
import sys
input= sys.stdin.readline


dx = [1,0,-1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]

dic = dict()
# 1갯수 각각 도형에 카운트
# 마지막에는 0만 찾아 다니면서 상하좌우 1의 조각 갯수 더함

def bfs(a: int,b: int,c: int,pos: int)-> int:
    queue = deque()
    queue.append([a,b,c])
    visited[a][b] = pos
    cnt_tmp = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                cnt_tmp += 1
                queue.append([nx,ny,cnt+1])
                visited[nx][ny] = pos
    return cnt_tmp
idx = 1
stk = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            tmp = bfs(i,j,1,idx)
            dic[idx] = tmp
            idx += 1
        elif graph[i][j] == 0:
            stk.append([i,j])
really = []
for i,j in stk:
    four = 0
    pre = []
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        level = visited[nx][ny]
        if level!=0 and level not in pre:
            four += dic[level]
            pre.append(level)
        #print('four', four)
    really.append(four)
# print(dic)
print(max(really)+1)