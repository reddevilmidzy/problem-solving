from itertools import combinations
import sys
input = sys.stdin.readline

d = [(0,1), (1,0), (-1,0), (0,-1)]

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= m

def check(s: tuple[int]):
    res = 0
    visited = [[False]*m for _ in range(n)]
    for i in s:
        y,x = i//m, i%m
        res += board[y][x]
        visited[y][x] = True
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if not out_of_range(ny,nx) and visited[ny][nx]:
                return -int(1e9)
    return res

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ans = []
for i in combinations(range(n*m), k):
    ans.append(check(i))

print(max(ans))