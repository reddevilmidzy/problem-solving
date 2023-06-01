from itertools import combinations
import sys
input = sys.stdin.readline

dx = (1,0,-1,0)
dy = (0,1,0,-1)
INF = int(1e9)

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= n

def position(val: tuple[int]) -> list[int]:
    return [(num//n, num%n) for num in val]

def cal(val: list[list[int]]):
    res = set()
    tmp = 0
    for y,x in val:
        tmp += board[y][x]
        res.add((y,x))
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if out_of_range(ny,nx): return INF
            res.add((ny,nx))
            tmp += board[ny][nx]

    return tmp if len(res) == 15 else INF

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
ans = []

for val in combinations(range(n**2), 3):
    ans.append(cal(position(val)))
    
print(min(ans))