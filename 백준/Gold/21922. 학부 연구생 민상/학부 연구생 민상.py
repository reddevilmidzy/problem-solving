import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = set()
def boundry(y: int, x: int) -> bool:
    return 0 <= y < n and 0 <= x < m

def dfs(y: int, x: int, d: int):
    
    while boundry(y, x):
        ans.add((y,x))
        if tmp[d][y][x]:
            break
        tmp[d][y][x] = True

        if graph[y][x] == 1:
            if d == 2:
                d = 3
            elif d == 3:
                d = 2
        elif graph[y][x] == 2:
            if d == 1:
                d = 0
            elif d == 0:
                d = 1
        elif graph[y][x] == 3:
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        elif graph[y][x] == 4:
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            elif d == 3:
                d = 1   
        x += dx[d]
        y += dy[d]        

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
tmp = [[[False]*m for _ in range(n)] for __ in range(4)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 9: # 에어콘
            dfs(i,j,0)
            dfs(i,j,1)
            dfs(i,j,2)
            dfs(i,j,3)
print(len(ans))