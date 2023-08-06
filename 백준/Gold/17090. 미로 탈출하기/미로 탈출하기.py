import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y,x):
    if visited[y][x] != -1: return visited[y][x]
    
    # 방문
    visited[y][x] = 0

    dy,dx = d[board[y][x]]
    ny,nx = dy+y,dx+x
    # 범위 밖 탈출 성공
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        visited[y][x] = 1
    else:
        visited[y][x] = max(visited[y][x], dfs(ny,nx))
    return visited[y][x]

n,m = map(int,input().split())
board = [input().rstrip() for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
d = {"U":(-1,0), "R":(0,1), "D":(1,0), "L":(0,-1)}

for y in range(n):
    for x in range(m):
        dfs(y,x)

print(sum(map(sum, visited)))